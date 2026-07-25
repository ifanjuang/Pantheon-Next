#!/usr/bin/env python3
"""CLI bridge used by the Hermes ``pantheon-document-intake`` skill.

The script is intentionally transport-only. It contains no Pantheon policy,
Paperless credential or project classification logic. The server-side gateway
holds the Paperless token and the Pantheon PEP/PDP seam.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


class ClientError(RuntimeError):
    pass


def _load_json(path: str) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ClientError(f"cannot read JSON file {path!r}: {exc}") from exc
    if not isinstance(value, dict):
        raise ClientError(f"JSON file {path!r} must contain an object")
    return value


def _load_text(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise ClientError(f"cannot read text file {path!r}: {exc}") from exc


class GatewayClient:
    def __init__(self) -> None:
        self.base_url = os.environ.get(
            "PANTHEON_PAPERLESS_GATEWAY_URL", "http://paperless-gateway:8082"
        ).rstrip("/")
        if not self.base_url.startswith(("http://", "https://")):
            raise ClientError("PANTHEON_PAPERLESS_GATEWAY_URL must use http:// or https://")
        self.api_key = os.environ.get("MVP_HERMES_API_KEY", "").strip()
        if not self.api_key:
            raise ClientError("MVP_HERMES_API_KEY is required in the Hermes runtime environment")
        try:
            self.timeout = float(os.environ.get("PANTHEON_PAPERLESS_GATEWAY_TIMEOUT", "30"))
        except ValueError as exc:
            raise ClientError("PANTHEON_PAPERLESS_GATEWAY_TIMEOUT must be numeric") from exc

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        url = self.base_url + path
        if params:
            filtered = {k: v for k, v in params.items() if v not in (None, "")}
            if filtered:
                url += "?" + urlencode(filtered)
        data = None
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        if body is not None:
            data = json.dumps(body, separators=(",", ":")).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = Request(url, data=data, headers=headers, method=method)
        try:
            with urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
        except HTTPError as exc:
            try:
                detail = exc.read().decode("utf-8")
            except Exception:
                detail = ""
            raise ClientError(f"gateway returned HTTP {exc.code}: {detail[:1000]}") from exc
        except (URLError, TimeoutError, OSError) as exc:
            raise ClientError(f"gateway unavailable: {exc}") from exc
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ClientError("gateway returned invalid JSON") from exc
        if not isinstance(payload, dict):
            raise ClientError("gateway response must be a JSON object")
        return payload


def _print(value: dict[str, Any]) -> None:
    json.dump(value, sys.stdout, ensure_ascii=False, indent=2, sort_keys=False)
    sys.stdout.write("\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pantheon-document-intake",
        description="Bounded Hermes client for Paperless-backed Pantheon document intake.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="read-only Paperless source search")
    p_search.add_argument("--query", default="")
    p_search.add_argument("--page", type=int, default=1)
    p_search.add_argument("--page-size", type=int, default=20)

    p_inspect = sub.add_parser("inspect", help="read-only Paperless document metadata")
    p_inspect.add_argument("--document-id", type=int, required=True)
    p_inspect.add_argument("--version-id")

    p_capture = sub.add_parser(
        "capture", help="inspect one exact immutable Source Capture candidate"
    )
    p_capture.add_argument("--document-id", type=int, required=True)
    p_capture.add_argument("--version-id", required=True)

    p_task = sub.add_parser("task", help="observe one Paperless native task")
    p_task.add_argument("--task-id", required=True)

    p_intake = sub.add_parser(
        "intake",
        help="governed exact-version intake into the existing Project Document pipeline",
    )
    p_intake.add_argument("--document-id", type=int, required=True)
    p_intake.add_argument("--version-id", required=True)
    p_intake.add_argument("--contract", required=True, help="Task Contract YAML file")
    p_intake.add_argument(
        "--decision", required=True, help="human decision reference JSON file"
    )
    p_intake.add_argument("--ingestion-id")

    p_metadata = sub.add_parser(
        "update-metadata",
        help="governed Paperless operational metadata mirror update",
    )
    p_metadata.add_argument("--document-id", type=int, required=True)
    p_metadata.add_argument("--version-id", required=True)
    p_metadata.add_argument("--contract", required=True, help="Task Contract YAML file")
    p_metadata.add_argument(
        "--changes", required=True, help="JSON object with allowlisted changes"
    )
    p_metadata.add_argument(
        "--decision", required=True, help="human decision reference JSON file"
    )
    p_metadata.add_argument(
        "--classification-candidate",
        help="optional JSON candidate retained as non-authoritative trace context",
    )

    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        client = GatewayClient()
        if args.command == "search":
            if args.page < 1 or not 1 <= args.page_size <= 100:
                raise ClientError("page must be >= 1 and page-size must be 1..100")
            result = client.request(
                "GET",
                "/v1/paperless/documents",
                params={"query": args.query, "page": args.page, "page_size": args.page_size},
            )
        elif args.command == "inspect":
            result = client.request(
                "GET",
                f"/v1/paperless/documents/{quote(str(args.document_id), safe='')}",
                params={"version_id": args.version_id},
            )
        elif args.command == "capture":
            result = client.request(
                "GET",
                f"/v1/paperless/documents/{quote(str(args.document_id), safe='')}/capture",
                params={"version_id": args.version_id},
            )
        elif args.command == "task":
            result = client.request(
                "GET", f"/v1/paperless/tasks/{quote(args.task_id, safe='')}"
            )
        elif args.command == "intake":
            result = client.request(
                "POST",
                "/v1/paperless/intakes",
                body={
                    "paperless_document_id": args.document_id,
                    "paperless_version_id": args.version_id,
                    "task_contract_yaml": _load_text(args.contract),
                    "decision_payload": _load_json(args.decision),
                    "ingestion_id": args.ingestion_id,
                },
            )
        elif args.command == "update-metadata":
            body: dict[str, Any] = {
                "changes": _load_json(args.changes),
                "paperless_version_id": args.version_id,
                "task_contract_yaml": _load_text(args.contract),
                "decision_payload": _load_json(args.decision),
            }
            if args.classification_candidate:
                body["classification_candidate"] = _load_json(
                    args.classification_candidate
                )
            result = client.request(
                "POST",
                f"/v1/paperless/documents/{quote(str(args.document_id), safe='')}/metadata",
                body=body,
            )
        else:  # pragma: no cover - argparse enforces this
            raise ClientError(f"unsupported command: {args.command}")
        _print(result)
        return 0
    except ClientError as exc:
        print(f"pantheon-document-intake: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
