"""Route-identity guard for the bounded Pantheon policy HTTP adapter."""

from __future__ import annotations

import sys
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_DIR))

from pantheon_mcp.http_api import create_app  # noqa: E402


def test_mounted_policy_routes_use_stable_responsibility_paths() -> None:
    app = create_app(api_key="route-identity-test", enable_docs=False)
    mounted = sorted(
        route.path
        for route in app.routes
        if getattr(route, "path", None)
    )

    assert mounted
    assert not [path for path in mounted if path == "/v1" or path.startswith("/v1/")]
    assert "/meta" in mounted
    assert "/policy/requests:classify" in mounted
    assert "/context-packs:validate" in mounted


def test_contract_revision_is_not_confused_with_route_identity() -> None:
    app = create_app(api_key="route-identity-test", enable_docs=False)
    assert app.version == "1.0.0-candidate"
