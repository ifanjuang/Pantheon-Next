"""Progressive request-handling projection.

This module turns caller-provided request observations plus the governed K/V/C
classification into the smallest useful governance handling recommendation.
It does not understand raw natural language, execute work, dispatch roles,
run a workflow, authorize an effect, or approve an output.

Hermes (or another admitted caller) may provide semantic observations as
candidates. Pantheon qualifies their governance consequence. Observations are
not truth, role viewpoints are not agents, and a topology recommendation is
not runtime dispatch.
"""

from __future__ import annotations

from typing import Any


# This is the implemented subset of ROLE_ACTIVATION.md mandatory_role_triggers.
# Tests bind every pair back to that governed doctrine so this projection cannot
# silently invent a parallel Role-trigger vocabulary.
ROLE_TRIGGER_MAP: dict[str, tuple[str, ...]] = {
    "complex_task": ("ATHENA",),
    "multi_step_workflow": ("ATHENA",),
    "source_required": ("ARGOS",),
    "evidence_gap": ("ARGOS",),
    "project_history_reuse": ("MNEMOSYNE",),
    "duplicate_or_supersession_risk": ("MNEMOSYNE",),
    "memory_promotion": ("MNEMOSYNE", "THEMIS"),
    "legal_or_professional_risk": ("THEMIS",),
    "liability_risk": ("THEMIS",),
    "external_effect": ("THEMIS",),
    "external_transmission": ("IRIS",),
    "recipient_specific_format": ("IRIS",),
    "artifact_fabrication": ("HEPHAISTOS",),
}

# Semantic intake uses task-facing conditions. They are normalized onto the
# existing Role Activation trigger vocabulary before a viewpoint is projected.
_SEMANTIC_TO_GOVERNANCE_TRIGGERS: dict[str, tuple[str, ...]] = {
    "complex_task": ("complex_task",),
    "multi_step_workflow": ("multi_step_workflow",),
    "source_required": ("source_required",),
    "evidence_gap": ("evidence_gap",),
    "contradiction_detected": ("evidence_gap",),
    "prior_state_required": ("project_history_reuse",),
    "version_or_supersession_risk": ("duplicate_or_supersession_risk",),
    "professional_position": ("legal_or_professional_risk",),
    "financial_or_contractual_effect": ("legal_or_professional_risk",),
    "liability_risk": ("liability_risk",),
    "external_effect": ("external_effect",),
    "external_transmission": ("external_transmission",),
    "recipient_specific_output": ("recipient_specific_format",),
    "artifact_required": ("artifact_fabrication",),
    "memory_promotion_requested": ("memory_promotion",),
}

_MATERIAL_RECONSULT_CONDITIONS = (
    "contradiction_detected",
    "source_required",
    "evidence_gap",
    "professional_position",
    "financial_or_contractual_effect",
    "liability_risk",
    "external_effect",
    "external_transmission",
    "memory_promotion_requested",
    "writes_state",
)


def _candidate_observations(request: dict[str, Any]) -> dict[str, Any]:
    observations = request.get("observations")
    return observations if isinstance(observations, dict) else {}


def _flag(request: dict[str, Any], observations: dict[str, Any], name: str) -> bool:
    """Read one candidate semantic flag without inferring it from prose."""
    if name in observations:
        return observations.get(name) is True
    return request.get(name) is True


def _observed_conditions(request: dict[str, Any]) -> list[str]:
    observations = _candidate_observations(request)
    detected: list[str] = []

    for condition in _SEMANTIC_TO_GOVERNANCE_TRIGGERS:
        if _flag(request, observations, condition):
            detected.append(condition)

    external = observations.get("external_effect", request.get("external_effect"))
    if external is True and "external_effect" not in detected:
        detected.append("external_effect")

    transmission = _flag(request, observations, "transmission_requested")
    if transmission and "external_transmission" not in detected:
        detected.append("external_transmission")

    if _flag(request, observations, "writes_state"):
        detected.append("writes_state")

    return list(dict.fromkeys(detected))


def _governance_triggers(conditions: list[str]) -> list[str]:
    triggers: list[str] = []
    for condition in conditions:
        for trigger in _SEMANTIC_TO_GOVERNANCE_TRIGGERS.get(condition, ()):
            if trigger not in triggers:
                triggers.append(trigger)
    return triggers


def _viewpoints(governance_triggers: list[str]) -> list[str]:
    roles: list[str] = []
    for trigger in governance_triggers:
        for role in ROLE_TRIGGER_MAP.get(trigger, ()):
            if role not in roles:
                roles.append(role)
    return roles


