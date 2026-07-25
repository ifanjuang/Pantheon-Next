"""Internal Cockpit/Hermes gateway for the bounded Paperless adapter.

The browser-facing Cockpit and Hermes skill talk to this service, not to
Paperless directly, so the Paperless token remains server-side. Read operations
expose source-runtime projections only. Consequential effects require the Hermes
API key and route through the Pantheon policy chokepoint.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Callable

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from . import store
from .contract import ContractError, TaskContract, assert_source_in_scope, load_contract
from .documents import DoclingServeClient, DocumentConversionError
from .paperless import (
    PaperlessClient,
    PaperlessConfigurationError,
    PaperlessError,
    PaperlessMutationError,
    PaperlessSourceCapture,
)
from .paperless_ingestion import PaperlessBindingError, intake_paperless_capture
from .policy_gate import HttpPolicyClient, PolicyClient, governed_effect


class MetadataUpdateBody(BaseModel):
    changes: dict[str, Any] = Field(min_length=1)
    paperless_version_id: str = Field(min_length=1)
    task_contract_yaml: str = Field(min_length=1)
    decision_payload: dict[str, Any]
    classification_candidate: dict[str, Any] = Field(default_factory=dict)


class PaperlessIntakeBody(BaseModel):
    paperless_document_id: int = Field(gt=0)
    paperless_version_id: str = Field(min_length=1)
    task_contract_yaml: str = Field(min_length=1)
    decision_payload: dict[str, Any]
    ingestion_id: str | None = None


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def _document_projection(document: dict[str, Any]) -> dict[str, Any]:
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
            key: search_hit.get(key)
            for key in ("score", "rank", "highlights")
            if key in search_hit
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
        raise PaperlessConfigurationError(
            "PANTHEON_POLICY_API_KEY is required for Paperless writes"
        )
    return HttpPolicyClient(base_url=base_url, api_key=api_key)


def _load_task_contract_yaml(text: str) -> TaskContract:
    path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".yaml", encoding="utf-8", delete=False
        ) as handle:
            handle.write(text)
            path = Path(handle.name)
        return load_contract(path)
    finally:
        if path is not None:
            path.unlink(missing_ok=True)


def _assert_capture_still_current(
    client: PaperlessClient,
    capture: PaperlessSourceCapture,
) -> None:
    """Fail closed if the source bytes changed before a root-metadata PATCH.

    Paperless file versions carry version-specific bytes while non-content
    metadata belongs to the root document. A decision derived from an exact
    historical capture must therefore not be replayed after the live document
    advances to different bytes.

    First re-read the exact selected version to detect any replacement or
    inconsistency. For the real Paperless client, also download the document
    without a ``version`` query; Paperless defines that as the latest version.
    Test doubles still exercise the exact-version re-read without needing the
    private HTTP transport.
    """

    recaptured = client.capture_document(
        capture.document_id,
        version_id=capture.version_id,
    )
    if recaptured.content_hash != capture.content_hash:
        raise PaperlessMutationError(
            "exact Paperless source changed after decision capture; metadata mutation refused"
        )

    if isinstance(client, PaperlessClient):
        response = client._request(  # internal adapter boundary; token remains server-side
            "GET",
            f"/api/documents/{capture.document_id}/download/",
            headers={"Accept": "*/*"},
        )
        latest_hash = "sha256:" + hashlib.sha256(bytes(response.content)).hexdigest()
        if latest_hash != capture.content_hash:
            raise PaperlessMutationError(
                "Paperless live document has a newer/different source version; "
                "metadata mutation requires a new capture and human decision"
            )


def _required_project_scope(contract: TaskContract) -> dict[str, str]:
    raw_scope = contract.raw.get("scope") or {}
    scope_type = str(raw_scope.get("scope_type") or "project")
    scope_id = str(
        raw_scope.get("scope_id")
        or raw_scope.get("parent_project_id")
        or raw_scope.get("project_id")
        or contract.dossier
    )
    if not scope_id.strip():
        raise ContractError(f"contract {contract.contract_id}: project scope id is empty")
    return {"scope_type": scope_type, "scope_id": scope_id}


def _required_ceiling(contract: TaskContract) -> str:
    ceiling = str(contract.raw.get("approval_ceiling") or "").strip()
    if not ceiling:
        raise ContractError(
            f"contract {contract.contract_id}: approval_ceiling is required for governed effect"
        )
    return ceiling


def _intake_object_identity(contract: TaskContract, capture: PaperlessSourceCapture) -> str:
    return f"paperless-intake:{contract.contract_id}:{capture.document_id}:{capture.version_id}"


def _intake_effect_digest(contract: TaskContract, capture: PaperlessSourceCapture) -> str:
    envelope = {
        "operation": "project_document_intake",
        "contract_digest": store.contract_digest(contract),
        "source_ref": capture.source_ref,
        "source_content_hash": capture.content_hash,
        "storage_reference": capture.storage_reference,
    }
    canonical = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _intake_policy_candidate(
    contract: TaskContract,
    capture: PaperlessSourceCapture,
) -> dict[str, Any]:
    scope = _required_project_scope(contract)
    return {
        "request": {
            "intent": "project_document_intake",
            "external_effect": False,
            "writes_state": True,
            "transmission_requested": False,
            "memory_promotion_requested": False,
            "professional_position": False,
            "financial_or_contractual_effect": False,
            "scope": scope,
        },
        "gate_signals": {"task_contract_ref": contract.contract_id},
        "decision_expectation": {
            "required_ceiling": _required_ceiling(contract),
            "required_scope": scope,
            "object_identity": _intake_object_identity(contract, capture),
            "expected_digest": _intake_effect_digest(contract, capture),
        },
        "runtime_trace": {
            "resource": "paperless_ngx",
            "paperless_document_id": capture.document_id,
            "paperless_version_id": capture.version_id,
            "source_ref": capture.source_ref,
            "source_content_hash": capture.content_hash,
        },
    }


def _metadata_object_identity(
    contract: TaskContract,
    capture: PaperlessSourceCapture,
) -> str:
    return f"paperless-metadata:{contract.contract_id}:{capture.document_id}:{capture.version_id}"


def _metadata_effect_digest(
    contract: TaskContract,
    capture: PaperlessSourceCapture,
    changes: dict[str, Any],
) -> str:
    envelope = {
        "operation": "external_document_metadata_update",
        "contract_digest": store.contract_digest(contract),
        "source_ref": capture.source_ref,
        "source_content_hash": capture.content_hash,
        "changes": changes,
    }
    canonical = json.dumps(envelope, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _metadata_policy_candidate(
    contract: TaskContract,
    capture: PaperlessSourceCapture,
    changes: dict[str, Any],
    classification_candidate: dict[str, Any],
) -> dict[str, Any]:
    scope = _required_project_scope(contract)
    return {
        "request": {
            "intent": "external_document_metadata_update",
            "external_effect": True,
            "writes_state": True,
            "transmission_requested": False,
            "memory_promotion_requested": False,
            "professional_position": False,
            "financial_or_contractual_effect": False,
            "scope": scope,
        },
        "gate_signals": {"task_contract_ref": contract.contract_id},
        "decision_expectation": {
            "required_ceiling": _required_ceiling(contract),
            "required_scope": scope,
            "object_identity": _metadata_object_identity(contract, capture),
            "expected_digest": _metadata_effect_digest(contract, capture, changes),
        },
        "runtime_trace": {
            "resource": "paperless_ngx",
            "paperless_document_id": capture.document_id,
            "paperless_version_id": capture.version_id,
            "source_ref": capture.source_ref,
            "source_content_hash": capture.content_hash,
            "changed_fields": sorted(changes),
        },
        "classification_candidate": classification_candidate,
    }


def _default_intake_executor(
    contract: TaskContract,
    capture: PaperlessSourceCapture,
    ingestion_id: str | None,
) -> dict[str, Any]:
    conn = store.connect()
    try:
        return intake_paperless_capture(
            conn,
            contract,
            capture,
            ingestion_id=ingestion_id,
            docling=DoclingServeClient.from_env(),
        )
    finally:
        conn.close()


def create_app(
    *,
    paperless_factory: Callable[[], PaperlessClient] = _default_paperless_factory,
    policy_factory: Callable[[], PolicyClient] = _default_policy_factory,
    intake_executor: Callable[
        [TaskContract, PaperlessSourceCapture, str | None], dict[str, Any]
    ] = _default_intake_executor,
    read_api_key: str | None = None,
    hermes_api_key: str | None = None,
) -> FastAPI:
    app = FastAPI(
        title="Pantheon Paperless Gateway",
        version="0.3.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    app.state.paperless_factory = paperless_factory
    app.state.policy_factory = policy_factory
    app.state.intake_executor = intake_executor
    app.state.read_api_key = (
        read_api_key if read_api_key is not None else os.getenv("MVP_COCKPIT_API_KEY", "")
    )
    app.state.hermes_api_key = (
        hermes_api_key if hermes_api_key is not None else os.getenv("MVP_HERMES_API_KEY", "")
    )

    def require_read_key(authorization: str | None = Header(default=None)) -> None:
        supplied = _bearer_token(authorization)
        permitted = [
            value
            for value in (app.state.read_api_key, app.state.hermes_api_key)
            if value
        ]
        if not permitted:
            raise HTTPException(
                status_code=503, detail="Paperless gateway read keys are not configured"
            )
        if not any(hmac.compare_digest(supplied, expected) for expected in permitted):
            raise HTTPException(status_code=401, detail="invalid read API key")

    def require_hermes_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.hermes_api_key
        if not expected:
            raise HTTPException(
                status_code=503, detail="Paperless gateway Hermes key is not configured"
            )
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
                "intake_surface": "fail_closed",
            }
        return {
            "status": "ok",
            "paperless_reachable": bool(observed.get("reachable")),
            "write_surface": "governed_only",
            "intake_surface": "governed_only",
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
        return {"task": task, "runtime_success_is_evidence": False}

    @app.post("/v1/paperless/intakes")
    def intake_document(
        body: PaperlessIntakeBody,
        _authorized: None = Depends(require_hermes_key),
    ) -> dict[str, Any]:
        try:
            contract = _load_task_contract_yaml(body.task_contract_yaml)
            capture = paperless().capture_document(
                body.paperless_document_id,
                version_id=body.paperless_version_id,
            )
            assert_source_in_scope(contract, capture.source_ref)
            candidate = _intake_policy_candidate(contract, capture)
            result = governed_effect(
                app.state.policy_factory(),
                candidate=candidate,
                decision_payload=body.decision_payload,
                effect=lambda: app.state.intake_executor(
                    contract, capture, body.ingestion_id
                ),
            )
        except ContractError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except PaperlessConfigurationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        except (PaperlessError, DocumentConversionError, PaperlessBindingError) as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc

        return {
            **result,
            "operation": "project_document_intake",
            "task_contract_ref": contract.contract_id,
            "source_ref": capture.source_ref,
            "source_content_hash": capture.content_hash,
            "decision_expectation": candidate["decision_expectation"],
            "knowledge_published": False,
            "evidence_admitted": False,
        }

    @app.post("/v1/paperless/documents/{document_id}/metadata")
    def update_metadata(
        document_id: int,
        body: MetadataUpdateBody,
        _authorized: None = Depends(require_hermes_key),
    ) -> dict[str, Any]:
        try:
            contract = _load_task_contract_yaml(body.task_contract_yaml)
            capture = paperless().capture_document(
                document_id, version_id=body.paperless_version_id
            )
            assert_source_in_scope(contract, capture.source_ref)
            candidate = _metadata_policy_candidate(
                contract, capture, body.changes, body.classification_candidate
            )
            client = paperless()

            def apply_metadata_update() -> dict[str, Any]:
                _assert_capture_still_current(client, capture)
                return client.update_document_metadata(document_id, body.changes)

            result = governed_effect(
                app.state.policy_factory(),
                candidate=candidate,
                decision_payload=body.decision_payload,
                effect=apply_metadata_update,
            )
        except ContractError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except PaperlessMutationError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        except PaperlessConfigurationError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        except PaperlessError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc

        return {
            **result,
            "operation": "external_document_metadata_update",
            "task_contract_ref": contract.contract_id,
            "source_ref": capture.source_ref,
            "source_content_hash": capture.content_hash,
            "changed_fields": sorted(body.changes),
            "decision_expectation": candidate["decision_expectation"],
            "canonical_business_classification_changed": False,
        }

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
