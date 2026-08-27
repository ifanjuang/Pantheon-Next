from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV = ROOT / "docs" / "governance"
REMOVED = GOV / "OPENWEBUI_INTEGRATION.md"
OBSOLETE = GOV / "authority" / "OBSOLETE_AND_ABSENT_INDEX.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_openwebui_integration_owner_is_removed():
    assert not REMOVED.exists()
    obsolete = _read(OBSOLETE)
    assert "`OPENWEBUI_INTEGRATION.md` (removed; Git history)" in obsolete
    assert "OpenWebUI is not a selected architecture component or governance owner" in obsolete


def test_no_active_governance_doc_depends_on_removed_owner():
    offenders = []
    for path in GOV.rglob("*.md"):
        if path == OBSOLETE:
            continue
        if "OPENWEBUI_INTEGRATION.md" in _read(path):
            offenders.append(path.relative_to(ROOT).as_posix())
    assert offenders == []


def test_decision_and_learning_surfaces_are_client_agnostic():
    decision = _read(GOV / "DECISION_SURFACE_SPEC.md")
    learning = _read(GOV / "AI_LEARNING_REPOS_DISTILLATION.md")
    assert "OpenWebUI" not in decision
    assert "OpenWebUI" not in learning
    assert "Pantheon Cockpit/Card" in decision
    assert "compatible clients" in decision
    assert "Runtime clients and Pantheon Cockpit" in learning
    assert "client selected != governance authority" in learning


def test_governance_ci_no_longer_requires_removed_owner():
    workflow = _read(ROOT / ".github" / "workflows" / "governance-ci.yml")
    assert "docs/governance/OPENWEBUI_INTEGRATION.md" not in workflow
    assert '"docs/governance/HERMES_INTEGRATION.md"' in workflow
    assert '"docs/governance/EXTERNAL_TOOLS_POLICY.md"' in workflow
