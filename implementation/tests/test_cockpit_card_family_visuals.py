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


def test_shared_blob_primitive_renders_three_css_shapes_with_stable_variants() -> None:
    renderer = (COCKPIT / "v3" / "collection" / "card_renderer.js").read_text(encoding="utf-8")
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert "function blobPrimitive()" in renderer
    assert "index <= 3" in renderer
    assert "article.dataset.variant = stableVariant(item.id)" in renderer
    for selector in (".card-blob--1", ".card-blob--2", ".card-blob--3"):
        assert selector in families
    assert "border-radius: var(--blob-radius" in cards
    assert "<svg" not in renderer.lower()
    assert "svg" not in cards.lower()
    assert "svg" not in families.lower()


def test_family_visuals_are_variables_not_geometry() -> None:
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


def test_markers_and_blobs_keep_flat_visual_language() -> None:
    cockpit = (STYLES / "cockpit.css").read_text(encoding="utf-8")
    cards = (STYLES / "cards.css").read_text(encoding="utf-8")
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert "--cockpit-accent-size: 12px" in cockpit
    assert "var(--cockpit-accent-size)" in families
    assert "var(--pantheon-cyan)" in families
    assert "var(--pantheon-yellow)" in families
    assert "var(--pantheon-magenta)" in families
    assert "border-radius: 50%" not in families
    for forbidden in ("box-shadow", "filter: blur", "backdrop-filter"):
        assert forbidden not in cards
        assert forbidden not in families


def test_affaires_pack_blobs_overlap_near_center_only_on_screen_layout() -> None:
    families = (STYLES / "families.css").read_text(encoding="utf-8")

    assert '@media screen and (min-width: 48rem)' in families
    for index in (1, 2, 3):
        selector = f'[data-level="pack"][data-family="affaires"] .card-blob--{index}'
        assert families.count(selector) == 2
    assert families.count("--blob-top: 50%") >= 1
    assert families.count("--blob-right: 50%") >= 1
    assert "--blob-shift-x: calc(50% + min(10vw, 6rem))" in families
    assert "--blob-shift-x: 50%" in families
    assert "--blob-shift-x: calc(50% - min(10vw, 6rem))" in families
    assert "--blob-shift-y: calc(-50% - min(10vw, 6rem))" in families
    assert "--blob-shift-y: -50%" in families
    assert "--blob-shift-y: calc(-50% + min(10vw, 6rem))" in families
    assert families.count("--blob-width: 75vw") == 1
    assert families.count("--blob-height: 75vw") == 1


def test_pantheon_blobs_are_transparent_with_one_pixel_opaque_outlines() -> None:
    families = (STYLES / "families.css").read_text(encoding="utf-8")
    pantheon = families.split('[data-family="pantheon"] {', 1)[1].split("}", 1)[0]

    assert "--blob-border-width: 1px" in pantheon
    assert "--blob-fill: transparent" in pantheon
    assert "--blob-opacity: 1" in pantheon


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
