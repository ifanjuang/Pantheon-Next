"""Immutable storage for exact Cockpit -> Hermes handoff contract snapshots.

Submitting a handoff creates a Work Issue assigned to Hermes. It does not start
an Hermes run. The persisted Task Contract / Context Pack remain candidate
snapshots external to Pantheon's canonical governance records.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from pathlib import Path
from typing import Any

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from . import card_scope, work_issue_read, work_issues

MIGRATION = Path(__file__).resolve().parent / "sql" / "003_hermes_handoff_contracts.sql"


class HandoffSubmissionError(ValueError):
    pass


class HandoffIdempotencyConflict(HandoffSubmissionError):
    pass


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _existing_by_idempotency(conn: psycopg.Connection, idempotency_key: str) -> dict | None:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM cockpit_hermes_handoffs WHERE idempotency_key = %s",
            (idempotency_key,),
        )
        row = cur.fetchone()
    return dict(row) if row else None


def _result_from_row(conn: psycopg.Connection, row: dict) -> dict:
    issue = work_issue_read.get_issue_record(conn, row["work_issue_id"])
    return {
        "handoff_id": row["handoff_id"],
        "case_ref": row["case_ref"],
        "task_contract_ref": row["task_contract_ref"],
        "context_pack_ref": row["context_pack_ref"],
        "preview_digest": row["preview_digest"],
        "work_issue": issue,
        "execution_started": False,
        "hermes_run_created": False,
        "status": "submitted_work_issue",
    }


def submit_handoff(
    conn: psycopg.Connection,
    *,
    actor: str,
    idempotency_key: str,
    question: str,
    preview: dict,
    card_context_envelope: dict,
    selected_context: list[dict],
    include_declared_descendants: bool,
) -> dict:
    if not actor or not actor.strip():
        raise HandoffSubmissionError("human actor is required")
    if len(idempotency_key.strip()) < 8:
        raise HandoffSubmissionError("idempotency_key must contain at least 8 characters")
    if preview.get("execution_authorized") is not False:
        raise HandoffSubmissionError("handoff preview must remain execution_authorized=false")
    if preview.get("requested_effect") != "read_only":
        raise HandoffSubmissionError("this handoff submission slice accepts read_only effect only")

    root = card_context_envelope.get("root_entity") or {}
    request_record = {
        "question": question.strip(),
        "preview_digest": preview["preview_digest"],
        "task_contract_ref": preview["task_contract"]["task_contract_ref"],
        "context_pack_ref": preview["context_pack"]["context_pack_ref"],
        "card_context_envelope": card_context_envelope,
        "selected_context": selected_context,
        "include_declared_descendants": bool(include_declared_descendants),
        "actor": actor.strip(),
    }
    request_digest = _digest(request_record)

    # Important transaction boundary: resolve_case_ref() performs owner reads. It
    # must happen inside the same explicit transaction as the handoff write rather
    # than starting an implicit outer transaction before conn.transaction().
    with conn.transaction():
        case_ref = card_scope.resolve_case_ref(conn, root_entity=root)
        existing = _existing_by_idempotency(conn, idempotency_key)
        if existing is not None:
            if existing["request_digest"] != request_digest:
                raise HandoffIdempotencyConflict(
                    "idempotency key already belongs to another Hermes handoff submission"
                )
            return _result_from_row(conn, existing)

        issue_id = f"work-{uuid.uuid4().hex}"
        handoff_id = f"handoff-{uuid.uuid4().hex}"
        title_seed = question.strip().replace("\n", " ")
        title = f"Hermes · {title_seed[:140]}" if title_seed else "Hermes · question Cockpit"
        work_issues.create_issue(
            conn,
            issue_id=issue_id,
            case_ref=case_ref,
            title=title,
            description=question.strip(),
            priority="normal",
            requested_effect="read_only",
            assigned_to="hermes",
            task_contract_ref=preview["task_contract"]["task_contract_ref"],
            context_pack_ref=preview["context_pack"]["context_pack_ref"],
            created_by=actor.strip(),
            idempotency_key=f"{idempotency_key}:work-issue",
        )
        issue = work_issue_read.get_issue_record(conn, issue_id)
        conn.execute(
            """
            INSERT INTO cockpit_hermes_handoffs (
                handoff_id, work_issue_id, case_ref,
                root_entity_id, root_entity_type, question, requested_effect,
                task_contract_ref, context_pack_ref, preview_digest,
                request_digest, task_contract, context_pack, selected_context,
                include_declared_descendants, idempotency_key, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, 'read_only', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                handoff_id,
                issue_id,
                case_ref,
                root["entity_id"],
                root["entity_type"],
                question.strip(),
                preview["task_contract"]["task_contract_ref"],
                preview["context_pack"]["context_pack_ref"],
                preview["preview_digest"],
                request_digest,
                Jsonb(preview["task_contract"]),
                Jsonb(preview["context_pack"]),
                Jsonb(selected_context),
                bool(include_declared_descendants),
                idempotency_key,
                actor.strip(),
            ),
        )
        return {
            "handoff_id": handoff_id,
            "case_ref": case_ref,
            "task_contract_ref": preview["task_contract"]["task_contract_ref"],
            "context_pack_ref": preview["context_pack"]["context_pack_ref"],
            "preview_digest": preview["preview_digest"],
            "work_issue": issue,
            "execution_started": False,
            "hermes_run_created": False,
            "status": "submitted_work_issue",
        }
