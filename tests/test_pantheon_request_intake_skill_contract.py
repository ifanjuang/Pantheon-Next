from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "templates/hermes/skills/pantheon-request-intake/SKILL.md"
ROLE_ACTIVATION = ROOT / "docs/governance/ROLE_ACTIVATION.md"
REQUEST_HANDLING = ROOT / "mcp-server/pantheon_mcp/request_handling.py"
FIXTURES = ROOT / "tests/fixtures/hermes_request_intake_cases.yaml"
REGISTRY = ROOT / "templates/TEMPLATE_REGISTRY.md"


def _role_triggers() -> set[str]:
    text = ROLE_ACTIVATION.read_text(encoding="utf-8")
    block = text.split("```yaml\nmandatory_role_triggers:\n", 1)[1].split("```", 1)[0]
    data = yaml.safe_load("mandatory_role_triggers:\n" + block)
    return {
        trigger
        for triggers in data["mandatory_role_triggers"].values()
        for trigger in triggers
    }


def test_request_intake_is_a_bounded_semantic_adapter_not_policy_authority() -> None:
    text = SKILL.read_text(encoding="utf-8")

    assert "name: pantheon-request-intake" in text
    assert "status: candidate_template_only" in text
    assert "governed_by: docs/governance/REQUEST_LIFECYCLE.md" in text
    assert "policy_contract: mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md" in text

    for invariant in (
        "semantic candidate != truth",
        "condition candidate != consequence classification",
        "coordination relation != dispatch",
        "completion requirement != approval",
        "Hermes interpretation != Pantheon decision",
        "Return a request candidate, never K/V/C.",
        "Do not state `PROCEED`, `CONSULT` or `GATE`; Pantheon returns those.",
        "Prefer the smallest sufficient candidate.",
    ):
        assert invariant in text

    assert "Do not choose a topology" in text
    assert "Do not reconsult after every internal step" in text
    assert "Do not emit a condition merely because a word appears in the request" in text


def test_skill_condition_examples_are_owned_by_role_activation_and_supported_by_policy() -> None:
    text = SKILL.read_text(encoding="utf-8")
    doctrine = _role_triggers()

    start = text.index("Common examples include:")
    block = text[start:].split("```text", 1)[1].split("```", 1)[0]
    advertised = {line.strip() for line in block.splitlines() if line.strip()}

    assert advertised <= doctrine

    request_handling = REQUEST_HANDLING.read_text(encoding="utf-8")
    for trigger in advertised:
        assert f'"{trigger}"' in request_handling


def test_broad_fixture_corpus_is_structural_and_contains_negative_expectations() -> None:
    data = yaml.safe_load(FIXTURES.read_text(encoding="utf-8"))
    cases = data["cases"]

    assert len(cases) >= 15
    assert len({case["id"] for case in cases}) == len(cases)

    required_ids = {
        "harmless_rewrite",
        "generic_explanation",
        "current_product_comparison",
        "software_diagnosis",
        "contradictory_documents",
        "creative_logo_options",
        "cctp_review",
        "disputed_invoice_reply",
        "prior_decision_recall",
        "send_client_message",
        "conditional_future_action",
        "format_contract_text_without_review",
        "verify_contract_claim",
        "remember_as_canonical",
        "public_release_note",
    }
    assert required_ids <= {case["id"] for case in cases}

    doctrine = _role_triggers()
    for case in cases:
        expected = case["expected"]
        conditions = set(expected.get("conditions") or [])
        forbidden = set(expected.get("forbidden_conditions") or [])
        assert conditions <= doctrine
        assert forbidden <= doctrine
        assert not conditions.intersection(forbidden)


def test_registry_lists_request_intake_once() -> None:
    registry = REGISTRY.read_text(encoding="utf-8")
    path = "templates/hermes/skills/pantheon-request-intake/SKILL.md"
    assert registry.count(path) == 1
