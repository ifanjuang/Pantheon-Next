"""Regression tests for external-content provenance hardening."""

from __future__ import annotations

import importlib.util
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
    name = "pantheon_context_bridge_provenance_hardening_test_plugin"
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
def plugin(monkeypatch):
    module = _load_package()
    monkeypatch.setattr(
        module.context_admission,
        "_scan_with_hermes",
        lambda content: ("no_findings", []),
    )
    external = module.external_content
    external._TASK_ROOTS.clear()
    external._TASK_TAINT_ROOTS.clear()
    external._PENDING_FETCHES.clear()
    external._ROOT_CANONICAL_IDENTITIES.clear()
    return module


class _Context:
    def __init__(self):
        self.calls = []

    def dispatch_tool(self, name, args):
        self.calls.append((name, args))
        return "external data"


def _post(plugin, *, command: str, workdir: Path, task_id: str, ok: bool = True) -> None:
    plugin.external_content.post_tool_call(
        "terminal",
        {"command": command, "workdir": str(workdir)},
        {"exit_code": 0 if ok else 1, "error": None if ok else "failed"},
        task_id=task_id,
        status="ok" if ok else "error",
    )


def test_executed_compound_fetch_is_taint_only(plugin, tmp_path) -> None:
    workdir = tmp_path / "work"
    workdir.mkdir()
    task_id = "task-compound"
    command = "git clone https://example.test/x.git extrepo && true"

    plugin.external_content.pre_tool_call(
        "terminal", {"command": command, "workdir": str(workdir)}, task_id=task_id
    )
    root = workdir / "extrepo"
    assert str(root) in plugin.external_content._pending_roots_for_task(task_id)

    root.mkdir()
    (root / "README.md").write_text("external", encoding="utf-8")
    _post(plugin, command=command, workdir=workdir, task_id=task_id)

    assert str(root) not in plugin.external_content._TASK_ROOTS.get(task_id, set())
    assert str(root) in plugin.external_content._taint_roots_for_task(task_id)
    with pytest.raises(PermissionError):
        plugin.external_content.make_guarded_read_handler(_Context())(
            {"path": str(root / "README.md")}, task_id=task_id
        )


def test_comment_hidden_fetch_can_only_taint(plugin, tmp_path) -> None:
    workdir = tmp_path / "work"
    workdir.mkdir()
    secret = tmp_path / "secret"
    secret.mkdir()
    (secret / "private.txt").write_text("private", encoding="utf-8")
    task_id = "task-comment"
    command = (
        "ln -s ../secret extrepo # "
        "git clone https://example.test/x.git extrepo"
    )

    plugin.external_content.pre_tool_call(
        "terminal", {"command": command, "workdir": str(workdir)}, task_id=task_id
    )
    root = workdir / "extrepo"
    root.symlink_to(secret, target_is_directory=True)
    _post(plugin, command=command, workdir=workdir, task_id=task_id)

    assert str(root) not in plugin.external_content._TASK_ROOTS.get(task_id, set())
    assert str(root) in plugin.external_content._taint_roots_for_task(task_id)


def test_shell_refetch_revokes_use_of_previously_explicit_root(plugin, tmp_path) -> None:
    workdir = tmp_path / "work"
    workdir.mkdir()
    target = workdir / "out.txt"
    target.write_text("initial", encoding="utf-8")
    task_id = "task-refetch"
    plugin.external_content._remember_roots(task_id, [str(target)])

    read = plugin.external_content.make_guarded_read_handler(_Context())
    assert read({"path": str(target)}, task_id=task_id).startswith(
        "<untrusted_tool_result"
    )

    command = "curl https://example.test/out.txt -o out.txt"
    plugin.external_content.pre_tool_call(
        "terminal", {"command": command, "workdir": str(workdir)}, task_id=task_id
    )
    with pytest.raises(PermissionError):
        read({"path": str(target)}, task_id=task_id)

    target.write_text("shell-overwrite", encoding="utf-8")
    _post(plugin, command=command, workdir=workdir, task_id=task_id)
    assert str(target) in plugin.external_content._taint_roots_for_task(task_id)
    with pytest.raises(PermissionError):
        read({"path": str(target)}, task_id=task_id)

    # A later successful shell refetch still cannot clear taint or grant authority.
    plugin.external_content.pre_tool_call(
        "terminal", {"command": command, "workdir": str(workdir)}, task_id=task_id
    )
    target.write_text("another-shell-overwrite", encoding="utf-8")
    _post(plugin, command=command, workdir=workdir, task_id=task_id)
    assert str(target) in plugin.external_content._taint_roots_for_task(task_id)
    with pytest.raises(PermissionError):
        read({"path": str(target)}, task_id=task_id)


def test_explicit_root_identity_cannot_be_repointed(plugin, tmp_path) -> None:
    root = tmp_path / "extrepo"
    root.mkdir()
    (root / "README.md").write_text("external", encoding="utf-8")
    task_id = "task-root-identity"
    plugin.external_content._remember_roots(task_id, [str(root)])

    original = tmp_path / "original-extrepo"
    root.rename(original)
    secret = tmp_path / "secret"
    secret.mkdir()
    (secret / "private.txt").write_text("private", encoding="utf-8")
    root.symlink_to(secret, target_is_directory=True)

    with pytest.raises(PermissionError):
        plugin.external_content.make_guarded_read_handler(_Context())(
            {"path": str(root / "private.txt")}, task_id=task_id
        )


def test_quoted_attached_curl_output_tracks_exact_file_as_taint(plugin, tmp_path) -> None:
    workdir = tmp_path / "work"
    workdir.mkdir()
    task_id = "task-curl-quoted"
    command = 'curl https://example.test/payload.txt -o"external file.txt"'
    target = workdir / "external file.txt"

    plugin.external_content.pre_tool_call(
        "terminal", {"command": command, "workdir": str(workdir)}, task_id=task_id
    )
    assert plugin.external_content._pending_roots_for_task(task_id) == {str(target)}
    target.write_text("external", encoding="utf-8")
    _post(plugin, command=command, workdir=workdir, task_id=task_id)

    assert str(target) in plugin.external_content._taint_roots_for_task(task_id)
    assert str(target) not in plugin.external_content._TASK_ROOTS.get(task_id, set())
    with pytest.raises(PermissionError):
        plugin.external_content.make_guarded_read_handler(_Context())(
            {"path": str(target)}, task_id=task_id
        )


def test_pinned_root_identity_is_task_scoped(plugin, tmp_path) -> None:
    root = tmp_path / "shared"
    root.mkdir()
    (root / "a.txt").write_text("a", encoding="utf-8")
    task_a = "task-a"
    task_b = "task-b"
    plugin.external_content._remember_roots(task_a, [str(root)])

    original = tmp_path / "shared-original"
    root.rename(original)
    replacement = tmp_path / "replacement"
    replacement.mkdir()
    (replacement / "secret.txt").write_text("secret", encoding="utf-8")
    root.symlink_to(replacement, target_is_directory=True)
    plugin.external_content._remember_roots(task_b, [str(root)])

    with pytest.raises(PermissionError):
        plugin.external_content.make_guarded_read_handler(_Context())(
            {"path": str(root / "secret.txt")}, task_id=task_a
        )
