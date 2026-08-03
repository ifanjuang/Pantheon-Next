"""Network-native read-only observations for the document runtime stack.

This adapter is intended for multi-container deployments where the observer is
not co-located with the Hermes CLI. It uses Hermes' authenticated read-only
``GET /v1/skills`` API to observe whether the bounded document skill is listed.

Paperless is an optional ``document_source_management`` binding. When it is not
selected, the observer emits an explicit ``not_selected`` / ``not_applicable``
projection instead of misclassifying the intentionally absent runtime as
unreachable or degraded.

The module observes only. It does not install, enable, approve, activate,
update, execute, schedule or route document work.
"""

from __future__ import annotations

import hmac
import json
import os
from datetime import datetime, timezone
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from fastapi import Depends, FastAPI, Header, HTTPException

from .document_runtime_observer import (
    observe_docling,
    observe_pantheon_pdp,
    observe_paperless_gateway,
)
from .runtime_observation import normalize_runtime_observations

_SKILL_NAME = "pantheon-document-intake"
_PAPERLESS_BINDING = "paperless_ngx"
_LOCAL_SOURCE_BINDING = "governed_local_source"


def _observed_at() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _safe_base_url(value: str, label: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"{label} must use http:// or https://")
    return value.rstrip("/")


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def _bounded_json_value(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> tuple[int, Any | None]:
    request = Request(
        url,
        headers={"Accept": "application/json", **(headers or {})},
        method="GET",
    )
    try:
        with opener(request, timeout=timeout) as response:
            status = int(getattr(response, "status", None) or response.getcode())
            raw = response.read(256_000)
    except HTTPError as exc:
        return int(exc.code), None
    except (URLError, TimeoutError, OSError):
        return 0, None

    if not raw:
        return status, None
    try:
        return status, json.loads(raw.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError):
        return status, None


def _normalize_source_binding(value: str | None) -> str:
    binding = (value or _LOCAL_SOURCE_BINDING).strip().lower()
    return binding or _LOCAL_SOURCE_BINDING


def observe_document_source_binding(
    binding: str,
    *,
    paperless_gateway_url: str,
    cockpit_read_key: str,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    """Observe only the selected document-source-management binding."""

    normalized = _normalize_source_binding(binding)
    if normalized == _PAPERLESS_BINDING:
        observed = observe_paperless_gateway(
            paperless_gateway_url,
            cockpit_read_key,
            timeout=timeout,
            opener=opener,
        )
        return {
            **observed,
            "capability": "document_source_management",
            "binding": _PAPERLESS_BINDING,
            "selection_status": "selected",
        }

    if normalized == _LOCAL_SOURCE_BINDING:
        return {
            "source": "document_source_management",
            "observation_source": "binding_configuration",
            "observed_at": _observed_at(),
            "capability": "document_source_management",
            "binding": _PAPERLESS_BINDING,
            "selected_binding": _LOCAL_SOURCE_BINDING,
            "selection_status": "not_selected",
            "installation_status": "not_applicable",
            "reachability_status": "not_applicable",
            "health_status": "not_applicable",
            "safety_status": "not_inferred",
            "detail": "Paperless is optional; governed local/NAS source ingestion remains available.",
        }

    return {
        "source": "document_source_management",
        "observation_source": "binding_configuration",
        "observed_at": _observed_at(),
        "capability": "document_source_management",
        "binding": normalized,
        "selection_status": "unsupported_binding",
        "installation_status": "not_observed",
        "reachability_status": "not_observed",
        "health_status": "not_observed",
        "safety_status": "not_inferred",
    }


def observe_hermes_skills_api(
    base_url: str,
    api_key: str,
    *,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    """Observe one skill through Hermes' authenticated read-only REST API."""

    observed_at = _observed_at()
    base_result = {
        "source": "hermes_native_inventory",
        "observation_source": "hermes_api_v1_skills",
        "observed_at": observed_at,
        "skill": _SKILL_NAME,
        "activation_status": "not_inferred",
        "approval_status": "not_inferred",
    }

    if not api_key:
        return {
            **base_result,
            "reachability_status": "not_configured",
            "runtime_api_status": "not_observed",
            "installation_status": "not_observed",
        }

    try:
        base = _safe_base_url(base_url, "Hermes API URL")
    except ValueError as exc:
        return {
            **base_result,
            "reachability_status": "configuration_error",
            "runtime_api_status": "not_observed",
            "installation_status": "not_observed",
            "detail": str(exc),
        }

    status, payload = _bounded_json_value(
        f"{base}/v1/skills",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=timeout,
        opener=opener,
    )
    reachable = 200 <= status < 300
    if not reachable:
        return {
            **base_result,
            "reachability_status": "unreachable",
            "http_status": status or None,
            "runtime_api_status": "endpoint_unreachable",
            "installation_status": "not_observed",
        }

    items: list[Any] | None = None
    if isinstance(payload, list):
        items = payload
    elif isinstance(payload, dict) and isinstance(payload.get("skills"), list):
        items = payload["skills"]

    if items is None:
        return {
            **base_result,
            "reachability_status": "reachable",
            "http_status": status,
            "runtime_api_status": "invalid_payload",
            "installation_status": "not_observed",
        }

    names = {
        str(item.get("name"))
        for item in items
        if isinstance(item, dict) and item.get("name") not in (None, "")
    }
    installed = _SKILL_NAME in names
    return {
        **base_result,
        "reachability_status": "reachable",
        "http_status": status,
        "runtime_api_status": "observed",
        "observed_skill_count": len(names),
        "installation_status": "installed_observed" if installed else "not_listed_observed",
    }


def collect_network_document_runtime_observations(
    *,
    document_source_binding: str,
    paperless_gateway_url: str,
    cockpit_read_key: str,
    policy_url: str,
    policy_api_key: str,
    docling_url: str,
    docling_api_key: str | None,
    hermes_api_url: str,
    hermes_api_key: str,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    normalized_binding = _normalize_source_binding(document_source_binding)
    observations = normalize_runtime_observations(
        [
            observe_document_source_binding(
                normalized_binding,
                paperless_gateway_url=paperless_gateway_url,
                cockpit_read_key=cockpit_read_key,
                timeout=timeout,
                opener=opener,
            ),
            observe_pantheon_pdp(
                policy_url,
                policy_api_key,
                timeout=timeout,
                opener=opener,
            ),
            observe_docling(
                docling_url,
                docling_api_key,
                timeout=timeout,
                opener=opener,
            ),
            observe_hermes_skills_api(
                hermes_api_url,
                hermes_api_key,
                timeout=timeout,
                opener=opener,
            ),
        ],
        label="network document runtime observations",
    )
    return {
        "object_type": "document_runtime_observation_set",
        "observed_at": _observed_at(),
        "document_source_binding": normalized_binding,
        "observations": observations,
        "synthetic_global_health": "not_computed",
        "authority_effect": "none",
        "write_effect": False,
        "activation_changed": False,
        "non_equivalences": [
            "Paperless absent != Pantheon degraded",
            "Paperless absent != document ingestion unavailable",
            "reachable != healthy",
            "healthy != safe",
            "installed != approved",
            "Hermes skill listed != capability approved",
            "PDP ready != effect authorized",
            "runtime success != Evidence",
            "runtime observation != activation decision",
        ],
    }


def create_app(
    *,
    read_api_key: str | None = None,
    collector: Callable[..., dict[str, Any]] = collect_network_document_runtime_observations,
) -> FastAPI:
    app = FastAPI(
        title="Pantheon Document Runtime Network Observer",
        version="0.2.0",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )
    app.state.read_api_key = (
        read_api_key if read_api_key is not None else os.getenv("MVP_COCKPIT_API_KEY", "")
    )
    app.state.collector = collector

    def require_read_key(authorization: str | None = Header(default=None)) -> None:
        expected = app.state.read_api_key
        if not expected:
            raise HTTPException(
                status_code=503,
                detail="document runtime network observer read key is not configured",
            )
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid read API key")

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "meaning": "observer_process_liveness_only",
            "authority_effect": "none",
        }

    @app.get("/documents/observations")
    def observations(_authorized: None = Depends(require_read_key)) -> dict[str, Any]:
        return app.state.collector(
            document_source_binding=os.getenv(
                "MVP_DOCUMENT_SOURCE_BINDING", _LOCAL_SOURCE_BINDING
            ),
            paperless_gateway_url=os.getenv("PANTHEON_PAPERLESS_GATEWAY_URL", ""),
            cockpit_read_key=app.state.read_api_key,
            policy_url=os.getenv("PANTHEON_POLICY_API_URL", "http://pantheon-policy-api:8000"),
            policy_api_key=os.getenv("PANTHEON_POLICY_API_KEY", ""),
            docling_url=os.getenv("DOCLING_SERVE_URL", "http://docling:5001"),
            docling_api_key=os.getenv("DOCLING_SERVE_API_KEY") or None,
            hermes_api_url=os.getenv("HERMES_API_URL", "http://hermes:8642"),
            hermes_api_key=os.getenv("HERMES_API_SERVER_KEY", ""),
            timeout=float(os.getenv("MVP_RUNTIME_OBSERVER_TIMEOUT", "8")),
        )

    return app


app = create_app()


def run() -> None:
    import uvicorn

    uvicorn.run(
        "mvp_vertical.document_runtime_network_observer:app",
        host=os.getenv("MVP_RUNTIME_OBSERVER_HOST", "127.0.0.1"),
        port=int(os.getenv("MVP_RUNTIME_OBSERVER_PORT", "8083")),
        reload=False,
    )


if __name__ == "__main__":
    run()
