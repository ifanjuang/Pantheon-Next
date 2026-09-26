from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "implementation" / "hermes" / "skills" / "ifja-vault-search" / "SKILL.md"


def test_latest_document_resolution_uses_source_chronology_not_ingest_metadata() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "Latest document / revision resolution" in text
    assert "Hindsight `get_document`" in text
    assert "source_revision" in text
    assert "source_document_date" in text
    assert "source_revision_history[]" in text
    assert "source_supersedes[]" in text
    assert "filesystem mtime" in text
    assert "cartouche date/index" in text
    assert "explicit supersedes/replaces relationship" in text
    assert "explicit coherent revision history/table" in text
    assert "comparable source revision/index" in text
    assert "source document date as tie-breaker/fallback" in text


def test_revision_date_conflicts_do_not_hide_human_errors() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "revision_date_conflict" in text
    assert "duplicate_revision" in text
    assert "incomparable_revision" in text
    assert "preserve the higher revision as the preferred candidate" in text
    assert "keep the lower revision visible as a conflicting candidate" in text
    assert "do not silently collapse them" in text
    assert "current revision is ambiguous" in text
