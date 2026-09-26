#!/usr/bin/env python3
"""Read-only Cockpit projection for AFFAIRES source + Markdown cartouche bundles."""

from __future__ import annotations

import argparse
import ctypes
import hashlib
from datetime import date, datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import os
from pathlib import Path
import re
import select
import sqlite3
import struct
import sys
import threading
import time
import unicodedata
from typing import Any, Callable, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlparse
from urllib.request import Request, urlopen

import yaml

# server.py is intentionally executable as a standalone script rather than a package.
# Add only its own directory so the colocated producer module is importable in both
# systemd/Docker execution and importlib-based contract tests.
_MODULE_ROOT = Path(__file__).resolve().parent
if str(_MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(_MODULE_ROOT))
from hindsight_producer import HindsightHTTPClient, HindsightProducer
from memory_reconciliation import (
    HermesReconciliationClient,
    MemoryReconciliationService,
    ReconciliationError,
    ReconciliationResidencyError,
)


APP_ROOT = _MODULE_ROOT
STATIC_ROOT = APP_ROOT / "static"
PROJECTION_ID = "affaires_source_cartouche_v3"
CARTOUCHE_SCHEMA = "pantheon/cartouche/v1"
FOLDER_CONTEXT_SCHEMA = "pantheon/folder-context/v1"
MARKDOWN_EXTENSIONS = {".md", ".markdown"}
LEGACY_MANIFEST_NAMES = {"document.yaml", "document.yml", "manifest.yaml", "manifest.yml"}
HINDSIGHT_ELIGIBLE_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".md", ".markdown", ".html", ".htm"}
HEAVY_VISIBLE_EXTENSIONS = {".rvt", ".rfa", ".rte", ".psd", ".psb"}
TEMP_SUFFIXES = {".bak", ".lock", ".lck", ".swp", ".tmp", ".temp", ".autosave"}
MAX_CARTOUCHE_BYTES = 512 * 1024
MAX_ITEMS = 10_000
STATUS_NAMES = ("COMPLETE", "CHECK", "CARTOUCHE_MISSING", "SOURCE_MISSING", "FOLDER")
REVISION_MODES = {"supersedes", "supplements"}
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def _visible(path: Path) -> bool:
    return not path.name.startswith(".") and not path.is_symlink()


def _direct_files(path: Path) -> list[Path]:
    """Return direct regular files, including dot-prefixed cartouches.

    Source admission still filters ordinary hidden files separately.
    """
    try:
        return sorted(
            (item for item in path.iterdir() if item.is_file() and not item.is_symlink()),
            key=lambda item: item.name.casefold(),
        )
    except OSError:
        return []


def _cartouche_name_for_source(source_name: str) -> str:
    return f".{source_name}.md"


def _is_document_cartouche(path: Path) -> bool:
    name = path.name
    return (
        name.startswith(".")
        and name.casefold().endswith(".md")
        and len(name) > len("..md")
        and not _is_temp_or_backup(path)
    )


def _is_temp_or_backup(path: Path) -> bool:
    name = path.name.casefold()
    if name.startswith("~$") or name.startswith(".~lock."):
        return True
    if path.suffix.casefold() in TEMP_SUFFIXES:
        return True
    # Revit numbered backup copies: Model.0001.rvt, Model.0002.rvt, ...
    if re.search(r"\.\d{4}\.r(?:vt|fa|te)$", name):
        return True
    return False


def _is_source_file(path: Path) -> bool:
    if not _visible(path) or _is_temp_or_backup(path):
        return False
    if path.name.casefold() == "_folder.md":
        return False
    if _is_document_cartouche(path):
        return False
    if path.name.casefold() in LEGACY_MANIFEST_NAMES:
        return False
    return True


def _read_cartouche(path: Path) -> tuple[dict[str, Any], str, str | None]:
    """Read one bounded Markdown cartouche without touching its source bytes."""
    try:
        if path.stat().st_size > MAX_CARTOUCHE_BYTES:
            return {}, "", "Cartouche Markdown trop volumineux"
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return {}, "", "Cartouche Markdown illisible"

    metadata: dict[str, Any] = {}
    body = text
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        closing = next((idx for idx, line in enumerate(lines[1:], start=1) if line.strip() == "---"), None)
        if closing is None:
            return {}, text, "Frontmatter YAML non terminé"
        raw_frontmatter = "\n".join(lines[1:closing])
        try:
            parsed = yaml.safe_load(raw_frontmatter) if raw_frontmatter.strip() else {}
        except yaml.YAMLError:
            return {}, "\n".join(lines[closing + 1 :]), "Frontmatter YAML illisible"
        if parsed is None:
            parsed = {}
        if not isinstance(parsed, dict):
            return {}, "\n".join(lines[closing + 1 :]), "Le frontmatter doit contenir un objet YAML"
        metadata = parsed
        body = "\n".join(lines[closing + 1 :])

    return metadata, body, None


def _meta_string(metadata: dict[str, Any], key: str) -> str | None:
    value = metadata.get(key)
    if isinstance(value, str) and value.strip():
        return value.strip()
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return None


def _schema_warning(metadata: dict[str, Any], expected: str) -> str | None:
    schema = _meta_string(metadata, "schema")
    if schema == expected:
        return None
    if schema is None:
        return f"schema absent (attendu: {expected})"
    return f"schema incompatible: {schema} (attendu: {expected})"


def _meta_tags(metadata: dict[str, Any]) -> list[str]:
    value = metadata.get("tags")
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if isinstance(item, (str, int, float)) and str(item).strip()]
    return []


def _revision_relation(
    metadata: dict[str, Any],
    document_id: str | None,
) -> tuple[dict[str, Any], list[str]]:
    """Parse only explicit revision semantics; index/date/name never imply lineage."""
    warnings: list[str] = []
    mode_present = "revision_mode" in metadata
    target_present = "revision_of" in metadata
    mode = _meta_string(metadata, "revision_mode")
    target = _meta_string(metadata, "revision_of")

    if not mode_present and not target_present:
        return {
            "revision_mode": None,
            "revision_of": None,
            "revision_target_present": None,
            "revision_target_status": "NONE",
        }, warnings

    if not mode or not target:
        warnings.append("revision_mode et revision_of doivent être renseignés ensemble")
        return {
            "revision_mode": mode,
            "revision_of": target,
            "revision_target_present": None,
            "revision_target_status": "INVALID",
        }, warnings

    normalized_mode = mode.casefold()
    invalid = False
    if normalized_mode not in REVISION_MODES:
        invalid = True
        warnings.append(
            "revision_mode invalide (attendu: supersedes ou supplements)"
        )
    if document_id and target == document_id:
        invalid = True
        warnings.append("revision_of ne peut pas référencer le document lui-même")

    return {
        "revision_mode": normalized_mode,
        "revision_of": target,
        "revision_target_present": None,
        "revision_target_status": "INVALID" if invalid else "UNRESOLVED",
    }, warnings


