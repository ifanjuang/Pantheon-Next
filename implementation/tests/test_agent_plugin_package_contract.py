"""Deliberately red contract for Agent Plugins package provenance normalization.

This slice defines the minimum MVP-side normalization boundary only. It does not
parse packages, install components, activate capabilities, or authorize tasks.
"""

from importlib import import_module


PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"


def _normalizer():
    module = import_module("mvp_vertical.agent_plugin_package")
    return module.normalize_agent_plugin_inventory


def _package_manifest():
    return {
        "$schema": PLUGIN_SCHEMA,
        "name": "example-project-tools",
        "version": "1.2.3",
        "extensions": {
            "fr.example.pantheon": {
                "approved": True,
                "risk": "low",
            }
        },
    }


def test_agent_plugin_package_is_provenance_not_governance_authority():
    rows = _normalizer()(
        manifest=_package_manifest(),
        package_digest="sha256:abc123",
        skills=[{"name": "inspect-project", "status": "valid"}],
        mcp_servers=[],
        observed_at="2026-08-07T08:00:00Z",
    )

    assert len(rows) == 1
    row = rows[0]
    assert row["source_kind"] == "agent_plugin"
    assert row["package_name"] == "example-project-tools"
    assert row["package_version"] == "1.2.3"
    assert row["package_digest"] == "sha256:abc123"
    assert row["component_kind"] == "skill"
    assert row["component_ref"] == "skills/inspect-project/SKILL.md"
    assert row["governance_state"] == "unreviewed"
    assert row["activation_state"] == "not_activated"
    assert row["task_authorization"] == "unauthorized"
    assert "approved" not in row


def test_agent_plugin_components_keep_independent_failure_boundaries():
    rows = _normalizer()(
        manifest=_package_manifest(),
        package_digest="sha256:abc123",
        skills=[
            {"name": "inspect-project", "status": "valid"},
            {"name": "broken-skill", "status": "invalid", "reason": "invalid_skill_manifest"},
        ],
        mcp_servers=[
            {"name": "revit-read", "status": "valid", "type": "stdio"},
            {"name": "broken-mcp", "status": "invalid", "reason": "unsupported_transport"},
        ],
        observed_at="2026-08-07T08:00:00Z",
    )

    by_ref = {row["component_ref"]: row for row in rows}
    assert by_ref["skills/inspect-project/SKILL.md"]["component_status"] == "discovered"
    assert by_ref["skills/broken-skill/SKILL.md"]["component_status"] == "invalid"
    assert by_ref["mcp.json#mcpServers/revit-read"]["component_status"] == "discovered"
    assert by_ref["mcp.json#mcpServers/broken-mcp"]["component_status"] == "invalid"
    assert by_ref["mcp.json#mcpServers/broken-mcp"]["failure_reason"] == "unsupported_transport"


def test_package_level_metadata_never_promotes_component_authorization():
    rows = _normalizer()(
        manifest=_package_manifest(),
        package_digest="sha256:abc123",
        skills=[{"name": "inspect-project", "status": "valid"}],
        mcp_servers=[{"name": "project-write", "status": "valid", "type": "streamable-http"}],
        observed_at="2026-08-07T08:00:00Z",
    )

    assert {row["governance_state"] for row in rows} == {"unreviewed"}
    assert {row["activation_state"] for row in rows} == {"not_activated"}
    assert {row["task_authorization"] for row in rows} == {"unauthorized"}
    assert all(row["package_extensions_are_claims"] is True for row in rows)


def test_same_package_may_supply_multiple_component_kinds_without_collapsing_identity():
    rows = _normalizer()(
        manifest=_package_manifest(),
        package_digest="sha256:abc123",
        skills=[{"name": "inspect-project", "status": "valid"}],
        mcp_servers=[{"name": "revit-read", "status": "valid", "type": "stdio"}],
        observed_at="2026-08-07T08:00:00Z",
    )

    assert {(row["component_kind"], row["component_ref"]) for row in rows} == {
        ("skill", "skills/inspect-project/SKILL.md"),
        ("mcp_server", "mcp.json#mcpServers/revit-read"),
    }
    assert len({row["component_id"] for row in rows}) == 2
    assert {row["package_digest"] for row in rows} == {"sha256:abc123"}
