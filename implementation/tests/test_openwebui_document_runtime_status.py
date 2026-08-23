from __future__ import annotations

import asyncio

from openwebui.pantheon_document_runtime_status import Tools


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


def _tools(payload):
    observed = []
    response = _Response(payload)
    tools = Tools(client_factory=lambda **kwargs: _Client(response, observed, **kwargs))
    tools.valves.gateway_url = "http://paperless-gateway:8082"
    tools.valves.api_key = "read-key"
    return tools, observed


def test_runtime_status_separates_reachability_from_health_and_activation():
    tools, observed = _tools(
        {
            "status": "ok",
            "paperless_reachable": True,
            "write_surface": "governed_only",
            "intake_surface": "governed_only",
        }
    )

    response, context = asyncio.run(tools.show_document_runtime_status())
    rendered = response.body.decode("utf-8")

    assert observed == ["http://paperless-gateway:8082/health"]
    assert "Paperless-ngx" in rendered
    assert "reachable" in rendered
    assert "not_established_by_reachability_probe" in rendered
    assert context["source_runtime"] == {
        "resource": "paperless_ngx",
        "reachability_status": "reachable",
        "health_status": "not_established_by_reachability_probe",
    }
    assert context["governance"] == {
        "activation_changed": False,
        "authority_effect": "none",
        "write_effect": False,
    }


def test_runtime_status_does_not_infer_hermes_skill_installation_or_policy_health():
    tools, _ = _tools(
        {
            "status": "ok",
            "paperless_reachable": True,
            "write_surface": "governed_only",
            "intake_surface": "governed_only",
        }
    )
    _, context = asyncio.run(tools.show_document_runtime_status())

    assert context["hermes_skill"] == {
        "skill": "pantheon-document-intake",
        "installation_status": "not_observed_by_gateway",
        "inventory_source": "hermes_native_inventory",
    }
    assert context["policy"]["reachability_status"] == "not_observed_by_this_surface"
    assert context["policy"]["authorization_status"] == "not_inferred"
    assert context["docling"]["health_status"] == "not_established"


def test_runtime_status_reports_paperless_unreachable_without_calling_it_unsafe():
    tools, _ = _tools(
        {
            "status": "degraded",
            "paperless_reachable": False,
            "write_surface": "fail_closed",
            "intake_surface": "fail_closed",
        }
    )
    response, context = asyncio.run(tools.show_document_runtime_status())
    rendered = response.body.decode("utf-8")

    assert context["source_runtime"]["reachability_status"] == "unreachable"
    assert context["gateway"]["status"] == "degraded"
    assert context["gateway"]["write_surface"] == "fail_closed"
    assert "Safety" in rendered
    assert "not_inferred" in rendered


def test_runtime_status_keeps_gateway_key_in_header_not_url():
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
                    "status": "ok",
                    "paperless_reachable": True,
                    "write_surface": "governed_only",
                    "intake_surface": "governed_only",
                }
            )

    tools = Tools(client_factory=Client)
    tools.valves.gateway_url = "http://paperless-gateway:8082"
    tools.valves.api_key = "super-secret-read-key"
    asyncio.run(tools.show_document_runtime_status())

    assert observed["headers"]["Authorization"] == "Bearer super-secret-read-key"
    assert "super-secret-read-key" not in observed["url"]
