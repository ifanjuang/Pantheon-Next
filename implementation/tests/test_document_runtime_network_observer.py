from __future__ import annotations

import json

from fastapi.testclient import TestClient

from mvp_vertical.document_runtime_network_observer import (
    collect_network_document_runtime_observations,
    create_app,
    observe_hermes_skills_api,
)


class _Response:
    def __init__(self, payload, status=200):
        self.payload = payload
        self.status = status

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def getcode(self):
        return self.status

    def read(self, _limit=-1):
        return json.dumps(self.payload).encode("utf-8")


def _opener(routes, observed):
    def open_(request, timeout):
        observed.append(
            (
                request.full_url,
                request.get_header("Authorization"),
                request.get_header("X-api-key"),
                timeout,
            )
        )
        return routes[request.full_url]

    return open_


def test_network_collector_observes_hermes_skills_api_without_cli_colocation():
    observed = []
    routes = {
        "http://paperless-gateway:8082/health": _Response(
            {
                "status": "ok",
                "paperless_reachable": True,
                "intake_surface": "governed_only",
                "write_surface": "governed_only",
            }
        ),
        "http://pantheon-policy-api:8000/readyz": _Response({"status": "ready"}),
        "http://pantheon-policy-api:8000/v1/meta": _Response(
            {
                "contract": "pantheon.policy.v1",
                "source_mode": "repository",
                "repository": {"version": "0.8.0", "commit": "abc123"},
                "secret": "must-not-leak",
            }
        ),
        "http://docling:5001/health": _Response({"status": "ok"}),
        "http://hermes:8642/v1/skills": _Response(
            [
                {
                    "name": "pantheon-document-intake",
                    "description": "bounded document intake",
                    "private_runtime_detail": "must-not-project",
                },
                {"name": "other-skill", "description": "other"},
            ]
        ),
    }

    result = collect_network_document_runtime_observations(
        paperless_gateway_url="http://paperless-gateway:8082",
        cockpit_read_key="read-key",
        policy_url="http://pantheon-policy-api:8000",
        policy_api_key="policy-key",
        docling_url="http://docling:5001",
        docling_api_key="docling-key",
        hermes_api_url="http://hermes:8642",
        hermes_api_key="hermes-api-key",
        opener=_opener(routes, observed),
    )

    by_source = {item["source"]: item for item in result["observations"]}
    assert result["synthetic_global_health"] == "not_computed"
    assert result["authority_effect"] == "none"
    assert result["write_effect"] is False
    assert result["activation_changed"] is False

    hermes = by_source["hermes_native_inventory"]
    assert hermes["observation_source"] == "hermes_api_v1_skills"
    assert hermes["reachability_status"] == "reachable"
    assert hermes["runtime_api_status"] == "observed"
    assert hermes["installation_status"] == "installed_observed"
    assert hermes["observed_skill_count"] == 2
    assert "private_runtime_detail" not in hermes
    assert hermes["approval_status"] == "not_inferred"

    assert [row[0] for row in observed] == [
        "http://paperless-gateway:8082/health",
        "http://pantheon-policy-api:8000/readyz",
        "http://pantheon-policy-api:8000/v1/meta",
        "http://docling:5001/health",
        "http://hermes:8642/v1/skills",
    ]
    assert observed[0][1] == "Bearer read-key"
    assert observed[1][1] == "Bearer policy-key"
    assert observed[2][1] == "Bearer policy-key"
    assert observed[3][2] == "docling-key"
    assert observed[4][1] == "Bearer hermes-api-key"


def test_hermes_http_inventory_is_not_guessed_without_api_key():
    result = observe_hermes_skills_api("http://hermes:8642", "")
    assert result["reachability_status"] == "not_configured"
    assert result["runtime_api_status"] == "not_observed"
    assert result["installation_status"] == "not_observed"
    assert result["activation_status"] == "not_inferred"


def test_hermes_http_inventory_refuses_to_infer_absence_from_invalid_payload():
    result = observe_hermes_skills_api(
        "http://hermes:8642",
        "api-key",
        opener=lambda _request, timeout: _Response({"unexpected": "shape"}),
    )
    assert result["reachability_status"] == "reachable"
    assert result["runtime_api_status"] == "invalid_payload"
    assert result["installation_status"] == "not_observed"


def test_network_observer_api_requires_cockpit_read_key():
    expected = {
        "object_type": "document_runtime_observation_set",
        "observations": [],
        "synthetic_global_health": "not_computed",
        "authority_effect": "none",
        "write_effect": False,
        "activation_changed": False,
    }

    def collector(**kwargs):
        assert kwargs["cockpit_read_key"] == "read-key"
        return expected

    client = TestClient(create_app(read_api_key="read-key", collector=collector))
    assert client.get("/health").json()["meaning"] == "observer_process_liveness_only"
    assert client.get("/v1/document-runtime/observations").status_code == 401
    response = client.get(
        "/v1/document-runtime/observations",
        headers={"Authorization": "Bearer read-key"},
    )
    assert response.status_code == 200
    assert response.json() == expected
