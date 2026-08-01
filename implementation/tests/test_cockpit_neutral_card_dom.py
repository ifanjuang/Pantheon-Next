from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"


def test_live_adapter_normalizes_legacy_renderer_output() -> None:
    adapter = (COCKPIT / "live_collection_adapter.js").read_text(encoding="utf-8")

    assert "const CLASS_MAP" in adapter
    assert '"v2-card": "card"' in adapter
    assert '"v2-card-inner": "card-inner"' in adapter
    assert '"v2-card-face": "card-face"' in adapter
    assert "normalizeCard(renderCard(model), model)" in adapter
    assert "node.dataset.level" in adapter
    assert "node.dataset.family" in adapter
    assert "node.dataset.kind" in adapter
    assert "--project-accent" in adapter


def test_live_adapter_does_not_inject_decorative_dom() -> None:
    adapter = (COCKPIT / "live_collection_adapter.js").read_text(encoding="utf-8")

    for decorative_contract in (
        "ensureBlobPrimitive",
        "card-blobs",
        "card-blob",
        "index <= 3",
    ):
        assert decorative_contract not in adapter


def test_canonical_card_css_has_no_legacy_or_decorative_dom_selectors() -> None:
    cards = (COCKPIT / "styles" / "cards.css").read_text(encoding="utf-8")

    for legacy in (
        ".v2-card",
        ".v2-card-inner",
        ".v2-card-face",
        ".v2-card-front",
        ".v2-card-back",
        ".v2-card-title",
    ):
        assert legacy not in cards

    for primitive in (
        ".card",
        ".card-inner",
        ".card-face",
        ".card-front",
        ".card-back",
    ):
        assert primitive in cards

    for decorative_dom_selector in (".card-blobs", ".card-blob"):
        assert decorative_dom_selector not in cards

    for css_effect_layer in (
        ".card-front::before",
        ".card-front::after",
        ".card-body::before",
        ".card-back::after",
        ".card-top::after",
    ):
        assert css_effect_layer in cards
