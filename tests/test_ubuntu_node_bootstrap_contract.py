from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deployment" / "ubuntu"
INSTALL = DEPLOY / "install-node"
UPDATE = DEPLOY / "update-node"
SKILL_SYNC = DEPLOY / "sync-hermes-governed-skills"
RELEASE = DEPLOY / "release.env"
README = DEPLOY / "README.md"
HERMES_LOCAL_COMPOSE = DEPLOY / "compose.hermes-local.yaml"
WORKSPACE_COCKPIT_COMPOSE = DEPLOY / "compose.workspace-cockpit-local.yaml"
WORKSPACE_COCKPIT_TAILSCALE = DEPLOY / "compose.workspace-cockpit-tailscale.yaml"
CONFIGURE_DOCLING = DEPLOY / "configure-docling-local"
CONFIGURE_WORKSPACE_COCKPIT = DEPLOY / "configure-workspace-cockpit-local"
CONFIGURE_AFFAIRES_NAS_MOUNT = DEPLOY / "configure-affaires-nas-mount"
CONFIGURE_HERMES_ACTIVITY = DEPLOY / "configure-hermes-activity-projection"
EXTERNAL_PINS = ROOT / "implementation" / "qualification" / "external-pins.json"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _pin(pin_id: str) -> dict:
    data = json.loads(_text(EXTERNAL_PINS))
    return data["pins"][pin_id]


def test_bootstrap_scripts_are_shell_syntax_valid() -> None:
    scripts = (
        INSTALL,
        UPDATE,
        SKILL_SYNC,
        CONFIGURE_DOCLING,
        CONFIGURE_WORKSPACE_COCKPIT,
        CONFIGURE_AFFAIRES_NAS_MOUNT,
        CONFIGURE_HERMES_ACTIVITY,
    )
    for script in scripts:
        assert script.exists()
        subprocess.run(["bash", "-n", str(script)], check=True)


def test_affaires_mount_configuration_is_generic_and_keeps_secrets_external() -> None:
    text = _text(CONFIGURE_AFFAIRES_NAS_MOUNT)
    assert "--source //HOST/SHARE" in text
    assert "--prefix-path RELATIVE/PATH" in text
    assert "credentials file must be owned by root with mode 0600" in text
    assert "Options=credentials=%s" in text
    assert "Type=cifs" in text
    assert "prefixpath=%s" in text
    assert "nosuid,nodev,noexec" in text
    assert "No hostname, share, project name or folder name is built into this script" in text


def test_workspace_cockpit_compose_is_read_only_and_loopback_only() -> None:
    text = _text(WORKSPACE_COCKPIT_COMPOSE)
    assert 'WORKSPACE_COCKPIT_BIND:-127.0.0.1' in text
    assert "read_only: true" in text
    assert "no-new-privileges:true" in text
    assert "cap_drop:" in text and "- ALL" in text
    assert "group_add:" in text
    assert "${AFFAIRES_GID:?set AFFAIRES_GID to the Linux-mounted NAS AFFAIRES group id}" in text
    affaires_mount = "${AFFAIRES_ROOT:?set AFFAIRES_ROOT to the Linux-mounted NAS AFFAIRES path}:/workspace/affaires:ro"
    assert text.count(affaires_mount) == 2
    assert "workspace-producer:" in text
    assert 'entrypoint: ["/opt/hermes/.venv/bin/python", "/app/producer_daemon.py"]' in text
    assert "--projection-only" in text
    assert "workspace-cockpit-state:/state:ro" in text
    assert "/srv/pantheon/obsidian" not in text
    assert '127.0.0.1:${ROLE_TRACE_ATTACH_PORT:-8190}:8190' in text
    assert "HERMES_ROLE_TRACE_API_KEY" in text
    assert "ROLE_TRACE_ATTACH_KEY" in text
    assert "ROLE_TRACE_READ_KEY" in text
    assert "WORKSPACE_HINDSIGHT_URL" in text
    assert "WORKSPACE_HINDSIGHT_BANK_ID" in text
    assert "WORKSPACE_HINDSIGHT_MAX_FILE_MB" in text
    assert "WORKSPACE_HINDSIGHT_SETTLE_OBSERVATIONS" in text
    assert "WORKSPACE_HINDSIGHT_SOURCE_KIND" in text
    assert "WORKSPACE_EXCLUDED_FOLDERS" in text
    assert "network_mode: host" in text
    assert "Kroqi=/workspace/affaires" in text
    assert 'WORKSPACE_RECONCILE_SECONDS:-3600' in text
    assert 'WORKSPACE_HINDSIGHT_BANK_ID:-IFJA_KROQI' in text
    assert 'WORKSPACE_HINDSIGHT_SETTLE_OBSERVATIONS:-2' in text
    assert 'WORKSPACE_HINDSIGHT_SOURCE_KIND:-kroqi-sync' in text


def test_workspace_cockpit_systemd_installer_keeps_cockpit_optional() -> None:
    text = _text(CONFIGURE_WORKSPACE_COCKPIT)
    assert "--enable-producer" in text
    assert "--enable-cockpit" in text
    assert "Requires=pantheon-affaires-producer.service" in text
    assert "systemctl enable --now pantheon-affaires-producer.service" in text
    assert "systemctl enable --now pantheon-workspace-cockpit.service" in text
    assert "if ((ENABLE_PRODUCER)); then" in text
    assert "if ((ENABLE_COCKPIT)); then" in text


