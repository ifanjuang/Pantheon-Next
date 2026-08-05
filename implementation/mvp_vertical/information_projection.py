"""Bounded projection metadata and Document links for Agency Information.

This module extends the existing Information owner. It does not duplicate
Document authority, bytes, extraction, archive state or professional truth.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from datetime import date, datetime
from pathlib import Path
from typing import Any, Literal

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

MIGRATION = Path(__file__).resolve().parent / "sql" / "012_information_card_projection.sql"
BACKING_MODES = {"native", "single_document", "multiple_documents"}
MEDIA_TYPES = {"email", "pdf", "text", "table", "image", "photo", "audio", "video", "docx", "xlsx", "ifc", "link", "other"}
LINK_ROLES = {"primary", "supporting", "attachment"}


class InformationProjectionError(ValueError):
    pass


class InformationProjectionNotFound(InformationProjectionError):
    pass


class StaleInformationProjectionWrite(InformationProjectionError):
    pass


class InformationProjectionGateRequired(InformationProjectionError):
    pass


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def _digest(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _ensure_information(conn: psycopg.Connection, information_id: str) -> dict:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM agency_information_cards WHERE information_id = %s", (information_id,))
        row = cur.fetchone()
    if row is None:
        raise InformationProjectionNotFound(f"unknown Agency Information: {information_id}")
    return _jsonable(dict(row))


def _normalize_media_types(values: list[str] | None) -> list[str]:
    normalized: list[str] = []
    seen: set[str] = set()
    for raw in values or ["text"]:
        value = str(raw).strip().lower()
        if value not in MEDIA_TYPES:
            raise InformationProjectionError(f"unsupported media type: {value}")
        if value not in seen:
            seen.add(value)
            normalized.append(value)
    if not normalized:
        raise InformationProjectionError("at least one media type is required")
    return normalized


def _normalize_contacts(values: list[dict] | None) -> list[dict]:
    output: list[dict] = []
    for index, raw in enumerate(values or []):
        if not isinstance(raw, dict):
            raise InformationProjectionError(f"contact ref {index + 1} must be an object")
        unknown = set(raw) - {"label", "person_id", "organization_id", "role"}
        if unknown:
            raise InformationProjectionError(f"unsupported contact ref field(s): {', '.join(sorted(unknown))}")
        label = str(raw.get("label") or "").strip()
        if not label:
            raise InformationProjectionError(f"contact ref {index + 1} requires label")
        item = {"label": label}
        for key in ("person_id", "organization_id", "role"):
            value = str(raw.get(key) or "").strip()
            if value:
                item[key] = value
        output.append(item)
    return output


def _metadata_row(conn: psycopg.Connection, information_id: str, *, lock: bool = False) -> dict:
    suffix = " FOR UPDATE" if lock else ""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"SELECT * FROM agency_information_projection_metadata WHERE information_id = %s{suffix}",
            (information_id,),
        )
        row = cur.fetchone()
    if row is None:
        return {
            "information_id": information_id,
            "backing_mode": "native",
            "source_date": None,
            "received_at": None,
            "issued_at": None,
            "media_types": ["text"],
            "contact_refs": [],
            "revision": 0,
            "updated_at": None,
        }
    return _jsonable(dict(row))


def _document_links(conn: psycopg.Connection, information_id: str) -> list[dict]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT information_id, document_id, role, observed_version, observed_digest, created_at
              FROM agency_information_document_links
             WHERE information_id = %s
             ORDER BY CASE role WHEN 'primary' THEN 0 WHEN 'supporting' THEN 1 ELSE 2 END,
                      document_id
            """,
            (information_id,),
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def get_projection(conn: psycopg.Connection, information_id: str) -> dict:
    information = _ensure_information(conn, information_id)
    metadata = _metadata_row(conn, information_id)
    links = _document_links(conn, information_id)
    backing_mode = "native" if not links else ("single_document" if len(links) == 1 else "multiple_documents")
    return {
        "information": information,
        "projection": {**metadata, "backing_mode": backing_mode, "document_refs": links},
        "document_authority_transferred": False,
        "authorization_inferred": False,
    }


