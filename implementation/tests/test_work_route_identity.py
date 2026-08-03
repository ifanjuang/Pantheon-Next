"""Stable route-identity guards for Work Issue reads and human decisions."""

from __future__ import annotations

from pathlib import Path

from mvp_vertical.cockpit_shell import create_cockpit_app


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


class _Connection:
    def close(self) -> None:
        pass


def test_mounted_work_routes_use_stable_responsibility_paths() -> None:
    app = create_cockpit_app(
        connect_fn=_Connection,
        initialize_fn=None,
        api_key="read-key",
        editor_api_key="editor-key",
        hermes_api_key="hermes-key",
    )
    mounted = {route.path for route in app.routes if getattr(route, "path", None)}

    assert "/work/issues" in mounted
    assert "/work/issues/{issue_id}/decision" in mounted
    assert "/work/issues/{issue_id}/decision/validate" in mounted
    assert "/work/issues/{issue_id}/decision/refuse" in mounted
    assert "/v1/projects/{parent_project_id}/work-issues" not in mounted
    assert not [path for path in mounted if path.startswith("/v1/work-issues")]


def test_active_cockpit_consumers_do_not_publish_old_work_routes() -> None:
    consumers = (
        COCKPIT / "data" / "cockpit_data_loader.js",
        COCKPIT / "demo_bootstrap.js",
        COCKPIT / "actions" / "card_actions.js",
    )
    for path in consumers:
        content = path.read_text(encoding="utf-8")
        assert "/v1/work-issues" not in content, path
        assert "/work-issues" not in content, path

    loader = consumers[0].read_text(encoding="utf-8")
    demo = consumers[1].read_text(encoding="utf-8")
    actions = consumers[2].read_text(encoding="utf-8")
    assert "../work/issues?case_ref=${encoded}" in loader
    assert 'url.pathname.endsWith("/work/issues")' in demo
    assert '../work/issues/${encodeURIComponent(issueId)}/decision' in actions


def test_unrelated_route_families_remain_outside_work_migration() -> None:
    loader = (COCKPIT / "data" / "cockpit_data_loader.js").read_text(encoding="utf-8")
    actions = (COCKPIT / "actions" / "card_actions.js").read_text(encoding="utf-8")

    assert "../v1/projects/${encoded}/documents" in loader
    assert "../v1/projects/${encoded}/knowledge" in loader
    assert "../v1/documents/${encodeURIComponent(id)}/chunks" in actions
