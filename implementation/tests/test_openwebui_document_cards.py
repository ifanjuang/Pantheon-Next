"""OpenWebUI Rich UI Document Card candidate."""

from __future__ import annotations

import asyncio

from openwebui.pantheon_document_cards import Tools


class _Response:
    def __init__(self, payload=None, text="", status_code=200) -> None:
        self._payload = payload
        self.text = text
        self.status_code = status_code

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    def json(self):
        return self._payload

    def raise_for_status(self) -> None:
        if not self.is_success:
            raise RuntimeError(f"HTTP {self.status_code}")


class _Client:
    def __init__(self, routes: dict, observed: list, **kwargs) -> None:
        self.routes = routes
        self.observed = observed
        self.kwargs = kwargs

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return False

    async def get(self, url: str) -> _Response:
        self.observed.append(url)
        return self.routes[url]


def test_rich_document_card_escapes_content_and_returns_display_context() -> None:
    base = "http://cockpit-api:8081"
    document_id = "doc-safe"
    card = {
        "document_id": document_id,
        "parent_project_id": "project-a",
        "title": "<script>alert(1)</script>.pdf",
        "media_type": "application/pdf",
        "analysis_status": "ready",
        "subject_tags": ["structure", "budget<script>"],
        "naming": {
            "phase_folder": "30_DCE",
            "revision_index": "A1",
            "distributor": "IFJ",
            "document_type": "CCTP",
            "object_name": "LOT-06",
            "document_date": "2026-07-20",
            "project_code": "MAISON-A",
        },
        "extraction": {"converter": "docling_serve"},
        "structured_extraction": {
            "status": "needs_review",
            "page_count": 12,
            "table_count": 3,
            "anomaly_count": 1,
        },
        "chunk_summary": {
            "total": 32,
            "indexed": 32,
            "with_quality_flags": 3,
            "verification_status": "not_observed",
        },
        "authority": {"is_source": False, "is_evidence": False, "is_memory": False},
    }
    routes = {
        f"{base}/v1/documents/{document_id}": _Response(card),
        f"{base}/v1/documents/{document_id}/markdown": _Response(
            text="# CCTP\n\n<img src=x onerror=alert(1)>"
        ),
        f"{base}/v1/documents/{document_id}/preview-link": _Response(
            {"url": "https://pantheon.test/preview.pdf", "expires_at": 1234}
        ),
    }
    observed = []
    tools = Tools(client_factory=lambda **kwargs: _Client(routes, observed, **kwargs))
    tools.valves.api_url = base
    tools.valves.api_key = "secret"

    response, context = asyncio.run(tools.show_document_card(document_id))
    rendered = response.body.decode("utf-8")
    assert "<script>alert(1)</script>" not in rendered
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in rendered
    assert "&lt;img src=x onerror=alert(1)&gt;" in rendered
    assert "https://pantheon.test/preview.pdf" in rendered
    assert "Pages extraites" in rendered
    assert "Tableaux" in rendered
    assert "needs_review" in rendered
    assert "Chunks indexés" in rendered
    assert "not_observed" in rendered
    assert "#structure" in rendered
    assert "#budget&lt;script&gt;" in rendered
    assert context["authority"] == "display_only"
    assert context["document_id"] == document_id
    assert context["structured_anomaly_count"] == 1
    assert context["chunk_count"] == 32
    assert context["indexed_chunk_count"] == 32
    assert context["chunk_verification_status"] == "not_observed"
    assert context["subject_tags"] == ["structure", "budget<script>"]
    assert len(observed) == 3
    assert response.headers["content-disposition"] == "inline"
