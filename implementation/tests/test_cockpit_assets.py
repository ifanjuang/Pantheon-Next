"""Static asset checks for the cards-first cockpit candidate."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    ROOT / "mvp_vertical" / "cockpit" / "app.js",
    ROOT / "mvp_vertical" / "cockpit" / "resources.js",
    ROOT / "mvp_vertical" / "cockpit" / "effects.js",
    ROOT / "mvp_vertical" / "cockpit" / "knowledge_updates.js",
    ROOT / "mvp_vertical" / "cockpit" / "demo.js",
    ROOT / "mvp_vertical" / "mobile_editor" / "app.js",
    ROOT / "mvp_vertical" / "mobile_editor" / "sw.js",
]


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda path: str(path.relative_to(ROOT)))
def test_cockpit_javascript_parses(script: Path) -> None:
    node = shutil.which("node")
    if node is None:  # pragma: no cover - depends on the runner image
        pytest.skip("Node.js is unavailable; JavaScript syntax check skipped")

    result = subprocess.run(
        [node, "--check", str(script)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_static_demo_reuses_cockpit_assets_and_blocks_network() -> None:
    html = (ROOT / "mvp_vertical" / "cockpit" / "demo.html").read_text(
        encoding="utf-8"
    )
    javascript = (ROOT / "mvp_vertical" / "cockpit" / "demo.js").read_text(
        encoding="utf-8"
    )

    assert 'href="styles/index.css"' in html
    for script in (
        "app.js",
        "resources.js",
        "effects.js",
        "knowledge_updates.js",
        "demo.js",
    ):
        assert f'src="{script}"' in html

    assert "window.PANTHEON_COCKPIT_DEMO = true" in html
    assert "window.fetch = async" in html
    assert "accès réseau désactivé" in html
    assert "données fictives" in html
    assert "state.documents = [" in javascript
    assert "state.knowledge = [" in javascript
    assert "state.workIssues = [" in javascript
    assert "state.resourceProfiles = {" in javascript
    assert "fetch(" not in javascript


def test_mobile_editor_exposes_and_clears_device_local_data() -> None:
    html = (ROOT / "mvp_vertical" / "mobile_editor" / "index.html").read_text(
        encoding="utf-8"
    )
    javascript = (ROOT / "mvp_vertical" / "mobile_editor" / "app.js").read_text(
        encoding="utf-8"
    )

    assert 'id="clear-local"' in html
    assert "sans chiffrement applicatif" in html
    assert '"pantheon-knowledge:"' in javascript
    assert '"pantheon-project:"' in javascript
    assert "localStorage.removeItem" in javascript
    assert 'sessionStorage.removeItem("pantheon-human-actor")' in javascript
    assert '$("clear-local").onclick = clearLocalData' in javascript


def test_mobile_editor_recovers_legacy_offline_revisions_before_queue_cleanup() -> None:
    javascript = (ROOT / "mvp_vertical" / "mobile_editor" / "app.js").read_text(
        encoding="utf-8"
    )

    assert "function legacyDraftKey" in javascript
    assert "function migrateLegacyRevisions" in javascript
    assert "operation?.type !== \"revision\"" in javascript
    assert "localStorage.setItem(" in javascript
    assert "legacyDraftKey(knowledgeId)" in javascript
    assert "recovered?.markdown ?? remoteMarkdown" in javascript
    assert "localStorage.removeItem(legacyDraftKey(updated.knowledge_id))" in javascript
    assert "ancienne(s) révision(s) récupérée(s) comme brouillon local" in javascript
    assert "retiredRevisions" not in javascript


def test_cockpit_update_retries_reuse_idempotency_and_refresh_all_projections() -> None:
    javascript = (
        ROOT / "mvp_vertical" / "cockpit" / "knowledge_updates.js"
    ).read_text(encoding="utf-8")

    assert "const updateIdempotencyKey = idempotencyKey();" in javascript
    assert "idempotency_key: updateIdempotencyKey" in javascript
    assert 'document.addEventListener("pantheon:knowledge-updated"' in javascript
    assert "load.click()" in javascript


def test_removed_site_list_registry_is_not_advertised_as_runtime_configuration() -> None:
    compose = (ROOT / "docker-compose.yml").read_text(encoding="utf-8")

    assert "MVP_SITE_LISTS_JSON" not in compose
    assert "/config" not in compose
    assert not (ROOT / "config" / "site_lists.json").exists()
    assert not (ROOT / "config" / "README.md").exists()
