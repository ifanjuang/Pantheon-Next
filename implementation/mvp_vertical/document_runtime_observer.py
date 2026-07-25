"""Read-only observations for the document runtime stack.

This module is an external runtime observation adapter. It does not install,
activate, approve, update or execute document work. Each observation keeps its
own source and timestamp so reachability cannot collapse into a synthetic global
"healthy" state.
"""

from __future__ import annotations

import hmac
import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timezone
from typing import Any, Callable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from fastapi import Depends, FastAPI, Header, HTTPException


_SKILL_NAME = "pantheon-document-intake"
_SKILL_TOKEN = re.compile(r"(?<![A-Za-z0-9_-])pantheon-document-intake(?![A-Za-z0-9_-])")


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


def _bounded_json_get(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> tuple[int, dict[str, Any] | None]:
    request = Request(url, headers={"Accept": "application/json", **(headers or {})}, method="GET")
    try:
        with opener(request, timeout=timeout) as response:
            status = int(getattr(response, "status", None) or response.getcode())
            raw = response.read(256_000)
    except HTTPError as exc:
        return int(exc.code), None
    except (URLError, TimeoutError, OSError):
        return 0, None

    if not raw:
        return status, {}
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError):
        return status, None
    return status, payload if isinstance(payload, dict) else None


