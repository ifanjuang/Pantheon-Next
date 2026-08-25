from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_active_hermes_surfaces_use_current_hosting_owners() -> None:
    active_sources = (
        "templates/hermes/SKILLS.md",
        "templates/hermes/DESIGN.md",
        "templates/hermes/CLAUDE.md",
        "templates/hermes/distribution/distribution-lock.example.yaml",
        "implementation/hermes/distribution/pantheon-standard.lock.yaml",
    )

    for relative in active_sources:
        text = _read(relative)
        assert "HERMES_CODE_HOSTING_BOUNDARY.md" not in text
        assert "NEXT_MVP_REPOSITORY_PLACEMENT.md" in text
        assert "HERMES_INTEGRATION.md" in text


def test_hosting_convergence_preserves_runtime_authority_boundaries() -> None:
    skills = _read("templates/hermes/SKILLS.md")
    materialized = _read("implementation/hermes/distribution/pantheon-standard.lock.yaml")

    assert "Executable scripts, installers, provider routers, queues and schedulers do not belong in this template surface." in skills
    assert "installation_state: not_observed" in materialized
    assert "activation_state: not_activated" in materialized
    assert "task_authorization_state: not_authorized" in materialized
    assert "admits_evidence: false" in materialized
