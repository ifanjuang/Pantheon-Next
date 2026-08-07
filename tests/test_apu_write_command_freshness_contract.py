"""Contract tests for H2 APU write-command freshness."""

from __future__ import annotations

from pathlib import Path

import jsonschema
import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012


ROOT = Path(__file__).resolve().parents[1]
APU = ROOT / "schemas" / "architecture-project-understanding"
EXAMPLES = ROOT / "schemas" / "examples" / "architecture-project-understanding"


def _validator() -> jsonschema.Draft202012Validator:
    schema = yaml.safe_load((APU / "write_command_candidate.schema.yaml").read_text(encoding="utf-8"))
    shared = yaml.safe_load((APU / "shared.schema.yaml").read_text(encoding="utf-8"))
    registry = Registry().with_resource(
        uri="shared.schema.yaml",
        resource=Resource.from_contents(shared, default_specification=DRAFT202012),
    )
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(
        schema,
        registry=registry,
        format_checker=jsonschema.FormatChecker(),
    )


def _example() -> dict:
    return yaml.safe_load(
        (EXAMPLES / "write_command_candidate.example.yaml").read_text(encoding="utf-8")
    )


def test_write_command_example_validates_with_freshness() -> None:
    example = _example()
    _validator().validate(example)
    assert example["operation"] == "add_match_to_existing_object"
    assert example["expected_owner_revision"] >= 1
    assert example["expected_object_revision"] >= 1
    assert example["match_axis"] in {"cross_index", "cross_source", "cross_level"}


def test_write_command_requires_project_and_target_revisions() -> None:
    validator = _validator()
    for field in ("project_ref", "expected_owner_revision", "expected_object_revision"):
        candidate = _example()
        candidate.pop(field)
        errors = list(validator.iter_errors(candidate))
        assert errors, f"write command unexpectedly accepts missing {field}"


def test_write_command_refuses_non_positive_target_revisions() -> None:
    validator = _validator()
    for field in ("expected_owner_revision", "expected_object_revision"):
        candidate = _example()
        candidate[field] = 0
        errors = list(validator.iter_errors(candidate))
        assert errors, f"write command unexpectedly accepts stale sentinel {field}=0"


def test_write_command_remains_candidate_only() -> None:
    schema = yaml.safe_load((APU / "write_command_candidate.schema.yaml").read_text(encoding="utf-8"))
    assert schema["properties"]["operation"]["const"] == "add_match_to_existing_object"
    assert schema["x-boundary"]["runtime_execution"] is False
    assert schema["x-boundary"]["automatic_apu_write"] is False
    assert schema["x-boundary"]["automatic_canonization"] is False
    assert schema["x-boundary"]["approval_engine"] is False
