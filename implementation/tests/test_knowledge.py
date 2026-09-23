"""PostgreSQL acceptance tests for Document → Knowledge and offline editing."""

from __future__ import annotations

import uuid
from pathlib import Path

import pytest

from mvp_vertical import knowledge, store
from mvp_vertical.contract import TaskContract
from mvp_vertical.policy_gate import StandInPolicyClient


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
    compilation_id = card["structured_extraction"]["compilation_id"]
    return card["document_id"], [f"chunk.{compilation_id}.0000"]


def _multi_source_fixture(
    conn,
    tmp_path: Path,
    *,
    parent_project_id: str = "project-maison-a",
) -> tuple[TaskContract, dict[str, dict]]:
    suffix = uuid.uuid4().hex
    dossier = f"knowledge-multi-{suffix}"
    source_refs = (
        f"Projects/MULTI/30_DCE/CCTP-{suffix}.md",
        f"Projects/MULTI/50_CHANTIER/CR-{suffix}.md",
    )
    contents = (
        "# CCTP\n\nLa façade reçoit un enduit minéral.",
        "# CR chantier\n\nLe support existant nécessite une reprise locale.",
    )
    for source_ref, body in zip(source_refs, contents, strict=True):
        path = tmp_path / source_ref
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    raw = {
        "object_type": "task_contract",
        "object_id": f"tc.multi.{suffix}",
        "contract_id": f"tc.multi.{suffix}",
        "scope": {
            "dossier": dossier,
            "parent_project_id": parent_project_id,
            "declared_sources": [{"source_ref": source_ref} for source_ref in source_refs],
        },
    }
    contract = TaskContract(
        raw=raw,
        path=tmp_path / f"task_contract-{suffix}.yaml",
        dossier=dossier,
        sources=source_refs,
    )
    assert store.ingest(
        conn, contract, tmp_path, ingestion_id=f"ingest-multi-{suffix}"
    ) == 2

    sources: dict[str, dict] = {}
    for source_ref in source_refs:
        card = store.get_document_card(conn, dossier, source_ref)
        compilation_id = card["structured_extraction"]["compilation_id"]
        sources[source_ref] = {
            "path": tmp_path / source_ref,
            "document_id": card["document_id"],
            "chunk_ref": f"chunk.{compilation_id}.0000",
        }
    return contract, sources


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
    assert snapshot["chunks"][0]["provenance"]["structural_locator"] == "markdown:block-1"


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


def test_publish_can_bind_current_chunks_from_multiple_same_project_documents(
    conn, tmp_path
) -> None:
    _contract, sources = _multi_source_fixture(conn, tmp_path)
    primary, supporting = list(sources.values())
    knowledge_id = f"knowledge.techniques.{uuid.uuid4().hex}"

    card = knowledge.publish_knowledge(
        conn,
        knowledge_id=knowledge_id,
        document_id=primary["document_id"],
        title="Synthèse façade multi-source",
        family="techniques",
        markdown="# Façade\n\nSynthèse du CCTP et du compte-rendu.",
        source_chunk_refs=[primary["chunk_ref"], supporting["chunk_ref"]],
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=f"publish-{uuid.uuid4().hex}",
    )

    assert card["source_chunk_refs"] == [
        primary["chunk_ref"],
        supporting["chunk_ref"],
    ]
    state = knowledge.get_knowledge_source_state(conn, knowledge_id)
    assert state["status"] == "current"
    assert state["needs_recompile"] is False
    assert state["dependency_count"] == 2
    assert [item["is_primary"] for item in state["dependencies"]] == [True, False]
    assert {item["document_id"] for item in state["dependencies"]} == {
        primary["document_id"],
        supporting["document_id"],
    }

    # The legacy transport slice remains a truthful primary-document view; the
    # full cross-source relation is projected separately by source state.
    snapshot = knowledge.validate_document_knowledge_slice(conn, knowledge_id)
    assert {
        chunk["document_ref"] for chunk in snapshot["chunks"]
    } == {primary["document_id"]}


