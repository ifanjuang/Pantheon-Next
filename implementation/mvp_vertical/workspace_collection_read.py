"""Read-only filesystem workspace projection into Cockpit Card Collections.

This module observes explicitly configured filesystem roots and emits ephemeral
Card projections. It does not create a Folder owner, persist Cards, infer
Project/Category/Source/Document/Knowledge identity, parse file contents or
change authorization/governance state.
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import re
from datetime import datetime, timezone
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


class WorkspacePathNotFile(WorkspaceCollectionReadError):
    """A file-detail read targeted an entry that is not a regular file."""


class WorkspaceConfigurationError(WorkspaceCollectionReadError):
    """The server-side workspace mapping is invalid."""


_WINDOWS_DRIVE = re.compile(r"^[A-Za-z]:(?:/|$)")


def parse_workspace_roots_config(raw_config: str | None) -> dict[str, str]:
    """Parse the deployment-owned JSON mapping without inventing any roots."""
    if raw_config is None or not raw_config.strip():
        return {}
    try:
        payload = json.loads(raw_config)
    except (TypeError, json.JSONDecodeError) as exc:
        raise WorkspaceConfigurationError(
            "MVP_WORKSPACE_ROOTS_JSON must be a JSON object"
        ) from exc
    if not isinstance(payload, dict):
        raise WorkspaceConfigurationError(
            "MVP_WORKSPACE_ROOTS_JSON must be a JSON object"
        )

    configured: dict[str, str] = {}
    for raw_ref, raw_root in payload.items():
        if not isinstance(raw_ref, str) or not isinstance(raw_root, str) or not raw_root.strip():
            raise WorkspaceConfigurationError(
                "MVP_WORKSPACE_ROOTS_JSON values must map workspace refs to non-empty paths"
            )
        configured[raw_ref] = raw_root
    return configured


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
        try:
            root = Path(raw_root).resolve()
        except (TypeError, ValueError) as exc:
            raise WorkspaceConfigurationError(
                f"invalid configured workspace root: {ref!r}"
            ) from exc
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


def _reject_hidden_components(relative_path: str) -> None:
    """Do not make explicitly addressed paths wider than directory navigation."""
    for part in PurePosixPath(relative_path).parts if relative_path else ():
        if part == "_VAULT.md" or part.startswith("."):
            raise WorkspacePathNotFound(
                f"workspace path is not exposed by the read projection: {relative_path!r}"
            )


def _reject_symlink_components(root: Path, relative_path: str) -> None:
    """Keep the first slice symlink-free, even when a link would stay in-root."""
    current = root
    for part in PurePosixPath(relative_path).parts if relative_path else ():
        current = current / part
        if current.is_symlink():
            raise WorkspaceCollectionReadError(
                f"workspace symlink entries are not exposed: {relative_path!r}"
            )


def _resolve_entry(root: Path, relative_path: str) -> Path:
    """Resolve one normalized visible path under one configured workspace root."""
    _reject_hidden_components(relative_path)
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
    return target


def _resolve_directory(root: Path, relative_path: str) -> Path:
    """Resolve a normalized path under one root and require a real directory."""
    target = _resolve_entry(root, relative_path)
    if not target.is_dir():
        raise WorkspacePathNotDirectory(
            f"workspace collection target is not a directory: {relative_path!r}"
        )
    return target


def _resolve_file(root: Path, relative_path: str) -> Path:
    """Resolve one visible regular file without following a symlink."""
    if not relative_path:
        raise WorkspacePathNotFile("workspace file path is required")
    target = _resolve_entry(root, relative_path)
    if not target.is_file():
        raise WorkspacePathNotFile(
            f"workspace entry is not a regular file: {relative_path!r}"
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


def _entry_detail_href(workspace_ref: str, relative_path: str) -> str:
    encoded_ref = quote(workspace_ref, safe="")
    query = urlencode({"path": relative_path})
    return f"/cockpit/workspace-entries/{encoded_ref}?{query}"


def _media_type(path: Path) -> str:
    return mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def _file_kind(path: Path, media_type: str) -> str:
    if media_type == "application/pdf" or path.suffix.casefold() == ".pdf":
        return "pdf"
    return "file"


def _basic_file_metadata(path: Path) -> dict:
    """Return cheap reconstructible facts suitable for collection Cards."""
    try:
        byte_size = path.stat().st_size
    except OSError as exc:
        raise WorkspaceCollectionReadError(
            f"workspace file cannot be inspected: {path.name!r}"
        ) from exc
    media_type = _media_type(path)
    return {
        "filename": path.name,
        "extension": path.suffix.casefold(),
        "media_type": media_type,
        "byte_size": byte_size,
        "file_kind": _file_kind(path, media_type),
    }


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
    except OSError as exc:
        raise WorkspaceCollectionReadError(
            f"workspace file cannot be hashed: {path.name!r}"
        ) from exc
    return digest.hexdigest()


def _filesystem_modified_at(path: Path) -> str:
    try:
        modified = path.stat().st_mtime
    except OSError as exc:
        raise WorkspaceCollectionReadError(
            f"workspace file timestamp cannot be observed: {path.name!r}"
        ) from exc
    return datetime.fromtimestamp(modified, tz=timezone.utc).isoformat()


def _adjacent_document_sidecar(path: Path, relative_path: str) -> dict:
    """Observe only sidecar presence; do not parse, validate or infer a binding."""
    sidecar = path.parent / "document.yaml"
    if sidecar.is_symlink():
        state = "unsupported_symlink"
        sidecar_ref = None
    elif sidecar.is_file():
        state = "present"
        parent = PurePosixPath(relative_path).parent
        sidecar_ref = PurePosixPath(parent, "document.yaml").as_posix()
        if sidecar_ref == "./document.yaml":
            sidecar_ref = "document.yaml"
    else:
        state = "absent"
        sidecar_ref = None
    return {
        "state": state,
        "relative_path": sidecar_ref,
        "parsed": False,
        "identity_mapping_resolved": False,
    }


def _workspace_card(
    *,
    workspace_ref: str,
    relative_path: str,
    name: str,
    kind: str,
    file_entry: Path | None = None,
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
    elif file_entry is not None:
        observed = _basic_file_metadata(file_entry)
        if observed["file_kind"] == "pdf":
            card["category"] = "PDF"
            card["summary"] = "PDF du workspace — projection en lecture seule"
        card["workspace_file"] = observed
        card["back"].extend(
            [
                ["Type MIME", observed["media_type"]],
                ["Taille (octets)", observed["byte_size"]],
            ]
        )
        card["entry_detail"] = {
            "state": "available",
            "load_action": {
                "kind": "entry_read",
                "href": _entry_detail_href(workspace_ref, relative_path),
            },
            "observation": "on_read",
            "persisted": False,
        }
    return card


def get_workspace_catalog(workspace_roots: Mapping[str, Path]) -> dict:
    """Project configured workspace references without exposing physical roots."""
    items = [
        _workspace_card(
            workspace_ref=workspace_ref,
            relative_path="",
            name=workspace_ref,
            kind="directory",
        )
        for workspace_ref in sorted(workspace_roots, key=lambda value: (value.casefold(), value))
    ]
    return {
        "collection": {
            "collection_id": "children:space:workspace",
            "parent_entity_id": "space:workspace",
            "state": "loaded" if items else "empty",
            "items": items,
            "can_add": False,
        },
        "cards_are_projections": True,
    }


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
                file_entry = None
            elif entry.is_file():
                kind = "file"
                kind_order = 1
                file_entry = entry
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
            file_entry=file_entry,
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


def get_workspace_entry(
    workspace_roots: Mapping[str, Path],
    workspace_ref: str,
    relative_path: str,
) -> dict:
    """Observe one exact file lazily and return a reconstructible Cockpit Card.

    The read intentionally computes the digest on demand instead of hashing every
    file during a directory listing. Re-reading after a filesystem change yields
    a new observation; nothing here is cached or persisted.
    """
    root = workspace_roots.get(workspace_ref)
    if root is None:
        raise WorkspaceNotFound(f"unknown workspace_ref: {workspace_ref!r}")

    normalized = normalize_relative_path(relative_path)
    entry = _resolve_file(root, normalized)
    card = _workspace_card(
        workspace_ref=workspace_ref,
        relative_path=normalized,
        name=entry.name,
        kind="file",
        file_entry=entry,
    )

    observed = dict(card["workspace_file"])
    observed["digest_sha256"] = _sha256_file(entry)
    observed["filesystem_modified_at"] = _filesystem_modified_at(entry)
    card["workspace_file"] = observed
    card["adjacent_document_sidecar"] = _adjacent_document_sidecar(entry, normalized)
    card["qualification"] = {
        "status": "workspace_observation_only",
        "identity_mapping": "not_resolved_by_workspace_projection",
        "automatic_document_admission": False,
    }
    card["authority"] = {
        "governed_identity": False,
        "is_evidence": False,
        "is_memory": False,
        "is_persisted": False,
    }
    card["back"].extend(
        [
            ["SHA-256", observed["digest_sha256"]],
            ["Modifié (filesystem)", observed["filesystem_modified_at"]],
            ["document.yaml adjacent", card["adjacent_document_sidecar"]["state"]],
        ]
    )

    return {
        "card": card,
        "card_is_projection": True,
        "observation_persisted": False,
        "source_binary_included": False,
        "content_parsed": False,
        "hindsight_required": False,
        "non_equivalences": [
            "workspace path != governed identity",
            "file observed != Document admitted",
            "manifest present != identity mapping resolved",
            "PDF observed != PDF content understood",
            "projection != persistence",
        ],
    }
