from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
HTML = COCKPIT / "index.html"
STYLES = COCKPIT / "styles"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_current_styles_replace_historical_refinement_chain() -> None:
    html = _text(HTML)
    for filename in ("cockpit.css", "cards.css", "families.css", "editors.css"):
        assert f'href="styles/{filename}"' in html
    for retired in ("v2.css", "v2_refinement.css", "v2_shell_controls.css"):
        assert retired not in html


def test_card_typography_is_controlled_by_level_variables() -> None:
    cards = _text(STYLES / "cards.css")
    families = _text(STYLES / "families.css")
    assert "var(--card-title-size" in cards
    assert "letter-spacing: -.045em" in cards
    assert "text-wrap: balance" in cards
    for level in ("pack", "booster", "card"):
        assert f'[data-level="{level}"]' in families
        assert "--card-title-size" in families


def test_motion_is_limited_to_flip_and_respects_reduced_motion() -> None:
    cards = _text(STYLES / "cards.css")
    assert "rotateY(180deg)" in cards
    assert "@media (prefers-reduced-motion: reduce)" in cards
    assert "animation: none !important" in cards
    assert ":hover" not in cards


def test_family_palettes_do_not_redefine_status_authority() -> None:
    families = _text(STYLES / "families.css")
    for family in ("knowledge", "skills", "tools", "affaires"):
        assert f'[data-family="{family}"]' in families
    assert "--status-ready" not in families
    assert "--status-review" not in families


def test_mobile_surface_keeps_navigation_controls_and_card_first_layout() -> None:
    html = _text(HTML)
    cockpit = _text(STYLES / "cockpit.css")
    for control_id in ("v2-previous", "v2-next", "v2-descend", "v2-ascend", "v2-flip"):
        assert f'id="{control_id}"' in html
    assert "@media" in cockpit
    assert ".v3-stage" in cockpit
    assert ".v2-navigation" in cockpit or ".v3-navigation" in cockpit


def test_live_stage_has_a_definite_viewport_height() -> None:
    cockpit = _text(STYLES / "cockpit.css")
    assert "height: 100dvh" in cockpit
    assert ".v3-stage" in cockpit
    assert "height: 100%" in cockpit
    assert ".v3-stage .swiper-wrapper" in cockpit


def test_live_schema_cards_are_normalized_before_entering_the_design_system() -> None:
    cards = _text(STYLES / "cards.css")
    adapter = _text(COCKPIT / "v3_swiper.js")

    for historical_selector in (
        ".v2-card",
        ".v2-card-inner",
        ".v2-card-face",
        ".v2-card-front",
        ".v2-card-back",
    ):
        assert historical_selector not in cards

    assert "function normalizeCard" in adapter
    assert "normalizeCard(renderCard(model), model)" in adapter
    assert 'classList.add("card")' in adapter
    assert 'dataset.level' in adapter
    assert 'dataset.family' in adapter
    assert 'dataset.kind' in adapter
    assert 'dataset.status' in adapter


def test_affaires_pack_blobs_use_two_axis_offsets_and_equal_viewport_size() -> None:
    families = _text(STYLES / "families.css")
    assert "--blob-width: 75vw" in families
    assert "--blob-height: 75vw" in families
    assert "--blob-shift-x: calc(50% + min(10vw, 6rem))" in families
    assert "--blob-shift-x: calc(50% - min(10vw, 6rem))" in families
    assert "--blob-shift-y: calc(-50% - min(10vw, 6rem))" in families
    assert "--blob-shift-y: calc(-50% + min(10vw, 6rem))" in families


def test_demo_flip_uses_neutral_card_contract_for_click_button_and_keyboard() -> None:
    demo = _text(COCKPIT / "v3" / "demo_collection_app.js")
    assert 'querySelector(".card")' in demo
    assert 'querySelector(".v2-card")' not in demo
    assert "function toggleFlip(card)" in demo
    assert 'card.addEventListener("click"' in demo
    assert 'card.addEventListener("keydown"' in demo