def _first_heading(body: str) -> str | None:
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and len(stripped) > 2:
            return stripped[2:].strip()
    return None


def _summary_excerpt(body: str, limit: int = 800) -> str:
    lines = body.splitlines()
    start: int | None = None
    for idx, line in enumerate(lines):
        heading = line.strip().casefold()
        if heading in {"## résumé", "## resume"}:
            start = idx + 1
            break

    chunks: list[str] = []
    if start is not None:
        for line in lines[start:]:
            stripped = line.strip()
            if stripped.startswith("## "):
                break
            if stripped:
                chunks.append(stripped)
    else:
        paragraph: list[str] = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                if paragraph:
                    break
                continue
            if stripped.startswith("#"):
                continue
            paragraph.append(stripped)
        chunks = paragraph

    text = " ".join(chunks).strip()
    if len(text) > limit:
        return text[: limit - 1].rstrip() + "…"
    return text


def _mtime_iso(path: Path) -> str | None:
    try:
        return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).isoformat().replace("+00:00", "Z")
    except OSError:
        return None


def _file_size(path: Path) -> int | None:
    try:
        return path.stat().st_size
    except OSError:
        return None


def _file_sha256(path: Path) -> tuple[str | None, str | None]:
    """Hash source bytes only when a cartouche explicitly requests integrity verification."""
    try:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest(), None
    except OSError:
        return None, "Source illisible pendant la vérification SHA-256"


def _declared_source_size(metadata: dict[str, Any]) -> tuple[int | None, str | None]:
    value = metadata.get("source_size_bytes")
    if value is None:
        return None, None
    if isinstance(value, bool):
        return None, "source_size_bytes invalide"
    if isinstance(value, int) and value >= 0:
        return value, None
    if isinstance(value, str):
        normalized = value.strip()
        if normalized.isdigit() and len(normalized) <= 20:
            try:
                return int(normalized), None
            except ValueError:
                pass
    return None, "source_size_bytes invalide"


def _source_integrity(
    metadata: dict[str, Any],
    source: Path,
    *,
    require_digest: bool = False,
    require_size: bool = False,
) -> tuple[dict[str, Any], list[str]]:
    """Verify an explicitly declared source checksum without hashing every AFFAIRES source."""
    warnings: list[str] = []
    declared_key_present = "source_sha256" in metadata
    declared = _meta_string(metadata, "source_sha256")
    declared_size, size_error = _declared_source_size(metadata)
    actual_size = _file_size(source)

    if size_error:
        warnings.append(size_error)
    elif require_size and declared_size is None:
        warnings.append("source_size_bytes absent du cartouche")
    elif declared_size is not None and actual_size is not None and declared_size != actual_size:
        warnings.append(
            f"source_size_bytes différent de la source : déclaré {declared_size}, observé {actual_size}"
        )

    if declared is None:
        if declared_key_present:
            warnings.append("source_sha256 invalide : chaîne hexadécimale attendue")
            return {
                "source_sha256": None,
                "source_sha256_verified": False,
                "source_integrity": "INVALID",
                "declared_source_size": declared_size,
            }, warnings
        if require_digest:
            warnings.append("source_sha256 absent du cartouche")
        return {
            "source_sha256": None,
            "source_sha256_verified": None,
            "source_integrity": "UNDECLARED",
            "declared_source_size": declared_size,
        }, warnings

    if not SHA256_RE.fullmatch(declared):
        warnings.append("source_sha256 invalide : 64 caractères hexadécimaux attendus")
        return {
            "source_sha256": declared,
            "source_sha256_verified": False,
            "source_integrity": "INVALID",
            "declared_source_size": declared_size,
        }, warnings

    normalized = declared.casefold()
    observed, hash_error = _file_sha256(source)
    if hash_error or observed is None:
        warnings.append(hash_error or "Vérification SHA-256 impossible")
        return {
            "source_sha256": normalized,
            "source_sha256_verified": False,
            "source_integrity": "UNREADABLE",
            "declared_source_size": declared_size,
        }, warnings

    verified = observed == normalized
    if not verified:
        warnings.append("source_sha256 ne correspond pas aux octets exacts de la source")
    return {
        "source_sha256": normalized,
        "source_sha256_verified": verified,
        "source_integrity": "VERIFIED" if verified else "MISMATCH",
        "declared_source_size": declared_size,
    }, warnings


def _safe_source_ref(value: str | None) -> tuple[str | None, str | None]:
    if not value:
        return None, None
    if "/" in value or "\\" in value or value in {".", ".."}:
        return None, "La source déclarée doit rester dans le même dossier"
    if Path(value).is_absolute() or Path(value).name != value:
        return None, "La source déclarée doit rester dans le même dossier"
    return value, None


def _subtitle(metadata: dict[str, Any]) -> str:
    parts = [
        _meta_string(metadata, "type"),
        _meta_string(metadata, "phase"),
        _meta_string(metadata, "index"),
        _meta_string(metadata, "document_date"),
    ]
    return " · ".join(part for part in parts if part) or "Cartouche Markdown"


