"""Build bounded Pantheon policy/decision payloads for the runtime PEP.

Runtime adapters know the concrete effect being attempted (Paperless metadata
update, project-document intake, capability action). The Pantheon HTTP API is
intentionally generic. This module translates runtime facts into that generic
contract without letting a caller redefine the object, digest, scope or known
external-effect status that the human decision must cover.
"""

from __future__ import annotations

from typing import Any


_REQUEST_FIELDS = frozenset(
    {
        "intent",
        "external_effect",
        "writes_state",
        "transmission_requested",
        "memory_promotion_requested",
        "professional_position",
        "financial_or_contractual_effect",
        "scope",
    }
)

_GATE_FIELDS = frozenset(
    {
        "task_contract_ref",
        "evidence_pack_candidate_ref",
        "human_decision_ref",
        "human_decision_level",
    }
)

_EXPECTATION_FIELDS = frozenset(
    {
        "required_ceiling",
        "required_scope",
        "object_identity",
        "expected_digest",
    }
)

_PAPERLESS_EXTERNAL_EFFECT_KINDS = frozenset(
    {
        "external_document_upload",
        "external_document_metadata_update",
    }
)

# Issue #664 qualification fixture. Only this synthetic intent carries the
# already-bound human decision into preflight so Pantheon can compose signed
# gate validation before emitting the one bounded external-effect permission.
# Real adapters remain on their existing transport contract until separately
# qualified.
_QUALIFICATION_EXTERNAL_EFFECT_INTENT = "qualification_external_effect"


def _scope_from_decision(decision_payload: dict[str, Any]) -> dict[str, Any] | None:
    expectation = decision_payload.get("expectation") or {}
    decision = decision_payload.get("decision") or {}
    scope = expectation.get("required_scope") or decision.get("scope")
    return dict(scope) if isinstance(scope, dict) else None


def _pep_owned_request_overrides(candidate: dict[str, Any]) -> dict[str, bool]:
    """Return effect facts that a runtime caller is not allowed to downgrade.

    The legacy Paperless helpers accept a caller-supplied candidate mapping for
    trace/context. Their executor is nevertheless known by the PEP: upload and
    root-document metadata mutation are external state writes. Recognize those
    effects both by their normal effect kind and by the structural fields the
    helper itself always adds, so a caller cannot hide the effect by replacing
    ``effect_kind`` or a nested ``request.external_effect`` value.

    False positives intentionally fail conservative: classifying an ambiguous
    candidate as an external write is safer than silently allowing one.
    """

    kind = str(candidate.get("effect_kind") or "").strip()
    paperless_upload_shape = "filename" in candidate and "content_hash" in candidate
    paperless_metadata_shape = "document_id" in candidate and "changed_fields" in candidate
    if (
        kind in _PAPERLESS_EXTERNAL_EFFECT_KINDS
        or paperless_upload_shape
        or paperless_metadata_shape
    ):
        return {"external_effect": True, "writes_state": True}
    return {}


def bind_decision_payload(
    candidate: dict[str, Any],
    decision_payload: dict[str, Any],
) -> dict[str, Any]:
    """Bind decision validation to PEP-owned effect facts when provided.

    ``decision`` remains caller-provided because it represents the human choice
    reference. ``expectation`` is different: it states what the effect actually
    requires. When an adapter supplies ``decision_expectation`` those fields are
    authoritative for this execution attempt and caller-supplied expectation
    values cannot override them.

    Backward compatibility is deliberately narrow: adapters that have not yet
    supplied ``decision_expectation`` retain their existing caller expectation.
    New consequential bindings should always derive and supply the expectation
    from runtime-observed identity, digest and Task Contract scope.
    """

    if not isinstance(decision_payload, dict):
        raise ValueError("decision_payload must be a mapping")
    decision = decision_payload.get("decision")
    if not isinstance(decision, dict):
        raise ValueError("decision_payload.decision must be a mapping")

    explicit = candidate.get("decision_expectation")
    if explicit is not None:
        if not isinstance(explicit, dict):
            raise ValueError("candidate.decision_expectation must be a mapping")
        expectation = {
            key: explicit[key]
            for key in _EXPECTATION_FIELDS
            if explicit.get(key) not in (None, "")
        }
        missing = sorted(_EXPECTATION_FIELDS - set(expectation))
        if missing:
            raise ValueError(
                "candidate.decision_expectation is incomplete: " + ", ".join(missing)
            )
    else:
        caller_expectation = decision_payload.get("expectation")
        if not isinstance(caller_expectation, dict):
            raise ValueError("decision_payload.expectation must be a mapping")
        expectation = dict(caller_expectation)

    return {
        "decision": dict(decision),
        "expectation": expectation,
    }


