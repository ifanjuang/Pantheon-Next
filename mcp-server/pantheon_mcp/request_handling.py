"""Progressive request-handling projection.

This module turns caller-provided governed conditions plus the K/V/C
classification into the smallest useful governance handling recommendation.
It does not understand raw natural language, execute work, dispatch roles,
run a workflow, authorize an effect, or approve an output.

The preferred input is a small list of existing ROLE_ACTIVATION conditions plus
optional non-persistent coordination relations. Topology is derived from those
relations, not from domain-specific Role combinations.
"""

from __future__ import annotations

from typing import Any


# Implemented subset of ROLE_ACTIVATION.md mandatory_role_triggers.
# Tests bind every pair back to that doctrine so this module cannot silently
# invent a parallel Role-trigger authority.
ROLE_TRIGGER_MAP: dict[str, tuple[str, ...]] = {
    "complex_task": ("ATHENA",),
    "scope_split_required": ("ATHENA",),
    "multi_step_workflow": ("ATHENA",),
    "factual_claim": ("ARGOS",),
    "external_reference": ("ARGOS",),
    "source_required": ("ARGOS",),
    "evidence_gap": ("ARGOS",),
    "source_freshness_risk": ("ARGOS",),
    "provenance_unclear": ("ARGOS",),
    "memory_recall_requested": ("MNEMOSYNE",),
    "prior_decision_reuse": ("MNEMOSYNE",),
    "project_history_reuse": ("MNEMOSYNE",),
    "duplicate_or_supersession_risk": ("MNEMOSYNE",),
    "memory_candidate": ("MNEMOSYNE",),
    "memory_promotion": ("MNEMOSYNE", "THEMIS"),
    "approval_required": ("THEMIS",),
    "legal_or_professional_risk": ("THEMIS",),
    "external_effect": ("THEMIS",),
    "policy_conflict": ("THEMIS",),
    "liability_risk": ("THEMIS",),
    "unclear_output": ("APOLLO",),
    "narrative_or_editorial_work": ("APOLLO",),
    "delivery_quality_required": ("APOLLO",),
    "artifact_fabrication": ("HEPHAISTOS",),
    "external_transmission": ("IRIS",),
    "client_delivery": ("IRIS",),
    "public_output": ("IRIS",),
    "handoff_required": ("IRIS",),
    "recipient_specific_format": ("IRIS",),
}

# Compatibility aliases only. New callers should prefer `conditions` using the
# governed vocabulary above.
_LEGACY_FIELD_TO_CONDITION: dict[str, str] = {
    "source_required": "source_required",
    "evidence_gap": "evidence_gap",
    "prior_state_required": "project_history_reuse",
    "version_or_supersession_risk": "duplicate_or_supersession_risk",
    "professional_position": "legal_or_professional_risk",
    "financial_or_contractual_effect": "legal_or_professional_risk",
    "liability_risk": "liability_risk",
    "external_effect": "external_effect",
    "external_transmission": "external_transmission",
    "recipient_specific_output": "recipient_specific_format",
    "artifact_required": "artifact_fabrication",
    "memory_promotion_requested": "memory_promotion",
    "complex_task": "complex_task",
    "multi_step_workflow": "multi_step_workflow",
}

_MATERIAL_RECONSULT_CONDITIONS = (
    "source_required",
    "evidence_gap",
    "source_freshness_risk",
    "provenance_unclear",
    "project_history_reuse",
    "duplicate_or_supersession_risk",
    "legal_or_professional_risk",
    "liability_risk",
    "external_effect",
    "external_transmission",
    "memory_promotion",
    "approval_required",
    "policy_conflict",
)

_SOURCE_CONDITIONS = {
    "factual_claim",
    "external_reference",
    "source_required",
    "evidence_gap",
    "source_freshness_risk",
    "provenance_unclear",
}
_CONTINUITY_CONDITIONS = {
    "memory_recall_requested",
    "prior_decision_reuse",
    "project_history_reuse",
    "duplicate_or_supersession_risk",
    "memory_candidate",
}
_RISK_CONDITIONS = {
    "approval_required",
    "legal_or_professional_risk",
    "external_effect",
    "policy_conflict",
    "liability_risk",
    "memory_promotion",
}
_STRUCTURE_CONDITIONS = {"complex_task", "scope_split_required", "multi_step_workflow"}
_DELIVERY_CONDITIONS = {
    "external_transmission",
    "client_delivery",
    "public_output",
    "handoff_required",
    "recipient_specific_format",
}


