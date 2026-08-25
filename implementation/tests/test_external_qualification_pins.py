from __future__ import annotations

import json
import re
from pathlib import Path

from tools.export_external_qualification_pins import REGISTRY, selected_exports

ROOT = Path(__file__).resolve().parents[2]


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


def test_exporter_emits_standardized_component_environment() -> None:
    values = selected_exports(
        [
            "hermes-agent",
            "hindsight",
            "hindsight-obsidian-sync",
            "self-hosted-livesync",
            "self-hosted-livesync-cli",
            "obsidian-desktop",
            "couchdb",
        ]
    )
    assert values["HERMES_VERSION"] == "0.20.5"
    assert values["HERMES_REF"] == "fcbd1076a93841fa88855acce810e342a5b78101"
    assert values["HINDSIGHT_VERSION"] == "0.9.1"
    assert values["HINDSIGHT_OBSIDIAN_VERSION"] == "0.2.1"
    assert values["HINDSIGHT_OBSIDIAN_REF"] == "daf529aacad14a5b8f7db9f34a7f49c9e3629b61"
    assert values["LIVESYNC_VERSION"] == "1.0.18"
    assert values["LIVESYNC_REF"] == "32e827692f1a552cd581de9da45cecd0711573d3"
    assert values["LIVESYNC_CLI_VERSION"] == "1.0.18-cli"
    assert values["OBSIDIAN_VERSION"] == "1.13.7"
    assert values["COUCHDB_VERSION"] == "3.5.0"


def test_current_workflows_must_not_gain_new_literal_pin_copies() -> None:
    """The registry is the current-pin authority; historical records are excluded."""
    data = _registry()
    forbidden = set()
    for pin in data["pins"].values():
        forbidden.add(pin["version"])
        if pin.get("ref"):
            forbidden.add(pin["ref"])

    # During migration old workflows still contain literals. New/updated workflows
    # opt into the registry by containing this marker. Once all active workflows
    # are migrated this test can be tightened to forbid every literal globally.
    workflow_root = ROOT / ".github" / "workflows"
    migrated = [
        path
        for path in workflow_root.glob("*.yml")
        if "export_external_qualification_pins.py" in path.read_text(encoding="utf-8")
    ]
    for path in migrated:
        text = path.read_text(encoding="utf-8")
        for literal in forbidden:
            assert literal not in text, f"{path} duplicates canonical pin {literal}"
