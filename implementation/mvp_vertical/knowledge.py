"""Transactional Document → Knowledge and offline-edit adapter.

Knowledge is reusable editorial Markdown. It is never Evidence, governed
memory, doctrine, or a replacement for the NAS original. All material writes
use exact optimistic versions and immutable idempotency keys.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

import jsonschema
import psycopg
import yaml
from psycopg.rows import dict_row


SCHEMA = Path(__file__).resolve().parent / "vendor" / "pantheon" / "document_knowledge_slice.schema.yaml"
FAMILIES = {"referentiels", "responsabilite", "methodologie", "techniques", "reglementations"}
REVIEW_STATUSES = {"generated_unreviewed", "needs_review", "reviewed", "superseded"}
INSTRUCTION_KINDS = {"rewrite", "expand", "simplify", "verify", "move_to_lot"}
ACTOR_KINDS = {"human", "hermes", "system"}


class KnowledgeError(ValueError):
    """Base refusal for the bounded Knowledge adapter."""


class KnowledgeNotFound(KnowledgeError):
    pass


class StaleKnowledgeWrite(KnowledgeError):
    pass


class IdempotencyConflict(KnowledgeError):
    pass


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _payload_digest(value: dict[str, Any]) -> str:
    canonical = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return _digest(canonical)


def _iso(value: datetime | None) -> str | None:
    return value.isoformat() if value is not None else None


def _knowledge_row(conn: psycopg.Connection, knowledge_id: str, *, lock: bool = False) -> dict:
    suffix = " FOR UPDATE" if lock else ""
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(f"SELECT * FROM knowledge_items WHERE knowledge_id = %s{suffix}", (knowledge_id,))
        row = cur.fetchone()
    if row is None:
        raise KnowledgeNotFound(f"unknown Knowledge item: {knowledge_id}")
    return dict(row)


def _document_row(conn: psycopg.Connection, document_id: str) -> dict:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT d.*, e.extraction_id, e.converter, e.converter_version, e.config_digest,
                   e.status AS extraction_status, e.quality_flags, e.error,
                   e.created_at AS extraction_created_at, o.observation_kind,
                   (SELECT MAX(v.version) FROM document_versions v
                     WHERE v.document_id = d.document_id) AS source_version
              FROM source_documents d
              LEFT JOIN extraction_runs e ON e.extraction_id = d.current_extraction_id
              LEFT JOIN extraction_observations o ON o.extraction_id = e.extraction_id
             WHERE d.document_id = %s
            """,
            (document_id,),
        )
        row = cur.fetchone()
    if row is None:
        raise KnowledgeNotFound(f"unknown source document: {document_id}")
    return dict(row)


def _chunk_refs(conn: psycopg.Connection, document: dict) -> list[str]:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT chunk_no FROM chunks WHERE dossier = %s AND source_ref = %s ORDER BY chunk_no",
            (document["dossier"], document["source_ref"]),
        )
        return [f"chunk.{document['extraction_id']}.{row[0]:04d}" for row in cur.fetchall()]


def _event_replay(
    conn: psycopg.Connection,
    *,
    idempotency_key: str,
    aggregate_ref: str,
    payload_digest: str,
) -> dict | None:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT aggregate_ref, payload_digest, result_snapshot FROM knowledge_events "
            "WHERE idempotency_key = %s",
            (idempotency_key,),
        )
        row = cur.fetchone()
    if row is None:
        return None
    if row["aggregate_ref"] != aggregate_ref or row["payload_digest"] != payload_digest:
        raise IdempotencyConflict("idempotency key already belongs to a different immutable effect")
    return row["result_snapshot"]


def _card_from_row(conn: psycopg.Connection, row: dict) -> dict:
    document = _document_row(conn, row["document_id"])
    refs = row["source_chunk_refs"]
    return {
        "card_type": "knowledge",
        "card_id": f"card-{row['knowledge_id']}",
        "knowledge_id": row["knowledge_id"],
        "document_ref": row["document_id"],
        "parent_project_id": document["parent_project_id"],
        "title": row["title"],
        "family": row["family"],
        "markdown_digest": row["markdown_digest"],
        "source_chunk_refs": list(refs),
        "review_status": row["review_status"],
        "version": row["version"],
        "created_by": row["created_by"],
        "created_at": _iso(row["created_at"]),
        "updated_at": _iso(row["updated_at"]),
        "authority": {"is_evidence": False, "is_memory": False, "is_doctrine": False},
    }


