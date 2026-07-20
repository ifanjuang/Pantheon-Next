"""Read-only Document Card API for the OpenWebUI cockpit candidate."""

from __future__ import annotations

import hashlib
import hmac
import os
import time
from pathlib import Path
from typing import Callable
from urllib.parse import quote, urlencode

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, PlainTextResponse

from . import store
from .contract import ContractError, resolve_source_within

PREVIEW_TTL_SECONDS = 300


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def _signature(secret: str, document_id: str, expires: int) -> str:
    payload = f"{document_id}:{expires}".encode("utf-8")
    return hmac.new(secret.encode("utf-8"), payload, hashlib.sha256).hexdigest()


def create_app(
    *,
    connect_fn: Callable = store.connect,
    document_root: str | Path | None = None,
    api_key: str | None = None,
    public_url: str | None = None,
) -> FastAPI:
    """Create the API with injectable effects for tests and deployment."""
    app = FastAPI(
        title="Pantheon Document Card API",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    app.state.connect_fn = connect_fn
    root_value = document_root if document_root is not None else os.getenv("MVP_DOCUMENT_ROOT")
    app.state.document_root = Path(root_value).resolve() if root_value else None
    app.state.api_key = api_key if api_key is not None else os.getenv("MVP_COCKPIT_API_KEY", "")
    app.state.public_url = (
        public_url if public_url is not None else os.getenv("MVP_COCKPIT_PUBLIC_URL", "")
    ).rstrip("/")

    def require_api_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.api_key
        if not expected:
            raise HTTPException(status_code=503, detail="cockpit API key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid cockpit API key")

    def with_connection(operation):
        conn = app.state.connect_fn()
        try:
            return operation(conn)
        finally:
            conn.close()

    @app.get("/health")
    def health() -> dict:
        return {
            "status": "ok",
            "mode": "read_only",
            "document_root_configured": app.state.document_root is not None,
            "api_key_configured": bool(app.state.api_key),
        }

    @app.get("/v1/projects/{parent_project_id}/documents")
    def project_documents(
        parent_project_id: str,
        _authorized: None = Depends(require_api_key),
    ) -> dict:
        cards = with_connection(
            lambda conn: store.list_document_cards(conn, parent_project_id)
        )
        return {"parent_project_id": parent_project_id, "documents": cards}

    @app.get("/v1/documents/{document_id}")
    def document_card(
        document_id: str,
        _authorized: None = Depends(require_api_key),
    ) -> dict:
        try:
            return with_connection(lambda conn: store.get_document_card_by_id(conn, document_id))
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get("/v1/documents/{document_id}/markdown", response_class=PlainTextResponse)
    def document_markdown(
        document_id: str,
        _authorized: None = Depends(require_api_key),
    ) -> PlainTextResponse:
        try:
            markdown = with_connection(lambda conn: store.get_document_markdown(conn, document_id))
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return PlainTextResponse(
            markdown,
            media_type="text/markdown; charset=utf-8",
            headers={"X-Pantheon-Derived": "true", "Cache-Control": "no-store"},
        )

    @app.get("/v1/documents/{document_id}/preview-link")
    def preview_link(
        document_id: str,
        request: Request,
        _authorized: None = Depends(require_api_key),
    ) -> dict:
        if app.state.document_root is None:
            raise HTTPException(status_code=503, detail="document root is not configured")
        try:
            with_connection(lambda conn: store.get_document_source(conn, document_id))
        except KeyError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        expires = int(time.time()) + PREVIEW_TTL_SECONDS
        signature = _signature(app.state.api_key, document_id, expires)
        base_url = app.state.public_url or str(request.base_url).rstrip("/")
        query = urlencode({"expires": expires, "signature": signature})
        url = f"{base_url}/v1/previews/{quote(document_id, safe='')}/original?{query}"
        return {
            "url": url,
            "expires_at": expires,
            "ttl_seconds": PREVIEW_TTL_SECONDS,
            "disposition": "inline",
        }

    @app.get("/v1/previews/{document_id}/original")
    def original_preview(document_id: str, expires: int, signature: str) -> FileResponse:
        secret = app.state.api_key
        now = int(time.time())
        if not secret or expires < now or expires > now + PREVIEW_TTL_SECONDS + 5:
            raise HTTPException(status_code=401, detail="expired preview link")
        expected = _signature(secret, document_id, expires)
        if not hmac.compare_digest(signature, expected):
            raise HTTPException(status_code=401, detail="invalid preview signature")
        if app.state.document_root is None:
            raise HTTPException(status_code=503, detail="document root is not configured")
        try:
            dossier, source_ref = with_connection(
                lambda conn: store.get_document_source(conn, document_id)
            )
            path = resolve_source_within(app.state.document_root, source_ref, dossier)
        except (KeyError, ContractError) as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        if not path.is_file():
            raise HTTPException(status_code=404, detail="original document is unavailable")
        media_type = with_connection(
            lambda conn: store.get_document_card_by_id(conn, document_id)["media_type"]
        )
        return FileResponse(
            path,
            media_type=media_type,
            filename=path.name,
            content_disposition_type="inline",
            headers={"Cache-Control": "private, no-store, max-age=0"},
        )

    return app


app = create_app()


def run() -> None:
    """Run the internal cockpit API with uvicorn."""
    import uvicorn

    uvicorn.run(
        "mvp_vertical.cockpit_api:app",
        host=os.getenv("MVP_COCKPIT_HOST", "127.0.0.1"),
        port=int(os.getenv("MVP_COCKPIT_PORT", "8081")),
        reload=False,
    )


if __name__ == "__main__":
    run()
