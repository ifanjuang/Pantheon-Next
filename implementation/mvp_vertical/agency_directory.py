"""Read-only directory projections for native Agency Data.

People, Organizations and project participations remain PostgreSQL-owned records.
This module exposes normalized reads only; mutation policy is intentionally kept
separate until actor/gate rules are defined for those record families.
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Any

import psycopg
from psycopg.rows import dict_row

from . import agency_data


class AgencyDirectoryError(ValueError):
    pass


class PersonNotFound(AgencyDirectoryError):
    pass


class OrganizationNotFound(AgencyDirectoryError):
    pass


class ParticipationNotFound(AgencyDirectoryError):
    pass


def _jsonable(value: Any) -> Any:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def _bounded_limit(limit: int) -> int:
    if limit < 1 or limit > 500:
        raise AgencyDirectoryError("directory limit must be between 1 and 500")
    return limit


def _accent_like(column: str) -> str:
    return f"unaccent(lower({column})) LIKE unaccent(lower(%s))"


def list_people(
    conn: psycopg.Connection,
    *,
    query: str | None = None,
    limit: int = 100,
) -> list[dict]:
    _bounded_limit(limit)
    params: list[Any] = []
    where = ""
    if query and query.strip():
        needle = f"%{query.strip()}%"
        where = "WHERE " + " OR ".join(
            [_accent_like("display_name"), _accent_like("email"), _accent_like("phone")]
        )
        params.extend([needle, needle, needle])
    params.append(limit)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"""
            SELECT *
              FROM agency_people
              {where}
             ORDER BY lower(display_name), person_id
             LIMIT %s
            """,
            params,
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def get_person(conn: psycopg.Connection, person_id: str) -> dict:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM agency_people WHERE person_id = %s", (person_id,))
        row = cur.fetchone()
    if row is None:
        raise PersonNotFound(f"unknown Agency Person: {person_id}")
    return _jsonable(dict(row))


def list_organizations(
    conn: psycopg.Connection,
    *,
    query: str | None = None,
    limit: int = 100,
) -> list[dict]:
    _bounded_limit(limit)
    params: list[Any] = []
    where = ""
    if query and query.strip():
        needle = f"%{query.strip()}%"
        where = "WHERE " + " OR ".join(
            [
                _accent_like("name"),
                _accent_like("email"),
                _accent_like("phone"),
                _accent_like("siret"),
            ]
        )
        params.extend([needle, needle, needle, needle])
    params.append(limit)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"""
            SELECT *
              FROM agency_organizations
              {where}
             ORDER BY lower(name), organization_id
             LIMIT %s
            """,
            params,
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def get_organization(conn: psycopg.Connection, organization_id: str) -> dict:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM agency_organizations WHERE organization_id = %s",
            (organization_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise OrganizationNotFound(f"unknown Agency Organization: {organization_id}")
    return _jsonable(dict(row))


def get_participation(conn: psycopg.Connection, participation_id: str) -> dict:
    """Return one exact ProjectParticipation without invoking a directory search."""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT p.*,
                   person.display_name AS person_name,
                   org.name AS organization_name,
                   project.display_name AS project_name,
                   project.code AS project_code
              FROM agency_project_participations p
              JOIN agency_projects project ON project.project_id = p.project_id
              LEFT JOIN agency_people person ON person.person_id = p.person_id
              LEFT JOIN agency_organizations org ON org.organization_id = p.organization_id
             WHERE p.participation_id = %s
            """,
            (participation_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise ParticipationNotFound(
            f"unknown Agency ProjectParticipation: {participation_id}"
        )
    return _jsonable(dict(row))


def list_participations(
    conn: psycopg.Connection,
    *,
    query: str | None = None,
    project_id: str | None = None,
    limit: int = 100,
) -> list[dict]:
    _bounded_limit(limit)
    clauses: list[str] = []
    params: list[Any] = []
    if project_id:
        clauses.append("p.project_id = %s")
        params.append(project_id)
    if query and query.strip():
        needle = f"%{query.strip()}%"
        clauses.append(
            "(" + " OR ".join(
                [
                    _accent_like("p.role"),
                    _accent_like("p.participation_type"),
                    _accent_like("p.label"),
                    _accent_like("person.display_name"),
                    _accent_like("org.name"),
                    _accent_like("project.display_name"),
                    _accent_like("project.code"),
                ]
            ) + ")"
        )
        params.extend([needle, needle, needle, needle, needle, needle, needle])
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    params.append(limit)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"""
            SELECT p.*,
                   person.display_name AS person_name,
                   org.name AS organization_name,
                   project.display_name AS project_name,
                   project.code AS project_code
              FROM agency_project_participations p
              JOIN agency_projects project ON project.project_id = p.project_id
              LEFT JOIN agency_people person ON person.person_id = p.person_id
              LEFT JOIN agency_organizations org ON org.organization_id = p.organization_id
              {where}
             ORDER BY lower(project.display_name), lower(p.role),
                      lower(COALESCE(p.label, person.display_name, org.name, ''))
             LIMIT %s
            """,
            params,
        )
        rows = cur.fetchall()
    return [_jsonable(dict(row)) for row in rows]


def list_project_participations(conn: psycopg.Connection, project_id: str) -> list[dict]:
    try:
        agency_data.get_project(conn, project_id)
    except agency_data.ProjectNotFound as exc:
        raise AgencyDirectoryError(str(exc)) from exc
    return list_participations(conn, project_id=project_id, limit=500)
