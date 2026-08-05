"""HTTP boundary tests for the Source intake route installer."""

from __future__ import annotations

from fastapi import FastAPI, Header, HTTPException
from fastapi.testclient import TestClient

from mvp_vertical import source_intake
from mvp_vertical.source_intake_api import install_source_intake_routes


class _Connection:
    def close(self) -> None:
        pass


def _client() -> TestClient:
    app = FastAPI()

    def with_connection(operation):
        conn = _Connection()
        try:
            return operation(conn)
        finally:
            conn.close()

    def require_read_key(authorization: str | None = Header(default=None)) -> None:
        if authorization != "Bearer read-key":
            raise HTTPException(status_code=401, detail="invalid read API key")

    def require_writer_kind(authorization: str | None = Header(default=None)) -> str:
        if authorization == "Bearer editor-key":
            return "human"
        if authorization == "Bearer hermes-key":
            return "hermes"
        raise HTTPException(status_code=401, detail="invalid writer API key")

    def require_actor(x_pantheon_actor: str | None = Header(default=None, alias="X-Pantheon-Actor")) -> str:
        if not x_pantheon_actor:
            raise HTTPException(status_code=422, detail="actor required")
        return x_pantheon_actor

    install_source_intake_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_writer_kind=require_writer_kind,
        require_actor=require_actor,
    )
    return TestClient(app)


def test_create_source_exposes_no_semantic_side_effect(monkeypatch) -> None:
    observed = {}

    def create_source(_conn, **values):
        observed.update(values)
        return {
            "source_id": values["source_id"],
            "project_link_status": "unassigned",
            "project_id": None,
            "revision": 1,
        }

    monkeypatch.setattr(source_intake, "create_source", create_source)
    response = _client().post(
        "/agency/sources",
        headers={"Authorization": "Bearer editor-key", "X-Pantheon-Actor": "ifan"},
        json={
            "source_id": "source-mail-1",
            "source_kind": "email",
            "origin": {"system": "gmail", "external_ref": "message-1"},
            "raw_source_ref": "gmail://message-1",
            "received_at": "2026-08-05T17:00:00Z",
            "declared_project_name": "Maison Blanc",
            "idempotency_key": "source-create-0001",
        },
    )
    assert response.status_code == 201
    body = response.json()
    assert body["project_mutated"] is False
    assert body["information_created"] is False
    assert body["evidence_admitted"] is False
    assert observed["actor_kind"] == "human"
    assert observed["origin_system"] == "gmail"


def test_suggestion_is_explicitly_not_a_confirmed_link(monkeypatch) -> None:
    monkeypatch.setattr(
        source_intake,
        "suggest_projects",
        lambda _conn, **values: {
            "source_id": values["source_id"],
            "project_link_status": "suggested",
            "project_id": None,
            "candidate_project_refs": values["candidates"],
            "revision": 2,
        },
    )
    response = _client().post(
        "/agency/sources/source-mail-1/suggest-projects",
        headers={"Authorization": "Bearer editor-key", "X-Pantheon-Actor": "ifan"},
        json={
            "expected_revision": 1,
            "idempotency_key": "source-suggest-0001",
            "candidates": [
                {
                    "project_ref": "project-blanc",
                    "score": 0.93,
                    "basis": ["declared_name_match"],
                    "producer": "matcher",
                    "created_at": "2026-08-05T17:01:00Z",
                }
            ],
        },
    )
    assert response.status_code == 200
    assert response.json()["project_link_confirmed"] is False
    assert response.json()["source"]["project_id"] is None


def test_hermes_global_source_write_is_refused_before_adapter(monkeypatch) -> None:
    called = False

    def create_source(_conn, **_values):
        nonlocal called
        called = True
        raise AssertionError("Hermes global write must not reach Source adapter")

    monkeypatch.setattr(source_intake, "create_source", create_source)
    response = _client().post(
        "/agency/sources",
        headers={"Authorization": "Bearer hermes-key", "X-Pantheon-Actor": "hermes"},
        json={
            "source_id": "source-hermes-1",
            "source_kind": "text",
            "origin": {"system": "hermes", "external_ref": "result-1"},
            "raw_source_ref": "native://candidate",
            "received_at": "2026-08-05T17:00:00Z",
            "idempotency_key": "source-hermes-0001",
        },
    )
    assert response.status_code == 403
    assert called is False


def test_source_list_is_bounded_and_read_only(monkeypatch) -> None:
    observed = {}

    def list_sources(_conn, **values):
        observed.update(values)
        return [{"source_id": "source-1", "project_link_status": "unassigned"}]

    monkeypatch.setattr(source_intake, "list_sources", list_sources)
    response = _client().get(
        "/agency/sources",
        params={"project_link_status": "unassigned", "limit": 25},
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 200
    assert response.json()["scope_match"] == "agency_sources"
    assert observed == {"project_link_status": "unassigned", "project_id": None, "limit": 25}
