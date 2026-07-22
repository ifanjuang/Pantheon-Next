"""Bounded Document/Knowledge API and mobile editor surface."""

from __future__ import annotations

import hashlib
import hmac
import os
import time
from pathlib import Path
from typing import Callable, Literal
from urllib.parse import quote, urlencode

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from . import knowledge, store
from .contract import ContractError, resolve_source_within

PREVIEW_TTL_SECONDS = 300
MOBILE_EDITOR = Path(__file__).resolve().parent / "mobile_editor"


class PublishKnowledgeBody(BaseModel):
    knowledge_id: str
    title: str
    family: Literal["referentiels", "responsabilite", "methodologie", "techniques", "reglementations"]
    markdown: str
    source_chunk_refs: list[str]
    created_by: str
    actor_kind: Literal["human", "hermes", "system"] = "human"
    idempotency_key: str
    expected_version: int = 0
    review_status: Literal["generated_unreviewed", "needs_review", "reviewed", "superseded"] = "generated_unreviewed"


class ReviseKnowledgeBody(BaseModel):
    markdown: str
    expected_version: int = Field(ge=1)
    actor: str
    actor_kind: Literal["human", "hermes", "system"] = "human"
    idempotency_key: str
    review_status: Literal["generated_unreviewed", "needs_review", "reviewed", "superseded"] | None = None


class EditRequestBody(BaseModel):
    request_id: str
    instruction_kind: Literal["rewrite", "expand", "simplify", "verify", "move_to_lot"]
    instruction: str
    base_version: int = Field(ge=1)
    selection_start: int = Field(ge=0)
    selection_end: int = Field(ge=0)
    selected_text: str
    requested_by: str
    idempotency_key: str
    replacement_markdown: str | None = None


class EditProposalBody(BaseModel):
    replacement_markdown: str


