import json
from pathlib import Path


FIXTURE = Path(__file__).parent / "fixtures" / "obsidian_headless_sync_topology_q1.json"


def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def test_qualification_reuses_existing_owners_and_does_not_adopt_authority():
    data = load_fixture()
    qualification = data["qualification"]
    candidate = data["candidate"]
    downstream = data["downstream_contract"]

    assert qualification["issue"] == 958
    assert qualification["parent_owner_issue"] == 660
    assert qualification["derived_memory_owner_issue"] == 659
    assert qualification["classification"] == "qualification_only"
    assert qualification["decision"] == "open"
    assert candidate["authority_adopted"] is False
    assert downstream["workspace_index_provider_selected_by_this_qualification"] is False
    assert downstream["notemesh_selected_by_this_qualification"] is False


def test_candidate_identity_and_upstream_capability_snapshot_are_explicit():
    data = load_fixture()
    candidate = data["candidate"]

    assert candidate["package"] == "obsidian-headless"
    assert candidate["observed_version"] == "0.0.14"
    assert candidate["status"] == "open_beta"
    assert candidate["runtime"]["node_min"] == 22
    assert candidate["runtime"]["requires_active_obsidian_sync_subscription"] is True
    assert candidate["runtime"]["linux_supported"] is True
    assert candidate["upstream_capabilities"]["continuous_sync"] is True
    assert set(candidate["upstream_capabilities"]["modes"]) == {
        "bidirectional",
        "pull-only",
        "mirror-remote",
    }
    assert set(candidate["upstream_capabilities"]["conflict_strategies"]) == {
        "merge",
        "conflict",
    }


def test_candidate_topology_is_strictly_smaller_in_active_materialization_components():
    data = load_fixture()
    topologies = data["topologies"]
    current_components = set(topologies["A_selected_current"]["components"])
    candidate_components = set(topologies["B_candidate"]["components"])

    assert "couchdb_ubuntu" in current_components
    assert "single_livesync_cli_materializer" in current_components
    assert "couchdb_ubuntu" not in candidate_components
    assert "single_livesync_cli_materializer" not in candidate_components
    assert "ubuntu_local_vault_mirror" in current_components
    assert "ubuntu_local_vault_mirror" in candidate_components
    assert len(candidate_components) < len(current_components)


def test_acceptance_surface_covers_the_open_issue_660_operational_risks():
    data = load_fixture()
    surface = set(data["acceptance_surface"])

    required = {
        "create",
        "edit",
        "rename",
        "delete",
        "offline_reconnect",
        "concurrent_conflict",
        "continuous_materialization",
        "daemon_restart",
        "ubuntu_reboot_redeploy",
        "network_interruption_recovery",
        "credentials_secrets_posture",
        "backup_rollback",
        "exactly_one_active_filesystem_sync_producer",
        "no_hindsight_activation_or_writeback",
    }
    assert required <= surface


def test_replacement_gate_requires_real_simplification_not_technical_success_only():
    data = load_fixture()
    gate = data["decision_gate"]

    replace = set(gate["replace_A_with_B_if"])
    reject = set(gate["reject_B_if"])

    assert "all_required_capabilities_preserved" in replace
    assert "couchdb_removed_from_active_path" in replace
    assert "self_hosted_livesync_cli_removed_from_active_path" in replace
    assert "exactly_one_active_materializer" in replace
    assert "parallel_sync_or_materialization_daemon_required_to_compensate" in reject


def test_hindsight_contract_is_unchanged_by_materializer_selection():
    data = load_fixture()
    downstream = data["downstream_contract"]

    assert downstream["hindsight_input"] == "ubuntu_local_vault_mirror"
    assert downstream["hindsight_producer"] == "exactly_one_hindsight_obsidian_sync"
    assert downstream["hindsight_writeback_to_vault"] is False


def test_no_runtime_result_is_claimed_before_live_obsidian_sync_execution():
    data = load_fixture()
    observations = data["runtime_observations"]

    assert observations["live_obsidian_sync_executed"] is False
    for key, value in observations.items():
        if key == "live_obsidian_sync_executed":
            continue
        assert value == "not_run"


def test_governance_non_equivalences_are_retained():
    data = load_fixture()
    invariants = set(data["invariants"])

    assert "sync success != authorization" in invariants
    assert "filesystem mirror != governed identity" in invariants
    assert "workspace note != Evidence" in invariants
    assert "projection != persistence" in invariants
    assert "materializer selection != WorkspaceIndex provider selection" in invariants
    assert "materializer selection != Hindsight producer selection" in invariants
