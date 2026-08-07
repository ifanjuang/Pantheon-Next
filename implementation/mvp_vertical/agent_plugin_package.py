"""Load and normalize Agent Plugins observations without granting authority.

The loader implements the bounded Agent Plugins v1 package-reading boundary. It
reads local package files and validates supported structures; it never downloads
schemas, installs or executes components, configures Hermes, activates capabilities,
or authorizes tasks.
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml


PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
_PLUGIN_FIELDS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}
_PLUGIN_NAME = re.compile(r"^[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?$")
_SKILL_NAME = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")

LOADER_AUTHORITY = {
    "installs_components": False,
    "activates_capabilities": False,
    "authorizes_tasks": False,
    "executes_components": False,
    "fetches_remote_schemas": False,
}


class AgentPluginPackageError(ValueError):
    pass


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
    """Return component-local, provenance-bearing Agent Plugin observations."""
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


def _inside(root: Path, candidate: Path) -> bool:
    try:
        candidate.relative_to(root)
        return True
    except ValueError:
        return False


def _read_json_object(path: Path, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise AgentPluginPackageError(f"invalid {label}: unable to read JSON") from exc
    if not isinstance(value, dict):
        raise AgentPluginPackageError(f"invalid {label}: top level must be an object")
    return value


def _load_manifest(path: Path) -> tuple[dict[str, Any], list[str]]:
    raw = _read_json_object(path, label="plugin.json")
    warnings: list[str] = []
    unknown = sorted(set(raw) - _PLUGIN_FIELDS)
    for field in unknown:
        warnings.append(f"ignored_unknown_manifest_field:{field}")

    manifest = {key: value for key, value in raw.items() if key in _PLUGIN_FIELDS}
    if manifest.get("$schema") != PLUGIN_SCHEMA:
        raise AgentPluginPackageError("unsupported plugin manifest schema")
    name = manifest.get("name")
    if not isinstance(name, str) or not _PLUGIN_NAME.fullmatch(name):
        raise AgentPluginPackageError("invalid plugin name")
    if "--" in name or ".." in name:
        raise AgentPluginPackageError("invalid plugin name repetition")

    for field in ("version", "description", "homepage", "repository", "license"):
        if field in manifest and not isinstance(manifest[field], str):
            raise AgentPluginPackageError(f"invalid plugin manifest field: {field}")
    author = manifest.get("author")
    if author is not None:
        if not isinstance(author, dict) or set(author) - {"name", "email", "url"}:
            raise AgentPluginPackageError("invalid plugin manifest field: author")
        if any(not isinstance(value, str) for value in author.values()):
            raise AgentPluginPackageError("invalid plugin manifest field: author")
    keywords = manifest.get("keywords")
    if keywords is not None and (
        not isinstance(keywords, list) or any(not isinstance(item, str) for item in keywords)
    ):
        raise AgentPluginPackageError("invalid plugin manifest field: keywords")

    if "extensions" in manifest and not isinstance(manifest["extensions"], dict):
        manifest.pop("extensions")
        warnings.append("ignored_non_object_extensions")
    return manifest, warnings


def _skill_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    closing = text.find("\n---", 4)
    if closing < 0:
        raise ValueError("unterminated frontmatter")
    try:
        value = yaml.safe_load(text[4:closing])
    except yaml.YAMLError as exc:
        raise ValueError("invalid yaml") from exc
    if not isinstance(value, dict):
        raise ValueError("frontmatter must be an object")
    return value


def _valid_skill(path: Path, directory_name: str) -> bool:
    try:
        metadata = _skill_frontmatter(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return False
    name = metadata.get("name")
    description = metadata.get("description")
    if (
        not isinstance(name, str)
        or not _SKILL_NAME.fullmatch(name)
        or "--" in name
        or name != directory_name
    ):
        return False
    if not isinstance(description, str) or not (1 <= len(description) <= 1024):
        return False
    compatibility = metadata.get("compatibility")
    if compatibility is not None and (
        not isinstance(compatibility, str) or not (1 <= len(compatibility) <= 500)
    ):
        return False
    for field in ("license", "allowed-tools"):
        if field in metadata and not isinstance(metadata[field], str):
            return False
    extra = metadata.get("metadata")
    if extra is not None and (
        not isinstance(extra, dict)
        or any(not isinstance(k, str) or not isinstance(v, str) for k, v in extra.items())
    ):
        return False
    return True


def _load_skills(root: Path, warnings: list[str]) -> list[dict[str, Any]]:
    skills_root = root / "skills"
    if not skills_root.exists():
        return []
    resolved_skills = skills_root.resolve()
    if not skills_root.is_dir() or not _inside(root, resolved_skills):
        warnings.append("invalid_skills_location")
        return []

    observations: list[dict[str, Any]] = []
    for directory in sorted(skills_root.iterdir(), key=lambda item: item.name):
        if not directory.is_dir():
            continue
        skill_path = directory / "SKILL.md"
        if not skill_path.exists():
            continue
        try:
            resolved = skill_path.resolve(strict=True)
        except OSError:
            observations.append(
                {"name": directory.name, "status": "invalid", "reason": "invalid_skill_manifest"}
            )
            continue
        if not _inside(root, resolved):
            observations.append(
                {
                    "name": directory.name,
                    "status": "invalid",
                    "reason": "skill_path_outside_plugin_root",
                }
            )
            continue
        if not resolved.is_file() or not _valid_skill(resolved, directory.name):
            observations.append(
                {"name": directory.name, "status": "invalid", "reason": "invalid_skill_manifest"}
            )
            continue
        observations.append({"name": directory.name, "status": "valid"})
    return observations


def _string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def _string_map(value: Any) -> bool:
    return isinstance(value, dict) and all(
        isinstance(key, str) and isinstance(item, str) for key, item in value.items()
    )


def _root_relative_path_is_safe(root: Path, value: str) -> bool:
    if not value.startswith("./"):
        return False
    return _inside(root, (root / value[2:]).resolve(strict=False))


def _placeholder_path_is_safe(value: str, placeholder: str) -> bool:
    if value == placeholder:
        return True
    prefix = placeholder + "/"
    if not value.startswith(prefix):
        return False
    remainder = value[len(prefix) :]
    return ".." not in Path(remainder).parts


def _valid_stdio(root: Path, server: dict[str, Any]) -> bool:
    if set(server) - {"type", "command", "args", "env", "cwd"}:
        return False
    command = server.get("command")
    if not isinstance(command, str) or not command or any(char.isspace() for char in command):
        return False
    if command.startswith("./"):
        if not _root_relative_path_is_safe(root, command):
            return False
    elif "/" in command or "\\" in command:
        return False
    args = server.get("args")
    if args is not None and not _string_list(args):
        return False
    env = server.get("env")
    if env is not None:
        if not _string_map(env) or {"PLUGIN_ROOT", "PLUGIN_DATA"} & set(env):
            return False
    cwd = server.get("cwd")
    if cwd is not None:
        if not isinstance(cwd, str):
            return False
        if not (
            _root_relative_path_is_safe(root, cwd)
            or _placeholder_path_is_safe(cwd, "${PLUGIN_ROOT}")
            or _placeholder_path_is_safe(cwd, "${PLUGIN_DATA}")
        ):
            return False
    return True


def _loopback_host(host: str) -> bool:
    if host == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def _valid_remote(server: dict[str, Any]) -> bool:
    if set(server) - {"type", "url", "headers"}:
        return False
    url = server.get("url")
    if not isinstance(url, str):
        return False
    parsed = urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return False
    if parsed.username is not None or parsed.password is not None or parsed.fragment:
        return False
    if parsed.scheme == "http" and not _loopback_host(parsed.hostname):
        return False
    headers = server.get("headers")
    if headers is not None:
        if not _string_map(headers):
            return False
        lowered = [key.lower() for key in headers]
        if len(lowered) != len(set(lowered)):
            return False
    return True


def _server_observation(root: Path, name: str, server: Any) -> dict[str, Any]:
    if not isinstance(server, dict):
        return {"name": name, "status": "invalid", "reason": "invalid_server_configuration"}
    transport = server.get("type")
    observation: dict[str, Any] = {"name": name, "status": "invalid"}
    if isinstance(transport, str):
        observation["type"] = transport
    valid = False
    if transport == "stdio":
        valid = _valid_stdio(root, server)
    elif transport in {"streamable-http", "sse"}:
        valid = _valid_remote(server)
    if valid:
        observation["status"] = "valid"
    else:
        observation["reason"] = "invalid_server_configuration"
    return observation


def _load_mcp(root: Path, manifest: dict[str, Any], warnings: list[str]) -> list[dict[str, Any]]:
    path = root / "mcp.json"
    if not path.exists():
        return []
    try:
        resolved = path.resolve(strict=True)
    except OSError:
        warnings.append("invalid_mcp_configuration")
        return []
    if not _inside(root, resolved) or not resolved.is_file():
        warnings.append("invalid_mcp_configuration")
        return []
    try:
        raw = _read_json_object(resolved, label="mcp.json")
    except AgentPluginPackageError:
        warnings.append("invalid_mcp_configuration")
        return []
    if set(raw) != {"$schema", "mcpServers"}:
        warnings.append("invalid_mcp_configuration")
        return []
    if raw.get("$schema") != MCP_SCHEMA or manifest.get("$schema") != PLUGIN_SCHEMA:
        warnings.append("invalid_mcp_configuration")
        return []
    servers = raw.get("mcpServers")
    if not isinstance(servers, dict):
        warnings.append("invalid_mcp_configuration")
        return []
    return [
        _server_observation(root, name, servers[name])
        for name in sorted(servers)
        if isinstance(name, str) and name
    ]


def load_agent_plugin_package(package_root: str | Path) -> dict[str, Any]:
    """Read one local Agent Plugins v1 package into non-authoritative observations."""
    supplied_root = Path(package_root)
    try:
        root = supplied_root.resolve(strict=True)
    except OSError as exc:
        raise AgentPluginPackageError("plugin root does not exist") from exc
    if not root.is_dir():
        raise AgentPluginPackageError("plugin root must be a directory")

    manifest_path = root / "plugin.json"
    try:
        resolved_manifest = manifest_path.resolve(strict=True)
    except OSError as exc:
        raise AgentPluginPackageError("plugin.json is required") from exc
    if not _inside(root, resolved_manifest) or not resolved_manifest.is_file():
        raise AgentPluginPackageError("plugin.json must remain inside plugin root")

    manifest, warnings = _load_manifest(resolved_manifest)
    skills = _load_skills(root, warnings)
    mcp_servers = _load_mcp(root, manifest, warnings)
    return {
        "manifest": manifest,
        "skills": skills,
        "mcp_servers": mcp_servers,
        "warnings": warnings,
        "authority": dict(LOADER_AUTHORITY),
    }
