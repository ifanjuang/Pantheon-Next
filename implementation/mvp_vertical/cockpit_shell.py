"""Cards-first cockpit composition over the bounded project APIs.

The shell exposes projections and narrowly governed owner writes. It does not own
object status, approval, execution, evidence, memory promotion or external action.
"""

from __future__ import annotations

import hmac
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Callable, Literal

import psycopg
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import (
    effect_guard,
    effect_preview,
    knowledge,
    knowledge_update,
    resource_profiles,
    site_manifest_preview,
    site_navigation_profile,
    store,
    work_issue_read,
    work_issues,
)
from .cockpit_api import create_app

COCKPIT = Path(__file__).resolve().parent / "cockpit"
_DEFAULT_INITIALIZER = object()


class EffectPreviewBody(BaseModel):
    information: str = Field(min_length=3, max_length=4000)
    explicit_object_refs: list[str] = Field(default_factory=list, max_length=10)
    effect_hint: Literal["CREATE", "UPDATE", "SUPERSEDE", "CONFLICT"] | None = None
    max_proposals: int = Field(default=5, ge=1, le=10)


class KnowledgeUpdatePreviewBody(BaseModel):
    proposed_markdown: str = Field(min_length=1, max_length=500_000)
    expected_version: int = Field(ge=1)
    review_status: Literal[
        "generated_unreviewed", "needs_review", "reviewed", "superseded"
    ] | None = None


class KnowledgeUpdateApplyBody(KnowledgeUpdatePreviewBody):
    base_markdown_digest: str = Field(min_length=8, max_length=100)
    confirmation_token: str = Field(min_length=32, max_length=200)
    confirmation_expires_at: int = Field(ge=1)
    confirmation_phrase: str = Field(min_length=1, max_length=100)
    idempotency_key: str = Field(min_length=8, max_length=200)


class StructureSiteScopeBody(BaseModel):
    url: str = Field(min_length=8, max_length=2048)
    path_prefixes: list[str] = Field(default_factory=list, max_length=8)
    max_depth: int = Field(default=2, ge=0, le=5)


class StructureManifestPreviewBody(BaseModel):
    mode: Literal["structure_only"] = "structure_only"
    sites: list[StructureSiteScopeBody] = Field(min_length=1, max_length=10)


class SiteNavigationProfilePreviewBody(BaseModel):
    task: str = Field(min_length=3, max_length=500)
    selected_urls: list[str] = Field(default_factory=list, max_length=10)


def connect_cockpit():
    """Open a runtime connection without replaying schema DDL per request."""
    return psycopg.connect(store.dsn_from_env())


def initialize_cockpit_schema() -> None:
    """Initialize the bounded store once at service startup, outside request handling."""
    conn = store.connect()
    try:
        conn.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()


