#!/usr/bin/env python3
"""Bounded AFFAIRES -> Hindsight producer used by the Workspace daemon.

The professional source stays on the mounted filesystem. This module only reads an
explicitly projected source file, uploads transient request bytes to Hindsight, and
persists reconstructible/technical synchronization state in SQLite.

It deliberately does not delete Hindsight documents when a source disappears. Hindsight
0.10.1 can retain derived observations beyond a document lifecycle, so destructive
reconciliation remains a separate qualification.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
import mimetypes
from pathlib import Path
import re
import sqlite3
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlparse
from urllib.request import Request, urlopen
import uuid


ACTIVE_STATUSES = {"SUBMITTED", "PENDING", "PROCESSING"}
TERMINAL_STATUSES = {"COMPLETED", "FAILED", "CANCELLED"}
SYNC_TABLE = "hindsight_sync"
TAG_SAFE_RE = re.compile(r"[^a-z0-9._-]+")


def _utc_now() -> str:
    return datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _tag_value(value: str) -> str:
    normalized = TAG_SAFE_RE.sub("-", value.strip().casefold()).strip("-")
    return normalized[:96]


def _metadata_value(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        return value or None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    return None


@dataclass(frozen=True)
class ProducerCandidate:
    workspace: str
    document_id: str
    hindsight_document_id: str
    source_path: Path
    relative_path: str
    source_sha256: str
    fingerprint: str
    context: str
    tags: list[str]
    metadata: dict[str, str]


class HindsightHTTPClient:
    """Small Hindsight 0.10.1 HTTP adapter with no third-party dependency."""

    def __init__(
        self,
        base_url: str,
        bank_id: str,
        *,
        authorization: str = "",
        timeout_seconds: float = 30.0,
        parser: str = "markitdown",
        max_file_bytes: int = 100 * 1024 * 1024,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.bank_id = bank_id
        self.authorization = authorization.strip()
        self.timeout_seconds = float(timeout_seconds)
        self.parser = parser.strip() or "markitdown"
        self.max_file_bytes = max(1, int(max_file_bytes))
        parsed = urlparse(self.base_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("Hindsight URL must be an absolute HTTP(S) URL")

    def _headers(self) -> dict[str, str]:
        headers = {"Accept": "application/json", "User-Agent": "pantheon-workspace-producer/1"}
        if self.authorization:
            headers["Authorization"] = self.authorization
        return headers

    def _json_response(self, request: Request) -> dict[str, Any]:
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                body = response.read()
        except HTTPError as exc:
            detail = exc.read(4096).decode("utf-8", errors="replace")
            raise RuntimeError(f"Hindsight HTTP {exc.code}: {detail}") from exc
        except (OSError, URLError) as exc:
            raise RuntimeError(f"Hindsight unavailable: {exc}") from exc
        try:
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise RuntimeError("Hindsight returned invalid JSON") from exc
        if not isinstance(payload, dict):
            raise RuntimeError("Hindsight returned an unexpected response")
        return payload

    def retain_file(
        self,
        source: Path,
        *,
        document_id: str,
        context: str,
        tags: list[str],
        metadata: dict[str, str],
    ) -> str:
        boundary = f"----pantheon-{uuid.uuid4().hex}"
        request_payload = json.dumps(
            {
                "parser": self.parser,
                "files_metadata": [
                    {
                        "context": context,
                        "document_id": document_id,
                        "tags": tags,
                        "metadata": metadata,
                        "timestamp": "unset",
                    }
                ],
            },
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
        try:
            file_size = source.stat().st_size
        except OSError as exc:
            raise RuntimeError(f"Source unavailable before Hindsight upload: {exc}") from exc
        if file_size > self.max_file_bytes:
            raise RuntimeError(
                f"Source exceeds Hindsight upload bound: {file_size} > {self.max_file_bytes} bytes"
            )
        file_bytes = source.read_bytes()
        content_type = mimetypes.guess_type(source.name)[0] or "application/octet-stream"

        parts = [
            f"--{boundary}\r\n".encode(),
            b'Content-Disposition: form-data; name="request"\r\n',
            b"Content-Type: application/json; charset=utf-8\r\n\r\n",
            request_payload,
            b"\r\n",
            f"--{boundary}\r\n".encode(),
            (
                f'Content-Disposition: form-data; name="files"; filename="{source.name}"\r\n'
            ).encode("utf-8"),
            f"Content-Type: {content_type}\r\n\r\n".encode(),
            file_bytes,
            b"\r\n",
            f"--{boundary}--\r\n".encode(),
        ]
        body = b"".join(parts)
        path = (
            f"/v1/default/banks/{quote(self.bank_id, safe='')}/files/retain"
        )
        headers = self._headers()
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
        request = Request(f"{self.base_url}{path}", data=body, headers=headers, method="POST")
        payload = self._json_response(request)
        operation_ids = payload.get("operation_ids")
        if (
            not isinstance(operation_ids, list)
            or len(operation_ids) != 1
            or not isinstance(operation_ids[0], str)
            or not operation_ids[0]
        ):
            raise RuntimeError("Hindsight file retain returned no unique operation_id")
        return operation_ids[0]

    def operation_status(self, operation_id: str) -> dict[str, Any]:
        path = (
            f"/v1/default/banks/{quote(self.bank_id, safe='')}/operations/"
            f"{quote(operation_id, safe='')}"
        )
        request = Request(f"{self.base_url}{path}", headers=self._headers(), method="GET")
        payload = self._json_response(request)
        status = payload.get("status")
        if status not in {"pending", "processing", "completed", "failed", "cancelled"}:
            raise RuntimeError(f"Unexpected Hindsight operation status: {status!r}")
        return payload

    def get_document(self, document_id: str) -> dict[str, Any]:
        """Read one exact retained document. This method performs no mutation."""
        path = (
            f"/v1/default/banks/{quote(self.bank_id, safe='')}/documents/"
            f"{quote(document_id, safe='')}"
        )
        request = Request(f"{self.base_url}{path}", headers=self._headers(), method="GET")
        return self._json_response(request)

    def list_document_chunks(
        self,
        document_id: str,
        *,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Read chunks for one exact retained document, never a bank-wide search."""
        query = urlencode({"limit": max(1, min(int(limit), 100)), "offset": max(0, int(offset))})
        path = (
            f"/v1/default/banks/{quote(self.bank_id, safe='')}/documents/"
            f"{quote(document_id, safe='')}/chunks?{query}"
        )
        request = Request(f"{self.base_url}{path}", headers=self._headers(), method="GET")
        return self._json_response(request)

    def list_memories(
        self,
        document_id: str,
        *,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        """Read memory units linked by Hindsight to one exact source document."""
        query = urlencode(
            {
                "document_id": document_id,
                "limit": max(1, min(int(limit), 100)),
                "offset": max(0, int(offset)),
            }
        )
        path = (
            f"/v1/default/banks/{quote(self.bank_id, safe='')}/memories/list?{query}"
        )
        request = Request(f"{self.base_url}{path}", headers=self._headers(), method="GET")
        return self._json_response(request)


class HindsightProducer:
    """One bounded producer owned by the Workspace daemon."""

    def __init__(
        self,
        *,
        roots: list[tuple[str, Path]],
        state_db: Path,
        client: HindsightHTTPClient,
        max_submits_per_reconcile: int = 4,
    ) -> None:
        self.roots = {name: root for name, root in roots}
        self.state_db = state_db
        self.client = client
        self.max_submits_per_reconcile = max(1, int(max_submits_per_reconcile))
        self._last_summary: dict[str, Any] = {
            "enabled": True,
            "bank_id": client.bank_id,
            "mode": "source-only",
            "delete_missing": False,
            "submitted": 0,
            "completed": 0,
            "pending": 0,
            "failed": 0,
            "blocked": 0,
            "stale": 0,
            "queued": 0,
            "last_error": None,
        }
        self._ensure_schema()

    def _connect(self) -> sqlite3.Connection:
        self.state_db.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.state_db, timeout=5)
        connection.row_factory = sqlite3.Row
        return connection

    def _ensure_schema(self) -> None:
        connection = self._connect()
        try:
            connection.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {SYNC_TABLE} (
                    hindsight_document_id TEXT PRIMARY KEY,
                    document_id TEXT NOT NULL,
                    workspace TEXT NOT NULL,
                    source_path TEXT NOT NULL,
                    source_sha256 TEXT NOT NULL,
                    fingerprint TEXT NOT NULL,
                    operation_id TEXT,
                    status TEXT NOT NULL,
                    last_error TEXT,
                    updated_at TEXT NOT NULL
                )
                """
            )
            connection.commit()
        finally:
            connection.close()

    def _states(self) -> dict[str, dict[str, Any]]:
        connection = self._connect()
        try:
            rows = connection.execute(f"SELECT * FROM {SYNC_TABLE}").fetchall()
            return {row["hindsight_document_id"]: dict(row) for row in rows}
        finally:
            connection.close()

    def _save(
        self,
        candidate: ProducerCandidate | None,
        *,
        hindsight_document_id: str,
        document_id: str,
        workspace: str,
        source_path: str,
        source_sha256: str,
        fingerprint: str,
        operation_id: str | None,
        status: str,
        last_error: str | None = None,
    ) -> None:
        connection = self._connect()
        try:
            with connection:
                connection.execute(
                    f"""
                    INSERT INTO {SYNC_TABLE}(
                        hindsight_document_id, document_id, workspace, source_path,
                        source_sha256, fingerprint, operation_id, status, last_error, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(hindsight_document_id) DO UPDATE SET
                        document_id=excluded.document_id,
                        workspace=excluded.workspace,
                        source_path=excluded.source_path,
                        source_sha256=excluded.source_sha256,
                        fingerprint=excluded.fingerprint,
                        operation_id=excluded.operation_id,
                        status=excluded.status,
                        last_error=excluded.last_error,
                        updated_at=excluded.updated_at
                    """,
                    (
                        hindsight_document_id,
                        document_id,
                        workspace,
                        source_path,
                        source_sha256,
                        fingerprint,
                        operation_id,
                        status,
                        last_error,
                        _utc_now(),
                    ),
                )
        finally:
            connection.close()

    def _candidate(self, card: dict[str, Any]) -> ProducerCandidate | None:
        if card.get("kind") != "document":
            return None
        if card.get("status") != "COMPLETE":
            return None
        if card.get("hindsight_eligible") is not True:
            return None
        # Slice A is intentionally source-only. EML/cartouche-derived candidates remain deferred.
        if card.get("hindsight_representation_candidate") != "source":
            return None

        workspace = card.get("workspace")
        document_id = card.get("document_id")
        relative_path = card.get("path")
        if not isinstance(workspace, str) or workspace not in self.roots:
            return None
        if not isinstance(document_id, str) or not document_id.strip():
            return None
        if not isinstance(relative_path, str) or not relative_path:
            return None

        root = self.roots[workspace]
        source = root / relative_path
        try:
            root_resolved = root.resolve(strict=True)
            source_resolved = source.resolve(strict=True)
            source_resolved.relative_to(root_resolved)
            if not source.is_file() or source.is_symlink():
                return None
        except (OSError, RuntimeError, ValueError):
            return None

        declared_sha = card.get("source_sha256")
        if card.get("source_sha256_verified") is True and isinstance(declared_sha, str):
            source_sha256 = declared_sha
        else:
            source_sha256 = _sha256(source)

        metadata: dict[str, str] = {
            "pantheon_document_id": document_id,
            "workspace": workspace,
            "source_path": relative_path,
            "source_sha256": source_sha256,
        }
        for target_key, card_key in (
            ("title", "title"),
            ("project_hint", "project"),
            ("phase_hint", "phase"),
            ("document_type", "document_type"),
            ("issuer", "issuer"),
        ):
            value = _metadata_value(card.get(card_key))
            if value is not None:
                metadata[target_key] = value

        context_parts = ["AFFAIRES professional source document"]
        if metadata.get("title"):
            context_parts.append(f"title={metadata['title']}")
        if metadata.get("document_type"):
            context_parts.append(f"type={metadata['document_type']}")
        if metadata.get("phase_hint"):
            context_parts.append(f"phase hint={metadata['phase_hint']}")
        if metadata.get("project_hint"):
            context_parts.append(f"project hint={metadata['project_hint']}")
        context = "; ".join(context_parts)

        tags = ["workspace:affaires"]
        for prefix, value in (
            ("project_hint", metadata.get("project_hint")),
            ("phase_hint", metadata.get("phase_hint")),
        ):
            if value:
                normalized = _tag_value(value)
                if normalized:
                    tags.append(f"{prefix}:{normalized}")
        for value in card.get("tags") or []:
            if isinstance(value, str):
                normalized = _tag_value(value)
                if normalized:
                    tags.append(f"tag:{normalized}")
        tags = list(dict.fromkeys(tags))

        fingerprint_payload = {
            "source_sha256": source_sha256,
            "context": context,
            "metadata": metadata,
            "tags": tags,
        }
        fingerprint = hashlib.sha256(
            json.dumps(
                fingerprint_payload,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        return ProducerCandidate(
            workspace=workspace,
            document_id=document_id,
            hindsight_document_id=f"{document_id}:source",
            source_path=source,
            relative_path=relative_path,
            source_sha256=source_sha256,
            fingerprint=fingerprint,
            context=context,
            tags=tags,
            metadata=metadata,
        )

    def _poll(self, row: dict[str, Any]) -> dict[str, Any]:
        operation_id = row.get("operation_id")
        if not operation_id:
            return row
        try:
            payload = self.client.operation_status(str(operation_id))
        except RuntimeError as exc:
            row["last_error"] = str(exc)
            self._save(
                None,
                hindsight_document_id=row["hindsight_document_id"],
                document_id=row["document_id"],
                workspace=row["workspace"],
                source_path=row["source_path"],
                source_sha256=row["source_sha256"],
                fingerprint=row["fingerprint"],
                operation_id=row.get("operation_id"),
                status=row["status"],
                last_error=row["last_error"],
            )
            return row

        mapped = str(payload["status"]).upper()
        row["status"] = mapped
        row["last_error"] = (
            str(payload.get("error_message"))
            if payload.get("error_message") is not None
            else None
        )
        self._save(
            None,
            hindsight_document_id=row["hindsight_document_id"],
            document_id=row["document_id"],
            workspace=row["workspace"],
            source_path=row["source_path"],
            source_sha256=row["source_sha256"],
            fingerprint=row["fingerprint"],
            operation_id=row.get("operation_id"),
            status=mapped,
            last_error=row.get("last_error"),
        )
        return row

    def reconcile(self, snapshot: dict[str, Any]) -> dict[str, Any]:
        states = self._states()
        for key, row in list(states.items()):
            if row.get("status") in ACTIVE_STATUSES:
                states[key] = self._poll(row)

        candidates: dict[str, ProducerCandidate] = {}
        seen_document_ids: set[str] = set()

        for workspace in snapshot.get("workspaces") or []:
            for card in workspace.get("cards") or []:
                document_id = card.get("document_id")
                if isinstance(document_id, str) and document_id:
                    seen_document_ids.add(document_id)
                try:
                    candidate = self._candidate(card)
                except OSError:
                    candidate = None
                if candidate is not None:
                    candidates[candidate.hindsight_document_id] = candidate

        submitted = 0
        last_error: str | None = None

        for key, candidate in candidates.items():
            row = states.get(key)
            # Active rows were already polled exactly once at the start of this reconcile.
            # Never double-poll an operation in the same pass: a fast PENDING -> COMPLETED
            # transition must not also trigger a replacement submit before the next snapshot.
            if row and row.get("status") in ACTIVE_STATUSES:
                continue

            if row and row.get("fingerprint") == candidate.fingerprint:
                if row.get("status") in {"COMPLETED", "STALE", "BLOCKED"}:
                    if row.get("status") != "COMPLETED":
                        self._save(
                            candidate,
                            hindsight_document_id=key,
                            document_id=candidate.document_id,
                            workspace=candidate.workspace,
                            source_path=candidate.relative_path,
                            source_sha256=candidate.source_sha256,
                            fingerprint=candidate.fingerprint,
                            operation_id=row.get("operation_id"),
                            status="COMPLETED",
                        )
                        row["status"] = "COMPLETED"
                    states[key] = row
                    continue
                if row.get("status") in {"FAILED", "CANCELLED"}:
                    continue

            if submitted >= self.max_submits_per_reconcile:
                self._save(
                    candidate,
                    hindsight_document_id=key,
                    document_id=candidate.document_id,
                    workspace=candidate.workspace,
                    source_path=candidate.relative_path,
                    source_sha256=candidate.source_sha256,
                    fingerprint=candidate.fingerprint,
                    operation_id=None,
                    status="QUEUED",
                )
                states[key] = {
                    "hindsight_document_id": key,
                    "document_id": candidate.document_id,
                    "workspace": candidate.workspace,
                    "source_path": candidate.relative_path,
                    "source_sha256": candidate.source_sha256,
                    "fingerprint": candidate.fingerprint,
                    "operation_id": None,
                    "status": "QUEUED",
                    "last_error": None,
                }
                continue

            try:
                operation_id = self.client.retain_file(
                    candidate.source_path,
                    document_id=candidate.hindsight_document_id,
                    context=candidate.context,
                    tags=candidate.tags,
                    metadata=candidate.metadata,
                )
            except (OSError, RuntimeError) as exc:
                last_error = str(exc)
                self._save(
                    candidate,
                    hindsight_document_id=key,
                    document_id=candidate.document_id,
                    workspace=candidate.workspace,
                    source_path=candidate.relative_path,
                    source_sha256=candidate.source_sha256,
                    fingerprint=candidate.fingerprint,
                    operation_id=None,
                    status="SUBMIT_ERROR",
                    last_error=last_error,
                )
                states[key] = {
                    "hindsight_document_id": key,
                    "document_id": candidate.document_id,
                    "workspace": candidate.workspace,
                    "source_path": candidate.relative_path,
                    "source_sha256": candidate.source_sha256,
                    "fingerprint": candidate.fingerprint,
                    "operation_id": None,
                    "status": "SUBMIT_ERROR",
                    "last_error": last_error,
                }
                continue

            submitted += 1
            self._save(
                candidate,
                hindsight_document_id=key,
                document_id=candidate.document_id,
                workspace=candidate.workspace,
                source_path=candidate.relative_path,
                source_sha256=candidate.source_sha256,
                fingerprint=candidate.fingerprint,
                operation_id=operation_id,
                status="SUBMITTED",
            )
            states[key] = {
                "hindsight_document_id": key,
                "document_id": candidate.document_id,
                "workspace": candidate.workspace,
                "source_path": candidate.relative_path,
                "source_sha256": candidate.source_sha256,
                "fingerprint": candidate.fingerprint,
                "operation_id": operation_id,
                "status": "SUBMITTED",
                "last_error": None,
            }

        for key, row in list(states.items()):
            if key in candidates or row.get("status") in ACTIVE_STATUSES:
                continue
            desired = "BLOCKED" if row.get("document_id") in seen_document_ids else "STALE"
            if row.get("status") != desired:
                self._save(
                    None,
                    hindsight_document_id=key,
                    document_id=row["document_id"],
                    workspace=row["workspace"],
                    source_path=row["source_path"],
                    source_sha256=row["source_sha256"],
                    fingerprint=row["fingerprint"],
                    operation_id=row.get("operation_id"),
                    status=desired,
                    last_error=row.get("last_error"),
                )
                row["status"] = desired

        states = self._states()
        counts = {
            "submitted": 0,
            "completed": 0,
            "pending": 0,
            "failed": 0,
            "blocked": 0,
            "stale": 0,
            "queued": 0,
        }
        for row in states.values():
            status = row.get("status")
            if status == "SUBMITTED":
                counts["submitted"] += 1
            elif status in {"PENDING", "PROCESSING"}:
                counts["pending"] += 1
            elif status == "COMPLETED":
                counts["completed"] += 1
            elif status in {"FAILED", "CANCELLED", "SUBMIT_ERROR"}:
                counts["failed"] += 1
            elif status == "BLOCKED":
                counts["blocked"] += 1
            elif status == "STALE":
                counts["stale"] += 1
            elif status == "QUEUED":
                counts["queued"] += 1

        self._last_summary = {
            "enabled": True,
            "bank_id": self.client.bank_id,
            "mode": "source-only",
            "delete_missing": False,
            **counts,
            "last_error": last_error,
            "last_reconcile_at": _utc_now(),
        }
        return dict(self._last_summary)

    def health(self) -> dict[str, Any]:
        return dict(self._last_summary)
