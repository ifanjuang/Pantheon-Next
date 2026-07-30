from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_demo_redirects_to_cockpit_v3_and_not_legacy_demo_assets():
    # Per issue #108, demo.html points at Cockpit V3 (v3.html?mode=demo) and does
    # not load the legacy demo assets directly.
    html = (COCKPIT / "demo.html").read_text(encoding="utf-8")

    assert "index.html?mode=demo" in html
    assert "v2.html?mode=demo" not in html
    assert 'href="styles/demo.css"' not in html
    assert '<script src="demo.js"' not in html
    assert '<script src="app.js"' not in html


def test_demo_bootstrap_loads_the_same_v2_modules():
    # v2.html loads every cockpit module through v2_bootstrap.js; the demo path
    # reuses the same modules via demo_bootstrap.js.
    demo_bootstrap = (COCKPIT / "demo_bootstrap.js").read_text(encoding="utf-8")
    v2_bootstrap = (COCKPIT / "v2_bootstrap.js").read_text(encoding="utf-8")
    v2_html = (COCKPIT / "index.html").read_text(encoding="utf-8")

    assert 'src="v3_bootstrap.js"' in v2_html

    modules = [
        "structured_interface.js",
        "context_resolver.js",
        "agency_data_binding.js",
        "spatial_navigation.js",
        "v2_app_schema.js",
        "v2_interaction_policy.js",
        "project_claim_view_adapter.js",
        "information_view_adapter.js",
        "v2_context.js",
        "v2_handoff.js",
        "v2_actions.js",
        "v2_candidate_actions.js",
        "schema_editor.js",
        "contacts_editor.js",
        "information_create.js",
    ]
    # demo_bootstrap.js is the demo-only read-only data setup entry point.
    assert "demo-data.json" in demo_bootstrap
    for module in modules:
        assert module in v2_bootstrap


def test_demo_fixture_is_fictional_and_read_only():
    fixture = json.loads((COCKPIT / "demo-data.json").read_text(encoding="utf-8"))
    bootstrap = (COCKPIT / "demo_bootstrap.js").read_text(encoding="utf-8")

    assert {project["project_id"] for project in fixture["projects"]} == {
        "demo-vallons",
        "demo-falaises",
        "demo-horizon",
        "demo-tilleuls",
    }
    assert "Démonstration statique : écriture désactivée" in bootstrap
    assert 'method !== "GET"' in bootstrap
    assert "demo-data.json" in bootstrap
