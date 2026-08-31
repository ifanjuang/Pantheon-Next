"""Keep the pin-freshness observation honest and keep it wired to the registry.

`external-pins.json` records which external artifact each qualification targets,
and until now nothing compared it to upstream. Dependabot cannot: it watches
`pip` and `github-actions`, while the pins are git refs, container images and
releases in a repository-specific registry. Three of ten pins had drifted
unnoticed when this check was written.

These tests exercise the comparison only. They never reach the network: upstream
heads are injected, so the suite stays deterministic and offline. Fetching lives
behind `observe_all` and is exercised by the scheduled workflow, not here.

```text
observation refreshed != pin moved
update_available != update_authorized
```
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

IMPLEMENTATION = Path(__file__).resolve().parents[1]
if str(IMPLEMENTATION) not in sys.path:
    sys.path.insert(0, str(IMPLEMENTATION))

from tools.check_external_pin_freshness import (  # noqa: E402
    DECLARED_SOURCES,
    FETCHABLE_SOURCES,
    OBSERVATIONS,
    OBSERVATIONS_SCHEMA,
    REGISTRY,
    REGISTRY_SCHEMA,
    FreshnessError,
    compare,
    load_json,
)


@pytest.fixture()
def registry() -> dict:
    return load_json(REGISTRY, REGISTRY_SCHEMA)


@pytest.fixture()
def observations() -> dict:
    return load_json(OBSERVATIONS, OBSERVATIONS_SCHEMA)


# --------------------------------------------------------------------------
# The observation record must stay wired to the registry it describes.
# --------------------------------------------------------------------------


def test_every_pin_has_an_upstream_observation_record(registry, observations) -> None:
    missing = sorted(set(registry["pins"]) - set(observations["observations"]))
    assert not missing, (
        "a pin with no observation record has an unanswerable freshness question; "
        f"add one to external-upstream-observations.json: {missing}"
    )


def test_no_observation_describes_a_pin_that_was_removed(registry, observations) -> None:
    orphaned = sorted(set(observations["observations"]) - set(registry["pins"]))
    assert not orphaned, f"observation records outlived their pins: {orphaned}"


def test_observation_records_are_structurally_complete(observations) -> None:
    for pin_id, record in observations["observations"].items():
        assert record["source"] in DECLARED_SOURCES, (pin_id, record["source"])
        assert record["locator"], pin_id
        assert record["latest_seen"], pin_id
        assert record["observed_on"], pin_id

        delta = record["delta"]
        if delta == "none":
            continue
        assert isinstance(delta, dict), pin_id
        assert delta["state"] in {"open", "acknowledged"}, (pin_id, delta["state"])
        assert delta["reason"].strip(), (
            f"{pin_id}: a recorded lag must say why it exists; an unexplained lag "
            "is the state this file was created to remove"
        )
        if delta["state"] == "acknowledged":
            assert delta["decided_on"], (
                f"{pin_id}: an acknowledged lag is a dated human decision, not a "
                "standing exemption"
            )


def test_the_observation_record_claims_no_authority(observations) -> None:
    assert observations["authority"] == {
        "deployment_truth": False,
        "installation_state": False,
        "runtime_activation": False,
        "update_authorization": False,
        "task_authorization": False,
        "evidence_admission": False,
    }


# --------------------------------------------------------------------------
# Comparison behaviour, on injected upstream heads.
# --------------------------------------------------------------------------


def _minimal() -> tuple[dict, dict]:
    registry = {
        "schema_id": REGISTRY_SCHEMA,
        "pins": {"thing": {"kind": "git", "version": "1.0.0"}},
    }
    observations = {
        "schema_id": OBSERVATIONS_SCHEMA,
        "observations": {
            "thing": {
                "source": "github_releases_latest",
                "locator": "org/thing",
                "latest_seen": "v1.0.0",
                "observed_on": "2026-08-31",
                "delta": "none",
            }
        },
    }
    return registry, observations


def test_an_aligned_pin_is_not_actionable() -> None:
    registry, observations = _minimal()
    report = compare(registry, observations, {"thing": "v1.0.0"})
    assert report["rows"][0]["signal"] == "aligned"
    assert report["actionable"] == []


def test_a_new_upstream_release_makes_the_observation_stale() -> None:
    registry, observations = _minimal()
    report = compare(registry, observations, {"thing": "v1.1.0"})
    assert report["rows"][0]["signal"] == "observation_stale"
    assert report["actionable"] == ["thing"]


def test_an_undecided_recorded_lag_is_actionable() -> None:
    registry, observations = _minimal()
    observations["observations"]["thing"]["delta"] = {"state": "open", "reason": "not reviewed"}
    report = compare(registry, observations, {"thing": "v1.0.0"})
    assert report["rows"][0]["signal"] == "unacknowledged_lag"
    assert report["actionable"] == ["thing"]


def test_a_dated_decision_closes_the_signal_without_moving_the_pin() -> None:
    registry, observations = _minimal()
    observations["observations"]["thing"]["delta"] = {
        "state": "acknowledged",
        "reason": "staying deliberately",
        "decided_on": "2026-08-31",
    }
    report = compare(registry, observations, {"thing": "v1.0.0"})
    assert report["rows"][0]["signal"] == "acknowledged_lag"
    assert report["actionable"] == []
    assert registry["pins"]["thing"]["version"] == "1.0.0"


def test_an_unreachable_host_does_not_silently_read_as_aligned() -> None:
    registry, observations = _minimal()
    report = compare(registry, observations, {"thing": "__unreachable__:URLError"})
    # Not actionable — a network failure is not a drift claim — but the row
    # carries the failure so a run of all-unreachable pins cannot look green.
    assert report["rows"][0]["upstream_head_now"].startswith("__unreachable__")
    assert report["rows"][0]["signal"] == "aligned"


def test_a_pin_without_an_observation_record_fails_closed() -> None:
    registry, observations = _minimal()
    registry["pins"]["other"] = {"kind": "git", "version": "2.0.0"}
    with pytest.raises(FreshnessError, match="missing"):
        compare(registry, observations, {})


def test_a_derived_pin_does_not_double_count_its_source_signal() -> None:
    registry, observations = _minimal()
    observations["observations"]["thing"]["source"] = "derived_from_source_pin"
    observations["observations"]["thing"]["delta"] = {"state": "open", "reason": "follows source"}
    report = compare(registry, observations, {})
    assert report["rows"][0]["signal"] == "derived"
    assert report["actionable"] == []


def test_the_report_claims_no_update_authority() -> None:
    registry, observations = _minimal()
    report = compare(registry, observations, {"thing": "v1.0.0"})
    assert report["authority"]["update_authorization"] is False
    assert report["authority"]["task_authorization"] is False


def test_fetchable_sources_are_a_subset_of_declared_sources() -> None:
    assert FETCHABLE_SOURCES <= DECLARED_SOURCES


def test_the_committed_records_parse_and_compare(registry, observations) -> None:
    """The real files must survive the comparison the workflow will run."""
    report = compare(registry, observations, {})
    assert len(report["rows"]) == len(registry["pins"])
    assert json.dumps(report)  # serialisable for the workflow artifact
