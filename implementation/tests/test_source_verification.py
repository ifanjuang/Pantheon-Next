"""Source-aligned verification contract tests."""

from __future__ import annotations

import pytest

from mvp_vertical.source_verification import (
    SourceVerificationObservation,
    SourceVerificationReport,
    not_observed_verification,
)


def _report(**overrides) -> SourceVerificationReport:
    values = {
        "source_version_id": "srcv-7",
        "source_digest": "sha256:source",
        "compilation_id": "cmp-example",
        "compilation_output_digest": "sha256:compilation",
        "binding_id": "visual-source-checker",
        "binding_version": "1.0.0",
        "execution_id": "run-1",
        "parameters_profile": "source-check-v1",
        "coverage_complete": True,
    }
    values.update(overrides)
    return SourceVerificationReport(**values)


def _observation(*, severity: str = "warning") -> SourceVerificationObservation:
    return SourceVerificationObservation(
        kind="changed_number",
        severity=severity,
        source_locator="page/2/region/4",
        derivative_locator="unit/cmp-example/12",
        message="The amount differs from the exact source page.",
        expected_digest="sha256:expected",
        observed_digest="sha256:observed",
    )


def test_not_observed_projection_is_explicit_and_non_authoritative():
    projection = not_observed_verification()

    assert projection["status"] == "not_observed"
    assert projection["report_id"] is None
    assert projection["authority"] == {
        "is_source_truth": False,
        "is_evidence": False,
        "is_professional_validation": False,
    }


def test_complete_run_without_mismatch_does_not_claim_verified_correctness():
    payload = _report().as_dict()

    assert payload["status"] == "no_mismatch_observed"
    assert payload["observations"] == []
    assert payload["authority"]["is_source_truth"] is False
    assert "verified" not in payload["status"]


def test_warning_observation_yields_mismatch_observed():
    payload = _report(observations=(_observation(),)).as_dict()

    assert payload["status"] == "mismatch_observed"
    assert payload["observations"][0]["kind"] == "changed_number"


def test_blocking_observation_requires_review():
    payload = _report(observations=(_observation(severity="blocking"),)).as_dict()

    assert payload["status"] == "review_required"
    assert payload["authority"]["is_professional_validation"] is False


def test_incomplete_coverage_remains_inconclusive_even_without_mismatch():
    payload = _report(
        coverage_complete=False,
        inconclusive_reasons=("page 3 could not be rendered",),
    ).as_dict()

    assert payload["status"] == "inconclusive"
    assert payload["inconclusive_reasons"] == ["page 3 could not be rendered"]


def test_report_identity_changes_with_exact_source_or_observation():
    baseline = _report()
    changed_source = _report(source_digest="sha256:other")
    changed_observation = _report(observations=(_observation(),))

    assert baseline.report_id != changed_source.report_id
    assert baseline.report_id != changed_observation.report_id
    assert baseline.report_id == _report().report_id


def test_contract_rejects_unknown_kinds_and_missing_provenance():
    with pytest.raises(ValueError, match="unsupported observation kind"):
        SourceVerificationObservation(
            kind="truth_score",
            severity="warning",
            source_locator="page/1",
            derivative_locator="unit/1",
            message="unsupported",
        )

    with pytest.raises(ValueError, match="source_digest is required"):
        _report(source_digest="")


def test_contract_rejects_ambiguous_coverage_and_invalid_observation_values():
    with pytest.raises(ValueError, match="coverage_complete must be a boolean"):
        _report(coverage_complete="false")

    with pytest.raises(ValueError, match="observations must contain"):
        _report(observations=("changed_number",))
