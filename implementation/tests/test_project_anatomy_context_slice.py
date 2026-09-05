from __future__ import annotations

import pytest

from mvp_vertical.project_anatomy_context_slice import (
    ProjectAnatomyContextError,
    build_object_context_slice,
    relation_semantics,
)


def _projection() -> dict:
    door_ref = {"entity_type": "stable_object", "entity_id": "OBJ-DOOR-01"}
    corridor_ref = {"entity_type": "stable_object", "entity_id": "OBJ-CORRIDOR-01"}
    office_ref = {"entity_type": "stable_object", "entity_id": "OBJ-OFFICE-01"}
    return {
        "project_ref": "project-context",
        "owner_revision": 7,
        "structure": {
            "objects": [
                {
                    "object_id": "OBJ-DOOR-01",
                    "object_family": "element",
                    "display_name": "Porte P01",
                    "internal_code": "P01",
                    "aliases": [],
                    "revision": 2,
                    "attribute_claims": [
                        {
                            "claim_type": "attribute_claim",
                            "claim_id": "claim-door-width",
                            "subject_ref": door_ref,
                            "attribute_key": "architecture.width",
                            "value": {"value_type": "number", "value": 0.90, "unit": "m"},
                            "proof_status": "accepted_as_support",
                            "source_representation_refs": ["rep-plan-p01"],
                            "phase_refs": ["PRO"],
                        }
                    ],
                    "relations": [
                        {
                            "claim_type": "relation_claim",
                            "claim_id": "rel-door-corridor",
                            "subject_ref": door_ref,
                            "relation_type": "spatial.adjacent_to",
                            "object_ref": corridor_ref,
                            "proof_status": "accepted_as_support",
                            "source_representation_refs": ["rep-plan-p01"],
                            "phase_refs": ["PRO"],
                        },
                        {
                            "claim_type": "relation_claim",
                            "claim_id": "rel-door-office",
                            "subject_ref": door_ref,
                            "relation_type": "architecture.opens_to",
                            "object_ref": office_ref,
                            "proof_status": "candidate",
                            "source_representation_refs": ["rep-plan-p01"],
                            "phase_refs": ["PRO"],
                        },
                    ],
                    "source_representation_refs": ["rep-plan-p01"],
                    "phase_refs": ["PRO"],
                    "attention_claim_refs": ["rel-door-office"],
                },
                {
                    "object_id": "OBJ-CORRIDOR-01",
                    "object_family": "spatial",
                    "display_name": "Circulation RDC",
                    "revision": 1,
                    "attribute_claims": [],
                    "relations": [],
                    "source_representation_refs": ["rep-plan-p01"],
                    "phase_refs": ["PRO"],
                    "attention_claim_refs": [],
                },
                {
                    "object_id": "OBJ-OFFICE-01",
                    "object_family": "spatial",
                    "display_name": "Bureau",
                    "revision": 1,
                    "attribute_claims": [],
                    "relations": [],
                    "source_representation_refs": ["rep-plan-p01"],
                    "phase_refs": ["PRO"],
                    "attention_claim_refs": [],
                },
            ]
        },
    }


def _requirements() -> list[dict]:
    return [
        {
            "requirement_id": "req-reg-door",
            "source": {
                "source_type": "regulation",
                "source_ref": "regulation://accessibility/article-x",
                "source_artifact_ref": "doc-reg-accessibility",
            },
            "requirement_kind": "attribute",
            "target": {
                "entity_ref": {"entity_type": "stable_object", "entity_id": "OBJ-DOOR-01"}
            },
            "constraint": {
                "operator": "min",
                "attribute_key": "architecture.width",
                "expected_value": {"value_type": "number", "value": 0.90, "unit": "m"},
            },
            "source_authority": "project_working_document",
            "proof_status": "accepted_as_support",
        },
        {
            "requirement_id": "req-tech-elements",
            "source": {
                "source_type": "technical_brief",
                "source_ref": "cctp://lot-menuiseries/article-3",
            },
            "requirement_kind": "existence",
            "target": {"selector": {"object_family": "element"}},
            "constraint": {"operator": "must_exist"},
            "source_authority": "project_working_document",
            "proof_status": "accepted_as_support",
        },
        {
            "requirement_id": "req-contract-width",
            "source": {
                "source_type": "contract",
                "source_ref": "contract://market/article-width",
            },
            "requirement_kind": "attribute",
            "target": {"selector": {"attribute_key": "architecture.width"}},
            "constraint": {
                "operator": "min",
                "attribute_key": "architecture.width",
                "expected_value": {"value_type": "number", "value": 0.88, "unit": "m"},
            },
            "source_authority": "project_working_document",
            "proof_status": "accepted_as_support",
        },
        {
            "requirement_id": "req-classification-unresolved",
            "source": {
                "source_type": "regulation",
                "source_ref": "regulation://fire/article-y",
            },
            "requirement_kind": "classification",
            "target": {
                "selector": {
                    "classification_scheme": "classification.fire_erp",
                    "classification_value": "emergency_exit",
                }
            },
            "constraint": {"operator": "equals"},
            "source_authority": "project_working_document",
            "proof_status": "candidate",
        },
    ]


