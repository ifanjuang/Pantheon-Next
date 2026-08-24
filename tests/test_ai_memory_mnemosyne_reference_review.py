from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = (
    ROOT
    / "docs"
    / "governance"
    / "reference_reviews"
    / "AI_MEMORY_MNEMOSYNE_RUNTIME_MEMORY_REVIEW.md"
)
BINDINGS = ROOT / "docs" / "governance" / "HERMES_CAPABILITY_BINDINGS.md"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_ai_memory_is_documented_as_mnemosyne_replacement_candidate_only() -> None:
    review = _text(REVIEW)

    assert "status: to_verify" in review
    assert "target_to_replace_if_qualified: Mnemosyne" in review
    assert "not_a_target: Hindsight" in review
    assert "activation: none" in review
    assert "Pantheon authority: none" in review
    assert "DO NOT    run Mnemosyne + ai-memory as concurrent steady-state fluid memories" in review


def test_ai_memory_review_preserves_memory_governance_invariants() -> None:
    review = _text(REVIEW)

    assert "retrieved memory != truth" in review
    assert "runtime history != Evidence" in review
    assert "successful continuation != authorization" in review
    assert "memory page != Evidence" in review
    assert "handoff delivered != authorization" in review
    assert "runtime write success != ingestion authority" in review


def test_ai_memory_review_does_not_promote_the_existing_binding_registry() -> None:
    review = _text(REVIEW)
    bindings = _text(BINDINGS)

    assert "The currently documented `assistant-personal` sandbox order remains unchanged" in review
    assert "Hindsight -> Mnemosyne -> Mem0" in review
    assert "sandbox_preference_order: Hindsight, Mnemosyne, Mem0" in bindings
    assert "preferred_binding: unbound" in bindings
    assert "forbidden_profiles: pantheon-governed" in bindings


def test_ai_memory_qualification_requires_target_topology_evidence() -> None:
    review = _text(REVIEW)

    for heading in (
        "### Q1 — current Hermes compatibility",
        "### Q2 — Hermes cross-session continuity",
        "### Q3 — cross-agent workstream handoff",
        "### Q4 — scope isolation",
        "### Q5 — capture confidentiality",
        "### Q6 — NAS outage and restart",
        "### Q7 — deletion/export/restore",
        "### Q8 — Hindsight non-duplication",
        "### Q9 — governance invariants",
    ):
        assert heading in review
