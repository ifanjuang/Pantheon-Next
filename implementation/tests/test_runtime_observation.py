from __future__ import annotations

from pathlib import Path

import pytest

from mvp_vertical import (
    document_runtime_network_observer,
    document_runtime_observer,
)
from mvp_vertical.runtime_observation import (
    RuntimeObservation,
    RuntimeObservationError,
    normalize_runtime_observation,
    normalize_runtime_observations,
)


def test_flat_observation_round_trip_preserves_adapter_owned_fields() -> None:
    original = {
        "source": " paperless_gateway ",
        "observation_source": " bounded_gateway_health ",
        "observed_at": "2026-08-04T00:00:00Z",
        "reachability_status": "reachable",
        "health_status": "not_established_by_reachability_probe",
        "metadata": {"service": "paperless"},
    }

    normalized = normalize_runtime_observation(original)

    assert normalized == {
        "source": "paperless_gateway",
        "observation_source": "bounded_gateway_health",
        "observed_at": "2026-08-04T00:00:00Z",
        "reachability_status": "reachable",
        "health_status": "not_established_by_reachability_probe",
        "metadata": {"service": "paperless"},
    }
    original["metadata"]["service"] = "mutated"
    assert normalized["metadata"]["service"] == "paperless"


def test_runtime_observation_is_internal_envelope_not_status_ontology() -> None:
    observation = RuntimeObservation.from_flat_mapping(
        {
            "source": "hermes_native_inventory",
            "observation_source": "hermes_api_v1_skills",
            "observed_at": "2026-08-04T00:00:00+00:00",
            "runtime_api_status": "observed",
            "installation_status": "installed_observed",
            "activation_status": "not_inferred",
            "approval_status": "not_inferred",
        }
    )

    flat = observation.as_flat_dict()
    assert flat["runtime_api_status"] == "observed"
    assert flat["installation_status"] == "installed_observed"
    assert flat["activation_status"] == "not_inferred"
    assert flat["approval_status"] == "not_inferred"
    assert "evidence_status" not in flat
    assert "task_authorized" not in flat


def test_observation_requires_explicit_timezone() -> None:
    with pytest.raises(RuntimeObservationError, match="explicit UTC offset"):
        normalize_runtime_observation(
            {
                "source": "docling_serve",
                "observation_source": "docling_health_endpoint",
                "observed_at": "2026-08-04T00:00:00",
            }
        )


def test_observation_list_preserves_order_and_rejects_non_array() -> None:
    normalized = normalize_runtime_observations(
        [
            {
                "source": "first",
                "observation_source": "probe",
                "observed_at": "2026-08-04T00:00:00Z",
                "local_status": "one",
            },
            {
                "source": "second",
                "observation_source": "inventory",
                "observed_at": "2026-08-04T00:00:01Z",
                "local_status": "two",
            },
        ]
    )
    assert [item["source"] for item in normalized] == ["first", "second"]

    with pytest.raises(RuntimeObservationError, match="must be an array"):
        normalize_runtime_observations("not-an-array")


def test_local_and_network_collectors_share_only_the_common_envelope() -> None:
    local_source = Path(document_runtime_observer.__file__).read_text(encoding="utf-8")
    network_source = Path(document_runtime_network_observer.__file__).read_text(encoding="utf-8")

    assert "normalize_runtime_observations" in local_source
    assert "normalize_runtime_observations" in network_source
    assert '"synthetic_global_health": "not_computed"' in local_source
    assert '"synthetic_global_health": "not_computed"' in network_source
    assert '"authority_effect": "none"' in local_source
    assert '"authority_effect": "none"' in network_source
    assert '"runtime success != Evidence"' in local_source
    assert '"runtime success != Evidence"' in network_source
