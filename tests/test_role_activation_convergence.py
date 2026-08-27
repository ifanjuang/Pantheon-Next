from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/governance/ROLE_ACTIVATION.md"


def _text() -> str:
    return DOC.read_text(encoding="utf-8")


def test_role_activation_has_no_retired_openwebui_owner() -> None:
    text = _text()
    assert "OpenWebUI" not in text
    assert "OPENWEBUI_INTEGRATION.md" not in text
    assert "openwebui_template_pack" not in text


def test_role_activation_uses_current_runtime_and_projection_owners() -> None:
    text = _text()
    assert "Hermes clients handle runtime interaction" in text
    assert "Hermes Agent executes externally" in text
    assert "Pantheon Cockpit exposes governed projections" in text
    assert "client selected != governance authority" in text
    assert "projection != persistence" in text


def test_activation_remains_eligibility_not_authority() -> None:
    text = _text()
    for invariant in (
        "role active != agent started",
        "domain enabled != professional authority",
        "skill eligible != task authorized",
        "task authorized != approved",
        "activation != retention authorization",
    ):
        assert invariant in text


def test_activation_reuses_existing_owners() -> None:
    text = _text()
    for owner in (
        "AGENTS.md",
        "MODULE_ACTIVATION.md",
        "UNIFORM_CAPABILITY_GOVERNANCE.md",
        "DOMAIN_PACK_SPEC.md",
        "TASK_CONTRACTS.md",
        "HERMES_INTEGRATION.md",
        "PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md",
    ):
        assert owner in text
