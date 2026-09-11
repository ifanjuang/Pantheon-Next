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


_ROLE_TRIGGER_MAP: dict[str, tuple[str, ...]] = {
    "complex_task": ("ATHENA",),
    "multi_step_workflow": ("ATHENA",),
    "source_required": ("ARGOS",),
    "evidence_gap": ("ARGOS",),
    "contradiction_detected": ("ARGOS",),
    "prior_state_required": ("MNEMOSYNE",),
    "version_or_supersession_risk": ("MNEMOSYNE",),
    "professional_position": ("THEMIS",),
    "financial_or_contractual_effect": ("THEMIS",),
    "liability_risk": ("THEMIS",),
    "external_effect": ("THEMIS",),
    "external_transmission": ("IRIS",),
    "recipient_specific_output": ("IRIS",),
    "artifact_required": ("HEPHAISTOS",),
}

_MATERIAL_RECONSULT_TRIGGERS = (
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


def _triggers(request: dict[str, Any]) -> list[str]:
    observations = _candidate_observations(request)
    detected: list[str] = []

    for trigger in _ROLE_TRIGGER_MAP:
        if _flag(request, observations, trigger):
            detected.append(trigger)

    external = observations.get("external_effect", request.get("external_effect"))
    if external is True and "external_effect" not in detected:
        detected.append("external_effect")
    if request.get("transmission_requested") is True and "external_transmission" not in detected:
        detected.append("external_transmission")

    if request.get("memory_promotion_requested") is True:
        detected.append("memory_promotion_requested")
    if request.get("writes_state") is True:
        detected.append("writes_state")

    return list(dict.fromkeys(detected))


def _viewpoints(triggers: list[str]) -> list[str]:
    roles: list[str] = []
    for trigger in triggers:
        for role in _ROLE_TRIGGER_MAP.get(trigger, ()):
            if role not in roles:
                roles.append(role)
    return roles


def _topology(triggers: list[str], viewpoints: list[str]) -> dict[str, Any] | None:
    """Recommend an existing Task Contract topology only when useful."""
    if len(viewpoints) <= 1:
        return None

    source_basis = any(t in triggers for t in ("source_required", "evidence_gap"))
    professional_judgement = any(
        t in triggers
        for t in ("professional_position", "financial_or_contractual_effect", "liability_risk")
    )
    prior_state = any(
        t in triggers for t in ("prior_state_required", "version_or_supersession_risk")
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


def _next_state(triggers: list[str]) -> dict[str, Any] | None:
    """Name only the next governed state that must be established."""
    source_basis = any(t in triggers for t in ("source_required", "evidence_gap"))
    prior_state = any(t in triggers for t in ("prior_state_required", "version_or_supersession_risk"))
    professional = any(
        t in triggers
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


def _consequential_effect_requested(request: dict[str, Any], triggers: list[str]) -> bool:
    """Separate candidate review from the effect that actually needs a gate."""
    observations = _candidate_observations(request)
    external = observations.get("external_effect", request.get("external_effect"))
    return bool(
        external is True
        or "external_transmission" in triggers
        or "memory_promotion_requested" in triggers
        or "writes_state" in triggers
    )


def recommend_handling(request: dict[str, Any], classification: dict[str, Any]) -> dict[str, Any]:
    """Return the smallest progressive governance handling recommendation.

    The function deliberately does not parse raw prose. It consumes explicit
    request fields and caller-provided semantic observations, then maps them to
    existing Role Activation and Task Contract topology vocabulary.
    """
    triggers = _triggers(request)
    viewpoints = _viewpoints(triggers)
    topology = _topology(triggers, viewpoints)
    next_state = _next_state(triggers)
    effect_requested = _consequential_effect_requested(request, triggers)

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
        t in triggers
        for t in ("professional_position", "financial_or_contractual_effect", "liability_risk")
    ):
        constraints.append("do_not_strengthen_unverified_professional_claim")
    if request.get("requested_transformation") in {"rewrite", "wording", "polish"}:
        constraints.append("preserve_claim_status_and_meaning")
    if classification.get("evidence_required"):
        constraints.append("retrieved_material_is_not_evidence_until_qualified")

    reconsult_if = [
        trigger
        for trigger in _MATERIAL_RECONSULT_TRIGGERS
        if trigger not in triggers
    ]

    handling: dict[str, Any] = {
        "disposition": disposition,
        "triggers": triggers,
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
    if "contradiction_detected" in triggers:
        handling["rite_candidate"] = "concordance_des_sources"
    if classification.get("blocked_until_gate"):
        handling["effect_gate"] = {
            "required_approval_ceiling": classification.get("required_approval_ceiling"),
            "required_before_effect": True,
            "effect_requested_now": effect_requested,
        }

    return handling
