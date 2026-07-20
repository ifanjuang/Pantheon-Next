import copy
from pathlib import Path

import jsonschema
import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"


EXAMPLE_SCHEMA_PAIRS = [
    (EXAMPLES / "document_knowledge_slice.example.yaml", SCHEMAS / "document_knowledge_slice.schema.yaml"),
    (EXAMPLES / "work_issue_slice.example.yaml", SCHEMAS / "work_issue_slice.schema.yaml"),
    (EXAMPLES / "task_contract.example.yaml", SCHEMAS / "task_contract.schema.yaml"),
    (EXAMPLES / "evidence_pack.example.yaml", SCHEMAS / "evidence_pack.schema.yaml"),
    (EXAMPLES / "register_candidate.example.yaml", SCHEMAS / "register_candidate.schema.yaml"),
    (EXAMPLES / "register_link.example.yaml", SCHEMAS / "register_link.schema.yaml"),
    (EXAMPLES / "impact_review.example.yaml", SCHEMAS / "impact_review.schema.yaml"),
    (EXAMPLES / "mvp_governed_loop_objects.example.yaml", SCHEMAS / "mvp_governed_loop_objects.schema.yaml"),
    (EXAMPLES / "answer_status.example.yaml", SCHEMAS / "answer_status.schema.yaml"),
    (EXAMPLES / "policy_decision.example.yaml", SCHEMAS / "policy_decision.schema.yaml"),
    (EXAMPLES / "capability_passport.example.yaml", SCHEMAS / "capability_passport.schema.yaml"),
    (EXAMPLES / "module_manifest.example.yaml", SCHEMAS / "module_manifest.schema.yaml"),
    (EXAMPLES / "shared_axes.example.yaml", SCHEMAS / "shared_axes.schema.yaml"),
    (EXAMPLES / "architecture-proof-register/shared.example.yaml", SCHEMAS / "architecture-proof-register/shared.schema.yaml"),
    (EXAMPLES / "architecture-proof-register/document_family.example.yaml", SCHEMAS / "architecture-proof-register/document_family.schema.yaml"),
    (EXAMPLES / "architecture-proof-register/indexed_document_version.example.yaml", SCHEMAS / "architecture-proof-register/indexed_document_version.schema.yaml"),
    (EXAMPLES / "architecture-proof-register/version_event.example.yaml", SCHEMAS / "architecture-proof-register/version_event.schema.yaml"),
    (EXAMPLES / "architecture-proof-register/proof_entry.example.yaml", SCHEMAS / "architecture-proof-register/proof_entry.schema.yaml"),
    (EXAMPLES / "architecture-proof-register/review_trigger.example.yaml", SCHEMAS / "architecture-proof-register/review_trigger.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/shared.example.yaml", SCHEMAS / "architecture-project-understanding/shared.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/stable_object.example.yaml", SCHEMAS / "architecture-project-understanding/stable_object.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/attribute_claim.example.yaml", SCHEMAS / "architecture-project-understanding/attribute_claim.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/calibration.example.yaml", SCHEMAS / "architecture-project-understanding/calibration.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/derivation.example.yaml", SCHEMAS / "architecture-project-understanding/derivation.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/evidence.example.yaml", SCHEMAS / "architecture-project-understanding/evidence.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/doubt.example.yaml", SCHEMAS / "architecture-project-understanding/doubt.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/contradiction.example.yaml", SCHEMAS / "architecture-project-understanding/contradiction.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/human_override.example.yaml", SCHEMAS / "architecture-project-understanding/human_override.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/canonization.example.yaml", SCHEMAS / "architecture-project-understanding/canonization.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/program.example.yaml", SCHEMAS / "architecture-project-understanding/program.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/requirement.example.yaml", SCHEMAS / "architecture-project-understanding/requirement.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/classification.example.yaml", SCHEMAS / "architecture-project-understanding/classification.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/classification_scheme.example.yaml", SCHEMAS / "architecture-project-understanding/classification_scheme.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/space_group.example.yaml", SCHEMAS / "architecture-project-understanding/space_group.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/program_change.example.yaml", SCHEMAS / "architecture-project-understanding/program_change.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/deviation.example.yaml", SCHEMAS / "architecture-project-understanding/deviation.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/spatial_node.example.yaml", SCHEMAS / "architecture-project-understanding/spatial_node.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/object_identity.example.yaml", SCHEMAS / "architecture-project-understanding/object_identity.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/object_relation.example.yaml", SCHEMAS / "architecture-project-understanding/object_relation.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/object_group.example.yaml", SCHEMAS / "architecture-project-understanding/object_group.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/property_set.example.yaml", SCHEMAS / "architecture-project-understanding/property_set.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/instance_override.example.yaml", SCHEMAS / "architecture-project-understanding/instance_override.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/object_note.example.yaml", SCHEMAS / "architecture-project-understanding/object_note.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/phase_state.example.yaml", SCHEMAS / "architecture-project-understanding/phase_state.schema.yaml"),
    (EXAMPLES / "architecture-project-understanding/analysis_context_candidate.example.yaml", SCHEMAS / "architecture-project-understanding/analysis_context_candidate.schema.yaml"),
    (EXAMPLES / "role_signal.example.yaml", SCHEMAS / "role_signal.schema.yaml"),
    (EXAMPLES / "workflow_manifest.example.yaml", SCHEMAS / "workflow_manifest.schema.yaml"),
    (EXAMPLES / "skill_manifest.example.yaml", SCHEMAS / "skill_manifest.schema.yaml"),
    (EXAMPLES / "context_pack.example.yaml", SCHEMAS / "context_pack.schema.yaml"),
    (EXAMPLES / "install_verification_evidence.example.yaml", SCHEMAS / "install_verification_evidence.schema.yaml"),
    (EXAMPLES / "observability_evidence.example.yaml", SCHEMAS / "observability_evidence.schema.yaml"),
    (EXAMPLES / "backup_evidence.example.yaml", SCHEMAS / "backup_evidence.schema.yaml"),
    (EXAMPLES / "exposure_evidence.example.yaml", SCHEMAS / "exposure_evidence.schema.yaml"),
    (EXAMPLES / "update_evidence.example.yaml", SCHEMAS / "update_evidence.schema.yaml"),
    (EXAMPLES / "verification_preset.example.yaml", SCHEMAS / "verification_preset.schema.yaml"),
]


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    assert isinstance(data, dict), f"{path} must contain a YAML mapping"
    return data


