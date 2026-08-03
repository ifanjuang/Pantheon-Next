from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from mvp_vertical.openwebui_capabilities import (
    OpenWebUICapabilityError,
    project_openwebui_capabilities,
    project_openwebui_resource,
)
from mvp_vertical.openwebui_capability_api import create_openwebui_capability_router


def test_projection_preserves_authorization_boundaries():
    projection = project_openwebui_capabilities(
        {"knowledge_ui": {"availability": True, "installed": True, "healthy": True}},
        version="0.9.5",
        endpoint="http://openwebui:8080",
    )
    knowledge = next(item for item in projection["capabilities"] if item["id"] == "knowledge_ui")
    assert knowledge["availability"] is True
    assert knowledge["installed"] is True
    assert knowledge["healthy"] is True
    assert knowledge["activated"] is False
    assert knowledge["task_authorized"] is False
    assert projection["authority"] == "projection_only"
    assert projection["status"] == "observed_not_authoritative"


def test_projection_refuses_unknown_capability_ids():
    with pytest.raises(OpenWebUICapabilityError):
        project_openwebui_capabilities({"invented_runtime": {"healthy": True}})


def test_resource_projection_uses_generic_tool_card_shape():
    resource = project_openwebui_resource(
        {"knowledge_ui": {"availability": True, "installed": True, "healthy": True}},
        version="0.9.5",
        endpoint="http://openwebui:8080",
    )
    assert resource["tool_id"] == "openwebui"
    assert resource["resource_type"] == "infrastructure_module"
    assert resource["installation_state"] == "installed_observed"
    assert resource["health_state"] == "healthy_observed"
    assert resource["activation_state"] == "not_activated"
    assert resource["task_authorization_state"] == "not_authorized"
    assert resource["authority"] == "projection_only"
    assert resource["detected_version"] == "0.9.5"
    assert all(not binding["activated"] and not binding["task_authorized"] for binding in resource["capability_bindings"])


def test_unobserved_values_remain_explicitly_unobserved():
    resource = project_openwebui_resource()
    assert resource["installation_state"] == "not_observed"
    assert resource["health_state"] == "not_observed"
    assert resource["native_state"] == "not_observed"
    assert resource["detected_version"] == "not_observed"
    assert resource["endpoint"] == "not_observed"


def test_routes_require_injected_read_guard_and_return_both_projections():
    app = FastAPI()
    app.include_router(
        create_openwebui_capability_router(
            require_read_key=lambda: None,
            observation_provider=lambda: {
                "version": "0.9.5",
                "endpoint": "http://openwebui:8080",
                "capabilities": {"conversation_folders": {"availability": True, "installed": True, "healthy": True}},
            },
        )
    )
    client = TestClient(app)
    capability_response = client.get("/capabilities/openwebui")
    assert capability_response.status_code == 200
    assert capability_response.json()["detected_version"] == "0.9.5"
    assert capability_response.json()["endpoint"] == "http://openwebui:8080"
    resource_response = client.get("/resources/openwebui")
    assert resource_response.status_code == 200
    resource_body = resource_response.json()
    assert resource_body["tool_id"] == "openwebui"
    assert resource_body["resource_type"] == "infrastructure_module"
    assert resource_body["activation_state"] == "not_activated"
    assert resource_body["task_authorization_state"] == "not_authorized"
    assert client.get("/v1/system/capabilities/openwebui").status_code == 404
    assert client.get("/v1/system/resources/openwebui").status_code == 404
