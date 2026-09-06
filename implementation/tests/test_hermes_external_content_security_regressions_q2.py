"""Security regressions for the external-content provenance state machine."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

import pytest

PLUGIN_DIR = (
    Path(__file__).resolve().parents[1]
    / "hermes"
    / "plugins"
    / "pantheon-context-bridge"
)


def _load_package():
    name = "pantheon_context_bridge_q2_security"
    spec = importlib.util.spec_from_file_location(
        name,
        PLUGIN_DIR / "__init__.py",
        submodule_search_locations=[str(PLUGIN_DIR)],
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def external():
    module = _load_package().external_content
    module._TASK_ROOTS.clear()
    module._TASK_TAINT_ROOTS.clear()
    module._PENDING_FETCHES.clear()
    module._ROOT_CANONICAL_IDENTITIES.clear()
    yield module
    module._TASK_ROOTS.clear()
    module._TASK_TAINT_ROOTS.clear()
    module._PENDING_FETCHES.clear()
    module._ROOT_CANONICAL_IDENTITIES.clear()


def _complete_terminal(external, task_id: str, command: str, cwd: Path) -> None:
    external.post_tool_call(
        "terminal",
        {"command": command, "workdir": str(cwd)},
        {"exit_code": 0},
        task_id=task_id,
        status="ok",
    )


def test_curl_token_passed_to_another_program_is_taint_only(external, tmp_path) -> None:
    task_id = "q2-noncommand-curl"
    target = tmp_path / "credential"
    command = (
        "python -c 'print(1)' curl https://example.test/a "
        f"-o {target}"
    )

    assert external.pre_tool_call(
        "terminal",
        {"command": command, "workdir": str(tmp_path)},
        task_id=task_id,
    ) is None
    assert str(target) in external._pending_roots_for_task(task_id)

    target.write_text("local-secret", encoding="utf-8")
    _complete_terminal(external, task_id, command, tmp_path)

    assert str(target) not in external._TASK_ROOTS.get(task_id, set())
    assert str(target) in external._taint_roots_for_task(task_id)
    with pytest.raises(PermissionError):
        external._require_guarded_path("pantheon_untrusted_read", str(target), task_id)


def test_command_substitution_fetch_can_never_promote(external, tmp_path) -> None:
    task_id = "q2-command-substitution"
    target = tmp_path / "out"
    command = f"echo $( curl https://example.test/a -o {target} )"

    assert external.pre_tool_call(
        "terminal",
        {"command": command, "workdir": str(tmp_path)},
        task_id=task_id,
    ) is None
    target.write_text("partial-or-external", encoding="utf-8")
    _complete_terminal(external, task_id, command, tmp_path)

    assert str(target) not in external._TASK_ROOTS.get(task_id, set())
    assert str(target) in external._taint_roots_for_task(task_id)


def test_symlinked_intrinsic_document_cache_is_not_guarded_read_authority(
    external, tmp_path, monkeypatch
) -> None:
    if not hasattr(os, "symlink"):
        pytest.skip("symlink unavailable")

    outside = tmp_path / "outside"
    outside.mkdir()
    secret = outside / "secret.txt"
    secret.write_text("secret", encoding="utf-8")
    cache = tmp_path / "documents"
    cache.symlink_to(outside, target_is_directory=True)
    monkeypatch.setenv("HERMES_DOCUMENT_CACHE_DIR", str(cache))

    candidate = cache / "secret.txt"
    assert external._path_under_any_root(
        str(candidate), external._blocking_roots_for_task("q2-intrinsic")
    )
    assert not external._path_safely_under_eligible_root(
        str(candidate), "q2-intrinsic"
    )
    with pytest.raises(PermissionError):
        external._require_guarded_path(
            "pantheon_untrusted_read", str(candidate), "q2-intrinsic"
        )


def test_curl_tracks_every_explicit_output_destination(external, tmp_path) -> None:
    task_id = "q2-multi-output"
    first = tmp_path / "first file"
    second = tmp_path / "second file"
    command = (
        'curl https://example.test/a -o "first file" '
        'https://example.test/b -o "second file"'
    )

    roots = external._extract_fetch_roots(command, str(tmp_path))
    assert roots == [str(first), str(second)]

    external.pre_tool_call(
        "terminal",
        {"command": command, "workdir": str(tmp_path)},
        task_id=task_id,
    )
    assert external._pending_roots_for_task(task_id) == {str(first), str(second)}

    first.write_text("a", encoding="utf-8")
    second.write_text("b", encoding="utf-8")
    _complete_terminal(external, task_id, command, tmp_path)

    assert {str(first), str(second)}.issubset(external._TASK_ROOTS[task_id])


def test_terminal_reader_preserves_quoted_path_with_spaces(external, tmp_path) -> None:
    task_id = "q2-reader-quoting"
    protected = tmp_path / "external file.txt"
    protected.write_text("external", encoding="utf-8")
    external._remember_roots(task_id, [str(protected)])

    blocked = external.pre_tool_call(
        "terminal",
        {
            "command": 'cat "external file.txt"',
            "workdir": str(tmp_path),
        },
        task_id=task_id,
    )
    assert blocked is not None
    assert blocked["action"] == "block"


def test_quoted_attached_curl_output_remains_exact(external, tmp_path) -> None:
    roots = external._extract_fetch_roots(
        'curl https://example.test/a -o"external file.txt"',
        str(tmp_path),
    )
    assert roots == [str(tmp_path / "external file.txt")]
