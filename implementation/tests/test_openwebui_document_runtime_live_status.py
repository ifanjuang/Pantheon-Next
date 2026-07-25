from __future__ import annotations

import asyncio

from openwebui.pantheon_document_runtime_live_status import Tools


class _Response:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload

    def raise_for_status(self):
        if not 200 <= self.status_code < 300:
            raise RuntimeError(f"HTTP {self.status_code}")


class _Client:
    def __init__(self, response, observed, **kwargs):
        self.response = response
        self.observed = observed
        self.kwargs = kwargs

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return False

    async def get(self, url):
        self.observed.append(url)
        return self.response


def test_live_status_renders_independent_observations_without_global_health():
    payload = {
        "object_type": "document_runtime_observation_set",
        "observed_at": "2026-07-24T06:00:00Z",
        "observations": [
            {
                "source": "paperless_gateway",
                "observation_source": "bounded_gateway_health",
                "observed_at": "2026-07-24T06:00:00Z",
                "reachability_status": "reachable",
                "paperless_reachability_status": "reachable",
                "health_status": "not_established_by_reachability_probe",
                "safety_status": "not_inferred",
            },
            {
                "source": "pantheon_pdp",
                "observation_source": "pantheon_policy_http",
                "observed_at": "2026-07-24T06:00:00Z",
                "reachability_status": "reachable",
                "readiness_status": "ready_observed",
                "authorization_status": "not_inferred_from_readiness",
            },
            {
                "source": "docling_serve",
                "observation_source": "docling_health_endpoint",
                "observed_at": "2026-07-24T06:00:00Z",
                "reachability_status": "reachable",
                "extraction_quality_status": "not_established_by_health_probe",
            },
            {
                "source": "hermes_native_inventory",
                "observation_source": "hermes_skills_list",
                "observed_at": "2026-07-24T06:00:00Z",
                "installation_status": "installed_observed",
                "activation_status": "not_inferred",
                "approval_status": "not_inferred",
            },
        ],
        "synthetic_global_health": "not_computed",
        "authority_effect": "none",
        "write_effect": False,
        "activation_changed": False,
        "non_equivalences": [
            "reachable != healthy",
            "installed != approved",
            "PDP ready != effect authorized",
        ],
    }
    observed = []
    response = _Response(payload)
    tools = Tools(client_factory=lambda **kwargs: _Client(response, observed, **kwargs))
    tools.valves.observer_url = "http://document-runtime-observer:8083"
    tools.valves.api_key = "read-key"

    html_response, context = asyncio.run(tools.show_document_runtime_live_status())
    rendered = html_response.body.decode("utf-8")

    assert observed == [
        "http://document-runtime-observer:8083/v1/document-runtime/observations"
    ]
    for title in (
        "Paperless / Gateway",
        "Pantheon PDP",
        "Docling Serve",
        "Hermes · pantheon-document-intake",
    ):
        assert title in rendered
    assert "not_computed" not in rendered
    assert "Aucun score global" in rendered
    assert "PDP ready != effect authorized" in rendered
    assert context["synthetic_global_health"] == "not_computed"
    assert context["governance"] == {
        "authority_effect": "none",
        "write_effect": False,
        "activation_changed": False,
    }


def test_live_status_keeps_observer_read_key_in_header():
    observed = {}

    class Client:
        def __init__(self, **kwargs):
            observed["headers"] = kwargs["headers"]

        async def __aenter__(self):
            return self

        async def __aexit__(self, *_args):
            return False

        async def get(self, url):
            observed["url"] = url
            return _Response(
                {
                    "observations": [],
                    "synthetic_global_health": "not_computed",
                    "authority_effect": "none",
                    "write_effect": False,
                    "activation_changed": False,
                }
            )

    tools = Tools(client_factory=Client)
    tools.valves.observer_url = "http://document-runtime-observer:8083"
    tools.valves.api_key = "super-secret-read-key"
    asyncio.run(tools.show_document_runtime_live_status())

    assert observed["headers"]["Authorization"] == "Bearer super-secret-read-key"
    assert "super-secret-read-key" not in observed["url"]
