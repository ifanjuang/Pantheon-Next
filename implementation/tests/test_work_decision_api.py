from fastapi.testclient import TestClient

from mvp_vertical.cockpit_shell import create_cockpit_app


def test_work_decision_routes_are_installed_and_require_editor_key():
    app = create_cockpit_app(
        connect_fn=lambda: None,
        initialize_fn=None,
        api_key="read-key",
        editor_api_key="editor-key",
        hermes_api_key="hermes-key",
    )
    paths = {route.path for route in app.routes}
    assert "/v1/work-issues/{issue_id}/decision" in paths
    assert "/v1/work-issues/{issue_id}/decision/validate" in paths
    assert "/v1/work-issues/{issue_id}/decision/refuse" in paths

    client = TestClient(app)
    response = client.get("/v1/work-issues/issue-1/decision")
    assert response.status_code == 401


def test_v2_action_module_is_loaded_and_keeps_hermes_as_prepare_only():
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    cockpit = root / "mvp_vertical" / "cockpit"
    bootstrap = (cockpit / "live_bootstrap.js").read_text(encoding="utf-8")
    actions = (cockpit / "v2_actions.js").read_text(encoding="utf-8")

    assert '"v2_actions.js"' in bootstrap
    assert '$("v2-handoff-prepare")?.click()' in actions
    assert '$("v2-handoff-submit")?.click()' not in actions
    assert '$("v2-handoff-admit")?.click()' not in actions
    assert '"/act"' not in actions  # path is assembled with the exact information id
    assert "/decision/validate" not in actions  # path is assembled from the selected action
    assert 'expected_revision: current.revision' in actions
    assert 'expected_version: issue.version' in actions
