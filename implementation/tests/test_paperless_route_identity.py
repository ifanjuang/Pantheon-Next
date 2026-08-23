"""Stable route identity for the optional Paperless resource binding."""

from mvp_vertical.paperless_gateway import create_app


def test_paperless_gateway_mounts_only_binding_specific_stable_routes() -> None:
    app = create_app(read_api_key="read-key", hermes_api_key="hermes-key")
    routes = {
        (method, route.path)
        for route in app.routes
        for method in getattr(route, "methods", set())
    }

    expected = {
        ("GET", "/resources/paperless/documents"),
        ("GET", "/resources/paperless/documents/{document_id}"),
        ("GET", "/resources/paperless/documents/{document_id}/capture"),
        ("GET", "/resources/paperless/tasks/{task_id}"),
        ("POST", "/resources/paperless/intakes"),
        ("POST", "/resources/paperless/documents/{document_id}/metadata"),
    }

    assert expected <= routes
    assert not {
        (method, path.replace("/resources/paperless", "/v1/paperless"))
        for method, path in expected
    } & routes


def test_paperless_route_family_keeps_optional_binding_identity() -> None:
    app = create_app(read_api_key="read-key", hermes_api_key="hermes-key")
    paperless_paths = {
        route.path
        for route in app.routes
        if "paperless" in getattr(route, "path", "")
    }

    assert paperless_paths
    assert all(path.startswith("/resources/paperless/") for path in paperless_paths)
    assert not any(path.startswith("/documents/") for path in paperless_paths)
    assert not any(path.startswith("/agency/") for path in paperless_paths)