def test_multisource_publication_refuses_cross_project_chunk(conn, tmp_path) -> None:
    _contract_a, sources_a = _multi_source_fixture(
        conn, tmp_path, parent_project_id="project-a"
    )
    _contract_b, sources_b = _multi_source_fixture(
        conn, tmp_path, parent_project_id="project-b"
    )
    primary = next(iter(sources_a.values()))
    foreign = next(iter(sources_b.values()))

    with pytest.raises(knowledge.KnowledgeError, match="primary Project scope"):
        knowledge.publish_knowledge(
            conn,
            knowledge_id=f"knowledge.techniques.{uuid.uuid4().hex}",
            document_id=primary["document_id"],
            title="Invalid cross-project synthesis",
            family="techniques",
            markdown="# Refus attendu",
            source_chunk_refs=[primary["chunk_ref"], foreign["chunk_ref"]],
            created_by="hermes-test",
            actor_kind="hermes",
            idempotency_key=f"publish-{uuid.uuid4().hex}",
        )


def test_source_change_calculates_knowledge_impact_without_mutating_knowledge(
    conn, tmp_path
) -> None:
    contract, sources = _multi_source_fixture(conn, tmp_path)
    primary, supporting = list(sources.values())
    knowledge_id = f"knowledge.techniques.{uuid.uuid4().hex}"
    original_markdown = "# Façade\n\nSynthèse stable avant nouvelle source."

    knowledge.publish_knowledge(
        conn,
        knowledge_id=knowledge_id,
        document_id=primary["document_id"],
        title="Synthèse façade à maintenir",
        family="techniques",
        markdown=original_markdown,
        source_chunk_refs=[primary["chunk_ref"], supporting["chunk_ref"]],
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=f"publish-{uuid.uuid4().hex}",
    )
    before = knowledge.get_knowledge_source_state(conn, knowledge_id)
    assert before["status"] == "current"

    supporting["path"].write_text(
        "# CR chantier\n\nLe support est désormais repris et accepté visuellement.",
        encoding="utf-8",
    )
    assert store.ingest(
        conn,
        contract,
        tmp_path,
        ingestion_id=f"reingest-{uuid.uuid4().hex}",
    ) == 2

    after = knowledge.get_knowledge_source_state(conn, knowledge_id)
    assert after["status"] == "needs_recompile"
    assert after["needs_recompile"] is True
    changed = next(
        item
        for item in after["dependencies"]
        if item["document_id"] == supporting["document_id"]
    )
    assert changed["state"] == "source_changed"
    assert changed["source_changed"] is True
    assert changed["bound_source_digest"] != changed["current_source_digest"]

    impacts = knowledge.list_document_knowledge_impacts(
        conn, supporting["document_id"]
    )
    assert [item["knowledge_id"] for item in impacts["knowledge"]] == [knowledge_id]
    assert impacts["knowledge"][0]["status"] == "needs_recompile"

    # Impact calculation is observation only.
    assert knowledge.get_knowledge_markdown(conn, knowledge_id) == original_markdown
    assert knowledge.get_knowledge_card(conn, knowledge_id)["version"] == 1


