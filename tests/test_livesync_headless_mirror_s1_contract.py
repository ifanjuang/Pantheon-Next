from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-headless-mirror-s1.yml"
SEQUENCE = ROOT / "implementation" / "tools" / "run_livesync_headless_mirror_s1.sh"


def test_s1_loads_reviewed_livesync_cli_and_couchdb_pins() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    sequence = SEQUENCE.read_text(encoding="utf-8")
    assert "export_external_qualification_pins.py" in raw
    assert "self-hosted-livesync self-hosted-livesync-cli couchdb" in raw
    assert "${{ env.LIVESYNC_REPOSITORY }}" in raw
    assert "${{ env.LIVESYNC_REF }}" in raw
    assert "LIVESYNC_CLI_VERSION" in raw
    assert 'COUCHDB_QUALIFIED_IMAGE="${COUCHDB_IMAGE}:${COUCHDB_VERSION}"' in sequence
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
