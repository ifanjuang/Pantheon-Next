"""Tests for the candidate native Hermes Pantheon context bridge plugin."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

PLUGIN_DIR = Path(__file__).resolve().parents[1] / "hermes" / "plugins" / "pantheon-context-bridge"


def _load_module(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, PLUGIN_DIR / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _load_package():
    name = "pantheon_context_bridge_test_plugin"
    spec = importlib.util.spec_from_file_location(
        name,
        PLUGIN_DIR / "__init__.py",
        submodule_search_locations=[str(PLUGIN_DIR)],
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class _Response:
    def __init__(self, payload: dict):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, _limit):
        return json.dumps(self.payload).encode("utf-8")


class _Context:
    def __init__(self):
        self.tools = []

    def register_tool(self, **kwargs):
        self.tools.append(kwargs)


def test_manifest_declares_only_two_read_only_context_tools_and_required_env() -> None:
    manifest = (PLUGIN_DIR / "plugin.yaml").read_text(encoding="utf-8")
    assert "pantheon_context_manifest" in manifest
    assert "pantheon_context_entity" in manifest
    assert "PANTHEON_HERMES_API_BASE" in manifest
    assert "PANTHEON_HERMES_API_KEY" in manifest
    assert "terminal" not in manifest
    assert "write" not in manifest.lower()

    schemas = _load_module("schemas.py", "pantheon_context_bridge_schemas_test")
    entity_schema = schemas.PANTHEON_CONTEXT_ENTITY["parameters"]
    assert "admission_id" not in entity_schema["properties"]
    assert "run_id" not in entity_schema["properties"]
    assert entity_schema["additionalProperties"] is False
    assert schemas.PANTHEON_CONTEXT_MANIFEST["parameters"]["properties"] == {}


def test_plugin_registers_only_reviewed_toolset() -> None:
    plugin = _load_package()
    ctx = _Context()
    plugin.register(ctx)
    assert [item["name"] for item in ctx.tools] == [
        "pantheon_context_manifest",
        "pantheon_context_entity",
    ]
    assert {item["toolset"] for item in ctx.tools} == {"pantheon_context"}


def test_manifest_handler_derives_admission_only_from_host_task_id(monkeypatch) -> None:
    tools = _load_module("tools.py", "pantheon_context_bridge_tools_manifest_test")
    monkeypatch.setenv("PANTHEON_HERMES_API_BASE", "http://pantheon:8000")
    monkeypatch.setenv("PANTHEON_HERMES_API_KEY", "secret")
    seen = {}

    def fake_urlopen(request, timeout):
        seen["url"] = request.full_url
        seen["method"] = request.get_method()
        seen["auth"] = request.get_header("Authorization")
        seen["actor"] = request.get_header("X-pantheon-hermes-actor")
        seen["timeout"] = timeout
        return _Response({"kind": "hermes_scoped_context_manifest", "entities": []})

    monkeypatch.setattr(tools, "urlopen", fake_urlopen)
    out = json.loads(
        tools.pantheon_context_manifest(
            {"admission_id": "admission-model-selected-ignored"},
            task_id="admission-host-session-123",
        )
    )
    assert out["kind"] == "hermes_scoped_context_manifest"
    assert seen["method"] == "GET"
    assert seen["url"].endswith(
        "/hermes/execution-admissions/admission-host-session-123/active-context"
    )
    assert "/v1/hermes/" not in seen["url"]
    assert "model-selected" not in seen["url"]
    assert seen["auth"] == "Bearer secret"
    assert seen["actor"] == "hermes-plugin:pantheon-context-bridge"


def test_entity_handler_uses_host_admission_and_only_model_selected_in_scope_entity(monkeypatch) -> None:
    tools = _load_module("tools.py", "pantheon_context_bridge_tools_entity_test")
    monkeypatch.setenv("PANTHEON_HERMES_API_BASE", "https://pantheon.example")
    monkeypatch.setenv("PANTHEON_HERMES_API_KEY", "secret")
    seen = {}

    def fake_urlopen(request, timeout):
        del timeout
        seen["url"] = request.full_url
        seen["method"] = request.get_method()
        return _Response({"kind": "hermes_scoped_context_entity", "record": {"project_id": "p1"}})

    monkeypatch.setattr(tools, "urlopen", fake_urlopen)
    out = json.loads(
        tools.pantheon_context_entity(
            {
                "entity_type": "project",
                "entity_id": "project:p1",
                "admission_id": "admission-evil",
                "run_id": "run-evil",
            },
            task_id="admission-real",
        )
    )
    assert out["record"]["project_id"] == "p1"
    assert seen["method"] == "GET"
    assert "/admission-real/active-context/entities/project/project%3Ap1" in seen["url"]
    assert "/v1/hermes/" not in seen["url"]
    assert "admission-evil" not in seen["url"]
    assert "run-evil" not in seen["url"]


def test_missing_or_non_admission_host_context_fails_closed(monkeypatch) -> None:
    tools = _load_module("tools.py", "pantheon_context_bridge_tools_refusal_test")
    monkeypatch.setenv("PANTHEON_HERMES_API_BASE", "http://pantheon")
    monkeypatch.setenv("PANTHEON_HERMES_API_KEY", "secret")

    missing = json.loads(tools.pantheon_context_manifest({}))
    assert "task_id is required" in missing["error"]

    wrong = json.loads(tools.pantheon_context_manifest({}, task_id="run-123"))
    assert "not a Pantheon admission identity" in wrong["error"]


def test_missing_plugin_environment_fails_closed(monkeypatch) -> None:
    tools = _load_module("tools.py", "pantheon_context_bridge_tools_env_test")
    monkeypatch.delenv("PANTHEON_HERMES_API_BASE", raising=False)
    monkeypatch.delenv("PANTHEON_HERMES_API_KEY", raising=False)
    out = json.loads(tools.pantheon_context_manifest({}, task_id="admission-123"))
    assert "environment is incomplete" in out["error"]