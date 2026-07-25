from __future__ import annotations

import hashlib

import httpx
import pytest
from fastapi.testclient import TestClient

from mvp_vertical.paperless import (
    PaperlessClient,
    PaperlessMutationError,
    governed_post_document,
)
from mvp_vertical.paperless_gateway import _assert_capture_still_current, create_app
from mvp_vertical.policy_gate import StandInPolicyClient


def _decision_payload() -> dict:
    scope = {"scope_type": "project", "scope_id": "P-42"}
    return {
        "decision": {
            "decision_id": "d-review",
            "decided_by": "marie.dupont",
            "scope": scope,
        },
        "expectation": {"required_scope": scope},
    }


def test_external_upload_cannot_downgrade_effect_fact_through_nested_request():
    calls: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return httpx.Response(200, json="must-not-run")

    paperless = PaperlessClient(
        "http://paperless:8000",
        "token",
        client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    result = governed_post_document(
        StandInPolicyClient(external_effect_allowed=False),
        paperless,
        filename="source.pdf",
        content=b"pdf",
        decision_payload=_decision_payload(),
        candidate={
            "effect_kind": "project_document_intake",
            "request": {"external_effect": False, "writes_state": False},
        },
    )

    assert result["status"] == "blocked"
    assert result["disposition"] == "blocked_external_effect_not_authorized"
    assert result["effect_ran"] is False
    assert calls == []


def test_metadata_guard_refuses_when_latest_bytes_differ_from_approved_capture():
    approved = b"%PDF-approved"
    newer = b"%PDF-newer-version"

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/documents/42/download/"
        content = approved if request.url.params.get("version") == "7" else newer
        return httpx.Response(
            200,
            content=content,
            headers={
                "content-type": "application/pdf",
                "content-disposition": 'attachment; filename="cctp.pdf"',
            },
        )

    paperless = PaperlessClient(
        "http://paperless:8000",
        "token",
        client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    capture = paperless.capture_document(42, version_id="7")
    assert capture.content_hash == "sha256:" + hashlib.sha256(approved).hexdigest()

    with pytest.raises(PaperlessMutationError, match="newer/different source version"):
        _assert_capture_still_current(paperless, capture)


def test_metadata_guard_accepts_when_latest_bytes_still_match_exact_capture():
    approved = b"%PDF-approved"

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/api/documents/42/download/"
        return httpx.Response(
            200,
            content=approved,
            headers={
                "content-type": "application/pdf",
                "content-disposition": 'attachment; filename="cctp.pdf"',
            },
        )

    paperless = PaperlessClient(
        "http://paperless:8000",
        "token",
        client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    capture = paperless.capture_document(42, version_id="7")
    _assert_capture_still_current(paperless, capture)


def test_malformed_task_contract_yaml_is_a_422_not_an_internal_error():
    app = create_app(
        paperless_factory=lambda: (_ for _ in ()).throw(AssertionError("must not reach Paperless")),
        policy_factory=lambda: StandInPolicyClient(),
        intake_executor=lambda *_args: (_ for _ in ()).throw(AssertionError("must not run")),
        read_api_key="read-key",
        hermes_api_key="hermes-key",
    )
    response = TestClient(app).post(
        "/v1/paperless/intakes",
        json={
            "paperless_document_id": 42,
            "paperless_version_id": "7",
            "task_contract_yaml": "object_type: task_contract\nscope: [unterminated",
            "decision_payload": {},
        },
        headers={"Authorization": "Bearer hermes-key"},
    )

    assert response.status_code == 422
    assert "cannot parse contract YAML" in response.json()["detail"]
