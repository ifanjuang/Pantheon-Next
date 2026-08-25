from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "hermes-livesync-reverse-q3.yml"
HARNESS = ROOT / "implementation" / "tools" / "run_hermes_livesync_reverse_q3.sh"


def test_q3_resolves_current_external_pins_from_registry() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert "export_external_qualification_pins.py" in raw
    assert "hermes-agent self-hosted-livesync self-hosted-livesync-cli couchdb" in raw
    assert "HERMES_REPOSITORY" in raw
    assert "HERMES_REF" in raw
    assert "LIVESYNC_REPOSITORY" in raw
    assert "LIVESYNC_REF" in raw
    assert "HERMES_OBSIDIAN_SKILL_BLOB" not in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_q3_uses_real_hermes_file_tools_then_existing_livesync_composition() -> None:
    raw = HARNESS.read_text(encoding="utf-8")
    assert raw.startswith("#!/usr/bin/env bash\nset -euo pipefail")
    assert "from tools.file_tools import patch_tool, read_file_tool, write_file_tool" in raw
    assert "write_file_tool(str(note), content)" in raw
    assert "read_file_tool(str(note))" in raw
    assert "patch_tool(" in raw
    assert '--vault "$NAS_VAULT" --interval 1 daemon' in raw
    assert "PANTHEON_HERMES_LIVESYNC_CREATE" in raw
    assert "PANTHEON_HERMES_LIVESYNC_PATCH" in raw
    assert "wait_for_client_marker" in raw
    assert 'second_client_kind": "self-hosted-livesync-cli-local-db"' in raw
    assert 'native_obsidian_client_verified": False' in raw
    assert '"${COUCHDB_IMAGE}:${COUCHDB_VERSION}"' in raw


def test_q3_preserves_sync_memory_authority_boundaries() -> None:
    raw = HARNESS.read_text(encoding="utf-8")
    assert 'hermes_direct_couchdb_write": False' in raw
    assert 'hindsight_ingestion_activated": False' in raw
    assert 'pantheon_state_mutated": False' in raw
    assert 'evidence_admitted": False' in raw
    assert 'delete_qualified": False' in raw
    assert 'move_rename_qualified": False' in raw
    assert "hindsight-obsidian-sync" not in raw
