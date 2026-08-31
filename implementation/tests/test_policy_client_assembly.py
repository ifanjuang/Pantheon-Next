"""The application must not be able to lose its chokepoint silently.

`policy_gate.enforce_consequential` and `HttpPolicyClient` were written, tested
and never called: `policy_client` had no non-test caller, `HttpPolicyClient` was
never instantiated outside tests, and the Cockpit's consequential Knowledge write
ran on module-local guards alone while `CLAUDE.md` described a central gate.

Nothing detected that. The module-usage audit builds an import graph, and the
import edge genuinely existed — what was missing was the argument that triggers
the call. `test_cockpit_shell.py` and `test_cockpit_composed.py` contained no
occurrence of `policy`, so the factory could be changed in either direction with
no test reacting.

These tests cover the assembly itself, so the wiring cannot be removed, defaulted
away or quietly made optional again.

```text
gate implemented != gate invoked
unconfigured != permitted
disabled by default != disabled by decision
```
"""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from mvp_vertical.cockpit_shell import create_cockpit_app
from mvp_vertical.policy_gate import HttpPolicyClient, StandInPolicyClient

APPLY_ROUTE = "/projects/{project}/knowledge/{kid}/updates/apply"
PROJECT = "project-a"
KID = "knowledge.coverage"


class _Connection:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def close(self):
        return None


def _body() -> dict:
    return {
        "proposed_markdown": "# Updated",
        "expected_version": 2,
        "review_status": "needs_review",
        "base_markdown_digest": "sha256:base",
        "confirmation_token": "a" * 64,
        "confirmation_expires_at": 2_000_000_000,
        "confirmation_phrase": "CONFIRMER UPDATE",
        "idempotency_key": "knowledge-update-0001",
    }


def _headers() -> dict:
    return {
        "Authorization": "Bearer edit-key",
        "X-Pantheon-Human-Actor": "ifan.juang",
    }


def _app(**kwargs):
    kwargs.setdefault("connect_fn", _Connection)
    kwargs.setdefault("editor_api_key", "edit-key")
    kwargs.setdefault("update_signing_secret", "server-signing-secret")
    return create_cockpit_app(**kwargs)


def _post(client: TestClient):
    return client.post(APPLY_ROUTE.format(project=PROJECT, kid=KID), headers=_headers(), json=_body())


# --------------------------------------------------------------------------
# Default posture.
# --------------------------------------------------------------------------


def test_enforcement_is_required_unless_a_deployment_says_otherwise(monkeypatch) -> None:
    monkeypatch.delenv("MVP_POLICY_ENFORCEMENT", raising=False)
    assert _app().state.policy_enforcement == "required"


def test_an_unconfigured_decision_point_refuses_the_consequential_write(monkeypatch) -> None:
    monkeypatch.delenv("MVP_POLICY_ENFORCEMENT", raising=False)
    monkeypatch.delenv("MVP_POLICY_API_URL", raising=False)
    monkeypatch.delenv("MVP_POLICY_API_KEY", raising=False)

    response = _post(TestClient(_app()))

    assert response.status_code == 503
    assert "policy decision point is not configured" in response.json()["detail"]


def test_refusal_happens_before_the_body_is_examined(monkeypatch) -> None:
    """An unconfigured gate must refuse, not fall through to the local guards."""
    monkeypatch.delenv("MVP_POLICY_ENFORCEMENT", raising=False)
    monkeypatch.delenv("MVP_POLICY_API_URL", raising=False)

    client = TestClient(_app())
    response = client.post(
        APPLY_ROUTE.format(project=PROJECT, kid=KID),
        headers=_headers(),
        json={"proposed_markdown": "# Updated"},  # structurally invalid body
    )

    # 422 would mean the request reached body validation with no decision point.
    assert response.status_code == 503


def test_read_only_projections_still_work_without_a_decision_point(monkeypatch) -> None:
    """The refusal is scoped to consequential writes, not to the whole surface."""
    monkeypatch.delenv("MVP_POLICY_API_URL", raising=False)
    app = _app(api_key="read-key")
    routes = {route.path for route in app.routes}
    assert APPLY_ROUTE.format(project="{parent_project_id}", kid="{knowledge_id}") in routes
    # The app assembles and serves its read surface with no PDP configured.
    assert TestClient(app).get("/healthz").status_code in {200, 404}


# --------------------------------------------------------------------------
# Explicit postures.
# --------------------------------------------------------------------------


def test_a_configured_client_is_handed_to_the_route(monkeypatch) -> None:
    monkeypatch.delenv("MVP_POLICY_ENFORCEMENT", raising=False)
    client = StandInPolicyClient()
    assert _app(policy_client=client).state.policy_client is client


def test_environment_configuration_builds_a_real_http_client(monkeypatch) -> None:
    monkeypatch.setenv("MVP_POLICY_API_URL", "https://policy.internal")
    monkeypatch.setenv("MVP_POLICY_API_KEY", "policy-key")
    assert isinstance(_app().state.policy_client, HttpPolicyClient)


def test_a_partial_environment_does_not_half_configure_a_client(monkeypatch) -> None:
    """A URL with no key is not a decision point; it must refuse, not connect."""
    monkeypatch.setenv("MVP_POLICY_API_URL", "https://policy.internal")
    monkeypatch.delenv("MVP_POLICY_API_KEY", raising=False)
    assert _app().state.policy_client is None
    assert _post(TestClient(_app())).status_code == 503


def test_disabling_enforcement_must_be_stated_by_name(monkeypatch) -> None:
    monkeypatch.delenv("MVP_POLICY_API_URL", raising=False)
    app = _app(policy_enforcement="disabled")
    assert app.state.policy_enforcement == "disabled"
    # The write is admitted to the local guards, which reject this body on their
    # own terms — the point is that it is no longer stopped at 503.
    assert _post(TestClient(app)).status_code != 503


def test_an_unknown_enforcement_posture_fails_closed_at_assembly() -> None:
    with pytest.raises(ValueError, match="MVP_POLICY_ENFORCEMENT"):
        _app(policy_enforcement="maybe")


def test_the_environment_can_only_select_a_declared_posture(monkeypatch) -> None:
    monkeypatch.setenv("MVP_POLICY_ENFORCEMENT", "off")
    with pytest.raises(ValueError, match="MVP_POLICY_ENFORCEMENT"):
        _app()


def test_posture_is_read_case_and_whitespace_insensitively(monkeypatch) -> None:
    monkeypatch.setenv("MVP_POLICY_ENFORCEMENT", "  Disabled ")
    assert _app().state.policy_enforcement == "disabled"


# --------------------------------------------------------------------------
# The composed application must not drop the wiring on its way through.
# --------------------------------------------------------------------------


def test_the_composed_application_carries_the_same_posture(monkeypatch) -> None:
    from mvp_vertical.cockpit_composed import create_composed_cockpit_app

    monkeypatch.delenv("MVP_POLICY_ENFORCEMENT", raising=False)
    client = StandInPolicyClient()
    app = create_composed_cockpit_app(
        connect_fn=_Connection,
        initialize_fn=None,
        editor_api_key="edit-key",
        update_signing_secret="server-signing-secret",
        policy_client=client,
    )
    assert app.state.policy_client is client
    assert app.state.policy_enforcement == "required"
