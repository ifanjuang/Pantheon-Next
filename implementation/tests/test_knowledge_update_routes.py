"""Cockpit API boundaries for the first owner-specific Knowledge UPDATE."""

from __future__ import annotations

from fastapi.testclient import TestClient

from mvp_vertical import knowledge_update
from mvp_vertical.cockpit_shell import create_cockpit_app


class _Connection:
    def close(self) -> None:
        pass


def test_update_preview_requires_editor_key_signing_authority_and_declared_human(monkeypatch) -> None:
    monkeypatch.setattr(
        knowledge_update,
        "preview_knowledge_update",
        lambda _conn, **values: {
            "status": "confirmation_required",
            "actor": values["actor"],
            "signing_secret": values["signing_secret"],
        },
    )
    path = "/v1/projects/project-a/knowledge/knowledge.coverage/updates/preview"
    body = {"proposed_markdown": "# Updated", "expected_version": 2}

    unsigned = TestClient(
        create_cockpit_app(connect_fn=_Connection, editor_api_key="edit-key")
    )
    assert unsigned.post(
        path,
        json=body,
        headers={
            "Authorization": "Bearer edit-key",
            "X-Pantheon-Human-Actor": "ifan.juang",
        },
    ).status_code == 503

    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            api_key="read-key",
            editor_api_key="edit-key",
            update_signing_secret="server-signing-secret",
        )
    )
    assert client.post(path, json=body).status_code == 401
    assert client.post(
        path,
        json=body,
        headers={"Authorization": "Bearer read-key", "X-Pantheon-Human-Actor": "ifan"},
    ).status_code == 401
    assert client.post(
        path,
        json=body,
        headers={"Authorization": "Bearer edit-key"},
    ).status_code == 422
    response = client.post(
        path,
        json=body,
        headers={
            "Authorization": "Bearer edit-key",
            "X-Pantheon-Human-Actor": "ifan.juang",
        },
    )
    assert response.status_code == 200
    assert response.json()["actor"] == "ifan.juang"
    assert response.json()["signing_secret"] == "server-signing-secret"


def test_update_apply_passes_only_exact_confirmed_effect(monkeypatch) -> None:
    observed = {}

    def apply(_conn, **values):
        observed.update(values)
        return {"status": "applied", "knowledge": {"version": 3}}

    monkeypatch.setattr(knowledge_update, "apply_knowledge_update", apply)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="edit-key",
            update_signing_secret="server-signing-secret",
        )
    )
    response = client.post(
        "/v1/projects/project-a/knowledge/knowledge.coverage/updates/apply",
        headers={
            "Authorization": "Bearer edit-key",
            "X-Pantheon-Human-Actor": "ifan.juang",
        },
        json={
            "proposed_markdown": "# Updated",
            "expected_version": 2,
            "review_status": "needs_review",
            "base_markdown_digest": "sha256:base",
            "confirmation_token": "a" * 64,
            "confirmation_expires_at": 2_000_000_000,
            "confirmation_phrase": "CONFIRMER UPDATE",
            "idempotency_key": "knowledge-update-0001",
        },
    )

    assert response.status_code == 200
    assert response.json()["status"] == "applied"
    assert observed == {
        "parent_project_id": "project-a",
        "knowledge_id": "knowledge.coverage",
        "actor": "ifan.juang",
        "signing_secret": "server-signing-secret",
        "proposed_markdown": "# Updated",
        "expected_version": 2,
        "review_status": "needs_review",
        "base_markdown_digest": "sha256:base",
        "confirmation_token": "a" * 64,
        "confirmation_expires_at": 2_000_000_000,
        "confirmation_phrase": "CONFIRMER UPDATE",
        "idempotency_key": "knowledge-update-0001",
    }


def test_expired_confirmation_maps_to_gone(monkeypatch) -> None:
    def expired(_conn, **_values):
        raise knowledge_update.KnowledgeUpdateExpired("expired")

    monkeypatch.setattr(knowledge_update, "apply_knowledge_update", expired)
    client = TestClient(
        create_cockpit_app(
            connect_fn=_Connection,
            editor_api_key="edit-key",
            update_signing_secret="server-signing-secret",
        )
    )
    response = client.post(
        "/v1/projects/project-a/knowledge/knowledge.coverage/updates/apply",
        headers={
            "Authorization": "Bearer edit-key",
            "X-Pantheon-Human-Actor": "ifan.juang",
        },
        json={
            "proposed_markdown": "# Updated",
            "expected_version": 2,
            "base_markdown_digest": "sha256:base",
            "confirmation_token": "a" * 64,
            "confirmation_expires_at": 1,
            "confirmation_phrase": "CONFIRMER UPDATE",
            "idempotency_key": "knowledge-update-0002",
        },
    )
    assert response.status_code == 410
