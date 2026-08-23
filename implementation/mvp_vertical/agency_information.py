"""Versioned Agency Information cards.

An ACTED Information card is immutable. Any later work happens in one working
version derived from the current ACTED version. The declarative Information
schema controls field shape and named projections; lifecycle transitions remain
explicit domain gates in this module.
"""

from __future__ import annotations

import uuid
from datetime import date, datetime
from pathlib import Path
from typing import Any, Literal

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from . import agency_schema

MIGRATION = Path(__file__).resolve().parent / "sql" / "004_agency_information_cards.sql"
WORKING_STATUSES = {"draft", "in_progress"}
VISIBLE_STATUSES = {"draft", "in_progress", "acted"}
ALL_STATUSES = VISIBLE_STATUSES | {"superseded"}
SOURCE_VERSION_FIELDS = {"source_type", "source_ref", "source_note", "source_version", "index_label"}


class AgencyInformationError(ValueError):
    pass


class InformationNotFound(AgencyInformationError):
    pass


class ImmutableActedInformation(AgencyInformationError):
    pass


class StaleInformationWrite(AgencyInformationError):
    pass


class InformationGateRequired(AgencyInformationError):
    pass


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def _row(conn: psycopg.Connection, information_id: str, *, lock: bool = False) -> dict:
    suffix = " FOR UPDATE" if lock else ""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"SELECT * FROM agency_information_cards WHERE information_id = %s{suffix}",
            (information_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise InformationNotFound(f"unknown Agency Information: {information_id}")
    return _jsonable(dict(row))


def _schema_values(values: dict[str, Any], *, allowed_fields: set[str]) -> dict[str, Any]:
    try:
        return agency_schema.normalize_declared_fields(
            "information",
            values,
            allowed_fields=allowed_fields,
        )
    except agency_schema.AgencySchemaError as exc:
        raise AgencyInformationError(str(exc)) from exc


def _editable_fields() -> set[str]:
    return set(agency_schema.get_information_view("edit")["fields"])


def _validate_source(source_ref: str | None, source_note: str | None) -> None:
    if not (source_ref and source_ref.strip()) and not (source_note and source_note.strip()):
        raise AgencyInformationError("source_ref or source_note is required")


def create_information(
    conn: psycopg.Connection,
    *,
    project_id: str,
    title: str,
    category: str,
    source_type: str,
    index_label: str,
    actor_kind: Literal["human", "system"],
    source_ref: str | None = None,
    source_note: str | None = None,
    source_version: str | None = None,
    information_date: date | None = None,
    summary: str = "",
    details: str = "",
    limits: list[str] | None = None,
    type_tags: list[str] | None = None,
    subject_tags: list[str] | None = None,
    author: str | None = None,
    status: Literal["draft", "in_progress"] = "draft",
    series_id: str | None = None,
) -> dict:
    if actor_kind not in {"human", "system"}:
        raise InformationGateRequired("Hermes cannot create a canonical Information series directly")
    if status not in WORKING_STATUSES:
        raise AgencyInformationError("new Information must start as draft or in_progress")
    _validate_source(source_ref, source_note)

    values = _schema_values(
        {
            "project_id": project_id,
            "title": title,
            "category": category,
            "source_type": source_type,
            "source_ref": source_ref,
            "source_note": source_note,
            "source_version": source_version,
            "index_label": index_label,
            "information_date": information_date,
            "summary": summary,
            "details": details,
            "limits": limits or [],
            "type_tags": type_tags or [],
            "subject_tags": subject_tags or [],
            "author": author,
            "status": status,
        },
        allowed_fields={
            "project_id",
            "title",
            "category",
            "source_type",
            "source_ref",
            "source_note",
            "source_version",
            "index_label",
            "information_date",
            "summary",
            "details",
            "limits",
            "type_tags",
            "subject_tags",
            "author",
            "status",
        },
    )

    information_id = f"info-{uuid.uuid4().hex}"
    series_id = series_id or f"info-series-{uuid.uuid4().hex}"
    with conn.transaction():
        conn.execute(
            """
            INSERT INTO agency_information_cards (
                information_id, series_id, project_id, title, category,
                source_type, source_ref, source_note, source_version, index_label,
                information_date, summary, details, status, limits, type_tags,
                subject_tags, author
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                information_id,
                series_id,
                values["project_id"],
                values["title"],
                values["category"],
                values["source_type"],
                values.get("source_ref"),
                values.get("source_note"),
                values.get("source_version"),
                values["index_label"],
                values.get("information_date"),
                values.get("summary") or "",
                values.get("details") or "",
                values["status"],
                Jsonb(values.get("limits") or []),
                Jsonb(values.get("type_tags") or []),
                Jsonb(values.get("subject_tags") or []),
                values.get("author"),
            ),
        )
    return _row(conn, information_id)


def derive_working_version(
    conn: psycopg.Connection,
    *,
    acted_information_id: str,
    new_index_label: str,
    source_ref: str | None,
    source_note: str | None,
    source_version: str | None = None,
    actor_kind: Literal["human", "system"] = "human",
) -> dict:
    if actor_kind not in {"human", "system"}:
        raise InformationGateRequired("Hermes cannot create the next source version directly")
    _validate_source(source_ref, source_note)

    source_values = _schema_values(
        {
            "source_ref": source_ref,
            "source_note": source_note,
            "source_version": source_version,
            "index_label": new_index_label,
        },
        allowed_fields={"source_ref", "source_note", "source_version", "index_label"},
    )

    with conn.transaction():
        acted = _row(conn, acted_information_id, lock=True)
        if acted["status"] != "acted":
            raise AgencyInformationError("working version must derive from the current acted Information")
        information_id = f"info-{uuid.uuid4().hex}"
        conn.execute(
            """
            INSERT INTO agency_information_cards (
                information_id, series_id, project_id, title, category,
                source_type, source_ref, source_note, source_version, index_label,
                information_date, summary, details, status, limits, type_tags,
                subject_tags, author, base_acted_id, previous_source_id
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'draft',%s,%s,%s,%s,%s,%s)
            """,
            (
                information_id,
                acted["series_id"],
                acted["project_id"],
                acted["title"],
                acted["category"],
                acted["source_type"],
                source_values.get("source_ref"),
                source_values.get("source_note"),
                source_values.get("source_version"),
                source_values["index_label"],
                acted.get("information_date"),
                acted.get("summary", ""),
                acted.get("details", ""),
                Jsonb(acted.get("limits", [])),
                Jsonb(acted.get("type_tags", [])),
                Jsonb(acted.get("subject_tags", [])),
                acted.get("author"),
                acted["information_id"],
                acted["information_id"],
            ),
        )
    return _row(conn, information_id)


def update_working_information(
    conn: psycopg.Connection,
    *,
    information_id: str,
    changes: dict,
    expected_revision: int,
    actor_kind: Literal["human", "hermes", "system"],
    hermes_admitted: bool = False,
) -> dict:
    if not changes:
        raise AgencyInformationError("at least one Information field must change")
    if actor_kind == "hermes" and not hermes_admitted:
        raise InformationGateRequired("Hermes Information editing requires an admitted bounded capability")

    editable_fields = _editable_fields()
    normalized = _schema_values(changes, allowed_fields=editable_fields)
    if "status" in normalized and normalized["status"] not in WORKING_STATUSES:
        raise AgencyInformationError("working status may only be draft or in_progress")

    with conn.transaction():
        current = _row(conn, information_id, lock=True)
        if current["status"] not in WORKING_STATUSES:
            raise ImmutableActedInformation("acted or superseded Information cannot be edited")
        if current["revision"] != expected_revision:
            raise StaleInformationWrite(
                f"stale Information revision: expected {expected_revision}, current {current['revision']}"
            )
        assignments: list[str] = []
        values: list[Any] = []
        for field in sorted(normalized):
            assignments.append(f"{field} = %s")
            values.append(Jsonb(normalized[field]) if field in {"limits", "type_tags", "subject_tags"} else normalized[field])
        assignments.extend(["revision = revision + 1", "updated_at = CURRENT_TIMESTAMP"])
        values.extend([information_id, expected_revision])
        with conn.cursor() as cur:
            cur.execute(
                f"UPDATE agency_information_cards SET {', '.join(assignments)} WHERE information_id = %s AND revision = %s",
                values,
            )
            if cur.rowcount != 1:
                raise StaleInformationWrite("Information changed before the update was persisted")
    return _row(conn, information_id)


def act_working_information(
    conn: psycopg.Connection,
    *,
    information_id: str,
    expected_revision: int,
    actor_kind: Literal["human"],
) -> dict:
    if actor_kind != "human":
        raise InformationGateRequired("only a human may act an Information version")
    with conn.transaction():
        working = _row(conn, information_id, lock=True)
        if working["status"] not in WORKING_STATUSES:
            raise AgencyInformationError("only a working Information version can be acted")
        if working["revision"] != expected_revision:
            raise StaleInformationWrite(
                f"stale Information revision: expected {expected_revision}, current {working['revision']}"
            )
        conn.execute(
            """
            UPDATE agency_information_cards
               SET status = 'superseded', revision = revision + 1,
                   updated_at = CURRENT_TIMESTAMP
             WHERE series_id = %s AND status = 'acted'
            """,
            (working["series_id"],),
        )
        conn.execute(
            """
            UPDATE agency_information_cards
               SET status = 'acted', acted_at = CURRENT_TIMESTAMP,
                   revision = revision + 1, updated_at = CURRENT_TIMESTAMP
             WHERE information_id = %s AND revision = %s
            """,
            (information_id, expected_revision),
        )
    return _row(conn, information_id)


def get_information_context(conn: psycopg.Connection, information_id: str) -> dict:
    current = _row(conn, information_id)
    acted = None
    if current["status"] in WORKING_STATUSES and current.get("base_acted_id"):
        acted = _row(conn, current["base_acted_id"])
    elif current["status"] == "acted":
        acted = current
    return {
        "current": current,
        "last_acted": acted,
        "working_assumptions_are_not_acted": current["status"] in WORKING_STATUSES,
        "edit_schema": agency_schema.get_information_schema("edit"),
        "schema_authorization_inferred": False,
    }


def list_project_information(conn: psycopg.Connection, project_id: str) -> list[dict]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT *
              FROM agency_information_cards
             WHERE project_id = %s AND status <> 'superseded'
             ORDER BY lower(title), series_id, created_at DESC
            """,
            (project_id,),
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]
