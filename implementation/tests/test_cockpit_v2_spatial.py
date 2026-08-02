"""Behavior and boundary checks for the executable Cockpit V2 spatial surface."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
PROJECTION = COCKPIT / "projection" / "cockpit_projection.js"
ASSEMBLER = COCKPIT / "projection" / "child_collection_assembler.js"
DATA_LOADER = COCKPIT / "data" / "cockpit_data_loader.js"


def _run_node(script: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is unavailable; JavaScript behavior check skipped")
    return subprocess.run([node, "-e", script], cwd=ROOT, check=False, capture_output=True, text=True)


@pytest.mark.parametrize(
    "path",
    [COCKPIT / "spatial_navigation.js", ASSEMBLER, PROJECTION, COCKPIT / "actions" / "card_actions.js", COCKPIT / "live_bootstrap.js"],
    ids=lambda path: str(path.relative_to(COCKPIT)),
)
def test_v2_javascript_parses(path: Path) -> None:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is unavailable; JavaScript syntax check skipped")
    result = subprocess.run([node, "--check", str(path)], check=False, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_spatial_navigation_keeps_sibling_and_parent_boundaries() -> None:
    script = r'''
      global.window = {};
      require("./mvp_vertical/cockpit/spatial_navigation.js");
      const nav = window.PantheonSpatialNavigation.create({
        root_collection_id: "primary-spaces",
        root_item_ids: ["pantheon", "affaires", "knowledge", "tools"],
      });
      nav.selectSibling("affaires");
      if (nav.snapshot().current_id !== "affaires") throw new Error("root selection failed");
      nav.descend({ parent_entity_id: "affaires", collection_id: "projects", item_ids: ["lieurey", "trouville", "mannevillette"] });
      nav.moveHorizontal(1);
      if (nav.snapshot().current_id !== "trouville") throw new Error("sibling navigation escaped collection");
      if (nav.snapshot().depth !== 1) throw new Error("horizontal navigation changed depth");
      nav.ascend();
      if (nav.snapshot().current_id !== "affaires" || nav.snapshot().depth !== 0) throw new Error("ascend did not restore parent");
      nav.returnToRoot("tools");
      if (nav.snapshot().current_id !== "tools") throw new Error("explicit root jump failed");
    '''
    result = _run_node(script)
    assert result.returncode == 0, result.stderr


def test_v2_route_exposes_four_spaces_and_live_agency_project_collection() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    bootstrap = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")
    cards_css = (COCKPIT / "styles" / "cards.css").read_text(encoding="utf-8")
    families_css = (COCKPIT / "styles" / "families.css").read_text(encoding="utf-8")
    javascript = PROJECTION.read_text(encoding="utf-8")
    assembler = ASSEMBLER.read_text(encoding="utf-8")
    data_loader = DATA_LOADER.read_text(encoding="utf-8")
    for space in ("pantheon", "affaires", "connaissances", "outils"):
        assert f'data-space="{space}"' in html
    assert 'data-space="decisions"' not in html
    for control in ("v2-previous", "v2-next", "v2-descend", "v2-ascend", "v2-flip", "v2-breadcrumb", "v2-project", "v2-token", "v2-load"):
        assert f'id="{control}"' in html
    assert 'class="v2-hermes-dock"' in html
    assert 'src="cockpit_bootstrap.js"' in html
    for module in (
        "spatial_navigation.js",
        "projection/navigation_registry_adapter.js",
        "projection/child_collection_assembler.js",
        "projection/cockpit_projection.js",
        "actions/card_actions.js",
    ):
        assert f'"{module}"' in bootstrap
    assert 'v2_' + 'app_schema.js' not in bootstrap
    assert 'v2_app.js' not in bootstrap
    assert 'params.get("mode") === "demo"' in bootstrap
    assert 'import("./demo_bootstrap.js")' in bootstrap
    for family in ("project", "information", "contact", "work", "decision", "tool"):
        assert f'[data-family="{family}"]' in families_css or f'[data-kind="{family}"]' in families_css
    assert 'prefers-reduced-motion: reduce' not in cards_css
    assert '.indicator-rail' in cards_css
    assert '.card-back' in cards_css
    assert "navigationProjection.rootItemIds" in javascript
    assert "navigationProjection.sourcesFor" in javascript
    assert 'space:decisions' not in javascript
    for operation in ("state.navigator.descend", "state.navigator.ascend", "state.navigator.returnToRoot"):
        assert operation in javascript
    assert 'state.flipped' in javascript
    assert 'PostgreSQL Agency Data' in javascript
    assert '../v1/agency/projects?limit=200' in data_loader
    assert "dataLoader.loadAgencyProjects(state.token)" in javascript
    assert "Array.isArray(payload.projects) ? payload.projects : []" in data_loader
    assert 'entity_type: "project_contacts"' in javascript
    assert 'title: "Contacts"' in javascript
    assert "projects(context)" in assembler
    assert '/participations' not in javascript


def test_pantheon_projects_decisions_and_current_runs_without_changing_authority() -> None:
    javascript = PROJECTION.read_text(encoding="utf-8")
    assembler = ASSEMBLER.read_text(encoding="utf-8")
    demo = (COCKPIT / "v3" / "providers" / "demo_provider.js").read_text(encoding="utf-8")
    assert "pending_change_candidates(context)" in assembler
    assert "work_decisions(context)" in assembler
    assert "current_runs(context)" in assembler
    assert 'entity_type: "work_decision"' in javascript
    assert 'entity_type: "project_change_candidate"' in javascript
    assert 'entity_type: item.entity_type || "hermes_run"' in javascript
    assert 'available_actions: item.available_actions || []' in javascript
    assert 'window.addEventListener("pantheon:current-runs"' in javascript
    assert 'if (item.id === "space:pantheon")' in demo
    assert 'return [...decisionModels(), ...activeRunModels()]' in demo
    assert 'space:decisions' not in demo


def test_v2_handoff_never_dispatches_or_starts_hermes_from_spatial_ui() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    handoff = (COCKPIT / "handoff" / "handoff_lifecycle.js").read_text(encoding="utf-8")
    app = PROJECTION.read_text(encoding="utf-8")
    actions = (COCKPIT / "actions" / "card_actions.js").read_text(encoding="utf-8")
    for control in ("v2-handoff-submit", "v2-handoff-admit", "v2-handoff-revoke"):
        assert f'id="{control}"' in html
    assert '>Admettre</button>' in html
    assert '>Révoquer</button>' in html
    assert '../v1/cockpit/hermes-handoffs/submit' in handoff
    assert '/admissions`' in handoff
    assert '/revocations`' in handoff
    assert '/runs/start' not in handoff
    assert '/v1/hermes/execution-admissions' not in handoff
    assert '$("v2-handoff-prepare")?.click()' in actions
    assert '$("v2-handoff-submit")?.click()' not in actions
    assert '$("v2-handoff-admit")?.click()' not in actions
    assert "direct_database_credentials" not in app
    assert "notion_token" not in app.lower()