def get_knowledge_card(conn: psycopg.Connection, knowledge_id: str) -> dict:
    return _card_from_row(conn, _knowledge_row(conn, knowledge_id))


def get_knowledge_markdown(conn: psycopg.Connection, knowledge_id: str) -> str:
    return str(_knowledge_row(conn, knowledge_id)["markdown"])


def list_knowledge_cards(conn: psycopg.Connection, parent_project_id: str) -> list[dict]:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT k.* FROM knowledge_items k
            JOIN source_documents d ON d.document_id = k.document_id
            WHERE d.parent_project_id = %s
            ORDER BY k.updated_at DESC, k.knowledge_id
            """,
            (parent_project_id,),
        )
        rows = [dict(row) for row in cur.fetchall()]
    return [_card_from_row(conn, row) for row in rows]


def _insert_event(
    conn: psycopg.Connection,
    *,
    aggregate_ref: str,
    event_type: str,
    actor: str,
    actor_kind: str,
    expected_version: int,
    idempotency_key: str,
    payload_digest: str,
    snapshot: dict,
) -> None:
    conn.execute(
        """
        INSERT INTO knowledge_events (
            event_id, aggregate_ref, event_type, actor, actor_kind,
            expected_version, resulting_version, idempotency_key,
            payload_digest, result_snapshot
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb)
        """,
        (
            f"event-{uuid.uuid4().hex}", aggregate_ref, event_type, actor, actor_kind,
            expected_version, expected_version + 1, idempotency_key,
            payload_digest, json.dumps(snapshot, ensure_ascii=False),
        ),
    )


def publish_knowledge(
    conn: psycopg.Connection,
    *,
    knowledge_id: str,
    document_id: str,
    title: str,
    family: str,
    markdown: str,
    source_chunk_refs: list[str],
    created_by: str,
    actor_kind: str,
    idempotency_key: str,
    expected_version: int = 0,
    review_status: str = "generated_unreviewed",
) -> dict:
    if expected_version != 0:
        raise StaleKnowledgeWrite("first publication requires expected_version 0")
    if not title.strip() or not markdown.strip() or not knowledge_id:
        raise KnowledgeError("knowledge_id, title and Markdown are required")
    if family not in FAMILIES or review_status not in REVIEW_STATUSES or actor_kind not in ACTOR_KINDS:
        raise KnowledgeError("invalid Knowledge family, review status or actor kind")
    payload = {
        "knowledge_id": knowledge_id, "document_id": document_id, "title": title,
        "family": family, "markdown": markdown, "source_chunk_refs": source_chunk_refs,
        "created_by": created_by, "actor_kind": actor_kind, "review_status": review_status,
        "expected_version": expected_version,
    }
    pdigest = _payload_digest(payload)
    with conn.transaction():
        replay = _event_replay(
            conn, idempotency_key=idempotency_key, aggregate_ref=knowledge_id, payload_digest=pdigest
        )
        if replay is not None:
            return replay
        document = _document_row(conn, document_id)
        current_refs = set(_chunk_refs(conn, document))
        if not source_chunk_refs or not set(source_chunk_refs).issubset(current_refs):
            raise KnowledgeError("Knowledge must cite one or more current chunks from its source document")
        with conn.cursor() as cur:
            cur.execute("SELECT 1 FROM knowledge_items WHERE knowledge_id = %s", (knowledge_id,))
            if cur.fetchone() is not None:
                raise IdempotencyConflict(
                    "Knowledge identity already exists; retry the original immutable idempotency key"
                )
        conn.execute(
            """
            INSERT INTO knowledge_items (
                knowledge_id, document_id, source_version, source_digest, extraction_id,
                title, family, markdown, markdown_digest,
                source_chunk_refs, review_status, version, created_by
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s, 1, %s)
            """,
            (
                knowledge_id, document_id, document["source_version"],
                document["source_digest"], document["extraction_id"],
                title.strip(), family, markdown, _digest(markdown),
                json.dumps(source_chunk_refs), review_status, created_by,
            ),
        )
        with conn.cursor() as cur:
            cur.execute(
                "SELECT chunk_no, body FROM chunks WHERE dossier = %s AND source_ref = %s",
                (document["dossier"], document["source_ref"]),
            )
            chunks = {f"chunk.{document['extraction_id']}.{number:04d}": (number, body) for number, body in cur.fetchall()}
        for chunk_ref in source_chunk_refs:
            ordinal, body = chunks[chunk_ref]
            conn.execute(
                """
                INSERT INTO knowledge_source_chunks (
                    knowledge_id, chunk_ref, document_id, extraction_id, ordinal,
                    text_digest, source_ref, source_digest, structural_locator
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    knowledge_id, chunk_ref, document_id, document["extraction_id"], ordinal,
                    _digest(body), document["source_ref"], document["source_digest"],
                    f"chunk/{ordinal}",
                ),
            )
        snapshot = get_knowledge_card(conn, knowledge_id)
        _insert_event(
            conn, aggregate_ref=knowledge_id, event_type="knowledge_published",
            actor=created_by, actor_kind=actor_kind, expected_version=0,
            idempotency_key=idempotency_key, payload_digest=pdigest, snapshot=snapshot,
        )
        validate_document_knowledge_slice(conn, knowledge_id)
    return snapshot


