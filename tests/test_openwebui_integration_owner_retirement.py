from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV = ROOT / "docs" / "governance"
REMOVED = GOV / "OPENWEBUI_INTEGRATION.md"
OBSOLETE = GOV / "authority" / "OBSOLETE_AND_ABSENT_INDEX.md"

# Follow-up debt owner: #785. This exact set is intentionally machine-tracked so
# no new current-authority OpenWebUI ownership residue can appear silently while
# owner-coherent follow-up slices reduce the set to zero.
KNOWN_CURRENT_AUTHORITY_OPENWEBUI_RESIDUES = {
    "docs/governance/ADAPTERS_AND_BINDINGS.md",
    "docs/governance/ADAPTIVE_REQUEST_METHOD.md",
    "docs/governance/BRIDGE_CONTRACT.md",
    "docs/governance/CODE_AUDIT_POST_PIVOT.md",
    "docs/governance/DISCORDIA.md",
    "docs/governance/DOCTOR_MODULE_SPEC.md",
    "docs/governance/DOSSIER_SITUATION_INTAKE.md",
    "docs/governance/EDITORIAL_LANGUAGE.md",
    "docs/governance/EXECUTION_MINIMALISM.md",
    "docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md",
    "docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md",
    "docs/governance/GOVERNED_AUTONOMY_GRADIENT.md",
    "docs/governance/GOVERNED_METHOD_STANDARD.md",
    "docs/governance/HERMES_INTEGRATION_MODELS_RECONCILIATION.md",
    "docs/governance/MODEL_CAPABILITY_PASSPORT.md",
    "docs/governance/MODULAR_DOMAIN_REORIENTATION.md",
    "docs/governance/MODULE_ACTIVATION.md",
    "docs/governance/PRE_EXECUTION_SIMULATION.md",
    "docs/governance/PROMPT_PLACEMENT.md",
    "docs/governance/REFERENCE_BOUNDARIES.md",
    "docs/governance/REJECTED_PATTERNS.md",
    "docs/governance/REQUEST_LIFECYCLE.md",
    "docs/governance/ROADMAP.md",
    "docs/governance/SKILL_WATCHLIST.md",
    "docs/governance/SOURCE_NEED_AND_REGISTRY.md",
    "docs/governance/TENSIONS_AND_RISKS.md",
    "docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md",
    "docs/governance/WORKFLOW_FORGING_PROTOCOL.md",
    "docs/governance/evidence_topology_antipatterns/README.md",
    "docs/governance/rites/RITE_EXAMPLES.md",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _is_current_authority(text: str) -> bool:
    status = next(
        (line for line in text.splitlines() if line.startswith("Status: ")),
        "",
    )
    return status.startswith(
        (
            "Status: canonical doctrine",
            "Status: active doctrine",
            "Status: active support",
        )
    )


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


def test_active_governance_openwebui_ownership_residue_is_explicitly_bounded():
    forbidden = (
        "OpenWebUI owns the cockpit surface",
        "user visibility or decision capture -> OpenWebUI",
        "OpenWebUI exposes.",
        "OpenWebUI may expose",
        "OpenWebUI may display",
        "through Agora, OpenWebUI",
    )
    offenders = []
    for path in GOV.rglob("*.md"):
        if path == OBSOLETE:
            continue
        text = _read(path)
        if not _is_current_authority(text):
            continue
        for phrase in forbidden:
            if phrase in text:
                offenders.append((path.relative_to(ROOT).as_posix(), phrase))

    offender_paths = {path for path, _ in offenders}
    unexpected = offender_paths - KNOWN_CURRENT_AUTHORITY_OPENWEBUI_RESIDUES
    no_longer_present = KNOWN_CURRENT_AUTHORITY_OPENWEBUI_RESIDUES - offender_paths

    assert unexpected == set()
    assert no_longer_present == set()


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


def test_agent_plugins_review_uses_current_client_agnostic_split():
    review = _read(GOV / "AGENT_PLUGINS_INTEROPERABILITY.md")
    assert "OpenWebUI" not in review
    assert "Agent Plugins 1.0.0 — Published" in review
    assert "Optional Hermes WebUI or other compatible clients may expose runtime interaction" in review
    assert "Hermes WebUI available != Hermes WebUI selected" in review
    assert "hermes_webui_required: false" in review
    assert "Hermes Agent executes external admitted work" in review
    assert "Pantheon Cockpit projects governed Cards" in review
    assert "multi-target capability available != multi-target need demonstrated" in review
    assert "hermes_runtime_adapter_required: not demonstrated" in review


def test_core_review_and_public_surfaces_are_client_agnostic():
    paths = (
        ROOT / "docs" / "HTTP_API_CONTRACT.md",
        ROOT / "mcp-server" / "docs" / "HTTP_API_CONTRACT.md",
        GOV / "APPROVALS.md",
        GOV / "RUN_GRAPH.md",
        GOV / "EVIDENCE_PACK.md",
        GOV / "TASK_CONTRACTS.md",
        GOV / "GOVERNANCE_COLLEGE.md",
        ROOT / "docs" / "intro-professionnelle.md",
    )
    for path in paths:
        text = _read(path)
        assert "OpenWebUI" not in text, path.relative_to(ROOT).as_posix()

    approvals = _read(GOV / "APPROVALS.md")
    trace = _read(GOV / "RUN_GRAPH.md")
    evidence = _read(GOV / "EVIDENCE_PACK.md")
    task_contracts = _read(GOV / "TASK_CONTRACTS.md")
    college = _read(GOV / "GOVERNANCE_COLLEGE.md")
    http_contract = _read(ROOT / "mcp-server" / "docs" / "HTTP_API_CONTRACT.md")
    intro = _read(ROOT / "docs" / "intro-professionnelle.md")

    assert "Hermes WebUI is optional/proposed" in approvals
    assert "Hermes WebUI is an optional/proposed external surface" in trace
    assert "Hermes WebUI is optional/proposed" in evidence
    assert "Hermes WebUI available != Hermes WebUI selected" in task_contracts
    assert "runtime client approval control != Pantheon approval" in college
    assert "The external runtime Policy Enforcement Point remains responsible" in http_contract
    assert "Pantheon Cockpit projects governed approval state" in approvals
    assert "Pantheon Cockpit projects governed trace/review state" in trace
    assert "runtime output != Evidence" in evidence
    assert "projection != persistence" in evidence
    assert "Hermes WebUI optionnelle / clients compatibles = interaction runtime possible." in intro
    assert "Pantheon Cockpit                               = projections gouvernées." in intro


def test_governance_ci_no_longer_requires_removed_owner():
    workflow = _read(ROOT / ".github" / "workflows" / "governance-ci.yml")
    assert "docs/governance/OPENWEBUI_INTEGRATION.md" not in workflow
    assert '"docs/governance/HERMES_INTEGRATION.md"' in workflow
    assert '"docs/governance/EXTERNAL_TOOLS_POLICY.md"' in workflow