def _document_card(workspace: str, root: Path, source: Path, cartouche: Path | None) -> dict[str, Any]:
    relative_source = source.relative_to(root).as_posix()
    extension = source.suffix.casefold()
    size = _file_size(source)

    if cartouche is None:
        return {
            "workspace": workspace,
            "kind": "document",
            "path": relative_source,
            "parent_path": source.parent.relative_to(root).as_posix() if source.parent != root else "",
            "name": source.name,
            "title": source.name,
            "subtitle": "Cartouche manquant",
            "summary": "",
            "status": "CARTOUCHE_MISSING",
            "document_id": None,
            "source": source.name,
            "source_present": True,
            "cartouche": None,
            "cartouche_present": False,
            "can_generate_cartouche": True,
            "project": None,
            "phase": None,
            "document_type": None,
            "index": None,
            "document_date": None,
            "issuer": None,
            "revision_mode": None,
            "revision_of": None,
            "revision_target_present": None,
            "revision_target_status": "NONE",
            "tags": [],
            "extension": extension.removeprefix(".").upper() or "FILE",
            "source_size": size,
            "source_sha256": None,
            "source_sha256_verified": None,
            "source_integrity": "UNDECLARED",
            "declared_source_size": None,
            "hindsight_format_supported": extension in HINDSIGHT_ELIGIBLE_EXTENSIONS,
            "hindsight_eligible": False,
            "hindsight_representation_candidate": None,
            "heavy_binary": extension in HEAVY_VISIBLE_EXTENSIONS,
            "modified_at": _mtime_iso(source),
            "warnings": [],
        }

    metadata, body, cartouche_error = _read_cartouche(cartouche)
    warnings: list[str] = []
    if cartouche_error:
        warnings.append(cartouche_error)
    else:
        schema_warning = _schema_warning(metadata, CARTOUCHE_SCHEMA)
        if schema_warning:
            warnings.append(schema_warning)

    declared, source_ref_error = _safe_source_ref(_meta_string(metadata, "source"))
    if source_ref_error:
        warnings.append(source_ref_error)
    elif declared is None:
        warnings.append("Source non déclarée dans le cartouche")
    elif declared != source.name:
        warnings.append(f"Source déclarée différente du fichier apparié : {declared}")

    document_id = _meta_string(metadata, "document_id")
    if not document_id:
        warnings.append("document_id absent du cartouche")

    revision, revision_warnings = _revision_relation(metadata, document_id)
    warnings.extend(revision_warnings)

    integrity, integrity_warnings = _source_integrity(
        metadata,
        source,
        require_digest=extension == ".eml",
        require_size=extension == ".eml",
    )
    warnings.extend(integrity_warnings)

    title = _meta_string(metadata, "title") or _first_heading(body) or source.stem
    status = "CHECK" if warnings else "COMPLETE"
    source_format_supported = extension in HINDSIGHT_ELIGIBLE_EXTENSIONS
    email_cartouche_candidate = (
        extension == ".eml"
        and status == "COMPLETE"
        and integrity.get("source_sha256_verified") is True
    )
    producer_eligible = status == "COMPLETE" and (
        source_format_supported or email_cartouche_candidate
    )
    return {
        "workspace": workspace,
        "kind": "document",
        "path": relative_source,
        "parent_path": source.parent.relative_to(root).as_posix() if source.parent != root else "",
        "name": source.name,
        "title": title,
        "subtitle": _subtitle(metadata),
        "summary": _summary_excerpt(body),
        "status": status,
        "document_id": document_id,
        "source": source.name,
        "source_present": True,
        "cartouche": cartouche.name,
        "cartouche_present": True,
        "can_generate_cartouche": False,
        "project": _meta_string(metadata, "project"),
        "phase": _meta_string(metadata, "phase"),
        "document_type": _meta_string(metadata, "type"),
        "index": _meta_string(metadata, "index"),
        "document_date": _meta_string(metadata, "document_date"),
        "issuer": _meta_string(metadata, "issuer"),
        **revision,
        "tags": _meta_tags(metadata),
        "extension": extension.removeprefix(".").upper() or "FILE",
        "source_size": size,
        **integrity,
        "hindsight_format_supported": source_format_supported,
        "hindsight_eligible": producer_eligible,
        "hindsight_representation_candidate": (
            "cartouche" if email_cartouche_candidate
            else "source" if source_format_supported and status == "COMPLETE"
            else None
        ),
        "heavy_binary": extension in HEAVY_VISIBLE_EXTENSIONS,
        "modified_at": max(
            (value for value in (_mtime_iso(source), _mtime_iso(cartouche)) if value),
            default=None,
        ),
        "warnings": warnings,
    }


def _orphan_cartouche_card(workspace: str, root: Path, cartouche: Path) -> dict[str, Any]:
    metadata, body, cartouche_error = _read_cartouche(cartouche)
    warnings: list[str] = []
    if cartouche_error:
        warnings.append(cartouche_error)
    else:
        schema_warning = _schema_warning(metadata, CARTOUCHE_SCHEMA)
        if schema_warning:
            warnings.append(schema_warning)

    declared, source_ref_error = _safe_source_ref(_meta_string(metadata, "source"))
    if source_ref_error:
        warnings.append(source_ref_error)

    source_path: Path | None = None
    source_present = False
    if declared:
        candidate = cartouche.parent / declared
        try:
            source_present = candidate.is_file() and not candidate.is_symlink() and _is_source_file(candidate)
        except OSError:
            source_present = False
        if source_present:
            source_path = candidate
            warnings.append("La source existe mais son basename ne correspond pas au cartouche")
    else:
        warnings.append("Source non déclarée dans le cartouche")

    document_id = _meta_string(metadata, "document_id")
    if not document_id:
        warnings.append("document_id absent du cartouche")

    revision, revision_warnings = _revision_relation(metadata, document_id)
    warnings.extend(revision_warnings)

    integrity = {
        "source_sha256": _meta_string(metadata, "source_sha256"),
        "source_sha256_verified": None,
        "source_integrity": "SOURCE_MISSING" if not source_present else "UNVERIFIED",
        "declared_source_size": _declared_source_size(metadata)[0],
    }
    if source_present and source_path is not None:
        integrity, integrity_warnings = _source_integrity(
            metadata,
            source_path,
            require_digest=source_path.suffix.casefold() == ".eml",
            require_size=source_path.suffix.casefold() == ".eml",
        )
        warnings.extend(integrity_warnings)

    fallback_title = cartouche.name[1:-3] if _is_document_cartouche(cartouche) else cartouche.stem
    title = _meta_string(metadata, "title") or _first_heading(body) or fallback_title
    status = "CHECK" if source_present else "SOURCE_MISSING"
    return {
        "workspace": workspace,
        "kind": "document",
        "path": (source_path or cartouche).relative_to(root).as_posix(),
        "parent_path": cartouche.parent.relative_to(root).as_posix() if cartouche.parent != root else "",
        "name": source_path.name if source_path else cartouche.name,
        "title": title,
        "subtitle": _subtitle(metadata) if source_present else "Source manquante",
        "summary": _summary_excerpt(body),
        "status": status,
        "document_id": document_id,
        "source": declared,
        "source_present": source_present,
        "cartouche": cartouche.name,
        "cartouche_present": True,
        "can_generate_cartouche": False,
        "project": _meta_string(metadata, "project"),
        "phase": _meta_string(metadata, "phase"),
        "document_type": _meta_string(metadata, "type"),
        "index": _meta_string(metadata, "index"),
        "document_date": _meta_string(metadata, "document_date"),
        "issuer": _meta_string(metadata, "issuer"),
        **revision,
        "tags": _meta_tags(metadata),
        "extension": source_path.suffix.removeprefix(".").upper() if source_path else None,
        "source_size": _file_size(source_path) if source_path else None,
        **integrity,
        "hindsight_format_supported": bool(
            source_path and source_path.suffix.casefold() in HINDSIGHT_ELIGIBLE_EXTENSIONS
        ),
        "hindsight_eligible": False,
        "hindsight_representation_candidate": None,
        "heavy_binary": bool(source_path and source_path.suffix.casefold() in HEAVY_VISIBLE_EXTENSIONS),
        "modified_at": max(
            (value for value in (_mtime_iso(cartouche), _mtime_iso(source_path) if source_path else None) if value),
            default=None,
        ),
        "warnings": warnings,
    }