def revise_knowledge(
    conn: psycopg.Connection,
    *,
    knowledge_id: str,
    markdown: str,
    expected_version: int,
    actor: str,
    actor_kind: str,
    idempotency_key: str,
    review_status: str | None = None,
) -> dict:
    if not markdown.strip() or actor_kind not in ACTOR_KINDS:
        raise KnowledgeError("non-empty Markdown and a valid actor kind are required")
    if review_status is not None and review_status not in REVIEW_STATUSES:
        raise KnowledgeError("invalid Knowledge review status")
    payload = {
        "knowledge_id": knowledge_id, "markdown": markdown,
        "expected_version": expected_version, "actor": actor, "actor_kind": actor_kind,
        "review_status": review_status,
    }
    pdigest = _payload_digest(payload)
    with conn.transaction():
        replay = _event_replay(
            conn, idempotency_key=idempotency_key, aggregate_ref=knowledge_id, payload_digest=pdigest
        )
        if replay is not None:
            return replay
        row = _knowledge_row(conn, knowledge_id, lock=True)
        if row["version"] != expected_version:
            raise StaleKnowledgeWrite(
                f"stale Knowledge version: expected {expected_version}, current {row['version']}"
            )
        next_status = review_status or row["review_status"]
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE knowledge_items
                   SET markdown = %s, markdown_digest = %s, review_status = %s,
                       version = version + 1, updated_at = CURRENT_TIMESTAMP
                 WHERE knowledge_id = %s AND version = %s
                """,
                (markdown, _digest(markdown), next_status, knowledge_id, expected_version),
            )
            if cur.rowcount != 1:
                raise StaleKnowledgeWrite("Knowledge changed before the revision was persisted")
        snapshot = get_knowledge_card(conn, knowledge_id)
        event_type = (
            "knowledge_review_status_changed"
            if markdown == row["markdown"] and next_status != row["review_status"]
            else "knowledge_revised"
        )
        _insert_event(
            conn, aggregate_ref=knowledge_id, event_type=event_type,
            actor=actor, actor_kind=actor_kind, expected_version=expected_version,
            idempotency_key=idempotency_key, payload_digest=pdigest, snapshot=snapshot,
        )
        validate_document_knowledge_slice(conn, knowledge_id)
    return snapshot


def create_edit_request(
    conn: psycopg.Connection,
    *,
    request_id: str,
    knowledge_id: str,
    instruction_kind: str,
    instruction: str,
    base_version: int,
    selection_start: int,
    selection_end: int,
    selected_text: str,
    requested_by: str,
    idempotency_key: str,
    replacement_markdown: str | None = None,
) -> dict:
    if instruction_kind not in INSTRUCTION_KINDS or not instruction.strip():
        raise KnowledgeError("invalid or empty intelligent-edit instruction")
    payload = {
        "request_id": request_id, "knowledge_id": knowledge_id,
        "instruction_kind": instruction_kind, "instruction": instruction,
        "base_version": base_version, "selection_start": selection_start,
        "selection_end": selection_end, "selected_text": selected_text,
        "requested_by": requested_by, "replacement_markdown": replacement_markdown,
    }
    pdigest = _payload_digest(payload)
    with conn.transaction():
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT request_payload_digest FROM knowledge_edit_requests "
                "WHERE request_idempotency_key = %s",
                (idempotency_key,),
            )
            replay = cur.fetchone()
        if replay is not None:
            if replay["request_payload_digest"] != pdigest:
                raise IdempotencyConflict("edit request idempotency key has different content")
            return get_edit_request(conn, request_id)
        item = _knowledge_row(conn, knowledge_id, lock=True)
        if item["version"] != base_version:
            raise StaleKnowledgeWrite(
                f"offline edit is based on version {base_version}; current version is {item['version']}"
            )
        markdown = item["markdown"]
        if selection_start < 0 or selection_end < selection_start or selection_end > len(markdown):
            raise KnowledgeError("selection range is outside the Markdown snapshot")
        if markdown[selection_start:selection_end] != selected_text:
            raise StaleKnowledgeWrite("selected text no longer matches the declared base snapshot")
        status = "proposed" if replacement_markdown is not None else "queued_for_hermes"
        conn.execute(
            """
            INSERT INTO knowledge_edit_requests (
                request_id, knowledge_id, instruction_kind, instruction, base_version,
                selection_start, selection_end, selected_text_digest,
                replacement_markdown, status, requested_by,
                request_idempotency_key, request_payload_digest
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                request_id, knowledge_id, instruction_kind, instruction, base_version,
                selection_start, selection_end, _digest(selected_text), replacement_markdown,
                status, requested_by, idempotency_key, pdigest,
            ),
        )
    return get_edit_request(conn, request_id)


