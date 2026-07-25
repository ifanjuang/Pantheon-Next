"""Bounded PostgreSQL adapter for native Agency Data records.

PostgreSQL is the system of record for these native agency records, but this
module is not a governance authority. Hermes and humans act through explicit,
revision-checked operations; neither receives arbitrary SQL through this API.
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

from .store import dsn_from_env

MIGRATION = Path(__file__).resolve().parent / "sql" / "002_agency_data.sql"

PROJECT_MUTABLE_FIELDS = {
    "code",
    "display_name",
    "description",
    "status",
    "phase",
    "location",
    "primary_client",
    "tags",
}
ACTOR_KINDS = {"human", "hermes", "system"}


class AgencyDataError(ValueError):
    """Base refusal for the bounded Agency Data adapter."""


class ProjectNotFound(AgencyDataError):
    pass


class StaleProjectWrite(AgencyDataError):
    pass


class IdempotencyConflict(AgencyDataError):
    pass


class GovernanceGateRequired(AgencyDataError):
    pass


def connect(dsn: str | None = None) -> psycopg.Connection:
    conn = psycopg.connect(dsn or dsn_from_env())
    conn.execute(MIGRATION.read_text(encoding="utf-8"))
    conn.commit()
    return conn


def _jsonable(value: Any) -> Any:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def _project_row(conn: psycopg.Connection, project_id: str, *, lock: bool = False) -> dict:
    suffix = " FOR UPDATE" if lock else ""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(f"SELECT * FROM agency_projects WHERE project_id = %s{suffix}", (project_id,))
        row = cur.fetchone()
    if row is None:
        raise ProjectNotFound(f"unknown Agency Project: {project_id}")
    return _jsonable(dict(row))


def _payload_digest(payload: dict) -> str:
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _validate_actor(actor: str, actor_kind: str) -> None:
    if not actor or not actor.strip():
        raise AgencyDataError("actor is required")
    if actor_kind not in ACTOR_KINDS:
        raise AgencyDataError("actor_kind must be human, hermes or system")


def _normalize_tags(tags: list[str] | None) -> list[str]:
    if tags is None:
        return []
    normalized: list[str] = []
    seen: set[str] = set()
    for value in tags:
        tag = str(value).strip()
        if not tag:
            continue
        key = tag.casefold()
        if key in seen:
            continue
        seen.add(key)
        normalized.append(tag)
    return normalized


def _replayed_snapshot(
    conn: psycopg.Connection,
    *,
    idempotency_key: str,
    project_id: str,
    payload_digest: str,
) -> dict | None:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT project_id, payload_digest, result_snapshot
              FROM agency_project_events
             WHERE idempotency_key = %s
            """,
            (idempotency_key,),
        )
        row = cur.fetchone()
    if row is None:
        return None
    if row["project_id"] != project_id or row["payload_digest"] != payload_digest:
        raise IdempotencyConflict("idempotency key already belongs to another Agency Data mutation")
    return _jsonable(dict(row["result_snapshot"]))