def build_preflight_payload(
    candidate: dict[str, Any],
    decision_payload: dict[str, Any],
) -> dict[str, Any]:
    """Translate one runtime candidate to ``pantheon.policy.v1`` preflight input.

    Normal runtime candidates contain only ``request`` and ``gate_signals`` as
    defined by the V0 transport. The synthetic #664 qualification intent also
    carries ``decision_validation`` so the PDP can actually compose the existing
    gate validator before emitting its fixture-only external-effect permission.
    Runtime-specific keys such as ``effect_kind`` and ``document_id`` remain
    local trace data and are not leaked into the policy transport schema.

    Callers may provide an explicit ``request`` / ``gate_signals`` mapping. When
    they provide only runtime-specific fields, conservative defaults are used:
    a consequential effect is assumed to write state and affect an external
    runtime unless the caller explicitly says otherwise. PEP-owned facts for
    known external executors are applied last and therefore cannot be downgraded
    by caller-provided request fields.
    """

    explicit_request = candidate.get("request")
    if explicit_request is not None and not isinstance(explicit_request, dict):
        raise ValueError("candidate.request must be a mapping")

    source_request = explicit_request or {}
    request: dict[str, Any] = {
        key: source_request[key]
        for key in _REQUEST_FIELDS
        if key in source_request
    }

    request.setdefault(
        "intent",
        str(
            candidate.get("intent")
            or candidate.get("effect_kind")
            or candidate.get("action")
            or "consequential_effect"
        ),
    )
    request.setdefault("external_effect", bool(candidate.get("external_effect", True)))
    request.setdefault("writes_state", bool(candidate.get("writes_state", True)))
    request.setdefault(
        "transmission_requested", bool(candidate.get("transmission_requested", False))
    )
    request.setdefault(
        "memory_promotion_requested", bool(candidate.get("memory_promotion_requested", False))
    )
    request.setdefault(
        "professional_position", bool(candidate.get("professional_position", False))
    )
    request.setdefault(
        "financial_or_contractual_effect",
        bool(candidate.get("financial_or_contractual_effect", False)),
    )

    if "scope" not in request:
        scope = candidate.get("scope")
        if isinstance(scope, dict):
            request["scope"] = dict(scope)
        else:
            inferred_scope = _scope_from_decision(decision_payload)
            if inferred_scope is not None:
                request["scope"] = inferred_scope

    # Apply non-overridable executor facts only after caller/context values have
    # been normalized. This closes the downgrade path where a Paperless write
    # supplied request.external_effect=false.
    request.update(_pep_owned_request_overrides(candidate))

    explicit_signals = candidate.get("gate_signals")
    if explicit_signals is not None and not isinstance(explicit_signals, dict):
        raise ValueError("candidate.gate_signals must be a mapping")

    source_signals = explicit_signals or {}
    gate_signals: dict[str, Any] = {
        key: source_signals[key]
        for key in _GATE_FIELDS
        if source_signals.get(key) not in (None, "")
    }

    for key in ("task_contract_ref", "evidence_pack_candidate_ref"):
        if key not in gate_signals and candidate.get(key) not in (None, ""):
            gate_signals[key] = candidate[key]

    decision = decision_payload.get("decision") or {}
    if gate_signals.get("human_decision_ref") in (None, "") and decision.get("decision_id"):
        gate_signals["human_decision_ref"] = decision["decision_id"]
    if gate_signals.get("human_decision_level") in (None, "") and decision.get("approval_level"):
        gate_signals["human_decision_level"] = decision["approval_level"]

    payload: dict[str, Any] = {
        "request": request,
        "gate_signals": gate_signals,
    }
    if request.get("intent") == _QUALIFICATION_EXTERNAL_EFFECT_INTENT:
        decision = decision_payload.get("decision")
        expectation = decision_payload.get("expectation")
        if not isinstance(decision, dict) or not isinstance(expectation, dict):
            raise ValueError(
                "qualification_external_effect requires a bound decision validation payload"
            )
        payload["decision_validation"] = {
            "decision": dict(decision),
            "expectation": dict(expectation),
        }
    return payload