def get_edit_request(conn: psycopg.Connection, request_id: str) -> dict:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM knowledge_edit_requests WHERE request_id = %s", (request_id,))
        row = cur.fetchone()
    if row is None:
        raise KnowledgeNotFound(f"unknown intelligent edit request: {request_id}")
    result = dict(row)
    for key in ("created_at", "updated_at"):
        result[key] = _iso(result[key])
    return result


def list_edit_requests(
    conn: psycopg.Connection,
    *,
    status: str = "queued_for_hermes",
    limit: int = 100,
) -> list[dict]:
    if status not in {"queued_for_hermes", "proposed", "applied", "conflict", "rejected"}:
        raise KnowledgeError("invalid intelligent edit request status")
    if limit < 1 or limit > 500:
        raise KnowledgeError("edit request limit must be between 1 and 500")
    with conn.cursor() as cur:
        cur.execute(
            "SELECT request_id FROM knowledge_edit_requests WHERE status = %s "
            "ORDER BY created_at ASC LIMIT %s",
            (status, limit),
        )
        request_ids = [row[0] for row in cur.fetchall()]
    return [get_edit_request(conn, request_id) for request_id in request_ids]


def complete_edit_request(
    conn: psycopg.Connection, *, request_id: str, replacement_markdown: str
) -> dict:
    if not replacement_markdown:
        raise KnowledgeError("Hermes proposal must contain replacement Markdown")
    with conn.transaction():
        request = get_edit_request(conn, request_id)
        item = _knowledge_row(conn, request["knowledge_id"], lock=True)
        status = "proposed" if item["version"] == request["base_version"] else "conflict"
        conn.execute(
            "UPDATE knowledge_edit_requests SET replacement_markdown = %s, status = %s, "
            "updated_at = CURRENT_TIMESTAMP WHERE request_id = %s",
            (replacement_markdown, status, request_id),
        )
    return get_edit_request(conn, request_id)


