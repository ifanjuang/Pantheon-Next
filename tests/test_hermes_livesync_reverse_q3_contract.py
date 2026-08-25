from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "hermes-livesync-reverse-q3.yml"
HARNESS = ROOT / "implementation" / "tools" / "run_hermes_livesync_reverse_q3.sh"

HERMES_COMMIT = "4c1f53be10d0fce1d25aee1975e5149b6c54f25a"
SKILL_BLOB = "cc8f3cf737a78fc68e73e5770ef0158815cb4028"
LIVESYNC_COMMIT = "32e827692f1a552cd581de9da45cecd0711573d3"


def test_q3_pins_exact_hermes_skill_and_qualified_livesync() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert HERMES_COMMIT in raw
    assert SKILL_BLOB in raw
    assert LIVESYNC_COMMIT in raw
    assert "1.0.18-cli" in raw
    assert "couchdb:3.5.0" in HARNESS.read_text(encoding="utf-8")
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


def test_q3_preserves_sync_memory_authority_boundaries() -> None:
    raw = HARNESS.read_text(encoding="utf-8")
    assert 'hermes_direct_couchdb_write": False' in raw
    assert 'hindsight_ingestion_activated": False' in raw
    assert 'pantheon_state_mutated": False' in raw
    assert 'evidence_admitted": False' in raw
    assert 'delete_qualified": False' in raw
    assert 'move_rename_qualified": False' in raw
    assert "hindsight-obsidian-sync" not in raw
