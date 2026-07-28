from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_demo_reuses_v2_styles_and_not_legacy_demo_assets():
    html = (COCKPIT / "demo.html").read_text(encoding="utf-8")

    assert 'href="styles/v2.css"' in html
    assert 'href="styles/v2_refinement.css"' in html
    assert 'src="demo_bootstrap.js"' in html
    assert "styles/demo.css" not in html
    assert 'src="demo.js"' not in html


def test_demo_bootstrap_loads_the_same_v2_modules():
    bootstrap = (COCKPIT / "demo_bootstrap.js").read_text(encoding="utf-8")
    v2_html = (COCKPIT / "v2.html").read_text(encoding="utf-8")

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
    for module in modules:
        assert module in v2_html
        assert module in bootstrap


def test_demo_fixture_is_fictional_and_read_only():
    fixture = json.loads((COCKPIT / "demo-data.json").read_text(encoding="utf-8"))
    bootstrap = (COCKPIT / "demo_bootstrap.js").read_text(encoding="utf-8")

    assert {project["project_id"] for project in fixture["projects"]} == {
        "demo-orangerie",
        "demo-atelier",
    }
    assert "Démonstration statique : écriture désactivée" in bootstrap
    assert 'method !== "GET"' in bootstrap
    assert "demo-data.json" in bootstrap
