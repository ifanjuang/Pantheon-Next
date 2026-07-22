"""Bounded HTTP projection of the Pantheon policy service.

This internal-network adapter is read-only. It is not an execution runtime,
approval engine, evidence store, memory engine or connector gateway. All policy
meaning lives in :mod:`pantheon_mcp.service`.
"""

from __future__ import annotations

import hmac
import os
from typing import Any, Callable

from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse

from .repo import RepoNotFound
from .service import POLICY_CONTRACT, PantheonPolicyService

DEFAULT_MAX_BODY_BYTES = 256 * 1024


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def _env_flag(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _compatibility_gap(operation: str, replacement: list[str]) -> dict[str, Any]:
    return {
        "contract": POLICY_CONTRACT,
        "operation": operation,
        "result": "contract_not_defined",
        "authority_effect": "none",
        "authorization_effect": "none",
        "write_effect": False,
        "execution_effect": False,
        "replacement": replacement,
        "message": (
            "The legacy route has no canonical object contract. Use the explicit "
            "versioned operation instead of inferring snapshot or context semantics."
        ),
    }


def create_app(
    *,
    service: PantheonPolicyService | None = None,
    api_key: str | None = None,
    max_body_bytes: int | None = None,
    enable_docs: bool | None = None,
) -> FastAPI:
    """Create the HTTP adapter with injectable dependencies for tests."""
    docs_enabled = (
        _env_flag("PANTHEON_POLICY_ENABLE_DOCS") if enable_docs is None else enable_docs
    )
    app = FastAPI(
        title="Pantheon Policy API",
        version="1.0.0-candidate",
        docs_url="/docs" if docs_enabled else None,
        redoc_url=None,
        openapi_url="/openapi.json" if docs_enabled else None,
    )
    app.state.service = service
    app.state.api_key = (
        api_key if api_key is not None else os.getenv("PANTHEON_POLICY_API_KEY", "")
    )
    app.state.max_body_bytes = max_body_bytes or int(
        os.getenv("PANTHEON_POLICY_MAX_BODY_BYTES", str(DEFAULT_MAX_BODY_BYTES))
    )

    def get_service() -> PantheonPolicyService:
        if app.state.service is None:
            app.state.service = PantheonPolicyService()
        return app.state.service

    def require_api_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.api_key
        if not expected:
            raise HTTPException(
                status_code=503,
                detail="Pantheon policy API key is not configured",
            )
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid policy API key")

    @app.middleware("http")
    async def enforce_body_limit(request: Request, call_next: Callable):
        if request.method in {"POST", "PUT", "PATCH"}:
            declared = request.headers.get("content-length")
            if declared:
                try:
                    if int(declared) > app.state.max_body_bytes:
                        return JSONResponse(
                            status_code=413,
                            content={
                                "contract": POLICY_CONTRACT,
                                "result": "request_too_large",
                                "max_body_bytes": app.state.max_body_bytes,
                            },
                        )
                except ValueError:
                    return JSONResponse(
                        status_code=400,
                        content={
                            "contract": POLICY_CONTRACT,
                            "result": "invalid_content_length",
                        },
                    )
            body = await request.body()
            if len(body) > app.state.max_body_bytes:
                return JSONResponse(
                    status_code=413,
                    content={
                        "contract": POLICY_CONTRACT,
                        "result": "request_too_large",
                        "max_body_bytes": app.state.max_body_bytes,
                    },
                )

            async def receive() -> dict[str, Any]:
                return {"type": "http.request", "body": body, "more_body": False}

            request._receive = receive
        return await call_next(request)

    @app.exception_handler(RepoNotFound)
    async def repo_not_found(_request: Request, exc: RepoNotFound) -> JSONResponse:
        return JSONResponse(
            status_code=503,
            content={
                "contract": POLICY_CONTRACT,
                "result": "repository_unavailable",
                "message": str(exc),
                "authority_effect": "none",
                "authorization_effect": "none",
            },
        )

    @app.get("/livez")
    def livez() -> dict[str, Any]:
        return {"status": "alive", "service": "pantheon-policy-api"}

    @app.get("/readyz", response_model=None)
    def readyz() -> Any:
        try:
            state = get_service().repository_state()
        except (RepoNotFound, OSError) as exc:
            return JSONResponse(
                status_code=503,
                content={"status": "not_ready", "reason": str(exc)},
            )
        return {
            "status": "ready",
            "repository_accessible": state["repository_accessible"],
            "repository": state["repository"],
            "warning": "ready != safe; healthy != authorized",
        }

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "mode": "read_only",
            "service": "pantheon-policy-api",
            "warning": "healthy != safe; runtime success != evidence",
        }

    protected = [Depends(require_api_key)]

    @app.get("/v1/meta", dependencies=protected)
    def meta() -> dict[str, Any]:
        return get_service().meta()

    @app.get("/v1/repository/state", dependencies=protected)
    def repository_state() -> dict[str, Any]:
        return get_service().repository_state()

    @app.get("/v1/consultation", dependencies=protected)
    def consultation_catalog() -> dict[str, Any]:
        return get_service().consultation_catalog()

    @app.get("/v1/sources", dependencies=protected)
    def list_sources() -> dict[str, Any]:
        return get_service().list_sources()

    @app.get("/v1/sources/{key}", dependencies=protected)
    def read_source(key: str) -> dict[str, Any]:
        return get_service().read_doctrine(key)

    @app.get("/v1/architecture/{topic}", dependencies=protected)
    def explain_architecture(topic: str) -> dict[str, Any]:
        return get_service().explain_architecture(topic)

    @app.post("/v1/policy/requests:classify", dependencies=protected)
    def classify_request(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().classify_request(body)

    @app.post("/v1/policy/preflights:evaluate", dependencies=protected)
    def evaluate_preflight(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().evaluate_preflight(body)

    @app.post("/v1/policy/external-actions:check", dependencies=protected)
    def check_external_action(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().check_external_action(str(body.get("description", "")))

    @app.post("/v1/observations/capabilities:qualify", dependencies=protected)
    def qualify_capability_status(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().qualify_capability_status(body)

    @app.post("/v1/candidates/task-contracts:prepare", dependencies=protected)
    def prepare_task_contract(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().prepare_task_contract(body)

    @app.post("/v1/candidates/evidence-packs:prepare", dependencies=protected)
    def prepare_evidence_pack(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().prepare_evidence_pack(body)

    @app.post("/v1/validations/passports", dependencies=protected)
    def validate_passport(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().validate_passport(body)

    @app.post("/v1/validations/apu-dossiers", dependencies=protected)
    def validate_apu_dossier(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().validate_apu_dossier(body)

    @app.post("/v1/verifications/install", dependencies=protected)
    def verify_install(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().verify_install(body)

    @app.post("/v1/verifications/observability", dependencies=protected)
    def verify_observability(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().verify_observability(body)

    @app.post("/v1/verifications/backup", dependencies=protected)
    def verify_backup(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().verify_backup(body)

    @app.post("/v1/verifications/exposure", dependencies=protected)
    def verify_exposure(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().verify_exposure(body)

    @app.post("/v1/verifications/update", dependencies=protected)
    def verify_update(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().verify_update(body)

    @app.post("/v1/verifications/presets:load", dependencies=protected)
    def load_verification_preset(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().load_verification_preset(body)

    @app.get("/v1/doctor", dependencies=protected)
    def run_doctor() -> dict[str, Any]:
        return get_service().run_doctor()

    @app.post("/v1/context-packs:plan", dependencies=protected)
    def plan_context_pack(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().plan_context_pack(body)

    @app.post("/v1/context-packs:validate", dependencies=protected)
    def validate_context_pack(body: dict[str, Any]) -> dict[str, Any]:
        return get_service().validate_context_pack(body)

    @app.post("/domain/approval/classify", dependencies=protected)
    def legacy_approval_classify(body: dict[str, Any]) -> dict[str, Any]:
        response = get_service().classify_request(body)
        response["compatibility_route"] = True
        response["replacement"] = "/v1/policy/requests:classify"
        return response

    @app.get("/runtime/context-pack", dependencies=protected)
    def legacy_context_pack() -> JSONResponse:
        return JSONResponse(
            status_code=501,
            content=_compatibility_gap(
                "legacy.context_pack",
                ["POST /v1/context-packs:plan", "POST /v1/context-packs:validate"],
            ),
        )

    @app.get("/domain/snapshot", dependencies=protected)
    def legacy_snapshot() -> JSONResponse:
        return JSONResponse(
            status_code=501,
            content=_compatibility_gap(
                "legacy.domain_snapshot",
                [
                    "GET /v1/repository/state",
                    "POST /v1/observations/capabilities:qualify",
                ],
            ),
        )

    return app


app = create_app()


def run() -> None:
    """Run the internal policy API with uvicorn."""
    import uvicorn

    uvicorn.run(
        "pantheon_mcp.http_api:app",
        host=os.getenv("PANTHEON_POLICY_HOST", "0.0.0.0"),
        port=int(os.getenv("PANTHEON_POLICY_PORT", "8000")),
        reload=False,
        access_log=_env_flag("PANTHEON_POLICY_ACCESS_LOG", False),
    )


if __name__ == "__main__":
    run()
