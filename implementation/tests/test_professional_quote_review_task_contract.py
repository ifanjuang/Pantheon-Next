from __future__ import annotations

import re
from pathlib import Path

import yaml

from mvp_vertical.contract import load_contract


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "dossiers/devis_reprise/task_contract.yaml"
METHOD_PATH = ROOT.parent / "docs/domain-packs/architecture/DOCUMENT_REVIEW.md"
ORACLE_PATH = ROOT / "tests/fixtures/professional_quote_review_cases.yaml"


def _text_block_after(marker: str) -> list[str]:
    text = METHOD_PATH.read_text(encoding="utf-8")
    tail = text.split(marker, 1)[1]
    match = re.search(r"```text\n(.*?)\n```", tail, re.DOTALL)
    assert match is not None, marker
    return [line.strip() for line in match.group(1).splitlines() if line.strip()]


def test_devis_reprise_contract_projects_current_document_review_method() -> None:
    contract = load_contract(CONTRACT_PATH)
    intent = contract.raw["intent"]
    method = intent["method_projection"]

    assert method["authority_ref"] == "docs/domain-packs/architecture/DOCUMENT_REVIEW.md"
    assert method["status"] == "task_scoped_non_authoritative_projection"
    assert method["use_case"] == "cctp_quote_comparison"
    assert method["acceptable_claim_types"] == _text_block_after("Acceptable claim types:")
    assert method["forbidden_outputs"] == _text_block_after("Forbidden output:")
    assert method["default_recommended_status"] == "requires_human_review"

    # Method projection is task data, not a parallel Capability/Skill admission.
    assert "capability_id" not in intent
    assert "skill" not in intent


def test_professional_oracle_uses_only_document_review_claim_types() -> None:
    contract = load_contract(CONTRACT_PATH)
    method_types = set(contract.raw["intent"]["method_projection"]["acceptable_claim_types"])
    oracle = yaml.safe_load(ORACLE_PATH.read_text(encoding="utf-8"))
    expected_types = {
        case["expected_claim_type"]
        for case in oracle["cases"]
        if case.get("expected_claim_type")
    }

    assert expected_types <= method_types


def test_devis_reprise_contract_no_longer_routes_a_reply_surface() -> None:
    contract = load_contract(CONTRACT_PATH)
    raw = contract.raw
    operations = raw["scope"]["operations"]

    assert "exposure_surface" not in raw
    assert "draft_reply_candidate" not in operations
    assert "prepare_result_candidate" in operations
    assert raw["expected_outputs"] == ["result_candidate", "evidence_pack_candidate"]
    assert "email" not in contract.intent.casefold()
    assert raw["forbidden_scope"] == [
        "external_send",
        "source_outside_declared_perimeter",
        "register_write",
        "approval_of_any_kind",
    ]
