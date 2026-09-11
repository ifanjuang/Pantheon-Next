from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "ai_logs/INDEX.md"


def test_semantic_intake_trace_is_indexed_once() -> None:
    text = INDEX.read_text(encoding="utf-8")
    path = "2026/Q3/2026-09-11-hermes-semantic-request-intake.md"
    assert text.count(path) == 1
