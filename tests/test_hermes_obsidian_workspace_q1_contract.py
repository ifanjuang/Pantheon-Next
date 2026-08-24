from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "hermes-obsidian-workspace-q1.yml"

HERMES_COMMIT = "f14059fad20e17acf2512785114791566e70bd06"
SKILL_BLOB = "cc8f3cf737a78fc68e73e5770ef0158815cb4028"


def test_q1_pins_exact_current_upstream_hermes_and_skill_blob() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert HERMES_COMMIT in raw
    assert SKILL_BLOB in raw
    assert "NousResearch/hermes-agent" in raw
    assert "skills/note-taking/obsidian/SKILL.md" in raw
    assert "latest" not in raw.lower()


def test_q1_exercises_actual_hermes_file_tools_on_synthetic_workspace() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert "write_file_tool" in raw
    assert "read_file_tool" in raw
    assert "patch_tool" in raw
    assert "PANTHEON_HERMES_OBSIDIAN_CREATE" in raw
    assert "PANTHEON_HERMES_OBSIDIAN_PATCH" in raw
    assert 'workspace / "Affaires" / "Alpha" / "note.md"' in raw
    assert "outside.md" in raw
    assert '"raw_tool_root_enforcement": False' in raw


def test_q1_preserves_authority_and_destructive_operation_boundaries() -> None:
    raw = WORKFLOW.read_text(encoding="utf-8")
    assert '"couchdb_direct_write": False' in raw
    assert '"hindsight_direct_write": False' in raw
    assert '"pantheon_state_mutated": False' in raw
    assert '"evidence_admitted": False' in raw
    assert '"delete_qualified": False' in raw
    assert '"move_rename_qualified": False' in raw
    assert "whole_file_overwrite_without_pantheon_revision_gate" in raw
