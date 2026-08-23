"""FastAPI routes for read-only OpenWebUI compatibility projections."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from .openwebui_capabilities import (
    project_openwebui_capabilities,
    project_openwebui_resource,
)
from .runtime_observation import wrap_runtime_observation


def _observed_at() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def create_openwebui_capability_router(
    *,
    require_read_key: Callable,
    observation_provider: Callable[[], dict] | None = None,
) -> APIRouter:
    """Build routes without coupling OpenWebUI observation to cockpit rendering."""

    router = APIRouter()
    provider = observation_provider or (lambda: {})

    def read_observation() -> dict:
        raw = provider()
        payload = raw if isinstance(raw, dict) else {}
        return wrap_runtime_observation(
            source="openwebui",
            observation_source="openwebui_compatibility_provider",
            observed_at=_observed_at(),
            payload=payload,
            label="OpenWebUI observation",
        )

    @router.get("/capabilities/openwebui")
    def openwebui_capabilities(
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        observation = read_observation()
        return project_openwebui_capabilities(
            observation.get("capabilities", {}),
            version=observation.get("version"),
            endpoint=observation.get("endpoint"),
        )

    @router.get("/resources/openwebui")
    def openwebui_resource(
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        """Return the generic Tool Card / Governed Resource projection."""
        observation = read_observation()
        return project_openwebui_resource(
            observation.get("capabilities", {}),
            version=observation.get("version"),
            endpoint=observation.get("endpoint"),
        )

    return router
