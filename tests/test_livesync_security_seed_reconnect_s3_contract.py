from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-security-seed-reconnect-s3.yml"


def _workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_s3_loads_reviewed_stable_matrix() -> None:
    raw = _workflow()
    assert "export_external_qualification_pins.py" in raw
    assert "self-hosted-livesync obsidian-desktop" in raw
    assert "${{ env.LIVESYNC_REPOSITORY }}" in raw
    assert "${{ env.LIVESYNC_REF }}" in raw
    assert "Obsidian-${OBSIDIAN_VERSION}.AppImage" in raw
    assert "test -x squashfs-root/obsidian" in raw
    assert "test -x squashfs-root/obsidian-cli" in raw
    assert "OBSIDIAN_BINARY=" in raw
    assert "OBSIDIAN_CLI=" in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_s3_reuses_upstream_real_restart_reconnect_scenario() -> None:
    raw = _workflow()
    assert "test:docker-couchdb:start" in raw
    assert "xvfb-run -a npm run test:e2e:obsidian:focused -- security-seed-reconnect" in raw
    assert '"scenario": "security-seed-reconnect"' in raw
    assert '"real_obsidian": true' in raw
    assert '"same_vault_profile_restart": true' in raw
    assert '"fresh_second_device": true' in raw
    assert '"encrypted_round_trip": true' in raw
    assert '"security_seed_refresh_verified": true' in raw


def test_s3_does_not_overclaim_offline_conflict_nas_or_authority() -> None:
    raw = _workflow()
    assert '"generic_network_offline_tested": false' in raw
    assert '"two_vault_conflict_qualification": false' in raw
    assert '"nas_deployment_tested": false' in raw
    assert '"hindsight_ingestion_activated": false' in raw
    assert '"pantheon_state_mutated": false' in raw
    assert '"evidence_admitted": false' in raw
    assert "hindsight-obsidian-sync" not in raw
    assert "portainer" not in raw.lower()
