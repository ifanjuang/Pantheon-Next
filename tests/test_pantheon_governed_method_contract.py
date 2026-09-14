from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "templates/hermes/skills/pantheon-governed-method/SKILL.md"
RECEIPT = ROOT / "templates/hermes/returns/source_preflight_receipt.template.yaml"


def test_governed_method_is_general_condition_driven_and_bounded() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "name: pantheon-governed-method" in text
    assert "not a workflow engine" in text
    for movement in (
        "Frame / Cadrer",
        "Admit / Admettre",
        "Qualify / Qualifier",
        "Compose / Composer",
        "Produce Candidate / Produire candidat",
        "Test / Éprouver",
        "Status / Statuer",
    ):
        assert movement in text
    for tool in (
        "find_relevant_sources",
        "classify_request",
        "evaluate_preflight",
        "prepare_task_contract_skeleton",
        "prepare_evidence_pack_skeleton",
        "plan_context_pack",
        "validate_context_pack",
    ):
        assert tool in text
    for readiness in (
        "ready",
        "ready_with_limits",
        "needs_revision",
        "needs_user_input",
        "blocked",
    ):
        assert readiness in text
    assert "Classify by material conditions, not by object names" in text
    assert "one primary method" in text
    assert "one guardrail method" in text
    assert "one verification method" in text
    assert "one such MCP function per `tool_call`" in text
    assert "Do not call `list_sources` on the normal answer path" in text
    assert "Judge the result the user requested" in text
    for business_object in ("budget", "mail", "cctp", "compte rendu"):
        assert business_object not in text.lower()


def test_source_preflight_receipt_requires_exact_sources_and_keeps_boundaries() -> None:
    payload = yaml.safe_load(RECEIPT.read_text(encoding="utf-8"))
    receipt = payload["source_preflight_receipt"]
    consultation = receipt["consultations"][0]

    assert payload["status"] == "candidate_template_only"
    assert consultation["source_family"] == "REQUIRED"
    assert consultation["exact_source_ref"] == "REQUIRED"
    assert consultation["exact_source_opened"] is False
    assert receipt["memory_leads"]["label_when_unconfirmed"] == "indice mémoire — non confirmé"
    assert receipt["context_pack_validation"]["tool"] == "validate_context_pack"
    assert receipt["completion"]["readiness"] == "needs_revision"
    assert receipt["completion"]["assessed_result"] == "REQUIRED"
    assert consultation["runtime_trace"]["observed"] is False
    assert receipt["boundaries"] == {
        "receipt_is_evidence": False,
        "receipt_is_source_validation": False,
        "receipt_is_approval": False,
        "memory_is_source_authority": False,
    }


def test_generic_contract_contains_no_project_or_deliverable_specific_identity() -> None:
    text = (SKILL.read_text(encoding="utf-8") + RECEIPT.read_text(encoding="utf-8")).lower()
    for specific_identity in ("floquet", "annola"):
        assert specific_identity not in text