def observe_paperless_gateway(
    base_url: str,
    read_key: str,
    *,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    observed_at = _observed_at()
    if not read_key:
        return {
            "source": "paperless_gateway",
            "observation_source": "bounded_gateway_health",
            "observed_at": observed_at,
            "reachability_status": "not_configured",
            "paperless_reachability_status": "not_observed",
            "health_status": "not_established",
            "safety_status": "not_inferred",
        }
    try:
        base = _safe_base_url(base_url, "Paperless gateway URL")
    except ValueError as exc:
        return {
            "source": "paperless_gateway",
            "observation_source": "bounded_gateway_health",
            "observed_at": observed_at,
            "reachability_status": "configuration_error",
            "detail": str(exc),
            "health_status": "not_established",
            "safety_status": "not_inferred",
        }
    status, payload = _bounded_json_get(
        f"{base}/health",
        headers={"Authorization": f"Bearer {read_key}"},
        timeout=timeout,
        opener=opener,
    )
    reachable = 200 <= status < 300 and isinstance(payload, dict)
    if not reachable:
        return {
            "source": "paperless_gateway",
            "observation_source": "bounded_gateway_health",
            "observed_at": observed_at,
            "reachability_status": "unreachable",
            "http_status": status or None,
            "paperless_reachability_status": "not_observed",
            "health_status": "not_established",
            "safety_status": "not_inferred",
        }
    paperless = bool(payload.get("paperless_reachable"))
    return {
        "source": "paperless_gateway",
        "observation_source": "bounded_gateway_health",
        "observed_at": observed_at,
        "reachability_status": "reachable",
        "http_status": status,
        "service_status": str(payload.get("status") or "unknown"),
        "paperless_reachability_status": "reachable" if paperless else "unreachable",
        "intake_surface": str(payload.get("intake_surface") or "unknown"),
        "write_surface": str(payload.get("write_surface") or "unknown"),
        "health_status": "not_established_by_reachability_probe",
        "safety_status": "not_inferred",
    }


def observe_pantheon_pdp(
    base_url: str,
    api_key: str,
    *,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    observed_at = _observed_at()
    if not api_key:
        return {
            "source": "pantheon_pdp",
            "observation_source": "pantheon_policy_http",
            "observed_at": observed_at,
            "reachability_status": "not_configured",
            "readiness_status": "not_observed",
            "authorization_status": "not_inferred",
            "safety_status": "not_inferred",
        }
    try:
        base = _safe_base_url(base_url, "Pantheon policy URL")
    except ValueError as exc:
        return {
            "source": "pantheon_pdp",
            "observation_source": "pantheon_policy_http",
            "observed_at": observed_at,
            "reachability_status": "configuration_error",
            "detail": str(exc),
            "readiness_status": "not_observed",
            "authorization_status": "not_inferred",
            "safety_status": "not_inferred",
        }

    auth = {"Authorization": f"Bearer {api_key}"}
    ready_status, ready = _bounded_json_get(
        f"{base}/readyz", headers=auth, timeout=timeout, opener=opener
    )
    meta_status, meta = _bounded_json_get(
        f"{base}/v1/meta", headers=auth, timeout=timeout, opener=opener
    )
    reachable = 200 <= ready_status < 300 or 200 <= meta_status < 300
    ready_observed = 200 <= ready_status < 300
    safe_meta: dict[str, Any] = {}
    if isinstance(meta, dict):
        for key in ("contract", "source_mode", "policy_version", "mode"):
            if key in meta:
                safe_meta[key] = meta[key]
        repository = meta.get("repository")
        if isinstance(repository, dict):
            safe_meta["repository"] = {
                key: repository.get(key)
                for key in ("version", "commit")
                if repository.get(key) not in (None, "")
            }

    return {
        "source": "pantheon_pdp",
        "observation_source": "pantheon_policy_http",
        "observed_at": observed_at,
        "reachability_status": "reachable" if reachable else "unreachable",
        "readiness_status": "ready_observed" if ready_observed else "not_ready_observed",
        "readyz_http_status": ready_status or None,
        "meta_http_status": meta_status or None,
        "metadata": safe_meta,
        "authorization_status": "not_inferred_from_readiness",
        "safety_status": "not_inferred",
    }


def observe_docling(
    base_url: str,
    api_key: str | None = None,
    *,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    observed_at = _observed_at()
    try:
        base = _safe_base_url(base_url, "Docling Serve URL")
    except ValueError as exc:
        return {
            "source": "docling_serve",
            "observation_source": "docling_health_endpoint",
            "observed_at": observed_at,
            "reachability_status": "configuration_error",
            "detail": str(exc),
            "extraction_quality_status": "not_established",
            "safety_status": "not_inferred",
        }
    headers = {"X-Api-Key": api_key} if api_key else {}
    status, payload = _bounded_json_get(
        f"{base}/health", headers=headers, timeout=timeout, opener=opener
    )
    reachable = 200 <= status < 300
    endpoint_status = "healthy_endpoint_observed" if reachable else "health_endpoint_unreachable"
    if isinstance(payload, dict) and payload.get("status") not in (None, ""):
        endpoint_status = str(payload["status"])
    return {
        "source": "docling_serve",
        "observation_source": "docling_health_endpoint",
        "observed_at": observed_at,
        "reachability_status": "reachable" if reachable else "unreachable",
        "http_status": status or None,
        "health_endpoint_status": endpoint_status,
        "extraction_quality_status": "not_established_by_health_probe",
        "safety_status": "not_inferred",
    }


def observe_hermes_skill_inventory(
    *,
    mode: str = "disabled",
    cli_path: str = "hermes",
    timeout: float = 10.0,
    runner: Callable[..., Any] = subprocess.run,
    which: Callable[[str], str | None] = shutil.which,
) -> dict[str, Any]:
    observed_at = _observed_at()
    if mode != "local_cli":
        return {
            "source": "hermes_native_inventory",
            "observation_source": "hermes_skills_list",
            "observed_at": observed_at,
            "runtime_cli_status": "not_observed",
            "skill": _SKILL_NAME,
            "installation_status": "not_observed",
            "activation_status": "not_inferred",
            "approval_status": "not_inferred",
        }

    executable = cli_path if os.path.isabs(cli_path) else which(cli_path)
    if not executable:
        return {
            "source": "hermes_native_inventory",
            "observation_source": "hermes_skills_list",
            "observed_at": observed_at,
            "runtime_cli_status": "cli_missing_on_observer_host",
            "skill": _SKILL_NAME,
            "installation_status": "not_observed",
            "activation_status": "not_inferred",
            "approval_status": "not_inferred",
        }
    try:
        completed = runner(
            [executable, "skills", "list"],
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "source": "hermes_native_inventory",
            "observation_source": "hermes_skills_list",
            "observed_at": observed_at,
            "runtime_cli_status": "observation_error",
            "detail": str(exc),
            "skill": _SKILL_NAME,
            "installation_status": "not_observed",
            "activation_status": "not_inferred",
            "approval_status": "not_inferred",
        }

    output = (completed.stdout or "") + "\n" + (completed.stderr or "")
    command_ok = int(completed.returncode) == 0
    installed = bool(command_ok and _SKILL_TOKEN.search(output))
    return {
        "source": "hermes_native_inventory",
        "observation_source": "hermes_skills_list",
        "observed_at": observed_at,
        "runtime_cli_status": "observed" if command_ok else "command_failed",
        "command_exit_code": int(completed.returncode),
        "skill": _SKILL_NAME,
        "installation_status": (
            "installed_observed" if installed else "not_listed_observed" if command_ok else "not_observed"
        ),
        "activation_status": "not_inferred",
        "approval_status": "not_inferred",
    }


def collect_document_runtime_observations(
    *,
    paperless_gateway_url: str,
    cockpit_read_key: str,
    policy_url: str,
    policy_api_key: str,
    docling_url: str,
    docling_api_key: str | None,
    hermes_inventory_mode: str,
    hermes_cli_path: str,
    timeout: float = 8.0,
    opener: Callable[..., Any] = urlopen,
    runner: Callable[..., Any] = subprocess.run,
    which: Callable[[str], str | None] = shutil.which,
) -> dict[str, Any]:
    observations = [
        observe_paperless_gateway(
            paperless_gateway_url,
            cockpit_read_key,
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
        observe_hermes_skill_inventory(
            mode=hermes_inventory_mode,
            cli_path=hermes_cli_path,
            timeout=timeout,
            runner=runner,
            which=which,
        ),
    ]
    return {
        "object_type": "document_runtime_observation_set",
        "observed_at": _observed_at(),
        "observations": observations,
        "synthetic_global_health": "not_computed",
        "authority_effect": "none",
        "write_effect": False,
        "activation_changed": False,
        "non_equivalences": [
            "reachable != healthy",
            "healthy != safe",
            "installed != approved",
            "PDP ready != effect authorized",
            "runtime success != Evidence",
            "runtime observation != activation decision",
        ],
    }


def create_app(
    *,
    read_api_key: str | None = None,
    collector: Callable[..., dict[str, Any]] = collect_document_runtime_observations,
) -> FastAPI:
    app = FastAPI(
        title="Pantheon Document Runtime Observer",
        version="0.1.0",
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
            raise HTTPException(status_code=503, detail="document runtime observer read key is not configured")
        if not hmac.compare_digest(_bearer_token(authorization), expected):
            raise HTTPException(status_code=401, detail="invalid read API key")

    @app.get("/health")
    def health() -> dict[str, Any]:
        return {
            "status": "ok",
            "meaning": "observer_process_liveness_only",
            "authority_effect": "none",
        }

    @app.get("/v1/document-runtime/observations")
    def observations(_authorized: None = Depends(require_read_key)) -> dict[str, Any]:
        return app.state.collector(
            paperless_gateway_url=os.getenv(
                "PANTHEON_PAPERLESS_GATEWAY_URL", "http://paperless-gateway:8082"
            ),
            cockpit_read_key=app.state.read_api_key,
            policy_url=os.getenv("PANTHEON_POLICY_API_URL", "http://pantheon-policy-api:8000"),
            policy_api_key=os.getenv("PANTHEON_POLICY_API_KEY", ""),
            docling_url=os.getenv("DOCLING_SERVE_URL", "http://docling-serve:5001"),
            docling_api_key=os.getenv("DOCLING_SERVE_API_KEY") or None,
            hermes_inventory_mode=os.getenv("MVP_HERMES_INVENTORY_MODE", "disabled"),
            hermes_cli_path=os.getenv("HERMES_CLI_PATH", "hermes"),
            timeout=float(os.getenv("MVP_RUNTIME_OBSERVER_TIMEOUT", "8")),
        )

    return app


app = create_app()


def run() -> None:
    import uvicorn

    uvicorn.run(
        "mvp_vertical.document_runtime_observer:app",
        host=os.getenv("MVP_RUNTIME_OBSERVER_HOST", "127.0.0.1"),
        port=int(os.getenv("MVP_RUNTIME_OBSERVER_PORT", "8083")),
        reload=False,
    )


if __name__ == "__main__":
    run()
