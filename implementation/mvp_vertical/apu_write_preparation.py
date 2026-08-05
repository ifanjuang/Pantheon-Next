"""Prepare and authorize bounded APU write commands without applying them."""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from . import apu_mapping_reviews, execution_results


MIGRATION = Path(__file__).resolve().parent / "sql" / "012_apu_write_preparation.sql"
COMMAND_AUTHORITY = {
    "is_fact": False,
    "is_evidence": False,
    "is_decision": False,
    "is_memory": False,
    "is_apu_write": False,
    "authorizes_external_effect": False,
}
AUTHORIZATION_ACTIONS = {"authorize_application", "reject_application"}


class ApuWritePreparationError(execution_results.ExecutionResultError):
    pass


class ApuWritePreparationNotFound(ApuWritePreparationError):
    pass


def _jsonable(value: Any) -> Any:
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    return value


def _digest(value: Any) -> str:
    rendered = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(rendered.encode("utf-8")).hexdigest()


def _required(value: Any, field: str) -> str:
    text = str(value or "").strip()
    if not text:
        raise ApuWritePreparationError(f"{field} is required")
    return text


def _stable_id(prefix: str, *parts: str) -> str:
    return f"{prefix}.{hashlib.sha256(chr(31).join(parts).encode()).hexdigest()[:24]}"


def _mapping(execution: dict[str, Any], result_ref: str, mapping_ref: str) -> tuple[dict[str, Any], dict[str, Any]]:
    result = next((item for item in execution.get("results", []) if item.get("result_id") == result_ref), None)
    if result is None or result.get("result_kind") != "apu_object_mapping":
        raise ApuWritePreparationNotFound("unknown APU mapping result")
    payload = result.get("payload") or {}
    mapping = next((item for item in payload.get("mappings", []) if item.get("mapping_id") == mapping_ref), None)
    if mapping is None:
        raise ApuWritePreparationNotFound("unknown APU mapping candidate")
    return payload, mapping


def _latest_selected_review(conn, *, execution_result_id: str, result_ref: str, mapping_ref: str) -> dict[str, Any]:
    reviews = apu_mapping_reviews.list_mapping_reviews(
        conn,
        execution_result_id=execution_result_id,
        result_ref=result_ref,
        mapping_ref=mapping_ref,
    )
    if not reviews or reviews[-1].get("action") != "select_existing_object":
        raise ApuWritePreparationError("latest mapping review must select_existing_object")
    return reviews[-1]


