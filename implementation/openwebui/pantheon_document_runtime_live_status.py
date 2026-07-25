"""
title: Pantheon Document Runtime Live Status
author: IFJ Architecture
version: 0.1.0
description: Read-only source-attributed runtime observations for the Pantheon Cockpit.
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


def _card(title: str, observation: dict) -> str:
    ignored = {"source", "observation_source", "observed_at", "metadata"}
    rows = []
    for key, value in observation.items():
        if key in ignored or isinstance(value, (dict, list)):
            continue
        rows.append(
            f"<div class='field'><span>{_escape(key.replace('_', ' '))}</span>{_escape(value)}</div>"
        )
    metadata = observation.get("metadata")
    if isinstance(metadata, dict) and metadata:
        rows.append(
            "<div class='field'><span>metadata</span>"
            + _escape(metadata)
            + "</div>"
        )
    return (
        "<article class='card'>"
        f"<div class='eyebrow'>{_escape(observation.get('observation_source') or 'observation')}</div>"
        f"<h2>{_escape(title)}</h2>"
        f"<p class='muted'>{_escape(observation.get('observed_at') or 'timestamp absent')}</p>"
        f"<div class='meta'>{''.join(rows)}</div>"
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
  <title>Pantheon · Document Runtime Observations</title>
  <style>
    :root {{ color-scheme: light dark; --bg:#f4f2ed; --panel:#fffefb; --ink:#252521;
      --muted:#6d6c65; --line:#dedbd2; --accent:#314f45; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; padding:18px; background:var(--bg); color:var(--ink);
      font:14px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ display:grid; gap:12px; max-width:1120px; margin:auto; }}
    .panel,.card {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:14px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(245px,1fr)); gap:10px; }}
    .eyebrow {{ color:var(--accent); font-size:11px; font-weight:750; text-transform:uppercase; letter-spacing:.08em; }}
    h1,h2,p {{ margin:0; }} h1 {{ font-size:21px; margin-top:4px; }} h2 {{ font-size:16px; }}
    .muted {{ color:var(--muted); margin-top:5px; }}
    .meta {{ display:grid; gap:7px; margin-top:12px; }}
    .field {{ border-top:1px solid var(--line); padding-top:7px; overflow-wrap:anywhere; }}
    .field span {{ display:block; font-size:11px; color:var(--muted); text-transform:uppercase; }}
    .rule {{ display:inline-block; margin:7px 5px 0 0; border:1px solid var(--line); border-radius:999px; padding:4px 8px; font-size:12px; }}
    @media (prefers-color-scheme:dark) {{ :root {{ --bg:#191a18; --panel:#242522; --ink:#ecebe5; --muted:#afaea6; --line:#3c3d38; --accent:#a7c7bb; }} }}
  </style>
</head>
<body><main>{content}</main></body>
</html>"""


class Tools:
    class Valves(BaseModel):
        observer_url: str = Field(
            default="http://document-runtime-observer:8083",
            description="Internal bounded document runtime observer URL",
        )
        api_key: str = Field(
            default="",
            description="Cockpit read key for the bounded observer",
            json_schema_extra={"input": {"type": "password"}},
        )
        timeout_seconds: float = Field(default=10.0, ge=1.0, le=30.0)

    def __init__(self, client_factory: Callable | None = None):
        self.valves = self.Valves()
        self._client_factory = client_factory or httpx.AsyncClient

    def _base_url(self) -> str:
        value = _safe_url(self.valves.observer_url.rstrip("/"))
        if value is None:
            raise ValueError("Document runtime observer URL must use http or https")
        if not self.valves.api_key:
            raise ValueError("Document runtime observer read key is not configured")
        return value

    def _client(self):
        return self._client_factory(
            timeout=self.valves.timeout_seconds,
            follow_redirects=False,
            headers={"Authorization": f"Bearer {self.valves.api_key}"},
        )

    async def show_document_runtime_live_status(self) -> tuple:
        """Show independent runtime observations without computing a global health verdict."""

        base = self._base_url()
        async with self._client() as client:
            response = await client.get(f"{base}/v1/document-runtime/observations")
            response.raise_for_status()
            payload = response.json()

        observations = payload.get("observations") or []
        by_source = {
            item.get("source"): item
            for item in observations
            if isinstance(item, dict) and item.get("source")
        }
        titles = {
            "paperless_gateway": "Paperless / Gateway",
            "pantheon_pdp": "Pantheon PDP",
            "docling_serve": "Docling Serve",
            "hermes_native_inventory": "Hermes · pantheon-document-intake",
        }
        cards = "".join(
            _card(titles.get(source, source), by_source[source])
            for source in (
                "paperless_gateway",
                "pantheon_pdp",
                "docling_serve",
                "hermes_native_inventory",
            )
            if source in by_source
        )
        rules = payload.get("non_equivalences") or []
        content = (
            "<section class='panel'><div class='eyebrow'>Document Runtime Observations</div>"
            "<h1>État observé, source par source</h1>"
            "<p class='muted'>Aucun score global de santé, de sécurité ou d’activation n’est calculé.</p>"
            + "".join(f"<span class='rule'>{_escape(rule)}</span>" for rule in rules)
            + "</section>"
            + f"<section class='grid'>{cards}</section>"
        )

        context = {
            "object_type": "document_runtime_observation_set",
            "observed_at": payload.get("observed_at"),
            "observations": observations,
            "synthetic_global_health": payload.get("synthetic_global_health", "not_computed"),
            "governance": {
                "authority_effect": payload.get("authority_effect", "none"),
                "write_effect": bool(payload.get("write_effect", False)),
                "activation_changed": bool(payload.get("activation_changed", False)),
            },
        }
        return HTMLResponse(_shell(content)), context
