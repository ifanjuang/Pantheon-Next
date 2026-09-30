from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PINS = ROOT / "implementation" / "qualification" / "external-pins.json"

REMOVED_ACTIVE_PATHS = (
    ".github/workflows/hermes-livesync-reverse-q3.yml",
    ".github/workflows/implementation-livesync-conflict-policy-s5.yml",
    ".github/workflows/implementation-livesync-headless-mirror-s1.yml",
    ".github/workflows/implementation-livesync-offline-reconnect-s4.yml",
    ".github/workflows/implementation-livesync-production-audit-s6.yml",
    ".github/workflows/implementation-livesync-real-obsidian-s2.yml",
    ".github/workflows/implementation-livesync-security-seed-reconnect-s3.yml",
    "deployment/ubuntu/configure-livesync-local",
    "deployment/ubuntu/configure-marker-local",
    "deployment/ubuntu/marker_idle_vram.py",
    "implementation/labs/livesync/pantheon-offline-reconnect-s4.ts",
    "implementation/tools/run_hermes_livesync_reverse_q3.sh",
    "implementation/tools/run_livesync_headless_mirror_s1.sh",
)

RETIRED_PINS = {
    "self-hosted-livesync",
    "self-hosted-livesync-cli",
    "couchdb",
}


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_livesync_active_surfaces_remain_retired() -> None:
    present = [
        relative
        for relative in REMOVED_ACTIVE_PATHS
        if (ROOT / relative).exists()
    ]
    assert present == []


def test_livesync_and_couchdb_are_not_active_qualification_pins() -> None:
    pins = json.loads(PINS.read_text(encoding="utf-8"))["pins"]
    assert RETIRED_PINS.isdisjoint(pins)

    # Do not over-retire adjacent optional tooling.
    assert "obsidian-desktop" in pins
    assert "hindsight-obsidian-sync" in pins


def test_ubuntu_baseline_cannot_install_or_update_livesync() -> None:
    for relative in (
        "deployment/ubuntu/install-node",
        "deployment/ubuntu/update-node",
        "deployment/ubuntu/release.env",
    ):
        text = _read(relative).lower()
        assert "livesync" not in text, relative
        assert "couchdb" not in text, relative


def test_ubuntu_shell_entrypoints_remain_syntactically_valid() -> None:
    for relative in (
        "deployment/ubuntu/install-node",
        "deployment/ubuntu/update-node",
    ):
        completed = subprocess.run(
            ["bash", "-n", str(ROOT / relative)],
            check=False,
            capture_output=True,
            text=True,
        )
        assert completed.returncode == 0, (
            f"{relative}: bash -n failed\n{completed.stderr}"
        )


def test_current_runtime_docs_classify_livesync_as_retired() -> None:
    status = _read("docs/governance/STATUS.md")
    what_runs = _read("docs/governance/WHAT_RUNS.md")
    obsolete = _read("docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md")

    assert "Self-hosted LiveSync     -> retired / no current target role" in status
    assert "architecture_status: retired" in what_runs
    assert "LiveSync/CouchDB -> retired; Git history only" in what_runs
    assert "Former Self-hosted LiveSync/CouchDB qualification and Ubuntu mirror path" in obsolete


def test_direct_affaires_topology_survives_retirement() -> None:
    status = _read("docs/governance/STATUS.md")
    assert "NAS / AFFAIRES" in status
    assert "Workspace daemon" in status
    assert "Hindsight" in status
