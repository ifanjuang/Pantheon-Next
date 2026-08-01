from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def _text(name: str) -> str:
    return (COCKPIT / name).read_text(encoding="utf-8")


def test_action_modules_consume_canonical_card_structure() -> None:
    actions = _text("v2_actions.js")
    candidates = _text("v2_candidate_actions.js")
    policy = _text("v2_interaction_policy.js")

    for source in (actions, candidates, policy):
        assert '.v2-card' not in source

    for selector in (".card", ".card-title", ".card-entity-id"):
        assert selector in actions

    assert ".card-actions button" in actions
    assert "button[data-card-action]" in actions
    assert "button[data-card-action]" in candidates
    assert "dataset.cardAction" in actions
    assert "dataset.cardAction" in candidates
    assert "data-v2-action" not in actions
    assert "data-v2-action" not in candidates


def test_interaction_policy_reads_the_same_canonical_active_card() -> None:
    policy = _text("v2_interaction_policy.js")
    assert 'querySelector(".card")' in policy
    assert 'querySelector(".v2-card")' not in policy
    assert 'attributeFilter: ["data-flipped"]' in policy
