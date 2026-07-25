from __future__ import annotations

import hashlib
import json

import httpx
import pytest

from mvp_vertical.paperless import (
    PaperlessClient,
    PaperlessConfigurationError,
    PaperlessMutationError,
    governed_post_document,
    governed_update_document_metadata,
    paperless_source_ref,
)
from mvp_vertical.policy_gate import StandInPolicyClient


def _decision_payload(decided_by: str = "marie.dupont") -> dict:
    scope = {"scope_type": "project", "scope_id": "P-42"}
    return {
        "decision": {"decision_id": "d1", "decided_by": decided_by, "scope": scope},
        "expectation": {"required_scope": scope},
    }


def _client(handler):
    transport = httpx.MockTransport(handler)
    return httpx.Client(transport=transport)


def test_configuration_requires_http_url_and_token():
    with pytest.raises(PaperlessConfigurationError):
        PaperlessClient("file:///tmp/paperless", "token")
    with pytest.raises(PaperlessConfigurationError):
        PaperlessClient("http://paperless:8000", "")


def test_list_documents_uses_token_auth_and_query():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["authorization"] = request.headers.get("authorization")
        seen["query"] = request.url.params.get("query")
        return httpx.Response(200, json={"count": 1, "results": [{"id": 17, "title": "CCTP"}]})

    client = PaperlessClient(
        "http://paperless:8000", "secret-token", client=_client(handler)
    )
    payload = client.list_documents(query="charpente")
    assert payload["count"] == 1
    assert seen == {"authorization": "Token secret-token", "query": "charpente"}


def test_exact_capture_preserves_version_hash_and_safe_source_ref():
    content = b"%PDF-1.7\nfictional"

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/documents/42/download/"
        assert request.url.params["version"] == "7"
        return httpx.Response(
            200,
            content=content,
            headers={
                "content-type": "application/pdf",
                "content-disposition": 'attachment; filename="Lieurey DCE CCTP.pdf"',
            },
        )

    client = PaperlessClient("http://paperless:8000", "token", client=_client(handler))
    capture = client.capture_document(42, version_id="7")
    assert capture.document_id == 42
    assert capture.version_id == "7"
    assert capture.original_filename == "Lieurey DCE CCTP.pdf"
    assert capture.content_hash == "sha256:" + hashlib.sha256(content).hexdigest()
    assert capture.storage_reference == "paperless://document/42/version/7"
    assert capture.source_ref == "paperless/42/versions/7/Lieurey-DCE-CCTP.pdf"
    with capture.materialized() as path:
        assert path.read_bytes() == content
        materialized = path
    assert not materialized.exists()


def test_capture_ref_requires_an_exact_version():
    with pytest.raises(ValueError):
        paperless_source_ref(12, "", "document.pdf")
    client = PaperlessClient("http://paperless:8000", "token", client=_client(lambda req: None))
    with pytest.raises(PaperlessConfigurationError):
        client.download_document(12, version_id="")


def test_upload_returns_consumption_task_uuid():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["path"] = request.url.path
        seen["authorization"] = request.headers.get("authorization")
        seen["content_type"] = request.headers.get("content-type", "")
        return httpx.Response(200, json="task-uuid-123")

    client = PaperlessClient("http://paperless:8000", "token", client=_client(handler))
    task_id = client.post_document(
        filename="document.pdf",
        content=b"pdf",
        media_type="application/pdf",
        title="Document",
        tags=[2, 9],
        custom_fields={11: "Lieurey"},
    )
    assert task_id == "task-uuid-123"
    assert seen["path"] == "/api/documents/post_document/"
    assert seen["authorization"] == "Token token"
    assert "multipart/form-data" in seen["content_type"]


def test_task_endpoint_normalizes_paginated_result():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["task_id"] == "abc"
        return httpx.Response(
            200,
            json={"count": 1, "results": [{"task_id": "abc", "status": "SUCCESS", "related_document": 77}]},
        )

    client = PaperlessClient("http://paperless:8000", "token", client=_client(handler))
    assert client.get_task("abc")["related_document"] == 77


def test_metadata_mutation_is_allowlisted():
    client = PaperlessClient(
        "http://paperless:8000",
        "token",
        client=_client(lambda request: httpx.Response(200, json={})),
    )
    with pytest.raises(PaperlessMutationError):
        client.update_document_metadata(1, {"content": "pretend truth"})
    with pytest.raises(PaperlessMutationError):
        client.update_document_metadata(1, {})


def test_governed_metadata_update_blocks_before_external_request():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json={"id": 42})

    paperless = PaperlessClient("http://paperless:8000", "token", client=_client(handler))
    result = governed_update_document_metadata(
        StandInPolicyClient(disposition="blocked_pending_human_decision"),
        paperless,
        document_id=42,
        changes={"tags": [3]},
        decision_payload=_decision_payload(),
    )
    assert result["status"] == "blocked"
    assert result["effect_ran"] is False
    assert calls == []


def test_governed_metadata_update_applies_only_after_valid_human_decision():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["method"] = request.method
        seen["path"] = request.url.path
        seen["json"] = json.loads(request.content.decode("utf-8"))
        return httpx.Response(200, json={"id": 42, "tags": [3, 8]})

    paperless = PaperlessClient("http://paperless:8000", "token", client=_client(handler))
    result = governed_update_document_metadata(
        StandInPolicyClient(),
        paperless,
        document_id=42,
        changes={"tags": [3, 8], "custom_fields": [{"field": 11, "value": "DCE"}]},
        decision_payload=_decision_payload(),
        candidate={"classification_status": "candidate_reviewed"},
    )
    assert result["status"] == "applied"
    assert result["effect_ran"] is True
    assert seen == {
        "method": "PATCH",
        "path": "/api/documents/42/",
        "json": {"tags": [3, 8], "custom_fields": [{"field": 11, "value": "DCE"}]},
    }


def test_governed_upload_fails_closed_for_non_human_decision():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json="should-not-run")

    paperless = PaperlessClient("http://paperless:8000", "token", client=_client(handler))
    result = governed_post_document(
        StandInPolicyClient(),
        paperless,
        filename="source.pdf",
        content=b"pdf",
        media_type="application/pdf",
        decision_payload=_decision_payload(decided_by="hermes"),
    )
    assert result["status"] == "blocked"
    assert result["effect_ran"] is False
    assert calls == []
