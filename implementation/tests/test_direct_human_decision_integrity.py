from __future__ import annotations

from mvp_vertical.policy_gate import StandInPolicyClient, enforce_consequential


def _candidate() -> dict:
    return {
        "intent": "act_working_information",
        "decision_expectation": {
            "required_ceiling": "C2",
            "required_scope": {"scope_type": "project", "scope_id": "project-a"},
            "object_identity": "agency_information:info-a",
            "expected_digest": "sha256:effect-a",
        },
        "request": {
            "intent": "act_working_information",
            "external_effect": False,
            "writes_state": True,
            "scope": {"scope_type": "project", "scope_id": "project-a"},
        },
    }


def _decision() -> dict:
    return {
        "decision": {
            "decision_id": "decision-a",
            "decided_by": "human-reviewer",
            "approval_level": "C2",
            "scope": {"scope_type": "project", "scope_id": "project-a"},
            "object_identity": "agency_information:info-a",
            "content_digest": "sha256:effect-a",
            "expires_at": "2099-01-01T00:00:00Z",
            "signature": "signed-outside-effect-owner",
        }
    }


def test_bare_decision_reference_cannot_be_upgraded_by_the_effect_owner() -> None:
    client = StandInPolicyClient()

    verdict = enforce_consequential(
        client,
        candidate=_candidate(),
        decision_payload={"decision": {"decision_id": "decision-a"}},
    )

    assert verdict.allowed is False
    assert verdict.disposition == "blocked_invalid_decision_envelope"
    assert "complete independently authored signed decision" in verdict.reasons[0]
    assert client.last_preflight is None
    assert client.last_decision is None


def test_human_response_cannot_substitute_for_a_direct_human_decision() -> None:
    client = StandInPolicyClient()

    verdict = enforce_consequential(
        client,
        candidate=_candidate(),
        decision_payload={
            "human_response": {
                "response_id": "human-response-a",
                "responded_by": "human-reviewer",
                "response_text": "Proceed.",
            }
        },
    )

    assert verdict.allowed is False
    assert verdict.disposition == "blocked_invalid_decision_envelope"
    assert verdict.reasons == ["decision_payload.decision must be a mapping"]
    assert client.last_preflight is None
    assert client.last_decision is None


def test_direct_human_effect_refuses_valid_but_unauthenticated_issuer() -> None:
    client = StandInPolicyClient(issuer_authenticated=False)

    verdict = enforce_consequential(
        client,
        candidate=_candidate(),
        decision_payload=_decision(),
    )

    assert verdict.allowed is False
    assert verdict.disposition == "blocked_unauthenticated_human_decision"
    assert client.last_preflight is not None
    assert client.last_decision is not None


def test_direct_human_effect_accepts_complete_authenticated_matching_decision() -> None:
    client = StandInPolicyClient(issuer_authenticated=True)

    verdict = enforce_consequential(
        client,
        candidate=_candidate(),
        decision_payload=_decision(),
    )

    assert verdict.allowed is True
    assert client.last_decision == {
        "decision": _decision()["decision"],
        "expectation": _candidate()["decision_expectation"],
    }


def test_non_direct_effect_does_not_inherit_direct_human_issuer_requirement() -> None:
    candidate = {
        "intent": "capability:install",
        "decision_expectation": {
            "required_ceiling": "C2",
            "required_scope": {"scope_type": "project", "scope_id": "project-a"},
            "object_identity": "capability:tool-a",
            "expected_digest": "sha256:tool-a",
        },
        "request": {
            "intent": "capability:install",
            "external_effect": False,
            "writes_state": True,
        },
    }
    decision = {
        "decision": {
            "decision_id": "decision-a",
            "decided_by": "human-reviewer",
            "approval_level": "C2",
            "scope": {"scope_type": "project", "scope_id": "project-a"},
            "object_identity": "capability:tool-a",
            "content_digest": "sha256:tool-a",
        }
    }
    client = StandInPolicyClient(issuer_authenticated=False)

    verdict = enforce_consequential(
        client,
        candidate=candidate,
        decision_payload=decision,
    )

    assert verdict.allowed is True
