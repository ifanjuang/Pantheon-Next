"""Progressive request-handling projection.

This module turns caller-provided governed conditions plus the K/V/C
classification into the smallest useful governance handling recommendation.
It does not understand raw natural language, execute work, dispatch roles,
run a workflow, authorize an effect, or approve an output.

The preferred input is a small list of existing ROLE_ACTIVATION conditions.
Legacy task-specific fields remain accepted only as compatibility aliases.
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
# governed vocabulary above. This keeps domain-specific semantics out of the
# handling core while preserving existing request fields during migration.
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


def _topology(conditions: list[str], viewpoints: list[str]) -> dict[str, Any] | None:
    """Recommend an existing topology only when a dependency is material."""
    if len(viewpoints) <= 1:
        return None

    source = bool(_SOURCE_CONDITIONS.intersection(conditions))
    continuity = bool(_CONTINUITY_CONDITIONS.intersection(conditions))
    risk = bool(_RISK_CONDITIONS.intersection(conditions))

    if source and risk:
        return {
            "suggested": "sequential_handoff",
            "reason": "qualify the supporting basis before relying on a consequential judgement",
            "ordered_viewpoints": [
                role for role in ("ARGOS", "MNEMOSYNE", "THEMIS") if role in viewpoints
            ],
        }

    if source and continuity:
        return {
            "suggested": "fanout_extract_then_single_synthesis",
            "reason": "source state and continuity/currentness can be qualified independently before synthesis",
            "parallel_viewpoints": [
                role for role in ("ARGOS", "MNEMOSYNE") if role in viewpoints
            ],
        }

    return {
        "suggested": "parallel_independent_workers",
        "reason": "several viewpoints are relevant without a proven ordering dependency",
        "parallel_viewpoints": viewpoints,
    }


def _completion_requirements(conditions: list[str]) -> list[str]:
    """Return generic observable conditions for the next legitimate transition."""
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
    topology = _topology(conditions, viewpoints)
    completion_requirements = _completion_requirements(conditions)
    effect_requested = _effect_requested(request, conditions)
    conflict_detected = bool(
        request.get("conflict_detected") is True
        or _observations(request).get("conflict_detected") is True
        or _observations(request).get("contradiction_detected") is True
    )

    if classification.get("blocked_until_gate") and effect_requested:
        disposition = "GATE"
    elif viewpoints or completion_requirements or conflict_detected or classification.get("blocked_until_gate"):
        disposition = "CONSULT"
    else:
        disposition = "PROCEED"

    constraints: list[str] = []
    if request.get("conditions") or request.get("observations"):
        constraints.append("declared_conditions_are_candidates_not_truth")
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
            "Handling is policy guidance only. A condition is candidate input, a "
            "viewpoint is not an agent, topology is not dispatch, completion is not "
            "approval, and Hermes remains the external executor."
        ),
    }

    if topology is not None:
        handling["topology"] = topology
    if conflict_detected:
        handling["rite_candidate"] = "concordance_des_sources"
    if classification.get("blocked_until_gate"):
        handling["effect_gate"] = {
            "required_approval_ceiling": classification.get("required_approval_ceiling"),
            "required_before_effect": True,
            "effect_requested_now": effect_requested,
        }

    return handling
