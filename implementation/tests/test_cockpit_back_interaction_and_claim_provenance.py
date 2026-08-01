from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
HTML = COCKPIT / "index.html"
POLICY = COCKPIT / "interactions" / "interaction_policy.js"
CLAIMS = COCKPIT / "project_claim_view_adapter.js"
CLAIM_CSS = COCKPIT / "styles" / "editors.css"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_v2_loads_back_face_interaction_policy_after_renderer() -> None:
    bootstrap = _text(COCKPIT / "live_bootstrap.js")

    assert '"v2_app_schema.js"' in bootstrap
    assert '"interactions/interaction_policy.js"' in bootstrap
    assert bootstrap.index('"v2_app_schema.js"') < bootstrap.index('"interactions/interaction_policy.js"')


def test_back_face_blocks_spatial_swipe_and_keyboard_navigation_only() -> None:
    policy = _text(POLICY)

    assert 'currentCard()?.dataset.flipped === "true"' in policy
    assert 'stage.addEventListener("pointerdown", stopSpatialPointer, true)' in policy
    assert 'stage.addEventListener("pointerup", stopSpatialPointer, true)' in policy
    assert 'document.addEventListener("keydown", stopSpatialKeys, true)' in policy
    assert 'event.stopImmediatePropagation();' in policy
    assert '"v2-flip"' in policy
    assert 'const NAV_IDS = ["v2-previous", "v2-next", "v2-ascend", "v2-descend"]' in policy
    assert 'SPATIAL_KEYS = new Set(["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Enter"])' in policy
    assert '" "' not in policy


def test_project_claim_provenance_is_visible_and_can_open_backing_information() -> None:
    claims = _text(CLAIMS)

    assert 'provenance.textContent = `Provenance · ${label}`' in claims
    assert 'button.textContent = "Ouvrir la source"' in claims
    assert 'backing.entity_type === "information"' in claims
    assert 'const target = `information:${informationId}`' in claims
    assert 'descend.click();' in claims
    assert 'next.click();' in claims
    assert 'L’Information source n’est pas disponible dans le scope Projet courant.' in claims


def test_claim_provenance_remains_a_project_projection_not_a_claim_card() -> None:
    claims = _text(CLAIMS)

    assert 'section.dataset.projectClaimProjection = field.key' in claims
    assert 'data-project-claim-projection' in claims
    assert 'entity_type: "claim"' not in claims
    assert 'family: "claim"' not in claims


def test_claim_provenance_has_canonical_component_styles() -> None:
    css = _text(CLAIM_CSS)

    assert '.v2-claim-provenance' in css
    assert '.v2-claim-provenance-action' in css
    assert ':focus-visible' in css
