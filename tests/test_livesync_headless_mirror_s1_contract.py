from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-headless-mirror-s1.yml"
SEQUENCE = ROOT / "implementation" / "tools" / "run_livesync_headless_mirror_s1.sh"


def test_s1_pins_reviewed_livesync_release_and_couchdb() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert "32e827692f1a552cd581de9da45cecd0711573d3" in raw
    assert "1.0.18-cli" in raw
    assert "vrtmrz/obsidian-livesync" in raw
    assert "couchdb:3.5.0" in raw + SEQUENCE.read_text(encoding="utf-8")
    assert "edge" not in raw.lower()
    assert "latest" not in raw.lower()


def test_s1_proves_couchdb_to_separate_headless_vault_materialization() -> None:
    raw = SEQUENCE.read_text(encoding="utf-8")
    assert raw.startswith("#!/usr/bin/env bash\nset -euo pipefail")
    assert 'DB_B="$LAB_ROOT/nas-db"' in raw
    assert 'VAULT_B="$LAB_ROOT/nas-vault"' in raw
    assert '--vault "$VAULT_B" --interval 1 daemon' in raw
    assert "PANTHEON_LIVESYNC_CREATE" in raw
    assert "PANTHEON_LIVESYNC_EDIT" in raw
    assert "PANTHEON_LIVESYNC_RENAMED" in raw
    assert " rm Projects/Alpha/note.md" in raw
    assert " rm Projects/Alpha/renamed.md" in raw
    assert "wait_for_absence" in raw
    assert "nas_mode': 'daemon'" in raw
    assert "create_verified': True" in raw
    assert "edit_verified': True" in raw
    assert "rename_verified': True" in raw
    assert "delete_verified': True" in raw


def test_s1_does_not_activate_hindsight_or_create_pantheon_authority() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8") + SEQUENCE.read_text(encoding="utf-8")
    assert "hindsight_ingestion_activated': False" in raw
    assert "pantheon_state_mutated': False" in raw
    assert "evidence_admitted': False" in raw
    assert "hindsight-obsidian-sync" not in raw
    assert "Remotely Save" not in raw
    assert "secrets." not in raw
