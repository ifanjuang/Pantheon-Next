"""Internal Cockpit/Hermes gateway for the bounded Paperless adapter.

The browser-facing Cockpit talks to this service, not to Paperless directly, so
the Paperless token remains server-side. Read operations expose source-runtime
projections only. Consequential metadata writes require the Hermes API key and
are routed through the live Pantheon PDP via the existing policy chokepoint.
"""

from __future__ import annotations

import hmac
import os
from typing import Any, Callable

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from .paperless import (
    PaperlessClient,
    PaperlessConfigurationError,
    PaperlessError,
    PaperlessMutationError,
    governed_update_document_metadata,
)
from .policy_gate import HttpPolicyClient, PolicyClient


class MetadataUpdateBody(BaseModel):
    changes: dict[str, Any] = Field(min_length=1)
    decision_payload: dict[str, Any]
    candidate: dict[str, Any] = Field(default_factory=dict)


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def _document_projection(document: dict[str, Any]) -> dict[str, Any]:
    """Expose useful Paperless metadata without claiming business authority."""

    allowed = (
        "id",
        "title",
        "created",
        "created_date",
        "modified",
        "added",
        "archive_serial_number",
        "original_file_name",
        "archived_file_name",
        "correspondent",
        "document_type",
        "storage_path",
        "tags",
        "custom_fields",
        "page_count",
        "mime_type",
    )
    projection = {key: document.get(key) for key in allowed if key in document}
    search_hit = document.get("__search_hit__")
    if isinstance(search_hit, dict):
        projection["search_hit"] = {
            key: search_hit.get(key) for key in ("score", "rank", "highlights") if key in search_hit
        }
    projection["source_runtime"] = "paperless_ngx"
    projection["authority"] = {
        "business_classification": False,
        "knowledge": False,
        "evidence": False,
        "approval": False,
    }
    return projection


def _default_paperless_factory() -> PaperlessClient:
    return PaperlessClient.from_env()


def _default_policy_factory() -> PolicyClient:
    base_url = os.getenv("PANTHEON_POLICY_API_URL", "http://pantheon-policy-api:8000")
    api_key = os.getenv("PANTHEON_POLICY_API_KEY", "")
    if not api_key:
        raise PaperlessConfigurationError("PANTHEON_POLICY_API_KEY is required for Paperless writes")
    return HttpPolicyClient(base_url=base_url, api_key=api_key)


def create_app(
    *,
    paperless_factory: Callable[[], PaperlessClient] = _default_paperless_factory,
    policy_factory: Callable[[], PolicyClient] = _default_policy_factory,
    read_api_key: str | None = None,
    hermes_api_key: str | None = None,
) -> FastAPI:
    app = FastAPI(
        title="Pantheon Paperless Gateway",
        version="0.1.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    app.state.paperless_factory = paperless_factory
    app.state.policy_factory = policy_factory
    app.state.read_api_key = (
        read_api_key if read_api_key is not None else os.getenv("MVP_COCKPIT_API_KEY", "")
    )
    app.state.hermes_api_key = (
        hermes_api_key if hermes_api_key is not None else os.getenv("MVP_HERMES_API_KEY", "")
    )

    def require_read_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.read_api_key
        if not expected:
            raise HTTPException(status_code=503, detail="Paperless gateway read key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid read API key")

    def require_hermes_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.hermes_api_key
        if not expected:
            raise HTTPException(status_code=503, detail="Paperless gateway Hermes key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid Hermes API key")

    def paperless() -> PaperlessClient:
        try:
            return app.state.paperless_factory()
        except PaperlessConfigurationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc

    @app.get("/health")
    def health() -> dict[str, Any]:
        try:
            observed = paperless().probe()
        except (PaperlessError, HTTPException):
            return {
                "status": "degraded",
                "paperless_reachable": False,
                "write_surface": "fail_closed",
            }
        return {
            "status": "ok",
            "paperless_reachable": bool(observed.get("reachable")),
            "write_surface": "governed_only",
        }

    @app.get("/v1/paperless/documents")
    def list_documents(
        query: str | None = None,
        page: int = 1,
        page_size: int = 50,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        if page < 1 or not 1 <= page_size <= 100:
            raise HTTPException(status_code=422, detail="invalid pagination")
        try:
            payload = paperless().list_documents(query=query, page=page, page_size=page_size)
        except PaperlessError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
        results = payload.get("results") or []
        return {
            "count": payload.get("count", len(results)),
            "next": payload.get("next"),
            "previous": payload.get("previous"),
            "documents": [_document_projection(item) for item in results],
            "source_runtime": "paperless_ngx",
        }

    @app.get("/v1/paperless/documents/{document_id}")
    def get_document(
        document_id: int,
        version_id: str | None = None,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        try:
            document = paperless().get_document(document_id, version_id=version_id)
        except PaperlessError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
        return _document_projection(document)

    @app.get("/v1/paperless/documents/{document_id}/capture")
    def inspect_exact_capture(
        document_id: int,
        version_id: str,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        try:
            capture = paperless().capture_document(document_id, version_id=version_id)
        except (PaperlessError, ValueError) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {
            "document_id": capture.document_id,
            "version_id": capture.version_id,
            "original_filename": capture.original_filename,
            "media_type": capture.media_type,
            "byte_size": capture.byte_size,
            "content_hash": capture.content_hash,
            "storage_reference": capture.storage_reference,
            "source_ref": capture.source_ref,
            "authority": {
                "source_capture_candidate": True,
                "evidence": False,
                "knowledge": False,
            },
        }

    @app.get("/v1/paperless/tasks/{task_id}")
    def task_status(
        task_id: str,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        try:
            task = paperless().get_task(task_id)
        except PaperlessError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc
        return {
            "task": task,
            "runtime_success_is_evidence": False,
        }

    @app.post("/v1/paperless/documents/{document_id}/metadata")
    def update_metadata(
        document_id: int,
        body: MetadataUpdateBody,
        _authorized: None = Depends(require_hermes_key),
    ) -> dict[str, Any]:
        try:
            policy = app.state.policy_factory()
            return governed_update_document_metadata(
                policy,
                paperless(),
                document_id=document_id,
                changes=body.changes,
                decision_payload=body.decision_payload,
                candidate=body.candidate,
            )
        except PaperlessMutationError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except PaperlessConfigurationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        except PaperlessError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc

    return app


app = create_app()


def run() -> None:
    import uvicorn

    uvicorn.run(
        "mvp_vertical.paperless_gateway:app",
        host=os.getenv("MVP_PAPERLESS_GATEWAY_HOST", "127.0.0.1"),
        port=int(os.getenv("MVP_PAPERLESS_GATEWAY_PORT", "8082")),
        reload=False,
    )


if __name__ == "__main__":
    run()
