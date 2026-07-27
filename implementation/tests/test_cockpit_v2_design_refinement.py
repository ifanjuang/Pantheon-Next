from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
HTML = COCKPIT / "v2.html"
REFINEMENT = COCKPIT / "styles" / "v2_refinement.css"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_refinement_is_loaded_after_base_v2_styles() -> None:
    html = _text(HTML)
    assert html.index('href="styles/v2.css"') < html.index('href="styles/v2_refinement.css"')


def test_card_typography_is_editorial_not_poster_scaled() -> None:
    css = _text(REFINEMENT)
    assert 'font-family: var(--font-body);' in css
    assert 'font-size: clamp(2.15rem, 6.5vw, 3.45rem);' in css
    assert 'letter-spacing: -.045em;' in css
    assert 'text-transform: none;' in css
    assert '4.4rem' not in css


def test_spatial_sibling_cues_exist_only_when_navigation_is_available() -> None:
    css = _text(REFINEMENT)
    assert '.v2-shell:has(#v2-previous:not(:disabled)) .v2-stage::before' in css
    assert '.v2-shell:has(#v2-next:not(:disabled)) .v2-stage::after' in css
    assert '.v2-stage[data-spatial-navigation="locked-on-back"]::before' in css
    assert '.v2-stage[data-spatial-navigation="locked-on-back"]::after' in css


def test_motion_is_low_amplitude_and_respects_reduced_motion() -> None:
    css = _text(REFINEMENT)
    assert 'translateX(1.25rem)' in css
    assert 'translateY(1.5rem)' in css
    assert '190ms var(--ease-out)' in css
    assert '210ms var(--ease-out)' in css
    assert '@media (prefers-reduced-motion: reduce)' in css
    assert 'animation: none !important;' in css


def test_family_palettes_are_muted_and_status_colors_are_not_redefined() -> None:
    css = _text(REFINEMENT)
    assert '--family-a: #fcfbf8;' in css
    assert '--family-a: #f3f5f6;' in css
    assert '--family-a: #f5ece4;' in css
    assert '--family-a: #f0eef6;' in css
    assert '--status-ready' not in css
    assert '--status-review' not in css


def test_back_face_copy_explains_interaction_model() -> None:
    html = _text(HTML)
    assert 'Recto : ← → frères · ↑ enfants · ↓ parent.' in html
    assert 'Verso : inspection, défilement et actions locales.' in html
