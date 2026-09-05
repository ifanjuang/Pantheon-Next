from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "pair_unsloth_runtime_q1.json"
PINS = ROOT / "implementation" / "qualification" / "external-pins.json"


def _fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def _pins() -> dict:
    return json.loads(PINS.read_text(encoding="utf-8"))["pins"]


def test_q1_targets_existing_external_pin_authority() -> None:
    fixture = _fixture()
    pins = _pins()

    assert fixture["schema_id"] == "pantheon.pair_unsloth_runtime_qualification_q1"
    assert fixture["revision"] == 1
    assert fixture["status"] == "candidate"
    assert fixture["live_executed"] is False

    assert fixture["target_pins"] == {
        "pair": "personal-ai-router",
        "unsloth": "unsloth",
        "hermes": "hermes-agent",
    }
    for pin_id in fixture["target_pins"].values():
        assert pin_id in pins


def test_q1_is_a_staged_lab_not_a_runtime_claim() -> None:
    fixture = _fixture()
    stages = fixture["stages"]

    assert [stage["stage_id"] for stage in stages] == [
        "q1a_pair_linux_isolated",
        "q1b_pair_linux_windows_cluster",
        "q1c_hermes_container_to_pair",
        "q1d_unsloth_as_existing_hermes_custom_provider",
        "q1e_classification",
    ]
    assert all(stage["result"] == "not_run" for stage in stages)

    authority = fixture["authority"]
    assert authority == {
        "deployment_selected": False,
        "installed": False,
        "runtime_qualified": False,
        "runtime_activated": False,
        "task_authorized": False,
        "evidence_admitted": False,
        "new_scheduler_authority": False,
        "new_router_authority": False,
        "new_runtime_owner": False,
    }


def test_pair_lab_preserves_physical_routing_ceiling() -> None:
    fixture = _fixture()
    by_id = {stage["stage_id"]: stage for stage in fixture["stages"]}

    cluster_checks = set(by_id["q1b_pair_linux_windows_cluster"]["required_checks"])
    assert "no_cross_machine_vram_pooling_claim" in cluster_checks
    assert "served_node_is_observable" in cluster_checks

    classification_checks = set(by_id["q1e_classification"]["required_checks"])
    assert "no_runtime_activation" in classification_checks
    assert "no_task_authorization" in classification_checks
    assert "no_evidence_admission" in classification_checks


def test_container_loopback_question_must_be_observed_not_assumed() -> None:
    fixture = _fixture()
    stage = next(
        item for item in fixture["stages"] if item["stage_id"] == "q1c_hermes_container_to_pair"
    )
    checks = set(stage["required_checks"])

    assert "current_compose_path_used_without_network_workaround" in checks
    assert "http_status_and_pair_error_recorded" in checks
    assert "no_403_assumed_before_execution" in checks
    assert "no_relay_or_host_network_change_in_q1" in checks


def test_unsloth_uses_existing_hermes_provider_seam_without_second_hermes() -> None:
    fixture = _fixture()
    stage = next(
        item
        for item in fixture["stages"]
        if item["stage_id"] == "q1d_unsloth_as_existing_hermes_custom_provider"
    )
    checks = set(stage["required_checks"])

    assert "existing_hermes_custom_provider_configuration" in checks
    assert "no_unsloth_start_hermes_path" in checks
    assert "pantheon_governed_profile_not_mutated" in checks


def test_q1_keeps_governance_non_equivalences_explicit() -> None:
    fixture = _fixture()
    rules = set(fixture["non_equivalences"])

    assert "runtime_success != task_authorization" in rules
    assert "runtime_success != Evidence" in rules
    assert "PAIR routing != Pantheon authorization" in rules
    assert "PAIR model availability != model approval" in rules
    assert "Unsloth provider configured != provider authorized" in rules
    assert "container connectivity != runtime qualification" in rules
