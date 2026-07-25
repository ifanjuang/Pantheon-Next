from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
COMPOSE = ROOT / "compose.phase-b.yaml"


def _compose() -> dict:
    value = yaml.safe_load(COMPOSE.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_phase_b_compose_uses_external_ai_net_and_no_database_host_port():
    compose = _compose()
    services = compose["services"]

    assert compose["networks"]["ai-net"]["external"] is True
    assert compose["networks"]["ai-net"]["name"] == "ai-net"

    required = {
        "pgvector",
        "docling",
        "paperless-broker",
        "paperless-db",
        "paperless",
        "paperless-gateway",
        "cockpit-api",
        "hermes",
        "document-runtime-observer",
    }
    assert required <= set(services)

    for name in required:
        assert "ai-net" in services[name]["networks"]

    for name in (
        "pgvector",
        "docling",
        "paperless-broker",
        "paperless-db",
        "paperless-gateway",
        "cockpit-api",
        "hermes",
        "document-runtime-observer",
    ):
        assert "ports" not in services[name]

    paperless_ports = services["paperless"]["ports"]
    assert paperless_ports == [
        "${PAPERLESS_HOST_BIND:-127.0.0.1}:${PAPERLESS_HOST_PORT:-8000}:8000"
    ]


def test_phase_b_cockpit_does_not_receive_backing_paperless_or_policy_secrets():
    services = _compose()["services"]
    cockpit_env = services["cockpit-api"]["environment"]

    assert "PAPERLESS_API_TOKEN" not in cockpit_env
    assert "PANTHEON_POLICY_API_KEY" not in cockpit_env
    assert "PANTHEON_DECISION_ISSUER_SIGNING_SECRET" not in cockpit_env
    assert "PANTHEON_DECISION_ISSUER_KEYS_PATH" not in cockpit_env

    gateway_env = services["paperless-gateway"]["environment"]
    assert "PAPERLESS_API_TOKEN" in gateway_env
    assert "PANTHEON_POLICY_API_KEY" in gateway_env


def test_phase_b_hermes_gets_bounded_gateway_inputs_not_backing_runtime_secrets():
    services = _compose()["services"]
    hermes_env = services["hermes"]["environment"]

    assert hermes_env["API_SERVER_ENABLED"] == "true"
    assert hermes_env["API_SERVER_HOST"] == "0.0.0.0"
    assert hermes_env["API_SERVER_PORT"] == "8642"
    assert "API_SERVER_KEY" in hermes_env
    assert hermes_env["PANTHEON_PAPERLESS_GATEWAY_URL"] == "http://paperless-gateway:8082"
    assert "MVP_HERMES_API_KEY" in hermes_env

    for forbidden in (
        "PAPERLESS_API_TOKEN",
        "PANTHEON_POLICY_API_KEY",
        "PANTHEON_DECISION_ISSUER_SIGNING_SECRET",
        "PANTHEON_DECISION_ISSUER_KEYS_PATH",
        "PAPERLESS_DB_PASSWORD",
    ):
        assert forbidden not in hermes_env


def test_phase_b_observer_uses_authenticated_hermes_http_inventory():
    services = _compose()["services"]
    observer = services["document-runtime-observer"]
    env = observer["environment"]

    assert observer["command"] == [
        "python",
        "-m",
        "mvp_vertical.document_runtime_network_observer",
    ]
    assert env["HERMES_API_URL"] == "http://hermes:8642"
    assert "HERMES_API_SERVER_KEY" in env
    assert env["PANTHEON_POLICY_API_URL"] == "http://pantheon-policy-api:8000"
    assert env["PANTHEON_PAPERLESS_GATEWAY_URL"] == "http://paperless-gateway:8082"
    assert env["DOCLING_SERVE_URL"] == "http://docling:5001"

    assert "PAPERLESS_API_TOKEN" not in env
    assert "MVP_HERMES_API_KEY" not in env
    assert "PANTHEON_DECISION_ISSUER_SIGNING_SECRET" not in env


def test_phase_b_mvp_services_share_one_reviewable_build_image():
    services = _compose()["services"]
    for name in ("paperless-gateway", "cockpit-api", "document-runtime-observer"):
        service = services[name]
        assert service["build"] == {"context": ".", "dockerfile": "Dockerfile"}
        assert service["image"] == (
            "${PANTHEON_MVP_IMAGE_NAME:-pantheon-mvp}:"
            "${PANTHEON_MVP_IMAGE_TAG:-phase-b}"
        )
