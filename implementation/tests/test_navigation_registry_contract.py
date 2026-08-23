"""Validate the operational Navigation Registry against the vendored Pantheon contract."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "mvp_vertical" / "cockpit" / "registries" / "navigation_registry.json"
SCHEMA_PATH = ROOT / "mvp_vertical" / "vendor" / "pantheon" / "navigation_registry.schema.yaml"
SOURCE_PATH = ROOT / "mvp_vertical" / "vendor" / "pantheon" / "navigation_registry.source.json"


def _registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def _schema() -> dict:
    return yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_operational_navigation_registry_validates_against_vendored_schema() -> None:
    schema = _schema()
    registry = _registry()
    jsonschema.Draft202012Validator.check_schema(schema)
    errors = sorted(
        jsonschema.Draft202012Validator(schema).iter_errors(registry),
        key=lambda error: list(error.path),
    )
    assert not errors, "\n".join(
        f"{'.'.join(map(str, error.path)) or '<root>'}: {error.message}"
        for error in errors
    )


def test_root_identities_and_sources_are_unique() -> None:
    registry = _registry()
    items = registry["root_collection"]["items"]
    identities = [item["id"] for item in items]
    assert identities == [
        "space:pantheon",
        "space:affaires",
        "space:connaissances",
        "space:workspace",
        "space:outils",
        "space:decisions",
    ]
    assert len(identities) == len(set(identities))
    assert all(len(item["sources"]) == len(set(item["sources"])) for item in items)


def test_vendored_schema_matches_recorded_source_digest() -> None:
    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    digest = sha256(SCHEMA_PATH.read_bytes()).hexdigest()
    assert source["source_repository"] == "ifanjuang/Pantheon-Next"
    assert source["source_path"] == "schemas/navigation_registry.schema.yaml"
    assert source["source_pull_request"] == 519
    assert source["source_commit"] == "1cbf5853838568f1ba235cea15bf53c9588bf8e6"
    assert source["posture"] == "vendored-reference"
    assert source["authority_transfer"] is False
    assert digest == source["sha256"]


def test_navigation_registry_boundaries_remain_non_authoritative() -> None:
    schema_text = SCHEMA_PATH.read_text(encoding="utf-8")
    for token in (
        "endpoint_routing: false",
        "child_assembly: false",
        "runtime_execution: false",
        "task_authorization: false",
        "approval: false",
        "evidence_qualification: false",
    ):
        assert token in schema_text
