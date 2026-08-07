"""Normalize Agent Plugins package observations without granting authority.

This module is intentionally limited to already-parsed observations supplied by
callers. It does not read package files, install components, configure Hermes,
activate capabilities, or authorize tasks.
"""

from __future__ import annotations

import hashlib
from typing import Any


def _component_id(package_digest: str, component_kind: str, component_ref: str) -> str:
    material = f"{package_digest}\0{component_kind}\0{component_ref}".encode("utf-8")
    return "agent-plugin-component-" + hashlib.sha256(material).hexdigest()[:24]


def _base_row(
    *,
    manifest: dict[str, Any],
    package_digest: str,
    component_kind: str,
    component_ref: str,
    observed_at: str,
) -> dict[str, Any]:
    return {
        "source_kind": "agent_plugin",
        "package_name": manifest.get("name"),
        "package_version": manifest.get("version"),
        "package_digest": package_digest,
        "component_id": _component_id(package_digest, component_kind, component_ref),
        "component_kind": component_kind,
        "component_ref": component_ref,
        "governance_state": "unreviewed",
        "activation_state": "not_activated",
        "task_authorization": "unauthorized",
        "package_extensions_are_claims": True,
        "observed_at": observed_at,
    }


def _component_status(component: dict[str, Any]) -> str:
    return "discovered" if component.get("status") == "valid" else "invalid"


def normalize_agent_plugin_inventory(
    *,
    manifest: dict[str, Any],
    package_digest: str,
    skills: list[dict[str, Any]],
    mcp_servers: list[dict[str, Any]],
    observed_at: str,
) -> list[dict[str, Any]]:
    """Return component-local, provenance-bearing Agent Plugin observations.

    Package metadata is descriptive provenance only. Every component starts
    unreviewed, not activated, and unauthorized regardless of package extension
    claims. Invalid components remain local failures and do not affect siblings.
    """
    rows: list[dict[str, Any]] = []

    for skill in skills:
        name = str(skill.get("name") or "").strip()
        if not name:
            continue
        component_ref = f"skills/{name}/SKILL.md"
        row = _base_row(
            manifest=manifest,
            package_digest=package_digest,
            component_kind="skill",
            component_ref=component_ref,
            observed_at=observed_at,
        )
        row["component_status"] = _component_status(skill)
        if row["component_status"] == "invalid" and skill.get("reason"):
            row["failure_reason"] = str(skill["reason"])
        rows.append(row)

    for server in mcp_servers:
        name = str(server.get("name") or "").strip()
        if not name:
            continue
        component_ref = f"mcp.json#mcpServers/{name}"
        row = _base_row(
            manifest=manifest,
            package_digest=package_digest,
            component_kind="mcp_server",
            component_ref=component_ref,
            observed_at=observed_at,
        )
        row["component_status"] = _component_status(server)
        if row["component_status"] == "invalid" and server.get("reason"):
            row["failure_reason"] = str(server["reason"])
        if server.get("type") is not None:
            row["transport"] = server.get("type")
        rows.append(row)

    return rows
