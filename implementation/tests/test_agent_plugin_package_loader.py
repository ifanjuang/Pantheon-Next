"""Contract tests for bounded Agent Plugins v1 package loading.

The loader reads and validates package metadata/components only. It must not install,
activate, execute, authorize, fetch remote schemas, or promote package claims.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from mvp_vertical import agent_plugin_package


PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _manifest(**extra) -> dict:
    value = {"$schema": PLUGIN_SCHEMA, "name": "project-tools", "version": "1.2.3"}
    value.update(extra)
    return value


def _skill(name: str, description: str = "Inspect a bounded project package.") -> str:
    return f"---\nname: {name}\ndescription: {description}\n---\n\n# {name}\n"


def test_loader_discovers_valid_skill_and_mcp_without_granting_authority(tmp_path: Path) -> None:
    _write(tmp_path / "plugin.json", json.dumps(_manifest()))
    _write(tmp_path / "skills" / "inspect-project" / "SKILL.md", _skill("inspect-project"))
    _write(
        tmp_path / "mcp.json",
        json.dumps(
            {
                "$schema": MCP_SCHEMA,
                "mcpServers": {
                    "revit-read": {"type": "stdio", "command": "./bin/revit-read"},
                    "project-api": {"type": "streamable-http", "url": "https://example.com/mcp"},
                },
            }
        ),
    )
    _write(tmp_path / "bin" / "revit-read", "not executed")

    loaded = agent_plugin_package.load_agent_plugin_package(tmp_path)

    assert loaded["manifest"]["name"] == "project-tools"
    assert loaded["warnings"] == []
    assert loaded["skills"] == [{"name": "inspect-project", "status": "valid"}]
    assert loaded["mcp_servers"] == [
        {"name": "project-api", "status": "valid", "type": "streamable-http"},
        {"name": "revit-read", "status": "valid", "type": "stdio"},
    ]
    assert loaded["authority"] == {
        "installs_components": False,
        "activates_capabilities": False,
        "authorizes_tasks": False,
        "executes_components": False,
        "fetches_remote_schemas": False,
    }


def test_manifest_unknown_field_and_non_object_extensions_are_reported_and_ignored(tmp_path: Path) -> None:
    manifest = _manifest(approved=True, extensions="not-an-object")
    _write(tmp_path / "plugin.json", json.dumps(manifest))
    _write(tmp_path / "skills" / "inspect-project" / "SKILL.md", _skill("inspect-project"))

    loaded = agent_plugin_package.load_agent_plugin_package(tmp_path)

    assert "approved" not in loaded["manifest"]
    assert "extensions" not in loaded["manifest"]
    assert set(loaded["warnings"]) == {
        "ignored_unknown_manifest_field:approved",
        "ignored_non_object_extensions",
    }
    assert loaded["skills"][0]["status"] == "valid"


def test_fatal_manifest_error_stops_component_discovery(tmp_path: Path) -> None:
    _write(tmp_path / "plugin.json", json.dumps({"$schema": PLUGIN_SCHEMA, "name": "Bad Name"}))
    _write(tmp_path / "skills" / "inspect-project" / "SKILL.md", _skill("inspect-project"))

    with pytest.raises(agent_plugin_package.AgentPluginPackageError, match="plugin name"):
        agent_plugin_package.load_agent_plugin_package(tmp_path)


def test_invalid_skill_and_invalid_mcp_server_are_local_failures(tmp_path: Path) -> None:
    _write(tmp_path / "plugin.json", json.dumps(_manifest()))
    _write(tmp_path / "skills" / "good-skill" / "SKILL.md", _skill("good-skill"))
    _write(tmp_path / "skills" / "bad-skill" / "SKILL.md", _skill("different-name"))
    _write(
        tmp_path / "mcp.json",
        json.dumps(
            {
                "$schema": MCP_SCHEMA,
                "mcpServers": {
                    "good-http": {"type": "streamable-http", "url": "https://example.com/mcp"},
                    "bad-http": {"type": "streamable-http", "url": "http://example.com/mcp"},
                },
            }
        ),
    )

    loaded = agent_plugin_package.load_agent_plugin_package(tmp_path)
    skills = {item["name"]: item for item in loaded["skills"]}
    servers = {item["name"]: item for item in loaded["mcp_servers"]}

    assert skills["good-skill"]["status"] == "valid"
    assert skills["bad-skill"] == {
        "name": "bad-skill",
        "status": "invalid",
        "reason": "invalid_skill_manifest",
    }
    assert servers["good-http"]["status"] == "valid"
    assert servers["bad-http"] == {
        "name": "bad-http",
        "status": "invalid",
        "reason": "invalid_server_configuration",
        "type": "streamable-http",
    }


def test_mcp_top_level_failure_disables_only_mcp_and_skill_path_escape_is_refused(tmp_path: Path) -> None:
    _write(tmp_path / "plugin.json", json.dumps(_manifest()))
    _write(tmp_path / "skills" / "good-skill" / "SKILL.md", _skill("good-skill"))
    _write(
        tmp_path / "mcp.json",
        json.dumps({"$schema": "https://agent-plugins.org/schemas/9.9.9/mcp.schema.json", "mcpServers": {}}),
    )

    loaded = agent_plugin_package.load_agent_plugin_package(tmp_path)
    assert loaded["skills"] == [{"name": "good-skill", "status": "valid"}]
    assert loaded["mcp_servers"] == []
    assert "invalid_mcp_configuration" in loaded["warnings"]

    outside = tmp_path.parent / "outside-skill.md"
    _write(outside, _skill("escaped"))
    escaped_dir = tmp_path / "skills" / "escaped"
    escaped_dir.mkdir(parents=True)
    try:
        (escaped_dir / "SKILL.md").symlink_to(outside)
    except OSError:
        pytest.skip("symlink creation unavailable")

    reloaded = agent_plugin_package.load_agent_plugin_package(tmp_path)
    by_name = {item["name"]: item for item in reloaded["skills"]}
    assert by_name["good-skill"]["status"] == "valid"
    assert by_name["escaped"] == {
        "name": "escaped",
        "status": "invalid",
        "reason": "skill_path_outside_plugin_root",
    }
