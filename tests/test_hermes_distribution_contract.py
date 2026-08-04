from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import jsonschema
import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
DISTRIBUTION = ROOT / "templates" / "hermes" / "distribution"
SCHEMA = DISTRIBUTION / "distribution-lock.schema.yaml"
EXAMPLE = DISTRIBUTION / "distribution-lock.example.yaml"
README = DISTRIBUTION / "README.md"


def _load(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _validator() -> jsonschema.Draft202012Validator:
    schema = _load(SCHEMA)
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(schema)


def test_distribution_example_validates_without_creating_authority() -> None:
    example = _load(EXAMPLE)
    _validator().validate(example)

    assert example["revision"] == 2
    assert example["source_pins"]["hermes_runtime"]["version"] == "0.19.0"
    assert example["source_pins"]["hermes_runtime"]["artifact_digest"] is None
    assert example["state"] == {
        "installation_state": "not_observed",
        "activation_state": "not_activated",
        "task_authorization_state": "not_authorized",
        "acceptance_state": "not_run",
        "observation_refs": [],
    }
    assert set(example["authority"].values()) == {False}
    assert all(item["enabled_by_default"] is False for item in example["components"])


def test_distribution_contract_keeps_components_independent_and_digest_bound() -> None:
    example = _load(EXAMPLE)
    components = {item["component_id"]: item for item in example["components"]}

    assert components["run-binding"]["kind"] == "run_binding"
    assert components["run-binding"]["digest_mode"] == "file"
    assert components["context-bridge"]["kind"] == "context_bridge"
    assert components["context-bridge"]["digest_mode"] == "tree"
    assert components["policy-mcp"]["required"] is False
    assert components["dashboard"]["required"] is False
    assert len({item["path"] for item in components.values()}) == len(components)
    assert all(item["content_digest"].startswith("sha256:") for item in components.values())


def test_distribution_schema_rejects_unbounded_runtime_version_and_missing_digest() -> None:
    example = _load(EXAMPLE)
    validator = _validator()

    ranged = deepcopy(example)
    ranged["source_pins"]["hermes_runtime"]["version"] = "0.19+"
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(ranged)

    missing_digest = deepcopy(example)
    del missing_digest["components"][0]["content_digest"]
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(missing_digest)


def test_observed_distribution_requires_runtime_artifact_digest() -> None:
    example = _load(EXAMPLE)
    validator = _validator()

    observed_without_artifact = deepcopy(example)
    observed_without_artifact["status"] = "observed"
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(observed_without_artifact)

    observed = deepcopy(observed_without_artifact)
    observed["source_pins"]["hermes_runtime"]["artifact_digest"] = (
        "sha256:" + "a" * 64
    )
    validator.validate(observed)


def test_tree_digest_documentation_has_closed_ephemeral_exclusions() -> None:
    readme = README.read_text(encoding="utf-8")

    assert "reject symbolic links" in readme
    assert ".git/" in readme
    assert "__pycache__/" in readme
    assert "*.pyc" in readme
    assert "*.pyo" in readme
    assert ".DS_Store" in readme
    assert "exclusion list is closed" in readme


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
