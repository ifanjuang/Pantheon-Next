from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
OBSERVER = ROOT / "deployment" / "ubuntu" / "observe-hermes-runtime"


def _text() -> str:
    return OBSERVER.read_text(encoding="utf-8")


def test_runtime_observer_is_shell_syntax_valid() -> None:
    assert OBSERVER.exists()
    subprocess.run(["bash", "-n", str(OBSERVER)], check=True)


def test_runtime_observer_reads_actual_container_and_image_identity() -> None:
    text = _text()

    assert 'CONTAINER_NAME="${HERMES_CONTAINER_NAME:-pantheon-hermes}"' in text
    assert 'docker inspect "$CONTAINER_NAME"' in text
    assert 'docker image inspect "$image_id"' in text
    assert '.[0].Config.Image' in text
    assert '.[0].Image' in text
    assert '.[0].RepoDigests' in text
    assert 'org.opencontainers.image.version' in text
    assert 'org.opencontainers.image.revision' in text
    assert 'release_target_image' in text
    assert 'recorded_image' in text
    assert 'hermes --version' in text


def test_runtime_observer_targets_post_1057_profile_surface() -> None:
    text = _text()

    assert 'PROFILE_ROOT="$STATE_ROOT/hermes/profiles/$PROFILE"' in text
    assert 'CONTAINER_PROFILE_ROOT="/opt/data/profiles/$PROFILE"' in text
    assert '.Destination == "/opt/data"' in text
    assert 'profile_data_mount_observed' in text
    assert 'profile_host_observation="not_observable"' in text
    assert 'profile_root_present=null' in text
    assert 'host_observation:$profile_host_observation' in text
    assert 'docker exec "$CONTAINER_NAME" test -d "$CONTAINER_PROFILE_ROOT"' in text
    assert 'config_digest' in text
    assert 'soul_digest' in text
    assert 'profile_snapshot_digest' in text
    assert 'no_bundled_skills_marker' in text
    assert 'local_skills:$profile_skills' in text
    assert 'skill_md_digest' in text

    # The pre-#1057 external skill projection path is no longer the owner of
    # the effective governed profile surface.
    assert "/opt/pantheon-skills" not in text
    assert "hermes-governed-skills" not in text
    assert "RELEASE_HERMES_GOVERNED_SKILLS" not in text
    assert "skills.external_dirs" not in text


def test_runtime_observer_remains_observation_only() -> None:
    text = _text()

    forbidden = (
        "docker start",
        "docker restart",
        "docker stop",
        "docker compose up",
        "docker compose pull",
        "config set",
        "profile create",
        "plugin install",
        "skill install",
        "/v1/runs",
    )
    for token in forbidden:
        assert token not in text

    assert 'write_effect:false' in text
    assert 'activation_changed:false' in text
    assert 'authority_effect:"none"' in text
    assert 'technical_receipt_is_evidence:false' in text
    assert '"profile snapshot != profile route active for a run"' in text
    assert '"profile-local skill != skill used"' in text
    assert '"runtime observation != Evidence"' in text


def test_runtime_observer_does_not_dump_secrets_or_arbitrary_image_labels() -> None:
    text = _text()

    assert "docker inspect -f '{{json .Config.Env}}'" not in text
    assert "env |" not in text
    assert "printenv" not in text
    assert ".Config.Env" not in text
    assert "secrets.env" not in text
    assert "image_labels:$image_labels" not in text
    assert "identity_labels:$identity_labels" in text
    assert 'org.opencontainers.image.source' in text
    assert 'org.opencontainers.image.title' in text


