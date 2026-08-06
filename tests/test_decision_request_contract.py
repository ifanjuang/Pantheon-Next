from pathlib import Path

import jsonschema
import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "decision_request.schema.yaml"
EXAMPLE_PATH = ROOT / "schemas" / "examples" / "decision_request.example.yaml"


def _load(path: Path) -> dict:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def _validator() -> jsonschema.Draft202012Validator:
    schema = _load(SCHEMA_PATH)
    jsonschema.Draft202012Validator.check_schema(schema)
    return jsonschema.Draft202012Validator(
        schema,
        format_checker=jsonschema.FormatChecker(),
    )


def test_decision_request_example_validates() -> None:
    _validator().validate(_load(EXAMPLE_PATH))


def test_blocking_request_requires_work_issue() -> None:
    invalid = _load(EXAMPLE_PATH)
    invalid["work_issue_ref"] = None
    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(invalid)


def test_option_response_requires_reviewable_options() -> None:
    invalid = _load(EXAMPLE_PATH)
    invalid["options"] = []
    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(invalid)


def test_pending_request_cannot_claim_a_resolution() -> None:
    invalid = _load(EXAMPLE_PATH)
    invalid["resolved_decision_ref"] = "decision-001"
    invalid["resolved_at"] = "2026-08-06T11:00:00Z"
    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(invalid)


def test_resolved_request_requires_a_separate_decision_record_reference() -> None:
    invalid = _load(EXAMPLE_PATH)
    invalid["status"] = "resolved"
    invalid["resolved_decision_ref"] = None
    invalid["resolved_at"] = None
    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(invalid)


def test_free_text_request_does_not_carry_choice_options() -> None:
    invalid = _load(EXAMPLE_PATH)
    invalid["decision_type"] = "question"
    invalid["response_mode"] = "free_text"
    with pytest.raises(jsonschema.ValidationError):
        _validator().validate(invalid)


def test_global_decisions_are_only_unclassified_requests() -> None:
    schema = _load(SCHEMA_PATH)
    rules = schema["x-decision-request-rules"]
    assert rules["global_decisions_view_contains_only_unclassified_requests"] is True
    assert rules["unclassified_request_has_null_project_ref"] is True
    assert rules["project_view_requires_matching_project_ref"] is True
    assert schema["x-boundary"]["agency_decision_owner"] is False


def test_request_is_not_decision_or_runtime_authority() -> None:
    schema = _load(SCHEMA_PATH)
    boundary = schema["x-boundary"]
    assert boundary["request_is_decision"] is False
    assert boundary["request_is_approval"] is False
    assert boundary["agency_decision_owner"] is False
    assert boundary["automatic_work_issue_transition"] is False
    assert boundary["automatic_runtime_continuation"] is False
    assert boundary["runtime_execution"] is False
    assert boundary["scheduler"] is False
    assert boundary["queue_system"] is False
    assert boundary["provider_routing"] is False
    assert boundary["memory_promotion"] is False
    assert boundary["evidence_admission"] is False
    assert boundary["automatic_approval"] is False
