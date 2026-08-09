"""Route and authority tests for Decision Requests."""

from fastapi import FastAPI, Header, HTTPException
from fastapi.testclient import TestClient

from mvp_vertical import apu_cross_family, decision_requests
from mvp_vertical.decision_request_api import install_decision_request_routes


def _headers(token: str, *, actor: str | None = None) -> dict[str, str]:
    headers = {"Authorization": f"Bearer {token}"}
    if actor is not None:
        headers["X-Pantheon-Human-Actor"] = actor
    return headers


def _app(monkeypatch) -> FastAPI:
    app = FastAPI()

    def with_connection(operation):
        return operation(None)

    def bearer(authorization: str | None) -> str:
        if not authorization or not authorization.startswith("Bearer "):
            return ""
        return authorization.removeprefix("Bearer ").strip()

    def require_read_key(authorization: str | None = Header(default=None)) -> None:
        if bearer(authorization) not in {"read-secret", "editor-secret"}:
            raise HTTPException(status_code=401, detail="invalid read key")

    def require_editor_key(authorization: str | None = Header(default=None)) -> None:
        if bearer(authorization) != "editor-secret":
            raise HTTPException(status_code=401, detail="invalid editor key")

    def require_human_actor(
        x_pantheon_human_actor: str | None = Header(
            default=None,
            alias="X-Pantheon-Human-Actor",
        ),
    ) -> str:
        if not x_pantheon_human_actor or not x_pantheon_human_actor.strip():
            raise HTTPException(status_code=422, detail="human actor required")
        return x_pantheon_human_actor.strip()

    pending = {
        "decision_request": {
            "request_id": "request-one",
            "status": "pending",
            "decision_type": "validation",
            "question": "Valider la proposition ?",
            "priority": "normal",
            "response_mode": "decision_value",
            "options": [],
            "blocking": True,
            "work_issue_ref": "issue-one",
            "candidate_ref": "candidate-one",
            "candidate_digest": {"algorithm": "sha256", "value": "a" * 64},
            "decision_surface": "cockpit.decisions",
            "decision_owner": "architect",
            "created_by": "human",
            "created_at": "2026-08-06T10:00:00+00:00",
            "revision": 1,
        },
        "decision_record": None,
        "events": [],
        "attention_required": True,
        "request_is_not_decision": True,
        "decision_is_not_execution": True,
    }
    resolved = {
        **pending,
        "decision_request": {
            **pending["decision_request"],
            "status": "resolved",
            "revision": 2,
            "resolved_decision_ref": "decision-one",
            "resolved_at": "2026-08-06T10:30:00+00:00",
        },
        "decision_record": {
            "object_type": "decision_record",
            "decision_id": "decision-one",
            "decision": "approve",
        },
        "attention_required": False,
    }

    monkeypatch.setattr(
        decision_requests,
        "create_request",
        lambda _conn, **_kwargs: pending,
    )
    monkeypatch.setattr(
        decision_requests,
        "list_requests",
        lambda _conn, **_kwargs: [pending],
    )
    monkeypatch.setattr(
        decision_requests,
        "get_request",
        lambda _conn, _request_id: pending,
    )
    monkeypatch.setattr(
        decision_requests,
        "resolve_request",
        lambda _conn, **_kwargs: resolved,
    )
    monkeypatch.setattr(
        decision_requests,
        "cancel_request",
        lambda _conn, **_kwargs: {
            **pending,
            "decision_request": {
                **pending["decision_request"],
                "status": "cancelled",
                "revision": 2,
            },
            "attention_required": False,
        },
    )
    synthetic_decision = {
        "decision_record": {"decision_id": "decision-one"},
        "decision_is_not_execution": True,
        "result_validated": False,
    }
    monkeypatch.setattr(
        decision_requests,
        "get_decision",
        lambda _conn, _decision_id: synthetic_decision,
    )

    # The cross-family scope adapter is route-facing. Route tests have no database
    # connection, so mock this seam rather than teaching production code to accept
    # conn=None.
    monkeypatch.setattr(
        apu_cross_family,
        "create_decision_request",
        lambda _conn, **_kwargs: pending,
    )
    monkeypatch.setattr(
        apu_cross_family,
        "list_requests",
        lambda _conn, **_kwargs: [pending],
    )
    monkeypatch.setattr(
        apu_cross_family,
        "get_request",
        lambda _conn, _request_id: pending,
    )
    monkeypatch.setattr(
        apu_cross_family,
        "enrich_request_projection",
        lambda _conn, projection: projection,
    )
    monkeypatch.setattr(
        apu_cross_family,
        "get_decision",
        lambda _conn, _decision_id: synthetic_decision,
    )
    monkeypatch.setattr(
        apu_cross_family,
        "list_decision_requests_for_apu_object",
        lambda _conn, **_kwargs: [],
    )

    install_decision_request_routes(
        app,
        with_connection=with_connection,
        require_read_key=require_read_key,
        require_editor_key=require_editor_key,
        require_human_actor=require_human_actor,
    )
    return app


