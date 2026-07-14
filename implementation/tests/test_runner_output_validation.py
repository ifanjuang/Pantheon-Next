"""Runner output validation (external review, finding #10). All DB-free.

Two things this closes:
  1. commitment_flags is an array of STRINGS (the vendored schema types it so);
     it used to be an array of dicts, diverging invisibly because the tested
     path always yielded the empty list.
  2. run() validates every emitted object against the vendored schema, so a
     later change (a divergent shape, a Block 2 LLM drafter) cannot quietly
     emit a malformed object — a broken cage is a bug, not a candidate.
"""

from __future__ import annotations

import pytest

from mvp_vertical.runner import (
    RunnerInvariantError,
    _assert_conforms_to_schema,
    _detect_commitments,
)


def test_commitment_flags_are_strings_not_dicts():
    flags = _detect_commitments("Bonjour, nous acceptons votre offre et vous pouvez lancer.")
    assert flags, "a commitment phrase must be flagged"
    assert all(isinstance(f, str) for f in flags), "commitment_flags must be strings (schema)"


def test_neutral_text_raises_no_commitment_flag():
    assert _detect_commitments("Voici les éléments retenus, sans conclusion.") == []


def _valid_candidate() -> dict:
    return {
        "object_type": "result_candidate",
        "object_id": "mvp.test.tc.rc-001",
        "result_candidate_id": "mvp.test.tc.rc-001",
        "status": "draft_to_review",
        "body": "Bonjour, …",
        "external_action_authorized": False,
        "commitment_flags": ["« nous acceptons » — engagement externe si envoyé tel quel"],
    }


def test_schema_validation_passes_a_conforming_candidate():
    _assert_conforms_to_schema([_valid_candidate()])  # must not raise


def test_schema_validation_catches_dict_commitment_flags():
    # The exact review #10 divergence: dicts where the schema wants strings.
    bad = _valid_candidate()
    bad["commitment_flags"] = [{"phrase": "nous acceptons", "risk": "…"}]
    with pytest.raises(RunnerInvariantError):
        _assert_conforms_to_schema([bad])


def test_schema_validation_catches_a_missing_required_field():
    bad = _valid_candidate()
    del bad["body"]  # body is required by the schema
    with pytest.raises(RunnerInvariantError):
        _assert_conforms_to_schema([bad])