def _apu_registry():
    """Registry exposing the architecture-project-understanding shared.schema.yaml
    under its bare filename, so factored cross-file refs resolve (issue #169)."""
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    shared = SCHEMAS / "architecture-project-understanding" / "shared.schema.yaml"
    resource = Resource.from_contents(load_yaml(shared), default_specification=DRAFT202012)
    return Registry().with_resource(uri="shared.schema.yaml", resource=resource)


def test_schema_examples_validate() -> None:
    registry = _apu_registry()
    for example_path, schema_path in EXAMPLE_SCHEMA_PAIRS:
        example = load_yaml(example_path)
        schema = load_yaml(schema_path)
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema, registry=registry)
        validator.validate(example)


def test_evidence_topology_fields_remain_documentary() -> None:
    task_contract_schema = load_yaml(SCHEMAS / "task_contract.schema.yaml")
    evidence_pack_schema = load_yaml(SCHEMAS / "evidence_pack.schema.yaml")
    workflow_manifest_schema = load_yaml(SCHEMAS / "workflow_manifest.schema.yaml")

    assert "reasoning_topology" in task_contract_schema["properties"]
    assert "evidence_items" in evidence_pack_schema["properties"]
    assert "handoff_artifacts" in evidence_pack_schema["properties"]
    assert "reasoning_topology_record" in evidence_pack_schema["properties"]
    assert "reasoning_topology_requirements" in workflow_manifest_schema["properties"]
    assert "evidence_item_requirements" in workflow_manifest_schema["properties"]
    assert "handoff_artifact_requirements" in workflow_manifest_schema["properties"]

    assert task_contract_schema["x-boundary"]["topology_dispatch"] is False
    assert evidence_pack_schema["x-boundary"]["topology_dispatch"] is False
    assert evidence_pack_schema["x-boundary"]["hidden_chain_of_thought_archive"] is False
    assert workflow_manifest_schema["x-boundary"]["topology_dispatch"] is False
    assert workflow_manifest_schema["x-boundary"]["hidden_chain_of_thought_archive"] is False


