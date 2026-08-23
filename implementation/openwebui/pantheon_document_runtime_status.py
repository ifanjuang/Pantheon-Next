"""
title: Pantheon Document Runtime Status
author: IFJ Architecture
version: 0.1.0
description: Read-only document runtime status projection for the Pantheon Cockpit.
requirements: httpx>=0.27
"""

from __future__ import annotations

import html
from typing import Callable
from urllib.parse import urlparse

import httpx
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field


def _escape(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def _safe_url(value: str | None) -> str | None:
    if not value:
        return None
    parsed = urlparse(value)
    return value if parsed.scheme in {"http", "https"} and parsed.netloc else None


def _badge(label: str, value: str) -> str:
    return (
        "<span class='badge'><strong>"
        + _escape(label)
        + "</strong> · "
        + _escape(value)
        + "</span>"
    )


def _card(title: str, status: str, rows: list[tuple[str, str]], note: str) -> str:
    fields = "".join(
        f"<div class='field'><span>{_escape(label)}</span>{_escape(value)}</div>"
        for label, value in rows
    )
    return (
        "<article class='card'>"
        f"<div class='eyebrow'>{_escape(status)}</div>"
        f"<h2>{_escape(title)}</h2>"
        f"<div class='meta'>{fields}</div>"
        f"<p class='muted'>{_escape(note)}</p>"
        "</article>"
    )


def _shell(content: str) -> str:
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy"
        content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
  <title>Pantheon · Document Runtime Status</title>
  <style>
    :root {{ color-scheme: light dark; --bg:#f4f2ed; --panel:#fffefb; --ink:#252521;
      --muted:#6d6c65; --line:#dedbd2; --accent:#314f45; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; padding:18px; background:var(--bg); color:var(--ink);
      font:14px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ display:grid; gap:12px; max-width:1080px; margin:auto; }}
    .panel,.card {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:14px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(245px,1fr)); gap:10px; }}
    .eyebrow {{ color:var(--accent); font-size:11px; font-weight:750; text-transform:uppercase; letter-spacing:.08em; }}
    h1,h2,p {{ margin:0; }} h1 {{ font-size:21px; margin-top:4px; }} h2 {{ font-size:16px; }}
    .muted {{ color:var(--muted); margin-top:10px; }}
    .badge {{ display:inline-block; border:1px solid var(--line); border-radius:999px; padding:4px 8px; margin:8px 5px 0 0; font-size:12px; }}
    .meta {{ display:grid; gap:7px; margin-top:12px; }}
    .field {{ border-top:1px solid var(--line); padding-top:7px; overflow-wrap:anywhere; }}
    .field span {{ display:block; font-size:11px; color:var(--muted); text-transform:uppercase; }}
    @media (prefers-color-scheme:dark) {{ :root {{ --bg:#191a18; --panel:#242522; --ink:#ecebe5; --muted:#afaea6; --line:#3c3d38; --accent:#a7c7bb; }} }}
  </style>
</head>
<body><main>{content}</main></body>
</html>"""


class Tools:
    class Valves(BaseModel):
        gateway_url: str = Field(
            default="http://paperless-gateway:8082",
            description="Internal bounded Paperless gateway URL",
        )
        api_key: str = Field(
            default="",
            description="Cockpit read key for the bounded gateway",
            json_schema_extra={"input": {"type": "password"}},
        )
        timeout_seconds: float = Field(default=10.0, ge=1.0, le=30.0)

    def __init__(self, client_factory: Callable | None = None):
        self.valves = self.Valves()
        self._client_factory = client_factory or httpx.AsyncClient

    def _base_url(self) -> str:
        value = _safe_url(self.valves.gateway_url.rstrip("/"))
        if value is None:
            raise ValueError("Document runtime gateway URL must use http or https")
        if not self.valves.api_key:
            raise ValueError("Document runtime status read key is not configured")
        return value

    def _client(self):
        return self._client_factory(
            timeout=self.valves.timeout_seconds,
            follow_redirects=False,
            headers={"Authorization": f"Bearer {self.valves.api_key}"},
        )

    async def show_document_runtime_status(self) -> tuple:
        """Show bounded runtime observations without converting reachability into safety."""

        base = self._base_url()
        async with self._client() as client:
            response = await client.get(f"{base}/health")
            response.raise_for_status()
            health = response.json()

        gateway_status = str(health.get("status") or "unknown")
        paperless_reachable = bool(health.get("paperless_reachable"))
        paperless_reachability = "reachable" if paperless_reachable else "unreachable"
        intake_surface = str(health.get("intake_surface") or "unknown")
        write_surface = str(health.get("write_surface") or "unknown")

        content = (
            "<section class='panel'><div class='eyebrow'>Document Runtime Status</div>"
            "<h1>Source documentaire et bindings</h1>"
            "<p class='muted'>Cette vue sépare présence observée, reachability, health, activation et autorisation.</p>"
            + _badge("Paperless", paperless_reachability)
            + _badge("Gateway", gateway_status)
            + _badge("Intake", intake_surface)
            + "</section>"
            + "<section class='grid'>"
            + _card(
                "Paperless-ngx",
                "runtime observation",
                [
                    ("Reachability", paperless_reachability),
                    ("Health", "not_established_by_reachability_probe"),
                    ("Safety", "not_inferred"),
                ],
                "Paperless reachable signifie seulement que le gateway a pu effectuer son probe borné.",
            )
            + _card(
                "Paperless Gateway",
                "exposure adapter",
                [
                    ("Service", gateway_status),
                    ("Project Document intake", intake_surface),
                    ("Native Paperless writes", write_surface),
                ],
                "Le gateway expose et applique le PEP ; il ne devient ni DMS, ni policy authority.",
            )
            + _card(
                "Pantheon PDP",
                "not observed here",
                [
                    ("Binding", "evaluated_at_effect_time"),
                    ("Reachability", "not_observed_by_this_surface"),
                    ("Effect authorization", "not_inferred_from_gateway_health"),
                ],
                "Le statut policy doit provenir du PDP lui-même. Un gateway healthy ne prouve aucune autorisation.",
            )
            + _card(
                "Docling",
                "not observed here",
                [
                    ("Binding", "required_for_binary_intake"),
                    ("Reachability", "not_observed_by_this_surface"),
                    ("Extraction health", "not_established"),
                ],
                "Le succès Paperless n'établit pas la disponibilité ni la qualité de l'analyse Docling.",
            )
            + _card(
                "Hermes skill",
                "native inventory required",
                [
                    ("Skill", "pantheon-document-intake"),
                    ("Installation", "not_observed_by_gateway"),
                    ("Activation", "not_inferred"),
                ],
                "L'installation du skill doit être observée dans l'inventaire natif Hermes, pas déduite du gateway.",
            )
            + _card(
                "Pantheon activation",
                "governance",
                [
                    ("Installed", "not_equal_approved"),
                    ("Healthy", "not_equal_safe"),
                    ("Runtime success", "not_equal_evidence"),
                ],
                "Cette carte ne change aucun statut d'adoption, d'activation, de Knowledge ou d'Evidence.",
            )
            + "</section>"
        )

        context = {
            "object_type": "document_runtime_status",
            "source_runtime": {
                "resource": "paperless_ngx",
                "reachability_status": paperless_reachability,
                "health_status": "not_established_by_reachability_probe",
            },
            "gateway": {
                "status": gateway_status,
                "intake_surface": intake_surface,
                "write_surface": write_surface,
            },
            "policy": {
                "reachability_status": "not_observed_by_this_surface",
                "authorization_status": "not_inferred",
            },
            "docling": {
                "reachability_status": "not_observed_by_this_surface",
                "health_status": "not_established",
            },
            "hermes_skill": {
                "skill": "pantheon-document-intake",
                "installation_status": "not_observed_by_gateway",
                "inventory_source": "hermes_native_inventory",
            },
            "governance": {
                "activation_changed": False,
                "authority_effect": "none",
                "write_effect": False,
            },
        }
        return HTMLResponse(_shell(content)), context
