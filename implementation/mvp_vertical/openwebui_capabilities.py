"""Read-only OpenWebUI capability and governed-resource projections.

This module reports adapter observations for cockpit display. It does not install,
activate, approve, authorize or execute OpenWebUI capabilities.
"""

from __future__ import annotations

import json
import os
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping

REGISTRY_PATH = Path(__file__).resolve().parent / "cockpit" / "openwebui_capabilities.json"


class OpenWebUICapabilityError(ValueError):
    """Raised when an observation cannot be normalized safely."""


def load_registry(path: str | Path | None = None) -> dict[str, Any]:
    registry_path = Path(path) if path is not None else REGISTRY_PATH
    with registry_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if payload.get("authority") != "projection_only":
        raise OpenWebUICapabilityError("OpenWebUI registry must remain projection_only")
    return payload


def _tri_state(value: object) -> bool | str:
    if value is True or value is False:
        return value
    if value in (None, "", "unknown", "not_observed"):
        return "not_observed"
    raise OpenWebUICapabilityError(
        "capability observation must be true, false or not_observed"
    )


def project_openwebui_capabilities(
    observations: Mapping[str, Mapping[str, object]] | None = None,
    *,
    version: str | None = None,
    endpoint: str | None = None,
) -> dict[str, Any]:
    """Merge bounded runtime observations into the static capability registry.

    Observations may update availability, installed and healthy only. Activation
    and task authorization remain false because technical detection cannot grant
    either status.
    """

    payload = deepcopy(load_registry())
    observed = observations or {}
    known_ids = {item["id"] for item in payload["capabilities"]}
    unknown_ids = sorted(set(observed) - known_ids)
    if unknown_ids:
        raise OpenWebUICapabilityError(
            f"unknown OpenWebUI capability observations: {', '.join(unknown_ids)}"
        )

    for capability in payload["capabilities"]:
        values = observed.get(capability["id"], {})
        for field in ("availability", "installed", "healthy"):
            if field in values:
                capability[field] = _tri_state(values[field])
            elif capability.get(field) == "unknown":
                capability[field] = "not_observed"
        capability["activated"] = False
        capability["task_authorized"] = False

    payload["detected_version"] = version or os.getenv("OPENWEBUI_VERSION") or "not_observed"
    payload["endpoint"] = endpoint or os.getenv("OPENWEBUI_URL") or "not_observed"
    payload["status"] = "observed_not_authoritative"
    return payload


def project_openwebui_resource(
    observations: Mapping[str, Mapping[str, object]] | None = None,
    *,
    version: str | None = None,
    endpoint: str | None = None,
) -> dict[str, Any]:
    """Project OpenWebUI through the generic Governed Resource / Tool Card shape.

    The resource is an ``infrastructure_module``. Its native capabilities remain
    separate binding projections. Compatibility and reachability observations do
    not establish adoption, safety, activation or task authorization.
    """

    projection = project_openwebui_capabilities(
        observations,
        version=version,
        endpoint=endpoint,
    )
    capabilities = projection["capabilities"]

    installed_values = {item["installed"] for item in capabilities}
    healthy_values = {item["healthy"] for item in capabilities}

    installation_state = (
        "installed_observed"
        if True in installed_values
        else "not_installed_observed"
        if installed_values == {False}
        else "not_observed"
    )
    health_state = (
        "healthy_observed"
        if True in healthy_values
        else "unhealthy_observed"
        if False in healthy_values
        else "not_observed"
    )

    return {
        "tool_id": "openwebui",
        "name": "OpenWebUI",
        "category": "Conversational exposure surface",
        "resource_type": "infrastructure_module",
        "provenance_mode": "openwebui_compatibility_projection",
        "runtime_owner": "openwebui",
        "installation_state": installation_state,
        "native_state": "observed" if projection["detected_version"] != "not_observed" else "not_observed",
        "health_state": health_state,
        "governance_state": "candidate",
        "update_state": "update_unknown",
        "activation_state": "not_activated",
        "task_authorization_state": "not_authorized",
        "detected_version": projection["detected_version"],
        "endpoint": projection["endpoint"],
        "capability_bindings": [
            {
                "capability_id": item["id"],
                "function": item["function"],
                "binding": item["binding"],
                "availability": item["availability"],
                "installed": item["installed"],
                "healthy": item["healthy"],
                "activated": False,
                "task_authorized": False,
            }
            for item in capabilities
        ],
        "authority": "projection_only",
        "forbidden_inferences": projection["invariants"],
    }