def _folder_card(workspace: str, root: Path, folder: Path) -> dict[str, Any]:
    folder_context = next(
        (item for item in _direct_files(folder) if item.name.casefold() == "_folder.md"),
        None,
    )
    metadata: dict[str, Any] = {}
    body = ""
    warnings: list[str] = []
    if folder_context:
        metadata, body, error = _read_cartouche(folder_context)
        if error:
            warnings.append(error)
        else:
            schema_warning = _schema_warning(metadata, FOLDER_CONTEXT_SCHEMA)
            if schema_warning:
                warnings.append(schema_warning)

    relative_path = folder.relative_to(root).as_posix()
    return {
        "workspace": workspace,
        "kind": "folder",
        "path": relative_path,
        "parent_path": folder.parent.relative_to(root).as_posix() if folder.parent != root else "",
        "name": folder.name,
        "title": _meta_string(metadata, "title") or _first_heading(body) or folder.name,
        "subtitle": _meta_string(metadata, "phase") or "Dossier",
        "summary": _summary_excerpt(body),
        "status": "CHECK" if warnings else "FOLDER",
        "folder_context": folder_context.name if folder_context else None,
        "folder_context_present": folder_context is not None,
        "can_generate_folder_context": folder_context is None,
        "project": _meta_string(metadata, "project"),
        "phase": _meta_string(metadata, "phase"),
        "tags": _meta_tags(metadata),
        "modified_at": max(
            (value for value in (_mtime_iso(folder), _mtime_iso(folder_context) if folder_context else None) if value),
            default=None,
        ),
        "warnings": warnings,
    }


def _directory_document_cards(workspace: str, root: Path, folder: Path) -> list[dict[str, Any]]:
    direct = _direct_files(folder)
    sources = [item for item in direct if _is_source_file(item)]
    cartouches = [item for item in direct if _is_document_cartouche(item)]
    # Pairing is exact and case-sensitive because Linux filenames are exact identifiers.
    cartouche_by_name = {item.name: item for item in cartouches}

    cards: list[dict[str, Any]] = []
    paired_cartouches: set[Path] = set()
    source_cards: list[dict[str, Any]] = []
    for source in sources:
        expected_name = _cartouche_name_for_source(source.name)
        cartouche = cartouche_by_name.get(expected_name)
        if cartouche:
            paired_cartouches.add(cartouche)
        card = _document_card(workspace, root, source, cartouche)
        cards.append(card)
        source_cards.append(card)

    # Portable storage can be case-insensitive and normalize Unicode even when Linux does not.
    portable_groups: dict[str, list[dict[str, Any]]] = {}
    for card in source_cards:
        key = unicodedata.normalize("NFC", card["name"]).casefold()
        portable_groups.setdefault(key, []).append(card)
    for group in portable_groups.values():
        exact_names = {card["name"] for card in group}
        if len(group) > 1 and len(exact_names) > 1:
            for card in group:
                card["status"] = "CHECK"
                card["name_conflict"] = "CASE_OR_UNICODE_COLLISION"
                card["hindsight_eligible"] = False
                card["hindsight_representation_candidate"] = None
                card["warnings"].append("Collision potentielle de nom sur stockage case-insensitive/normalisé")

    for cartouche in cartouches:
        if cartouche in paired_cartouches:
            continue
        metadata, _body, read_error = _read_cartouche(cartouche)
        # Ignore unrelated hidden Markdown unless it declares itself as a Pantheon cartouche
        # or otherwise carries cartouche-shaped metadata.
        if (
            read_error is None
            and _meta_string(metadata, "schema") != CARTOUCHE_SCHEMA
            and not any(key in metadata for key in ("source", "document_id"))
        ):
            continue
        cards.append(_orphan_cartouche_card(workspace, root, cartouche))

    return cards


def _walk_directories(root: Path, max_depth: int) -> Iterable[Path]:
    def visit(parent: Path, depth: int) -> Iterable[Path]:
        if depth > max_depth:
            return
        try:
            children = sorted(
                (item for item in parent.iterdir() if item.is_dir() and _visible(item)),
                key=lambda item: item.name.casefold(),
            )
        except OSError:
            return
        for child in children:
            yield child
            if depth < max_depth:
                yield from visit(child, depth + 1)

    yield from visit(root, 1)


def scan_workspaces(roots: list[tuple[str, Path]], max_depth: int = 2) -> dict[str, Any]:
    workspaces: list[dict[str, Any]] = []

    for label, root in roots:
        cards: list[dict[str, Any]] = []
        errors: list[str] = []
        root_available = root.is_dir() and os.access(root, os.R_OK | os.X_OK)
        if not root_available:
            errors.append("Source AFFAIRES indisponible")
        else:
            candidates: list[dict[str, Any]] = []
            candidates.extend(_directory_document_cards(label, root, root))
            for folder in _walk_directories(root, max_depth):
                candidates.append(_folder_card(label, root, folder))
                candidates.extend(_directory_document_cards(label, root, folder))
                if len(candidates) >= MAX_ITEMS:
                    errors.append(f"Inventaire limité aux {MAX_ITEMS} premiers éléments")
                    break

            cards.extend(candidates[:MAX_ITEMS])

        workspaces.append({"name": label, "available": root_available, "cards": cards, "errors": errors})

    # A copied bundle must not silently become the same Hindsight document in two places.
    document_ids: dict[str, list[dict[str, Any]]] = {}
    for workspace in workspaces:
        for card in workspace["cards"]:
            if card.get("kind") == "document" and card.get("document_id"):
                document_ids.setdefault(card["document_id"], []).append(card)
    for document_id, duplicates in document_ids.items():
        if len(duplicates) < 2:
            continue
        for card in duplicates:
            # Preserve a more specific broken-pair state such as SOURCE_MISSING.
            if card.get("status") == "COMPLETE":
                card["status"] = "CHECK"
            card["hindsight_eligible"] = False
            card["hindsight_representation_candidate"] = None
            card["identity_conflict"] = "DUPLICATE_DOCUMENT_ID"
            card["warnings"].append(f"document_id dupliqué dans AFFAIRES: {document_id}")

    for workspace in workspaces:
        for card in workspace["cards"]:
            target = card.get("revision_of")
            if not target or card.get("revision_target_status") == "INVALID":
                continue
            matches = document_ids.get(target, [])
            if len(matches) == 1:
                card["revision_target_present"] = True
                card["revision_target_status"] = "RESOLVED"
            elif len(matches) > 1:
                card["revision_target_present"] = True
                card["revision_target_status"] = "AMBIGUOUS"
            else:
                # Missing history is observable but does not make index/date authoritative
                # and does not block an otherwise valid current bundle.
                card["revision_target_present"] = False
                card["revision_target_status"] = "MISSING"

    totals = {status: 0 for status in STATUS_NAMES}
    total_items = 0
    document_count = 0
    folder_count = 0
    for workspace in workspaces:
        for card in workspace["cards"]:
            totals[card["status"]] = totals.get(card["status"], 0) + 1
            total_items += 1
            if card["kind"] == "folder":
                folder_count += 1
            else:
                document_count += 1

    return {
        "generated_at": datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z"),
        "projection": PROJECTION_ID,
        "read_only": True,
        "totals": totals,
        "workspace_count": len(workspaces),
        "item_count": total_items,
        "package_count": total_items,
        "document_count": document_count,
        "folder_count": folder_count,
        "workspaces": workspaces,
    }


