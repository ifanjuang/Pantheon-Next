"""Semantic ProjectClaim persistence for Agency Data.

A ProjectClaim is backend semantics, not a visible Cockpit family. It records a
source-qualified value that may be projected on a Project while preserving the
entity that backs it.

    ProjectClaim != Evidence
    ProjectClaim != approval
    source_backed != verified != opposable

Rows are append-only. A later claim may supersede a prior claim; the prior row is
never rewritten. Every emitted claim is validated against the vendored Pantheon
Next governance schema.
"""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

import jsonschema
import psycopg
import yaml
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from . import agency_schema

SCHEMA = Path(__file__).resolve().parent / "vendor" / "pantheon" / "project_claim.schema.yaml"

GOVERNANCE_REFS = [
    "docs/domain-packs/architecture/PROJECT_CARD_DECK_COMPOSITION.md",
    "docs/governance/AGENCY_DATA_SYSTEM_OF_RECORD.md",
    "docs/governance/CARD_STACK_MODEL.md",
]
CLAIM_STATUSES = {"asserted", "source_backed", "verified", "contested", "retired"}
SOURCE_KINDS = {"information", "document", "human_assertion", "derived", "external_projection"}


class AgencyClaimError(ValueError):
    pass


class ClaimNotFound(AgencyClaimError):
    pass


class ClaimContractViolation(AgencyClaimError):
    pass


@lru_cache(maxsize=1)
def _validator() -> jsonschema.Draft202012Validator:
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    return jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())


def validate_claim(claim: dict[str, Any]) -> None:
    try:
        _validator().validate(claim)
    except jsonschema.ValidationError as exc:
        raise ClaimContractViolation(
            f"project claim violates its governed contract: {exc.message}"
        ) from exc


