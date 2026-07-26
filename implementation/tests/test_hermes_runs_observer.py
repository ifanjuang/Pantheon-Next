"""Tests for read-only Hermes Runs API contract observation."""

from __future__ import annotations

import httpx
import pytest

from mvp_vertical.hermes_runs_observer import HermesRunsApiObserver, HermesRunsObservationError

BASE = "http://hermes:8642"


def _client(handler):
    return httpx.Client(transport=httpx.MockTransport(handler))


def _capabilities(**feature_overrides):
    features = {
        "chat_completions": True,
        "responses_api": True,
        "run_submission": True,
        "run_status": True,
        "run_events_sse": True,
        "run_stop": True,
        "run_approval": True,
    }
    features.update(feature_overrides)
    return {
        "object": "hermes.api_server.capabilities",
        "platform": "hermes-agent",
        "model": "pantheon-governed",
        "auth": {"type": "bearer", "required": True},
        "features": features,
        "endpoints": {
            "run_submit": "/v1/runs",
            "run_status": "/v1/runs/{run_id}",
            "toolsets": "/v1/toolsets",
        },
    }


def test_observer_reads_only_capabilities_and_toolsets_and_performs_no_effect() -> None:
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append((request.method, request.url.path, request.headers.get("authorization")))
        if request.url.path == "/v1/capabilities":
            return httpx.Response(200, json=_capabilities())
        if request.url.path == "/v1/toolsets":
            return httpx.Response(200, json=[{
                "name": "mcp-pantheon",
                "enabled": True,
                "configured": True,
                "tools": ["pantheon_context_manifest", "pantheon_context_entity"],
            }])
        raise AssertionError(f"unexpected request {request.method} {request.url.path}")

    observed = HermesRunsApiObserver(
        BASE,
        "api-key",
        allowed_tools={"pantheon_context_manifest", "pantheon_context_entity"},
        required_tools={"pantheon_context_manifest", "pantheon_context_entity"},
        client=_client(handler),
    ).observe()

    assert observed["runs_api_status"] == "compatible"
    assert observed["safety_status"] == "qualified"
    assert observed["tool_surface"]["active_toolsets"] == ["mcp-pantheon"]
    assert observed["run_submission_performed"] is False
    assert observed["run_stop_performed"] is False
    assert observed["approval_effect_performed"] is False
    assert observed["write_effect"] is False
    assert observed["authority_effect"] == "none"
    assert seen == [
        ("GET", "/v1/capabilities", "Bearer api-key"),
        ("GET", "/v1/toolsets", "Bearer api-key"),
    ]


def test_full_or_extra_runtime_tool_surface_is_not_qualified() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/capabilities":
            return httpx.Response(200, json=_capabilities())
        return httpx.Response(200, json=[{
            "name": "hermes-api-server",
            "enabled": True,
            "configured": True,
            "tools": ["pantheon_context_manifest", "pantheon_context_entity", "terminal", "write_file"],
        }])

    observed = HermesRunsApiObserver(
        BASE,
        "api-key",
        allowed_tools={"pantheon_context_manifest", "pantheon_context_entity"},
        required_tools={"pantheon_context_manifest"},
        client=_client(handler),
    ).observe()
    assert observed["runtime_reachable"] is True
    assert observed["runs_api_status"] == "compatible"
    assert observed["safety_status"] == "not_qualified"
    assert observed["tool_surface"]["unexpected_tools"] == ["terminal", "write_file"]


def test_without_reviewed_allowlist_safety_remains_not_evaluated() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/capabilities":
            return httpx.Response(200, json=_capabilities())
        return httpx.Response(200, json=[{
            "name": "hermes-api-server",
            "enabled": True,
            "configured": True,
            "tools": ["terminal", "write_file"],
        }])

    observed = HermesRunsApiObserver(BASE, "api-key", client=_client(handler)).observe()
    assert observed["runs_api_status"] == "compatible"
    assert observed["safety_status"] == "not_evaluated"
    assert "terminal" in observed["tool_surface"]["active_tools"]


def test_missing_runs_feature_marks_contract_incomplete_without_side_effect() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/capabilities":
            return httpx.Response(200, json=_capabilities(run_events_sse=False))
        return httpx.Response(200, json=[])

    observed = HermesRunsApiObserver(BASE, "api-key", client=_client(handler)).observe()
    assert observed["runs_api_status"] == "incomplete"
    assert observed["missing_run_features"] == ["run_events_sse"]
    assert observed["run_submission_performed"] is False


def test_toolset_disabled_or_unconfigured_does_not_count_as_active() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/capabilities":
            return httpx.Response(200, json=_capabilities())
        return httpx.Response(200, json=[
            {"name": "mcp-pantheon", "enabled": True, "configured": True, "tools": ["pantheon_context_manifest"]},
            {"name": "terminal", "enabled": False, "configured": True, "tools": ["terminal"]},
            {"name": "file", "enabled": True, "configured": False, "tools": ["write_file"]},
        ])

    observed = HermesRunsApiObserver(
        BASE,
        "api-key",
        allowed_tools={"pantheon_context_manifest"},
        required_tools={"pantheon_context_manifest"},
        client=_client(handler),
    ).observe()
    assert observed["safety_status"] == "qualified"
    assert observed["tool_surface"]["active_tools"] == ["pantheon_context_manifest"]


def test_required_tools_must_be_within_reviewed_allowlist() -> None:
    with pytest.raises(HermesRunsObservationError, match="subset of allowed_tools"):
        HermesRunsApiObserver(
            BASE,
            "api-key",
            allowed_tools={"pantheon_context_manifest"},
            required_tools={"pantheon_context_entity"},
        )


def test_bad_capability_contract_fails_closed() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/v1/capabilities":
            return httpx.Response(200, json={"object": "unexpected"})
        return httpx.Response(200, json=[])

    with pytest.raises(HermesRunsObservationError, match="unexpected contract object"):
        HermesRunsApiObserver(BASE, "api-key", client=_client(handler)).observe()
