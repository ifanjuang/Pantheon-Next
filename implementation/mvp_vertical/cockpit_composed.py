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
    execution_results,
    store,
    work_issues,
)
from .apu_write_api import install_apu_write_routes
from .cockpit_shell import create_cockpit_app
from .contradictory_review_api import install_contradictory_review_routes
from .document_structure_api import install_document_structure_routes
from .execution_result_api import install_execution_result_routes


def initialize_composed_schema() -> None:
    """Initialize bounded persistence once, in dependency order."""
    conn = store.connect()
    try:
        conn.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(agency_data.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(agency_change_candidate_review.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(contradictory_review_store.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(execution_results.MIGRATION.read_text(encoding="utf-8"))
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

    install_document_structure_routes(app, with_connection=with_connection, require_read_key=require_read_key)
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
