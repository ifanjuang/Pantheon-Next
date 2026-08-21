"""Read-only filesystem workspace projection into Cockpit Card Collections.

This module observes explicitly configured filesystem roots and emits ephemeral
Card projections. It does not create a Folder owner, persist Cards, infer
Project/Category/Source/Document/Knowledge identity, parse file contents or
change authorization/governance state.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path, PurePosixPath
from typing import Mapping
from urllib.parse import quote, urlencode


class WorkspaceCollectionReadError(ValueError):
    """The configured workspace or requested collection cannot be projected safely."""


class WorkspaceNotFound(WorkspaceCollectionReadError):
    """The requested opaque workspace reference is not configured."""


class WorkspacePathNotFound(WorkspaceCollectionReadError):
    """The requested relative workspace path does not exist."""


class WorkspacePathNotDirectory(WorkspaceCollectionReadError):
    """A collection read targeted an entry that is not a directory."""


class WorkspaceConfigurationError(WorkspaceCollectionReadError):
    """The server-side workspace mapping is invalid."""


_WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:(?:/|$)")


def prepare_workspace_roots(
    workspace_roots: Mapping[str, str | Path] | None,
) -> dict[str, Path]:
    """Resolve the explicit server-owned workspace mapping once at composition time."""
    prepared: dict[str, Path] = {}
    for raw_ref, raw_root in (workspace_roots or {}).items():
        ref = str(raw_ref).strip()
        if not ref or ref in {".", ".."} or "/" in ref or "\\" in ref:
            raise WorkspaceConfigurationError(
                f"invalid workspace_ref: {raw_ref!r}"
            )
        if ref in prepared:
            raise WorkspaceConfigurationError(f"duplicate workspace_ref: {ref!r}")
        root = Path(raw_root).resolve()
        if not root.exists() or not root.is_dir():
            raise WorkspaceConfigurationError(
                f"configured workspace root is not an existing directory: {ref!r}"
            )
        prepared[ref] = root
    return prepared


def normalize_relative_path(relative_path: str | None) -> str:
    """Normalize one client-supplied relative POSIX path without broadening scope.

    This intentionally mirrors the existing Task Contract source-path invariant:
    no backslashes, absolute paths or ``..`` traversal. The root collection uses
    the empty string as its relative path.
    """
    if relative_path in (None, ""):
        return ""
    if not isinstance(relative_path, str):
        raise WorkspaceCollectionReadError("workspace path must be a string")
    if "\x00" in relative_path:
        raise WorkspaceCollectionReadError("workspace path contains a NUL byte")
    if "\\" in relative_path or _WINDOWS_DRIVE.match(relative_path):
        raise WorkspaceCollectionReadError(
            f"workspace path is not a relative POSIX path: {relative_path!r}"
        )
    path = PurePosixPath(relative_path)
    if path.is_absolute():
        raise WorkspaceCollectionReadError(
            f"workspace path is not relative: {relative_path!r}"
        )
    if ".." in path.parts:
        raise WorkspaceCollectionReadError(
            f"workspace path traverses outside the configured root: {relative_path!r}"
        )
    normalized = path.as_posix()
    return "" if normalized == "." else normalized


def _reject_symlink_components(root: Path, relative_path: str) -> None:
    """Keep the first slice symlink-free, even when a link would stay in-root."""
    current = root
    for part in PurePosixPath(relative_path).parts if relative_path else ():
        current = current / part
        if current.is_symlink():
            raise WorkspaceCollectionReadError(
                f"workspace symlink entries are not exposed: {relative_path!r}"
            )


def _resolve_directory(root: Path, relative_path: str) -> Path:
    """Resolve a normalized path under one root and require a real directory."""
    _reject_symlink_components(root, relative_path)
    target = (root / relative_path).resolve()
    root_real = root.resolve()
    if not target.is_relative_to(root_real):
        raise WorkspaceCollectionReadError(
            f"workspace path resolves outside the configured root: {relative_path!r}"
        )
    if not target.exists():
        raise WorkspacePathNotFound(
            f"workspace path does not exist: {relative_path!r}"
        )
    if not target.is_dir():
        raise WorkspacePathNotDirectory(
            f"workspace collection target is not a directory: {relative_path!r}"
        )
    return target


def _entry_id(workspace_ref: str, relative_path: str) -> str:
    digest = hashlib.sha256(
        f"{workspace_ref}\0{relative_path}".encode("utf-8")
    ).hexdigest()
    return f"workspace-entry:{digest}"


def _child_collection_href(workspace_ref: str, relative_path: str) -> str:
    encoded_ref = quote(workspace_ref, safe="")
    query = urlencode({"path": relative_path})
    return f"/cockpit/workspace-collections/{encoded_ref}?{query}"


def _workspace_card(
    *,
    workspace_ref: str,
    relative_path: str,
    name: str,
    kind: str,
) -> dict:
    entity_id = _entry_id(workspace_ref, relative_path)
    is_directory = kind == "directory"
    card = {
        "entity_id": entity_id,
        "entity_type": "workspace_entry",
        "role": "container" if is_directory else "entity",
        "family": "information",
        "presentation_family": "information",
        "category": "Dossier" if is_directory else "Fichier",
        "title": name,
        "summary": (
            "Dossier du workspace — projection en lecture seule"
            if is_directory
            else "Fichier du workspace — projection en lecture seule"
        ),
        "status": "neutral",
        "type_tags": [],
        "subject_tags": [],
        "limits": [],
        "available_actions": [],
        "back": [
            ["Workspace", workspace_ref],
            ["Chemin relatif", relative_path],
            ["Nature", "Dossier" if is_directory else "Fichier"],
        ],
        "workspace_ref": workspace_ref,
        "relative_path": relative_path,
        "workspace_entry_kind": kind,
    }
    if is_directory:
        card["child_collection"] = {
            "state": "available",
            "collection_id": f"children:{entity_id}",
            "load_action": {
                "kind": "collection_read",
                "href": _child_collection_href(workspace_ref, relative_path),
            },
            "can_add": False,
            "create_action": None,
        }
    return card


def _relative_child_path(parent: str, name: str) -> str:
    return PurePosixPath(parent, name).as_posix() if parent else PurePosixPath(name).as_posix()


def get_workspace_collection(
    workspace_roots: Mapping[str, Path],
    workspace_ref: str,
    relative_path: str | None = "",
) -> dict:
    """Project the direct children of one explicitly configured workspace directory."""
    root = workspace_roots.get(workspace_ref)
    if root is None:
        raise WorkspaceNotFound(f"unknown workspace_ref: {workspace_ref!r}")

    normalized = normalize_relative_path(relative_path)
    directory = _resolve_directory(root, normalized)

    projected: list[tuple[int, str, str, dict]] = []
    try:
        entries = list(directory.iterdir())
    except OSError as exc:
        raise WorkspaceCollectionReadError(
            f"workspace directory cannot be listed: {normalized!r}"
        ) from exc

    for entry in entries:
        name = entry.name
        if name == "_VAULT.md" or name.startswith(".") or entry.is_symlink():
            continue
        try:
            if entry.is_dir():
                kind = "directory"
                kind_order = 0
            elif entry.is_file():
                kind = "file"
                kind_order = 1
            else:
                continue
        except OSError as exc:
            raise WorkspaceCollectionReadError(
                f"workspace entry cannot be inspected: {name!r}"
            ) from exc

        child_path = _relative_child_path(normalized, name)
        card = _workspace_card(
            workspace_ref=workspace_ref,
            relative_path=child_path,
            name=name,
            kind=kind,
        )
        projected.append((kind_order, name.casefold(), name, card))

    projected.sort(key=lambda item: item[:3])
    items = [item[3] for item in projected]
    parent_entity_id = _entry_id(workspace_ref, normalized)
    return {
        "collection": {
            "collection_id": f"children:{parent_entity_id}",
            "parent_entity_id": parent_entity_id,
            "state": "loaded" if items else "empty",
            "items": items,
            "can_add": False,
        },
        "cards_are_projections": True,
    }
