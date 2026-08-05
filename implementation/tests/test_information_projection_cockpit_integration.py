"""Cockpit integration expectation for Information projection routes."""

from __future__ import annotations

from mvp_vertical.information_projection_api import install_information_projection_routes


def test_information_projection_installer_is_available() -> None:
    assert callable(install_information_projection_routes)