def apply_edit_request(
    conn: psycopg.Connection,
    *,
    request_id: str,
    actor: str,
    actor_kind: str,
    idempotency_key: str,
) -> dict:
    request = get_edit_request(conn, request_id)
    apply_payload_digest = _payload_digest(
        {
            "request_id": request_id,
            "actor": actor,
            "actor_kind": actor_kind,
            "idempotency_key": idempotency_key,
        }
    )
    if request["status"] == "applied":
        if (
            request["apply_idempotency_key"] != idempotency_key
            or request["apply_payload_digest"] != apply_payload_digest
        ):
            raise IdempotencyConflict("edit request was already applied by a different effect")
        return request["apply_result_snapshot"]
    if request["status"] == "conflict":
        raise StaleKnowledgeWrite("edit request already conflicts with a newer Knowledge version")
    if request["status"] != "proposed" or request["replacement_markdown"] is None:
        raise KnowledgeError("edit request has no applicable Hermes proposal")
    item = _knowledge_row(conn, request["knowledge_id"])
    start, end = request["selection_start"], request["selection_end"]
    selected = item["markdown"][start:end]
    if item["version"] != request["base_version"] or _digest(selected) != request["selected_text_digest"]:
        conn.commit()
        with conn.transaction():
            conn.execute(
                "UPDATE knowledge_edit_requests SET status = 'conflict', "
                "updated_at = CURRENT_TIMESTAMP WHERE request_id = %s",
                (request_id,),
            )
        raise StaleKnowledgeWrite("Knowledge changed after the intelligent edit was proposed")
    revised = item["markdown"][:start] + request["replacement_markdown"] + item["markdown"][end:]
    conn.commit()
    snapshot = revise_knowledge(
        conn, knowledge_id=request["knowledge_id"], markdown=revised,
        expected_version=request["base_version"], actor=actor,
        actor_kind=actor_kind, idempotency_key=idempotency_key,
    )
    with conn.transaction():
        result = {"knowledge": snapshot, "edit_request": None}
        conn.execute(
            "UPDATE knowledge_edit_requests SET status = 'applied', applied_version = %s, "
            "apply_idempotency_key = %s, apply_payload_digest = %s, "
            "apply_result_snapshot = %s::jsonb, "
            "updated_at = CURRENT_TIMESTAMP WHERE request_id = %s",
            (
                snapshot["version"], idempotency_key, apply_payload_digest,
                json.dumps({"knowledge": snapshot}, ensure_ascii=False), request_id,
            ),
        )
    current_request = get_edit_request(conn, request_id)
    result = {"knowledge": snapshot, "edit_request": current_request}
    conn.commit()
    with conn.transaction():
        conn.execute(
            "UPDATE knowledge_edit_requests SET apply_result_snapshot = %s::jsonb "
            "WHERE request_id = %s",
            (json.dumps(result, ensure_ascii=False), request_id),
        )
    return result


def _schema() -> dict:
    value = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise KnowledgeError("vendored Document → Knowledge schema is invalid")
    return value


