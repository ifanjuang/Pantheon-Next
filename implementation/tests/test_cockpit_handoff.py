"""Static boundary checks for the Cockpit Hermes handoff dock."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
COCKPIT = ROOT / "mvp_vertical" / "cockpit"
HANDOFF = COCKPIT / "handoff" / "handoff_lifecycle.js"
HANDOFF_SEND = COCKPIT / "handoff" / "handoff_send.js"


def test_handoff_javascript_parses() -> None:
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is unavailable; JavaScript syntax check skipped")
    result = subprocess.run([node, "--check", str(HANDOFF)], check=False, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_handoff_separates_conversation_governance_and_runtime() -> None:
    html = (COCKPIT / "index.html").read_text(encoding="utf-8")
    bootstrap = (COCKPIT / "live_bootstrap.js").read_text(encoding="utf-8")
    javascript = HANDOFF.read_text(encoding="utf-8")
    send_javascript = HANDOFF_SEND.read_text(encoding="utf-8")
    css = (COCKPIT / "styles" / "editors.css").read_text(encoding="utf-8")

    for control in ('id="v2-handoff-question"', 'id="v2-handoff-actor"', 'id="v2-handoff-ttl"', 'id="v2-handoff-revoke-reason"', 'id="v2-handoff-descendants"', 'id="v2-handoff-send"', 'id="v2-handoff-prepare"', 'id="v2-handoff-submit"', 'id="v2-handoff-admit"', 'id="v2-handoff-revoke"'):
        assert control in html

    assert '"handoff/handoff_lifecycle.js"' in bootstrap
    assert '"handoff/handoff_send.js"' in bootstrap
    assert '"v2_' + 'handoff.js"' not in bootstrap
    assert '"v2_' + 'hermes_send.js"' not in bootstrap
    assert 'src="cockpit_bootstrap.js"' in html
    assert 'href="styles/editors.css"' in html
    assert '../v1/cockpit/hermes-handoffs/preview' in javascript
    assert '../v1/cockpit/hermes-handoffs/submit' in javascript
    assert '/admissions`' in javascript
    assert '/revocations`' in javascript
    assert 'scope_widened_implicitly: false' in javascript
    assert 'selected_context: selectedContext.map' in javascript
    assert '/runs/start' not in javascript
    assert '/v1/hermes/execution-admissions' not in javascript
    assert 'v2-handoff-send' in send_javascript
    assert 'v2-handoff-prepare' in send_javascript
    assert '.v2-handoff-shell' in css
    assert '.v2-handoff-question' in css
