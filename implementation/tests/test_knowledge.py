"""PostgreSQL acceptance tests for Document → Knowledge and offline editing."""

from __future__ import annotations

import uuid
from pathlib import Path

import pytest

from mvp_vertical import knowledge, store
from mvp_vertical.contract import TaskContract


@pytest.fixture
def conn():
    try:
        connection = store.connect()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL/pgvector unreachable: {exc}")
    yield connection
    connection.close()


def _source(conn, tmp_path: Path) -> tuple[str, list[str]]:
    suffix = uuid.uuid4().hex
    dossier = f"knowledge-{suffix}"
    source_ref = f"Projects/MAISON-A/30_DCE/MAISON-A_A1_DCE_IFJ_CCTP_LOT-06-{suffix}_2026-07-20.md"
    path = tmp_path / source_ref
    path.parent.mkdir(parents=True)
    path.write_text("# Façades\n\nLes reprises concernent le support existant.", encoding="utf-8")
    raw = {
        "object_type": "task_contract",
        "object_id": f"tc.{suffix}",
        "contract_id": f"tc.{suffix}",
        "scope": {
            "dossier": dossier,
            "parent_project_id": "project-maison-a",
            "declared_sources": [{"source_ref": source_ref}],
        },
    }
    contract = TaskContract(
        raw=raw, path=tmp_path / "task_contract.yaml", dossier=dossier, sources=(source_ref,)
    )
    assert store.ingest(conn, contract, tmp_path, ingestion_id=f"ingest-{suffix}") == 1
    card = store.get_document_card(conn, dossier, source_ref)
    assert card["extraction"]["observation_kind"] == "direct_text"
    extraction_id = card["extraction"]["extraction_id"]
    return card["document_id"], [f"chunk.{extraction_id}.0000"]


def _publish(conn, tmp_path: Path) -> tuple[dict, str]:
    document_id, refs = _source(conn, tmp_path)
    knowledge_id = f"knowledge.techniques.{uuid.uuid4().hex}"
    card = knowledge.publish_knowledge(
        conn,
        knowledge_id=knowledge_id,
        document_id=document_id,
        title="Reprise des façades existantes",
        family="techniques",
        markdown="# Reprise des façades\n\nPréparer le support existant.",
        source_chunk_refs=refs,
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=f"publish-{uuid.uuid4().hex}",
    )
    return card, document_id


def test_publish_is_schema_valid_unreviewed_and_without_authority(conn, tmp_path) -> None:
    card, _document_id = _publish(conn, tmp_path)

    assert card["review_status"] == "generated_unreviewed"
    assert card["version"] == 1
    assert card["authority"] == {
        "is_evidence": False,
        "is_memory": False,
        "is_doctrine": False,
    }
    snapshot = knowledge.validate_document_knowledge_slice(conn, card["knowledge_id"])
    assert snapshot["extraction"]["observation_kind"] == "direct_text"
    assert snapshot["document_card"]["parent_project_id"] == "project-maison-a"


def test_publish_replay_is_idempotent_and_key_content_is_immutable(conn, tmp_path) -> None:
    document_id, refs = _source(conn, tmp_path)
    knowledge_id = f"knowledge.methodologie.{uuid.uuid4().hex}"
    key = f"publish-{uuid.uuid4().hex}"
    arguments = dict(
        knowledge_id=knowledge_id,
        document_id=document_id,
        title="Préparation du support",
        family="methodologie",
        markdown="# Préparation\n\nNettoyer le support.",
        source_chunk_refs=refs,
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=key,
    )
    first = knowledge.publish_knowledge(conn, **arguments)
    assert knowledge.publish_knowledge(conn, **arguments) == first
    with conn.cursor() as cur:
        cur.execute("SELECT count(*) FROM knowledge_events WHERE aggregate_ref = %s", (knowledge_id,))
        assert cur.fetchone()[0] == 1

    with pytest.raises(knowledge.IdempotencyConflict):
        knowledge.publish_knowledge(conn, **{**arguments, "title": "Autre titre"})


