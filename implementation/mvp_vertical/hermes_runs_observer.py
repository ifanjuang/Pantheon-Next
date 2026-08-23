"""Read-only observation of the public Hermes Agent API-server contract.

This is a control-plane probe, not a dispatcher. It never creates, stops or
approves a run and it never executes a Hermes tool. The observer reads only the
stable discovery surfaces exposed by the reviewed Hermes Agent runtime:

- GET /v1/capabilities
- GET /v1/toolsets

Hermes 0.20.0 wraps the toolset list in an OpenAI-style list envelope:
``{"object": "list", "platform": "api_server", "data": [...]}``.
A historical bare list remains readable only as an explicitly labelled
compatibility surface; malformed or differently scoped envelopes fail closed.

The same locked observer component may capture one profile-local memory status
receipt by invoking the official ``hermes -p <profile> memory status`` command
without a shell. It never mutates configuration, reads arbitrary profile files,
enables or disables tools, or retains raw command output.

A reachable API is not automatically safe for a Pantheon-admitted run. The
profile route, tool surface and complete memory posture all fail closed unless
explicitly observed and qualified.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from datetime import datetime, timezone
from typing import Any, Callable, Iterable
from urllib.parse import unquote, urlsplit


REQUIRED_RUN_FEATURES = (
    "run_submission",
    "run_status",
    "run_events_sse",
    "run_stop",
)
MAX_MEMORY_STATUS_CHARS = 64_000
MAX_MEMORY_OBSERVATION_AGE_SECONDS = 300.0
MAX_FUTURE_CLOCK_SKEW_SECONDS = 30.0
_PROFILE_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
_DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
_ANSI_PATTERN = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


class HermesRunsObservationError(ValueError):
    pass


class HermesMemoryObservationError(HermesRunsObservationError):
    pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_profile_name(value: str) -> str:
    profile = str(value or "").strip()
    if not profile or not _PROFILE_PATTERN.fullmatch(profile):
        raise HermesMemoryObservationError(
            "Hermes profile must contain only letters, numbers, hyphens or underscores"
        )
    return profile


def _memory_toggle(text: str, label: str) -> str:
    match = re.search(
        rf"^\s*{re.escape(label)}\s*:\s*(enabled|disabled)\b",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not match:
        return "unknown"
    return "on" if match.group(1).lower() == "enabled" else "off"


def _memory_provider(text: str) -> str:
    match = re.search(
        r"^\s*Provider\s*:\s*(.*?)\s*$",
        text,
        flags=re.IGNORECASE | re.MULTILINE,
    )
    if not match:
        return "unknown"
    value = match.group(1).strip().lower()
    if not value:
        return "unknown"
    if value.startswith("(none") or "built-in only" in value or "builtin only" in value:
        return "off"
    return "selected"


def _observation_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value.strip())
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed.astimezone(timezone.utc)


def parse_memory_status(
    output: str,
    *,
    profile: str,
    command: list[str] | None = None,
    exit_code: int = 0,
    captured_at: str | None = None,
) -> dict[str, Any]:
    """Parse official human-readable memory status into a bounded receipt."""

    profile = normalize_profile_name(profile)
    if not isinstance(output, str):
        raise HermesMemoryObservationError("Hermes memory status output must be text")
    if len(output) > MAX_MEMORY_STATUS_CHARS:
        raise HermesMemoryObservationError(
            f"Hermes memory status output exceeds {MAX_MEMORY_STATUS_CHARS} characters"
        )

    normalized = _ANSI_PATTERN.sub("", output).replace("\r\n", "\n").replace("\r", "\n")
    axes = {
        "external_provider": _memory_provider(normalized),
        "built_in_memory_injection": _memory_toggle(normalized, "Memory injection"),
        "built_in_user_profile_injection": _memory_toggle(normalized, "User profile"),
        "memory_tool": _memory_toggle(normalized, "Memory tool"),
    }
    missing = sorted(name for name, value in axes.items() if value == "unknown")
    active = sorted(name for name, value in axes.items() if value in {"on", "selected"})

    if exit_code != 0:
        status = "not_qualified"
        reason = "Hermes memory status command did not exit successfully"
    elif missing:
        status = "not_qualified"
        reason = "Hermes memory status output is incomplete"
    elif active:
        status = "not_qualified"
        reason = "Hermes governed memory posture contains active memory inputs"
    else:
        status = "qualified"
        reason = None

    return {
        "kind": "hermes_profile_memory_observation",
        "observation_source": "hermes_memory_status_cli",
        "profile": profile,
        "captured_at": captured_at or _now(),
        "command": list(command or ["hermes", "-p", profile, "memory", "status"]),
        "exit_code": int(exit_code),
        "stdout_digest": "sha256:" + hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "raw_output_retained": False,
        **axes,
        "missing_axes": missing,
        "active_axes": active,
        "status": status,
        "reason": reason,
        "write_effect": False,
        "activation_changed": False,
        "authority_effect": "none",
        "technical_receipt_is_evidence": False,
        "non_equivalences": [
            "hermes memory off != built-in memory injection off",
            "memory tool absent != memory injection disabled",
            "stored memory != admitted memory",
            "memory observation != Evidence",
        ],
    }


def capture_memory_status(
    *,
    profile: str,
    hermes_command: str = "hermes",
    timeout: float = 10.0,
    runner: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    """Capture one profile-local status command without a shell or mutation."""

    profile = normalize_profile_name(profile)
    command_name = str(hermes_command or "").strip()
    if not command_name:
        raise HermesMemoryObservationError("Hermes command is required")
    if timeout <= 0:
        raise HermesMemoryObservationError("Hermes memory status timeout must be positive")

    command = [command_name, "-p", profile, "memory", "status"]
    run = runner or subprocess.run
    try:
        completed = run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise HermesMemoryObservationError("Hermes memory status capture failed") from exc

    stdout = completed.stdout if isinstance(completed.stdout, str) else ""
    return parse_memory_status(
        stdout,
        profile=profile,
        command=command,
        exit_code=int(completed.returncode),
    )


def qualify_memory_observation(
    receipt: dict[str, Any] | None,
    *,
    expected_profile: str | None,
    observed_at: datetime | None = None,
    max_age_seconds: float = MAX_MEMORY_OBSERVATION_AGE_SECONDS,
) -> dict[str, Any]:
    """Fail closed when a supplied receipt is incomplete, stale or active."""

    if max_age_seconds <= 0:
        raise HermesMemoryObservationError("Hermes memory observation max age must be positive")
    reference_time = observed_at or datetime.now(timezone.utc)
    if reference_time.tzinfo is None:
        raise HermesMemoryObservationError("Hermes memory observation reference time must be timezone-aware")
    reference_time = reference_time.astimezone(timezone.utc)

    if receipt is None:
        return {
            "status": "not_evaluated",
            "expected_profile": expected_profile,
            "observed_profile": None,
            "external_provider": "unknown",
            "built_in_memory_injection": "unknown",
            "built_in_user_profile_injection": "unknown",
            "memory_tool": "unknown",
            "session_memory_key": "absent",
            "reason": "no profile memory observation was supplied",
            "missing_axes": [
                "external_provider",
                "built_in_memory_injection",
                "built_in_user_profile_injection",
                "memory_tool",
            ],
            "active_axes": [],
            "observation_source": None,
            "captured_at": None,
            "age_seconds": None,
            "stdout_digest": None,
            "raw_output_retained": False,
        }
    if not isinstance(receipt, dict):
        raise HermesMemoryObservationError("Hermes memory observation must be an object")
    if receipt.get("kind") != "hermes_profile_memory_observation":
        raise HermesMemoryObservationError("Hermes memory observation has an unexpected kind")

    observed_profile = normalize_profile_name(str(receipt.get("profile") or ""))
    expected = normalize_profile_name(expected_profile) if expected_profile else None
    valid_values = {
        "external_provider": {"off", "selected", "unknown"},
        "built_in_memory_injection": {"off", "on", "unknown"},
        "built_in_user_profile_injection": {"off", "on", "unknown"},
        "memory_tool": {"off", "on", "unknown"},
    }
    axes: dict[str, str] = {}
    for name, allowed in valid_values.items():
        value = str(receipt.get(name) or "unknown")
        if value not in allowed:
            raise HermesMemoryObservationError(f"Hermes memory observation has invalid {name}")
        axes[name] = value

    missing = sorted(name for name, value in axes.items() if value == "unknown")
    active = sorted(name for name, value in axes.items() if value in {"on", "selected"})
    reasons: list[str] = []
    if expected is None:
        reasons.append("no expected profile was supplied")
    elif observed_profile != expected:
        reasons.append("memory observation profile differs from expected profile")

    if receipt.get("observation_source") != "hermes_memory_status_cli":
        reasons.append("memory observation has an unexpected source")
    captured_at = _observation_time(receipt.get("captured_at"))
    age_seconds: float | None = None
    if captured_at is None:
        reasons.append("memory observation has no valid timezone-aware capture time")
    else:
        age_seconds = (reference_time - captured_at).total_seconds()
        if age_seconds > max_age_seconds:
            reasons.append("memory observation is stale")
        elif age_seconds < -MAX_FUTURE_CLOCK_SKEW_SECONDS:
            reasons.append("memory observation capture time is in the future")

    command = receipt.get("command")
    expected_tail = ["-p", observed_profile, "memory", "status"]
    if not isinstance(command, list) or len(command) < 5 or command[-4:] != expected_tail:
        reasons.append("memory observation command does not target the observed profile")
    if receipt.get("exit_code") != 0:
        reasons.append("memory status command did not exit successfully")
    if receipt.get("status") != "qualified":
        reasons.append("memory observation is not qualified")
    if receipt.get("raw_output_retained") is not False:
        reasons.append("memory observation retained raw command output")
    if receipt.get("write_effect") is not False or receipt.get("activation_changed") is not False:
        reasons.append("memory observation reports a mutation effect")
    if receipt.get("authority_effect") != "none":
        reasons.append("memory observation reports an authority effect")
    if receipt.get("technical_receipt_is_evidence") is not False:
        reasons.append("memory observation is incorrectly classified as Evidence")

    digest = str(receipt.get("stdout_digest") or "")
    if not _DIGEST_PATTERN.fullmatch(digest):
        reasons.append("memory observation has no valid output digest")
    if missing:
        reasons.append("memory observation has missing axes")
    if active:
        reasons.append("memory observation has active axes")

    status = "qualified" if not reasons else "not_qualified"
    return {
        "status": status,
        "expected_profile": expected,
        "observed_profile": observed_profile,
        **axes,
        "session_memory_key": "absent",
        "reason": None if status == "qualified" else "; ".join(reasons),
        "missing_axes": missing,
        "active_axes": active,
        "observation_source": receipt.get("observation_source"),
        "captured_at": captured_at.isoformat() if captured_at is not None else None,
        "age_seconds": round(age_seconds, 3) if age_seconds is not None else None,
        "stdout_digest": digest or None,
        "raw_output_retained": receipt.get("raw_output_retained") is True,
    }


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


def _normalize_toolsets_contract(payload: Any) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Normalize the reviewed 0.20 envelope or an explicit legacy bare list."""

    if isinstance(payload, list):
        return payload, {
            "object": "legacy_bare_list",
            "platform": None,
            "data_field": False,
            "compatibility_surface": True,
        }
    if not isinstance(payload, dict):
        raise HermesRunsObservationError(
            "Hermes /v1/toolsets must return an object list envelope"
        )
    if payload.get("object") != "list":
        raise HermesRunsObservationError(
            "Hermes /v1/toolsets returned an unexpected contract object"
        )
    if payload.get("platform") != "api_server":
        raise HermesRunsObservationError(
            "Hermes /v1/toolsets returned an unexpected platform scope"
        )
    data = payload.get("data")
    if not isinstance(data, list):
        raise HermesRunsObservationError(
            "Hermes /v1/toolsets list envelope has a non-list data field"
        )
    return data, {
        "object": "list",
        "platform": "api_server",
        "data_field": True,
        "compatibility_surface": False,
    }


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