def test_recompile_request_is_candidate_only_and_apply_rebinds_provenance(
    conn, tmp_path
) -> None:
    contract, sources = _multi_source_fixture(conn, tmp_path)
    primary, supporting = list(sources.values())
    knowledge_id = f"knowledge.techniques.{uuid.uuid4().hex}"
    original_markdown = "# Façade\n\nSynthèse avant évolution du compte-rendu."

    knowledge.publish_knowledge(
        conn,
        knowledge_id=knowledge_id,
        document_id=primary["document_id"],
        title="Synthèse façade recompilable",
        family="techniques",
        markdown=original_markdown,
        source_chunk_refs=[primary["chunk_ref"], supporting["chunk_ref"]],
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=f"publish-{uuid.uuid4().hex}",
    )

    supporting["path"].write_text(
        "# CR chantier\n\nLe support est repris et le primaire est désormais prescrit.",
        encoding="utf-8",
    )
    assert store.ingest(
        conn,
        contract,
        tmp_path,
        ingestion_id=f"reingest-{uuid.uuid4().hex}",
    ) == 2

    context = knowledge.build_knowledge_recompile_context(conn, knowledge_id)
    assert context["needs_recompile"] is True
    assert context["ready_for_candidate"] is True
    assert context["context_complete"] is True
    assert context["allowed_source_chunk_refs"]

    request_id = f"recompile-{uuid.uuid4().hex}"
    queued = knowledge.create_recompile_request(
        conn,
        request_id=request_id,
        knowledge_id=knowledge_id,
        requested_by="human:architect",
        idempotency_key=f"request-{uuid.uuid4().hex}",
    )
    request = queued["edit_request"]
    assert request["status"] == "queued_for_hermes"
    assert request["selection_start"] == 0
    assert request["selection_end"] == len(original_markdown)
    assert request["recompile_context_digest"] == context["context_digest"]
    assert queued["candidate_only"] is True
    assert queued["applies_automatically"] is False

    # Queueing alone is not a Knowledge write.
    assert knowledge.get_knowledge_markdown(conn, knowledge_id) == original_markdown
    assert knowledge.get_knowledge_card(conn, knowledge_id)["version"] == 1

    hermes_context = knowledge.get_recompile_context_for_request(conn, request_id)
    chosen_refs = [
        dependency["current_candidate_chunks"][0]["chunk_ref"]
        for dependency in hermes_context["dependencies"]
        if dependency["current_candidate_chunks"]
    ]
    assert len(chosen_refs) == 2

    proposed_markdown = (
        "# Façade\n\nLe support est repris ; le primaire prescrit doit être intégré "
        "à la synthèse actuelle."
    )
    proposal = knowledge.complete_edit_request(
        conn,
        request_id=request_id,
        replacement_markdown=proposed_markdown,
        replacement_source_chunk_refs=chosen_refs,
    )
    assert proposal["status"] == "proposed"
    assert proposal["replacement_source_chunk_refs"] == chosen_refs

    # Hermes proposing still does not write Knowledge.
    assert knowledge.get_knowledge_markdown(conn, knowledge_id) == original_markdown
    assert knowledge.get_knowledge_source_state(conn, knowledge_id)["status"] == "needs_recompile"

    client = StandInPolicyClient()
    apply_digest = knowledge._payload_digest(
        {
            "request_id": request_id,
            "knowledge_id": knowledge_id,
            "base_version": request["base_version"],
            "selected_text_digest": request["selected_text_digest"],
            "replacement_markdown": proposed_markdown,
            "recompile_context_digest": request["recompile_context_digest"],
            "replacement_source_chunk_refs": chosen_refs,
        }
    )
    decision_payload = {
        "decision": {
            "decision_id": f"decision-{uuid.uuid4().hex}",
            "decided_by": "human:architect",
            "approval_level": "C2",
            "scope": {
                "scope_type": "project",
                "scope_id": "project-maison-a",
            },
            "object_identity": f"knowledge_edit_request:{request_id}",
            "content_digest": apply_digest,
            "expires_at": "2099-01-01T00:00:00Z",
            "signature": "signed-recompile-decision",
        }
    }
    applied = knowledge.apply_edit_request(
        conn,
        request_id=request_id,
        actor="human:architect",
        actor_kind="human",
        idempotency_key=f"apply-{uuid.uuid4().hex}",
        policy_client=client,
        decision_payload=decision_payload,
    )
    assert client.last_decision["expectation"]["expected_digest"] == apply_digest
    assert applied["knowledge"]["version"] == 2
    assert applied["knowledge"]["source_chunk_refs"] == chosen_refs
    assert knowledge.get_knowledge_markdown(conn, knowledge_id) == proposed_markdown

    refreshed = knowledge.get_knowledge_source_state(conn, knowledge_id)
    assert refreshed["status"] == "current"
    assert refreshed["needs_recompile"] is False
    assert refreshed["dependency_count"] == 2

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT base_content_snapshot, resulting_content_snapshot
              FROM knowledge_events
             WHERE aggregate_ref = %s
               AND event_type = 'knowledge_revised'
             ORDER BY occurred_at DESC, event_id DESC
             LIMIT 1
            """,
            (knowledge_id,),
        )
        base_snapshot, resulting_snapshot = cur.fetchone()
    assert base_snapshot["version"] == 1
    assert base_snapshot["markdown"] == original_markdown
    assert base_snapshot["source_chunk_refs"] == [
        primary["chunk_ref"],
        supporting["chunk_ref"],
    ]
    assert resulting_snapshot["version"] == 2
    assert resulting_snapshot["markdown"] == proposed_markdown
    assert resulting_snapshot["source_chunk_refs"] == chosen_refs


def test_recompile_context_refuses_tampered_frozen_source_chunk(
    conn, tmp_path
) -> None:
    contract, sources = _multi_source_fixture(conn, tmp_path)
    primary, supporting = list(sources.values())
    knowledge_id = f"knowledge.techniques.{uuid.uuid4().hex}"

    knowledge.publish_knowledge(
        conn,
        knowledge_id=knowledge_id,
        document_id=primary["document_id"],
        title="Synthèse façade avec provenance figée",
        family="techniques",
        markdown="# Façade\n\nVersion initiale.",
        source_chunk_refs=[primary["chunk_ref"], supporting["chunk_ref"]],
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=f"publish-{uuid.uuid4().hex}",
    )

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT source_ref, source_digest, ordinal
              FROM knowledge_source_chunks
             WHERE knowledge_id = %s
               AND document_id = %s
            """,
            (knowledge_id, supporting["document_id"]),
        )
        old_source_ref, old_source_digest, old_ordinal = cur.fetchone()

    supporting["path"].write_text(
        "# CR chantier\n\nLe support est repris dans la nouvelle version.",
        encoding="utf-8",
    )
    assert store.ingest(
        conn,
        contract,
        tmp_path,
        ingestion_id=f"reingest-{uuid.uuid4().hex}",
    ) == 2

    # Simulate corruption of the immutable historical retrieval chunk. The
    # frozen provenance digest must make the old side of the recompile diff
    # unusable rather than silently accepting the modified body.
    conn.execute(
        """
        UPDATE chunks
           SET body = 'contenu historique altéré'
         WHERE source_ref = %s
           AND source_digest = %s
           AND chunk_no = %s
        """,
        (old_source_ref, old_source_digest, old_ordinal),
    )
    conn.commit()

    context = knowledge.build_knowledge_recompile_context(conn, knowledge_id)
    assert context["needs_recompile"] is True
    assert context["context_complete"] is False
    assert context["ready_for_candidate"] is False

    with pytest.raises(
        knowledge.KnowledgeError,
        match="context is incomplete",
    ):
        knowledge.create_recompile_request(
            conn,
            request_id=f"recompile-{uuid.uuid4().hex}",
            knowledge_id=knowledge_id,
            requested_by="human:architect",
            idempotency_key=f"request-{uuid.uuid4().hex}",
        )