def _install_initializer(app: FastAPI, initializer: Callable[[], None]) -> None:
    """Compose one fail-closed initializer with FastAPI's current lifespan API."""
    original_lifespan = app.router.lifespan_context

    @asynccontextmanager
    async def lifespan(application: FastAPI):
        initializer()
        async with original_lifespan(application) as state:
            yield state

    app.router.lifespan_context = lifespan


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def create_cockpit_app(
    *,
    connect_fn: Callable = connect_cockpit,
    initialize_fn: Callable[[], None] | None | object = _DEFAULT_INITIALIZER,
    document_root: str | Path | None = None,
    api_key: str | None = None,
    editor_api_key: str | None = None,
    hermes_api_key: str | None = None,
    update_signing_secret: str | None = None,
    public_url: str | None = None,
) -> FastAPI:
    """Compose the existing bounded API with the cards-first static shell."""
    app = create_app(
        connect_fn=connect_fn,
        document_root=document_root,
        api_key=api_key,
        editor_api_key=editor_api_key,
        hermes_api_key=hermes_api_key,
        public_url=public_url,
    )
    app.state.update_signing_secret = (
        update_signing_secret
        if update_signing_secret is not None
        else os.getenv("MVP_UPDATE_SIGNING_SECRET", "")
    )

    if initialize_fn is _DEFAULT_INITIALIZER:
        initialize_fn = initialize_cockpit_schema if connect_fn is connect_cockpit else None
    if initialize_fn is not None:
        _install_initializer(app, initialize_fn)

    def require_read_key(authorization: str | None = Header(default=None)) -> None:
        supplied = _bearer_token(authorization)
        expected = [key for key in (app.state.api_key, app.state.editor_api_key) if key]
        if not expected:
            raise HTTPException(status_code=503, detail="read API key is not configured")
        if not any(hmac.compare_digest(supplied, key) for key in expected):
            raise HTTPException(status_code=401, detail="invalid read API key")

    def require_editor_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.editor_api_key
        if not expected:
            raise HTTPException(status_code=503, detail="editor API key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid editor API key")

    def require_update_signing_secret() -> str:
        secret = app.state.update_signing_secret
        if not secret:
            raise HTTPException(
                status_code=503,
                detail="Knowledge update signing authority is not configured",
            )
        return secret

    def require_human_actor(
        x_pantheon_human_actor: str | None = Header(
            default=None, alias="X-Pantheon-Human-Actor"
        ),
    ) -> str:
        if not x_pantheon_human_actor or not x_pantheon_human_actor.strip():
            raise HTTPException(
                status_code=422,
                detail="X-Pantheon-Human-Actor is required for a consequential Knowledge write",
            )
        return x_pantheon_human_actor.strip()

    def with_connection(operation):
        conn = app.state.connect_fn()
        try:
            return operation(conn)
        finally:
            conn.close()

    def knowledge_update_write(operation):
        try:
            return with_connection(operation)
        except knowledge.KnowledgeNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except knowledge_update.KnowledgeUpdateExpired as exc:
            raise HTTPException(status_code=410, detail=str(exc)) from exc
        except (knowledge.StaleKnowledgeWrite, knowledge.IdempotencyConflict) as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except (knowledge_update.KnowledgeUpdateError, knowledge.KnowledgeError) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.get("/v1/projects/{parent_project_id}/work-issues")
    def project_work_issues(
        parent_project_id: str,
        include_terminal: bool = True,
        limit: int = 100,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        """List Work Issues whose exact `case_ref` matches the opened project."""
        try:
            projections = with_connection(
                lambda conn: work_issue_read.list_issue_projections(
                    conn,
                    parent_project_id,
                    include_terminal=include_terminal,
                    limit=limit,
                )
            )
        except work_issues.WorkIssueError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {
            "parent_project_id": parent_project_id,
            "scope_match": "exact_case_ref",
            "work_issues": projections,
        }

    @app.get("/v1/projects/{parent_project_id}/resource-profiles")
    def project_resource_profiles(
        parent_project_id: str,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        """Expose observed file composition and Knowledge-linked web addresses."""
        try:
            return with_connection(
                lambda conn: resource_profiles.list_project_resource_profiles(
                    conn, parent_project_id
                )
            )
        except resource_profiles.ResourceProfileError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post(
        "/v1/projects/{parent_project_id}/knowledge/{knowledge_id}/site-manifests/preview"
    )
    def preview_site_manifest(
        parent_project_id: str,
        knowledge_id: str,
        body: StructureManifestPreviewBody,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        """Preview one exact Knowledge-linked structure perimeter without fetching it."""
        try:
            return with_connection(
                lambda conn: site_manifest_preview.preview_structure_manifest(
                    conn,
                    parent_project_id=parent_project_id,
                    knowledge_id=knowledge_id,
                    mode=body.mode,
                    sites=[site.model_dump() for site in body.sites],
                )
            )
        except knowledge.KnowledgeNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except (
            site_manifest_preview.SiteManifestPreviewError,
            knowledge.KnowledgeError,
        ) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post(
        "/v1/projects/{parent_project_id}/knowledge/{knowledge_id}/navigation-profiles/preview"
    )
    def preview_navigation_profiles(
        parent_project_id: str,
        knowledge_id: str,
        body: SiteNavigationProfilePreviewBody,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        """Preview task-specific navigation candidates without querying or installing skills."""
        try:
            return with_connection(
                lambda conn: site_navigation_profile.preview_site_navigation_profiles(
                    conn,
                    parent_project_id=parent_project_id,
                    knowledge_id=knowledge_id,
                    task=body.task,
                    selected_urls=body.selected_urls or None,
                )
            )
        except knowledge.KnowledgeNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except (
            site_navigation_profile.SiteNavigationProfileError,
            knowledge.KnowledgeError,
        ) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post("/v1/projects/{parent_project_id}/effects/preview")
    def preview_project_effects(
        parent_project_id: str,
        body: EffectPreviewBody,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        """Propose deterministic effects without persisting or applying them."""
        try:
            preview = with_connection(
                lambda conn: effect_preview.preview_project_effects(
                    conn,
                    parent_project_id=parent_project_id,
                    information=body.information,
                    explicit_object_refs=body.explicit_object_refs,
                    effect_hint=body.effect_hint,
                    max_proposals=body.max_proposals,
                )
            )
            return effect_guard.enforce_preview(preview)
        except effect_preview.EffectPreviewError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post(
        "/v1/projects/{parent_project_id}/knowledge/{knowledge_id}/updates/preview"
    )
    def preview_knowledge_update(
        parent_project_id: str,
        knowledge_id: str,
        body: KnowledgeUpdatePreviewBody,
        _authorized: None = Depends(require_editor_key),
        signing_secret: str = Depends(require_update_signing_secret),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        """Return a signed diff for one exact Knowledge UPDATE."""
        return knowledge_update_write(
            lambda conn: knowledge_update.preview_knowledge_update(
                conn,
                parent_project_id=parent_project_id,
                knowledge_id=knowledge_id,
                actor=actor,
                signing_secret=signing_secret,
                **body.model_dump(),
            )
        )

    @app.post(
        "/v1/projects/{parent_project_id}/knowledge/{knowledge_id}/updates/apply"
    )
    def apply_knowledge_update(
        parent_project_id: str,
        knowledge_id: str,
        body: KnowledgeUpdateApplyBody,
        _authorized: None = Depends(require_editor_key),
        signing_secret: str = Depends(require_update_signing_secret),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        """Apply only the exact signed and explicitly confirmed Knowledge UPDATE."""
        return knowledge_update_write(
            lambda conn: knowledge_update.apply_knowledge_update(
                conn,
                parent_project_id=parent_project_id,
                knowledge_id=knowledge_id,
                actor=actor,
                signing_secret=signing_secret,
                **body.model_dump(),
            )
        )

    if COCKPIT.is_dir():
        app.mount("/cockpit", StaticFiles(directory=COCKPIT, html=True), name="cockpit")
    return app


app = create_cockpit_app()


def run() -> None:
    """Run the composed internal cockpit API with uvicorn."""
    import uvicorn

    uvicorn.run(
        "mvp_vertical.cockpit_shell:app",
        host=os.getenv("MVP_COCKPIT_HOST", "127.0.0.1"),
        port=int(os.getenv("MVP_COCKPIT_PORT", "8081")),
        reload=False,
    )


if __name__ == "__main__":
    run()
