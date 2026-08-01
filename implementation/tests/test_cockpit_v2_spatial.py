"""Behavior and boundary checks for the executable Cockpit V2 spatial surface."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def _run_node(script: str) -> subprocess.CompletedProcess[str]:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - depends on runner image
        pytest.skip("Node.js is unavailable; JavaScript behavior check skipped")
    return subprocess.run(
        [node, "-e", script],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


@pytest.mark.parametrize("name", ["spatial_navigation.js", "v2_app_schema.js", "actions/card_actions.js", "live_bootstrap.js"])
def test_v2_javascript_parses(name: str) -> None:
    node = shutil.which("node")
    if node is None:  # pragma: no cover
        pytest.skip("Node.js is unavailable; JavaScript syntax check skipped")
    result = subprocess.run(
        [node, "--check", str(COCKPIT / name)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_spatial_navigation_keeps_sibling_and_parent_boundaries() -> None:
    script = r'''
      global.window = {};
      require("./mvp_vertical/cockpit/spatial_navigation.js");
      const nav = window.PantheonSpatialNavigation.create({
        root_collection_id: "primary-spaces",
        root_item_ids: ["pantheon", "decisions", "affaires", "knowledge", "tools"],
      });

      nav.selectSibling("affaires");
      if (nav.snapshot().current_id !== "affaires") throw new Error("root selection failed");

      nav.descend({
        parent_entity_id: "affaires",
        collection_id: "projects",
        item_ids: ["lieurey", "trouville", "mannevillette"],
      });
      nav.moveHorizontal(1);
      if (nav.snapshot().current_id !== "trouville") throw new Error("sibling navigation escaped collection");
      if (nav.snapshot().depth !== 1) throw new Error("horizontal navigation changed depth");

      nav.ascend();
      if (nav.snapshot().current_id !== "affaires" || nav.snapshot().depth !== 0) {
        throw new Error("ascend did not restore parent");
      }

      nav.returnToRoot("tools");
      if (nav.snapshot().current_id !== "tools") throw new Error("explicit root jump failed");
    '''
    result = _run_node(script)
    assert result.returncode == 0, result.stderr


def test_v2_route_exposes_five_spaces_and_live_agency_project_collection() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    bootstrap = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")
    cards_css = (COCKPIT / "styles" / "cards.css").read_text(encoding="utf-8")
    families_css = (COCKPIT / "styles" / "families.css").read_text(encoding="utf-8")
    javascript = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")

    for space in ("pantheon", "decisions", "affaires", "connaissances", "outils"):
        assert f'data-space="{space}"' in html

    assert 'id="v2-previous"' in html
    assert 'id="v2-next"' in html
    assert 'id="v2-descend"' in html
    assert 'id="v2-ascend"' in html
    assert 'id="v2-flip"' in html
    assert 'id="v2-breadcrumb"' in html
    assert 'class="v2-hermes-dock"' in html
    assert 'id="v2-project"' in html
    assert 'id="v2-token"' in html
    assert 'id="v2-load"' in html
    assert 'src="cockpit_bootstrap.js"' in html
    assert '"spatial_navigation.js"' in bootstrap
    assert '"v2_app_schema.js"' in bootstrap
    assert '"actions/card_actions.js"' in bootstrap
    assert 'v2_app.js' not in bootstrap
    assert 'params.get("mode") === "demo"' in bootstrap
    assert 'import("./demo_bootstrap.js")' in bootstrap

    for family in ("project", "information", "contact", "work", "decision", "tool"):
        assert f'[data-family="{family}"]' in families_css or f'[data-kind="{family}"]' in families_css
    assert 'prefers-reduced-motion: reduce' in cards_css
    assert '.indicator-rail' in cards_css
    assert '.card-back' in cards_css

    assert 'ROOT_SPACES = ["pantheon", "decisions", "affaires", "connaissances", "outils"]' in javascript
    assert 'state.navigator.descend' in javascript
    assert 'state.navigator.ascend' in javascript
    assert 'state.navigator.returnToRoot' in javascript
    assert 'state.flipped' in javascript
    assert 'PostgreSQL Agency Data' in javascript
    assert '../v1/agency/projects?limit=200' in javascript
    assert 'state.projects = payload.projects || []' in javascript
    assert 'entity_type: "project_contacts"' in javascript
    assert 'title: "Contacts"' in javascript
    assert '/participations' not in javascript


def test_v2_handoff_never_dispatches_or_starts_hermes_from_spatial_ui() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    handoff = (COCKPIT / "v2_handoff.js").read_text(encoding="utf-8")
    app = (COCKPIT / "v2_app_schema.js").read_text(encoding="utf-8")
    actions = (COCKPIT / "actions" / "card_actions.js").read_text(encoding="utf-8")

    assert 'id="v2-handoff-submit"' in html
    assert 'id="v2-handoff-admit"' in html
    assert 'id="v2-handoff-revoke"' in html
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
