"""Regression checks for the executed Obsidian graph/health qualification result."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PREPARED = ROOT / "tests" / "fixtures" / "obsidian_graph_health_pilot.json"
OBSERVED = ROOT / "tests" / "fixtures" / "obsidian_graph_health_observed_v2026.08.6.json"


def test_observed_graph_health_result_stays_separate_from_prepared_expectations() -> None:
    prepared = json.loads(PREPARED.read_text(encoding="utf-8"))
    observed = json.loads(OBSERVED.read_text(encoding="utf-8"))

    assert prepared["execution_status"] == "prepared_not_executed"
    assert "observed_results" not in prepared
    assert observed["execution_status"] == "executed_partial_not_accepted"
    assert observed["provider_acceptance"] == "not_accepted"
    assert observed["pilot_id"] == prepared["pilot_id"]


def test_observed_result_is_pinned_to_exact_upstream_deterministic_surfaces() -> None:
    observed = json.loads(OBSERVED.read_text(encoding="utf-8"))
    provider = observed["provider"]

    assert provider["stable_release"] == "v2026.08.6"
    assert provider["stable_release_sha"] == "8b5859d0f895e51e785d3ba22ed8008297e8d367"
    assert provider["current_main_observed_sha"] == "37596cffeef43faecd9b61246b0b119b11a87bc4"
    assert provider["source_blobs"] == {
        "graph_analysis.py": "9e2ff9be961f4149aa09d490e10089fb1d700c69",
        "lint.py": "09a2b8207e02296455fd4d9a9401e6aa1fbdd66d",
    }
    assert provider["current_main_uses_same_deterministic_blobs"] is True


def test_observed_result_preserves_partial_passes_without_provider_promotion() -> None:
    observed = json.loads(OBSERVED.read_text(encoding="utf-8"))
    cases = observed["case_results"]

    for case_id in (
        "bookkeeping_not_hub",
        "raw_staging_excluded",
        "bounded_shortest_path",
        "isolated_question",
        "broken_menuiseries_link",
        "protected_material_no_mutation",
    ):
        assert cases[case_id]["status"] == "pass"

    assert observed["raw_observations"]["write_check"] == {
        "changed": False,
        "added_removed_or_modified": [],
    }
    assert "provider-wide adoption" in observed["qualification_decision"]["not_accepted_now"]


def test_observed_result_keeps_link_precision_and_scope_failures_visible() -> None:
    observed = json.loads(OBSERVED.read_text(encoding="utf-8"))
    cases = observed["case_results"]

    valid_links = cases["valid_obsidian_links_not_broken"]
    assert valid_links["status"] == "fail"
    assert valid_links["false_positive_count"] == 6
    assert set(valid_links["false_positive_targets"]) == {
        "plan.pdf",
        "perspective.png",
        "planning.base",
        "schema.canvas",
        "cctp.md",
        "chauffage\\",
    }

    scope = cases["bounded_scope"]
    assert scope["status"] == "fail"
    assert scope["native_scope_parameter"] is False
    assert scope["sentinel_in_full_vault_graph"] is True
    assert "caller or an adapter" in scope["reason"]


def test_semantic_duplicate_and_contradiction_capabilities_are_not_inferred_from_missing_implementation() -> None:
    observed = json.loads(OBSERVED.read_text(encoding="utf-8"))
    cases = observed["case_results"]

    assert cases["heating_duplicate_candidate"]["status"] == "not_demonstrated"
    assert cases["heating_contradiction_candidate"]["status"] == "not_demonstrated"
    assert "semantic detector" in cases["heating_duplicate_candidate"]["reason"]
    assert "semantic contradiction detector" in cases["heating_contradiction_candidate"]["reason"]


def test_observed_result_preserves_governance_boundaries() -> None:
    observed = json.loads(OBSERVED.read_text(encoding="utf-8"))

    for invariant in (
        "observed result != provider-wide truth",
        "partial capability pass != provider adoption",
        "read-only success != authorization",
        "graph relation != Evidence",
        "health finding != defect confirmed",
        "provider output != governed Knowledge",
    ):
        assert invariant in observed["invariants"]

    assert observed["qualification_decision"]["next_action"].startswith(
        "Keep obsidian-wiki as a replaceable partial capability reference."
    )
