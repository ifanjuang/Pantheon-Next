from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-conflict-policy-s5.yml"


def _workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_s5_pins_current_stable_matrix_and_real_obsidian() -> None:
    raw = _workflow()
    assert "32e827692f1a552cd581de9da45cecd0711573d3" in raw
    assert "LIVESYNC_VERSION: 1.0.18" in raw
    assert "OBSIDIAN_VERSION: 1.13.7" in raw
    assert "vrtmrz/obsidian-livesync" in raw
    assert "obsidianmd/obsidian-releases" in raw
    assert "npm run build" in raw
    assert "test -x squashfs-root/obsidian" in raw
    assert "test -x squashfs-root/obsidian-cli" in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_s5_reuses_upstream_conflict_policy_scenario_directly() -> None:
    raw = _workflow()
    assert "xvfb-run -a npm run test:e2e:obsidian:conflict-dialog-policy" in raw
    assert "test:e2e:obsidian:focused -- conflict-dialog-policy" not in raw
    assert '"scenario": "conflict-dialog-policy"' in raw
    assert '"real_obsidian": true' in raw
    assert '"three_live_versions_reviewed_pairwise": true' in raw
    assert '"concat_resolution_verified": true' in raw
    assert '"postponed_conflict_persists_restart": true' in raw
    assert '"ordinary_repeat_prompt_suppressed": true' in raw
    assert '"explicit_conflict_command_reopens_dialog": true' in raw
    assert '"replicated_resolution_clears_dialog_state": true' in raw


def test_s5_does_not_overclaim_transport_nas_or_authority() -> None:
    raw = _workflow()
    assert '"transport_origin_conflict_tested": false' in raw
    assert '"two_vault_transport_conflict_tested": false' in raw
    assert '"nas_deployment_tested": false' in raw
    assert '"hindsight_ingestion_activated": false' in raw
    assert '"pantheon_state_mutated": false' in raw
    assert '"evidence_admitted": false' in raw
    assert "test:docker-couchdb:start" not in raw
    assert "hindsight-obsidian-sync" not in raw
