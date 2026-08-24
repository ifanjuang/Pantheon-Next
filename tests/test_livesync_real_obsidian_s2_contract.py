from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-real-obsidian-s2.yml"


def _workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_s2_pins_reviewed_livesync_and_uses_real_obsidian_upstream_scenario() -> None:
    raw = _workflow()
    assert "32e827692f1a552cd581de9da45cecd0711573d3" in raw
    assert "LIVESYNC_VERSION: 1.0.18" in raw
    assert "OBSIDIAN_VERSION: 1.13.7" in raw
    assert "vrtmrz/obsidian-livesync" in raw
    assert "obsidianmd/obsidian-releases" in raw
    assert "Obsidian-${OBSIDIAN_VERSION}.AppImage" in raw
    assert "test -x squashfs-root/obsidian" in raw
    assert "test -x squashfs-root/obsidian-cli" in raw
    assert "OBSIDIAN_BINARY=" in raw
    assert "OBSIDIAN_CLI=" in raw
    assert "xvfb-run -a npm run test:e2e:obsidian:focused -- two-vault-sync" in raw
    assert "test:docker-couchdb:start" in raw
    assert "test:e2e:obsidian:install-appimage" not in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_s2_exercises_upstream_conflict_extensions() -> None:
    raw = _workflow()
    assert 'E2E_OBSIDIAN_INCLUDE_MARKDOWN_CONFLICT: "true"' in raw
    assert 'E2E_OBSIDIAN_INCLUDE_CONFLICT_OPERATIONS: "true"' in raw


def test_s2_does_not_claim_nas_hindsight_or_pantheon_authority() -> None:
    raw = _workflow()
    assert '"nas_deployment_tested": false' in raw
    assert '"hindsight_ingestion_activated": false' in raw
    assert '"pantheon_state_mutated": false' in raw
    assert '"evidence_admitted": false' in raw
    assert "hindsight-obsidian-sync" not in raw
    assert "portainer" not in raw.lower()