def test_runtime_observer_builds_bounded_receipt_from_observed_profile(tmp_path: Path) -> None:
    """Drive the observer against a fake docker and check what it surfaces.

    The fake container deliberately reports `0.0.0-fixture` rather than the
    registry's current `hermes-agent` version. Two reasons: the observer must
    report what it *observed*, so a fixture equal to the configured pin would
    let the assertion pass for the wrong reason; and restating a canonical pin
    literal in an active qualification source is what
    `implementation/tests/test_external_qualification_pins.py` exists to refuse.
    """
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    fake_docker = fake_bin / "docker"
    fake_docker.write_text(
        """#!/usr/bin/env bash
set -eu
if [[ "$1" == "inspect" ]]; then
  cat <<JSON
[{"State":{"Running":true,"StartedAt":"2026-09-14T06:00:00Z"},"Id":"container-123","Config":{"Image":"nousresearch/hermes-agent:v2026.9.14"},"Image":"sha256:image-456","Mounts":[{"Source":"$STATE_ROOT/hermes","Destination":"/opt/data","RW":true}]}]
JSON
elif [[ "$1" == "image" && "$2" == "inspect" ]]; then
  cat <<'JSON'
[{"RepoDigests":["nousresearch/hermes-agent@sha256:repo-789"],"Created":"2026-09-11T00:00:00Z","Config":{"Labels":{"org.opencontainers.image.version":"0.0.0-fixture","org.opencontainers.image.revision":"rev-abc","org.opencontainers.image.source":"https://github.com/NousResearch/hermes-agent","org.opencontainers.image.title":"Hermes Agent","secret.label":"must-not-surface"}}}]
JSON
elif [[ "$1" == "exec" && "$3" == "test" && "$4" == "-d" ]]; then
  exit 0
elif [[ "$1" == "exec" && "$3" == "hermes" && "$4" == "--version" ]]; then
  printf 'Hermes Agent 0.0.0-fixture\n'
else
  printf 'unexpected fake docker call: %s\n' "$*" >&2
  exit 64
fi
""",
        encoding="utf-8",
    )
    fake_docker.chmod(0o755)

    config_root = tmp_path / "etc-pantheon"
    config_root.mkdir()
    (config_root / "versions.env").write_text(
        "HERMES_IMAGE=nousresearch/hermes-agent:v2026.9.14\n", encoding="utf-8"
    )

    state_root = tmp_path / "state"
    profile = state_root / "hermes" / "profiles" / "pantheon-governed"
    skill = profile / "skills" / "pantheon-governed-method"
    skill.mkdir(parents=True)
    (profile / "config.yaml").write_text("tools:\n  tool_search:\n    enabled: auto\n", encoding="utf-8")
    (profile / "SOUL.md").write_text("governed profile\n", encoding="utf-8")
    (skill / "SKILL.md").write_text("# governed method\n", encoding="utf-8")
    (profile / "skills" / ".no-bundled-skills").touch()

    env = os.environ.copy()
    env.update(
        {
            "PATH": f"{fake_bin}:{env['PATH']}",
            "CONFIG_ROOT": str(config_root),
            "STATE_ROOT": str(state_root),
        }
    )
    completed = subprocess.run(
        [str(OBSERVER)],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=True,
    )
    receipt = json.loads(completed.stdout)

    assert receipt["container"]["running"] is True
    assert receipt["container"]["configured_image"] == "nousresearch/hermes-agent:v2026.9.14"
    assert receipt["container"]["image_id"] == "sha256:image-456"
    assert receipt["container"]["repo_digests"] == ["nousresearch/hermes-agent@sha256:repo-789"]
    assert receipt["container"]["identity_labels"]["version"] == "0.0.0-fixture"
    assert "secret.label" not in receipt["container"]["identity_labels"]
    assert receipt["container"]["profile_data_mount_observed"] is True
    assert receipt["deployment"]["target_matches_container_config"] is True
    assert receipt["deployment"]["recorded_matches_container_config"] is True
    assert receipt["profile"]["host_root_present"] is True
    assert receipt["profile"]["host_observation"] == "observed_present"
    assert receipt["profile"]["visible_in_container"] is True
    assert receipt["profile"]["snapshot_digest"].startswith("sha256:")
    assert receipt["profile"]["no_bundled_skills_marker"] is True
    assert [item["name"] for item in receipt["profile"]["local_skills"]] == [
        "pantheon-governed-method"
    ]
    assert receipt["runtime_version"] == {"status": "observed", "value": "Hermes Agent 0.0.0-fixture"}
    assert receipt["write_effect"] is False
    assert receipt["activation_changed"] is False
    assert receipt["authority_effect"] == "none"
    assert receipt["technical_receipt_is_evidence"] is False