from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_mvp_loop_uses_current_runtime_projection_and_retrieval_owners() -> None:
    text = (ROOT / "docs/governance/MVP_GOVERNED_TASK_LOOP.md").read_text(
        encoding="utf-8"
    )

    assert "OPENWEBUI_INTEGRATION.md" not in text
    assert "OpenWebUI exposes" not in text
    assert "Hermes Web/dashboard" in text
    assert "Hermes Agent" in text
    assert "Pantheon Cockpit" in text
    assert "pgvector` may be a demonstrated binding, not an architectural requirement" in text
    assert "provider selected != authority transfer" in text
    assert "retrieved != truth" in text
    assert "projection != persistence" in text


def test_mvp_loop_does_not_require_parallel_runtime_or_rag_owners() -> None:
    text = (ROOT / "docs/governance/MVP_GOVERNED_TASK_LOOP.md").read_text(
        encoding="utf-8"
    )

    assert "a Pantheon agent runtime" in text
    assert "a canonical RAG framework" in text
    assert "a mandatory vector database" in text
    assert "a second generic chat UI" in text
