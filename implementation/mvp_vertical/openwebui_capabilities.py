"""Read-only OpenWebUI capability projection.

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
    if value in (None, "", "unknown"):
        return "unknown"
    raise OpenWebUICapabilityError("capability observation must be true, false or unknown")


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
        capability["activated"] = False
        capability["task_authorized"] = False

    payload["detected_version"] = version or os.getenv("OPENWEBUI_VERSION") or "unknown"
    payload["endpoint"] = endpoint or os.getenv("OPENWEBUI_URL") or "unknown"
    payload["status"] = "observed_not_authoritative"
    return payload
