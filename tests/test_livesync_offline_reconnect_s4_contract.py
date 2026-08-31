from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "implementation-livesync-offline-reconnect-s4.yml"
SCENARIO = ROOT / "implementation" / "labs" / "livesync" / "pantheon-offline-reconnect-s4.ts"


def _workflow() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def _scenario() -> str:
    return SCENARIO.read_text(encoding="utf-8")


def test_s4_loads_reviewed_stable_matrix_and_real_clients() -> None:
    raw = _workflow()
    assert "export_external_qualification_pins.py" in raw
    assert "self-hosted-livesync obsidian-desktop" in raw
    assert "${{ env.LIVESYNC_REPOSITORY }}" in raw
    assert "${{ env.LIVESYNC_REF }}" in raw
    assert "npm run build -w self-hosted-livesync-cli" in raw
    assert "test -x squashfs-root/obsidian" in raw
    assert "test -x squashfs-root/obsidian-cli" in raw
    assert "latest" not in raw.lower()
    assert "edge" not in raw.lower()


def test_s4_physically_stops_couchdb_and_commits_edit_locally_before_restart() -> None:
    raw = _scenario()
    assert 'const couchDbContainer = "couchdb-test"' in raw
    assert 'execFileSync("docker", ["stop", couchDbContainer]' in raw
    assert "await assertCouchDbDown(couchDb)" in raw
    assert "await createNoteInsideRealObsidian" in raw
    assert "await waitForLocalDatabaseEntry" in raw
    assert 'execFileSync("docker", ["start", couchDbContainer]' in raw
    assert "await waitForCouchDbUp(couchDb)" in raw
    assert "await pushLocalChanges" in raw
    assert "waitForCouchDbDocs" in raw


def test_s4_uses_fresh_cli_consumer_for_byte_exact_remote_readback() -> None:
    raw = _scenario()
    assert '"sync"]' in raw
    assert '"pull",' in raw
    assert "Fresh LiveSync CLI consumer did not retrieve the offline-created note byte-for-byte" in raw
    assert "PANTHEON_LIVESYNC_OFFLINE_RECONNECT_S4" in raw


def test_s4_does_not_overclaim_automatic_reconnect_conflict_nas_or_authority() -> None:
    raw = _workflow()
    assert '"automatic_reconnect_tested": false' in raw
    assert '"two_vault_conflict_qualification": false' in raw
    assert '"nas_deployment_tested": false' in raw
    assert '"hindsight_ingestion_activated": false' in raw
    assert '"pantheon_state_mutated": false' in raw
    assert '"evidence_admitted": false' in raw
    assert "hindsight-obsidian-sync" not in raw
    assert "portainer" not in raw.lower()


def test_the_shared_retry_wrapper_is_a_trigger_for_this_lab() -> None:
    """A change to the shared wrapper must run the labs that execute it.

    All four Obsidian labs go through one script. Referencing it in `run:` is
    not enough: if it is absent from the path filters, a pull request that
    breaks only the wrapper runs none of its consumers and merges unexercised.
    """
    raw = _workflow()
    triggers, separator, _ = raw.partition("permissions:")
    assert separator, "workflow shape changed; the trigger section is no longer delimited"
    assert "implementation/tools/obsidian_e2e_with_flake_report.sh" in raw, "this lab no longer executes the shared wrapper"
    assert "implementation/tools/obsidian_e2e_with_flake_report.sh" in triggers, (
        "the wrapper is executed but is not a declared trigger path"
    )
