"""Unit tests for server-side declared Card scope and explicit context validation."""

from __future__ import annotations

import pytest

from mvp_vertical import (
    agency_data,
    agency_directory,
    card_scope,
    knowledge,
    store,
    work_issue_read,
)


class _Connection:
    pass


def test_project_scope_resolves_only_participations_and_direct_documents(monkeypatch) -> None:
    monkeypatch.setattr(
        agency_data,
        "get_project",
        lambda _conn, project_id: {"project_id": project_id},
    )
    monkeypatch.setattr(
        agency_directory,
        "list_project_participations",
        lambda _conn, project_id: [
            {"participation_id": "bet", "project_id": project_id},
            {"participation_id": "client", "project_id": project_id},
        ],
    )
    monkeypatch.setattr(
        store,
        "list_document_cards",
        lambda _conn, project_id: [
            {"document_id": "cctp", "source_ref": f"nas://{project_id}/cctp.pdf"},
        ],
    )

    resolved = card_scope.resolve_declared_descendants(
        _Connection(),
        root_entity={"entity_id": "project:lieurey", "entity_type": "project"},
    )

    assert resolved["policy"] == "project_declared_children"
    assert resolved["descendants"] == [
        {"entity_id": "participation:bet", "entity_type": "project_participation"},
        {"entity_id": "participation:client", "entity_type": "project_participation"},
        {"entity_id": "document:cctp", "entity_type": "document"},
    ]
    assert resolved["source_refs"] == ["nas://lieurey/cctp.pdf"]
    assert resolved["counts"] == {"project_participations": 2, "documents": 1}


def test_document_scope_adds_source_but_no_implicit_relations(monkeypatch) -> None:
    monkeypatch.setattr(
        store,
        "get_document_card_by_id",
        lambda _conn, document_id: {
            "document_id": document_id,
            "source_ref": "nas://lieurey/cctp.pdf",
        },
    )
    resolved = card_scope.resolve_declared_descendants(
        _Connection(),
        root_entity={"entity_id": "document:cctp", "entity_type": "document"},
    )
    assert resolved["policy"] == "document_source_only"
    assert resolved["descendants"] == []
    assert resolved["source_refs"] == ["nas://lieurey/cctp.pdf"]


def test_known_cockpit_space_stays_root_only() -> None:
    resolved = card_scope.resolve_declared_descendants(
        _Connection(),
        root_entity={"entity_id": "space:outils", "entity_type": "cockpit_space"},
    )
    assert resolved == {
        "policy": "root_only",
        "root_owner_id": "space:outils",
        "descendants": [],
        "source_refs": [],
        "counts": {},
    }


def test_unknown_cockpit_space_is_refused() -> None:
    with pytest.raises(card_scope.CardScopeError, match="unknown Cockpit space"):
        card_scope.resolve_declared_descendants(
            _Connection(),
            root_entity={"entity_id": "space:forged", "entity_type": "cockpit_space"},
        )


def test_explicit_document_and_knowledge_context_derives_sources_server_side(monkeypatch) -> None:
    monkeypatch.setattr(
        store,
        "get_document_card_by_id",
        lambda _conn, document_id: {
            "document_id": document_id,
            "source_ref": "nas://lieurey/cctp.pdf",
        },
    )
    monkeypatch.setattr(
        knowledge,
        "get_knowledge_card",
        lambda _conn, knowledge_id: {
            "knowledge_id": knowledge_id,
            "source_chunk_refs": ["chunk.extract.0001", "chunk.extract.0002"],
        },
    )

    resolved = card_scope.resolve_explicit_context(
        _Connection(),
        entity_refs=[
            {"entity_id": "document:cctp", "entity_type": "document"},
            {"entity_id": "knowledge:structure", "entity_type": "knowledge"},
        ],
    )

    assert resolved["entities"] == [
        {"entity_id": "document:cctp", "entity_type": "document"},
        {"entity_id": "knowledge:structure", "entity_type": "knowledge"},
    ]
    assert resolved["source_refs"] == [
        "nas://lieurey/cctp.pdf",
        "chunk.extract.0001",
        "chunk.extract.0002",
    ]


def test_work_issue_case_resolution_uses_record_not_aggregate_projection(monkeypatch) -> None:
    monkeypatch.setattr(
        work_issue_read,
        "get_issue_record",
        lambda _conn, issue_id: {"issue_id": issue_id, "case_ref": "lieurey"},
    )
    assert card_scope.resolve_case_ref(
        _Connection(),
        root_entity={"entity_id": "work:123", "entity_type": "work_issue"},
    ) == "lieurey"
