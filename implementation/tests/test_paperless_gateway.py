from __future__ import annotations

from fastapi.testclient import TestClient

from mvp_vertical.paperless import PaperlessSourceCapture
from mvp_vertical.paperless_gateway import create_app
from mvp_vertical.policy_gate import StandInPolicyClient


class _FakePaperless:
    def __init__(self) -> None:
        self.updates = []

    def probe(self):
        return {"reachable": True, "document_count": 2}

    def list_documents(self, *, query=None, page=1, page_size=50):
        return {
            "count": 1,
            "results": [
                {
                    "id": 42,
                    "title": "CCTP charpente",
                    "tags": [3],
                    "content": "derived OCR should not be exposed by the projection",
                    "__search_hit__": {"score": 0.9, "rank": 0, "highlights": "CCTP"},
                }
            ],
        }

    def get_document(self, document_id, *, version_id=None):
        return {
            "id": document_id,
            "title": "CCTP charpente",
            "document_type": 7,
            "content": "not part of the bounded projection",
        }

    def capture_document(self, document_id, *, version_id):
        return PaperlessSourceCapture(
            document_id=document_id,
            version_id=version_id,
            original_filename="cctp.pdf",
            media_type="application/pdf",
            byte_size=3,
            content_hash="sha256:abc",
            storage_reference=f"paperless://document/{document_id}/version/{version_id}",
            source_ref=f"paperless/{document_id}/versions/{version_id}/cctp.pdf",
            content=b"pdf",
        )

    def get_task(self, task_id):
        return {"task_id": task_id, "status": "SUCCESS", "related_document": 42}

    def update_document_metadata(self, document_id, changes):
        self.updates.append((document_id, changes))
        return {"id": document_id, **changes}


def _decision_payload(decided_by="marie.dupont"):
    scope = {"scope_type": "project", "scope_id": "P-42"}
    return {
        "decision": {"decision_id": "d1", "decided_by": decided_by, "scope": scope},
        "expectation": {"required_scope": scope},
    }


def _app(fake, policy=None):
    return create_app(
        paperless_factory=lambda: fake,
        policy_factory=lambda: policy or StandInPolicyClient(),
        read_api_key="read-key",
        hermes_api_key="hermes-key",
    )


def test_health_exposes_reachability_without_document_data():
    client = TestClient(_app(_FakePaperless()))
    assert client.get("/health").json() == {
        "status": "ok",
        "paperless_reachable": True,
        "write_surface": "governed_only",
    }


def test_read_routes_require_bearer_key():
    client = TestClient(_app(_FakePaperless()))
    assert client.get("/v1/paperless/documents").status_code == 401
    ok = client.get(
        "/v1/paperless/documents?query=CCTP",
        headers={"Authorization": "Bearer read-key"},
    )
    assert ok.status_code == 200
    payload = ok.json()
    assert payload["documents"][0]["title"] == "CCTP charpente"
    assert "content" not in payload["documents"][0]
    assert payload["documents"][0]["authority"]["business_classification"] is False


def test_exact_capture_returns_identity_not_bytes():
    client = TestClient(_app(_FakePaperless()))
    response = client.get(
        "/v1/paperless/documents/42/capture?version_id=7",
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["storage_reference"] == "paperless://document/42/version/7"
    assert payload["source_ref"] == "paperless/42/versions/7/cctp.pdf"
    assert "content" not in payload
    assert payload["authority"]["source_capture_candidate"] is True


def test_task_success_is_explicitly_not_evidence():
    client = TestClient(_app(_FakePaperless()))
    response = client.get(
        "/v1/paperless/tasks/task-1",
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 200
    assert response.json()["runtime_success_is_evidence"] is False


def test_metadata_write_requires_hermes_key():
    client = TestClient(_app(_FakePaperless()))
    response = client.post(
        "/v1/paperless/documents/42/metadata",
        json={"changes": {"tags": [3]}, "decision_payload": _decision_payload()},
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 401


def test_metadata_write_is_blocked_before_paperless_when_policy_blocks():
    fake = _FakePaperless()
    client = TestClient(
        _app(fake, StandInPolicyClient(disposition="blocked_pending_human_decision"))
    )
    response = client.post(
        "/v1/paperless/documents/42/metadata",
        json={"changes": {"tags": [3]}, "decision_payload": _decision_payload()},
        headers={"Authorization": "Bearer hermes-key"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "blocked"
    assert fake.updates == []


def test_metadata_write_applies_after_policy_and_human_decision():
    fake = _FakePaperless()
    client = TestClient(_app(fake))
    response = client.post(
        "/v1/paperless/documents/42/metadata",
        json={
            "changes": {"tags": [3, 8]},
            "decision_payload": _decision_payload(),
            "candidate": {"classification_status": "candidate_reviewed"},
        },
        headers={"Authorization": "Bearer hermes-key"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "applied"
    assert fake.updates == [(42, {"tags": [3, 8]})]