def prepare_write_command(
    conn,
    *,
    execution_result_id: str,
    result_ref: str,
    mapping_ref: str,
    prepared_by: str,
    idempotency_key: str,
) -> dict[str, Any]:
    key = _required(idempotency_key, "idempotency_key")
    actor = _required(prepared_by, "prepared_by")
    execution = execution_results.get_execution_result(conn, execution_result_id)
    payload, mapping = _mapping(execution, result_ref, mapping_ref)
    review = _latest_selected_review(
        conn,
        execution_result_id=execution_result_id,
        result_ref=result_ref,
        mapping_ref=mapping_ref,
    )
    target = _required(review.get("selected_stable_object_ref"), "selected_stable_object_ref")
    candidates = {item.get("stable_object_ref") for item in mapping.get("match_candidates", [])}
    if target not in candidates:
        raise ApuWritePreparationError("selected object is no longer present in mapping candidates")

    command_id = _stable_id("apu-write-command", execution_result_id, result_ref, mapping_ref, review["review_id"])
    command_payload = {
        "command_id": command_id,
        "operation": "add_match_to_existing_object",
        "project_ref": payload.get("project_ref"),
        "source_execution_result_ref": execution_result_id,
        "source_mapping_result_ref": result_ref,
        "source_mapping_ref": mapping_ref,
        "source_review_ref": review["review_id"],
        "target_stable_object_ref": target,
        "source_candidate_ref": _required(mapping.get("candidate_object_ref"), "candidate_object_ref"),
        "source_artifact_ref": payload.get("document_ref"),
        "certainty": mapping.get("certainty"),
        "rationale": _required(mapping.get("rationale"), "mapping.rationale"),
        "prepared_by": actor,
        "limitations": ["Une autorisation humaine distincte est requise avant toute application."],
        "authority": dict(COMMAND_AUTHORITY),
    }
    command_payload = {k: v for k, v in command_payload.items() if v is not None}
    digest = _digest(command_payload)
    command_payload["payload_digest"] = digest

    with conn.transaction():
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM apu_write_command_candidates WHERE idempotency_key = %s", (key,))
            replay = cur.fetchone()
            if replay is not None:
                if replay["payload_digest"] != digest:
                    raise execution_results.ExecutionResultConflict("write-command idempotency key belongs to different content")
                return _jsonable(dict(replay)) | {"command": replay["command_payload"], "authority": dict(COMMAND_AUTHORITY)}
        conn.execute(
            """INSERT INTO apu_write_command_candidates (
                command_id, execution_result_id, result_ref, mapping_ref, source_review_ref,
                operation, project_ref, target_stable_object_ref, source_candidate_ref,
                source_artifact_ref, certainty, rationale, command_payload, payload_digest,
                prepared_by, idempotency_key
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (command_id, execution_result_id, result_ref, mapping_ref, review["review_id"],
             "add_match_to_existing_object", payload.get("project_ref"), target,
             mapping["candidate_object_ref"], payload.get("document_ref"), mapping.get("certainty"),
             mapping["rationale"], Jsonb(command_payload), digest, actor, key),
        )
    return get_write_command(conn, command_id)


def get_write_command(conn, command_id: str) -> dict[str, Any]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM apu_write_command_candidates WHERE command_id = %s", (command_id,))
        row = cur.fetchone()
    if row is None:
        raise ApuWritePreparationNotFound(f"unknown APU write command: {command_id}")
    return _jsonable(dict(row)) | {"command": _jsonable(row["command_payload"]), "authority": dict(COMMAND_AUTHORITY)}


def append_authorization(
    conn,
    *,
    command_id: str,
    action: str,
    note: str | None,
    authorized_by: str,
    idempotency_key: str,
) -> dict[str, Any]:
    if action not in AUTHORIZATION_ACTIONS:
        raise ApuWritePreparationError("unsupported authorization action")
    key = _required(idempotency_key, "idempotency_key")
    actor = _required(authorized_by, "authorized_by")
    command = get_write_command(conn, command_id)
    digest = command["payload_digest"]
    payload = {"command_ref": command_id, "command_payload_digest": digest, "action": action, "note": (note or "").strip() or None, "authorized_by": actor}
    payload_digest = _digest(payload)
    with conn.transaction():
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT * FROM apu_write_authorization_events WHERE idempotency_key = %s", (key,))
            replay = cur.fetchone()
            if replay is not None:
                if replay["payload_digest"] != payload_digest:
                    raise execution_results.ExecutionResultConflict("write-authorization idempotency key belongs to different content")
                return _jsonable(dict(replay)) | {"authority": _authorization_authority(replay["action"])}
        authorization_id = _stable_id("apu-write-authorization", command_id, key)
        conn.execute(
            """INSERT INTO apu_write_authorization_events (
                authorization_id, command_ref, command_payload_digest, action, note,
                authorized_by, idempotency_key, payload_digest
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (authorization_id, command_id, digest, action, payload["note"], actor, key, payload_digest),
        )
    return get_authorization(conn, authorization_id)


def _authorization_authority(action: str) -> dict[str, bool]:
    return {"authorizes_command_application": action == "authorize_application", "applies_command": False, "confirms_stable_identity": False, "admits_evidence": False, "promotes_memory": False}


def get_authorization(conn, authorization_id: str) -> dict[str, Any]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM apu_write_authorization_events WHERE authorization_id = %s", (authorization_id,))
        row = cur.fetchone()
    if row is None:
        raise ApuWritePreparationNotFound(f"unknown APU write authorization: {authorization_id}")
    return _jsonable(dict(row)) | {"authority": _authorization_authority(row["action"])}


def list_authorizations(conn, command_id: str) -> list[dict[str, Any]]:
    get_write_command(conn, command_id)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM apu_write_authorization_events WHERE command_ref = %s ORDER BY authorized_at, authorization_id", (command_id,))
        rows = cur.fetchall()
    return [_jsonable(dict(row)) | {"authority": _authorization_authority(row["action"])} for row in rows]