class ApplyEditBody(BaseModel):
    actor: str
    actor_kind: Literal["human", "hermes", "system"] = "human"
    idempotency_key: str


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
    editor_api_key: str | None = None,
    hermes_api_key: str | None = None,
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
    app.state.editor_api_key = (
        editor_api_key if editor_api_key is not None else os.getenv("MVP_EDITOR_API_KEY", "")
    )
    app.state.hermes_api_key = (
        hermes_api_key if hermes_api_key is not None else os.getenv("MVP_HERMES_API_KEY", "")
    )
    app.state.public_url = (
        public_url if public_url is not None else os.getenv("MVP_COCKPIT_PUBLIC_URL", "")
    ).rstrip("/")

    def require_api_key(authorization: str | None = Header(default=None)) -> None:
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

    def with_connection(operation):
        conn = app.state.connect_fn()
        try:
            return operation(conn)
        finally:
            conn.close()

    @app.get("/health")
    def health() -> dict:
        editor_enabled = bool(app.state.editor_api_key)
        preview_secret_configured = bool(app.state.api_key or app.state.editor_api_key)
        return {
            "status": "ok",
            "mode": "bounded_read_write" if editor_enabled else "read_only",
            "preview_effect": "none",
            "write_surface": "bounded_document_knowledge_writes" if editor_enabled else "disabled",
            "document_root_configured": app.state.document_root is not None,
            "read_api_key_configured": preview_secret_configured,
            "editor_mode": "bounded_read_write" if editor_enabled else "disabled",
            "signed_knowledge_update_gate": (
                "configured" if bool(getattr(app.state, "update_signing_secret", "")) else "not_configured"
            ),
            "hermes_edit_binding": "polling_ready" if app.state.hermes_api_key else "disabled",
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

    @app.get("/v1/projects/{parent_project_id}/knowledge")
    def project_knowledge(
        parent_project_id: str,
        _authorized: None = Depends(require_api_key),
    ) -> dict:
        cards = with_connection(
            lambda conn: knowledge.list_knowledge_cards(conn, parent_project_id)
        )
        return {"parent_project_id": parent_project_id, "knowledge": cards}

    @app.get("/v1/knowledge/{knowledge_id}")
    def knowledge_card(
        knowledge_id: str,
        _authorized: None = Depends(require_api_key),
    ) -> dict:
        try:
            return with_connection(lambda conn: knowledge.get_knowledge_card(conn, knowledge_id))
        except knowledge.KnowledgeNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get("/v1/knowledge/{knowledge_id}/markdown", response_class=PlainTextResponse)
    def knowledge_markdown(
        knowledge_id: str,
        _authorized: None = Depends(require_api_key),
    ) -> PlainTextResponse:
        try:
            markdown = with_connection(
                lambda conn: knowledge.get_knowledge_markdown(conn, knowledge_id)
            )
        except knowledge.KnowledgeNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return PlainTextResponse(
            markdown,
            media_type="text/markdown; charset=utf-8",
            headers={"X-Pantheon-Knowledge": "generated", "Cache-Control": "private, no-cache"},
        )

    def knowledge_write(operation):
        try:
            return with_connection(operation)
        except knowledge.KnowledgeNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except (knowledge.StaleKnowledgeWrite, knowledge.IdempotencyConflict) as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except knowledge.KnowledgeError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post("/v1/documents/{document_id}/knowledge", status_code=201)
    def publish_knowledge(
        document_id: str,
        body: PublishKnowledgeBody,
        _authorized: None = Depends(require_editor_key),
    ) -> dict:
        return knowledge_write(
            lambda conn: knowledge.publish_knowledge(
                conn, document_id=document_id, **body.model_dump()
            )
        )

    @app.put("/v1/knowledge/{knowledge_id}")
    def revise_knowledge(
        knowledge_id: str,
        body: ReviseKnowledgeBody,
        _authorized: None = Depends(require_editor_key),
    ) -> dict:
        """Retired direct write; use the project-scoped signed UPDATE gate."""
        raise HTTPException(
            status_code=410,
            detail=(
                "direct Knowledge revision is retired; use the project-scoped "
                "signed update preview/apply routes"
            ),
        )

    @app.post("/v1/knowledge/{knowledge_id}/edit-requests", status_code=202)
    def request_intelligent_edit(
        knowledge_id: str,
        body: EditRequestBody,
        _authorized: None = Depends(require_editor_key),
    ) -> dict:
        return knowledge_write(
            lambda conn: knowledge.create_edit_request(
                conn, knowledge_id=knowledge_id, **body.model_dump()
            )
        )

    @app.put("/v1/edit-requests/{request_id}/proposal")
    def complete_intelligent_edit(
        request_id: str,
        body: EditProposalBody,
        _authorized: None = Depends(require_hermes_key),
    ) -> dict:
        return knowledge_write(
            lambda conn: knowledge.complete_edit_request(
                conn, request_id=request_id, replacement_markdown=body.replacement_markdown
            )
        )

    @app.get("/v1/edit-requests")
    def intelligent_edit_queue(
        status: Literal[
            "queued_for_hermes", "proposed", "applied", "conflict", "rejected"
        ] = "queued_for_hermes",
        limit: int = 100,
        _authorized: None = Depends(require_hermes_key),
    ) -> dict:
        return {
            "edit_requests": knowledge_write(
                lambda conn: knowledge.list_edit_requests(conn, status=status, limit=limit)
            )
        }

    @app.post("/v1/edit-requests/{request_id}/apply")
    def apply_intelligent_edit(
        request_id: str,
        body: ApplyEditBody,
        _authorized: None = Depends(require_editor_key),
    ) -> dict:
        return knowledge_write(
            lambda conn: knowledge.apply_edit_request(
                conn, request_id=request_id, **body.model_dump()
            )
        )

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
        secret = app.state.api_key or app.state.editor_api_key
        if not secret:
            raise HTTPException(status_code=503, detail="preview signing secret is not configured")
        expires = int(time.time()) + PREVIEW_TTL_SECONDS
        signature = _signature(secret, document_id, expires)
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
        secret = app.state.api_key or app.state.editor_api_key
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

    if MOBILE_EDITOR.is_dir():
        app.mount("/editor", StaticFiles(directory=MOBILE_EDITOR, html=True), name="mobile-editor")

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