class _InotifyWatcher:
    """Best-effort Linux event accelerator; periodic reconcile remains authoritative."""

    _EVENT = struct.Struct("iIII")
    _IN_ATTRIB = 0x00000004
    _IN_CLOSE_WRITE = 0x00000008
    _IN_MOVED_FROM = 0x00000040
    _IN_MOVED_TO = 0x00000080
    _IN_CREATE = 0x00000100
    _IN_DELETE = 0x00000200
    _IN_DELETE_SELF = 0x00000400
    _IN_MOVE_SELF = 0x00000800
    _IN_Q_OVERFLOW = 0x00004000
    _IN_IGNORED = 0x00008000
    _IN_ISDIR = 0x40000000
    _WATCH_MASK = (
        _IN_ATTRIB
        | _IN_CLOSE_WRITE
        | _IN_MOVED_FROM
        | _IN_MOVED_TO
        | _IN_CREATE
        | _IN_DELETE
        | _IN_DELETE_SELF
        | _IN_MOVE_SELF
    )

    def __init__(
        self,
        roots: list[tuple[str, Path]],
        max_depth: int,
        on_event: Callable[[], None],
    ) -> None:
        self._roots = [root for _, root in roots]
        self._max_depth = max_depth
        self._on_event = on_event
        self._fd = -1
        self._libc: Any = None
        self._watches: dict[int, Path] = {}
        self._watch_lock = threading.RLock()
        self._stop = threading.Event()
        self._rebuild = threading.Event()
        self._thread: threading.Thread | None = None
        self.mode = "reconcile-only"

    def _within_depth(self, path: Path) -> bool:
        for root in self._roots:
            try:
                depth = len(path.relative_to(root).parts)
            except ValueError:
                continue
            if depth <= self._max_depth:
                return True
        return False

    def _add_watch(self, path: Path) -> None:
        if self._fd < 0 or not self._within_depth(path):
            return
        try:
            if not path.is_dir() or path.is_symlink() or not _visible(path):
                return
        except OSError:
            return
        wd = self._libc.inotify_add_watch(self._fd, os.fsencode(path), self._WATCH_MASK)
        if wd >= 0:
            with self._watch_lock:
                self._watches[int(wd)] = path

    def _reset_watches(self) -> None:
        if self._fd < 0:
            return
        with self._watch_lock:
            old = list(self._watches)
            self._watches.clear()
        for wd in old:
            try:
                self._libc.inotify_rm_watch(self._fd, wd)
            except Exception:
                pass
        for root in self._roots:
            try:
                if not root.is_dir():
                    continue
            except OSError:
                continue
            self._add_watch(root)
            for folder in _walk_directories(root, self._max_depth):
                self._add_watch(folder)

    def start(self) -> bool:
        if not sys.platform.startswith("linux"):
            return False
        try:
            libc = ctypes.CDLL(None, use_errno=True)
            libc.inotify_init1.argtypes = [ctypes.c_int]
            libc.inotify_init1.restype = ctypes.c_int
            libc.inotify_add_watch.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_uint32]
            libc.inotify_add_watch.restype = ctypes.c_int
            libc.inotify_rm_watch.argtypes = [ctypes.c_int, ctypes.c_int]
            libc.inotify_rm_watch.restype = ctypes.c_int
            fd = libc.inotify_init1(os.O_NONBLOCK | getattr(os, "O_CLOEXEC", 0))
        except (AttributeError, OSError):
            return False
        if fd < 0:
            return False

        self._libc = libc
        self._fd = int(fd)
        self._reset_watches()
        self.mode = "inotify"
        self._thread = threading.Thread(target=self._run, name="workspace-inotify", daemon=True)
        self._thread.start()
        return True

    def request_rebuild(self) -> None:
        if self._fd >= 0:
            self._rebuild.set()

    def _run(self) -> None:
        while not self._stop.is_set():
            if self._rebuild.is_set():
                self._rebuild.clear()
                self._reset_watches()
            try:
                readable, _, _ = select.select([self._fd], [], [], 0.5)
            except (OSError, ValueError):
                if self._stop.is_set():
                    break
                continue
            if not readable:
                continue
            try:
                payload = os.read(self._fd, 64 * 1024)
            except BlockingIOError:
                continue
            except OSError:
                if self._stop.is_set():
                    break
                continue

            offset = 0
            changed = False
            rebuild = False
            while offset + self._EVENT.size <= len(payload):
                wd, mask, _cookie, name_len = self._EVENT.unpack_from(payload, offset)
                offset += self._EVENT.size
                raw_name = payload[offset : offset + name_len]
                offset += name_len
                name = raw_name.rstrip(b"\0").decode(errors="surrogateescape") if raw_name else ""

                if mask & self._IN_Q_OVERFLOW:
                    changed = True
                    rebuild = True
                    continue

                with self._watch_lock:
                    base = self._watches.get(wd)
                if mask & self._IN_IGNORED:
                    with self._watch_lock:
                        self._watches.pop(wd, None)
                    continue

                if base and name and mask & self._IN_ISDIR and mask & (self._IN_CREATE | self._IN_MOVED_TO):
                    self._add_watch(base / name)
                    rebuild = True
                if mask & self._IN_ISDIR and mask & (
                    self._IN_DELETE_SELF | self._IN_MOVE_SELF | self._IN_MOVED_FROM | self._IN_DELETE
                ):
                    rebuild = True
                if mask & self._WATCH_MASK:
                    changed = True

            if rebuild:
                self._rebuild.set()
            if changed:
                self._on_event()

    def stop(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2)
        if self._fd >= 0:
            try:
                os.close(self._fd)
            except OSError:
                pass
            self._fd = -1
        self.mode = "stopped"


