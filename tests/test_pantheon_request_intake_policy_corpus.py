from __future__ import annotations

from pathlib import Path

import yaml

from pantheon_mcp import policy


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT.parent / "tests" / "fixtures" / "hermes_request_intake_cases.yaml"


def _request_candidate(case: dict) -> dict:
    expected = case["expected"]
    request = {
        "intent": case["request"],
        "conditions": expected.get("conditions") or [],
    }
    if expected.get("requested_transformation"):
        request["requested_transformation"] = expected["requested_transformation"]
    if expected.get("completion_requirements"):
        request["completion_requirements"] = expected["completion_requirements"]
    if expected.get("conflict_detected"):
        request["conflict_detected"] = True

    coordination = expected.get("coordination")
    if isinstance(coordination, dict):
        projected: dict = {}
        if coordination.get("requires"):
            projected["requires"] = [["supporting_basis", "review"]]
        if coordination.get("independent"):
            projected["independent"] = [["work_a", "work_b"]]
        if coordination.get("synthesize"):
            projected["synthesize"] = True
        if coordination.get("branch_on"):
            projected["branch_on"] = coordination["branch_on"]
        if coordination.get("repeat_until"):
            projected["repeat_until"] = coordination["repeat_until"]
        if projected:
            request["coordination"] = projected
    return request


def test_fixture_candidates_project_through_existing_policy_without_new_intake_authority() -> None:
    cases = yaml.safe_load(FIXTURES.read_text(encoding="utf-8"))["cases"]
    reports = {
        case["id"]: policy.classify_request(_request_candidate(case))
        for case in cases
    }

    assert reports["harmless_rewrite"]["consequence_level"] == "K0"
    assert reports["harmless_rewrite"]["handling"]["disposition"] == "PROCEED"
    assert "topology" not in reports["harmless_rewrite"]["handling"]

    assert reports["format_contract_text_without_review"]["consequence_level"] == "K0"
    assert reports["format_contract_text_without_review"]["handling"]["disposition"] == "PROCEED"

    assert reports["generic_explanation"]["handling"]["role_viewpoints"] == ["ARGOS"]
    assert reports["current_product_comparison"]["handling"]["topology"]["suggested"] == "fanout_extract_then_single_synthesis"
    assert reports["software_diagnosis"]["handling"]["coordination"]["repeat_until"] == ["tests_pass"]
    assert "topology" not in reports["software_diagnosis"]["handling"]
    assert reports["contradictory_documents"]["handling"]["rite_candidate"] == "concordance_des_sources"
    assert reports["creative_logo_options"]["handling"]["topology"]["suggested"] == "fanout_extract_then_single_synthesis"
    assert reports["cctp_review"]["handling"]["topology"]["suggested"] == "sequential_handoff"
    assert reports["prior_decision_recall"]["handling"]["role_viewpoints"] == ["MNEMOSYNE"]
    assert reports["conditional_future_action"]["handling"]["topology"]["suggested"] == "router"

    for case_id in ("send_client_message", "remember_as_canonical", "public_release_note"):
        assert reports[case_id]["consequence_level"] == "K4"
        assert reports[case_id]["handling"]["disposition"] == "GATE"

    assert reports["disputed_invoice_reply"]["handling"]["disposition"] == "CONSULT"
    assert reports["verify_contract_claim"]["handling"]["disposition"] == "CONSULT"