def _jsonable(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def _claim_from_row(row: dict[str, Any]) -> dict[str, Any]:
    backing_ref = None
    if row.get("backing_entity_type") and row.get("backing_entity_id"):
        backing_ref = {
            "entity_type": row["backing_entity_type"],
            "entity_id": row["backing_entity_id"],
            "observed_status": row.get("backing_observed_status"),
        }
    claim = {
        "claim_id": row["claim_id"],
        "project_id": row["project_id"],
        "claim_type": row["claim_type"],
        "value": row["value"],
        "unit": row.get("unit"),
        "backing_ref": backing_ref,
        "provenance": {
            "source_kind": row["source_kind"],
            "source_ref": row.get("source_ref"),
            "asserted_by": row.get("asserted_by"),
            "derivation_note": row.get("derivation_note"),
        },
        "status": row["status"],
        "observed_at": _jsonable(row["observed_at"]),
        "revision": row["revision"],
        "supersedes": row.get("supersedes"),
        "note": row.get("note"),
        "governance_refs": list(GOVERNANCE_REFS),
    }
    validate_claim(claim)
    return claim


def _declared_claim_field(claim_type: str) -> dict[str, Any]:
    fields = agency_schema.project_claim_fields()
    field = fields.get(str(claim_type or "").strip())
    if field is None:
        raise AgencyClaimError(f"undeclared Project claim type: {claim_type}")
    return field


def _normalize_claim_value(field: dict[str, Any], value: Any) -> Any:
    if field.get("aggregation") == "list":
        if not isinstance(value, str):
            raise AgencyClaimError(f"Project claim {field['claim_type']} requires one scalar string value")
        value = value.strip()
        if not value:
            raise AgencyClaimError(f"Project claim {field['claim_type']} may not be empty")
        return value
    try:
        return agency_schema.normalize_field_value("project", field, value)
    except agency_schema.AgencySchemaError as exc:
        raise AgencyClaimError(str(exc)) from exc


def _normalize_backing_ref(backing_ref: dict[str, Any] | None) -> dict[str, str | None] | None:
    if backing_ref is None:
        return None
    if not isinstance(backing_ref, dict):
        raise AgencyClaimError("backing_ref must be an object")
    unknown = set(backing_ref) - {"entity_type", "entity_id", "observed_status"}
    if unknown:
        raise AgencyClaimError(f"unsupported backing_ref field(s): {', '.join(sorted(unknown))}")
    entity_type = str(backing_ref.get("entity_type") or "").strip()
    entity_id = str(backing_ref.get("entity_id") or "").strip()
    if not entity_type or not entity_id:
        raise AgencyClaimError("backing_ref requires entity_type and entity_id")
    observed_status = backing_ref.get("observed_status")
    return {
        "entity_type": entity_type,
        "entity_id": entity_id,
        "observed_status": str(observed_status).strip() if observed_status is not None else None,
    }


def _normalize_observed_at(observed_at: str | datetime | None) -> str:
    if observed_at is None:
        return datetime.now(timezone.utc).isoformat()
    if isinstance(observed_at, datetime):
        value = observed_at
    elif isinstance(observed_at, str):
        text = observed_at.strip().replace("Z", "+00:00")
        try:
            value = datetime.fromisoformat(text)
        except ValueError as exc:
            raise AgencyClaimError("observed_at must be an ISO datetime") from exc
    else:
        raise AgencyClaimError("observed_at must be an ISO datetime")
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.isoformat()


def record_claim(
    conn: psycopg.Connection,
    *,
    project_id: str,
    claim_type: str,
    value: Any,
    actor: str,
    source_kind: str = "human_assertion",
    backing_ref: dict[str, Any] | None = None,
    source_ref: str | None = None,
    derivation_note: str | None = None,
    status: str = "asserted",
    observed_at: str | datetime | None = None,
    supersedes: str | None = None,
    note: str | None = None,
    claim_id: str | None = None,
) -> dict[str, Any]:
    """Append one governed claim. This records a value; it approves nothing."""
    project_id = str(project_id or "").strip()
    actor = str(actor or "").strip()
    claim_type = str(claim_type or "").strip()
    if not project_id or not actor or not claim_type:
        raise AgencyClaimError("project_id, claim_type and actor are required")
    if status not in CLAIM_STATUSES:
        raise AgencyClaimError(f"unknown claim status: {status}")
    if source_kind not in SOURCE_KINDS:
        raise AgencyClaimError(f"unknown claim source_kind: {source_kind}")

    field = _declared_claim_field(claim_type)
    normalized_value = _normalize_claim_value(field, value)
    normalized_backing = _normalize_backing_ref(backing_ref)
    if status in {"source_backed", "verified"} and normalized_backing is None:
        raise AgencyClaimError(f"{status} Project claim requires backing_ref")
    expected_unit = field.get("unit")
    unit = expected_unit if expected_unit else None
    observed = _normalize_observed_at(observed_at)
    claim_id = str(claim_id or f"claim.{uuid.uuid4().hex}").strip().lower()

    if supersedes:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT project_id, claim_type FROM agency_project_claims WHERE claim_id = %s",
                (supersedes,),
            )
            prior = cur.fetchone()
        if prior is None:
            raise ClaimNotFound(f"unknown superseded Project claim: {supersedes}")
        if prior["project_id"] != project_id or prior["claim_type"] != claim_type:
            raise AgencyClaimError("supersedes must reference the same project and claim_type")

    candidate = {
        "claim_id": claim_id,
        "project_id": project_id,
        "claim_type": claim_type,
        "value": normalized_value,
        "unit": unit,
        "backing_ref": normalized_backing,
        "provenance": {
            "source_kind": source_kind,
            "source_ref": str(source_ref).strip() if source_ref is not None else None,
            "asserted_by": actor,
            "derivation_note": str(derivation_note).strip() if derivation_note is not None else None,
        },
        "status": status,
        "observed_at": observed,
        "revision": 0,
        "supersedes": supersedes,
        "note": str(note).strip() if note is not None else None,
        "governance_refs": list(GOVERNANCE_REFS),
    }
    validate_claim(candidate)

    with conn.transaction():
        project = conn.execute(
            "SELECT project_id FROM agency_projects WHERE project_id = %s",
            (project_id,),
        ).fetchone()
        if project is None:
            raise AgencyClaimError(f"unknown Agency Project: {project_id}")
        conn.execute(
            """
            INSERT INTO agency_project_claims (
                claim_id, project_id, claim_type, value, unit,
                backing_entity_type, backing_entity_id, backing_observed_status,
                source_kind, source_ref, asserted_by, derivation_note,
                status, observed_at, revision, supersedes, note
            ) VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s, %s,
                %s, %s, 0, %s, %s
            )
            """,
            (
                claim_id,
                project_id,
                claim_type,
                Jsonb(normalized_value),
                unit,
                normalized_backing["entity_type"] if normalized_backing else None,
                normalized_backing["entity_id"] if normalized_backing else None,
                normalized_backing["observed_status"] if normalized_backing else None,
                source_kind,
                candidate["provenance"]["source_ref"],
                actor,
                candidate["provenance"]["derivation_note"],
                status,
                observed,
                supersedes,
                candidate["note"],
            ),
        )
    return get_claim(conn, claim_id)