def test_stale_revision_refuses_without_partial_effect(conn, tmp_path) -> None:
    card, _document_id = _publish(conn, tmp_path)
    knowledge_id = card["knowledge_id"]
    revised = knowledge.revise_knowledge(
        conn,
        knowledge_id=knowledge_id,
        markdown="# Reprise des façades\n\nPurger, nettoyer et préparer le support.",
        expected_version=1,
        actor="mobile-user",
        actor_kind="human",
        idempotency_key=f"revise-{uuid.uuid4().hex}",
    )
    assert revised["version"] == 2

    with pytest.raises(knowledge.StaleKnowledgeWrite):
        knowledge.revise_knowledge(
            conn,
            knowledge_id=knowledge_id,
            markdown="contenu obsolète",
            expected_version=1,
            actor="offline-mobile",
            actor_kind="human",
            idempotency_key=f"stale-{uuid.uuid4().hex}",
        )
    assert knowledge.get_knowledge_markdown(conn, knowledge_id).startswith("# Reprise")
    assert knowledge.get_knowledge_card(conn, knowledge_id)["version"] == 2


def test_selected_zone_request_waits_for_hermes_then_applies_exact_version(conn, tmp_path) -> None:
    card, _document_id = _publish(conn, tmp_path)
    knowledge_id = card["knowledge_id"]
    markdown = knowledge.get_knowledge_markdown(conn, knowledge_id)
    selected = "Préparer le support existant."
    start = markdown.index(selected)
    request_id = f"edit-{uuid.uuid4().hex}"

    request = knowledge.create_edit_request(
        conn,
        request_id=request_id,
        knowledge_id=knowledge_id,
        instruction_kind="expand",
        instruction="Détailler la préparation du support.",
        base_version=1,
        selection_start=start,
        selection_end=start + len(selected),
        selected_text=selected,
        requested_by="mobile-user",
        idempotency_key=f"request-{uuid.uuid4().hex}",
    )
    assert request["status"] == "queued_for_hermes"

    proposal = knowledge.complete_edit_request(
        conn,
        request_id=request_id,
        replacement_markdown="Purger les parties non adhérentes, dépoussiérer puis appliquer le primaire.",
    )
    assert proposal["status"] == "proposed"
    apply_key = f"apply-{uuid.uuid4().hex}"
    applied = knowledge.apply_edit_request(
        conn,
        request_id=request_id,
        actor="mobile-user",
        actor_kind="human",
        idempotency_key=apply_key,
    )
    assert applied["knowledge"]["version"] == 2
    assert applied["edit_request"]["status"] == "applied"
    assert "Purger les parties" in knowledge.get_knowledge_markdown(conn, knowledge_id)
    assert knowledge.apply_edit_request(
        conn,
        request_id=request_id,
        actor="mobile-user",
        actor_kind="human",
        idempotency_key=apply_key,
    ) == applied


def test_offline_edit_request_refuses_a_stale_base_version(conn, tmp_path) -> None:
    card, _document_id = _publish(conn, tmp_path)
    knowledge_id = card["knowledge_id"]
    original = knowledge.get_knowledge_markdown(conn, knowledge_id)
    knowledge.revise_knowledge(
        conn,
        knowledge_id=knowledge_id,
        markdown=original + "\n\nAjout synchronisé.",
        expected_version=1,
        actor="other-device",
        actor_kind="human",
        idempotency_key=f"revise-{uuid.uuid4().hex}",
    )

    with pytest.raises(knowledge.StaleKnowledgeWrite, match="current version is 2"):
        knowledge.create_edit_request(
            conn,
            request_id=f"edit-{uuid.uuid4().hex}",
            knowledge_id=knowledge_id,
            instruction_kind="rewrite",
            instruction="Reformuler.",
            base_version=1,
            selection_start=0,
            selection_end=1,
            selected_text="#",
            requested_by="offline-mobile",
            idempotency_key=f"request-{uuid.uuid4().hex}",
        )
