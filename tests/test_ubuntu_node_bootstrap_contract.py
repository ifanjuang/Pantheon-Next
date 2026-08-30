from __future__ import annotations

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deployment" / "ubuntu"
INSTALL = DEPLOY / "install-node"
UPDATE = DEPLOY / "update-node"
RELEASE = DEPLOY / "release.env"
README = DEPLOY / "README.md"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_bootstrap_scripts_are_shell_syntax_valid() -> None:
    for script in (INSTALL, UPDATE):
        assert script.exists()
        subprocess.run(["bash", "-n", str(script)], check=True)


def test_install_defaults_fail_private_and_keep_optional_services_inactive() -> None:
    text = _text(INSTALL)
    assert 'NODE_BIND_ADDRESS="127.0.0.1"' in text
    assert 'COMFYUI_BIND_ADDRESS="127.0.0.1"' in text
    assert "ENABLE_HINDSIGHT=0" in text
    assert "systemctl disable livesync-headless.service" in text
    assert "ConditionPathExists=$STATE_ROOT/livesync/db/settings.json" in text
    assert "daemon --interval 30" in text
    assert "installed != activated" in text
    assert "activated != task-authorized" in text


def test_release_lock_has_no_floating_latest_and_preserves_qualified_livesync_ref() -> None:
    text = _text(RELEASE)
    assert ":latest" not in text
    assert "RELEASE_LIVESYNC_REF=32e827692f1a552cd581de9da45cecd0711573d3" in text
    assert "RELEASE_COUCHDB_IMAGE=couchdb:3.5.0" in text


def test_updater_never_follows_main_or_silently_updates_stateful_services() -> None:
    text = _text(UPDATE)
    assert "git pull" not in text
    assert "PANTHEON_COMMIT_OVERRIDE" in text
    assert "STATEFUL_BACKUP_CONFIRMED" in text
    assert "available upstream != qualified for this node" in text
    assert "successful update != activation or task authorization" in text


def test_operator_readme_preserves_authority_and_storage_boundaries() -> None:
    text = _text(README)
    assert "A NAS is not required in the active execution path" in text
    assert "filesystem mirror != governed identity" in text
    assert "installed != activated" in text
    assert "Syncthing" in text and "optional" in text
    assert "Comfy MCP" in text
