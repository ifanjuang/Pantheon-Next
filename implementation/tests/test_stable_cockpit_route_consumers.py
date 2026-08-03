"""Static guards for stable Cockpit and Agency route consumers."""

from pathlib import Path

from mvp_vertical.cockpit_shell import create_cockpit_app


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
MOBILE_EDITOR = ROOT / "mvp_vertical" / "mobile_editor" / "app.js"


def test_composed_app_mounts_only_stable_cockpit_shell_routes() -> None:
    app = create_cockpit_app(connect_fn=lambda: None)
    routes = {
        (method, route.path)
        for route in app.routes
        for method in getattr(route, "methods", set())
    }

    expected = {
        ("GET", "/projects/{parent_project_id}/resource-profiles"),
        ("POST", "/projects/{parent_project_id}/effects/preview"),
        (
            "POST",
            "/projects/{parent_project_id}/knowledge/{knowledge_id}/navigation-profiles/preview",
        ),
        (
            "POST",
            "/projects/{parent_project_id}/knowledge/{knowledge_id}/site-manifests/preview",
        ),
        (
            "POST",
            "/projects/{parent_project_id}/knowledge/{knowledge_id}/updates/preview",
        ),
        (
            "POST",
            "/projects/{parent_project_id}/knowledge/{knowledge_id}/updates/apply",
        ),
    }
    retired = {(method, f"/v1{path}") for method, path in expected}

    assert expected <= routes
    assert not (retired & routes)


def test_mobile_editor_uses_stable_update_routes_without_migrating_document_reads() -> None:
    source = MOBILE_EDITOR.read_text(encoding="utf-8")

    assert (
        "../projects/${encodeURIComponent(state.project)}/knowledge/"
        "${encodeURIComponent(state.current.knowledge_id)}/updates/preview"
    ) in source
    assert (
        "../projects/${encodeURIComponent(state.project)}/knowledge/"
        "${encodeURIComponent(pending.knowledgeId)}/updates/apply"
    ) in source
    assert "/v1/projects/${encodeURIComponent(state.project)}/knowledge/" not in source.split(
        "updates/preview"
    )[0][-180:]

    # Document/Knowledge reads and edit requests belong to the later Documents slice.
    assert "../v1/projects/${encodeURIComponent(state.project)}/knowledge" in source
    assert "../v1/knowledge/${encodeURIComponent(item.knowledge_id)}/markdown" in source
    assert "../v1/knowledge/${encodeURIComponent(operation.knowledge_id)}/edit-requests" in source


def test_active_agency_cockpit_consumers_have_no_retired_prefix() -> None:
    context = (COCKPIT / "context" / "context_selection.js").read_text(encoding="utf-8")
    information = (COCKPIT / "information_view_adapter.js").read_text(encoding="utf-8")

    assert "/v1/agency/" not in context
    assert "/v1/agency/" not in information
    assert "../agency/projects?" in context
    assert "../agency/information/" in information
