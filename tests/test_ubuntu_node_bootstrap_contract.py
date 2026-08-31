from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deployment" / "ubuntu"
INSTALL = DEPLOY / "install-node"
UPDATE = DEPLOY / "update-node"
RELEASE = DEPLOY / "release.env"
README = DEPLOY / "README.md"
EXTERNAL_PINS = ROOT / "implementation" / "qualification" / "external-pins.json"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _pin(pin_id: str) -> dict:
    data = json.loads(_text(EXTERNAL_PINS))
    return data["pins"][pin_id]


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


def test_install_service_users_can_traverse_managed_runtime_paths() -> None:
    text = _text(INSTALL)
    assert 'install -d -m 0711 "$APP_ROOT"' in text
    assert 'install -d -m 0711 "$AI_ROOT/models" "$AI_ROOT/cache"' in text
    assert 'install -d -m 0755 "$UV_PYTHON_INSTALL_DIR"' in text
    assert 'UV_PYTHON_INSTALL_DIR="$APP_ROOT/python"' in text
    assert "export UV_PYTHON_INSTALL_DIR" in text
    assert 'User=comfyui' in text
    assert 'Environment="OLLAMA_MODELS=$AI_ROOT/models/ollama"' in text


def test_install_apply_requires_reviewed_ubuntu_and_immutable_pantheon_commit() -> None:
    text = _text(INSTALL)
    assert '--apply is reviewed only for Ubuntu $TARGET_UBUNTU; detected $OS_VERSION' in text
    assert '[[ "$RESOLVED_PANTHEON_COMMIT" =~ ^[0-9a-f]{40}$ ]]' in text
    assert "PANTHEON_COMMIT must resolve to a full 40-character lowercase commit SHA" in text
    assert "--apply will refuse this host" in text


def test_release_lock_has_no_floating_latest_and_preserves_qualified_livesync_ref() -> None:
    text = _text(RELEASE)
    couchdb = _pin("couchdb")
    livesync = _pin("self-hosted-livesync")

    assert ":latest" not in text
    assert f"RELEASE_LIVESYNC_REF={livesync['ref']}" in text
    assert f"RELEASE_COUCHDB_IMAGE={couchdb['image']}:{couchdb['version']}" in text

    # The Hindsight image and the LiveSync CLI image were unguarded, and the
    # deployment target had already drifted ahead of its qualification: the
    # release lock carried a newer Hindsight image than the registry pinned. A
    # deployment target ahead of the qualification that is supposed to justify
    # it is the same class of gap in the other direction. Versions are read from
    # the registry here and never restated, so this guard cannot itself drift.
    #
    #     deployment target != qualified artifact
    hindsight = _pin("hindsight")
    livesync_cli = _pin("self-hosted-livesync-cli")
    assert f"RELEASE_HINDSIGHT_IMAGE={hindsight['image']}:{hindsight['version']}" in text
    assert f"livesync-cli:{livesync_cli['version']}" in text


def test_bootstrap_scripts_have_one_reviewed_target_owner() -> None:
    """Scripts must consume release.env, not carry a second pin set in fallbacks."""
    for script in (INSTALL, UPDATE):
        text = _text(script)
        assert 'RELEASE_LOCK="$SCRIPT_DIR/release.env"' in text
        assert 'source "$RELEASE_LOCK"' in text
        assert "reviewed deployment lock is missing" in text
        assert "RELEASE_COUCHDB_IMAGE:-" not in text
        assert "RELEASE_HINDSIGHT_IMAGE:-" not in text
        assert "RELEASE_LIVESYNC_REF:-" not in text
        assert "RELEASE_LIVESYNC_IMAGE:-" not in text


def test_bootstrap_scripts_fail_closed_when_release_lock_is_missing(tmp_path: Path) -> None:
    for source in (INSTALL, UPDATE):
        script = tmp_path / source.name
        shutil.copy2(source, script)
        result = subprocess.run(
            ["bash", str(script), "--doctor" if source == INSTALL else "--check"],
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode != 0
        assert "reviewed deployment lock is missing" in result.stderr


def test_updater_never_follows_main_or_silently_updates_stateful_services() -> None:
    text = _text(UPDATE)
    assert "git pull" not in text
    assert "PANTHEON_COMMIT_OVERRIDE" in text
    assert "STATEFUL_BACKUP_CONFIRMED" in text
    assert "available upstream != qualified for this node" in text
    assert "successful update != activation or task authorization" in text
    assert 'install -d -m 0700 "$checkpoint"' in text
    assert "umask 077" in text


def test_operator_readme_preserves_authority_and_storage_boundaries() -> None:
    text = _text(README)
    assert "A NAS is not required in the active execution path" in text
    assert "filesystem mirror != governed identity" in text
    assert "installed != activated" in text
    assert "Syncthing" in text and "optional" in text
    assert "Comfy MCP" in text
