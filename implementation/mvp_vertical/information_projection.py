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
MEDIA_TYPES = {
    "email", "pdf", "text", "table", "image", "photo", "audio", "video",
    "docx", "xlsx", "ifc", "link", "other",
}
LINK_ROLES = {"primary", "supporting", "attachment"}


class InformationProjectionError(ValueError):
    pass


class InformationProjectionNotFound(InformationProjectionError):
    pass


class StaleInformationProjectionWrite(InformationProjectionError):
    pass


class InformationProjectionGateRequired(InformationProjectionError):
    pass


class InformationProjectionIdempotencyConflict(InformationProjectionError):
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


def _validate_actor(actor: str, actor_kind: str) -> None:
    if not actor or not actor.strip():
        raise InformationProjectionError("actor is required")
    if actor_kind not in {"human", "system"}:
        raise InformationProjectionGateRequired(
            "Hermes cannot mutate canonical Information projection metadata directly"
        )


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
    seen: set[tuple[str, str, str, str]] = set()
    for index, raw in enumerate(values or []):
        if not isinstance(raw, dict):
            raise InformationProjectionError(f"contact ref {index + 1} must be an object")
        unknown = set(raw) - {"label", "person_id", "organization_id", "role"}
        if unknown:
            raise InformationProjectionError(
                f"unsupported contact ref field(s): {', '.join(sorted(unknown))}"
            )
        label = str(raw.get("label") or "").strip()
        if not label:
            raise InformationProjectionError(f"contact ref {index + 1} requires label")
        item = {"label": label}
        for key in ("person_id", "organization_id", "role"):
            value = str(raw.get(key) or "").strip()
            if value:
                item[key] = value
        identity = (
            label.casefold(),
            item.get("person_id", ""),
            item.get("organization_id", ""),
            item.get("role", "").casefold(),
        )
        if identity not in seen:
            seen.add(identity)
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
            SELECT information_id, document_id, role, observed_version,
                   observed_digest, created_at
              FROM agency_information_document_links
             WHERE information_id = %s
             ORDER BY CASE role WHEN 'primary' THEN 0 WHEN 'supporting' THEN 1 ELSE 2 END,
                      document_id
            """,
            (information_id,),
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def _backing_mode(links: list[dict]) -> str:
    if not links:
        return "native"
    return "single_document" if len(links) == 1 else "multiple_documents"


def _replayed(
    conn: psycopg.Connection,
    *,
    information_id: str,
    idempotency_key: str,
    payload_digest: str,
) -> dict | None:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT information_id, payload_digest, result_snapshot
              FROM agency_information_projection_events
             WHERE idempotency_key = %s
            """,
            (idempotency_key,),
        )
        row = cur.fetchone()
    if row is None:
        return None
    if row["information_id"] != information_id or row["payload_digest"] != payload_digest:
        raise InformationProjectionIdempotencyConflict(
            "idempotency key already belongs to another Information projection mutation"
        )
    return _jsonable(dict(row["result_snapshot"]))


