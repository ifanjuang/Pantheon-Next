from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "governance" / "reference_reviews" / "AI_MEMORY_MNEMOSYNE_RUNTIME_MEMORY_REVIEW.md"
TRACE = ROOT / "ai_logs" / "2026" / "Q3" / "2026-08-25-ai-memory-mnemosyne-comparison.md"


def _review() -> str:
    return REVIEW.read_text(encoding="utf-8")


def test_review_pins_rechecked_upstream_identities() -> None:
    raw = _review()
    assert "c304ff6ecba54b05c488345e2c4b0bba81cb9574" in raw
    assert "8e6c010bc823b7833061f0ee53c2a73a9dd6dd24" in raw
    assert "8e61b19b7481c86ece5ee24285e74514daf2398c" in raw
    assert "af8885b35ebb00ff0199fb01f44b4d3f77c31bd3" in raw
    assert "ai-memory 1.28.1" in raw
    assert "ai-memory `1.32.0`" in raw


def test_review_preserves_single_runtime_memory_convergence() -> None:
    raw = _review()
    assert "possible Mnemosyne successor" in raw
    assert "not_a_target: Hindsight" in raw
    assert "activation: none" in raw
    assert "one fluid runtime-memory provider, not two" in raw


def test_review_preserves_governance_boundaries() -> None:
    raw = _review()
    for invariant in (
        "memory recalled != truth",
        "memory artifact != Evidence",
        "handoff delivered != authorization",
        "runtime write success != ingestion authority",
        "folder/path != governed identity",
    ):
        assert invariant in raw


def test_review_uses_neutral_workspace_vocabulary() -> None:
    raw = _review() + TRACE.read_text(encoding="utf-8")
    assert "IFJA" not in raw
    assert "ifja-" not in raw.lower()


def test_trace_records_no_activation() -> None:
    raw = TRACE.read_text(encoding="utf-8")
    assert "DO NOT activate ai-memory" in raw
    assert "No runtime, dependency, Docker" in raw
