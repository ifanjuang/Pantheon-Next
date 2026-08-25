from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "hermes-hindsight-ingestion-q5.yml"
HARNESS = ROOT / "implementation" / "tools" / "run_hermes_hindsight_ingestion_q5.sh"

HERMES_COMMIT = "4c1f53be10d0fce1d25aee1975e5149b6c54f25a"
SKILL_BLOB = "cc8f3cf737a78fc68e73e5770ef0158815cb4028"
OBSIDIAN_SYNC_COMMIT = "daf529aacad14a5b8f7db9f34a7f49c9e3629b61"


def test_q5_pins_current_qualified_hindsight_matrix_and_hermes_skill() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert HERMES_COMMIT in raw
    assert SKILL_BLOB in raw
    assert OBSIDIAN_SYNC_COMMIT in raw
    assert 'HINDSIGHT_VERSION: "0.9.1"' in raw
    assert "p.version!=='0.2.1'" in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_q5_proves_hermes_file_write_is_not_hindsight_write_path() -> None:
    raw = HARNESS.read_text(encoding="utf-8")
    assert raw.startswith("#!/usr/bin/env bash\nset -euo pipefail")
    assert "from tools.file_tools import patch_tool, read_file_tool, write_file_tool" in raw
    assert "write_file_tool(str(note),content)" in raw
    assert "read_file_tool(str(note))" in raw
    assert "patch_tool(" in raw
    assert "AFTER_HERMES_CREATE=$(retain_batch_count)" in raw
    assert 'test "$BEFORE_CREATE" = "$AFTER_HERMES_CREATE"' in raw
    assert "AFTER_HERMES_PATCH=$(retain_batch_count)" in raw
    assert 'test "$BEFORE_PATCH" = "$AFTER_HERMES_PATCH"' in raw
    assert "pre-sync-create-recall.json" in raw
    assert "pre-sync-patch-recall.json" in raw


def test_q5_keeps_hindsight_obsidian_as_single_ingestion_producer() -> None:
    raw = HARNESS.read_text(encoding="utf-8")
    assert 'node "$CLI" reconcile' in raw
    assert "reconcile: +1 added" in raw
    assert "reconcile: +0 added, ~1 updated" in raw
    assert 'single_hindsight_producer_kind\':\'hindsight-obsidian-sync\'' in raw
    assert 'hermes_direct_hindsight_write\':False' in raw
    assert 'source_provenance_verified\':True' in raw
    assert 'hindsight_writeback_to_vault\':False' in raw
    assert 'pantheon_state_mutated\':False' in raw
    assert 'evidence_admitted\':False' in raw
    assert "sync_retain" not in raw
