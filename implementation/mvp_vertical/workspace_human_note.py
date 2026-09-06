"""Bounded human-authored note editing for one exact Workspace source.

This module owns only one low-consequence fragment inside an adjacent
``document.yaml``. It does not adopt a full document manifest schema, infer a
Document identity, qualify the source, write Evidence, or authorize Hermes.

The managed fragment is delimited so unrelated YAML bytes/comments can remain
untouched instead of round-tripping an unknown future manifest through PyYAML.
"""

from __future__ import annotations

import errno
import hashlib
import os
import re
import stat as stat_module
import uuid
from pathlib import Path, PurePosixPath
from typing import Mapping

import yaml

from . import workspace_collection_read


class WorkspaceHumanNoteError(ValueError):
    """The human-note operation cannot be performed without widening ownership."""


class WorkspaceHumanNoteConflict(WorkspaceHumanNoteError):
    """The caller's manifest basis or source binding is stale/conflicting."""


_START_MARKER = "# >>> Pantheon workspace note"
_END_MARKER = "# <<< Pantheon workspace note"
_START_RE = re.compile(r"(?m)^# >>> Pantheon workspace note\r?\n")
_END_RE = re.compile(r"(?m)^# <<< Pantheon workspace note(?:\r?\n|$)")
_NAMESPACE = "pantheon_workspace"
_SIDECAR_NAME = "document.yaml"


def _sidecar_relative_path(source_relative_path: str) -> str:
    parent = PurePosixPath(source_relative_path).parent
    value = PurePosixPath(parent, _SIDECAR_NAME).as_posix()
    return _SIDECAR_NAME if value == f"./{_SIDECAR_NAME}" else value