def get_claim(conn: psycopg.Connection, claim_id: str) -> dict[str, Any]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM agency_project_claims WHERE claim_id = %s", (claim_id,))
        row = cur.fetchone()
    if row is None:
        raise ClaimNotFound(f"unknown Project claim: {claim_id}")
    return _claim_from_row(dict(row))


def list_project_claims(conn: psycopg.Connection, project_id: str, *, limit: int = 500) -> list[dict[str, Any]]:
    project_id = str(project_id or "").strip()
    if not project_id:
        raise AgencyClaimError("project_id is required")
    if limit < 1 or limit > 1000:
        raise AgencyClaimError("claim list limit must be between 1 and 1000")
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT *
              FROM agency_project_claims
             WHERE project_id = %s
             ORDER BY observed_at DESC, created_at DESC, claim_id DESC
             LIMIT %s
            """,
            (project_id, limit),
        )
        rows = [dict(row) for row in cur.fetchall()]
    return [_claim_from_row(row) for row in rows]


def active_project_claims(conn: psycopg.Connection, project_id: str) -> list[dict[str, Any]]:
    """Return unsuperseded, non-retired claims in newest-first order."""
    claims = list_project_claims(conn, project_id)
    superseded = {claim["supersedes"] for claim in claims if claim.get("supersedes")}
    return [
        claim
        for claim in claims
        if claim["status"] != "retired" and claim["claim_id"] not in superseded
    ]


def project_claim_projection(conn: psycopg.Connection, project_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return display values plus provenance refs for declared Project claim fields."""
    active = active_project_claims(conn, project_id)
    fields = agency_schema.project_claim_fields()
    by_type: dict[str, list[dict[str, Any]]] = {}
    for claim in active:
        if claim["claim_type"] in fields:
            by_type.setdefault(claim["claim_type"], []).append(claim)

    values: dict[str, Any] = {}
    refs: dict[str, Any] = {}
    for claim_type, field in fields.items():
        candidates = by_type.get(claim_type, [])
        if not candidates:
            continue
        if field.get("aggregation") == "list":
            seen: set[str] = set()
            projected_values: list[Any] = []
            projected_refs: list[dict[str, Any]] = []
            for claim in candidates:
                marker = json.dumps(claim["value"], sort_keys=True, ensure_ascii=False)
                if marker in seen:
                    continue
                seen.add(marker)
                projected_values.append(claim["value"])
                projected_refs.append(claim)
            values[claim_type] = projected_values
            refs[claim_type] = projected_refs
        else:
            values[claim_type] = candidates[0]["value"]
            refs[claim_type] = candidates[0]
    return values, refs


def enrich_project_with_claims(conn: psycopg.Connection, project: dict[str, Any]) -> dict[str, Any]:
    enriched = dict(project)
    values, refs = project_claim_projection(conn, project["project_id"])
    enriched["claim_values"] = values
    enriched["claim_refs"] = refs
    return enriched
