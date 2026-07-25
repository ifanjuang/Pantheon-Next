"""Policy chokepoint seam (Phase C): a consequential effect routes through the
Pantheon policy check before it happens.

This repository does not embed the Pantheon policy service. It defines the seam
the runtime uses to consult a Policy Decision Point (Pantheon `mcp-server`) and
to enforce the verdict — the Policy Enforcement Point role.

Rules:

- fail closed on transport, malformed payload or non-eligible preflight;
- bind human-decision validation to PEP-derived effect facts when supplied;
- never let a validated decision override explicit PDP effect-denial flags;
- neutralize runtime/model smart approvals.

`eligible_for_candidate_work` is not an external-effect authorization. The
current Pantheon V0 preflight explicitly returns `external_effect_allowed=false`
and `canonical_effect_allowed=false`; the live PEP honors those flags.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Protocol

from .policy_request import bind_decision_payload, build_preflight_payload

_ELIGIBLE_DISPOSITIONS = frozenset(
    {"eligible_for_candidate_work", "eligible_with_gate_signals_unverified"}
)


class PolicyClient(Protocol):
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
    """Consult the PDP and decide whether the local executor may run."""

    try:
        bound_decision = bind_decision_payload(candidate, decision_payload)
        preflight_payload = build_preflight_payload(candidate, bound_decision)
        preflight = client.preflight(preflight_payload)
    except Exception as exc:
        return GateVerdict(False, "policy_unavailable", [f"preflight call failed: {exc}"])

    disposition = str(preflight.get("policy_disposition", "unknown"))
    if disposition not in _ELIGIBLE_DISPOSITIONS:
        reasons = [f"preflight disposition: {disposition}"]
        reasons += list(preflight.get("missing_requirements", []))
        return GateVerdict(False, disposition, reasons)

    request = preflight_payload["request"]
    requests_external_effect = bool(
        request.get("external_effect") or request.get("transmission_requested")
    )
    if requests_external_effect and preflight.get("external_effect_allowed") is not True:
        return GateVerdict(
            False,
            "blocked_external_effect_not_authorized",
            [
                "Pantheon preflight did not authorize an external effect",
                f"policy disposition: {disposition}",
            ],
        )

    if request.get("memory_promotion_requested") and preflight.get(
        "canonical_effect_allowed"
    ) is not True:
        return GateVerdict(
            False,
            "blocked_canonical_effect_not_authorized",
            [
                "Pantheon preflight did not authorize a canonical/memory effect",
                f"policy disposition: {disposition}",
            ],
        )

    try:
        validation = client.validate_decision(bound_decision)
    except Exception as exc:
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
    """Deterministic offline PDP stand-in for tests; not Pantheon authority.

    The stand-in is deliberately policy-version-neutral. Its external-effect
    flag defaults to ``True`` for backward-compatible seam tests. Tests that
    model the current Pantheon V0 must pass ``external_effect_allowed=False``
    explicitly. Live behavior always comes from ``HttpPolicyClient`` responses,
    never from these defaults.
    """

    _SYSTEM_PREFIXES = ("system", "service", "runtime", "hermes", "bot", "agent")

    def __init__(
        self,
        *,
        disposition: str = "eligible_for_candidate_work",
        external_effect_allowed: bool = True,
        canonical_effect_allowed: bool = False,
    ):
        self._disposition = disposition
        self._external_effect_allowed = external_effect_allowed
        self._canonical_effect_allowed = canonical_effect_allowed
        self.last_preflight: dict[str, Any] | None = None
        self.last_decision: dict[str, Any] | None = None

    def preflight(self, candidate: dict[str, Any]) -> dict[str, Any]:
        self.last_preflight = candidate
        return {
            "policy_disposition": self._disposition,
            "missing_requirements": [],
            "external_effect_allowed": self._external_effect_allowed,
            "canonical_effect_allowed": self._canonical_effect_allowed,
        }

    def validate_decision(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.last_decision = payload
        decision = payload.get("decision") or {}
        expectation = payload.get("expectation") or {}
        findings: list[str] = []
        signer = str(decision.get("decided_by", "")).strip().lower()
        if not signer or signer.split(":", 1)[0].split("-", 1)[0] in self._SYSTEM_PREFIXES:
            findings.append("decided_by is empty or a non-human identity")
        req_scope = expectation.get("required_scope")
        if req_scope is not None and decision.get("scope") != req_scope:
            findings.append("decision scope does not match required scope")
        required_ceiling = expectation.get("required_ceiling")
        if required_ceiling is not None and decision.get("approval_level") != required_ceiling:
            findings.append("decision approval_level does not match required ceiling")
        object_identity = expectation.get("object_identity")
        if object_identity is not None and decision.get("object_identity") != object_identity:
            findings.append("decision object_identity does not match effect object")
        expected_digest = expectation.get("expected_digest")
        if expected_digest is not None and decision.get("content_digest") != expected_digest:
            findings.append("decision content_digest does not match effect digest")
        verdict = "valid" if not findings else "invalid"
        return {"verdict": verdict, "findings": findings}


class HttpPolicyClient:
    """Real ``PolicyClient`` for the Pantheon internal HTTP PDP."""

    _PREFLIGHT = "/v1/policy/preflights:evaluate"
    _VALIDATE = "/v1/policy/decisions:validate"

    def __init__(
        self,
        base_url: str,
        api_key: str,
        *,
        timeout: float = 5.0,
        client: Any | None = None,
    ):
        self._base_url = base_url.rstrip("/")
        self._api_key = api_key
        self._timeout = timeout
        self._client = client

    def _post(self, path: str, body: dict[str, Any]) -> dict[str, Any]:
        client = self._client
        owns = client is None
        if owns:
            import httpx

            client = httpx.Client(timeout=self._timeout)
        try:
            response = client.post(
                self._base_url + path,
                json=body,
                headers={"Authorization": f"Bearer {self._api_key}"},
                timeout=self._timeout,
            )
            response.raise_for_status()
            return response.json()
        finally:
            if owns:
                client.close()

    def preflight(self, candidate: dict[str, Any]) -> dict[str, Any]:
        return self._post(self._PREFLIGHT, candidate)

    def validate_decision(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self._post(self._VALIDATE, payload)
