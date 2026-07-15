from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "templates" / "hermes" / "dashboard-plugins" / "pantheon-modules"
MANIFEST = PLUGIN / "dashboard" / "manifest.json"
DIST = PLUGIN / "dashboard" / "dist" / "index.js"
CSS = PLUGIN / "dashboard" / "dist" / "style.css"


def _function_block(source: str, name: str, next_name: str) -> str:
    start = source.index(f"function {name}(")
    end = source.index(f"function {next_name}(", start)
    return source[start:end]


def _marked_block(source: str, start_marker: str, end_marker: str) -> str:
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    return source[start:end]


def test_dashboard_manifest_and_installer_manifest_are_aligned() -> None:
    dashboard = json.loads(MANIFEST.read_text(encoding="utf-8"))
    plugin = yaml.safe_load((PLUGIN / "plugin.yaml").read_text(encoding="utf-8"))

    assert dashboard["name"] == plugin["name"] == "pantheon-modules"
    assert dashboard["version"] == plugin["version"] == "0.1.0"
    assert dashboard["entry"] == "dist/index.js"
    assert dashboard["css"] == "dist/style.css"
    assert "api" not in dashboard
    marker = (PLUGIN / "__init__.py").read_text(encoding="utf-8")
    assert "registers no hooks, tools, providers, routes" in marker
    assert "def register(_ctx) -> None:" in marker
    assert ".register_" not in marker
    assert not plugin.get("hooks")
    assert not plugin.get("provides_tools")

    assert DIST.is_file()
    assert CSS.is_file()


def test_bundle_uses_host_sdk_and_preserves_state_axes() -> None:
    source = DIST.read_text(encoding="utf-8")

    assert "window.__HERMES_PLUGIN_SDK__" in source
    assert 'registry.register("pantheon-modules", PantheonModulesPage)' in source
    assert "__HERMES_SESSION_TOKEN__" not in source
    assert "localStorage." not in source
    assert "fetch(" not in source

    for api_method in (
        "getMemory",
        "getMcpCatalog",
        "getMcpServers",
        "getPluginsHub",
        "setMemoryProvider",
        "installMcpCatalogEntry",
        "setMcpServerEnabled",
        "testMcpServer",
        "enableAgentPlugin",
        "disableAgentPlugin",
    ):
        assert f'"{api_method}"' in source

    for label in (
        "Listed",
        "Detected",
        "Installed",
        "Configured",
        "Hermes enabled",
        "Reachable",
        "Health",
        "Governance",
        "Task use",
    ):
        assert f'"{label}"' in source

    assert "Hermes enabled ≠ Pantheon governance activation ≠ task authorization" in source


def test_every_native_operation_has_an_immediate_human_confirmation() -> None:
    source = DIST.read_text(encoding="utf-8")

    blocks = (
        _function_block(source, "handleMemory", "handlePlugin"),
        _function_block(source, "handlePlugin", "handleMcpToggle"),
        _function_block(source, "handleMcpToggle", "handleProbe"),
        _function_block(source, "handleProbe", "handleEnvChange"),
        _marked_block(source, "function handleInstall(", "const actionProps ="),
    )
    for block in blocks:
        assert "window.confirm(" in block


def test_known_capability_policies_remain_cautious() -> None:
    source = DIST.read_text(encoding="utf-8")

    for capability in ("mem0", "n8n", "pantheon-policy", "langgraph", "memvid"):
        assert capability in source

    for tool in (
        "health",
        "list_workflows",
        "get_workflow",
        "find_workflows",
        "list_executions",
        "get_execution",
        "recent_failures",
        "export_workflow",
        "activate_workflow",
        "deactivate_workflow",
        "container_logs",
    ):
        assert f'"{tool}"' in source

    assert "No native activation action is exposed for this candidate." in source
    assert "Only one external Hermes memory provider" in source
    assert "Installation or Hermes enablement never authorizes" in source


def test_review_first_install_documentation_uses_supported_subdirectory_form() -> None:
    readme = (PLUGIN / "README.md").read_text(encoding="utf-8")

    assert (
        "ifanjuang/Pantheon-Next/templates/hermes/dashboard-plugins/pantheon-modules"
        in readme
    )
    assert "--no-enable" in readme
    assert "hermes plugins enable pantheon-modules" in readme
    assert "8b209e0dd7b8e308d5b923fa80f7a72f71042636" in readme
    assert "7a9ae00795593aa1fdb4e61ecd640e8bfd0c3841" in readme


@pytest.mark.skipif(shutil.which("node") is None, reason="Node.js is not installed")
def test_bundle_syntax_and_normalizers_with_a_mock_host() -> None:
    subprocess.run(["node", "--check", str(DIST)], check=True, capture_output=True, text=True)

    script = f"""
global.window = {{
  __HERMES_PLUGIN_SDK__: {{
    React: {{ createElement: function () {{ return null; }} }},
    hooks: {{}},
    components: {{}},
    api: {{}}
  }},
  __HERMES_PLUGINS__: {{ register: function () {{}} }}
}};
require({json.dumps(str(DIST))});
const t = window.__PANTHEON_MODULES_TEST__;
const inventory = t.normalizeInventory({{
  memory: {{ active: "mem0", providers: [{{
    name: "mem0", status: "ready", configured: true, description: "memory"
  }}] }},
  catalog: {{ entries: [{{
    name: "n8n", description: "automation", installed: false, enabled: false,
    required_env: [{{ name: "N8N_API_KEY", required: true }}],
    default_enabled: ["health"]
  }}] }},
  servers: {{ servers: [{{ name: "pantheon-policy", enabled: true }}] }},
  hub: {{ plugins: [{{ name: "example", runtime_status: "disabled" }}] }}
}}, {{ "pantheon-policy": {{ ok: true, tools: [{{ name: "list_sources" }}] }} }});
if (!t.isSecretEnv("N8N_API_KEY") || t.isSecretEnv("N8N_BASE_URL")) process.exit(2);
if (!inventory.memory[0].enabled || inventory.memory[0].policy.governance !== "candidate") process.exit(3);
if (inventory.mcps[0].id !== "n8n" || inventory.mcps[0].configured !== null) process.exit(4);
const wiki = inventory.mcps.find(function (item) {{ return item.id === "pantheon-policy"; }});
if (!wiki || wiki.reachable !== true || wiki.policy.risk !== "low") process.exit(5);
if (inventory.plugins[0].enabled !== false) process.exit(6);
"""
    subprocess.run(["node", "-e", script], check=True, capture_output=True, text=True)
