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
    (EXAMPLES / "answer_status.example.yaml", SCHEMAS / "answer_status.schema.yaml"),
    (EXAMPLES / "policy_decision.example.yaml", SCHEMAS / "policy_decision.schema.yaml"),
    (EXAMPLES / "capability_passport.example.yaml", SCHEMAS / "capability_passport.schema.yaml"),
    (EXAMPLES / "shared_axes.example.yaml", SCHEMAS / "shared_axes.schema.yaml"),
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