class WorkspaceIndex:
    """Reconstructible technical index for fast Cockpit reads and later sync ownership."""

    SCHEMA_VERSION = "1"

    def __init__(
        self,
        roots: list[tuple[str, Path]],
        max_depth: int,
        state_db: Path,
        *,
        reconcile_seconds: float = 60.0,
        debounce_seconds: float = 0.5,
        enable_watcher: bool = True,
        producer: HindsightProducer | None = None,
    ) -> None:
        self.roots = roots
        self.max_depth = max_depth
        self.state_db = state_db
        self.reconcile_seconds = max(0.1, float(reconcile_seconds))
        self.debounce_seconds = max(0.0, float(debounce_seconds))
        self.enable_watcher = enable_watcher
        self.producer = producer
        self._snapshot: dict[str, Any] = {
            "generated_at": None,
            "projection": PROJECTION_ID,
            "read_only": True,
            "totals": {status: 0 for status in STATUS_NAMES},
            "workspace_count": len(roots),
            "item_count": 0,
            "package_count": 0,
            "document_count": 0,
            "folder_count": 0,
            "workspaces": [{"name": label, "available": False, "cards": [], "errors": ["Index non initialisé"]} for label, _ in roots],
            "index_state": {"mode": "initializing", "watcher": "reconcile-only"},
            "hindsight_producer": {"enabled": producer is not None},
        }
        self._snapshot_lock = threading.RLock()
        self._reconcile_lock = threading.Lock()
        self._dirty = threading.Event()
        self._stop = threading.Event()
        self._coordinator: threading.Thread | None = None
        self._watcher = _InotifyWatcher(roots, max_depth, self.mark_dirty)
        self._watcher_mode = "reconcile-only"
        self._last_error: str | None = None

    def _persist(self, snapshot: dict[str, Any], reason: str) -> str | None:
        try:
            self.state_db.parent.mkdir(parents=True, exist_ok=True)
            connection = sqlite3.connect(self.state_db, timeout=5)
            try:
                connection.execute("PRAGMA journal_mode=DELETE")
                connection.execute("PRAGMA synchronous=NORMAL")
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS workspace_entries (
                        entry_key TEXT PRIMARY KEY,
                        workspace TEXT NOT NULL,
                        kind TEXT NOT NULL,
                        path TEXT NOT NULL,
                        status TEXT NOT NULL,
                        payload_json TEXT NOT NULL,
                        observed_at TEXT NOT NULL
                    )
                    """
                )
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS workspace_meta (
                        key TEXT PRIMARY KEY,
                        value TEXT NOT NULL
                    )
                    """
                )
                observed_at = snapshot["generated_at"] or ""
                with connection:
                    connection.execute("DELETE FROM workspace_entries")
                    for workspace in snapshot["workspaces"]:
                        workspace_name = workspace["name"]
                        for card in workspace["cards"]:
                            entry_key = json.dumps(
                                [workspace_name, card.get("kind"), card.get("path"), card.get("cartouche")],
                                ensure_ascii=False,
                                separators=(",", ":"),
                            )
                            connection.execute(
                                """
                                INSERT INTO workspace_entries(
                                    entry_key, workspace, kind, path, status, payload_json, observed_at
                                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                                """,
                                (
                                    entry_key,
                                    workspace_name,
                                    card.get("kind") or "",
                                    card.get("path") or "",
                                    card.get("status") or "",
                                    json.dumps(card, ensure_ascii=False, separators=(",", ":")),
                                    observed_at,
                                ),
                            )
                    meta = {
                        "schema_version": self.SCHEMA_VERSION,
                        "projection": PROJECTION_ID,
                        "last_reconcile_at": observed_at,
                        "last_reconcile_reason": reason,
                    }
                    connection.executemany(
                        "INSERT OR REPLACE INTO workspace_meta(key, value) VALUES (?, ?)",
                        list(meta.items()),
                    )
            finally:
                connection.close()
        except (OSError, sqlite3.Error) as exc:
            return f"{type(exc).__name__}: {exc}"
        return None

    def reconcile(self, reason: str = "manual") -> dict[str, Any]:
        with self._reconcile_lock:
            snapshot = scan_workspaces(self.roots, self.max_depth)
            if self.producer is None:
                snapshot["hindsight_producer"] = {"enabled": False}
            else:
                try:
                    snapshot["hindsight_producer"] = self.producer.reconcile(snapshot)
                except Exception as exc:  # producer failure must not take Cockpit navigation down
                    snapshot["hindsight_producer"] = {
                        **self.producer.health(),
                        "last_error": f"{type(exc).__name__}: {exc}",
                    }
            index_state = {
                "mode": "indexed",
                "watcher": self._watcher_mode,
                "last_reconcile_at": snapshot["generated_at"],
                "last_reconcile_reason": reason,
                "reconcile_seconds": self.reconcile_seconds,
            }
            snapshot["index_state"] = index_state
            persistence_error = self._persist(snapshot, reason)
            if persistence_error:
                index_state["state_error"] = persistence_error
                self._last_error = persistence_error
            else:
                self._last_error = None
            with self._snapshot_lock:
                self._snapshot = snapshot
            if self._watcher_mode == "inotify":
                self._watcher.request_rebuild()
            return snapshot

    def snapshot(self) -> dict[str, Any]:
        with self._snapshot_lock:
            return self._snapshot

    def health(self) -> dict[str, Any]:
        with self._snapshot_lock:
            state = dict(self._snapshot.get("index_state") or {})
        state["state_error"] = self._last_error
        state["hindsight_producer"] = (
            self.producer.health() if self.producer is not None else {"enabled": False}
        )
        return state

    def mark_dirty(self) -> None:
        self._dirty.set()

    def _coordinator_loop(self) -> None:
        next_periodic = time.monotonic() + self.reconcile_seconds
        while not self._stop.is_set():
            timeout = max(0.0, next_periodic - time.monotonic())
            dirty = self._dirty.wait(timeout)
            if self._stop.is_set():
                break
            if dirty:
                if self._stop.wait(self.debounce_seconds):
                    break
                self._dirty.clear()
                reason = "watch"
            else:
                reason = "periodic"
            try:
                self.reconcile(reason)
            except Exception as exc:  # defensive: an index failure must not kill the HTTP service
                self._last_error = f"{type(exc).__name__}: {exc}"
                print(f"workspace-cockpit: reconcile failed: {self._last_error}", file=sys.stderr)
            next_periodic = time.monotonic() + self.reconcile_seconds

    def start(self) -> None:
        if self.enable_watcher and self._watcher.start():
            self._watcher_mode = "inotify"
        self.reconcile("startup")
        self._coordinator = threading.Thread(
            target=self._coordinator_loop,
            name="workspace-reconcile",
            daemon=True,
        )
        self._coordinator.start()

    def stop(self) -> None:
        self._stop.set()
        self._dirty.set()
        if self._coordinator:
            self._coordinator.join(timeout=2)
        self._watcher.stop()


def _path_is_within(candidate: Path, root: Path) -> bool:
    try:
        candidate.resolve(strict=False).relative_to(root.resolve(strict=False))
        return True
    except (OSError, RuntimeError, ValueError):
        return False


