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


def test_active_governance_does_not_assign_openwebui_architecture_ownership():
    forbidden = (
        "OpenWebUI owns the cockpit surface",
        "user visibility or decision capture -> OpenWebUI",
    )
    offenders = []
    for path in GOV.rglob("*.md"):
        if path == OBSOLETE:
            continue
        text = _read(path)
        for phrase in forbidden:
            if phrase in text:
                offenders.append((path.relative_to(ROOT).as_posix(), phrase))
    assert offenders == []


def test_decision_learning_and_placement_surfaces_are_client_agnostic():
    decision = _read(GOV / "DECISION_SURFACE_SPEC.md")
    learning = _read(GOV / "AI_LEARNING_REPOS_DISTILLATION.md")
    placement = _read(GOV / "CAPABILITY_PLACEMENT.md")
    assert "OpenWebUI" not in decision
    assert "OpenWebUI" not in learning
    assert "OpenWebUI" not in placement
    assert "Pantheon Cockpit/Card" in decision
    assert "compatible clients" in decision
    assert "Runtime clients and Pantheon Cockpit" in learning
    assert "client selected != governance authority" in learning
    assert "Replaceable clients expose runtime interaction" in placement
    assert "Pantheon Cockpit/Card surfaces project governed state" in placement
    assert "client selection does not transfer governance authority" in placement


def test_governance_ci_no_longer_requires_removed_owner():
    workflow = _read(ROOT / ".github" / "workflows" / "governance-ci.yml")
    assert "docs/governance/OPENWEBUI_INTEGRATION.md" not in workflow
    assert '"docs/governance/HERMES_INTEGRATION.md"' in workflow
    assert '"docs/governance/EXTERNAL_TOOLS_POLICY.md"' in workflow