def test_relation_semantics_explain_without_creating_claims() -> None:
    adjacency = relation_semantics("spatial.adjacent_to")
    assert adjacency["symmetric"] is True
    assert adjacency["transitive"] is False
    assert adjacency["creates_relation_claim"] is False
    assert adjacency["authority_effect"] is False

    unknown = relation_semantics("architecture.frames_view_to")
    assert unknown["status"] == "opaque_unregistered"
    assert unknown["creates_relation_claim"] is False


def test_same_object_can_carry_regulatory_technical_and_contract_requirements() -> None:
    result = build_object_context_slice(
        _projection(),
        object_id="OBJ-DOOR-01",
        admitted_object_ids=["OBJ-DOOR-01"],
        requirements=_requirements(),
    )
    matched = {row["requirement"]["requirement_id"]: row for row in result["requirements"]}
    assert set(matched) == {"req-reg-door", "req-tech-elements", "req-contract-width"}
    assert matched["req-reg-door"]["match_basis"] == "exact_entity_ref"
    assert matched["req-tech-elements"]["match_basis"] == "deterministic_selector"
    assert matched["req-contract-width"]["match_basis"] == "deterministic_selector"
    assert "doc-reg-accessibility" in result["source_refs"]
    assert result["authority"]["resolves_compliance"] is False


def test_classification_selector_remains_unresolved_without_explicit_resolution() -> None:
    result = build_object_context_slice(
        _projection(),
        object_id="OBJ-DOOR-01",
        requirements=_requirements(),
    )
    unresolved = {
        row["requirement"]["requirement_id"]: row["reason"]
        for row in result["unresolved_requirement_selectors"]
    }
    assert unresolved == {
        "req-classification-unresolved": "classification_selector_requires_explicit_resolution"
    }


def test_relation_neighbour_identity_does_not_widen_context_implicitly() -> None:
    result = build_object_context_slice(
        _projection(),
        object_id="OBJ-DOOR-01",
        admitted_object_ids=["OBJ-DOOR-01", "OBJ-CORRIDOR-01"],
    )
    assert {row["object_id"] for row in result["neighbours"]} == {"OBJ-CORRIDOR-01"}
    assert result["withheld_neighbour_refs"] == [
        {
            "entity_ref": {"entity_type": "stable_object", "entity_id": "OBJ-OFFICE-01"},
            "reason": "outside_explicitly_admitted_object_scope",
        }
    ]
    assert result["scope"]["implicit_traversal_performed"] is False
    assert result["scope"]["global_search_performed"] is False


def test_root_must_be_explicitly_admitted() -> None:
    with pytest.raises(ProjectAnatomyContextError, match="outside the admitted"):
        build_object_context_slice(
            _projection(),
            object_id="OBJ-DOOR-01",
            admitted_object_ids=["OBJ-CORRIDOR-01"],
        )


def test_context_slice_never_exposes_compliance_or_decision_authority() -> None:
    result = build_object_context_slice(
        _projection(),
        object_id="OBJ-DOOR-01",
        requirements=_requirements(),
    )
    assert result["authority"] == {
        "projection_only": True,
        "creates_project_fact": False,
        "creates_relation_claim": False,
        "resolves_compliance": False,
        "is_evidence": False,
        "is_decision": False,
        "authorizes_effect": False,
    }
    assert "compliant" not in result
    assert "current_value" not in result