def _topology(conditions: list[str], viewpoints: list[str]) -> dict[str, Any] | None:
    """Recommend an existing Task Contract topology only when useful."""
    if len(viewpoints) <= 1:
        return None

    source_basis = any(t in conditions for t in ("source_required", "evidence_gap"))
    professional_judgement = any(
        t in conditions
        for t in ("professional_position", "financial_or_contractual_effect", "liability_risk")
    )
    prior_state = any(
        t in conditions for t in ("prior_state_required", "version_or_supersession_risk")
    )

    if source_basis and professional_judgement:
        return {
            "suggested": "sequential_handoff",
            "reason": "establish source/evidence basis before consequential professional judgement",
            "ordered_viewpoints": [role for role in ("ARGOS", "MNEMOSYNE", "THEMIS") if role in viewpoints],
        }

    if source_basis and prior_state:
        return {
            "suggested": "fanout_extract_then_single_synthesis",
            "reason": "source qualification and prior-state/currentness can be established independently before synthesis",
            "parallel_viewpoints": [role for role in ("ARGOS", "MNEMOSYNE") if role in viewpoints],
        }

    return {
        "suggested": "parallel_independent_workers",
        "reason": "several governance viewpoints may review the same current state without a proven dependency",
        "parallel_viewpoints": viewpoints,
    }


def _next_state(conditions: list[str]) -> dict[str, Any] | None:
    """Name only the next governed state that must be established."""
    source_basis = any(t in conditions for t in ("source_required", "evidence_gap"))
    prior_state = any(
        t in conditions for t in ("prior_state_required", "version_or_supersession_risk")
    )
    professional = any(
        t in conditions
        for t in ("professional_position", "financial_or_contractual_effect", "liability_risk")
    )

    if source_basis:
        required = ["applicable_source_basis_qualified"]
        if prior_state:
            required.append("current_or_superseded_state_qualified")
        return {
            "purpose": "establish_factual_basis",
            "completion_requires": required,
        }

    if prior_state:
        return {
            "purpose": "establish_current_state",
            "completion_requires": ["current_or_superseded_state_qualified"],
        }

    if professional:
        return {
            "purpose": "assess_professional_consequence",
            "completion_requires": ["professional_boundary_reviewed"],
        }

    return None


def _consequential_effect_requested(request: dict[str, Any], conditions: list[str]) -> bool:
    """Separate candidate review from the effect that actually needs a gate."""
    observations = _candidate_observations(request)
    external = observations.get("external_effect", request.get("external_effect"))
    return bool(
        external is True
        or "external_transmission" in conditions
        or "memory_promotion_requested" in conditions
        or "writes_state" in conditions
    )


def recommend_handling(request: dict[str, Any], classification: dict[str, Any]) -> dict[str, Any]:
    """Return the smallest progressive governance handling recommendation.

    The function deliberately does not parse raw prose. It consumes explicit
    request fields and caller-provided semantic observations, normalizes them to
    existing Role Activation triggers, then reuses existing Task Contract
    topology vocabulary when coordination is materially needed.
    """
    conditions = _observed_conditions(request)
    governance_triggers = _governance_triggers(conditions)
    viewpoints = _viewpoints(governance_triggers)
    topology = _topology(conditions, viewpoints)
    next_state = _next_state(conditions)
    effect_requested = _consequential_effect_requested(request, conditions)

    if classification.get("blocked_until_gate") and effect_requested:
        disposition = "GATE"
    elif viewpoints or next_state or classification.get("blocked_until_gate"):
        # K4 candidate work may still need consultation before any effect is
        # attempted. The gate constrains the effect, not the prior analysis.
        disposition = "CONSULT"
    else:
        disposition = "PROCEED"

    constraints: list[str] = []
    if request.get("observations"):
        constraints.append("semantic_observations_are_candidates_not_truth")
    if any(
        t in conditions
        for t in ("professional_position", "financial_or_contractual_effect", "liability_risk")
    ):
        constraints.append("do_not_strengthen_unverified_professional_claim")
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
        "observed_conditions": conditions,
        "governance_triggers": governance_triggers,
        "role_viewpoints": viewpoints,
        "constraints": constraints,
        "reconsult_if": reconsult_if,
        "authority_note": (
            "Handling is policy guidance only. A viewpoint is not an agent, a topology "
            "is not dispatch, phase completion is not approval, and Hermes remains the "
            "external executor inside the admitted boundary."
        ),
    }

    if topology is not None:
        handling["topology"] = topology
    if next_state is not None:
        handling["next_state"] = next_state
    if "contradiction_detected" in conditions:
        handling["rite_candidate"] = "concordance_des_sources"
    if classification.get("blocked_until_gate"):
        handling["effect_gate"] = {
            "required_approval_ceiling": classification.get("required_approval_ceiling"),
            "required_before_effect": True,
            "effect_requested_now": effect_requested,
        }

    return handling
