from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
STYLES = COCKPIT / "styles"


def test_canonical_page_loads_only_current_visual_authorities() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    expected = (
        'href="styles/cockpit.css"',
        'href="styles/cards.css"',
        'href="styles/families.css"',
        'href="styles/editors.css"',
    )
    for reference in expected:
        assert reference in html
    assert html.index(expected[0]) < html.index(expected[1]) < html.index(expected[2]) < html.index(expected[3])
    for retired in ("v2.css", "v2_refinement.css", "v3_living_cards.css", "v3_card_blobs.css"):
        assert retired not in html


def test_renderer_emits_semantic_card_dom_without_decorative_nodes() -> None:
    renderer = (COCKPIT / "v3" / "collection" / "card_renderer.js").read_text(encoding="utf-8")
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")

    assert "article.dataset.variant = stableVariant(item.id)" in renderer
    for decorative_term in ("blobPrimitive", "card-blobs", "card-blob", "markerPrimitive", "effectPrimitive"):
        assert decorative_term not in renderer
    assert ".card-front::before" in cards
    assert ".card-front::after" in cards
    assert ".card-body::before" in cards
    assert ".card-top::after" in cards
    assert ".card-back::after" in cards
    assert "<svg" not in renderer.lower()


def test_family_visuals_are_variables_not_layout_geometry() -> None:
    families = (STYLES / "families.css").read_text(encoding="utf-8")
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")

    for family in ("pantheon", "affaires", "knowledge", "skills", "tools"):
        assert f'[data-family="{family}"]' in families
    for kind in ("project", "work", "folder"):
        assert f'[data-kind="{kind}"]' in families
    assert "display:" not in families
    assert "position:" not in families
    assert '[data-family="knowledge"]' not in cards
    assert '[data-kind="work"]' not in cards


def test_markers_frames_and_effects_keep_flat_visual_language() -> None:
    cockpit = (STYLES / "cockpit.css").read_text(encoding="utf-8")
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert "--cockpit-accent-size: 12px" in cockpit
    assert "--cockpit-back-border-general: 12px" in cockpit
    assert "var(--cockpit-accent-size)" in families
    assert "var(--pantheon-cyan)" in families
    assert "var(--pantheon-yellow)" in families
    assert "var(--pantheon-magenta)" in families
    assert "border-radius: 50%" not in families
    for forbidden in ("box-shadow", "filter: blur", "backdrop-filter"):
        assert forbidden not in cards
        assert forbidden not in families


def test_shared_effect_geometry_is_card_relative_and_viewport_independent() -> None:
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert "width: var(--effect-width, 75%)" in cards
    assert "height: var(--effect-height, 75%)" in cards
    assert "top: var(--effect-top, 50%)" in cards
    assert "left: var(--effect-left, 50%)" in cards
    assert "translate(-50%, -50%)" in cards
    for index in (1, 2, 3):
        assert f"--effect-{index}-" in cards
    for viewport_unit in ("75vw", "75vh", "min(10vw", "@media screen"):
        assert viewport_unit not in families


def test_css_alone_decides_which_cards_receive_decorative_effects() -> None:
    renderer = (COCKPIT / "v3" / "collection" / "card_renderer.js").read_text(encoding="utf-8")
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert "--effects-opacity: 1" in families
    assert '[data-family="pantheon"]' in families
    assert '[data-family="affaires"]' in families
    assert '[data-kind="project"]' in families
    assert "effects-opacity" not in renderer
    assert "effect-1" not in renderer


def test_affaires_reuses_shared_effect_geometry_with_colour_only_variation() -> None:
    families = (STYLES / "families.css").read_text(encoding="utf-8")
    affaires = families.split('[data-family="affaires"] {', 1)[1].split("}", 1)[0]

    assert "--effects-opacity: 1" in affaires
    assert "--effect-1-fill: #ffd952" in affaires
    assert "--effect-2-fill: #c64035" in affaires
    assert "--effect-3-fill: #822767" in affaires


def test_pantheon_effects_are_transparent_with_one_pixel_opaque_outlines() -> None:
    families = (STYLES / "families.css").read_text(encoding="utf-8")
    pantheon = families.split('[data-family="pantheon"] {', 1)[1].split("}", 1)[0]

    assert "--effect-border-width: 1px" in pantheon
    assert "--effect-1-color: var(--pantheon-cyan)" in pantheon
    assert "--effect-2-color: var(--pantheon-yellow)" in pantheon
    assert "--effect-3-color: var(--pantheon-magenta)" in pantheon
    assert "--effect-1-fill" not in pantheon


def test_family_visuals_do_not_change_business_model() -> None:
    renderer = (COCKPIT / "v3" / "collection" / "card_renderer.js").read_text(encoding="utf-8")
    provider = (COCKPIT / "v3" / "providers" / "demo_provider.js").read_text(encoding="utf-8")

    assert "article.dataset.family" in renderer
    assert "article.dataset.level" in renderer
    assert "article.dataset.kind" in renderer
    assert '"project"' in provider
    assert '"work"' in provider
    for visual_file in ("cockpit.css", "cards.css", "families.css", "editors.css"):
        assert visual_file not in renderer
        assert visual_file not in provider


def test_visual_language_document_keeps_presentation_boundary_explicit() -> None:
    document = (ROOT / "docs" / "cockpit" / "CARD_VISUAL_LANGUAGE.md").read_text(encoding="utf-8")
    assert "visual projection != semantic model" in document
    assert "project colour != status" in document
    assert "UI status != authorization" in document
