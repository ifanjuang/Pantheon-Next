"""Policy chokepoint seam (Phase C): a consequential effect routes through the
Pantheon policy check before it happens.

This repository does not embed the Pantheon policy service. It defines the seam
the runtime uses to consult a Policy Decision Point (Pantheon `mcp-server`) and
to enforce the verdict — the Policy Enforcement Point role. A real deployment
injects an HTTP client to that PDP; tests inject the deterministic stand-in
below.

Two rules make this a real chokepoint, not advice:

- **Fail closed.** If the policy client is unavailable, or the verdict is not a
  clear allow, the consequential effect is blocked and never runs.
- **Smart-approvals neutralized.** The seam never auto-approves. Only an eligible
  preflight *and* a valid human decision permit the effect; an in-runtime
  "smart approval" cannot substitute for the human decision.

`STAND-IN`: `StandInPolicyClient` occupies the PDP seat for offline tests. It is
not the Pantheon policy service:

    stand_in_policy_client != Pantheon PDP
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Protocol

# Preflight dispositions that permit continued (candidate) work. Anything else
# blocks. Mirrors the Pantheon preflight contract; the seat is external.
_ELIGIBLE_DISPOSITIONS = frozenset(
    {"eligible_for_candidate_work", "eligible_with_gate_signals_unverified"}
)


class PolicyClient(Protocol):
    """The bounded surface the seam consults. A real client calls the Pantheon
    mcp-server (`POST /v1/policy/preflights:evaluate` and
    `POST /v1/policy/decisions:validate`); it never executes the effect."""

    def preflight(self, candidate: dict[str, Any]) -> dict[str, Any]:
        ...

    def validate_decision(self, payload: dict[str, Any]) -> dict[str, Any]:
        ...


@dataclass(frozen=True)
class GateVerdict:
    allowed: bool
    disposition: str
    reasons: list[str] = field(default_factory=list)


def enforce_consequential(
    client: PolicyClient,
    *,
    candidate: dict[str, Any],
    decision_payload: dict[str, Any],
) -> GateVerdict:
    """Consult the PDP and return whether the consequential effect may proceed.

    Fail closed: any client error, a non-eligible preflight, or a decision that
    is not `valid` yields `allowed=False`. The effect must not run unless
    `allowed` is True."""
    try:
        preflight = client.preflight(candidate)
    except Exception as exc:  # PDP unavailable -> fail closed
        return GateVerdict(False, "policy_unavailable", [f"preflight call failed: {exc}"])

    disposition = str(preflight.get("policy_disposition", "unknown"))
    if disposition not in _ELIGIBLE_DISPOSITIONS:
        reasons = [f"preflight disposition: {disposition}"]
        reasons += list(preflight.get("missing_requirements", []))
        return GateVerdict(False, disposition, reasons)

    # An eligible preflight is not enough for a consequential effect: the human
    # decision must validate (the gate-validation slice). Smart-approvals never
    # substitute for it.
    try:
        validation = client.validate_decision(decision_payload)
    except Exception as exc:  # PDP unavailable -> fail closed
        return GateVerdict(False, "policy_unavailable", [f"decision validation failed: {exc}"])

    if validation.get("verdict") != "valid":
        reasons = [f"decision verdict: {validation.get('verdict', 'unknown')}"]
        reasons += list(validation.get("findings", []))
        return GateVerdict(False, disposition, reasons)

    return GateVerdict(True, disposition, [])


def governed_effect(
    client: PolicyClient,
    *,
    candidate: dict[str, Any],
    decision_payload: dict[str, Any],
    effect: Callable[[], Any],
) -> dict[str, Any]:
    """Run a consequential `effect` only behind an allow verdict.

    `effect` is a zero-argument callable that performs the actual consequential
    write (e.g. applying a Knowledge revision). It is invoked only when the
    chokepoint allows; on a block it never runs and a refusal is returned as
    data. This is the seam that makes Pantheon master in fact for this effect."""
    verdict = enforce_consequential(
        client, candidate=candidate, decision_payload=decision_payload
    )
    if not verdict.allowed:
        return {
            "status": "blocked",
            "disposition": verdict.disposition,
            "reasons": verdict.reasons,
            "effect_ran": False,
        }
    return {
        "status": "applied",
        "disposition": verdict.disposition,
        "effect_ran": True,
        "result": effect(),
    }


class StandInPolicyClient:
    """Deterministic offline PDP stand-in for tests. It is NOT the Pantheon
    policy service; it lets the seam be exercised without a live PDP.

    `preflight` echoes a caller-declared disposition (default eligible).
    `validate_decision` performs a minimal human-signer / required-field check so
    the seam's allow/block branches are testable. Real validation lives in the
    Pantheon `mcp-server` gate-validation slice."""

    _SYSTEM_PREFIXES = ("system", "service", "runtime", "hermes", "bot", "agent")

    def __init__(self, *, disposition: str = "eligible_for_candidate_work"):
        self._disposition = disposition

    def preflight(self, candidate: dict[str, Any]) -> dict[str, Any]:
        disposition = candidate.get("declared_disposition", self._disposition)
        missing = candidate.get("missing_requirements", [])
        return {"policy_disposition": disposition, "missing_requirements": list(missing)}

    def validate_decision(self, payload: dict[str, Any]) -> dict[str, Any]:
        decision = payload.get("decision") or {}
        expectation = payload.get("expectation") or {}
        findings: list[str] = []
        signer = str(decision.get("decided_by", "")).strip().lower()
        if not signer or signer.split(":", 1)[0].split("-", 1)[0] in self._SYSTEM_PREFIXES:
            findings.append("decided_by is empty or a non-human identity")
        req_scope = expectation.get("required_scope")
        if req_scope is not None and decision.get("scope") != req_scope:
            findings.append("decision scope does not match required scope")
        verdict = "valid" if not findings else "invalid"
        return {"verdict": verdict, "findings": findings}
