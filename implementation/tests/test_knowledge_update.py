"""Signed and human-confirmed Knowledge UPDATE gate tests."""

from __future__ import annotations

import pytest

from mvp_vertical import knowledge, knowledge_update


CARD = {
    "knowledge_id": "knowledge.coverage",
    "parent_project_id": "project-lieurey",
    "title": "Choix de couverture",
    "review_status": "needs_review",
    "version": 3,
}
CURRENT = "# Couverture\n\nLe zinc reste à confirmer.\n"
PROPOSED = "# Couverture\n\nLe client confirme le zinc naturel.\n"


class _Connection:
    pass


def _patch_reads(monkeypatch, *, card=None, markdown=CURRENT):
    monkeypatch.setattr(
        knowledge,
        "get_knowledge_card",
        lambda _conn, _knowledge_id: dict(card or CARD),
    )
    monkeypatch.setattr(
        knowledge,
        "get_knowledge_markdown",
        lambda _conn, _knowledge_id: markdown,
    )


def test_preview_returns_signed_diff_without_writing(monkeypatch) -> None:
    _patch_reads(monkeypatch)
    preview = knowledge_update.preview_knowledge_update(
        _Connection(),
        parent_project_id="project-lieurey",
        knowledge_id="knowledge.coverage",
        proposed_markdown=PROPOSED,
        expected_version=3,
        actor="ifan.juang",
        signing_secret="editor-secret",
        now=1_000,
    )

    assert preview["status"] == "confirmation_required"
    assert preview["effect"] == "UPDATE"
    assert preview["target"]["current_version"] == 3
    assert preview["target"]["proposed_review_status"] == "needs_review"
    assert "-Le zinc reste à confirmer." in preview["diff"]
    assert "+Le client confirme le zinc naturel." in preview["diff"]
    assert preview["confirmation"]["phrase"] == "CONFIRMER UPDATE"
    assert preview["confirmation"]["expires_at"] == 1_300
    assert preview["identity"]["assurance"] == "partial"


def test_apply_verifies_exact_preview_and_delegates_transactional_write(monkeypatch) -> None:
    _patch_reads(monkeypatch)
    preview = knowledge_update.preview_knowledge_update(
        _Connection(),
        parent_project_id="project-lieurey",
        knowledge_id="knowledge.coverage",
        proposed_markdown=PROPOSED,
        expected_version=3,
        actor="ifan.juang",
        signing_secret="editor-secret",
        review_status="needs_review",
        now=1_000,
    )
    observed = {}

    def revise(_conn, **values):
        observed.update(values)
        return {**CARD, "version": 4, "markdown_digest": "new"}

    monkeypatch.setattr(knowledge, "revise_knowledge", revise)
    result = knowledge_update.apply_knowledge_update(
        _Connection(),
        parent_project_id="project-lieurey",
        knowledge_id="knowledge.coverage",
        proposed_markdown=PROPOSED,
        expected_version=3,
        base_markdown_digest=preview["base_markdown_digest"],
        actor="ifan.juang",
        signing_secret="editor-secret",
        confirmation_token=preview["confirmation"]["token"],
        confirmation_expires_at=preview["confirmation"]["expires_at"],
        confirmation_phrase="CONFIRMER UPDATE",
        idempotency_key="update-knowledge-0001",
        review_status="needs_review",
        now=1_010,
    )

    assert result["status"] == "applied"
    assert result["knowledge"]["version"] == 4
    assert observed == {
        "knowledge_id": "knowledge.coverage",
        "markdown": PROPOSED,
        "expected_version": 3,
        "actor": "ifan.juang",
        "actor_kind": "human",
        "idempotency_key": "update-knowledge-0001",
        "review_status": None,
    }


def test_apply_rejects_expiry_tampering_scope_and_stale_markdown(monkeypatch) -> None:
    _patch_reads(monkeypatch)
    preview = knowledge_update.preview_knowledge_update(
        _Connection(),
        parent_project_id="project-lieurey",
        knowledge_id="knowledge.coverage",
        proposed_markdown=PROPOSED,
        expected_version=3,
        actor="ifan.juang",
        signing_secret="editor-secret",
        now=1_000,
    )
    common = dict(
        conn=_Connection(),
        parent_project_id="project-lieurey",
        knowledge_id="knowledge.coverage",
        proposed_markdown=PROPOSED,
        expected_version=3,
        base_markdown_digest=preview["base_markdown_digest"],
        actor="ifan.juang",
        signing_secret="editor-secret",
        confirmation_token=preview["confirmation"]["token"],
        confirmation_expires_at=preview["confirmation"]["expires_at"],
        confirmation_phrase="CONFIRMER UPDATE",
        idempotency_key="update-knowledge-0002",
    )

    with pytest.raises(knowledge_update.KnowledgeUpdateExpired):
        knowledge_update.apply_knowledge_update(**common, now=1_301)

    with pytest.raises(knowledge_update.KnowledgeUpdateError, match="immutable UPDATE"):
        knowledge_update.apply_knowledge_update(
            **{**common, "proposed_markdown": PROPOSED + "\nAltération"}, now=1_010
        )

    _patch_reads(monkeypatch, card={**CARD, "parent_project_id": "project-other"})
    with pytest.raises(knowledge_update.KnowledgeUpdateError, match="exact opened project"):
        knowledge_update.apply_knowledge_update(**common, now=1_010)

    _patch_reads(monkeypatch, markdown=CURRENT + "\nChangement concurrent")
    with pytest.raises(knowledge.StaleKnowledgeWrite, match="changed after"):
        knowledge_update.apply_knowledge_update(**common, now=1_010)


def test_preview_refuses_noop_stale_version_and_status_change(monkeypatch) -> None:
    _patch_reads(monkeypatch)
    with pytest.raises(knowledge_update.KnowledgeUpdateError, match="no material change"):
        knowledge_update.preview_knowledge_update(
            _Connection(),
            parent_project_id="project-lieurey",
            knowledge_id="knowledge.coverage",
            proposed_markdown=CURRENT,
            expected_version=3,
            actor="ifan.juang",
            signing_secret="editor-secret",
        )
    with pytest.raises(knowledge.StaleKnowledgeWrite, match="current 3"):
        knowledge_update.preview_knowledge_update(
            _Connection(),
            parent_project_id="project-lieurey",
            knowledge_id="knowledge.coverage",
            proposed_markdown=PROPOSED,
            expected_version=2,
            actor="ifan.juang",
            signing_secret="editor-secret",
        )
    with pytest.raises(knowledge_update.KnowledgeUpdateError, match="separate governed"):
        knowledge_update.preview_knowledge_update(
            _Connection(),
            parent_project_id="project-lieurey",
            knowledge_id="knowledge.coverage",
            proposed_markdown=PROPOSED,
            expected_version=3,
            actor="ifan.juang",
            signing_secret="editor-secret",
            review_status="reviewed",
        )
