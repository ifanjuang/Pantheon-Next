from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "mvp_vertical" / "cockpit" / "registries" / "materials.json"
RETIRED_PATH = ROOT / "mvp_vertical" / "cockpit" / "v3" / "materials.json"


def test_material_registry_has_stable_identity_and_unique_materials() -> None:
    payload = json.loads(REGISTRY.read_text(encoding="utf-8"))

    assert payload["schema_id"] == "cockpit.materials"
    assert payload["revision"] == 1
    assert "schema_version" not in payload
    assert payload["assignment"] == {
        "strategy": "stable-entity-hash",
        "fallback_key": "projection-index",
    }

    materials = payload["materials"]
    identifiers = [material["id"] for material in materials]
    assert len(materials) == 12
    assert len(identifiers) == len(set(identifiers))
    assert all(len(material["stops"]) >= 5 for material in materials)


def test_generation_named_material_path_is_retired() -> None:
    assert REGISTRY.is_file()
    assert not RETIRED_PATH.exists()