def test_recompile_proposal_conflicts_if_source_context_moves_again(
    conn, tmp_path
) -> None:
    contract, sources = _multi_source_fixture(conn, tmp_path)
    primary, supporting = list(sources.values())
    knowledge_id = f"knowledge.techniques.{uuid.uuid4().hex}"

    knowledge.publish_knowledge(
        conn,
        knowledge_id=knowledge_id,
        document_id=primary["document_id"],
        title="Synthèse façade à contexte figé",
        family="techniques",
        markdown="# Façade\n\nVersion initiale.",
        source_chunk_refs=[primary["chunk_ref"], supporting["chunk_ref"]],
        created_by="hermes-test",
        actor_kind="hermes",
        idempotency_key=f"publish-{uuid.uuid4().hex}",
    )

    supporting["path"].write_text(
        "# CR chantier\n\nPremière évolution.",
        encoding="utf-8",
    )
    assert store.ingest(
        conn,
        contract,
        tmp_path,
        ingestion_id=f"reingest-a-{uuid.uuid4().hex}",
    ) == 2

    request_id = f"recompile-{uuid.uuid4().hex}"
    queued = knowledge.create_recompile_request(
        conn,
        request_id=request_id,
        knowledge_id=knowledge_id,
        requested_by="human:architect",
        idempotency_key=f"request-{uuid.uuid4().hex}",
    )
    queued_context = queued["recompile_context"]
    old_allowed = list(queued_context["allowed_source_chunk_refs"])

    supporting["path"].write_text(
        "# CR chantier\n\nDeuxième évolution après mise en file.",
        encoding="utf-8",
    )
    assert store.ingest(
        conn,
        contract,
        tmp_path,
        ingestion_id=f"reingest-b-{uuid.uuid4().hex}",
    ) == 2

    with pytest.raises(
        knowledge.StaleKnowledgeWrite,
        match="source context changed",
    ):
        knowledge.get_recompile_context_for_request(conn, request_id)

    proposal = knowledge.complete_edit_request(
        conn,
        request_id=request_id,
        replacement_markdown="# Façade\n\nProposition devenue obsolète.",
        replacement_source_chunk_refs=old_allowed,
    )
    assert proposal["status"] == "conflict"
    assert knowledge.get_knowledge_card(conn, knowledge_id)["version"] == 1


