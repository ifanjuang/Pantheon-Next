from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from mvp_vertical.openwebui_capabilities import (
    OpenWebUICapabilityError,
    project_openwebui_capabilities,
)
from mvp_vertical.openwebui_capability_api import create_openwebui_capability_router


def test_projection_preserves_authorization_boundaries():
    projection = project_openwebui_capabilities(
        {
            "knowledge_ui": {
                "availability": True,
                "installed": True,
                "healthy": True,
            }
        },
        version="0.9.5",
        endpoint="http://openwebui:8080",
    )

    knowledge = next(
        item for item in projection["capabilities"] if item["id"] == "knowledge_ui"
    )
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


def test_route_requires_injected_read_guard_and_returns_projection():
    app = FastAPI()

    def require_read_key():
        return None

    app.include_router(
        create_openwebui_capability_router(
            require_read_key=require_read_key,
            observation_provider=lambda: {
                "version": "0.9.5",
                "endpoint": "http://openwebui:8080",
                "capabilities": {
                    "conversation_folders": {
                        "availability": True,
                        "installed": True,
                        "healthy": True,
                    }
                },
            },
        )
    )

    response = TestClient(app).get("/v1/system/capabilities/openwebui")
    assert response.status_code == 200
    body = response.json()
    assert body["detected_version"] == "0.9.5"
    assert body["endpoint"] == "http://openwebui:8080"
