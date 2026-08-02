from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRUCTURED_INTERFACE = ROOT / "mvp_vertical" / "cockpit" / "structured_interface.js"


def test_root_spaces_fail_closed_without_projection_definition() -> None:
    source = STRUCTURED_INTERFACE.read_text(encoding="utf-8")
    assert "Root card projection definition unavailable" in source
    assert "if (!definition)" in source


def test_non_root_cards_remain_unaffected() -> None:
    source = STRUCTURED_INTERFACE.read_text(encoding="utf-8")
    assert 'input?.entity_type !== "cockpit_space"' in source
    assert "if (!rootDefinition) return projection;" in source


def test_root_definition_still_controls_projection_metadata() -> None:
    source = STRUCTURED_INTERFACE.read_text(encoding="utf-8")
    for token in (
        "rootDefinition.card_role",
        "rootDefinition.presentation_family",
        "rootDefinition.category",
        "rootDefinition.title",
        "rootDefinition.summary",
        "rootDefinition.status",
        "rootDefinition.detail_rows",
    ):
        assert token in source
