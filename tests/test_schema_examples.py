from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"


EXAMPLE_SCHEMA_PAIRS = [
    (EXAMPLES / "task_contract.example.yaml", SCHEMAS / "task_contract.schema.yaml"),
    (EXAMPLES / "evidence_pack.example.yaml", SCHEMAS / "evidence_pack.schema.yaml"),
    (EXAMPLES / "register_candidate.example.yaml", SCHEMAS / "register_candidate.schema.yaml"),
    (EXAMPLES / "register_link.example.yaml", SCHEMAS / "register_link.schema.yaml"),
    (EXAMPLES / "impact_review.example.yaml", SCHEMAS / "impact_review.schema.yaml"),
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
]


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    assert isinstance(data, dict), f"{path} must contain a YAML mapping"
    return data


def test_schema_examples_validate() -> None:
    for example_path, schema_path in EXAMPLE_SCHEMA_PAIRS:
        example = load_yaml(example_path)
        schema = load_yaml(schema_path)
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.validate(instance=example, schema=schema)


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
