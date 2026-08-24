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
ACTIVE_LOCK = ROOT / "implementation" / "hermes" / "distribution" / "pantheon-standard.lock.yaml"
RUNTIME_REVIEW = ROOT / "docs" / "governance" / "HERMES_RUNTIME_SURFACE_REVIEW.md"
EXECUTION_RUNBOOK = ROOT / "docs" / "install" / "HERMES_EXECUTION_BRIDGE_RUNBOOK.md"


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

    assert example["revision"] == 3
    assert set(example["source_pins"]) == {"pantheon_repository", "hermes_runtime"}
    assert example["source_pins"]["pantheon_repository"]["repository"] == (
        "ifanjuang/Pantheon-Next"
    )
    assert example["source_pins"]["hermes_runtime"]["version"] == "0.20.0"
    assert example["source_pins"]["hermes_runtime"]["artifact_digest"] is None
    assert example["source_pins"]["hermes_runtime"]["observation_ref"] == (
        "docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md"
    )
    assert example["state"] == {
        "installation_state": "not_observed",
        "activation_state": "not_activated",
        "task_authorization_state": "not_authorized",
        "acceptance_state": "not_run",
        "observation_refs": [],
    }
    assert set(example["authority"].values()) == {False}
    assert all(item["enabled_by_default"] is False for item in example["components"])
    assert all("source_repository" not in item for item in example["components"])


def test_distribution_transition_still_accepts_active_revision_2_lock() -> None:
    active = _load(ACTIVE_LOCK)
    _validator().validate(active)

    assert active["revision"] == 2
    assert "pantheon_next" in active["source_pins"]
    assert "pantheon_mvp" in active["source_pins"]
    assert "pantheon_repository" not in active["source_pins"]
    assert all("source_repository" in item for item in active["components"])


def test_revision_3_rejects_revision_2_repository_shape() -> None:
    example = _load(EXAMPLE)
    validator = _validator()

    legacy_pin = deepcopy(example)
    legacy_pin["source_pins"]["pantheon_mvp"] = {
        "repository": "ifanjuang/pantheon-mvp",
        "ref": "2" * 40,
    }
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(legacy_pin)

    legacy_component = deepcopy(example)
    legacy_component["components"][0]["source_repository"] = "Pantheon-Next"
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(legacy_component)


def test_revision_2_bridge_still_requires_legacy_pin_and_component_source() -> None:
    active = _load(ACTIVE_LOCK)
    validator = _validator()

    missing_pin = deepcopy(active)
    del missing_pin["source_pins"]["pantheon_mvp"]
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(missing_pin)

    missing_component_source = deepcopy(active)
    del missing_component_source["components"][0]["source_repository"]
    with pytest.raises(jsonschema.ValidationError):
        validator.validate(missing_component_source)


def test_distribution_schema_marks_revision_2_as_temporary_bridge() -> None:
    schema = _load(SCHEMA)
    migration = schema["x-migration"]

    assert migration["target_revision"] == 3
    assert migration["revision_2_status"] == "temporary_compatibility_only"
    assert migration["removal_condition"] == (
        "active_lock_and_audit_authority_migrated_to_revision_3"
    )


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
    ranged["source_pins"]["hermes_runtime"]["version"] = "0.20+"
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


def test_runtime_review_preserves_boundary_and_live_observation_gate() -> None:
    review = RUNTIME_REVIEW.read_text(encoding="utf-8")

    assert "Current reviewed target: Hermes Agent 0.20.0." in review
    assert "version: 0.20.0" in review
    assert "kernel_change_required: false" in review
    assert "real_instance_observation_required: true" in review
    assert "artifact_digest: null" in review
    assert "trusted peer != approved actor" in review
    assert "citation present != Evidence admitted" in review
    assert "voice command received != human approval recorded" in review
    assert "provider" in review and "model_options" in review


def test_operator_runbook_matches_governed_profile_memory_cli_contract() -> None:
    runbook = EXECUTION_RUNBOOK.read_text(encoding="utf-8")

    assert "export HERMES_GOVERNED_PROFILE=pantheon-governed" in runbook
    assert '/p/${HERMES_GOVERNED_PROFILE}' in runbook
    assert "must not include a trailing `/v1` path" in runbook

    assert runbook.count("pantheon-hermes capture-memory-status") == 2
    assert "--output memory-status-observe.json" in runbook
    assert "--output memory-status-launch.json" in runbook
    assert "valid for at most five minutes" in runbook
    assert "memory_posture.age_seconds <= 300" in runbook

    observe = runbook.split("pantheon-hermes observe", 1)[1].split("```", 1)[0]
    assert '--expected-profile "${HERMES_GOVERNED_PROFILE}"' in observe
    assert "--memory-status-receipt memory-status-observe.json" in observe
    assert observe.count("--allowed-tool") == 2
    assert observe.count("--required-tool") == 2

    launch = runbook.split("pantheon-hermes launch", 1)[1].split("```", 1)[0]
    assert '--expected-profile "${HERMES_GOVERNED_PROFILE}"' in launch
    assert "--memory-status-receipt memory-status-launch.json" in launch
    assert launch.count("--allowed-tool") == 2
    assert launch.count("--required-tool") == 2
    assert "--admission-id admission-<ID>" in launch

    assert "profile_surface.status = qualified" in runbook
    assert "tool_surface.unexpected_tools = []" in runbook
    assert "tool_surface.missing_required_tools = []" in runbook
    assert "memory_posture.built_in_memory_injection = off" in runbook
    assert "memory_posture.built_in_user_profile_injection = off" in runbook
    assert "memory_posture.memory_tool = off" in runbook
    assert "memory_posture.session_memory_key = absent" in runbook
    assert "session_memory_header_sent = false" in runbook

    assert "\nunexpected_tools = []\n" not in runbook
    assert "\nmissing_required_tools = []\n" not in runbook
    assert "result_accepted = false" not in runbook
    assert "evidence_admitted = false" not in runbook
    assert "project_mutated = false" not in runbook
    assert "The bounded Pantheon API response is carried under `recorded`" in runbook

    assert "X-Hermes-Session-Key = absent" in runbook
    assert "profile route answered != governed profile qualified" in runbook
    assert "fresh memory observation != task authorized" in runbook
    assert "It does not authorize future tasks" in runbook


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
