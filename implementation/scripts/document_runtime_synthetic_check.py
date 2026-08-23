#!/usr/bin/env python3
"""Operator-run synthetic verification for the document runtime vertical.

Default mode is read-only. The optional intake mode is deliberately restricted to
an explicitly synthetic Task Contract and uses the installed Hermes skill's
transport script. The operator helper may sign a synthetic human decision and
verify its issuer against the Pantheon PDP, but those secrets are stripped from
the skill subprocess environment.

It never uploads/deletes Paperless sources, publishes Knowledge, admits Evidence,
mutates Paperless metadata or changes activation state.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from mvp_vertical.decision_signing import signed_decision_payload


class CheckError(RuntimeError):
    pass


_SKILL_STRIPPED_ENV = frozenset(
    {
        "PAPERLESS_API_TOKEN",
        "PANTHEON_POLICY_API_KEY",
        "PANTHEON_DECISION_ISSUER_KEYS_PATH",
        "PANTHEON_DECISION_ISSUER_SIGNING_SECRET",
    }
)


def _json_request(
    method: str,
    url: str,
    *,
    bearer: str,
    body: dict[str, Any] | None = None,
    timeout: float = 20.0,
) -> dict[str, Any]:
    data = None
    headers = {"Accept": "application/json", "Authorization": f"Bearer {bearer}"}
    if body is not None:
        data = json.dumps(body, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:1000]
        raise CheckError(f"HTTP {exc.code} from {url}: {detail}") from exc
    except (URLError, TimeoutError, OSError) as exc:
        raise CheckError(f"unreachable {url}: {exc}") from exc
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise CheckError(f"invalid JSON from {url}") from exc
    if not isinstance(value, dict):
        raise CheckError(f"expected JSON object from {url}")
    return value


def _load_json_object(path: str | Path) -> dict[str, Any]:
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CheckError(f"cannot read JSON object {str(path)!r}: {exc}") from exc
    if not isinstance(value, dict):
        raise CheckError(f"JSON file {str(path)!r} must contain an object")
    return value


def _index_observations(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        item["source"]: item
        for item in payload.get("observations", [])
        if isinstance(item, dict) and isinstance(item.get("source"), str)
    }


def assess_observations(payload: dict[str, Any]) -> dict[str, Any]:
    observed = _index_observations(payload)
    checks = {
        "paperless_source_path": (
            observed.get("paperless_gateway", {}).get("paperless_reachability_status")
            == "reachable"
        ),
        "pantheon_pdp_ready": (
            observed.get("pantheon_pdp", {}).get("readiness_status") == "ready_observed"
        ),
        "docling_health_endpoint": (
            observed.get("docling_serve", {}).get("reachability_status") == "reachable"
        ),
        "hermes_skill_installed": (
            observed.get("hermes_native_inventory", {}).get("installation_status")
            == "installed_observed"
        ),
    }
    return {
        "checks": checks,
        "candidate_ready_for_synthetic_intake": all(checks.values()),
        "meaning": "transport_and_runtime_prerequisites_only",
        "safety_status": "not_inferred",
        "production_authorization": False,
    }


def _skill_root(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    hermes_home = Path(os.environ.get("HERMES_HOME", "~/.hermes")).expanduser()
    return (hermes_home / "skills" / "pantheon-document-intake").resolve()


def _skill_subprocess_env(source: dict[str, str] | None = None) -> dict[str, str]:
    env = dict(os.environ if source is None else source)
    for name in _SKILL_STRIPPED_ENV:
        env.pop(name, None)
    return env


def _run_skill_json(
    skill_root: Path,
    args: list[str],
    *,
    timeout: float = 120.0,
    runner=subprocess.run,
    env_source: dict[str, str] | None = None,
) -> dict[str, Any]:
    script = skill_root / "scripts" / "pantheon_document_intake.py"
    if not script.is_file():
        raise CheckError(f"installed skill transport script not found: {script}")
    try:
        completed = runner(
            [sys.executable, str(script), *args],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            env=_skill_subprocess_env(env_source),
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise CheckError(f"cannot execute installed skill transport: {exc}") from exc
    if int(completed.returncode) != 0:
        raise CheckError(
            "installed skill transport failed: "
            + (completed.stderr or completed.stdout or "no diagnostic")[:2000]
        )
    try:
        value = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CheckError("installed skill transport returned invalid JSON") from exc
    if not isinstance(value, dict):
        raise CheckError("installed skill transport must return a JSON object")
    return value


def _assert_synthetic_contract(contract_path: Path, source_ref: str) -> str:
    try:
        text = contract_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CheckError(f"cannot read Task Contract: {exc}") from exc
    lowered = text.lower()
    if "synthetic" not in lowered:
        raise CheckError(
            "refusing intake: Task Contract must be explicitly synthetic (contain 'synthetic')"
        )
    if source_ref not in text:
        raise CheckError(
            "refusing intake: exact Paperless source_ref is not present in the synthetic Task Contract"
        )
    return text


def _prepare_decision_payload(
    decision_path: Path,
    *,
    signing_secret: str | None,
) -> tuple[dict[str, Any], bool]:
    payload = _load_json_object(decision_path)
    if signing_secret:
        try:
            return signed_decision_payload(payload, signing_secret), True
        except ValueError as exc:
            raise CheckError(f"cannot sign synthetic decision: {exc}") from exc
    return payload, False


def _write_temporary_decision(payload: dict[str, Any]) -> Path:
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        encoding="utf-8",
        delete=False,
    )
    try:
        json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"))
        handle.write("\n")
        return Path(handle.name)
    finally:
        handle.close()


def _issuer_validation_projection(value: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value.get(key)
        for key in (
            "verdict",
            "issuer_authenticated",
            "checks",
            "findings",
            "gate_signal_validation_performed",
        )
        if key in value
    }


def _validate_issuer_proof(
    *,
    policy_url: str,
    policy_api_key: str,
    decision_payload: dict[str, Any],
    expectation: dict[str, Any],
) -> dict[str, Any]:
    if not policy_url.strip() or not policy_api_key.strip():
        raise CheckError(
            "PANTHEON_POLICY_API_URL and PANTHEON_POLICY_API_KEY are required for issuer proof"
        )
    decision = decision_payload.get("decision")
    if not isinstance(decision, dict):
        raise CheckError("synthetic decision payload has no decision mapping")
    result = _json_request(
        "POST",
        policy_url.rstrip("/") + "/v1/policy/decisions:validate",
        bearer=policy_api_key,
        body={"decision": decision, "expectation": expectation},
    )
    return _issuer_validation_projection(result)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Observe the document runtime stack and optionally verify one synthetic intake."
    )
    parser.add_argument(
        "--observer-url",
        default=os.environ.get(
            "PANTHEON_DOCUMENT_RUNTIME_OBSERVER_URL", "http://document-runtime-observer:8083"
        ),
    )
    parser.add_argument(
        "--cockpit-key",
        default=os.environ.get("MVP_COCKPIT_API_KEY", ""),
        help="Prefer MVP_COCKPIT_API_KEY environment variable; do not put secrets in shell history.",
    )
    parser.add_argument("--run-intake", action="store_true")
    parser.add_argument("--require-issuer-auth", action="store_true")
    parser.add_argument("--ack", default="")
    parser.add_argument("--skill-root")
    parser.add_argument("--document-id", type=int)
    parser.add_argument("--version-id")
    parser.add_argument("--contract")
    parser.add_argument("--decision")
    parser.add_argument("--ingestion-id", default="synthetic-document-runtime-check")
    parser.add_argument(
        "--policy-url",
        default=os.environ.get("PANTHEON_POLICY_API_URL", "http://pantheon-policy-api:8000"),
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if not args.cockpit_key:
            raise CheckError("MVP_COCKPIT_API_KEY is required for the read-only observer")
        observer_url = args.observer_url.rstrip("/")
        observations = _json_request(
            "GET",
            f"{observer_url}/v1/document-runtime/observations",
            bearer=args.cockpit_key,
        )
        assessment = assess_observations(observations)
        receipt: dict[str, Any] = {
            "object_type": "synthetic_document_runtime_check_receipt",
            "synthetic": True,
            "observations": observations,
            "assessment": assessment,
            "intake_attempted": False,
            "technical_receipt_is_evidence": False,
            "human_issuer_authentication_status": "not_attempted",
            "human_issuer_authentication_proven": False,
            "activation_changed": False,
            "production_authorization": False,
        }
        issuer_requirement_failed = False

        if args.run_intake:
            if args.ack != "SYNTHETIC_ONLY":
                raise CheckError("--run-intake requires --ack SYNTHETIC_ONLY")
            if not assessment["candidate_ready_for_synthetic_intake"]:
                raise CheckError("runtime observations are not ready for a synthetic intake attempt")
            missing = [
                name
                for name, value in (
                    ("--document-id", args.document_id),
                    ("--version-id", args.version_id),
                    ("--contract", args.contract),
                    ("--decision", args.decision),
                )
                if value in (None, "")
            ]
            if missing:
                raise CheckError("missing synthetic intake arguments: " + ", ".join(missing))
            if not os.environ.get("MVP_HERMES_API_KEY", "").strip():
                raise CheckError("MVP_HERMES_API_KEY must be present in the operator environment")

            root = _skill_root(args.skill_root)
            capture = _run_skill_json(
                root,
                [
                    "capture",
                    "--document-id",
                    str(args.document_id),
                    "--version-id",
                    str(args.version_id),
                ],
            )
            source_ref = str(capture.get("source_ref") or "")
            if not source_ref:
                raise CheckError("exact capture returned no source_ref")
            _assert_synthetic_contract(Path(args.contract), source_ref)

            signing_secret = os.environ.get(
                "PANTHEON_DECISION_ISSUER_SIGNING_SECRET", ""
            ).strip()
            if args.require_issuer_auth and not signing_secret:
                raise CheckError(
                    "--require-issuer-auth requires PANTHEON_DECISION_ISSUER_SIGNING_SECRET"
                )
            decision_payload, signed = _prepare_decision_payload(
                Path(args.decision), signing_secret=signing_secret or None
            )
            decision_path = _write_temporary_decision(decision_payload)
            try:
                intake_args = [
                    "intake",
                    "--document-id",
                    str(args.document_id),
                    "--version-id",
                    str(args.version_id),
                    "--contract",
                    str(Path(args.contract)),
                    "--decision",
                    str(decision_path),
                    "--ingestion-id",
                    str(args.ingestion_id),
                ]
                result = _run_skill_json(root, intake_args)
            finally:
                decision_path.unlink(missing_ok=True)

            receipt.update(
                {
                    "intake_attempted": True,
                    "decision_signed_by_operator_helper": signed,
                    "source_capture": {
                        key: capture.get(key)
                        for key in (
                            "document_id",
                            "version_id",
                            "original_filename",
                            "content_hash",
                            "storage_reference",
                            "source_ref",
                        )
                    },
                    "intake_result": result,
                    "knowledge_published": bool(result.get("knowledge_published", False)),
                    "evidence_admitted": bool(result.get("evidence_admitted", False)),
                    "agent_skill_selection_proven": False,
                }
            )

            expectation = result.get("decision_expectation")
            policy_key = os.environ.get("PANTHEON_POLICY_API_KEY", "").strip()
            if signed and isinstance(expectation, dict) and policy_key:
                validation = _validate_issuer_proof(
                    policy_url=args.policy_url,
                    policy_api_key=policy_key,
                    decision_payload=decision_payload,
                    expectation=expectation,
                )
                proven = bool(
                    validation.get("verdict") == "valid"
                    and validation.get("issuer_authenticated") is True
                )
                receipt["issuer_validation"] = validation
                receipt["human_issuer_authentication_proven"] = proven
                receipt["human_issuer_authentication_status"] = (
                    "proven" if proven else "not_proven"
                )
            elif signed:
                receipt["human_issuer_authentication_status"] = "not_observed"

            if args.require_issuer_auth and not receipt["human_issuer_authentication_proven"]:
                issuer_requirement_failed = True

        json.dump(receipt, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        if args.run_intake:
            if issuer_requirement_failed:
                return 5
            return 0 if receipt.get("intake_result", {}).get("status") == "applied" else 4
        return 0 if assessment["candidate_ready_for_synthetic_intake"] else 3
    except CheckError as exc:
        print(f"document-runtime-synthetic-check: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
