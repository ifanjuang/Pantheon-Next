"""Read-only tests for Pantheon Next governance schemas.

These tests validate declarative schema structure and fictional examples only.
They must not execute workflows, call tools, mutate memory, approve outputs, or
interact with OpenWebUI/Hermes runtime surfaces.
"""

from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = SCHEMAS / "examples"

SCHEMA_TO_EXAMPLE = {
    "task_contract.schema.yaml": "task_contract.example.yaml",
    "task_contract_revision.schema.yaml": "task_contract_revision.example.yaml",
    "evidence_pack.schema.yaml": "evidence_pack.example.yaml",
    "register_candidate.schema.yaml": "register_candidate.example.yaml",
    "answer_status.schema.yaml": "answer_status.example.yaml",
    "policy_decision.schema.yaml": "policy_decision.example.yaml",
    "capability_passport.schema.yaml": "capability_passport.example.yaml",
    "shared_axes.schema.yaml": "shared_axes.example.yaml",
    "architecture-proof-register/shared.schema.yaml": "architecture-proof-register/shared.example.yaml",
    "architecture-proof-register/document_family.schema.yaml": "architecture-proof-register/document_family.example.yaml",
    "architecture-proof-register/indexed_document_version.schema.yaml": "architecture-proof-register/indexed_document_version.example.yaml",
    "architecture-proof-register/version_event.schema.yaml": "architecture-proof-register/version_event.example.yaml",
    "architecture-proof-register/proof_entry.schema.yaml": "architecture-proof-register/proof_entry.example.yaml",
    "architecture-proof-register/review_trigger.schema.yaml": "architecture-proof-register/review_trigger.example.yaml",
    "role_signal.schema.yaml": "role_signal.example.yaml",
    "workflow_manifest.schema.yaml": "workflow_manifest.example.yaml",
    "skill_manifest.schema.yaml": "skill_manifest.example.yaml",
    "context_pack.schema.yaml": "context_pack.example.yaml",
}

FORBIDDEN_SCHEMA_TERMS = {
    "athena-agent",
    "argos-agent",
    "themis-agent",
    "apollo-agent",
    "zeus-agent",
    "iris-agent",
    "hephaistos-agent",
    "HEPHAESTUS",
    "hephaestus-agent",
}

BOUNDARY_MARKERS = {
    "runtime_execution: false",
    "provider_routing: false",
    "memory_promotion: false",
}


def test_schema_and_example_files_exist() -> None:
    """Every governed schema should have a fictional example fixture."""

    assert SCHEMAS.exists(), "schemas/ directory is missing"
    assert EXAMPLES.exists(), "schemas/examples/ directory is missing"

    for schema_name, example_name in SCHEMA_TO_EXAMPLE.items():
        assert (SCHEMAS / schema_name).is_file(), f"missing schema: {schema_name}"
        assert (EXAMPLES / example_name).is_file(), f"missing example: {example_name}"


def test_schema_files_keep_non_runtime_boundaries() -> None:
    """Schemas must remain validation contracts, not runtime declarations."""

    for schema_name in SCHEMA_TO_EXAMPLE:
        text = (SCHEMAS / schema_name).read_text(encoding="utf-8")

        assert "x-boundary:" in text, f"missing x-boundary in {schema_name}"
        assert "runtime_execution: false" in text, f"runtime boundary missing in {schema_name}"

        if schema_name != "context_pack.schema.yaml":
            assert any(marker in text for marker in BOUNDARY_MARKERS), (
                f"expected at least one core anti-runtime marker in {schema_name}"
            )

        for forbidden in FORBIDDEN_SCHEMA_TERMS:
            assert forbidden not in text, f"non-canonical term {forbidden!r} in {schema_name}"


def test_schema_readme_records_validation_only_boundary() -> None:
    """The schema index should state the validation-only boundary explicitly."""

    readme = (SCHEMAS / "README.md").read_text(encoding="utf-8")

    assert "Status: implemented — reconciled schema baseline" in readme
    assert "context_pack.schema.yaml" in readme
    assert "Schemas are validation contracts." in readme
    assert "runtime components" in readme
    assert "provider routers" in readme
    assert "memory promotion engines" in readme
    assert "workflow engines" in readme
    assert "tool routers" in readme
    assert "schedulers" in readme
    assert "queues" in readme


def test_schema_governance_refs_point_to_existing_docs() -> None:
    """Schema governance references should resolve to repository files when local."""

    yaml = pytest.importorskip("yaml", reason="PyYAML is required for YAML structure tests")

    for schema_name in SCHEMA_TO_EXAMPLE:
        schema = yaml.safe_load((SCHEMAS / schema_name).read_text(encoding="utf-8"))
        refs = schema.get("properties", {}).get("governance_refs", {}).get("default", [])

        assert refs, f"governance_refs default is missing in {schema_name}"

        for ref in refs:
            if ref.startswith("docs/") or ref.startswith("schemas/"):
                assert (ROOT / ref).exists(), f"broken governance ref in {schema_name}: {ref}"


def test_examples_validate_against_schemas_when_dependencies_are_available() -> None:
    """Validate fictional examples against their schemas when dependencies exist."""

    yaml = pytest.importorskip("yaml", reason="PyYAML is required for schema example tests")
    jsonschema = pytest.importorskip(
        "jsonschema", reason="jsonschema is required for schema example tests"
    )

    validator_cls = jsonschema.Draft202012Validator
    format_checker = jsonschema.FormatChecker()

    for schema_name, example_name in SCHEMA_TO_EXAMPLE.items():
        schema = yaml.safe_load((SCHEMAS / schema_name).read_text(encoding="utf-8"))
        example = yaml.safe_load((EXAMPLES / example_name).read_text(encoding="utf-8"))

        validator_cls.check_schema(schema)
        validator = validator_cls(schema, format_checker=format_checker)
        errors = sorted(validator.iter_errors(example), key=lambda error: list(error.path))

        assert not errors, _format_validation_errors(schema_name, example_name, errors)


def _format_validation_errors(schema_name: str, example_name: str, errors: list[object]) -> str:
    lines = [f"{example_name} failed validation against {schema_name}:"]

    for error in errors[:10]:
        path = ".".join(str(part) for part in getattr(error, "path", [])) or "<root>"
        lines.append(f"- {path}: {getattr(error, 'message', error)}")

    if len(errors) > 10:
        lines.append(f"- ... {len(errors) - 10} additional errors")

    return "\n".join(lines)