def _insert_event(
    conn: psycopg.Connection,
    *,
    project_id: str,
    event_type: Literal["project_created", "project_updated"],
    actor: str,
    actor_kind: str,
    expected_revision: int,
    idempotency_key: str,
    payload: dict,
    result_snapshot: dict,
) -> None:
    conn.execute(
        """
        INSERT INTO agency_project_events (
            event_id, project_id, event_type, actor, actor_kind,
            expected_revision, resulting_revision, idempotency_key,
            payload_digest, payload, result_snapshot
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            f"agency-event-{uuid.uuid4().hex}",
            project_id,
            event_type,
            actor,
            actor_kind,
            expected_revision,
            expected_revision + 1,
            idempotency_key,
            _payload_digest(payload),
            Jsonb(payload),
            Jsonb(result_snapshot),
        ),
    )


def list_projects(
    conn: psycopg.Connection,
    *,
    query: str | None = None,
    limit: int = 100,
) -> list[dict]:
    if limit < 1 or limit > 500:
        raise AgencyDataError("project list limit must be between 1 and 500")
    params: list[Any] = []
    where = ""
    if query and query.strip():
        needle = f"%{query.strip()}%"
        where = "WHERE code ILIKE %s OR display_name ILIKE %s OR location ILIKE %s"
        params.extend([needle, needle, needle])
    params.append(limit)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"""
            SELECT *
              FROM agency_projects
              {where}
             ORDER BY lower(display_name), lower(code), project_id
             LIMIT %s
            """,
            params,
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def get_project(conn: psycopg.Connection, project_id: str) -> dict:
    return _project_row(conn, project_id)


def list_project_participations(conn: psycopg.Connection, project_id: str) -> list[dict]:
    _project_row(conn, project_id)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT p.*,
                   person.display_name AS person_name,
                   org.name AS organization_name
              FROM agency_project_participations p
              LEFT JOIN agency_people person ON person.person_id = p.person_id
              LEFT JOIN agency_organizations org ON org.organization_id = p.organization_id
             WHERE p.project_id = %s
             ORDER BY lower(p.role), lower(COALESCE(p.label, person.display_name, org.name, ''))
            """,
            (project_id,),
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def create_project(
    conn: psycopg.Connection,
    *,
    project_id: str,
    code: str,
    display_name: str,
    actor: str,
    actor_kind: str,
    idempotency_key: str,
    description: str = "",
    status: str | None = None,
    phase: str | None = None,
    location: str | None = None,
    primary_client: str | None = None,
    tags: list[str] | None = None,
) -> dict:
    _validate_actor(actor, actor_kind)
    if actor_kind == "hermes":
        raise GovernanceGateRequired(
            "Hermes project creation requires an admitted bounded capability; direct creation is not admitted"
        )
    project_id = project_id.strip()
    code = code.strip()
    display_name = display_name.strip()
    if not project_id or not code or not display_name:
        raise AgencyDataError("project_id, code and display_name are required")

    payload = {
        "operation": "create_project",
        "project_id": project_id,
        "code": code,
        "display_name": display_name,
        "description": description,
        "status": status,
        "phase": phase,
        "location": location,
        "primary_client": primary_client,
        "tags": _normalize_tags(tags),
        "actor": actor,
        "actor_kind": actor_kind,
    }
    digest = _payload_digest(payload)

    with conn.transaction():
        replayed = _replayed_snapshot(
            conn,
            idempotency_key=idempotency_key,
            project_id=project_id,
            payload_digest=digest,
        )
        if replayed is not None:
            return replayed

        with conn.cursor() as cur:
            cur.execute("SELECT project_id FROM agency_projects WHERE project_id = %s", (project_id,))
            if cur.fetchone() is not None:
                raise AgencyDataError(f"Agency Project already exists: {project_id}")
            cur.execute(
                """
                INSERT INTO agency_projects (
                    project_id, code, display_name, description, status, phase,
                    location, primary_client, tags, created_by, updated_by
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    project_id,
                    code,
                    display_name,
                    description,
                    status,
                    phase,
                    location,
                    primary_client,
                    Jsonb(payload["tags"]),
                    actor,
                    actor,
                ),
            )

        snapshot = _project_row(conn, project_id)
        _insert_event(
            conn,
            project_id=project_id,
            event_type="project_created",
            actor=actor,
            actor_kind=actor_kind,
            expected_revision=0,
            idempotency_key=idempotency_key,
            payload=payload,
            result_snapshot=snapshot,
        )
        return snapshot


def update_project(
    conn: psycopg.Connection,
    *,
    project_id: str,
    changes: dict,
    actor: str,
    actor_kind: str,
    expected_revision: int,
    idempotency_key: str,
) -> dict:
    _validate_actor(actor, actor_kind)
    if expected_revision < 1:
        raise AgencyDataError("expected_revision must be at least 1")
    unknown = set(changes) - PROJECT_MUTABLE_FIELDS
    if unknown:
        raise AgencyDataError(f"unsupported Agency Project field(s): {', '.join(sorted(unknown))}")
    if not changes:
        raise AgencyDataError("at least one project field must change")

    normalized = dict(changes)
    if "tags" in normalized:
        normalized["tags"] = _normalize_tags(normalized["tags"])
    for key in {"code", "display_name"} & normalized.keys():
        normalized[key] = str(normalized[key]).strip()
        if not normalized[key]:
            raise AgencyDataError(f"{key} cannot be empty")

    if actor_kind == "hermes":
        raise GovernanceGateRequired(
            "Hermes direct Agency Data mutation is disabled; use an admitted bounded capability"
        )

    payload = {
        "operation": "update_project",
        "project_id": project_id,
        "expected_revision": expected_revision,
        "changes": normalized,
        "actor": actor,
        "actor_kind": actor_kind,
    }
    digest = _payload_digest(payload)

    with conn.transaction():
        replayed = _replayed_snapshot(
            conn,
            idempotency_key=idempotency_key,
            project_id=project_id,
            payload_digest=digest,
        )
        if replayed is not None:
            return replayed

        current = _project_row(conn, project_id, lock=True)
        if current["revision"] != expected_revision:
            raise StaleProjectWrite(
                f"stale Agency Project revision: expected {expected_revision}, current {current['revision']}"
            )

        assignments: list[str] = []
        values: list[Any] = []
        for field in sorted(normalized):
            assignments.append(f"{field} = %s")
            values.append(Jsonb(normalized[field]) if field == "tags" else normalized[field])
        assignments.extend([
            "revision = revision + 1",
            "updated_by = %s",
            "updated_at = CURRENT_TIMESTAMP",
        ])
        values.extend([actor, project_id, expected_revision])
        with conn.cursor() as cur:
            cur.execute(
                f"""
                UPDATE agency_projects
                   SET {', '.join(assignments)}
                 WHERE project_id = %s AND revision = %s
                """,
                values,
            )
            if cur.rowcount != 1:
                raise StaleProjectWrite("Agency Project changed before the mutation was persisted")

        snapshot = _project_row(conn, project_id)
        _insert_event(
            conn,
            project_id=project_id,
            event_type="project_updated",
            actor=actor,
            actor_kind=actor_kind,
            expected_revision=expected_revision,
            idempotency_key=idempotency_key,
            payload=payload,
            result_snapshot=snapshot,
        )
        return snapshot
