import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "mvp_vertical" / "cockpit" / "registries"
REQUIRED_TAG_KEYS = {"slug", "title", "description", "icon_provider", "icon_key", "color"}


def _load(name: str) -> dict:
    return json.loads((REGISTRY_DIR / name).read_text(encoding="utf-8"))


def _slugs(payload: dict) -> set[str]:
    return {item["slug"] for item in payload["tags"]}


def test_type_and_subject_tag_registries_are_disjoint() -> None:
    type_tags = _load("type_tags.json")
    subject_tags = _load("subject_tags.json")

    overlap = _slugs(type_tags) & _slugs(subject_tags)
    assert not overlap, f"tag slugs must belong to one vocabulary only: {sorted(overlap)}"


def test_tag_registry_entries_have_complete_presentation_metadata() -> None:
    icon_css = (ROOT / "mvp_vertical" / "cockpit" / "styles" / "cards.css").read_text(encoding="utf-8")
    radix_keys = set(re.findall(r'\.radix-icon\[data-icon="([^"]+)"\]', icon_css))
    for filename in ("type_tags.json", "subject_tags.json"):
        payload = _load(filename)
        assert payload["version"] >= 1
        assert payload["kind"] in {"type_tags", "subject_tags"}
        assert payload["tags"]
        for item in payload["tags"]:
            missing = REQUIRED_TAG_KEYS - item.keys()
            assert not missing, f"{filename}:{item.get('slug')} missing {sorted(missing)}"
            assert all(str(item[key]).strip() for key in REQUIRED_TAG_KEYS)
            assert item["icon_provider"] in {"radix", "material-symbols"}
            if item["icon_provider"] == "radix":
                assert item["icon_key"] in radix_keys, f"{filename}:{item['slug']} references an unvendored Radix icon"
            else:
                assert re.fullmatch(r"[a-z0-9_]+", item["icon_key"])


def test_every_rendered_tag_has_an_icon_including_unknown_tags() -> None:
    renderer = (ROOT / "mvp_vertical" / "cockpit" / "rendering" / "card_renderer.js").read_text(encoding="utf-8")
    tag_icons = (ROOT / "mvp_vertical" / "cockpit" / "rendering" / "tag_icons.js").read_text(encoding="utf-8")
    index = (ROOT / "mvp_vertical" / "cockpit" / "index.html").read_text(encoding="utf-8")

    assert 'import { createTagToken } from "./tag_icons.js"' in renderer
    assert 'icon_key: "label"' in tag_icons
    assert "styles/cards.css" in index
    assert "Material+Symbols+Rounded" in index


def test_dce_is_a_type_tag_not_a_subject_tag() -> None:
    type_tags = _load("type_tags.json")
    subject_tags = _load("subject_tags.json")

    assert "dce" in _slugs(type_tags)
    assert "dce" not in _slugs(subject_tags)


def test_status_and_limit_registries_remain_separate_from_tags() -> None:
    type_slugs = _slugs(_load("type_tags.json"))
    subject_slugs = _slugs(_load("subject_tags.json"))
    classification_slugs = type_slugs | subject_slugs

    for filename in ("status_registry.json", "limit_registry.json"):
        payload = _load(filename)
        values = payload["values"]
        assert values
        for item in values:
            assert {"slug", "title", "icon_key", "color"} <= item.keys()
            assert item["slug"] not in classification_slugs
