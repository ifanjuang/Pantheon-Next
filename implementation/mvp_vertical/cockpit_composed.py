"""Compose the Cockpit with append-only contradictory review candidate routes.

This module mounts an implementation extension. It does not execute rites,
authorize tasks, validate Evidence, close ZEUS or approve reviewed artifacts.
"""

from __future__ import annotations

import hmac
import os

from fastapi import Header, HTTPException

from . import agency_data, contradictory_review_store, store, work_issues
from .cockpit_shell import create_cockpit_app
from .contradictory_review_api import install_contradictory_review_routes


def initialize_composed_schema() -> None:
    """Initialize bounded persistence once, in dependency order."""
    conn = store.connect()
    try:
        conn.execute(work_issues.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(agency_data.MIGRATION.read_text(encoding="utf-8"))
        conn.execute(contradictory_review_store.MIGRATION.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def create_composed_cockpit_app(**kwargs):
    """Create the existing Cockpit and mount the review candidate extension."""
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

    def require_hermes_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.hermes_api_key
        if not expected:
            raise HTTPException(status_code=503, detail="Hermes API key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid Hermes API key")

    install_contradictory_review_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_hermes_key=require_hermes_key,
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
