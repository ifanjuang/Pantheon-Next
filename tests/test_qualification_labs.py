"""Seventeen labs run somebody else's project. This holds what that costs.

Two separate things are held here. The arbitration — which labs deserve to block
merges — is a human decision, and these tests only keep the backlog countable and
non-growing. The drift detection is mechanical, and it is checked in both
directions: a lab that has stopped matching the registry must be caught, and a
lab that matches must not be reported.
"""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


LABS = load_module("check_qualification_labs", ".github/scripts/check_qualification_labs.py")
REGISTRY = json.loads((ROOT / ".github" / "qualification-labs.json").read_text(encoding="utf-8"))
PINS = json.loads(
    (ROOT / "implementation" / "qualification" / "external-pins.json").read_text(encoding="utf-8")
)
DISCOVERED = LABS.discover(ROOT / ".github" / "workflows")


def test_the_registry_and_the_workflows_agree_today() -> None:
    errors, rows = LABS.verify(DISCOVERED, REGISTRY, PINS)
    assert errors == [], "\n".join(errors)
    assert len(rows) == len(DISCOVERED)


def test_discovery_finds_labs_by_what_they_run_not_by_their_name() -> None:
    """A lab renamed or moved must still be discovered."""
    assert len(DISCOVERED) >= 15
    for lab in DISCOVERED.values():
        assert lab["external"] or lab["resolves_from_registry"]
    ordinary = {"governance-ci.yml", "implementation-ci.yml", "catalog-ci.yml"}
    assert not (ordinary & set(DISCOVERED)), (
        "a workflow that runs no external project was classified as a lab"
    )


def test_a_new_lab_cannot_appear_without_an_entry() -> None:
    errors, _ = LABS.verify(
        {**DISCOVERED, "new-lab.yml": {
            "workflow": "new-lab.yml", "name": "New", "blocking": True,
            "resolves_from_registry": True, "external": [], "literal_targets": {},
        }},
        REGISTRY,
        PINS,
    )
    assert any("has no entry here" in error for error in errors)


def test_an_entry_for_a_lab_that_no_longer_exists_fails() -> None:
    trimmed = {k: v for k, v in DISCOVERED.items() if k != "implementation-livesync-headless-mirror-s1.yml"}
    errors, _ = LABS.verify(trimmed, REGISTRY, PINS)
    assert any("no longer a qualification lab" in error for error in errors)


def test_a_hardcoded_target_must_be_declared() -> None:
    """A new frozen target may not appear unnoticed."""
    labs = copy.deepcopy(DISCOVERED)
    labs["implementation-livesync-headless-mirror-s1.yml"]["literal_targets"] = {
        "SOMETHING_COMMIT": "0123456789abcdef"
    }
    errors, _ = LABS.verify(labs, REGISTRY, PINS)
    assert any("is not declared" in error for error in errors)


def test_a_declared_target_that_the_workflow_dropped_fails() -> None:
    labs = copy.deepcopy(DISCOVERED)
    labs["hermes-langfuse-q1.yml"]["literal_targets"] = {}
    errors, _ = LABS.verify(labs, REGISTRY, PINS)
    assert any("no longer pins" in error for error in errors)


def test_a_target_naming_a_pin_the_registry_does_not_define_fails() -> None:
    registry = copy.deepcopy(REGISTRY)
    for entry in registry["labs"]:
        if entry["workflow"] == "hermes-langfuse-q1.yml":
            entry["targets"]["HERMES_COMMIT"] = "no-such-pin"
    errors, _ = LABS.verify(DISCOVERED, registry, PINS)
    assert any("registry does not define" in error for error in errors)


def test_drift_is_detected_and_absence_of_drift_is_not_invented() -> None:
    """Both directions, so the detector cannot pass by never firing."""
    _, rows = LABS.verify(DISCOVERED, REGISTRY, PINS)
    drifting = {row["workflow"] for row in rows if row["drift"]}
    assert drifting, "no drift detected at all; the comparison has stopped working"

    aligned = copy.deepcopy(PINS)
    aligned["pins"]["hermes-agent"]["ref"] = "4c1f53be10d0fce1d25aee1975e5149b6c54f25a"
    _, rows = LABS.verify(DISCOVERED, REGISTRY, aligned)
    q1 = next(row for row in rows if row["workflow"] == "hermes-langfuse-q1.yml")
    assert not q1["drift"], "a lab matching the registry was still reported as drifted"


def test_the_ceilings_match_the_debt_that_exists() -> None:
    """A ceiling above the real count is headroom nobody decided to grant."""
    _, rows = LABS.verify(DISCOVERED, REGISTRY, PINS)
    undeclared = [row for row in rows if row["blocking"] and not row["guards"]]
    drifting = [row for row in rows if row["drift"]]
    assert REGISTRY["blocking_without_declared_decision_ceiling"] == len(undeclared)
    assert REGISTRY["frozen_target_drift_ceiling"] == len(drifting)


def test_the_report_does_not_present_the_arbitration_as_settled() -> None:
    _, rows = LABS.verify(DISCOVERED, REGISTRY, PINS)
    report = LABS.render(rows, REGISTRY)
    assert "arbitration, not an audit result" in report
    assert "not arbitrated" in report
