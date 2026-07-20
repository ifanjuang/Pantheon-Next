"""
title: Pantheon Document Cards
author: IFJ Architecture
version: 0.1.0
description: Read-only project Document Cards backed by the Pantheon MVP cockpit API.
requirements: httpx>=0.27
"""

from __future__ import annotations

import html
from typing import Callable
from urllib.parse import quote, urlparse

import httpx
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field


def _escape(value) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def _safe_web_url(value: str | None) -> str | None:
    if not value:
        return None
    parsed = urlparse(value)
    return value if parsed.scheme in {"http", "https"} and parsed.netloc else None


def _document_label(card: dict) -> str:
    naming = card.get("naming") or {}
    return naming.get("object_name") or card.get("title") or card.get("document_id", "Document")


def _shell(content: str, title: str = "Documents") -> str:
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy"
        content="default-src 'none'; style-src 'unsafe-inline'; img-src http: https: data:;
                 frame-src http: https:; base-uri 'none'; form-action 'none'">
  <title>{_escape(title)}</title>
  <style>
    :root {{ color-scheme: light dark; --bg:#f4f2ed; --panel:#fffefb; --ink:#252521;
      --muted:#6d6c65; --line:#dedbd2; --accent:#314f45; --warn:#9a6125; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; padding:18px; background:var(--bg); color:var(--ink);
      font:14px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,
      "Segoe UI",sans-serif; }}
    .stack {{ display:grid; gap:12px; max-width:1080px; margin:auto; }}
    .panel {{ background:var(--panel); border:1px solid var(--line); border-radius:16px;
      padding:16px; box-shadow:0 8px 24px rgb(37 37 33 / 7%); }}
    .eyebrow {{ color:var(--accent); font-size:11px; font-weight:750; letter-spacing:.1em;
      text-transform:uppercase; }}
    h1,h2,p {{ margin:0; }} h1 {{ font-size:21px; margin-top:4px; }} h2 {{ font-size:16px; }}
    .muted {{ color:var(--muted); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:10px; }}
    .card {{ border:1px solid var(--line); border-radius:12px; padding:13px;
      background:var(--panel); }}
    .meta {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(145px,1fr)); gap:8px;
      margin-top:14px; }}
    .field {{ border-top:1px solid var(--line); padding-top:7px; }}
    .field span {{ display:block; color:var(--muted); font-size:11px; text-transform:uppercase;
      letter-spacing:.06em; }}
    .badge {{ display:inline-block; border:1px solid var(--line); border-radius:999px;
      padding:3px 8px; margin:7px 5px 0 0; color:var(--muted); font-size:12px; }}
    .ok {{ color:var(--accent); border-color:#9bb2aa; }} .warn {{ color:var(--warn); }}
    iframe,.preview-image {{ width:100%; min-height:520px; border:1px solid var(--line);
      border-radius:12px; background:white; }}
    .preview-image {{ object-fit:contain; }}
    pre {{ margin:0; white-space:pre-wrap; overflow-wrap:anywhere; font:13px/1.5 ui-monospace,
      SFMono-Regular,Consolas,monospace; max-height:420px; overflow:auto; }}
    a {{ color:var(--accent); }}
    @media (prefers-color-scheme:dark) {{ :root {{ --bg:#191a18; --panel:#242522; --ink:#ecebe5;
      --muted:#afaea6; --line:#3c3d38; --accent:#a7c7bb; --warn:#e0ad73; }} }}
    @media (max-width:640px) {{ body {{ padding:10px; }} .panel {{ padding:13px; }}
      iframe,.preview-image {{ min-height:390px; }} }}
  </style>
</head>
<body><main class="stack">{content}</main></body>
</html>"""


class Tools:
    class Valves(BaseModel):
        api_url: str = Field(
            default="http://127.0.0.1:8081",
            description="Internal Pantheon Document Card API base URL",
        )
        api_key: str = Field(
            default="",
            description="Bearer key for the read-only cockpit API",
            json_schema_extra={"input": {"type": "password"}},
        )
        timeout_seconds: float = Field(default=15.0, ge=1.0, le=60.0)
        markdown_preview_chars: int = Field(default=12000, ge=1000, le=50000)

    def __init__(self, client_factory: Callable | None = None):
        self.valves = self.Valves()
        self._client_factory = client_factory or httpx.AsyncClient

    def _base_url(self) -> str:
        value = _safe_web_url(self.valves.api_url.rstrip("/"))
        if value is None:
            raise ValueError("Pantheon API URL must use http or https")
        if not self.valves.api_key:
            raise ValueError("Pantheon cockpit API key is not configured")
        return value

    def _client(self):
        return self._client_factory(
            timeout=self.valves.timeout_seconds,
            follow_redirects=False,
            headers={"Authorization": f"Bearer {self.valves.api_key}"},
        )

    async def list_project_documents(self, parent_project_id: str) -> tuple:
        """Display all indexed Document Cards attached to one exact parent project ID."""
        base = self._base_url()
        async with self._client() as client:
            response = await client.get(
                f"{base}/v1/projects/{quote(parent_project_id, safe='')}/documents"
            )
            response.raise_for_status()
            payload = response.json()
        cards = payload.get("documents") or []
        items = []
        for card in cards:
            naming = card.get("naming") or {}
            status = card.get("analysis_status", "unknown")
            css = "ok" if status == "ready" else "warn"
            items.append(
                "<article class='card'>"
                f"<div class='eyebrow'>{_escape(naming.get('phase_folder') or 'Document')}</div>"
                f"<h2>{_escape(_document_label(card))}</h2>"
                f"<p class='muted'>{_escape(card.get('title'))}</p>"
                f"<span class='badge {css}'>{_escape(status)}</span>"
                f"<span class='badge'>{_escape(naming.get('document_type'))}</span>"
                f"<span class='badge'>{_escape(naming.get('revision_index'))}</span>"
                f"<p class='muted'>ID : {_escape(card.get('document_id'))}</p>"
                "</article>"
            )
        items_html = "".join(items) or '<p class="muted">Aucun document.</p>'
        content = (
            "<section class='panel'>"
            "<div class='eyebrow'>Projet</div>"
            f"<h1>{_escape(parent_project_id)}</h1>"
            f"<p class='muted'>{len(cards)} document(s) indexé(s)</p>"
            "</section>"
            "<section class='grid'>"
            f"{items_html}"
            "</section>"
        )
        context = {
            "parent_project_id": parent_project_id,
            "document_count": len(cards),
            "document_ids": [card.get("document_id") for card in cards],
            "authority": "display_only",
        }
        response = HTMLResponse(
            _shell(content, parent_project_id),
            headers={"Content-Disposition": "inline"},
        )
        return response, context

    async def show_document_card(self, document_id: str) -> tuple:
        """Display one Document Card, its derived Markdown and a short-lived original preview."""
        base = self._base_url()
        encoded_id = quote(document_id, safe="")
        async with self._client() as client:
            card_response = await client.get(f"{base}/v1/documents/{encoded_id}")
            card_response.raise_for_status()
            card = card_response.json()
            markdown_response = await client.get(f"{base}/v1/documents/{encoded_id}/markdown")
            markdown = markdown_response.text if markdown_response.is_success else ""
            preview_response = await client.get(
                f"{base}/v1/documents/{encoded_id}/preview-link"
            )
            preview_payload = preview_response.json() if preview_response.is_success else {}

        naming = card.get("naming") or {}
        extraction = card.get("extraction") or {}
        authority = card.get("authority") or {}
        status = card.get("analysis_status", "unknown")
        status_css = "ok" if status == "ready" else "warn"
        fields = [
            ("Projet", naming.get("project_code")),
            ("Phase", naming.get("phase_folder")),
            ("Indice", naming.get("revision_index")),
            ("Distributeur", naming.get("distributor")),
            ("Type", naming.get("document_type")),
            ("Objet", naming.get("object_name")),
            ("Date", naming.get("document_date")),
            ("Format", card.get("media_type")),
        ]
        field_html = "".join(
            f"<div class='field'><span>{_escape(label)}</span>{_escape(value or '—')}</div>"
            for label, value in fields
        )
        preview_url = _safe_web_url(preview_payload.get("url"))
        media_type = card.get("media_type") or ""
        if preview_url and media_type == "application/pdf":
            original_html = (
                f"<iframe src='{_escape(preview_url)}' "
                "title='Aperçu du document original'></iframe>"
            )
        elif preview_url and media_type.startswith("image/"):
            original_html = (
                f"<img class='preview-image' src='{_escape(preview_url)}' "
                "alt='Aperçu du document original'>"
            )
        elif preview_url:
            original_html = (
                f"<p><a href='{_escape(preview_url)}' target='_blank' rel='noreferrer'>"
                "Ouvrir temporairement l’original</a></p>"
            )
        else:
            original_html = "<p class='muted'>Aperçu original indisponible.</p>"

        clipped_markdown = markdown[: self.valves.markdown_preview_chars]
        if len(markdown) > len(clipped_markdown):
            clipped_markdown += "\n\n[… aperçu tronqué …]"
        content = (
            "<section class='panel'>"
            f"<div class='eyebrow'>{_escape(naming.get('phase_folder') or 'Document')}</div>"
            f"<h1>{_escape(_document_label(card))}</h1>"
            f"<p class='muted'>{_escape(card.get('title'))}</p>"
            f"<span class='badge {status_css}'>{_escape(status)}</span>"
            "<span class='badge'>Docling : "
            f"{_escape(extraction.get('converter') or 'direct')}</span>"
            f"<div class='meta'>{field_html}</div>"
            "</section>"
            "<section class='panel'><div class='eyebrow'>Original NAS · lien signé 5 min</div>"
            f"{original_html}</section>"
            "<section class='panel'><div class='eyebrow'>Markdown dérivé</div>"
            f"<pre>{_escape(clipped_markdown or 'Aucun contenu Markdown disponible.')}</pre>"
            "</section>"
            "<section class='panel'><div class='eyebrow'>Limites d’autorité</div>"
            "<p>Cette carte expose le document. Elle ne valide ni la vérité professionnelle, "
            "ni la preuve, ni la mémoire.</p>"
            f"<span class='badge'>source : {_escape(authority.get('is_source', False))}</span>"
            f"<span class='badge'>preuve : {_escape(authority.get('is_evidence', False))}</span>"
            f"<span class='badge'>mémoire : {_escape(authority.get('is_memory', False))}</span>"
            "</section>"
        )
        context = {
            "document_id": card.get("document_id"),
            "parent_project_id": card.get("parent_project_id"),
            "analysis_status": status,
            "phase": naming.get("phase_code"),
            "document_type": naming.get("document_type"),
            "authority": "display_only",
            "original_preview_expires": preview_payload.get("expires_at"),
        }
        return HTMLResponse(
            _shell(content, _document_label(card)),
            headers={"Content-Disposition": "inline"},
        ), context
