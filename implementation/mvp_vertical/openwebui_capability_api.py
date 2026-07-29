"""FastAPI route for the read-only OpenWebUI capability projection."""

from __future__ import annotations

from collections.abc import Callable

from fastapi import APIRouter, Depends

from .openwebui_capabilities import project_openwebui_capabilities


def create_openwebui_capability_router(
    *,
    require_read_key: Callable,
    observation_provider: Callable[[], dict] | None = None,
) -> APIRouter:
    """Build a router without coupling capability detection to cockpit internals."""

    router = APIRouter()
    provider = observation_provider or (lambda: {})

    @router.get("/v1/system/capabilities/openwebui")
    def openwebui_capabilities(
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        observation = provider()
        return project_openwebui_capabilities(
            observation.get("capabilities", {}),
            version=observation.get("version"),
            endpoint=observation.get("endpoint"),
        )

    return router