def _record_event(
    conn: psycopg.Connection,
    *,
    information_id: str,
    event_type: str,
    actor: str,
    actor_kind: str,
    expected_revision: int,
    resulting_revision: int,
    idempotency_key: str,
    payload: dict,
    result_snapshot: dict,
) -> None:
    conn.execute(
        """
        INSERT INTO agency_information_projection_events (
            event_id, information_id, event_type, actor, actor_kind,
            expected_revision, resulting_revision, idempotency_key,
            payload_digest, payload, result_snapshot
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            f"info-projection-event-{uuid.uuid4().hex}", information_id, event_type,
            actor, actor_kind, expected_revision, resulting_revision, idempotency_key,
            _digest(payload), Jsonb(payload), Jsonb(result_snapshot),
        ),
    )


def get_projection(conn: psycopg.Connection, information_id: str) -> dict:
    information = _ensure_information(conn, information_id)
    metadata = _metadata_row(conn, information_id)
    links = _document_links(conn, information_id)
    return {
        "information": information,
        "projection": {
            **metadata,
            "backing_mode": _backing_mode(links),
            "document_refs": links,
            "business_date": information.get("information_date"),
            "professional_index": information.get("index_label"),
            "business_kind": information.get("category"),
            "lifecycle_status": information.get("status"),
        },
        "document_authority_transferred": False,
        "authorization_inferred": False,
    }


def list_project_projections(conn: psycopg.Connection, project_id: str) -> list[dict]:
    rows = conn.execute(
        """
        SELECT information_id
          FROM agency_information_cards
         WHERE project_id = %s AND status <> 'superseded'
         ORDER BY lower(title), series_id, created_at DESC
        """,
        (project_id,),
    ).fetchall()
    return [get_projection(conn, row[0]) for row in rows]


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
    _validate_actor(actor, actor_kind)
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
        replay = _replayed(
            conn,
            information_id=information_id,
            idempotency_key=idempotency_key,
            payload_digest=digest,
        )
        if replay is not None:
            return replay
        current = _metadata_row(conn, information_id, lock=True)
        if current["revision"] != expected_revision:
            raise StaleInformationProjectionWrite(
                f"stale Information projection revision: expected {expected_revision}, "
                f"current {current['revision']}"
            )
        resulting_revision = expected_revision + 1
        conn.execute(
            """
            INSERT INTO agency_information_projection_metadata (
                information_id, source_date, received_at, issued_at,
                media_types, contact_refs, revision, updated_at
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP)
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
                information_id, source_date, received_at, issued_at,
                Jsonb(payload["media_types"]), Jsonb(payload["contact_refs"]),
                resulting_revision,
            ),
        )
        snapshot = get_projection(conn, information_id)
        _record_event(
            conn,
            information_id=information_id,
            event_type="projection_metadata_updated",
            actor=actor,
            actor_kind=actor_kind,
            expected_revision=expected_revision,
            resulting_revision=resulting_revision,
            idempotency_key=idempotency_key,
            payload=payload,
            result_snapshot=snapshot,
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
    _validate_actor(actor, actor_kind)
    if role not in LINK_ROLES:
        raise InformationProjectionError("unsupported Document link role")
    if observed_version is not None and observed_version < 1:
        raise InformationProjectionError("observed_version must be positive")
    payload = {
        "operation": "add_document_link",
        "information_id": information_id,
        "document_id": document_id,
        "role": role,
        "observed_version": observed_version,
        "observed_digest": observed_digest,
        "actor": actor,
        "actor_kind": actor_kind,
    }
    digest = _digest(payload)
    with conn.transaction():
        _ensure_information(conn, information_id)
        if conn.execute(
            "SELECT 1 FROM source_documents WHERE document_id = %s", (document_id,)
        ).fetchone() is None:
            raise InformationProjectionNotFound(f"unknown Document: {document_id}")
        replay = _replayed(
            conn,
            information_id=information_id,
            idempotency_key=idempotency_key,
            payload_digest=digest,
        )
        if replay is not None:
            return replay
        current = _metadata_row(conn, information_id, lock=True)
        if current["revision"] != expected_revision:
            raise StaleInformationProjectionWrite(
                f"stale Information projection revision: expected {expected_revision}, "
                f"current {current['revision']}"
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
        resulting_revision = expected_revision + 1
        conn.execute(
            """
            INSERT INTO agency_information_projection_metadata (information_id, revision)
            VALUES (%s,%s)
            ON CONFLICT (information_id) DO UPDATE SET
                revision = EXCLUDED.revision,
                updated_at = CURRENT_TIMESTAMP
            """,
            (information_id, resulting_revision),
        )
        snapshot = get_projection(conn, information_id)
        _record_event(
            conn,
            information_id=information_id,
            event_type="document_link_added",
            actor=actor,
            actor_kind=actor_kind,
            expected_revision=expected_revision,
            resulting_revision=resulting_revision,
            idempotency_key=idempotency_key,
            payload=payload,
            result_snapshot=snapshot,
        )
        return snapshot


def remove_document_link(
    conn: psycopg.Connection,
    *,
    information_id: str,
    document_id: str,
    expected_revision: int,
    actor: str,
    actor_kind: Literal["human", "system"],
    idempotency_key: str,
) -> dict:
    _validate_actor(actor, actor_kind)
    payload = {
        "operation": "remove_document_link",
        "information_id": information_id,
        "document_id": document_id,
        "actor": actor,
        "actor_kind": actor_kind,
    }
    digest = _digest(payload)
    with conn.transaction():
        _ensure_information(conn, information_id)
        replay = _replayed(
            conn,
            information_id=information_id,
            idempotency_key=idempotency_key,
            payload_digest=digest,
        )
        if replay is not None:
            return replay
        current = _metadata_row(conn, information_id, lock=True)
        if current["revision"] != expected_revision:
            raise StaleInformationProjectionWrite(
                f"stale Information projection revision: expected {expected_revision}, "
                f"current {current['revision']}"
            )
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM agency_information_document_links
                 WHERE information_id = %s AND document_id = %s
                """,
                (information_id, document_id),
            )
            if cur.rowcount != 1:
                raise InformationProjectionNotFound(
                    f"Document {document_id} is not linked to Information {information_id}"
                )
        resulting_revision = expected_revision + 1
        conn.execute(
            """
            INSERT INTO agency_information_projection_metadata (information_id, revision)
            VALUES (%s,%s)
            ON CONFLICT (information_id) DO UPDATE SET
                revision = EXCLUDED.revision,
                updated_at = CURRENT_TIMESTAMP
            """,
            (information_id, resulting_revision),
        )
        snapshot = get_projection(conn, information_id)
        _record_event(
            conn,
            information_id=information_id,
            event_type="document_link_removed",
            actor=actor,
            actor_kind=actor_kind,
            expected_revision=expected_revision,
            resulting_revision=resulting_revision,
            idempotency_key=idempotency_key,
            payload=payload,
            result_snapshot=snapshot,
        )
        return snapshot