def test_evidence_items_support_optional_claim_status() -> None:
    evidence_pack_schema = load_yaml(SCHEMAS / "evidence_pack.schema.yaml")
    evidence_item_properties = evidence_pack_schema["properties"]["evidence_items"]["items"]["properties"]

    assert "claim_status" in evidence_item_properties
    assert evidence_item_properties["claim_status"]["enum"] == [
        "supported",
        "weak",
        "unverified",
        "contradicted",
        "out_of_scope",
    ]


def test_module_manifest_remains_declaration_only() -> None:
    module_manifest_schema = load_yaml(SCHEMAS / "module_manifest.schema.yaml")

    assert "activation" in module_manifest_schema["properties"]
    assert "task_authorization" in module_manifest_schema["properties"]
    assert "interface" in module_manifest_schema["properties"]
    assert "governance" in module_manifest_schema["properties"]
    assert "composition" in module_manifest_schema["properties"]
    assert module_manifest_schema["x-boundary"]["runtime_execution"] is False
    assert module_manifest_schema["x-boundary"]["memory_promotion"] is False
    assert module_manifest_schema["x-boundary"]["automatic_authorization"] is False


def _workflow_validator():
    schema = load_yaml(SCHEMAS / "workflow_manifest.schema.yaml")
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema, registry=_apu_registry())


def test_governed_composition_signature_negatives() -> None:
    """A capability_step must carry its full governance signature; an incomplete
    or unknown-property step is rejected (issue #218, task 1)."""
    validator = _workflow_validator()
    example = load_yaml(EXAMPLES / "workflow_manifest.example.yaml")
    validator.validate(example)  # the shipped example is complete

    for missing in (
        "declared_scope",
        "forbidden_scope",
        "required_task_contract",
        "evidence_pack_shape",
        "approval_ceiling",
        "register_behavior",
        "risk_class",
        "refusal_tests",
    ):
        broken = copy.deepcopy(example)
        del broken["governed_composition"]["capability_steps"][0][missing]
        with pytest.raises(jsonschema.ValidationError):
            validator.validate(broken)

    unknown = copy.deepcopy(example)
    unknown["governed_composition"]["capability_steps"][0]["surprise_field"] = "no"
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(unknown)


def test_governed_composition_required_evidence_needs_v_and_e() -> None:
    """When post_execution_evidence.required is true, answer_verification (V) and
    probative_certainty (E) are mandatory; when it is false they may be omitted
    (issue #218, task 2)."""
    validator = _workflow_validator()
    example = load_yaml(EXAMPLES / "workflow_manifest.example.yaml")

    for missing in ("answer_verification", "probative_certainty"):
        broken = copy.deepcopy(example)
        peg = broken["governed_composition"]["gates"]["post_execution_evidence"]
        assert peg["required"] is True
        del peg[missing]
        with pytest.raises(jsonschema.ValidationError):
            validator.validate(broken)

    # required=false: V and E may be omitted (positive control, must not raise)
    not_required = copy.deepcopy(example)
    peg = not_required["governed_composition"]["gates"]["post_execution_evidence"]
    peg["required"] = False
    peg.pop("answer_verification", None)
    peg.pop("probative_certainty", None)
    validator.validate(not_required)


def test_governed_composition_gate_decision_enum() -> None:
    """The pre-execution gate decision is a closed enum (issue #218, task 3)."""
    validator = _workflow_validator()
    example = load_yaml(EXAMPLES / "workflow_manifest.example.yaml")
    bad = copy.deepcopy(example)
    bad["governed_composition"]["gates"]["pre_execution_eligibility"]["decision"] = "maybe"
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(bad)