def _secure_open_directory(root: Path, relative_path: str) -> int:
    """Open one existing workspace directory using openat/no-follow traversal."""
    if not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY"):
        raise WorkspaceHumanNoteError(
            "workspace note editing requires O_NOFOLLOW and O_DIRECTORY support"
        )
    normalized = workspace_collection_read.normalize_relative_path(relative_path)
    parts = PurePosixPath(normalized).parts if normalized else ()
    for part in parts:
        if part == "_VAULT.md" or part.startswith("."):
            raise WorkspaceHumanNoteError("hidden workspace paths are not writable")

    opened: list[int] = []
    try:
        current = os.open(root, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        opened.append(current)
        for part in parts:
            current = os.open(
                part,
                os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                dir_fd=current,
            )
            opened.append(current)
        result = opened.pop()
        for descriptor in reversed(opened):
            os.close(descriptor)
        return result
    except FileNotFoundError as exc:
        raise WorkspaceHumanNoteError("workspace note parent directory does not exist") from exc
    except OSError as exc:
        raise WorkspaceHumanNoteError(
            "workspace note parent cannot be opened without following links"
        ) from exc
    finally:
        for descriptor in reversed(opened):
            try:
                os.close(descriptor)
            except OSError:
                pass


def _read_sidecar_bytes(parent_fd: int) -> bytes | None:
    try:
        fd = os.open(_SIDECAR_NAME, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
    except FileNotFoundError:
        return None
    except OSError as exc:
        if exc.errno in {errno.ELOOP, errno.EMLINK}:
            raise WorkspaceHumanNoteError("document.yaml symlinks are not writable") from exc
        raise WorkspaceHumanNoteError("document.yaml cannot be opened safely") from exc

    try:
        observed = os.fstat(fd)
        if not stat_module.S_ISREG(observed.st_mode):
            raise WorkspaceHumanNoteError("document.yaml is not a regular file")
        chunks: list[bytes] = []
        while True:
            block = os.read(fd, 1024 * 1024)
            if not block:
                break
            chunks.append(block)
        return b"".join(chunks)
    except OSError as exc:
        raise WorkspaceHumanNoteError("document.yaml cannot be read safely") from exc
    finally:
        os.close(fd)


def _manifest_digest(raw: bytes | None) -> str | None:
    return hashlib.sha256(raw).hexdigest() if raw is not None else None


def _decode_manifest(raw: bytes | None) -> tuple[str, dict]:
    if raw is None:
        return "", {}
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise WorkspaceHumanNoteError("document.yaml must be UTF-8") from exc
    try:
        value = yaml.safe_load(text) if text.strip() else {}
    except yaml.YAMLError as exc:
        raise WorkspaceHumanNoteError("document.yaml is invalid YAML") from exc
    if value is None:
        value = {}
    if not isinstance(value, dict):
        raise WorkspaceHumanNoteError("document.yaml root must be a mapping")
    return text, value


def _managed_range(text: str) -> tuple[int, int] | None:
    starts = list(_START_RE.finditer(text))
    ends = list(_END_RE.finditer(text))
    if not starts and not ends:
        return None
    if len(starts) != 1 or len(ends) != 1 or starts[0].start() >= ends[0].start():
        raise WorkspaceHumanNoteError("document.yaml has an invalid Pantheon note fragment")
    return starts[0].start(), ends[0].end()


def _note_state(raw: bytes | None, source_relative_path: str) -> dict:
    text, manifest = _decode_manifest(raw)
    managed_range = _managed_range(text)
    namespace = manifest.get(_NAMESPACE)
    if namespace is not None and not isinstance(namespace, dict):
        raise WorkspaceHumanNoteError("pantheon_workspace must be a mapping")
    if namespace is not None and managed_range is None:
        raise WorkspaceHumanNoteConflict(
            "document.yaml already owns pantheon_workspace outside the managed note fragment"
        )
    namespace = namespace or {}
    source_path = namespace.get("source_path")
    note = namespace.get("human_note")
    if source_path is not None and not isinstance(source_path, str):
        raise WorkspaceHumanNoteError("pantheon_workspace.source_path must be a string")
    if note is not None and not isinstance(note, str):
        raise WorkspaceHumanNoteError("pantheon_workspace.human_note must be a string")

    if source_path is None:
        binding_state = "unbound"
    elif source_path == source_relative_path:
        binding_state = "bound"
    else:
        binding_state = "mismatch"

    return {
        "text": text,
        "manifest": manifest,
        "managed_range": managed_range,
        "source_path": source_path,
        "human_note": note or "",
        "binding_state": binding_state,
    }


def _render_fragment(source_relative_path: str, human_note: str) -> str:
    payload = {
        _NAMESPACE: {
            "source_path": source_relative_path,
            "human_note": human_note,
        }
    }
    body = yaml.safe_dump(
        payload,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    ).rstrip("\n")
    return f"{_START_MARKER}\n{body}\n{_END_MARKER}\n"


def _replace_fragment(text: str, managed_range: tuple[int, int] | None, replacement: str) -> str:
    if managed_range is not None:
        start, end = managed_range
        return text[:start] + replacement + text[end:]
    if not replacement:
        return text
    if not text:
        return replacement
    separator = "" if text.endswith(("\n", "\r")) else "\n"
    return text + separator + replacement


def _atomic_replace(parent_fd: int, raw: bytes) -> None:
    temp_name = f".{_SIDECAR_NAME}.pantheon-{uuid.uuid4().hex}.tmp"
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
    fd: int | None = None
    try:
        fd = os.open(temp_name, flags, 0o644, dir_fd=parent_fd)
        offset = 0
        while offset < len(raw):
            offset += os.write(fd, raw[offset:])
        os.fsync(fd)
        os.close(fd)
        fd = None
        os.replace(
            temp_name,
            _SIDECAR_NAME,
            src_dir_fd=parent_fd,
            dst_dir_fd=parent_fd,
        )
        os.fsync(parent_fd)
    except OSError as exc:
        raise WorkspaceHumanNoteError("document.yaml could not be replaced atomically") from exc
    finally:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        try:
            os.unlink(temp_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        except OSError:
            pass


def _context(
    workspace_roots: Mapping[str, str | Path],
    workspace_ref: str,
    relative_path: str,
) -> tuple[str, int]:
    try:
        observation = workspace_collection_read.observe_workspace_file(
            workspace_roots,
            workspace_ref,
            relative_path,
            include_digest=False,
        )
    except workspace_collection_read.WorkspaceCollectionReadError as exc:
        raise WorkspaceHumanNoteError(str(exc)) from exc
    normalized = observation["relative_path"]
    root = workspace_roots.get(workspace_ref)
    if root is None:
        raise WorkspaceHumanNoteError(f"unknown workspace_ref: {workspace_ref!r}")
    parent = PurePosixPath(normalized).parent.as_posix()
    if parent == ".":
        parent = ""
    return normalized, _secure_open_directory(Path(root), parent)


def read_workspace_human_note(
    workspace_roots: Mapping[str, str | Path],
    workspace_ref: str,
    relative_path: str,
) -> dict:
    """Read the one managed human note without inferring document identity."""
    normalized, parent_fd = _context(workspace_roots, workspace_ref, relative_path)
    try:
        raw = _read_sidecar_bytes(parent_fd)
        state = _note_state(raw, normalized)
        return {
            "workspace_ref": workspace_ref,
            "relative_path": normalized,
            "sidecar_relative_path": _sidecar_relative_path(normalized),
            "manifest_state": "present" if raw is not None else "absent",
            "manifest_digest": _manifest_digest(raw),
            "binding_state": state["binding_state"],
            "human_note": state["human_note"],
            "managed_fragment": state["managed_range"] is not None,
            "governed_identity": False,
            "is_evidence": False,
        }
    finally:
        os.close(parent_fd)


def write_workspace_human_note(
    workspace_roots: Mapping[str, str | Path],
    workspace_ref: str,
    relative_path: str,
    *,
    human_note: str,
    expected_manifest_digest: str | None,
) -> dict:
    """Apply one explicit human note with optimistic manifest-digest protection."""
    if not isinstance(human_note, str):
        raise WorkspaceHumanNoteError("human_note must be a string")
    note = human_note.rstrip()
    normalized, parent_fd = _context(workspace_roots, workspace_ref, relative_path)
    try:
        raw = _read_sidecar_bytes(parent_fd)
        current_digest = _manifest_digest(raw)
        if current_digest != expected_manifest_digest:
            raise WorkspaceHumanNoteConflict(
                "document.yaml changed since it was read; refresh the note before saving"
            )
        state = _note_state(raw, normalized)
        if state["binding_state"] == "mismatch":
            raise WorkspaceHumanNoteConflict(
                "document.yaml Pantheon note is bound to another workspace source"
            )

        replacement = _render_fragment(normalized, note) if note else ""
        updated_text = _replace_fragment(state["text"], state["managed_range"], replacement)
        updated_raw = updated_text.encode("utf-8")
        if updated_raw == (raw or b""):
            return read_workspace_human_note(workspace_roots, workspace_ref, normalized)

        # Recheck immediately before the atomic replace. This is an optimistic
        # concurrency gate, not a claim that external editors participate in a
        # filesystem-wide transaction protocol.
        if _manifest_digest(_read_sidecar_bytes(parent_fd)) != current_digest:
            raise WorkspaceHumanNoteConflict(
                "document.yaml changed while the note was being prepared"
            )

        if not updated_text.strip():
            if raw is not None:
                try:
                    os.unlink(_SIDECAR_NAME, dir_fd=parent_fd)
                    os.fsync(parent_fd)
                except FileNotFoundError as exc:
                    raise WorkspaceHumanNoteConflict(
                        "document.yaml disappeared while the note was being saved"
                    ) from exc
                except OSError as exc:
                    raise WorkspaceHumanNoteError("document.yaml could not be removed") from exc
        else:
            _atomic_replace(parent_fd, updated_raw)
    finally:
        os.close(parent_fd)

    return read_workspace_human_note(workspace_roots, workspace_ref, normalized)
