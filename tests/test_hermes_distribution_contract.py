from __future__ import annotations

from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTION = ROOT / "templates" / "hermes" / "distribution"
SCHEMA = DISTRIBUTION / "distribution-lock.schema.yaml"
EXAMPLE = DISTRIBUTION / "distribution-lock.example.yaml"


def _load(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_distribution_example_validates_without_creating_authority() -> None:
    schema = _load(SCHEMA)
    example = _load(EXAMPLE)

    jsonschema.Draft202012Validator.check_schema(schema)
    jsonschema.Draft202012Validator(schema).validate(example)

    assert example["state"] == {
        "installation_state": "not_observed",
        "activation_state": "not_activated",
        "task_authorization_state": "not_authorized",
        "acceptance_state": "not_run",
        "observation_refs": [],
    }
    assert set(example["authority"].values()) == {False}
    assert all(item["enabled_by_default"] is False for item in example["components"])


def test_distribution_contract_keeps_components_independent() -> None:
    example = _load(EXAMPLE)
    components = {item["component_id"]: item for item in example["components"]}

    assert components["run-binding"]["kind"] == "run_binding"
    assert components["context-bridge"]["kind"] == "context_bridge"
    assert components["policy-mcp"]["required"] is False
    assert components["dashboard"]["required"] is False
    assert len({item["path"] for item in components.values()}) == len(components)


def test_distribution_schema_is_template_only_and_non_runtime() -> None:
    schema = _load(SCHEMA)
    boundary = schema["x-boundary"]

    assert boundary["governed_identity"] is False
    assert boundary["runtime_execution"] is False
    assert boundary["installation"] is False
    assert boundary["activation"] is False
    assert boundary["task_authorization"] is False
    assert boundary["dispatch"] is False
    assert boundary["plugin_manager"] is False
    assert boundary["evidence_admission"] is False
