from __future__ import annotations

import json
from types import SimpleNamespace

from fastapi.testclient import TestClient

from mvp_vertical.document_runtime_observer import (
    collect_document_runtime_observations,
    create_app,
    observe_hermes_skill_inventory,
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


def test_collector_keeps_independent_sources_and_never_computes_global_health():
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
        "http://docling-serve:5001/health": _Response({"status": "ok"}),
    }

    result = collect_document_runtime_observations(
        paperless_gateway_url="http://paperless-gateway:8082",
        cockpit_read_key="read-key",
        policy_url="http://pantheon-policy-api:8000",
        policy_api_key="policy-key",
        docling_url="http://docling-serve:5001",
        docling_api_key="docling-key",
        hermes_inventory_mode="local_cli",
        hermes_cli_path="/usr/local/bin/hermes",
        opener=_opener(routes, observed),
        runner=lambda *args, **kwargs: SimpleNamespace(
            returncode=0,
            stdout="Installed skills\n- pantheon-document-intake\n",
            stderr="",
        ),
        which=lambda _name: "/usr/local/bin/hermes",
    )

    by_source = {item["source"]: item for item in result["observations"]}
    assert result["synthetic_global_health"] == "not_computed"
    assert result["authority_effect"] == "none"
    assert result["write_effect"] is False
    assert result["activation_changed"] is False

    assert by_source["paperless_gateway"]["paperless_reachability_status"] == "reachable"
    assert by_source["paperless_gateway"]["health_status"] == "not_established_by_reachability_probe"
    assert by_source["pantheon_pdp"]["readiness_status"] == "ready_observed"
    assert by_source["pantheon_pdp"]["authorization_status"] == "not_inferred_from_readiness"
    assert by_source["pantheon_pdp"]["metadata"]["repository"]["commit"] == "abc123"
    assert "secret" not in by_source["pantheon_pdp"]["metadata"]
    assert by_source["docling_serve"]["reachability_status"] == "reachable"
    assert by_source["docling_serve"]["extraction_quality_status"] == "not_established_by_health_probe"
    assert by_source["hermes_native_inventory"]["installation_status"] == "installed_observed"
    assert by_source["hermes_native_inventory"]["approval_status"] == "not_inferred"

    urls = [row[0] for row in observed]
    assert urls == [
        "http://paperless-gateway:8082/health",
        "http://pantheon-policy-api:8000/readyz",
        "http://pantheon-policy-api:8000/v1/meta",
        "http://docling-serve:5001/health",
    ]
    assert observed[0][1] == "Bearer read-key"
    assert observed[1][1] == "Bearer policy-key"
    assert observed[2][1] == "Bearer policy-key"
    assert observed[3][2] == "docling-key"


def test_hermes_inventory_is_not_guessed_when_observer_is_not_on_hermes_host():
    result = observe_hermes_skill_inventory(mode="disabled")
    assert result["runtime_cli_status"] == "not_observed"
    assert result["installation_status"] == "not_observed"
    assert result["activation_status"] == "not_inferred"


def test_hermes_inventory_uses_fixed_native_list_command_without_shell():
    called = {}

    def runner(command, **kwargs):
        called["command"] = command
        called["kwargs"] = kwargs
        return SimpleNamespace(
            returncode=0,
            stdout="pantheon-document-intake\nother-skill\n",
            stderr="",
        )

    result = observe_hermes_skill_inventory(
        mode="local_cli",
        cli_path="hermes",
        runner=runner,
        which=lambda name: "/opt/hermes/bin/hermes" if name == "hermes" else None,
    )
    assert called["command"] == ["/opt/hermes/bin/hermes", "skills", "list"]
    assert "shell" not in called["kwargs"]
    assert called["kwargs"]["capture_output"] is True
    assert result["installation_status"] == "installed_observed"


def test_observer_api_requires_read_key_and_exposes_only_collector_projection():
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
