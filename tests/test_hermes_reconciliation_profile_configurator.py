from __future__ import annotations

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "deployment" / "ubuntu" / "configure-hermes-reconciliation-profile"


def _text() -> str:
    return SCRIPT.read_text(encoding="utf-8")


def test_reconciliation_profile_configurator_is_shell_syntax_valid() -> None:
    assert SCRIPT.exists()
    subprocess.run(["bash", "-n", str(SCRIPT)], check=True)


def test_reconciliation_profile_configurator_keeps_activation_separate() -> None:
    text = _text()
    assert 'PROFILE="${HERMES_RECONCILIATION_PROFILE:-reconciliation}"' in text
    assert 'hermes profile create "$PROFILE" --no-skills --no-alias' in text
    assert "gateway start" not in text
    assert "gateway.multiplex_profiles" not in text
    assert "profile configured; no gateway was started and no routing was changed" in text


def test_reconciliation_profile_configurator_enforces_no_tool_boundary() -> None:
    text = _text()
    assert "config set platform_toolsets.api_server '[\"no_mcp\"]'" in text
    assert "config set --force plugins.enabled '[]'" in text
    assert "config set --force mcp_servers '{}'" in text
    assert "config set context.engine compressor" in text
    assert "config set tools.tool_search.enabled false" in text
    assert 'toolsets = get("/v1/toolsets")' in text
    assert 'row.get("enabled") is True' in text
    assert "reconciliation profile exposes enabled toolsets" in text


def test_reconciliation_profile_configurator_keeps_memory_packet_local() -> None:
    text = _text()
    assert 'config set memory.provider ""' in text
    assert "memories/MEMORY.md memories/USER.md MEMORY.md USER.md" in text
    assert "dedicated profile carries built-in memory content" in text
    assert '''[[ "$provider" == '""' || "$provider" == "null" ]]''' in text
    assert "external memory provider must be disabled" in text


def test_reconciliation_profile_configurator_requires_separate_secret_and_runtime_contract() -> None:
    text = _text()
    assert "HERMES_RECONCILIATION_API_KEY" in text
    assert "reconciliation API key must differ from the default Hermes API key" in text
    assert '--runtime-url requires HERMES_RECONCILIATION_API_KEY' in text
    assert 'features.get("responses_api") is not True' in text
    assert 'session_delete.get("method") != "DELETE"' in text
    assert '"/api/sessions/{session_id}"' in text
    assert "configured != activated; runtime observed != task authorized; reconciliation output != Evidence" in text
