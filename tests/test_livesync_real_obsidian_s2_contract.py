from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-real-obsidian-s2.yml"


def _workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_s2_loads_reviewed_livesync_and_real_obsidian_pins() -> None:
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
    assert "test:docker-couchdb:start" in raw
    assert "test:e2e:obsidian:install-appimage" not in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_s2_reuses_upstream_cli_to_real_obsidian_compatibility_scenario() -> None:
    raw = _workflow()
    assert "xvfb-run -a npm run test:e2e:obsidian:focused -- cli-to-obsidian-sync" in raw
    assert '"scenario": "cli-to-obsidian-sync"' in raw
    assert '"real_obsidian": true' in raw
    assert '"real_livesync_cli": true' in raw
    assert '"couchdb_transport": true' in raw
    assert '"e2ee_round_trip": true' in raw
    assert '"path_obfuscation": true' in raw
    assert '"two_vault_conflict_qualification": false' in raw
    assert "two-vault-sync" not in raw
    assert "E2E_OBSIDIAN_INCLUDE_MARKDOWN_CONFLICT" not in raw
    assert "E2E_OBSIDIAN_INCLUDE_CONFLICT_OPERATIONS" not in raw


def test_s2_does_not_claim_nas_hindsight_or_pantheon_authority() -> None:
    raw = _workflow()
    assert '"nas_deployment_tested": false' in raw
    assert '"hindsight_ingestion_activated": false' in raw
    assert '"pantheon_state_mutated": false' in raw
    assert '"evidence_admitted": false' in raw
    assert "hindsight-obsidian-sync" not in raw
    assert "portainer" not in raw.lower()
