"""
title: Pantheon Paperless Source Inbox
author: IFJ Architecture
version: 0.1.0
description: Read-only Paperless document-source inbox through the bounded Pantheon gateway.
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


def _safe_url(value: str | None) -> str | None:
    if not value:
        return None
    parsed = urlparse(value)
    return value if parsed.scheme in {"http", "https"} and parsed.netloc else None


def _shell(content: str, title: str) -> str:
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy"
        content="default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
  <title>{_escape(title)}</title>
  <style>
    :root {{ color-scheme: light dark; --bg:#f4f2ed; --panel:#fffefb; --ink:#252521;
      --muted:#6d6c65; --line:#dedbd2; --accent:#314f45; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; padding:18px; background:var(--bg); color:var(--ink);
      font:14px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
    main {{ display:grid; gap:12px; max-width:1080px; margin:auto; }}
    .panel,.card {{ background:var(--panel); border:1px solid var(--line); border-radius:14px; padding:14px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:10px; }}
    .eyebrow {{ color:var(--accent); font-size:11px; font-weight:750; text-transform:uppercase; letter-spacing:.08em; }}
    h1,h2,p {{ margin:0; }} h1 {{ font-size:21px; margin-top:4px; }} h2 {{ font-size:16px; }}
    .muted {{ color:var(--muted); }}
    .badge {{ display:inline-block; border:1px solid var(--line); border-radius:999px; padding:3px 8px; margin:7px 5px 0 0; font-size:12px; color:var(--muted); }}
    .meta {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:8px; margin-top:12px; }}
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
            description="Internal Pantheon Paperless gateway URL",
        )
        api_key: str = Field(
            default="",
            description="Bearer key for the read-only Paperless gateway",
            json_schema_extra={"input": {"type": "password"}},
        )
        timeout_seconds: float = Field(default=20.0, ge=1.0, le=60.0)

    def __init__(self, client_factory: Callable | None = None):
        self.valves = self.Valves()
        self._client_factory = client_factory or httpx.AsyncClient

    def _base_url(self) -> str:
        value = _safe_url(self.valves.gateway_url.rstrip("/"))
        if value is None:
            raise ValueError("Paperless gateway URL must use http or https")
        if not self.valves.api_key:
            raise ValueError("Paperless gateway API key is not configured")
        return value

    def _client(self):
        return self._client_factory(
            timeout=self.valves.timeout_seconds,
            follow_redirects=False,
            headers={"Authorization": f"Bearer {self.valves.api_key}"},
        )

    async def search_document_sources(self, query: str = "", page_size: int = 20) -> tuple:
        """Search the Paperless source inbox without classifying or mutating documents."""

        base = self._base_url()
        params = {"page_size": max(1, min(page_size, 100))}
        if query.strip():
            params["query"] = query.strip()
        async with self._client() as client:
            response = await client.get(f"{base}/v1/paperless/documents", params=params)
            response.raise_for_status()
            payload = response.json()

        documents = payload.get("documents") or []
        cards = []
        for document in documents:
            search_hit = document.get("search_hit") or {}
            cards.append(
                "<article class='card'>"
                "<div class='eyebrow'>Source Paperless</div>"
                f"<h2>{_escape(document.get('title') or 'Document')}</h2>"
                f"<p class='muted'>ID Paperless : {_escape(document.get('id'))}</p>"
                f"<span class='badge'>type : {_escape(document.get('document_type') or '—')}</span>"
                f"<span class='badge'>tags : {_escape(document.get('tags') or [])}</span>"
                + (
                    f"<p class='muted'>Résultat #{_escape(search_hit.get('rank'))} · score {_escape(search_hit.get('score'))}</p>"
                    if search_hit
                    else ""
                )
                + "</article>"
            )
        empty_html = '<p class="muted">Aucune source.</p>'
        cards_html = "".join(cards) or empty_html
        content = (
            "<section class='panel'><div class='eyebrow'>Paperless · Source Inbox</div>"
            f"<h1>{_escape(query or 'Tous les documents')}</h1>"
            f"<p class='muted'>{_escape(payload.get('count', len(documents)))} source(s). "
            "Lecture uniquement : aucun classement n’est appliqué ici.</p></section>"
            f"<section class='grid'>{cards_html}</section>"
        )
        context = {
            "source_runtime": "paperless_ngx",
            "query": query,
            "document_ids": [item.get("id") for item in documents],
            "authority": "source_display_only",
        }
        return HTMLResponse(_shell(content, "Paperless Source Inbox")), context

    async def inspect_document_source(self, document_id: int) -> tuple:
        """Inspect Paperless operational metadata without treating it as project truth."""

        base = self._base_url()
        async with self._client() as client:
            response = await client.get(
                f"{base}/v1/paperless/documents/{quote(str(document_id), safe='')}"
            )
            response.raise_for_status()
            document = response.json()

        fields = [
            ("Paperless ID", document.get("id")),
            ("Titre", document.get("title")),
            ("Créé", document.get("created")),
            ("Ajouté", document.get("added")),
            ("Correspondant", document.get("correspondent")),
            ("Type", document.get("document_type")),
            ("Storage path", document.get("storage_path")),
            ("Tags", document.get("tags")),
            ("Champs", document.get("custom_fields")),
        ]
        meta = "".join(
            f"<div class='field'><span>{_escape(label)}</span>{_escape(value or '—')}</div>"
            for label, value in fields
        )
        content = (
            "<section class='panel'><div class='eyebrow'>Source Paperless</div>"
            f"<h1>{_escape(document.get('title') or f'Document {document_id}')}</h1>"
            f"<div class='meta'>{meta}</div></section>"
            "<section class='panel'><div class='eyebrow'>Autorité</div>"
            "<p>Ces métadonnées sont opérationnelles. Elles ne constituent ni la classification métier canonique, ni Knowledge, ni Evidence.</p></section>"
        )
        return HTMLResponse(_shell(content, str(document.get("title") or document_id))), {
            "paperless_document_id": document_id,
            "source_runtime": "paperless_ngx",
            "authority": "operational_metadata_only",
        }

    async def inspect_exact_source_capture(self, document_id: int, version_id: str) -> tuple:
        """Inspect the immutable identity candidate for one exact Paperless version."""

        base = self._base_url()
        async with self._client() as client:
            response = await client.get(
                f"{base}/v1/paperless/documents/{quote(str(document_id), safe='')}/capture",
                params={"version_id": version_id},
            )
            response.raise_for_status()
            capture = response.json()
        fields = [
            ("Document", capture.get("document_id")),
            ("Version", capture.get("version_id")),
            ("Original", capture.get("original_filename")),
            ("MIME", capture.get("media_type")),
            ("Octets", capture.get("byte_size")),
            ("SHA-256", capture.get("content_hash")),
            ("Storage reference", capture.get("storage_reference")),
            ("Source ref", capture.get("source_ref")),
        ]
        meta = "".join(
            f"<div class='field'><span>{_escape(label)}</span>{_escape(value or '—')}</div>"
            for label, value in fields
        )
        content = (
            "<section class='panel'><div class='eyebrow'>Source Capture candidate</div>"
            f"<h1>{_escape(capture.get('original_filename'))}</h1><div class='meta'>{meta}</div></section>"
            "<section class='panel'><p>Version exacte et digest observés. Cette capture n’est pas automatiquement Evidence ou Knowledge.</p></section>"
        )
        return HTMLResponse(_shell(content, "Source Capture")), {
            "document_id": document_id,
            "version_id": version_id,
            "content_hash": capture.get("content_hash"),
            "storage_reference": capture.get("storage_reference"),
            "authority": "source_capture_candidate",
        }