class CockpitHandler(BaseHTTPRequestHandler):
    roots: list[tuple[str, Path]] = []
    max_depth = 2
    workspace_index: WorkspaceIndex | None = None
    role_trace_url = ""
    role_trace_key = ""
    memory_reconciliation: MemoryReconciliationService | None = None

    def _headers(self, status: HTTPStatus, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; "
            "connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'",
        )
        self.end_headers()

    def _json(self, value: Any, status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(value, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        self._headers(status, "application/json; charset=utf-8")
        self.wfile.write(body)

    def _proxy_role_trace(self, upstream_path: str, *, stream: bool = False) -> None:
        if not self.role_trace_url or not self.role_trace_key:
            self._json({"error": "role_trace_not_configured"}, HTTPStatus.NOT_FOUND)
            return
        headers = {"Authorization": f"Bearer {self.role_trace_key}"}
        last_event_id = self.headers.get("Last-Event-ID", "").strip()
        if last_event_id:
            headers["Last-Event-ID"] = last_event_id
        request = Request(f"{self.role_trace_url}{upstream_path}", headers=headers)
        try:
            response = urlopen(request, timeout=190 if stream else 5)
        except HTTPError as exc:
            body = exc.read(16_384)
            self._headers(HTTPStatus(exc.code), exc.headers.get_content_type() or "application/json")
            self.wfile.write(body)
            return
        except (OSError, URLError):
            self._json({"error": "role_trace_unavailable"}, HTTPStatus.BAD_GATEWAY)
            return
        with response:
            content_type = response.headers.get("Content-Type", "application/json")
            self._headers(HTTPStatus.OK, content_type)
            while True:
                chunk = response.read(8192)
                if not chunk:
                    break
                self.wfile.write(chunk)
                if stream:
                    self.wfile.flush()

    def do_POST(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlparse(self.path).path
        match = re.fullmatch(r"/api/documents/([^/]+)/reconcile-memory", path)
        if not match:
            self._json({"error": "not_found"}, HTTPStatus.NOT_FOUND)
            return
        if self.memory_reconciliation is None:
            self._json({"error": "memory_reconciliation_not_configured"}, HTTPStatus.NOT_FOUND)
            return
        if self.headers.get("X-Pantheon-Intent", "").strip() != "memory-reconcile":
            self._json({"error": "explicit_intent_required"}, HTTPStatus.FORBIDDEN)
            return
        content_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().casefold()
        if content_type != "application/json":
            self._json({"error": "application_json_required"}, HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
            return
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self._json({"error": "invalid_content_length"}, HTTPStatus.BAD_REQUEST)
            return
        if content_length < 0 or content_length > 8192:
            self._json({"error": "request_too_large"}, HTTPStatus.REQUEST_ENTITY_TOO_LARGE)
            return
        try:
            raw = self.rfile.read(content_length)
            body = json.loads(raw.decode("utf-8") or "{}")
        except (UnicodeError, json.JSONDecodeError):
            self._json({"error": "invalid_json"}, HTTPStatus.BAD_REQUEST)
            return
        if not isinstance(body, dict):
            self._json({"error": "json_object_required"}, HTTPStatus.BAD_REQUEST)
            return
        focus = body.get("focus", "")
        if not isinstance(focus, str):
            self._json({"error": "focus_must_be_string"}, HTTPStatus.BAD_REQUEST)
            return
        document_id = unquote(match.group(1))
        snapshot = (
            self.workspace_index.snapshot()
            if self.workspace_index is not None
            else scan_workspaces(self.roots, self.max_depth)
        )
        try:
            result = self.memory_reconciliation.reconcile(
                snapshot,
                document_id,
                focus=focus,
            )
        except ReconciliationResidencyError as exc:
            self._json(
                {"error": "memory_reconciliation_residency_failure", "detail": str(exc)},
                HTTPStatus.BAD_GATEWAY,
            )
            return
        except ReconciliationError as exc:
            self._json(
                {"error": "memory_reconciliation_failed", "detail": str(exc)},
                HTTPStatus.CONFLICT,
            )
            return
        self._json(result, HTTPStatus.OK)

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlparse(self.path).path
        if path == "/api/health":
            index_state = self.workspace_index.health() if self.workspace_index else {"mode": "direct-scan"}
            self._json(
                {
                    "status": "ok",
                    "projection": PROJECTION_ID,
                    "read_only": True,
                    "role_trace": bool(self.role_trace_url),
                    "memory_reconciliation": self.memory_reconciliation is not None,
                    "index": index_state,
                }
            )
            return
        if path == "/api/workspaces":
            if self.workspace_index:
                self._json(self.workspace_index.snapshot())
            else:
                self._json(scan_workspaces(self.roots, self.max_depth))
            return
        if path == "/api/role-traces/latest":
            self._proxy_role_trace("/internal/role-traces/latest")
            return
        role_match = re.fullmatch(r"/api/role-traces/(run_[A-Za-z0-9]{8,128})(/events)?", path)
        if role_match:
            run_id, suffix = role_match.groups()
            self._proxy_role_trace(
                f"/internal/role-traces/{run_id}{suffix or ''}",
                stream=suffix == "/events",
            )
            return
        asset = {"/": "index.html", "/app.js": "app.js", "/styles.css": "styles.css"}.get(path)
        if not asset:
            self._json({"error": "not_found"}, HTTPStatus.NOT_FOUND)
            return
        target = STATIC_ROOT / asset
        try:
            body = target.read_bytes()
        except OSError:
            self._json({"error": "asset_unavailable"}, HTTPStatus.INTERNAL_SERVER_ERROR)
            return
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        if content_type.startswith("text/") or content_type == "application/javascript":
            content_type += "; charset=utf-8"
        self._headers(HTTPStatus.OK, content_type)
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None:
        print(f"workspace-cockpit: {self.address_string()} {format % args}", file=sys.stderr)


def _root(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("expected NAME=/absolute/path")
    name, raw_path = value.split("=", 1)
    path = Path(raw_path)
    if not name.strip() or not path.is_absolute():
        raise argparse.ArgumentTypeError("expected NAME=/absolute/path")
    return name.strip(), path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8189)
    parser.add_argument("--root", action="append", type=_root, required=True)
    parser.add_argument("--max-depth", type=int, default=2, choices=range(1, 5))
    parser.add_argument(
        "--state-db",
        default=os.getenv("WORKSPACE_INDEX_DB", "/tmp/pantheon-workspace-cockpit/index.sqlite3"),
        help="absolute path to reconstructible SQLite index state",
    )
    parser.add_argument(
        "--reconcile-seconds",
        type=float,
        default=float(os.getenv("WORKSPACE_RECONCILE_SECONDS", "60")),
        help="periodic full reconcile interval (default 60s)",
    )
    parser.add_argument(
        "--watch-debounce-ms",
        type=int,
        default=int(os.getenv("WORKSPACE_WATCH_DEBOUNCE_MS", "500")),
        help="coalesce filesystem event bursts before reconcile",
    )
    parser.add_argument("--no-watch", action="store_true", help="disable inotify acceleration; periodic reconcile remains")
    parser.add_argument(
        "--hindsight-url",
        default=os.getenv("WORKSPACE_HINDSIGHT_URL", ""),
        help="Hindsight base URL; producer stays disabled when omitted",
    )
    parser.add_argument(
        "--hindsight-bank-id",
        default=os.getenv("WORKSPACE_HINDSIGHT_BANK_ID", ""),
        help="target Hindsight bank id; required with --hindsight-url",
    )
    parser.add_argument(
        "--hindsight-parser",
        default=os.getenv("WORKSPACE_HINDSIGHT_PARSER", "markitdown"),
        help="file parser requested from Hindsight (default markitdown)",
    )
    parser.add_argument(
        "--hindsight-max-submits-per-reconcile",
        type=int,
        default=int(os.getenv("WORKSPACE_HINDSIGHT_MAX_SUBMITS_PER_RECONCILE", "4")),
        help="bound new Hindsight file submissions per reconcile",
    )
    parser.add_argument(
        "--hindsight-max-file-mb",
        type=int,
        default=int(os.getenv("WORKSPACE_HINDSIGHT_MAX_FILE_MB", "100")),
        help="reject a source before buffering it when larger than this many MiB",
    )
    parser.add_argument(
        "--reconcile-hermes-url",
        default=os.getenv("WORKSPACE_RECONCILE_HERMES_URL", ""),
        help="dedicated no-tool Hermes profile base URL for on-demand memory reconciliation",
    )
    parser.add_argument(
        "--reconcile-hermes-model",
        default=os.getenv("WORKSPACE_RECONCILE_HERMES_MODEL", ""),
        help="optional model/model-route override for the dedicated reconciliation profile",
    )
    parser.add_argument(
        "--reconcile-max-context-chars",
        type=int,
        default=int(os.getenv("WORKSPACE_RECONCILE_MAX_CONTEXT_CHARS", "48000")),
        help="maximum serialized Hindsight/cartouche context sent to Hermes",
    )
    parser.add_argument("--check", action="store_true", help="scan once, print summary, and exit")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.check:
        result = scan_workspaces(args.root, args.max_depth)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if all(workspace["available"] for workspace in result["workspaces"]) else 1
    state_db = Path(args.state_db)
    if not state_db.is_absolute():
        raise SystemExit("--state-db must be an absolute path")
    if args.reconcile_seconds < 0.1:
        raise SystemExit("--reconcile-seconds must be >= 0.1")
    if args.watch_debounce_ms < 0:
        raise SystemExit("--watch-debounce-ms must be >= 0")
    if args.hindsight_max_submits_per_reconcile < 1:
        raise SystemExit("--hindsight-max-submits-per-reconcile must be >= 1")
    if args.hindsight_max_file_mb < 1:
        raise SystemExit("--hindsight-max-file-mb must be >= 1")
    if args.reconcile_max_context_chars < 8000:
        raise SystemExit("--reconcile-max-context-chars must be >= 8000")
    if bool(args.hindsight_url.strip()) != bool(args.hindsight_bank_id.strip()):
        raise SystemExit("--hindsight-url and --hindsight-bank-id must be configured together")
    if any(_path_is_within(state_db, root) for _, root in args.root):
        raise SystemExit("--state-db must remain outside every watched workspace root")

    producer: HindsightProducer | None = None
    hindsight_client: HindsightHTTPClient | None = None
    if args.hindsight_url.strip():
        hindsight_client = HindsightHTTPClient(
            args.hindsight_url.strip(),
            args.hindsight_bank_id.strip(),
            authorization=os.getenv("WORKSPACE_HINDSIGHT_AUTHORIZATION", "").strip(),
            timeout_seconds=float(os.getenv("WORKSPACE_HINDSIGHT_TIMEOUT_SECONDS", "30")),
            parser=args.hindsight_parser,
            max_file_bytes=args.hindsight_max_file_mb * 1024 * 1024,
        )
        producer = HindsightProducer(
            roots=args.root,
            state_db=state_db,
            client=hindsight_client,
            max_submits_per_reconcile=args.hindsight_max_submits_per_reconcile,
        )

    reconcile_hermes_url = args.reconcile_hermes_url.strip().rstrip("/")
    reconcile_hermes_key = os.getenv("WORKSPACE_RECONCILE_HERMES_KEY", "").strip()
    if bool(reconcile_hermes_url) != bool(reconcile_hermes_key):
        raise SystemExit(
            "WORKSPACE_RECONCILE_HERMES_URL and WORKSPACE_RECONCILE_HERMES_KEY must be configured together"
        )
    if reconcile_hermes_url and hindsight_client is None:
        raise SystemExit("memory reconciliation requires the configured Hindsight producer/client")
    if reconcile_hermes_url and not reconcile_hermes_url.startswith(("http://", "https://")):
        raise SystemExit("WORKSPACE_RECONCILE_HERMES_URL must be HTTP(S)")

    CockpitHandler.roots = args.root
    CockpitHandler.max_depth = args.max_depth
    CockpitHandler.memory_reconciliation = None
    if reconcile_hermes_url and hindsight_client is not None:
        CockpitHandler.memory_reconciliation = MemoryReconciliationService(
            hindsight_client=hindsight_client,
            hermes_client=HermesReconciliationClient(
                reconcile_hermes_url,
                reconcile_hermes_key,
                model=args.reconcile_hermes_model,
                timeout_seconds=float(os.getenv("WORKSPACE_RECONCILE_HERMES_TIMEOUT_SECONDS", "120")),
            ),
            max_context_chars=args.reconcile_max_context_chars,
        )

    workspace_index = WorkspaceIndex(
        args.root,
        args.max_depth,
        state_db,
        reconcile_seconds=args.reconcile_seconds,
        debounce_seconds=args.watch_debounce_ms / 1000.0,
        enable_watcher=not args.no_watch,
        producer=producer,
    )
    workspace_index.start()
    CockpitHandler.workspace_index = workspace_index

    role_trace_url = os.getenv("WORKSPACE_ROLE_TRACE_URL", "").strip().rstrip("/")
    role_trace_key = os.getenv("WORKSPACE_ROLE_TRACE_KEY", "").strip()
    if bool(role_trace_url) != bool(role_trace_key):
        raise SystemExit("WORKSPACE_ROLE_TRACE_URL and WORKSPACE_ROLE_TRACE_KEY must be configured together")
    if role_trace_url and not role_trace_url.startswith(("http://", "https://")):
        raise SystemExit("WORKSPACE_ROLE_TRACE_URL must be HTTP(S)")
    CockpitHandler.role_trace_url = role_trace_url
    CockpitHandler.role_trace_key = role_trace_key
    server = ThreadingHTTPServer((args.host, args.port), CockpitHandler)
    print(f"workspace-cockpit listening on http://{args.host}:{args.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        workspace_index.stop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