def test_ordinary_edit_does_not_rebind_source_provenance(conn, tmp_path) -> None:
    card, _document_id = _publish(conn, tmp_path)
    knowledge_id = card["knowledge_id"]
    original_refs = list(card["source_chunk_refs"])
    markdown = knowledge.get_knowledge_markdown(conn, knowledge_id)
    selected = "Préparer le support existant."
    start = markdown.index(selected)
    request_id = f"edit-{uuid.uuid4().hex}"

    knowledge.create_edit_request(
        conn,
        request_id=request_id,
        knowledge_id=knowledge_id,
        instruction_kind="rewrite",
        instruction="Reformuler sans changer les sources.",
        base_version=1,
        selection_start=start,
        selection_end=start + len(selected),
        selected_text=selected,
        requested_by="human:architect",
        idempotency_key=f"request-{uuid.uuid4().hex}",
    )
    knowledge.complete_edit_request(
        conn,
        request_id=request_id,
        replacement_markdown="Préparer soigneusement le support existant.",
    )
    applied = knowledge.apply_edit_request(
        conn,
        request_id=request_id,
        actor="human:architect",
        actor_kind="human",
        idempotency_key=f"apply-{uuid.uuid4().hex}",
    )
    assert applied["knowledge"]["source_chunk_refs"] == original_refs


def test_ordinary_revision_keeps_pre_recompile_idempotency_digest(
    conn, tmp_path
) -> None:
    card, _document_id = _publish(conn, tmp_path)
    knowledge_id = card["knowledge_id"]
    key = f"legacy-revise-{uuid.uuid4().hex}"
    proposed = "# Reprise des façades\n\nPréparer puis contrôler le support."
    arguments = {
        "knowledge_id": knowledge_id,
        "markdown": proposed,
        "expected_version": 1,
        "actor": "mobile-user",
        "actor_kind": "human",
        "idempotency_key": key,
        "review_status": None,
    }
    expected_digest = knowledge._payload_digest(
        {
            "knowledge_id": knowledge_id,
            "markdown": proposed,
            "expected_version": 1,
            "actor": "mobile-user",
            "actor_kind": "human",
            "review_status": None,
        }
    )

    first = knowledge.revise_knowledge(conn, **arguments)
    with conn.cursor() as cur:
        cur.execute(
            "SELECT payload_digest FROM knowledge_events WHERE idempotency_key = %s",
            (key,),
        )
        assert cur.fetchone()[0] == expected_digest

    # A retry from a client that obtained the key before Slice 2 must replay
    # instead of conflicting because a new nullable field was added later.
    assert knowledge.revise_knowledge(conn, **arguments) == first


