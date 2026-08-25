from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from tools.export_external_qualification_pins import REGISTRY, selected_exports

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_HERMES_LOCK = ROOT / "implementation" / "hermes" / "distribution" / "pantheon-standard.lock.yaml"
HISTORICAL_ACTIVE_PATHS = {
    ROOT / ".github" / "workflows" / "implementation-hindsight-obsidian-hermes-o3-lab.yml",
    ROOT / "implementation" / "tools" / "run_hindsight_obsidian_hermes_o3.sh",
    ROOT / "implementation" / "tests" / "test_hindsight_obsidian_hermes_o3_contract.py",
}


def _registry() -> dict:
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_external_pin_registry_is_bounded_and_non_authoritative() -> None:
    data = _registry()
    assert data["schema_id"] == "pantheon.external_qualification_pins"
    assert data["revision"] == 1
    assert data["authority"] == {
        "deployment_truth": False,
        "installation_state": False,
        "runtime_activation": False,
        "task_authorization": False,
        "evidence_admission": False,
    }

    pins = data["pins"]
    assert set(pins) >= {
        "hermes-agent",
        "hindsight",
        "hindsight-obsidian-sync",
        "self-hosted-livesync",
        "self-hosted-livesync-cli",
        "obsidian-desktop",
        "couchdb",
        "mnemosyne-memory",
        "mnemosyne-hermes",
    }

    prefixes = [pin["env_prefix"] for pin in pins.values()]
    assert len(prefixes) == len(set(prefixes))
    assert all(re.fullmatch(r"[A-Z][A-Z0-9_]*", prefix) for prefix in prefixes)

    for pin_id, pin in pins.items():
        assert isinstance(pin["version"], str) and pin["version"]
        if pin["kind"] == "git":
            assert re.fullmatch(r"[0-9a-f]{40}", pin["ref"]), pin_id
            assert re.fullmatch(r"[^/\s]+/[^/\s]+", pin["repository"]), pin_id
        if pin["kind"] == "container":
            assert isinstance(pin["image"], str) and pin["image"], pin_id
            digest = pin.get("digest")
            assert digest is None or re.fullmatch(r"sha256:[0-9a-f]{64}", digest), pin_id
        source_pin = pin.get("source_pin")
        if source_pin is not None:
            assert source_pin in pins, (pin_id, source_pin)


def test_exporter_emits_registry_values_without_second_pin_authority() -> None:
    data = _registry()
    selected = [
        "hermes-agent",
        "hindsight",
        "hindsight-obsidian-sync",
        "self-hosted-livesync",
        "self-hosted-livesync-cli",
        "obsidian-desktop",
        "couchdb",
    ]
    values = selected_exports(selected)

    for pin_id in selected:
        pin = data["pins"][pin_id]
        prefix = pin["env_prefix"]
        assert values[f"{prefix}_PIN_ID"] == pin_id
        for field, suffix in {
            "version": "VERSION",
            "ref": "REF",
            "repository": "REPOSITORY",
            "image": "IMAGE",
            "package": "PACKAGE",
            "source_pin": "SOURCE_PIN",
        }.items():
            if pin.get(field) is not None:
                assert values[f"{prefix}_{suffix}"] == str(pin[field])


def test_candidate_hermes_distribution_snapshot_tracks_current_runtime_pin() -> None:
    data = _registry()
    lock = yaml.safe_load(CANDIDATE_HERMES_LOCK.read_text(encoding="utf-8"))
    assert lock["status"] == "candidate"
    assert (
        lock["source_pins"]["hermes_runtime"]["version"]
        == data["pins"]["hermes-agent"]["version"]
    )


def _current_pin_literals(data: dict) -> set[str]:
    literals: set[str] = set()
    for pin in data["pins"].values():
        literals.add(pin["version"])
        if pin.get("ref"):
            literals.add(pin["ref"])
    return literals


def _active_qualification_sources() -> list[Path]:
    roots = [
        ROOT / ".github" / "workflows",
        ROOT / "implementation" / "tools",
        ROOT / "implementation" / "tests",
        ROOT / "tests",
    ]
    suffixes = {".yml", ".yaml", ".py", ".sh", ".ts"}
    paths: list[Path] = []
    for root in roots:
        for path in root.rglob("*"):
            if path.is_file() and path.suffix in suffixes and path not in HISTORICAL_ACTIVE_PATHS:
                paths.append(path)
    return paths


def test_active_qualification_code_does_not_duplicate_current_pin_literals() -> None:
    """Current pins live in the registry; explicit historical fixtures are exempt."""
    forbidden = _current_pin_literals(_registry())
    for path in _active_qualification_sources():
        if path == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        for literal in forbidden:
            assert literal not in text, f"{path} duplicates canonical current pin {literal}"
