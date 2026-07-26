import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "mvp_vertical" / "cockpit" / "registries"
REQUIRED_TAG_KEYS = {"slug", "title", "description", "icon_key", "color"}


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
    for filename in ("type_tags.json", "subject_tags.json"):
        payload = _load(filename)
        assert payload["version"] >= 1
        assert payload["kind"] in {"type_tags", "subject_tags"}
        assert payload["tags"]
        for item in payload["tags"]:
            missing = REQUIRED_TAG_KEYS - item.keys()
            assert not missing, f"{filename}:{item.get('slug')} missing {sorted(missing)}"
            assert all(str(item[key]).strip() for key in REQUIRED_TAG_KEYS)


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
