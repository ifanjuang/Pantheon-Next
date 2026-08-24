from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def _lines(relative: str) -> set[str]:
    return {line.strip() for line in _read(relative).splitlines()}


def test_active_work_rules_close_initial_import_compatibility_debt() -> None:
    text = _read("CLAUDE.md")

    assert "compatibility debt created by the initial `pantheon-mvp` import is closed" in text
    assert "initial import may temporarily retain vendored governance snapshots" not in text
    assert "Do not reintroduce vendored governance snapshots" in text


def test_current_implementation_placement_is_monorepo_native() -> None:
    placement = _read("docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md")
    tool_card = _read("docs/governance/TOOL_CARD_MODEL.md")
    registry = _read("registries/README.md")

    assert "Pantheon implementation" in placement
    assert "implementation/" in placement
    assert "Pantheon implementation under `implementation/`" in tool_card
    assert "implementation/mvp_vertical/cockpit/registries/" in registry

    assert "belongs in `pantheon-mvp`" not in tool_card
    assert "`pantheon-mvp` may own operational instances" not in registry
    assert "validate the existing pantheon-mvp tag instance against a vendored reference" not in registry


def test_hermes_templates_review_current_monorepo_consumers() -> None:
    readme = _read("templates/hermes/README.md")
    design = _read("templates/hermes/DESIGN.md")
    claude = _read("templates/hermes/CLAUDE.md")

    assert "current co-located consumers under `implementation/`" in readme
    assert "former `pantheon-mvp/main` remains historical provenance" in readme
    assert "current `pantheon-mvp/main`" not in readme
    assert "current `pantheon-mvp/main`" not in claude
    assert "- `pantheon-mvp`: candidate PostgreSQL/API/Cockpit implementation" not in design


def test_cockpit_orientation_points_to_co_located_candidate() -> None:
    assets = _read("docs/assets/README.md")
    card_stack = _read("docs/assets/card-stack/README.md")
    control_readme = _read("docs/assets/pantheon-control/README.md")
    control_index = _read("docs/assets/pantheon-control/index.html")

    for text in (assets, card_stack, control_readme, control_index):
        assert "implementation/mvp_vertical/cockpit" in text

    assert "Product cockpit screens, executable product renderers, synthetic project data and runtime scenarios belong in `ifanjuang/pantheon-mvp`" not in assets
    assert "implemented cards-first frontend is owned by the external `ifanjuang/pantheon-mvp`" not in card_stack
    assert "Le cockpit candidat vit dans <code>pantheon-mvp</code>" not in control_index


def test_historical_repository_name_remains_valid_provenance() -> None:
    placement = _read("docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md")
    card_stack = _read("docs/assets/card-stack/README.md")

    assert "former repository = ifanjuang/pantheon-mvp" in placement
    assert "source cutoff      = d960862dd0e23b7003a0f3e4ee0ea630ffc12af9" in placement
    assert "historical commit: 4ee41a845ec51db3118a584db0411a300450ccbd" in card_stack


def test_runtime_adapter_index_uses_logical_tool_card_owner() -> None:
    text = _read("docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md")

    assert "Concrete catalogue records, card projection and Hermes/runtime reconciliation belong to `Pantheon implementation` under `implementation/`" in text
    assert "Concrete catalogue records, card projection and Hermes/runtime reconciliation belong in `pantheon-mvp`" not in text


def test_phase_b_operator_docs_point_to_existing_monorepo_compose_files() -> None:
    core = ROOT / "implementation/compose.phase-b.yaml"
    paperless = ROOT / "implementation/compose.paperless.yaml"
    assert core.is_file()
    assert paperless.is_file()

    runbook = _read("docs/install/PLATFORM_PHASE_B_DEPLOYMENT_RUNBOOK.md")
    portainer = _read("docs/install/PORTAINER_PHASE_B_HANDOFF.md")
    paperless_install = _read("docs/install/PAPERLESS_INITIAL_INSTALLATION.md")

    for text in (runbook, portainer, paperless_install):
        assert "implementation/compose.phase-b.yaml" in text
        assert "implementation/compose.paperless.yaml" in text
        assert "--profile paperless" not in text

    assert "reviewed pantheon-mvp commit" not in runbook
    assert "ifanjuang/pantheon-mvp\n  core: compose.phase-b.yaml" not in portainer


def test_hermes_document_intake_runbook_uses_reviewed_monorepo_skill_source() -> None:
    skill_root = ROOT / "implementation/hermes/skills/pantheon-document-intake"
    assert (skill_root / "SKILL.md").is_file()
    assert (skill_root / "scripts/pantheon_document_intake.py").is_file()

    runbook = _read("docs/install/HERMES_PANTHEON_DOCUMENT_INTAKE_SKILL.md")
    assert "implementation/hermes/skills/pantheon-document-intake/" in runbook
    assert "PANTHEON_NEXT_SKILL_COMMIT" in runbook
    assert "raw.githubusercontent.com/ifanjuang/Pantheon-Next/" in runbook
    assert "raw.githubusercontent.com/ifanjuang/pantheon-mvp/" not in runbook
    assert "reviewed pantheon-mvp commit" not in runbook


def test_document_runtime_doctrine_uses_co_located_pantheon_adapter_placement() -> None:
    paths = (
        "docs/governance/PAPERLESS_NGX_DOCUMENT_RUNTIME.md",
        "docs/governance/HERMES_PAPERLESS_DOCUMENT_INTAKE_BINDING.md",
        "docs/governance/DOCUMENT_RUNTIME_STATUS_PROJECTION.md",
        "docs/governance/DOCUMENT_RUNTIME_LIVE_OBSERVATIONS.md",
    )

    for path in paths:
        text = _read(path)
        assert "implementation/" in text
        # Historical provenance may still say "former repository"; only an
        # active source declaration using the old repository is forbidden.
        assert "repository: ifanjuang/pantheon-mvp" not in _lines(path)

    assert "### `ifanjuang/pantheon-mvp`" not in _read("docs/governance/PAPERLESS_NGX_DOCUMENT_RUNTIME.md")


def test_internal_link_checker_recognizes_implementation_as_repository_root() -> None:
    checker_path = ROOT / ".github/scripts/check_internal_links.py"
    spec = spec_from_file_location("check_internal_links", checker_path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    target = "implementation/hermes/skills/pantheon-document-intake/"
    line = f"Current candidate source: `{target}`"
    matches = [match.group("path") for match in module.PATH_RE.finditer(line)]

    assert matches == [target]
    assert module.normalize_candidate(target, "docs/governance/example.md", line) == target


def test_runtime_interface_names_are_not_misread_as_repository_owners() -> None:
    portainer = _read("docs/install/PORTAINER_PHASE_B_HANDOFF.md")
    paperless_runtime = _read("docs/governance/PAPERLESS_NGX_DOCUMENT_RUNTIME.md")

    assert "The `MVP_*` names remain active runtime interfaces" in portainer
    assert "historical implementation provenance only" in paperless_runtime
