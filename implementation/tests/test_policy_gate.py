"""Tests for the policy chokepoint seam (Phase C)."""

from mvp_vertical.policy_gate import (
    GateVerdict,
    StandInPolicyClient,
    enforce_consequential,
    governed_effect,
)


def _decision_payload(decided_by="marie.dupont", scope=None):
    scope = scope or {"scope_type": "project", "scope_id": "P-42"}
    return {
        "decision": {"decision_id": "d1", "decided_by": decided_by, "scope": scope},
        "expectation": {"required_scope": {"scope_type": "project", "scope_id": "P-42"}},
    }


class _RaisingClient:
    def preflight(self, candidate):
        raise ConnectionError("PDP down")

    def validate_decision(self, payload):  # pragma: no cover - never reached
        raise AssertionError("must not be called after preflight failure")


def test_eligible_preflight_and_valid_decision_allow_the_effect():
    client = StandInPolicyClient()
    ran = []
    out = governed_effect(
        client,
        candidate={},
        decision_payload=_decision_payload(),
        effect=lambda: ran.append("written") or "ok",
    )
    assert out["status"] == "applied"
    assert out["effect_ran"] is True
    assert out["result"] == "ok"
    assert ran == ["written"]


def test_non_eligible_preflight_blocks_and_effect_never_runs():
    client = StandInPolicyClient(disposition="blocked_pending_human_decision")
    ran = []
    out = governed_effect(
        client,
        candidate={},
        decision_payload=_decision_payload(),
        effect=lambda: ran.append("written"),
    )
    assert out["status"] == "blocked"
    assert out["effect_ran"] is False
    assert ran == []
    assert "blocked_pending_human_decision" in out["disposition"]


def test_invalid_decision_blocks_even_when_preflight_is_eligible():
    client = StandInPolicyClient()
    ran = []
    # system signer -> decision invalid
    out = governed_effect(
        client,
        candidate={},
        decision_payload=_decision_payload(decided_by="hermes"),
        effect=lambda: ran.append("written"),
    )
    assert out["status"] == "blocked"
    assert out["effect_ran"] is False
    assert ran == []
    assert any("non-human" in r for r in out["reasons"])


def test_scope_mismatch_blocks():
    client = StandInPolicyClient()
    out = governed_effect(
        client,
        candidate={},
        decision_payload=_decision_payload(scope={"scope_type": "project", "scope_id": "OTHER"}),
        effect=lambda: "written",
    )
    assert out["status"] == "blocked"
    assert any("scope" in r for r in out["reasons"])


def test_pdp_unavailable_fails_closed():
    ran = []
    out = governed_effect(
        _RaisingClient(),
        candidate={},
        decision_payload=_decision_payload(),
        effect=lambda: ran.append("written"),
    )
    assert out["status"] == "blocked"
    assert out["disposition"] == "policy_unavailable"
    assert out["effect_ran"] is False
    assert ran == []


def test_enforce_consequential_returns_a_verdict():
    verdict = enforce_consequential(
        StandInPolicyClient(), candidate={}, decision_payload=_decision_payload()
    )
    assert isinstance(verdict, GateVerdict)
    assert verdict.allowed is True
