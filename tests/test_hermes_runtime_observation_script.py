from __future__ import annotations

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
OBSERVER = ROOT / "deployment" / "ubuntu" / "observe-hermes-runtime"


def _text() -> str:
    return OBSERVER.read_text(encoding="utf-8")


def test_runtime_observer_is_shell_syntax_valid() -> None:
    assert OBSERVER.exists()
    subprocess.run(["bash", "-n", str(OBSERVER)], check=True)


def test_runtime_observer_reads_actual_container_identity_and_skill_projection() -> None:
    text = _text()

    assert 'docker inspect "$CONTAINER_NAME"' in text
    assert 'docker image inspect "$image_id"' in text
    assert '.[0].Config.Image' in text
    assert '.[0].Image' in text
    assert '.[0].RepoDigests' in text
    assert 'org.opencontainers.image.version' in text
    assert 'org.opencontainers.image.revision' in text
    assert 'config get skills.external_dirs --json' in text
    assert 'has("value")' in text
    assert 'hermes --version' in text
    assert 'read_only_exec_attempted' in text
    assert 'skill_md_digest' in text
    assert 'read_only_mount_observed' in text
    assert 'release_target_image' in text
    assert 'recorded_image' in text


def test_runtime_observer_compares_projected_skills_with_release_owner() -> None:
    text = _text()

    assert 'RELEASE_HERMES_GOVERNED_SKILLS' in text
    assert 'release_target:$target_skill_names' in text
    assert 'matches_release_target:$skills_match_target' in text
    assert 'missing_release_target:$missing_target_skills' in text
    assert 'unexpected_projected:$unexpected_projected_skills' in text
    assert '"skill set matches release target != skill used"' in text


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
    assert '"skill projected != skill used"' in text
    assert '"profile config present != profile route active"' in text
    assert '"runtime observation != Evidence"' in text


def test_runtime_observer_does_not_dump_environment_or_arbitrary_image_labels() -> None:
    text = _text()

    assert "docker inspect -f '{{json .Config.Env}}'" not in text
    assert "env |" not in text
    assert "printenv" not in text
    assert "image_labels:$image_labels" not in text
    assert "identity_labels:$identity_labels" in text
    assert 'org.opencontainers.image.source' in text
    assert 'org.opencontainers.image.title' in text
