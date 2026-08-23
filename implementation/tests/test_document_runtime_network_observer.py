from __future__ import annotations

import json

from fastapi.testclient import TestClient

from mvp_vertical.document_runtime_network_observer import (
    collect_network_document_runtime_observations,
    create_app,
    observe_document_source_binding,
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
        observed.append((request.full_url, request.get_header("Authorization"), request.get_header("X-api-key"), timeout))
        return routes[request.full_url]
    return open_


def test_network_collector_observes_selected_paperless_and_hermes_skills_api():
    observed = []
    routes = {
        "http://paperless-gateway:8082/health": _Response({"status": "ok", "paperless_reachable": True, "intake_surface": "governed_only", "write_surface": "governed_only"}),
        "http://pantheon-policy-api:8000/readyz": _Response({"status": "ready"}),
        "http://pantheon-policy-api:8000/v1/meta": _Response({"contract": "pantheon.policy.v1", "source_mode": "repository", "repository": {"version": "0.8.0", "commit": "abc123"}, "secret": "must-not-leak"}),
        "http://docling:5001/health": _Response({"status": "ok"}),
        "http://hermes:8642/v1/skills": _Response([
            {"name": "pantheon-document-intake", "description": "bounded document intake", "private_runtime_detail": "must-not-project"},
            {"name": "other-skill", "description": "other"},
        ]),
    }
    result = collect_network_document_runtime_observations(
        document_source_binding="paperless_ngx", paperless_gateway_url="http://paperless-gateway:8082",
        cockpit_read_key="read-key", policy_url="http://pantheon-policy-api:8000", policy_api_key="policy-key",
        docling_url="http://docling:5001", docling_api_key="docling-key",
        hermes_api_url="http://hermes:8642", hermes_api_key="hermes-api-key",
        opener=_opener(routes, observed),
    )
    by_source = {item["source"]: item for item in result["observations"]}
    assert result["document_source_binding"] == "paperless_ngx"
    assert result["synthetic_global_health"] == "not_computed"
    assert result["authority_effect"] == "none"
    assert result["write_effect"] is False
    assert result["activation_changed"] is False
    paperless = by_source["paperless_gateway"]
    assert paperless["selection_status"] == "selected"
    assert paperless["binding"] == "paperless_ngx"
    assert paperless["paperless_reachability_status"] == "reachable"
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


def test_governed_local_source_makes_paperless_not_applicable_and_does_not_probe_it():
    observed = []
    routes = {
        "http://pantheon-policy-api:8000/readyz": _Response({"status": "ready"}),
        "http://pantheon-policy-api:8000/v1/meta": _Response({"contract": "pantheon.policy.v1", "repository": {"version": "0.8.0"}}),
        "http://docling:5001/health": _Response({"status": "ok"}),
        "http://hermes:8642/v1/skills": _Response([]),
    }
    result = collect_network_document_runtime_observations(
        document_source_binding="governed_local_source", paperless_gateway_url="", cockpit_read_key="read-key",
        policy_url="http://pantheon-policy-api:8000", policy_api_key="policy-key",
        docling_url="http://docling:5001", docling_api_key=None,
        hermes_api_url="http://hermes:8642", hermes_api_key="hermes-api-key",
        opener=_opener(routes, observed),
    )
    by_source = {item["source"]: item for item in result["observations"]}
    source = by_source["document_source_management"]
    assert result["document_source_binding"] == "governed_local_source"
    assert source["selected_binding"] == "governed_local_source"
    assert source["selection_status"] == "not_selected"
    assert source["installation_status"] == "not_applicable"
    assert source["reachability_status"] == "not_applicable"
    assert source["health_status"] == "not_applicable"
    assert not any("paperless-gateway" in row[0] for row in observed)
    assert "Paperless absent != Pantheon degraded" in result["non_equivalences"]
    assert "Paperless absent != document ingestion unavailable" in result["non_equivalences"]


def test_binding_helper_does_not_call_network_for_governed_local_source():
    called = False
    def opener(_request, timeout):
        nonlocal called
        called = True
        raise AssertionError("must not probe optional unselected Paperless binding")
    result = observe_document_source_binding("governed_local_source", paperless_gateway_url="", cockpit_read_key="read-key", opener=opener)
    assert called is False
    assert result["selection_status"] == "not_selected"
    assert result["reachability_status"] == "not_applicable"


def test_unknown_document_source_binding_is_not_guessed():
    result = observe_document_source_binding("unknown_dms", paperless_gateway_url="", cockpit_read_key="read-key")
    assert result["selection_status"] == "unsupported_binding"
    assert result["installation_status"] == "not_observed"
    assert result["reachability_status"] == "not_observed"


def test_hermes_http_inventory_is_not_guessed_without_api_key():
    result = observe_hermes_skills_api("http://hermes:8642", "")
    assert result["reachability_status"] == "not_configured"
    assert result["runtime_api_status"] == "not_observed"
    assert result["installation_status"] == "not_observed"
    assert result["activation_status"] == "not_inferred"


def test_hermes_http_inventory_refuses_to_infer_absence_from_invalid_payload():
    result = observe_hermes_skills_api("http://hermes:8642", "api-key", opener=lambda _request, timeout: _Response({"unexpected": "shape"}))
    assert result["reachability_status"] == "reachable"
    assert result["runtime_api_status"] == "invalid_payload"
    assert result["installation_status"] == "not_observed"


def test_network_observer_api_requires_cockpit_read_key(monkeypatch):
    expected = {"object_type": "document_runtime_observation_set", "observations": [], "synthetic_global_health": "not_computed", "authority_effect": "none", "write_effect": False, "activation_changed": False}
    def collector(**kwargs):
        assert kwargs["cockpit_read_key"] == "read-key"
        assert kwargs["document_source_binding"] == "governed_local_source"
        return expected
    monkeypatch.delenv("MVP_DOCUMENT_SOURCE_BINDING", raising=False)
    client = TestClient(create_app(read_api_key="read-key", collector=collector))
    assert client.get("/health").json()["meaning"] == "observer_process_liveness_only"
    assert client.get("/documents/observations").status_code == 401
    response = client.get("/documents/observations", headers={"Authorization": "Bearer read-key"})
    assert response.status_code == 200
    assert response.json() == expected
    assert client.get("/v1/document-runtime/observations", headers={"Authorization": "Bearer read-key"}).status_code == 404
