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
    assert "/work/issues/{issue_id}/decision" in paths
    assert "/work/issues/{issue_id}/decision/validate" in paths
    assert "/work/issues/{issue_id}/decision/refuse" in paths
    assert not [path for path in paths if path.startswith("/v1/work-issues")]

    client = TestClient(app)
    response = client.get("/work/issues/issue-1/decision")
    assert response.status_code == 401


def test_card_action_module_is_loaded_and_keeps_hermes_as_prepare_only():
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]
    cockpit = root / "mvp_vertical" / "cockpit"
    bootstrap = (cockpit / "live_bootstrap.js").read_text(encoding="utf-8")
    actions = (cockpit / "actions" / "card_actions.js").read_text(encoding="utf-8")

    assert '"actions/card_actions.js"' in bootstrap
    assert '$("v2-handoff-prepare")?.click()' in actions
    assert '$("v2-handoff-submit")?.click()' not in actions
    assert '$("v2-handoff-admit")?.click()' not in actions
    assert '../agency/information/${encodeURIComponent(id)}/context' in actions
    assert '../agency/information/${encodeURIComponent(id)}/act' in actions
    assert '../agency/information/${encodeURIComponent(id)}/working-version' in actions
    assert '../work/issues/${encodeURIComponent(issueId)}/decision' in actions
    assert 'decision/${validate ? "validate" : "refuse"}' in actions
    assert "/v1/agency/" not in actions
    assert "/v1/work-issues/" not in actions
    assert 'expected_revision: current.revision' in actions
    assert 'expected_version: issue.version' in actions
