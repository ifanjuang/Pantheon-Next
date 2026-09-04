from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/obsidian-headless-sync-q2a.yml"
RUNNER = ROOT / "implementation/tools/run_obsidian_headless_sync_q2a.sh"
Q1_FIXTURE = ROOT / "tests/fixtures/obsidian_headless_sync_topology_q1.json"


def test_q2a_files_exist_and_stack_on_q1_contract():
    assert WORKFLOW.exists()
    assert RUNNER.exists()
    assert Q1_FIXTURE.exists()


def test_runtime_is_manual_and_fail_closed_on_synthetic_inputs():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "workflow_dispatch:" in text
    assert "if: github.event_name == 'workflow_dispatch'" in text
    assert "environment: obsidian-sync-qualification" in text
    for name in (
        "OBSIDIAN_SYNC_EMAIL",
        "OBSIDIAN_SYNC_PASSWORD",
        "OBSIDIAN_SYNC_VAULT",
    ):
        assert f"secrets.{name}" in text
        assert f'test -n "${name}"' in text
    assert "obsidian-headless@0.0.14" in text


def test_q2a_uses_two_isolated_local_views_and_run_scoped_material():
    text = RUNNER.read_text(encoding="utf-8")
    assert 'A="$ROOT/device-a"' in text
    assert 'B="$ROOT/device-b"' in text
    assert 'PREFIX="pantheon-q2a-${PANTHEON_Q2A_RUN_ID}"' in text
    assert 'setup_vault "$A"' in text
    assert 'setup_vault "$B"' in text
    assert "--mode bidirectional" in text
    assert "--conflict-strategy conflict" in text


def test_q2a_observes_crud_conflict_continuous_and_restart_without_overclaiming():
    text = RUNNER.read_text(encoding="utf-8")
    for needle in (
        "create_edit_rename_delete",
        "concurrent_conflict_preserves_both_markers",
        "continuous_materialization",
        "daemon_restart",
        "one_long_running_materializer_in_harness",
    ):
        assert needle in text
    for needle in (
        '"native_desktop_offline_reconnect": "requires Q2b/native client"',
        '"ubuntu_host_reboot_redeploy": "requires Q2b/#864 node"',
        '"network_interruption_recovery": "requires Q2b/#864 node"',
        '"backup_rollback": "requires Q2b/#864 node"',
    ):
        assert needle in text


def test_q2a_does_not_activate_parallel_pantheon_subsystems():
    text = (WORKFLOW.read_text(encoding="utf-8") + "\n" + RUNNER.read_text(encoding="utf-8")).lower()
    forbidden = (
        "hindsight-obsidian-sync",
        "sync_retain",
        "notemesh",
        "couchdb",
        "self-hosted-livesync",
        "deployment #864 change",
    )
    for needle in forbidden:
        assert needle not in text


def test_q2a_cleans_only_its_run_scope_and_unlinks_credentials():
    text = RUNNER.read_text(encoding="utf-8")
    assert 'rm -rf "$A/$PREFIX"' in text
    assert 'test ! -e "$B/$PREFIX"' in text
    assert 'ob sync-unlink --path "$A"' in text
    assert 'ob sync-unlink --path "$B"' in text
    assert "ob logout" in text
    assert 'rm -rf "$A"' not in text
    assert 'rm -rf "$B"' not in text


def test_q2a_preserves_authority_distinctions_in_observation():
    text = RUNNER.read_text(encoding="utf-8")
    for needle in (
        '"production_switch": False',
        '"issue_660_changed": False',
        '"issue_659_changed": False',
        '"hindsight_activated": False',
        '"workspace_index_provider_selected": False',
    ):
        assert needle in text
