from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = (
    ROOT
    / "docs"
    / "governance"
    / "authority"
    / "PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json"
)


def _registry() -> dict:
    value = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_system_ownership_uses_logical_responsibility_identities() -> None:
    registry = _registry()

    assert registry["revision"] == 3
    assert set(registry["owners"]) == {
        "Pantheon governance",
        "Pantheon implementation",
        "Hermes/external runtime",
        "Cockpit/OpenWebUI",
    }
    assert "Pantheon-Next" not in registry["owners"]
    assert "pantheon-mvp" not in registry["owners"]


def test_every_concept_owner_resolves_to_a_declared_logical_owner() -> None:
    registry = _registry()
    owners = set(registry["owners"])

    for concept in registry["concepts"]:
        for field in (
            "semantic_owner",
            "implementation_owner",
            "runtime_owner",
            "projection_owner",
        ):
            owner = concept.get(field)
            if owner is not None:
                assert owner in owners, f"{concept['id']}.{field} -> {owner}"


def test_repository_names_are_not_used_as_concept_owner_identities() -> None:
    registry = _registry()
    retired = {"Pantheon-Next", "pantheon-mvp"}

    for concept in registry["concepts"]:
        referenced = {
            concept.get("semantic_owner"),
            concept.get("implementation_owner"),
            concept.get("runtime_owner"),
            concept.get("projection_owner"),
        }
        assert not (retired & referenced), concept["id"]
