from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
REGISTRY = COCKPIT / "registries" / "navigation_registry.json"


def test_navigation_registry_declares_stable_roots_and_abstract_sources() -> None:
    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))

    assert payload["schema_version"] == "cockpit.navigation.registry.v1"
    root = payload["root_collection"]
    assert root["id"] == "primary-spaces"
    assert [item["id"] for item in root["items"]] == [
        "space:pantheon",
        "space:affaires",
        "space:connaissances",
        "space:outils",
    ]
    assert root["items"][0]["sources"] == [
        "pending_change_candidates",
        "work_decisions",
        "current_runs",
    ]
    assert root["items"][1]["sources"] == ["projects"]
    assert root["items"][2]["sources"] == ["knowledge"]
    assert root["items"][3]["sources"] == ["tools"]


def test_navigation_registry_is_loaded_before_the_projection() -> None:
    bootstrap = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")

    loader_import = 'import("./projection/navigation_registry_loader.js")'
    adapter = '"projection/navigation_registry_adapter.js"'
    projection = '"projection/cockpit_projection.js"'

    assert loader_import in bootstrap
    assert "await loadNavigationRegistry();" in bootstrap
    assert adapter in bootstrap
    assert bootstrap.index(adapter) < bootstrap.index(projection)


def test_navigation_registry_loader_is_strict_and_not_authoritative() -> None:
    loader = (COCKPIT / "projection" / "navigation_registry_loader.js").read_text(encoding="utf-8")
    adapter = (COCKPIT / "projection" / "navigation_registry_adapter.js").read_text(encoding="utf-8")

    assert "ALLOWED_SOURCES" in loader
    assert "Duplicate navigation root" in loader
    assert "Unknown navigation source" in loader
    assert "root_collection_id: root.id" in adapter
    assert "root_item_ids: root.items.map(item => item.id)" in adapter

    forbidden = (
        "Authorization",
        "ChangeCandidate",
        "Evidence",
        "approved =",
        "task_authorized",
        "fetch(\"../v1",
    )
    for token in forbidden:
        assert token not in adapter
