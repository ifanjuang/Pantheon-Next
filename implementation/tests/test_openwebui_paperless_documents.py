from __future__ import annotations

import asyncio

from openwebui.pantheon_paperless_documents import Tools


class _Response:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload

    def raise_for_status(self):
        if not 200 <= self.status_code < 300:
            raise RuntimeError(f"HTTP {self.status_code}")


class _Client:
    def __init__(self, routes, observed, **kwargs):
        self.routes = routes
        self.observed = observed
        self.kwargs = kwargs

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return False

    async def get(self, url, params=None):
        self.observed.append((url, params))
        key = (url, tuple(sorted((params or {}).items())))
        return self.routes[key]


def test_source_inbox_is_read_only_and_escapes_titles():
    base = "http://paperless-gateway:8082"
    routes = {
        (
            f"{base}/v1/paperless/documents",
            (("page_size", 20), ("query", "CCTP")),
        ): _Response(
            {
                "count": 1,
                "documents": [
                    {
                        "id": 42,
                        "title": "<script>CCTP</script>",
                        "tags": [3],
                        "document_type": 7,
                        "authority": {"business_classification": False},
                    }
                ],
            }
        )
    }
    observed = []
    tools = Tools(client_factory=lambda **kwargs: _Client(routes, observed, **kwargs))
    tools.valves.gateway_url = base
    tools.valves.api_key = "read-key"

    response, context = asyncio.run(tools.search_document_sources("CCTP"))
    rendered = response.body.decode("utf-8")
    assert "<script>CCTP</script>" not in rendered
    assert "&lt;script&gt;CCTP&lt;/script&gt;" in rendered
    assert context["authority"] == "source_display_only"
    assert context["document_ids"] == [42]
    assert observed == [(f"{base}/v1/paperless/documents", {"page_size": 20, "query": "CCTP"})]


def test_exact_capture_surface_keeps_source_evidence_boundary():
    base = "http://paperless-gateway:8082"
    routes = {
        (
            f"{base}/v1/paperless/documents/42/capture",
            (("version_id", "7"),),
        ): _Response(
            {
                "document_id": 42,
                "version_id": "7",
                "original_filename": "cctp.pdf",
                "media_type": "application/pdf",
                "byte_size": 100,
                "content_hash": "sha256:abc",
                "storage_reference": "paperless://document/42/version/7",
                "source_ref": "paperless/42/versions/7/cctp.pdf",
            }
        )
    }
    observed = []
    tools = Tools(client_factory=lambda **kwargs: _Client(routes, observed, **kwargs))
    tools.valves.gateway_url = base
    tools.valves.api_key = "read-key"

    response, context = asyncio.run(tools.inspect_exact_source_capture(42, "7"))
    rendered = response.body.decode("utf-8")
    assert "sha256:abc" in rendered
    assert "pas automatiquement Evidence ou Knowledge" in rendered
    assert context["authority"] == "source_capture_candidate"
    assert context["storage_reference"] == "paperless://document/42/version/7"
