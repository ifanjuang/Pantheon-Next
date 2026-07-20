"""Read-only cockpit API and signed original preview boundaries."""

from __future__ import annotations

import time

from fastapi.testclient import TestClient

from mvp_vertical import knowledge, store
from mvp_vertical.cockpit_api import create_app


DOCUMENT_ID = "doc-0123456789abcdef01234567"
SOURCE_REF = (
    "Projects/MAISON-A/30_DCE/"
    "MAISON-A_A1_DCE_IFJ_CCTP_LOT-06_2026-07-20.pdf"
)


class _Connection:
    def close(self) -> None:
        pass


def _card() -> dict:
    return {
        "card_type": "project_document",
        "card_id": f"card-{DOCUMENT_ID}",
        "document_id": DOCUMENT_ID,
        "parent_project_id": "project-maison-a",
        "title": SOURCE_REF.rsplit("/", 1)[-1],
        "source_ref": SOURCE_REF,
        "media_type": "application/pdf",
        "analysis_status": "ready",
        "naming": {"phase_folder": "30_DCE", "document_type": "CCTP"},
        "extraction": {"converter": "docling_serve"},
        "authority": {"is_source": False, "is_evidence": False, "is_memory": False},
    }


def test_cockpit_api_requires_bearer_key_and_serves_bounded_preview(
    monkeypatch, tmp_path
) -> None:
    original = tmp_path / SOURCE_REF
    original.parent.mkdir(parents=True)
    original.write_bytes(b"fictional-pdf")
    monkeypatch.setattr(store, "list_document_cards", lambda _conn, _project: [_card()])
    monkeypatch.setattr(store, "get_document_card_by_id", lambda _conn, _id: _card())
    monkeypatch.setattr(
        store, "get_document_markdown", lambda _conn, _id: "# CCTP\n\nLot 06"
    )
    monkeypatch.setattr(
        store, "get_document_source", lambda _conn, _id: ("dossier-a", SOURCE_REF)
    )
    app = create_app(
        connect_fn=_Connection,
        document_root=tmp_path,
        api_key="test-secret",
        public_url="https://pantheon.test",
    )
    client = TestClient(app)

    assert client.get("/health").json()["mode"] == "read_only"
    assert client.get("/v1/projects/project-maison-a/documents").status_code == 401
    headers = {"Authorization": "Bearer test-secret"}
    listed = client.get(
        "/v1/projects/project-maison-a/documents", headers=headers
    ).json()
    assert listed["documents"][0]["document_id"] == DOCUMENT_ID
    markdown = client.get(f"/v1/documents/{DOCUMENT_ID}/markdown", headers=headers)
    assert markdown.headers["x-pantheon-derived"] == "true"
    assert markdown.text.startswith("# CCTP")

    link = client.get(
        f"/v1/documents/{DOCUMENT_ID}/preview-link", headers=headers
    ).json()
    assert link["url"].startswith(
        f"https://pantheon.test/v1/previews/{DOCUMENT_ID}/original?"
    )
    path_and_query = link["url"].removeprefix("https://pantheon.test")
    preview = client.get(path_and_query)
    assert preview.status_code == 200
    assert preview.content == b"fictional-pdf"
    assert preview.headers["cache-control"] == "private, no-store, max-age=0"
    assert "inline" in preview.headers["content-disposition"]

    tampered = path_and_query.replace("signature=", "signature=bad")
    assert client.get(tampered).status_code == 401


def test_preview_link_rejects_expired_timestamp(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(
        store, "get_document_source", lambda _conn, _id: ("dossier-a", SOURCE_REF)
    )
    app = create_app(connect_fn=_Connection, document_root=tmp_path, api_key="secret")
    client = TestClient(app)
    response = client.get(
        f"/v1/previews/{DOCUMENT_ID}/original",
        params={"expires": int(time.time()) - 1, "signature": "invalid"},
    )
    assert response.status_code == 401


def test_knowledge_reads_accept_editor_key_and_writes_require_it(monkeypatch) -> None:
    knowledge_card = {
        "card_type": "knowledge",
        "knowledge_id": "knowledge.techniques.facades",
        "title": "Reprise des façades",
        "family": "techniques",
        "review_status": "generated_unreviewed",
        "version": 1,
        "authority": {"is_evidence": False, "is_memory": False, "is_doctrine": False},
    }
    monkeypatch.setattr(knowledge, "list_knowledge_cards", lambda _conn, _project: [knowledge_card])
    monkeypatch.setattr(knowledge, "get_knowledge_card", lambda _conn, _id: knowledge_card)
    monkeypatch.setattr(knowledge, "get_knowledge_markdown", lambda _conn, _id: "# Façades")
    observed = {}

    def publish(_conn, **values):
        observed.update(values)
        return knowledge_card

    monkeypatch.setattr(knowledge, "publish_knowledge", publish)
    monkeypatch.setattr(
        knowledge,
        "list_edit_requests",
        lambda _conn, **_values: [{"request_id": "edit-1", "status": "queued_for_hermes"}],
    )
    app = create_app(
        connect_fn=_Connection,
        api_key="read-key",
        editor_api_key="edit-key",
        hermes_api_key="hermes-key",
    )
    client = TestClient(app)
    edit_headers = {"Authorization": "Bearer edit-key"}

    health = client.get("/health").json()
    assert health["editor_mode"] == "bounded_read_write"
    assert health["hermes_edit_binding"] == "polling_ready"
    listed = client.get("/v1/projects/project-maison-a/knowledge", headers=edit_headers)
    assert listed.json()["knowledge"][0]["review_status"] == "generated_unreviewed"
    markdown = client.get("/v1/knowledge/knowledge.techniques.facades/markdown", headers=edit_headers)
    assert markdown.headers["x-pantheon-knowledge"] == "generated"

    body = {
        "knowledge_id": "knowledge.techniques.facades",
        "title": "Reprise des façades",
        "family": "techniques",
        "markdown": "# Façades",
        "source_chunk_refs": ["chunk.doc.0000"],
        "created_by": "mobile-user",
        "idempotency_key": "publish-mobile-1",
    }
    assert client.post(f"/v1/documents/{DOCUMENT_ID}/knowledge", json=body).status_code == 401
    response = client.post(
        f"/v1/documents/{DOCUMENT_ID}/knowledge", json=body, headers=edit_headers
    )
    assert response.status_code == 201
    assert observed["document_id"] == DOCUMENT_ID
    assert observed["review_status"] == "generated_unreviewed"
    assert client.get("/v1/edit-requests", headers=edit_headers).status_code == 401
    hermes_queue = client.get(
        "/v1/edit-requests", headers={"Authorization": "Bearer hermes-key"}
    )
    assert hermes_queue.json()["edit_requests"][0]["status"] == "queued_for_hermes"


def test_mobile_editor_shell_is_available() -> None:
    client = TestClient(create_app(connect_fn=_Connection, api_key="read-key"))
    response = client.get("/editor/")
    assert response.status_code == 200
    assert "Pantheon Knowledge" in response.text
    assert client.get("/editor/manifest.webmanifest").status_code == 200