def update_projection_metadata(
    conn: psycopg.Connection,
    *,
    information_id: str,
    source_date: date | None,
    received_at: datetime | None,
    issued_at: datetime | None,
    media_types: list[str] | None,
    contact_refs: list[dict] | None,
    expected_revision: int,
    actor: str,
    actor_kind: Literal["human", "system"],
    idempotency_key: str,
) -> dict:
    if actor_kind not in {"human", "system"}:
        raise InformationProjectionGateRequired("Hermes cannot mutate canonical Information projection metadata directly")
    payload = {
        "operation": "update_projection_metadata",
        "information_id": information_id,
        "source_date": source_date.isoformat() if source_date else None,
        "received_at": received_at.isoformat() if received_at else None,
        "issued_at": issued_at.isoformat() if issued_at else None,
        "media_types": _normalize_media_types(media_types),
        "contact_refs": _normalize_contacts(contact_refs),
        "actor": actor,
        "actor_kind": actor_kind,
    }
    digest = _digest(payload)
    with conn.transaction():
        _ensure_information(conn, information_id)
        replay = conn.execute(
            "SELECT payload_digest, result_snapshot FROM agency_information_projection_events WHERE idempotency_key = %s",
            (idempotency_key,),
        ).fetchone()
        if replay:
            if replay[0] != digest:
                raise InformationProjectionError("idempotency key already belongs to another projection mutation")
            return _jsonable(dict(replay[1]))
        current = _metadata_row(conn, information_id, lock=True)
        if current["revision"] != expected_revision:
            raise StaleInformationProjectionWrite(
                f"stale Information projection revision: expected {expected_revision}, current {current['revision']}"
            )
        resulting_revision = expected_revision + 1
        conn.execute(
            """
            INSERT INTO agency_information_projection_metadata (
                information_id, backing_mode, source_date, received_at, issued_at,
                media_types, contact_refs, revision, updated_at
            ) VALUES (%s, 'native', %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
            ON CONFLICT (information_id) DO UPDATE SET
                source_date = EXCLUDED.source_date,
                received_at = EXCLUDED.received_at,
                issued_at = EXCLUDED.issued_at,
                media_types = EXCLUDED.media_types,
                contact_refs = EXCLUDED.contact_refs,
                revision = EXCLUDED.revision,
                updated_at = CURRENT_TIMESTAMP
            """,
            (
                information_id,
                source_date,
                received_at,
                issued_at,
                Jsonb(payload["media_types"]),
                Jsonb(payload["contact_refs"]),
                resulting_revision,
            ),
        )
        snapshot = get_projection(conn, information_id)
        conn.execute(
            """
            INSERT INTO agency_information_projection_events (
                event_id, information_id, event_type, actor, actor_kind,
                expected_revision, resulting_revision, idempotency_key,
                payload_digest, payload, result_snapshot
            ) VALUES (%s,%s,'projection_metadata_updated',%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                f"info-projection-event-{uuid.uuid4().hex}", information_id, actor, actor_kind,
                expected_revision, resulting_revision, idempotency_key, digest,
                Jsonb(payload), Jsonb(snapshot),
            ),
        )
        return snapshot


def add_document_link(
    conn: psycopg.Connection,
    *,
    information_id: str,
    document_id: str,
    role: Literal["primary", "supporting", "attachment"],
    observed_version: int | None,
    observed_digest: str | None,
    expected_revision: int,
    actor: str,
    actor_kind: Literal["human", "system"],
    idempotency_key: str,
) -> dict:
    if actor_kind not in {"human", "system"}:
        raise InformationProjectionGateRequired("Hermes cannot link canonical Documents directly")
    if role not in LINK_ROLES:
        raise InformationProjectionError("unsupported Document link role")
    payload = {
        "operation": "add_document_link", "information_id": information_id,
        "document_id": document_id, "role": role,
        "observed_version": observed_version, "observed_digest": observed_digest,
        "actor": actor, "actor_kind": actor_kind,
    }
    digest = _digest(payload)
    with conn.transaction():
        _ensure_information(conn, information_id)
        if conn.execute("SELECT 1 FROM source_documents WHERE document_id = %s", (document_id,)).fetchone() is None:
            raise InformationProjectionNotFound(f"unknown Document: {document_id}")
        replay = conn.execute(
            "SELECT payload_digest, result_snapshot FROM agency_information_projection_events WHERE idempotency_key = %s",
            (idempotency_key,),
        ).fetchone()
        if replay:
            if replay[0] != digest:
                raise InformationProjectionError("idempotency key already belongs to another projection mutation")
            return _jsonable(dict(replay[1]))
        current = _metadata_row(conn, information_id, lock=True)
        if current["revision"] != expected_revision:
            raise StaleInformationProjectionWrite(
                f"stale Information projection revision: expected {expected_revision}, current {current['revision']}"
            )
        conn.execute(
            """
            INSERT INTO agency_information_document_links (
                information_id, document_id, role, observed_version, observed_digest
            ) VALUES (%s,%s,%s,%s,%s)
            ON CONFLICT (information_id, document_id) DO UPDATE SET
                role = EXCLUDED.role,
                observed_version = EXCLUDED.observed_version,
                observed_digest = EXCLUDED.observed_digest
            """,
            (information_id, document_id, role, observed_version, observed_digest),
        )
        link_count = conn.execute(
            "SELECT count(*) FROM agency_information_document_links WHERE information_id = %s",
            (information_id,),
        ).fetchone()[0]
        backing_mode = "single_document" if link_count == 1 else "multiple_documents"
        resulting_revision = expected_revision + 1
        conn.execute(
            """
            INSERT INTO agency_information_projection_metadata (information_id, backing_mode, revision)
            VALUES (%s,%s,%s)
            ON CONFLICT (information_id) DO UPDATE SET
                backing_mode = EXCLUDED.backing_mode,
                revision = EXCLUDED.revision,
                updated_at = CURRENT_TIMESTAMP
            """,
            (information_id, backing_mode, resulting_revision),
        )
        snapshot = get_projection(conn, information_id)
        conn.execute(
            """
            INSERT INTO agency_information_projection_events (
                event_id, information_id, event_type, actor, actor_kind,
                expected_revision, resulting_revision, idempotency_key,
                payload_digest, payload, result_snapshot
            ) VALUES (%s,%s,'document_link_added',%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                f"info-projection-event-{uuid.uuid4().hex}", information_id, actor, actor_kind,
                expected_revision, resulting_revision, idempotency_key, digest,
                Jsonb(payload), Jsonb(snapshot),
            ),
        )
        return snapshot
