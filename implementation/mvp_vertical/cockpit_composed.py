"""Compose the Cockpit with bounded implementation extension routes.

This module mounts implementation extensions. It does not execute rites,
authorize tasks, validate Evidence, close ZEUS or approve reviewed artifacts.
"""

from __future__ import annotations

import hmac
import os

from fastapi import Header, HTTPException

from . import (
    agency_change_candidate_review,
    agency_data,
    apu_mapping_reviews,
    apu_write_preparation,
    contradictory_review_store,
    entity_relations,
    execution_results,
    information_projection,
    knowledge_edit_variants,
    source_intake,
    store,
    work_issue_scopes,
    work_issues,
)
from .apu_write_api import install_apu_write_routes
from .cockpit_shell import create_cockpit_app
from .contradictory_review_api import install_contradictory_review_routes
from .document_structure_api import install_document_structure_routes
from .entity_relation_api import install_entity_relation_routes
from .execution_result_api import install_execution_result_routes
from .knowledge_edit_variant_api import install_knowledge_edit_variant_routes
from .work_issue_scope_api import install_work_issue_scope_routes


def initialize_composed_schema() -> None:
    """Initialize bounded persistence once, in dependency order."""
    conn = store.connect()
    try:
        conn.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(agency_data.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(source_intake.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(information_projection.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(work_issue_scopes.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(entity_relations.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(agency_change_candidate_review.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(contradictory_review_store.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(execution_results.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(knowledge_edit_variants.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(apu_mapping_reviews.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(apu_write_preparation.MIGRATION.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def create_composed_cockpit_app(**kwargs):
    """Create the existing Cockpit and mount bounded extensions."""
    initialize_fn = kwargs.pop("initialize_fn", initialize_composed_schema)
    app = create_cockpit_app(initialize_fn=initialize_fn, **kwargs)

    def with_connection(operation):
        conn = app.state.connect_fn()
        try:
            return operation(conn)
        finally:
            conn.close()

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

    def require_hermes_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.hermes_api_key
        if not expected:
            raise HTTPException(status_code=503, detail="Hermes API key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid Hermes API key")

    def require_human_actor(
        x_pantheon_human_actor: str | None = Header(
            default=None,
            alias="X-Pantheon-Human-Actor",
        ),
    ) -> str:
        if not x_pantheon_human_actor or not x_pantheon_human_actor.strip():
            raise HTTPException(
                status_code=422,
                detail="X-Pantheon-Human-Actor is required for a WorkIssue scope mutation",
            )
        return x_pantheon_human_actor.strip()

    install_document_structure_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
    )
    install_contradictory_review_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_hermes_key=require_hermes_key,
    )
    install_execution_result_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_editor_key=require_editor_key,
        require_hermes_key=require_hermes_key,
    )
    install_knowledge_edit_variant_routes(
        app,
        with_connection=with_connection,
        require_editor_key=require_editor_key,
    )
    install_work_issue_scope_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_editor_key=require_editor_key,
        require_human_actor=require_human_actor,
    )
    install_entity_relation_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_editor_key=require_editor_key,
    )
    install_apu_write_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_editor_key=require_editor_key,
    )
    return app


app = create_composed_cockpit_app()


def run() -> None:
    """Run the composed internal Cockpit API with uvicorn."""
    import uvicorn

    uvicorn.run(
        "mvp_vertical.cockpit_composed:app",
        host=os.getenv("MVP_COCKPIT_HOST", "127.0.0.1"),
        port=int(os.getenv("MVP_COCKPIT_PORT", "8081")),
        reload=False,
    )


if __name__ == "__main__":
    run()