def _observations(request: dict[str, Any]) -> dict[str, Any]:
    value = request.get("observations")
    return value if isinstance(value, dict) else {}


def _declared_conditions(request: dict[str, Any]) -> list[str]:
    """Collect governed conditions without inferring them from prose."""
    out: list[str] = []

    raw = request.get("conditions") or []
    if isinstance(raw, str):
        raw = [raw]
    if isinstance(raw, list):
        for item in raw:
            value = str(item)
            if value in ROLE_TRIGGER_MAP and value not in out:
                out.append(value)

    observations = _observations(request)
    for condition in ROLE_TRIGGER_MAP:
        if observations.get(condition) is True and condition not in out:
            out.append(condition)

    for field, condition in _LEGACY_FIELD_TO_CONDITION.items():
        value = observations.get(field, request.get(field))
        if value is True and condition not in out:
            out.append(condition)

    if request.get("transmission_requested") is True and "external_transmission" not in out:
        out.append("external_transmission")

    return out


def _viewpoints(conditions: list[str]) -> list[str]:
    roles: list[str] = []
    for condition in conditions:
        for role in ROLE_TRIGGER_MAP.get(condition, ()):
            if role not in roles:
                roles.append(role)
    return roles


def _pairs(value: Any) -> list[list[str]]:
    """Normalize a list of two-item relations; malformed candidates are ignored."""
    if not isinstance(value, list):
        return []
    out: list[list[str]] = []
    for item in value:
        if isinstance(item, (list, tuple)) and len(item) == 2:
            pair = [str(item[0]), str(item[1])]
            if pair not in out:
                out.append(pair)
    return out


def _groups(value: Any) -> list[list[str]]:
    """Normalize independent groups with at least two named members."""
    if not isinstance(value, list):
        return []
    out: list[list[str]] = []
    for item in value:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            group = [str(member) for member in item]
            if group not in out:
                out.append(group)
    return out


def _strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    return []


def _coordination(request: dict[str, Any]) -> dict[str, Any]:
    """Return bounded, non-persistent coordination relations supplied by caller."""
    raw = request.get("coordination")
    if not isinstance(raw, dict):
        return {}

    coordination: dict[str, Any] = {}
    requires = _pairs(raw.get("requires"))
    independent = _groups(raw.get("independent"))
    branch_on = _strings(raw.get("branch_on"))
    repeat_until = _strings(raw.get("repeat_until"))
    synthesize = bool(raw.get("synthesize", False))

    if requires:
        coordination["requires"] = requires
    if independent:
        coordination["independent"] = independent
    if synthesize:
        coordination["synthesize"] = True
    if branch_on:
        coordination["branch_on"] = branch_on
    if repeat_until:
        coordination["repeat_until"] = repeat_until
    return coordination


def _topology(coordination: dict[str, Any]) -> dict[str, Any] | None:
    """Derive an existing Task Contract topology from generic relations only."""
    if coordination.get("requires"):
        return {
            "suggested": "sequential_handoff",
            "reason": "an explicit dependency requires one state to precede another",
        }

    if coordination.get("branch_on"):
        return {
            "suggested": "router",
            "reason": "the next path depends on an explicit observed condition",
        }

    if coordination.get("independent") and coordination.get("synthesize"):
        return {
            "suggested": "fanout_extract_then_single_synthesis",
            "reason": "independent work may proceed separately before a shared synthesis",
        }

    if coordination.get("independent"):
        return {
            "suggested": "parallel_independent_workers",
            "reason": "explicitly independent work may proceed in parallel",
        }

    # repeat_until is a control condition, not an existing Task Contract topology.
    return None