def test_ordinary_edit_request_keeps_pre_recompile_idempotency_digest(
    conn, tmp_path
) -> None:
    card, _document_id = _publish(conn, tmp_path)
    knowledge_id = card["knowledge_id"]
    markdown = knowledge.get_knowledge_markdown(conn, knowledge_id)
    selected = "Préparer le support existant."
    start = markdown.index(selected)
    request_id = f"legacy-edit-{uuid.uuid4().hex}"
    key = f"legacy-request-{uuid.uuid4().hex}"
    arguments = {
        "request_id": request_id,
        "knowledge_id": knowledge_id,
        "instruction_kind": "rewrite",
        "instruction": "Reformuler sans changer le sens.",
        "base_version": 1,
        "selection_start": start,
        "selection_end": start + len(selected),
        "selected_text": selected,
        "requested_by": "mobile-user",
        "idempotency_key": key,
        "replacement_markdown": None,
    }
    expected_digest = knowledge._payload_digest(
        {
            "request_id": request_id,
            "knowledge_id": knowledge_id,
            "instruction_kind": "rewrite",
            "instruction": "Reformuler sans changer le sens.",
            "base_version": 1,
            "selection_start": start,
            "selection_end": start + len(selected),
            "selected_text": selected,
            "requested_by": "mobile-user",
            "replacement_markdown": None,
        }
    )

    first = knowledge.create_edit_request(conn, **arguments)
    assert first["request_payload_digest"] == expected_digest
    assert knowledge.create_edit_request(conn, **arguments) == first


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


def test_slice_carries_the_document_structure_and_binds_every_chunk(conn, tmp_path) -> None:
    """The contract requires the structure; this shows the slice actually carries it.

    `document_structure_read` has computed this since #229, but the slice never
    included it, so the vendored contract's name was the only thing tying the two
    together. Upstream then made `document_structure` and a per-chunk
    `fragment_ref` required, which is what turned an unused projection into a
    conformance failure.
    """
    card, _document_id = _publish(conn, tmp_path)
    snapshot = knowledge.validate_document_knowledge_slice(conn, card["knowledge_id"])

    structure = snapshot["document_structure"]
    assert structure["document_ref"] == snapshot["source_document"]["document_id"]
    assert structure["extraction_ref"] == snapshot["extraction"]["extraction_id"]
    assert structure["native_units"] and structure["fragments"]

    # Only what the contract declares. The read API also returns chunk_anchors and
    # an authority block, and page bounds inside each locator.
    assert "chunk_anchors" not in structure
    assert "authority" not in structure
    for fragment in structure["fragments"]:
        assert set(fragment["locator"]) <= {"structural_locator", "region"}

    fragment_ids = {fragment["fragment_id"] for fragment in structure["fragments"]}
    assert snapshot["chunks"]
    for chunk in snapshot["chunks"]:
        assert chunk["fragment_ref"] in fragment_ids, chunk


def test_publication_refuses_a_document_with_no_compiled_structure(conn, tmp_path) -> None:
    """The requirement has to fail loudly, naming the missing step."""
    card, document_id = _publish(conn, tmp_path)
    conn.execute(
        "DELETE FROM document_compilation_bindings WHERE document_id = %s", (document_id,)
    )
    with pytest.raises(knowledge.KnowledgeError, match="compiled document structure"):
        knowledge.validate_document_knowledge_slice(conn, card["knowledge_id"])