def test_hindsight_file_retain_runtime_posture_is_explicit() -> None:
    text = _text(HERMES_LOCAL_COMPOSE)
    assert "HINDSIGHT_API_FILE_PARSER: markitdown" in text
    assert "HINDSIGHT_API_RETAIN_MISSION:" in text
    assert "revision/index/version token" in text
    assert "revision-history or revision-table entries" in text
    assert "Never infer document chronology" in text
    assert "preserve an unresolved reference instead of guessing" in text
    assert 'HINDSIGHT_API_FILE_DELETE_AFTER_RETAIN: "true"' in text
    assert 'HINDSIGHT_API_FILE_PARSER_MARKITDOWN_OCR_ENABLED: "false"' in text
    assert 'HINDSIGHT_API_STORE_DOCUMENT_TEXT: "true"' in text
    assert "shm_size: 1gb" in text


def test_workspace_cockpit_remote_access_uses_pinned_userspace_tailscale() -> None:
    release = _text(RELEASE)
    compose = _text(WORKSPACE_COCKPIT_TAILSCALE)
    assert "RELEASE_TAILSCALE_IMAGE=tailscale/tailscale:v" in release
    assert "${RELEASE_TAILSCALE_IMAGE:" in compose
    assert 'TS_USERSPACE: "true"' in compose
    assert "/dev/net/tun" not in compose
    assert "network_mode: host" not in compose
    assert "TS_AUTHKEY" not in compose
    assert "pantheon-cockpit-tailscale-state" in compose


def test_install_defaults_fail_private_and_keep_optional_services_inactive() -> None:
    text = _text(INSTALL)
    assert 'NODE_BIND_ADDRESS="127.0.0.1"' in text
    assert 'COMFYUI_BIND_ADDRESS="127.0.0.1"' in text
    assert "ENABLE_HINDSIGHT=0" in text
    assert "livesync" not in text.lower()
    assert "couchdb" not in text.lower()
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


def test_release_lock_has_no_floating_latest_and_tracks_active_runtime_pins() -> None:
    text = _text(RELEASE)

    assert ":latest" not in text
    assert "RELEASE_LIVESYNC" not in text
    assert "RELEASE_COUCHDB" not in text

    hindsight = _pin("hindsight")
    assert f"RELEASE_HINDSIGHT_IMAGE={hindsight['image']}:{hindsight['version']}" in text

def test_release_lock_curates_governed_hermes_skills_without_exposing_all_templates() -> None:
    text = _text(RELEASE)
    line = next(
        line for line in text.splitlines()
        if line.startswith("RELEASE_HERMES_GOVERNED_SKILLS=")
    )
    for name in (
        "ifja-project-context",
        "pantheon-activity-projection",
        "pantheon-request-intake",
        "source-research",
    ):
        assert name in line
    assert "templates/hermes/skills" not in line


def test_bootstrap_scripts_have_one_reviewed_target_owner() -> None:
    """Scripts must consume release.env, not carry a second pin set in fallbacks."""
    for script in (INSTALL, UPDATE):
        text = _text(script)
        assert 'RELEASE_LOCK="$SCRIPT_DIR/release.env"' in text
        assert 'source "$RELEASE_LOCK"' in text
        assert "reviewed deployment lock is missing" in text
        assert "RELEASE_HINDSIGHT_IMAGE:-" not in text
        assert "RELEASE_LIVESYNC" not in text
        assert "RELEASE_COUCHDB" not in text


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


def test_governed_skill_sync_uses_target_checkout_and_read_only_external_dir() -> None:
    text = _text(SKILL_SYNC)
    assert 'RELEASE_LOCK="$CHECKOUT/deployment/ubuntu/release.env"' in text
    assert 'RELEASE_HERMES_GOVERNED_SKILLS' in text
    assert 'HOST_SKILLS_ROOT="$STATE_ROOT/hermes-governed-skills"' in text
    assert 'CONTAINER_SKILLS_ROOT="/opt/pantheon-skills"' in text
    assert '/srv/pantheon/hermes-governed-skills:/opt/pantheon-skills:ro' in text
    assert 'config get skills.external_dirs --json' in text
    assert 'config set skills.external_dirs "$merged"' in text
    assert 'find "$src" -type l' in text
    assert 'find "$stage" -type d -exec chmod 0555' in text
    assert 'find "$stage" -type f -exec chmod 0444' in text
    assert "hermes profile create" not in text
    assert "available skill != skill used" in text
    assert "projection != persistence" in text


def test_install_and_pantheon_update_sync_governed_skills_without_creating_profile() -> None:
    install = _text(INSTALL)
    update = _text(UPDATE)
    call = 'bash "$SCRIPT_DIR/sync-hermes-governed-skills"'
    assert call in install
    assert call in update
    assert "hermes profile create" not in install
    assert "hermes profile create" not in update


def test_updater_checkpoints_governed_skill_projection_before_mutation() -> None:
    text = _text(UPDATE)
    assert '$STATE_ROOT/hermes/profiles/pantheon-governed/config.yaml' in text
    assert '$checkpoint/hermes-pantheon-governed/config.yaml' in text
    assert '$STATE_ROOT/hermes-governed-skills' in text
    assert '$checkpoint/hermes-governed-skills' in text


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
    assert "Hermes execution itself does not make a NAS an authority dependency." in text
    assert "The selected professional Workspace path uses the reviewed NAS `/AFFAIRES` tree as its source filesystem" in text
    assert "filesystem mirror != governed identity" in text
    assert "installed != activated" in text
    assert "Syncthing" in text and "optional" in text
    assert "Comfy MCP" in text
