"""Read-only observation of the public Hermes Agent API-server contract.

This is a control-plane probe, not a dispatcher. It never creates, stops or
approves a run and it never executes a Hermes tool. The observer reads only the
stable discovery surfaces documented by Hermes Agent v0.19+:

- GET /v1/capabilities
- GET /v1/toolsets

A reachable API is not automatically safe for a Pantheon-admitted run. Tool
surface qualification is evaluated only against an explicit operator-reviewed
allowlist; without one the safety posture remains ``not_evaluated``.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable


REQUIRED_RUN_FEATURES = (
    "run_submission",
    "run_status",
    "run_events_sse",
    "run_stop",
)


class HermesRunsObservationError(ValueError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _string_set(values: Iterable[str] | None, *, label: str) -> set[str] | None:
    if values is None:
        return None
    output: set[str] = set()
    for raw in values:
        value = str(raw or "").strip()
        if not value:
            raise HermesRunsObservationError(f"{label} entries must be non-empty strings")
        output.add(value)
    return output


def _json_response(response: Any, *, surface: str) -> Any:
    try:
        response.raise_for_status()
    except Exception as exc:
        raise HermesRunsObservationError(f"Hermes {surface} request failed") from exc
    try:
        return response.json()
    except Exception as exc:
        raise HermesRunsObservationError(f"Hermes {surface} response is not valid JSON") from exc


def _active_tools(toolsets: list[dict[str, Any]]) -> tuple[set[str], list[str]]:
    tools: set[str] = set()
    active_names: list[str] = []
    for raw in toolsets:
        if not isinstance(raw, dict):
            raise HermesRunsObservationError("Hermes /v1/toolsets entries must be objects")
        name = str(raw.get("name") or "").strip()
        if not name:
            raise HermesRunsObservationError("Hermes /v1/toolsets entry is missing name")
        if raw.get("enabled") is not True or raw.get("configured") is not True:
            continue
        active_names.append(name)
        concrete = raw.get("tools") or []
        if not isinstance(concrete, list):
            raise HermesRunsObservationError(
                f"Hermes toolset {name!r} exposes a non-list tools field"
            )
        for tool in concrete:
            tool_name = str(tool or "").strip()
            if tool_name:
                tools.add(tool_name)
    return tools, sorted(active_names)


def _assess_tool_surface(
    toolsets: list[dict[str, Any]],
    *,
    allowed_tools: set[str] | None,
    required_tools: set[str] | None,
) -> dict[str, Any]:
    active_tools, active_toolsets = _active_tools(toolsets)
    base = {
        "active_toolsets": active_toolsets,
        "active_tools": sorted(active_tools),
        "allowed_tools": sorted(allowed_tools) if allowed_tools is not None else None,
        "required_tools": sorted(required_tools) if required_tools is not None else None,
    }
    if allowed_tools is None:
        return {
            **base,
            "status": "not_evaluated",
            "unexpected_tools": [],
            "missing_required_tools": [],
            "reason": "no reviewed allowed_tools policy was supplied",
        }

    unexpected = sorted(active_tools - allowed_tools)
    missing = sorted((required_tools or set()) - active_tools)
    status = "qualified" if not unexpected and not missing else "not_qualified"
    return {
        **base,
        "status": status,
        "unexpected_tools": unexpected,
        "missing_required_tools": missing,
        "reason": None if status == "qualified" else "active Hermes tool surface differs from reviewed policy",
    }


class HermesRunsApiObserver:
    """Observe the stable Hermes API contract without causing a runtime effect."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        allowed_tools: Iterable[str] | None = None,
        required_tools: Iterable[str] | None = None,
        timeout: float = 5.0,
        client: Any | None = None,
    ) -> None:
        base_url = base_url.strip().rstrip("/")
        if not base_url:
            raise HermesRunsObservationError("Hermes base_url is required")
        if not api_key:
            raise HermesRunsObservationError("Hermes API key is required")
        self._base_url = base_url
        self._api_key = api_key
        self._allowed_tools = _string_set(allowed_tools, label="allowed_tools")
        self._required_tools = _string_set(required_tools, label="required_tools")
        if self._required_tools and self._allowed_tools is not None:
            outside = self._required_tools - self._allowed_tools
            if outside:
                raise HermesRunsObservationError(
                    "required_tools must be a subset of allowed_tools: " + ", ".join(sorted(outside))
                )
        self._timeout = timeout
        self._client = client

    def observe(self) -> dict[str, Any]:
        client = self._client
        owns_client = client is None
        if owns_client:
            import httpx  # lazy: observer remains optional infrastructure

            client = httpx.Client(timeout=self._timeout)

        headers = {"Authorization": f"Bearer {self._api_key}"}
        try:
            capabilities = _json_response(
                client.get(
                    self._base_url + "/v1/capabilities",
                    headers=headers,
                    timeout=self._timeout,
                ),
                surface="/v1/capabilities",
            )
            toolsets = _json_response(
                client.get(
                    self._base_url + "/v1/toolsets",
                    headers=headers,
                    timeout=self._timeout,
                ),
                surface="/v1/toolsets",
            )
        finally:
            if owns_client:
                client.close()

        if not isinstance(capabilities, dict):
            raise HermesRunsObservationError("Hermes /v1/capabilities must return an object")
        if capabilities.get("object") != "hermes.api_server.capabilities":
            raise HermesRunsObservationError(
                "Hermes /v1/capabilities returned an unexpected contract object"
            )
        if not isinstance(toolsets, list):
            raise HermesRunsObservationError("Hermes /v1/toolsets must return a list")

        features = capabilities.get("features") or {}
        if not isinstance(features, dict):
            raise HermesRunsObservationError("Hermes capabilities.features must be an object")
        missing_run_features = [
            feature for feature in REQUIRED_RUN_FEATURES if features.get(feature) is not True
        ]
        runs_api_status = "compatible" if not missing_run_features else "incomplete"
        tool_surface = _assess_tool_surface(
            toolsets,
            allowed_tools=self._allowed_tools,
            required_tools=self._required_tools,
        )

        return {
            "kind": "hermes_runs_api_observation",
            "observation_source": "hermes_public_api",
            "observed_at": _now(),
            "base_url": self._base_url,
            "platform": capabilities.get("platform"),
            "model": capabilities.get("model"),
            "auth": capabilities.get("auth"),
            "runs_api_status": runs_api_status,
            "required_run_features": list(REQUIRED_RUN_FEATURES),
            "missing_run_features": missing_run_features,
            "features": features,
            "endpoints": capabilities.get("endpoints") or {},
            "tool_surface": tool_surface,
            "runtime_reachable": True,
            "health_status": "api_contract_observed",
            "safety_status": tool_surface["status"],
            "run_submission_performed": False,
            "run_stop_performed": False,
            "approval_effect_performed": False,
            "write_effect": False,
            "activation_changed": False,
            "authority_effect": "none",
            "non_equivalences": [
                "reachable != healthy",
                "healthy != safe",
                "Runs API available != run authorized",
                "toolset configured != toolset approved",
                "tool surface qualified != production activated",
                "observation != Evidence",
            ],
        }
