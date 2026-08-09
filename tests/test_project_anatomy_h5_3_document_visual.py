"""H5.3 qualification for structured documents, PDF drawings and site images."""

from __future__ import annotations

import copy
from collections.abc import Callable
from pathlib import Path
from typing import Any

import jsonschema
import pytest
import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas" / "architecture-project-understanding"
EXAMPLES = ROOT / "schemas" / "examples" / "architecture-project-understanding"
CORPUS = EXAMPLES / "document_visual_qualification_corpus.yaml"


def _load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def _validator() -> jsonschema.Draft202012Validator:
    registry = Registry()
    for name in (
        "shared.schema.yaml",
        "source_representation.schema.yaml",
        "attribute_claim.schema.yaml",
        "relation_claim.schema.yaml",
    ):
        registry = registry.with_resource(
            uri=name,
            resource=Resource.from_contents(
                _load(SCHEMAS / name),
                default_specification=DRAFT202012,
            ),
        )
    return jsonschema.Draft202012Validator(
        _load(SCHEMAS / "observation_bundle.schema.yaml"),
        format_checker=jsonschema.FormatChecker(),
        registry=registry,
    )


def _merge(base: Any, overrides: Any) -> Any:
    if not isinstance(base, dict) or not isinstance(overrides, dict):
        return copy.deepcopy(overrides)
    merged = copy.deepcopy(base)
    for key, value in overrides.items():
        merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
    return merged


def _cases() -> list[dict[str, Any]]:
    corpus = _load(CORPUS)
    assert corpus["base_example"] == "observation_bundle.example.yaml"
    base = _load(EXAMPLES / corpus["base_example"])
    return [scenario | {"bundle": _merge(base, scenario["overrides"])} for scenario in corpus["scenarios"]]


def _case_id(case: dict[str, Any]) -> str:
    return "+".join(case["scenario_ids"])


def _candidate_authority(bundle: dict[str, Any]) -> None:
    assert set(bundle["authority"].values()) == {False}
    assert all(item["proof_status"] == "candidate" for item in bundle["source_representations"])
    assert all(
        item["proof_status"] == "candidate"
        for key in ("attribute_claim_candidates", "relation_claim_candidates")
        for item in bundle[key]
    )


def _requirement_not_observation(bundle: dict[str, Any]) -> None:
    assert bundle["attribute_claim_candidates"] == []
    assert any(item["code"] == "requirement.separate_path" for item in bundle["withheld"])
    assert bundle["source_representations"][0]["context"]["native_context"]["semantic_role"] == "prescription"


def _partial_absence_refused(bundle: dict[str, Any]) -> None:
    assert bundle["coverage"]["completeness"] == "partial_for_declared_scope"
    assert bundle["coverage"]["absence_inference_allowed"] is False
    assert bundle["coverage"]["observed_scope"] != bundle["scope"]


def _pdf_local_identity(bundle: dict[str, Any]) -> None:
    representation = bundle["source_representations"][0]
    assert representation["identifiers"] == [{"scheme": "drawing.local_label", "value": "P12"}]
    assert bundle["relation_claim_candidates"] == []


def _scale_uncertainty_withheld(bundle: dict[str, Any]) -> None:
    assert bundle["attribute_claim_candidates"] == []
    assert bundle["source_representations"][0]["coordinate_frame"] == "PIXEL"
    assert any(item["code"] == "measurement.scale_unresolved" for item in bundle["gaps"])
    assert any(item["code"] == "measurement.real_world_area_withheld" for item in bundle["withheld"])


def _apparent_not_contractual(bundle: dict[str, Any]) -> None:
    claim = bundle["attribute_claim_candidates"][0]
    assert claim["attribute_key"] == "physical.apparent_condition"
    assert claim["assertion_mode"] == "derived"
    assert claim["source_authority"] == "model_interpretation_candidate"
    forbidden = ("nonconform", "compliance", "received", "reservation")
    assert not any(token in claim["attribute_key"] for token in forbidden)


def _photo_field_not_absence(bundle: dict[str, Any]) -> None:
    assert bundle["coverage"]["absence_inference_allowed"] is False
    assert set(bundle["coverage"]["excluded_reasons"]) == {
        "hidden_faces_not_visible",
        "concealed_fixings_not_visible",
    }


def _photo_history_preserved(bundle: dict[str, Any]) -> None:
    before, after = bundle["source_representations"]
    assert before["observed_at"] < after["observed_at"]
    assert before["content_digest"] != after["content_digest"]
    values = [claim["value"]["value"] for claim in bundle["attribute_claim_candidates"]]
    assert values == ["apparent_defect", "no_visible_defect_in_observed_region"]
    assert any(item["code"] == "temporal.continuity_not_observed" for item in bundle["gaps"])
    assert any(item["code"] == "review.no_reservation_inference" for item in bundle["warnings"])


def _non_success_absence_refused(bundle: dict[str, Any]) -> None:
    assert bundle["operational_outcome"] == "failed"
    assert bundle["coverage"]["absence_inference_allowed"] is False


def _no_fabricated_candidates(bundle: dict[str, Any]) -> None:
    assert bundle["source_representations"] == []
    assert bundle["attribute_claim_candidates"] == []
    assert bundle["relation_claim_candidates"] == []
    assert bundle["gaps"]


INVARIANTS: dict[str, Callable[[dict[str, Any]], None]] = {
    "candidate_authority": _candidate_authority,
    "requirement_not_observation": _requirement_not_observation,
    "partial_absence_refused": _partial_absence_refused,
    "pdf_local_identity": _pdf_local_identity,
    "scale_uncertainty_withheld": _scale_uncertainty_withheld,
    "apparent_not_contractual": _apparent_not_contractual,
    "photo_field_not_absence": _photo_field_not_absence,
    "photo_history_preserved": _photo_history_preserved,
    "non_success_absence_refused": _non_success_absence_refused,
    "no_fabricated_candidates": _no_fabricated_candidates,
}


@pytest.mark.parametrize("case", _cases(), ids=_case_id)
def test_h5_3_document_visual_cases_validate_and_keep_boundaries(case: dict[str, Any]) -> None:
    assert case["expected_valid"] is True
    _validator().validate(case["bundle"])
    for invariant in case["invariants"]:
        INVARIANTS[invariant](case["bundle"])


def test_h5_3_uses_one_canonical_bundle_without_new_source_specific_contract() -> None:
    corpus = _load(CORPUS)
    assert corpus["status"] == "qualification_only"
    assert {case_id for case in corpus["scenarios"] for case_id in case["scenario_ids"]} == {
        "H53-DOC-REQ",
        "H53-PDF-PARTIAL",
        "H53-PDF-SCALE",
        "H53-PHOTO-DEFECT",
        "H53-PHOTO-HISTORY",
        "H53-DOC-CORRUPT",
    }
    assert set(INVARIANTS) == {
        invariant
        for case in corpus["scenarios"]
        for invariant in case["invariants"]
    }