def build_document_knowledge_slice(conn: psycopg.Connection, knowledge_id: str) -> dict:
    item = _knowledge_row(conn, knowledge_id)
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            """
            SELECT d.document_id, d.parent_project_id, v.source_ref, v.source_digest,
                   v.media_type, v.byte_size, d.created_at,
                   v.created_at AS version_created_at,
                   e.extraction_id, e.converter, e.converter_version, e.config_digest,
                   e.status AS extraction_status, e.quality_flags, e.error,
                   e.created_at AS extraction_created_at, o.observation_kind
              FROM source_documents d
              JOIN document_versions v ON v.document_id = d.document_id AND v.version = %s
              JOIN extraction_runs e ON e.extraction_id = %s AND e.document_id = d.document_id
              LEFT JOIN extraction_observations o ON o.extraction_id = e.extraction_id
             WHERE d.document_id = %s AND v.source_digest = %s
            """,
            (
                item["source_version"], item["extraction_id"],
                item["document_id"], item["source_digest"],
            ),
        )
        row = cur.fetchone()
    if row is None:
        raise KnowledgeError("Knowledge source snapshot is no longer internally consistent")
    document = dict(row)
    document["source_version"] = item["source_version"]
    document["analysis_status"] = document["extraction_status"]
    if not document["observation_kind"]:
        raise KnowledgeError("source document lacks a complete extraction observation or version")
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT * FROM knowledge_source_chunks WHERE knowledge_id = %s ORDER BY ordinal",
            (knowledge_id,),
        )
        chunk_rows = [dict(row) for row in cur.fetchall()]
        cur.execute(
            "SELECT * FROM knowledge_events WHERE aggregate_ref = %s ORDER BY occurred_at, event_id",
            (knowledge_id,),
        )
        event_rows = [dict(row) for row in cur.fetchall()]
    card = _card_from_row(conn, item)
    return {
        "source_document": {
            "document_id": document["document_id"],
            "parent_project_id": document["parent_project_id"],
            "source_ref": document["source_ref"],
            "source_digest": document["source_digest"],
            "media_type": document["media_type"],
            "byte_size": document["byte_size"],
            "analysis_status": document["analysis_status"],
            "version": document["source_version"],
            "created_at": _iso(document["created_at"]),
            "updated_at": _iso(document["version_created_at"]),
        },
        "extraction": {
            "extraction_id": document["extraction_id"],
            "document_ref": document["document_id"],
            "source_digest": document["source_digest"],
            "converter": document["converter"],
            "converter_version": document["converter_version"],
            "config_digest": document["config_digest"],
            "observation_kind": document["observation_kind"],
            "status": document["extraction_status"],
            "quality_flags": document["quality_flags"] or [],
            "created_at": _iso(document["extraction_created_at"]),
            **({"error": document["error"]} if document["error"] else {}),
        },
        "chunks": [
            {
                "chunk_id": chunk["chunk_ref"],
                "document_ref": chunk["document_id"],
                "extraction_ref": chunk["extraction_id"],
                "ordinal": chunk["ordinal"],
                "text_digest": chunk["text_digest"],
                "provenance": {
                    "source_ref": chunk["source_ref"],
                    "source_digest": chunk["source_digest"],
                    "extraction_ref": chunk["extraction_id"],
                    "structural_locator": chunk["structural_locator"],
                },
            }
            for chunk in chunk_rows
        ],
        "document_card": {
            "card_id": f"card-{document['document_id']}",
            "document_ref": document["document_id"],
            "parent_project_id": document["parent_project_id"],
            "source_ref": document["source_ref"],
            "title": Path(document["source_ref"]).name,
            "analysis_status": document["analysis_status"],
            "source_version": document["source_version"],
            "authority": {"is_source": False, "is_evidence": False, "is_memory": False},
        },
        "knowledge_publications": [
            {
                "knowledge_id": card["knowledge_id"],
                "document_ref": card["document_ref"],
                "title": card["title"],
                "family": card["family"],
                "markdown_digest": card["markdown_digest"],
                "source_chunk_refs": card["source_chunk_refs"],
                "review_status": card["review_status"],
                "version": card["version"],
                "created_by": card["created_by"],
                "created_at": card["created_at"],
                "updated_at": card["updated_at"],
                "authority": card["authority"],
            }
        ],
        "events": [
            {
                "event_id": event["event_id"],
                "aggregate_kind": event["aggregate_kind"],
                "aggregate_ref": event["aggregate_ref"],
                "event_type": event["event_type"],
                "actor": event["actor"],
                "actor_kind": event["actor_kind"],
                "expected_version": event["expected_version"],
                "resulting_version": event["resulting_version"],
                "idempotency_key": event["idempotency_key"],
                "occurred_at": _iso(event["occurred_at"]),
            }
            for event in event_rows
        ],
        "governance_refs": [
            "docs/governance/DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md",
            "docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md",
        ],
    }


def validate_document_knowledge_slice(conn: psycopg.Connection, knowledge_id: str) -> dict:
    snapshot = build_document_knowledge_slice(conn, knowledge_id)
    try:
        jsonschema.Draft202012Validator(
            _schema(), format_checker=jsonschema.FormatChecker()
        ).validate(snapshot)
    except jsonschema.ValidationError as exc:
        raise KnowledgeError(f"Document → Knowledge contract refusal: {exc.message}") from exc
    return snapshot