def _profile_from_base_url(base_url: str) -> str | None:
    segments = [unquote(value) for value in urlsplit(base_url).path.split("/") if value]
    if len(segments) >= 2 and segments[-2] == "p":
        return normalize_profile_name(segments[-1])
    return None


def _assess_profile_surface(base_url: str, expected_profile: str | None) -> dict[str, Any]:
    observed_profile = _profile_from_base_url(base_url)
    if expected_profile is None:
        return {
            "status": "not_evaluated",
            "expected_profile": None,
            "observed_profile": observed_profile,
            "route_observed": observed_profile is not None,
            "reason": "no expected Hermes profile was supplied",
        }
    expected = normalize_profile_name(expected_profile)
    status = "qualified" if observed_profile == expected else "not_qualified"
    return {
        "status": status,
        "expected_profile": expected,
        "observed_profile": observed_profile,
        "route_observed": observed_profile is not None,
        "reason": None if status == "qualified" else "Hermes base_url does not target the expected /p/<profile> route",
    }


def _combined_safety_status(*statuses: str) -> str:
    if "not_qualified" in statuses:
        return "not_qualified"
    if statuses and all(value == "qualified" for value in statuses):
        return "qualified"
    return "not_evaluated"


class HermesRunsApiObserver:
    """Observe the stable Hermes API contract without causing a runtime effect."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        expected_profile: str | None = None,
        memory_observation: dict[str, Any] | None = None,
        memory_observation_max_age_seconds: float = MAX_MEMORY_OBSERVATION_AGE_SECONDS,
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
        if memory_observation_max_age_seconds <= 0:
            raise HermesRunsObservationError("Hermes memory observation max age must be positive")
        self._base_url = base_url
        self._api_key = api_key
        self._expected_profile = expected_profile
        self._memory_observation = memory_observation
        self._memory_observation_max_age_seconds = memory_observation_max_age_seconds
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
            toolsets_payload = _json_response(
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
        toolsets, toolsets_contract = _normalize_toolsets_contract(toolsets_payload)

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
        profile_surface = _assess_profile_surface(self._base_url, self._expected_profile)
        memory_posture = qualify_memory_observation(
            self._memory_observation,
            expected_profile=self._expected_profile,
            max_age_seconds=self._memory_observation_max_age_seconds,
        )

        safety_status = _combined_safety_status(
            tool_surface["status"],
            profile_surface["status"],
            memory_posture["status"],
        )
        safety_reasons = [
            value["reason"]
            for value in (tool_surface, profile_surface, memory_posture)
            if value.get("reason")
        ]

        return {
            "kind": "hermes_runs_api_observation",
            "observation_source": "hermes_public_api_and_profile_memory_receipt",
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
            "toolsets_contract": toolsets_contract,
            "profile_surface": profile_surface,
            "tool_surface": tool_surface,
            "memory_posture": memory_posture,
            "session_memory_header_sent": False,
            "runtime_reachable": True,
            "health_status": "api_contract_observed",
            "safety_status": safety_status,
            "safety_reasons": safety_reasons,
            "run_submission_performed": False,
            "run_stop_performed": False,
            "approval_effect_performed": False,
            "write_effect": False,
            "activation_changed": False,
            "authority_effect": "none",
            "non_equivalences": [
                "reachable != healthy",
                "healthy != safe",
                "profile route answered != governed profile qualified",
                "hermes memory off != built-in memory injection off",
                "memory tool absent != memory injection disabled",
                "fresh memory observation != task authorized",
                "Runs API available != run authorized",
                "toolset configured != toolset approved",
                "tool surface qualified != production activated",
                "memory posture qualified != task authorized",
                "observation != Evidence",
            ],
        }