def _create_payload() -> dict:
    return {
        "request_id": "request-one",
        "decision_type": "validation",
        "question": "Valider la proposition ?",
        "priority": "normal",
        "response_mode": "decision_value",
        "blocking": True,
        "work_issue_ref": "issue-one",
        "candidate_ref": "candidate-one",
        "candidate_digest": {"algorithm": "sha256", "value": "a" * 64},
        "decision_surface": "cockpit.decisions",
        "decision_owner": "architect",
        "idempotency_key": "create-request-one",
    }


def test_decision_routes_are_installed(monkeypatch) -> None:
    app = _app(monkeypatch)
    methods_by_path: dict[str, set[str]] = {}
    for route in app.routes:
        path = getattr(route, "path", "")
        if "decision" in path:
            methods_by_path.setdefault(path, set()).update(route.methods or set())
    assert methods_by_path["/decision-requests"] == {"GET", "POST"}
    assert methods_by_path["/agency/projects/{project_id}/decision-requests"] == {"GET"}
    assert methods_by_path["/work/issues/{issue_id}/blocking-decision-request"] == {"GET"}
    assert methods_by_path["/decision-requests/{request_id}"] == {"GET"}
    assert methods_by_path["/decision-requests/{request_id}/resolve"] == {"POST"}
    assert methods_by_path["/decision-requests/{request_id}/cancel"] == {"POST"}
    assert methods_by_path["/decisions/{decision_id}"] == {"GET"}


def test_hermes_key_cannot_create_or_resolve_decision_request(monkeypatch) -> None:
    client = TestClient(_app(monkeypatch))
    create = client.post(
        "/decision-requests",
        json=_create_payload(),
        headers=_headers("hermes-secret", actor="hermes-runtime"),
    )
    assert create.status_code == 401

    resolve = client.post(
        "/decision-requests/request-one/resolve",
        json={
            "decision_id": "decision-one",
            "decision": "approve",
            "identity_assurance": "declared",
            "expected_revision": 1,
            "idempotency_key": "resolve-request-one",
        },
        headers=_headers("hermes-secret", actor="hermes-runtime"),
    )
    assert resolve.status_code == 401


def test_editor_key_still_requires_human_actor(monkeypatch) -> None:
    client = TestClient(_app(monkeypatch))
    response = client.post(
        "/decision-requests",
        json=_create_payload(),
        headers=_headers("editor-secret"),
    )
    assert response.status_code == 422


def test_resolution_explicitly_refuses_execution_inference(monkeypatch) -> None:
    client = TestClient(_app(monkeypatch))
    response = client.post(
        "/decision-requests/request-one/resolve",
        json={
            "decision_id": "decision-one",
            "decision": "approve",
            "identity_assurance": "declared",
            "expected_revision": 1,
            "idempotency_key": "resolve-request-one",
        },
        headers=_headers("editor-secret", actor="architect-human"),
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["effect"] == "decision_recorded"
    assert payload["work_issue_transitioned"] is False
    assert payload["runtime_continuation_authorized"] is False
    assert payload["action_executed"] is False


def test_pending_list_is_the_attention_inbox(monkeypatch) -> None:
    client = TestClient(_app(monkeypatch))
    response = client.get(
        "/decision-requests?status=pending",
        headers=_headers("read-secret"),
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["attention_only_when_pending"] is True
    assert payload["decision_requests"][0]["attention_required"] is True
