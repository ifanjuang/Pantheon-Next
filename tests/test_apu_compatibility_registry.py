from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "schemas" / "architecture-project-understanding" / "compatibility.registry.yaml"


def _registry() -> dict:
    value = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_compatibility_registry_has_one_explicit_emission_posture_per_carrier() -> None:
    registry = _registry()
    assert registry["registry_id"] == "project-anatomy-v02-compatibility"
    assert registry["version"] == "0.2"
    entries = registry["entries"]
    assert isinstance(entries, dict) and entries
    for name, entry in entries.items():
        assert entry["status"] in {"canonical", "support", "compatibility_only"}, name
        assert isinstance(entry["canonical_emission"], bool), name
        assert entry["replacement"], name
        if entry["status"] == "compatibility_only":
            assert entry["canonical_emission"] is False, name


def test_v02_has_one_identity_value_and_relation_emission_path() -> None:
    entries = _registry()["entries"]
    assert entries["stable_object"] == {
        "status": "canonical",
        "canonical_emission": True,
        "replacement": "stable_object",
    }
    assert entries["attribute_claim"]["status"] == "canonical"
    assert entries["relation_claim"]["status"] == "canonical"
    assert entries["source_representation"]["status"] == "canonical"

    assert entries["object_identity"]["canonical_emission"] is False
    assert entries["stable_object.matches"]["canonical_emission"] is False
    assert entries["object_relation"]["canonical_emission"] is False
    assert entries["property_set"]["canonical_emission"] is False


def test_duplicate_governance_carriers_are_compatibility_only() -> None:
    entries = _registry()["entries"]
    for name in (
        "evidence",
        "doubt",
        "object_note",
        "program_change",
        "deviation",
        "canonization",
    ):
        assert entries[name]["status"] == "compatibility_only"
        assert entries[name]["canonical_emission"] is False
