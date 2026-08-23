"""Shared route identity for local and network document observers."""

from mvp_vertical.document_runtime_network_observer import create_app as create_network_app
from mvp_vertical.document_runtime_observer import create_app as create_local_app


def _routes(app):
    return {
        (method, route.path)
        for route in app.routes
        for method in getattr(route, "methods", set())
    }


def test_local_and_network_bindings_share_one_stable_observation_contract() -> None:
    expected = ("GET", "/documents/observations")
    retired = ("GET", "/v1/document-runtime/observations")

    for app in (create_local_app(read_api_key="read-key"), create_network_app(read_api_key="read-key")):
        routes = _routes(app)
        assert expected in routes
        assert retired not in routes
        assert ("GET", "/health") in routes


def test_observer_route_does_not_imply_global_health_or_authority() -> None:
    payload = {
        "object_type": "document_runtime_observation_set",
        "observations": [],
        "synthetic_global_health": "not_computed",
        "authority_effect": "none",
        "write_effect": False,
        "activation_changed": False,
    }

    for factory in (create_local_app, create_network_app):
        app = factory(read_api_key="read-key", collector=lambda **_kwargs: payload)
        route = next(route for route in app.routes if getattr(route, "path", None) == "/documents/observations")
        assert route.methods == {"GET"}
