"""Read-only Cockpit HTTP surface for filesystem workspace Card collections."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Mapping

from fastapi import Depends, FastAPI, HTTPException, Query

from . import workspace_collection_read


def _place_route_before_cockpit_static_mount(app: FastAPI, endpoint: Callable) -> None:
    """Keep one composed `/cockpit/*` API route ahead of the existing static mount.

    `create_cockpit_app()` installs the static `/cockpit` mount before composed
    extension routes are added. Starlette matches in route order, so a later
    `/cockpit/*` API route would otherwise be swallowed by StaticFiles and
    return its 404 before the API dependency or handler can run.

    This helper moves only the route owned by this adapter. It does not reorder
    unrelated routes or change the static shell owner.
    """
    route = next(
        (
            candidate
            for candidate in reversed(app.router.routes)
            if getattr(candidate, "endpoint", None) is endpoint
        ),
        None,
    )
    if route is None:  # pragma: no cover - FastAPI registration invariant
        raise RuntimeError("workspace collection route was not registered")

    app.router.routes.remove(route)
    static_mount_index = next(
        (
            index
            for index, candidate in enumerate(app.router.routes)
            if getattr(candidate, "path", None) == "/cockpit"
            and getattr(candidate, "name", None) == "cockpit"
        ),
        len(app.router.routes),
    )
    app.router.routes.insert(static_mount_index, route)


def install_workspace_collection_read_routes(
    app: FastAPI,
    *,
    workspace_roots: Mapping[str, str | Path] | None,
    require_read_key: Callable,
) -> None:
    """Mount the bounded read surface over an explicit server-side root mapping."""
    roots = workspace_collection_read.prepare_workspace_roots(workspace_roots)
    app.state.workspace_roots = roots

    @app.get("/cockpit/workspace-collections/{workspace_ref}")
    def get_workspace_collection(
        workspace_ref: str,
        path: str = Query(default="", max_length=4096),
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        try:
            return workspace_collection_read.get_workspace_collection(
                roots,
                workspace_ref,
                path,
            )
        except (
            workspace_collection_read.WorkspaceNotFound,
            workspace_collection_read.WorkspacePathNotFound,
        ) as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except workspace_collection_read.WorkspaceCollectionReadError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    _place_route_before_cockpit_static_mount(app, get_workspace_collection)
