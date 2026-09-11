from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "ai_logs/2026/Q3/2026-09-11-hermes-semantic-request-intake.md"


def test_semantic_intake_log_preserves_existing_authority_boundaries() -> None:
    text = LOG.read_text(encoding="utf-8")

    assert "REQUEST_LIFECYCLE.md" in text
    assert "ROLE_ACTIVATION.md" in text
    assert "request_handling.py" in text
    assert "semantic intake was not added to that plugin" in text
    assert "semantic candidate != truth" in text
    assert "condition candidate != consequence classification" in text
    assert "retrieved != Evidence" in text
    assert "runtime success != authorization" in text
    assert "projection != persistence" in text
    assert "false-positive / false-negative" in text