def _derived_completion_requirements(conditions: list[str]) -> list[str]:
    """Fallback requirements derived from governed conditions."""
    required: list[str] = []
    if _STRUCTURE_CONDITIONS.intersection(conditions):
        required.append("scope_and_method_bounded")
    if _SOURCE_CONDITIONS.intersection(conditions):
        required.append("supporting_basis_qualified")
    if _CONTINUITY_CONDITIONS.intersection(conditions):
        required.append("current_state_qualified")
    if _RISK_CONDITIONS.intersection(conditions):
        required.append("consequence_boundary_reviewed")
    if _DELIVERY_CONDITIONS.intersection(conditions):
        required.append("delivery_boundary_qualified")
    return required


def _completion_requirements(request: dict[str, Any], conditions: list[str]) -> list[str]:
    """Prefer explicit acceptance conditions; otherwise use bounded fallbacks."""
    explicit = _strings(request.get("completion_requirements"))
    return explicit or _derived_completion_requirements(conditions)


def _effect_requested(request: dict[str, Any], conditions: list[str]) -> bool:
    observations = _observations(request)
    external = observations.get("external_effect", request.get("external_effect"))
    return bool(
        external is True
        or "external_transmission" in conditions
        or "memory_promotion" in conditions
        or request.get("writes_state") is True
        or observations.get("writes_state") is True
    )


def recommend_handling(request: dict[str, Any], classification: dict[str, Any]) -> dict[str, Any]:
    """Return the smallest progressive governance handling recommendation."""
    conditions = _declared_conditions(request)
    viewpoints = _viewpoints(conditions)
    coordination = _coordination(request)
    topology = _topology(coordination)
    completion_requirements = _completion_requirements(request, conditions)
    effect_requested = _effect_requested(request, conditions)
    conflict_detected = bool(
        request.get("conflict_detected") is True
        or _observations(request).get("conflict_detected") is True
        or _observations(request).get("contradiction_detected") is True
    )

    needs_consult = bool(
        viewpoints
        or completion_requirements
        or coordination
        or conflict_detected
        or classification.get("blocked_until_gate")
    )

    if classification.get("blocked_until_gate") and effect_requested:
        disposition = "GATE"
    elif needs_consult:
        disposition = "CONSULT"
    else:
        disposition = "PROCEED"

    constraints: list[str] = []
    if request.get("conditions") or request.get("observations") or coordination:
        constraints.append("declared_conditions_and_relations_are_candidates_not_truth")
    if _RISK_CONDITIONS.intersection(conditions):
        constraints.append("do_not_increase_claim_authority_without_support")
    if request.get("requested_transformation") in {"rewrite", "wording", "polish"}:
        constraints.append("preserve_claim_status_and_meaning")
    if classification.get("evidence_required"):
        constraints.append("retrieved_material_is_not_evidence_until_qualified")

    reconsult_if = [
        condition
        for condition in _MATERIAL_RECONSULT_CONDITIONS
        if condition not in conditions
    ]

    handling: dict[str, Any] = {
        "disposition": disposition,
        "conditions": conditions,
        "role_viewpoints": viewpoints,
        "completion_requirements": completion_requirements,
        "constraints": constraints,
        "reconsult_if": reconsult_if,
        "authority_note": (
            "Handling is policy guidance only. Conditions and coordination relations "
            "are candidate inputs, a viewpoint is not an agent, topology is not "
            "dispatch, completion is not approval, and Hermes remains the external executor."
        ),
    }

    if coordination:
        handling["coordination"] = coordination
    if topology is not None:
        handling["topology"] = topology
    if request.get("current_state") is not None:
        handling["current_state"] = request.get("current_state")
    if request.get("target_state") is not None:
        handling["target_state"] = request.get("target_state")
    if conflict_detected:
        handling["rite_candidate"] = "concordance_des_sources"
    if classification.get("blocked_until_gate"):
        handling["effect_gate"] = {
            "required_approval_ceiling": classification.get("required_approval_ceiling"),
            "required_before_effect": True,
            "effect_requested_now": effect_requested,
        }

    return handling
