from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES = ROOT / "mvp_vertical" / "cockpit" / "styles"


def test_pantheon_affaires_pack_and_project_booster_share_one_geometry() -> None:
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert "--effect-1-width: var(--effect-1-width, 75%)" in cards
    assert "--effect-2-width: var(--effect-2-width, 75%)" in cards
    assert "--effect-3-width: var(--effect-3-width, 75%)" in cards

    project = families.split('[data-kind="project"]', 1)[1].split('[data-kind="work"]', 1)[0]
    for legacy_override in (
        "--effect-1-width:",
        "--effect-1-height:",
        "--effect-2-width:",
        "--effect-2-height:",
        "--effect-2-top:",
        "--effect-2-left:",
        "--effect-3-width:",
        "--effect-3-height:",
        "--effect-3-top:",
        "--effect-3-left:",
    ):
        assert legacy_override not in project


def test_shared_blobs_rotate_in_opposite_directions_with_stable_variation() -> None:
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")

    assert "card-blob-rotate-forward" in cards
    assert "card-blob-rotate-reverse" in cards
    assert "+ 360deg" in cards
    assert "- 360deg" in cards
    assert '.card[data-variant="1"]' in cards
    assert '.card[data-variant="2"]' in cards
    assert '.card[data-variant="3"]' in cards
    assert "@media (prefers-reduced-motion: reduce)" in cards
    assert "animation: none !important" in cards
