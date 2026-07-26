from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CORE_COMPOSE = ROOT / "compose.phase-b.yaml"
PAPERLESS_COMPOSE = ROOT / "compose.paperless.yaml"


def _compose(path: Path) -> dict:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def test_phase_b_core_uses_external_ai_net_and_contains_no_paperless_services():
    compose = _compose(CORE_COMPOSE)
    services = compose["services"]

    assert compose["networks"]["ai-net"]["external"] is True
    assert compose["networks"]["ai-net"]["name"] == "ai-net"

    core = {
        "pgvector",
        "docling",
        "cockpit-api",
        "hermes",
        "document-runtime-observer",
    }
    assert core <= set(services)
    assert not {
        "paperless-broker",
        "paperless-db",
        "paperless",
        "paperless-gateway",
    } & set(services)

    for name in core:
        assert "ai-net" in services[name]["networks"]
        assert "ports" not in services[name]

    observer = services["document-runtime-observer"]
    assert "paperless-gateway" not in observer.get("depends_on", {})
    assert observer["environment"]["MVP_DOCUMENT_SOURCE_BINDING"] == (
        "${MVP_DOCUMENT_SOURCE_BINDING:-governed_local_source}"
    )
    assert "PANTHEON_PAPERLESS_GATEWAY_URL" not in observer["environment"]

    hermes_env = services["hermes"]["environment"]
    assert "PANTHEON_PAPERLESS_GATEWAY_URL" not in hermes_env
    assert "MVP_HERMES_API_KEY" not in hermes_env


def test_paperless_overlay_contains_only_optional_binding_and_core_overrides():
    compose = _compose(PAPERLESS_COMPOSE)
    services = compose["services"]

    assert compose["networks"]["ai-net"]["external"] is True
    assert compose["networks"]["ai-net"]["name"] == "ai-net"

    assert set(services) == {
        "paperless-broker",
        "paperless-db",
        "paperless",
        "paperless-gateway",
        "hermes",
        "document-runtime-observer",
    }

    for name in ("paperless-broker", "paperless-db", "paperless", "paperless-gateway"):
        assert "ai-net" in services[name]["networks"]

    for name in ("paperless-broker", "paperless-db", "paperless-gateway"):
        assert "ports" not in services[name]

    assert services["paperless"]["ports"] == [
        "${PAPERLESS_HOST_BIND:-127.0.0.1}:${PAPERLESS_HOST_PORT:-8000}:8000"
    ]

    hermes_env = services["hermes"]["environment"]
    assert hermes_env["PANTHEON_PAPERLESS_GATEWAY_URL"] == "http://paperless-gateway:8082"
    assert "MVP_HERMES_API_KEY" in hermes_env

    observer = services["document-runtime-observer"]
    assert observer["depends_on"]["paperless-gateway"]["condition"] == "service_started"
    assert observer["environment"]["MVP_DOCUMENT_SOURCE_BINDING"] == "paperless_ngx"
    assert observer["environment"]["PANTHEON_PAPERLESS_GATEWAY_URL"] == (
        "http://paperless-gateway:8082"
    )


def test_core_compose_does_not_reference_paperless_required_variables():
    text = CORE_COMPOSE.read_text(encoding="utf-8")
    for name in (
        "PAPERLESS_IMAGE",
        "PAPERLESS_DB_IMAGE",
        "PAPERLESS_BROKER_IMAGE",
        "PAPERLESS_DB_PASSWORD",
        "PAPERLESS_SECRET_KEY",
        "PAPERLESS_DATA_PATH",
        "PAPERLESS_MEDIA_PATH",
        "PAPERLESS_API_TOKEN",
    ):
        assert name not in text


def test_phase_b_cockpit_does_not_receive_backing_paperless_or_policy_secrets():
    core_services = _compose(CORE_COMPOSE)["services"]
    overlay_services = _compose(PAPERLESS_COMPOSE)["services"]
    cockpit_env = core_services["cockpit-api"]["environment"]

    assert "PAPERLESS_API_TOKEN" not in cockpit_env
    assert "PANTHEON_POLICY_API_KEY" not in cockpit_env
    assert "PANTHEON_DECISION_ISSUER_SIGNING_SECRET" not in cockpit_env
    assert "PANTHEON_DECISION_ISSUER_KEYS_PATH" not in cockpit_env

    gateway_env = overlay_services["paperless-gateway"]["environment"]
    assert "PAPERLESS_API_TOKEN" in gateway_env
    assert "PANTHEON_POLICY_API_KEY" in gateway_env


def test_phase_b_mvp_services_share_one_reviewable_build_image():
    core_services = _compose(CORE_COMPOSE)["services"]
    overlay_services = _compose(PAPERLESS_COMPOSE)["services"]
    for service in (
        core_services["cockpit-api"],
        core_services["document-runtime-observer"],
        overlay_services["paperless-gateway"],
    ):
        assert service["build"] == {"context": ".", "dockerfile": "Dockerfile"}
        assert service["image"] == (
            "${PANTHEON_MVP_IMAGE_NAME:-pantheon-mvp}:"
            "${PANTHEON_MVP_IMAGE_TAG:-phase-b}"
        )
