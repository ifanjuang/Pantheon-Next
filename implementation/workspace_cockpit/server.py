#!/usr/bin/env python3
"""Read-only Cockpit projection for AFFAIRES source + Markdown cartouche bundles."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import os
from pathlib import Path
import re
import sys
from typing import Any, Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

import yaml


APP_ROOT = Path(__file__).resolve().parent
STATIC_ROOT = APP_ROOT / "static"
PROJECTION_ID = "affaires_source_cartouche_v1"
MARKDOWN_EXTENSIONS = {".md", ".markdown"}
LEGACY_MANIFEST_NAMES = {"document.yaml", "document.yml", "manifest.yaml", "manifest.yml"}
HINDSIGHT_ELIGIBLE_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".html", ".htm"}
HEAVY_VISIBLE_EXTENSIONS = {".rvt", ".rfa", ".rte", ".psd", ".psb"}
TEMP_SUFFIXES = {".bak", ".lock", ".lck", ".swp", ".tmp", ".temp", ".autosave"}
MAX_CARTOUCHE_BYTES = 512 * 1024
MAX_ITEMS = 10_000
STATUS_NAMES = ("COMPLETE", "CHECK", "CARTOUCHE_MISSING", "SOURCE_MISSING", "FOLDER")


def _visible(path: Path) -> bool:
    return not path.name.startswith(".") and not path.is_symlink()


def _direct_files(path: Path) -> list[Path]:
    try:
        return sorted(
            (item for item in path.iterdir() if item.is_file() and _visible(item)),
            key=lambda item: item.name.casefold(),
        )
    except OSError:
        return []


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
    if path.suffix.casefold() in MARKDOWN_EXTENSIONS:
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
    return None


def _meta_tags(metadata: dict[str, Any]) -> list[str]:
    value = metadata.get("tags")
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    if isinstance(value, list):
        return [str(item).strip() for item in value if isinstance(item, (str, int, float)) and str(item).strip()]
    return []


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
    try:
        size = source.stat().st_size
    except OSError:
        size = None

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
            "tags": [],
            "extension": extension.removeprefix(".").upper() or "FILE",
            "source_size": size,
            "hindsight_eligible": extension in HINDSIGHT_ELIGIBLE_EXTENSIONS,
            "heavy_binary": extension in HEAVY_VISIBLE_EXTENSIONS,
            "modified_at": _mtime_iso(source),
            "warnings": [],
        }

    metadata, body, cartouche_error = _read_cartouche(cartouche)
    warnings: list[str] = []
    if cartouche_error:
        warnings.append(cartouche_error)

    declared, source_ref_error = _safe_source_ref(_meta_string(metadata, "source"))
    if source_ref_error:
        warnings.append(source_ref_error)
    elif declared is None:
        warnings.append("Source non déclarée dans le cartouche")
    elif declared.casefold() != source.name.casefold():
        warnings.append(f"Source déclarée différente du fichier apparié : {declared}")

    document_id = _meta_string(metadata, "document_id")
    if not document_id:
        warnings.append("document_id absent du cartouche")

    title = _meta_string(metadata, "title") or _first_heading(body) or source.stem
    status = "CHECK" if warnings else "COMPLETE"
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
        "tags": _meta_tags(metadata),
        "extension": extension.removeprefix(".").upper() or "FILE",
        "source_size": size,
        "hindsight_eligible": extension in HINDSIGHT_ELIGIBLE_EXTENSIONS,
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

    title = _meta_string(metadata, "title") or _first_heading(body) or cartouche.stem
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
        "tags": _meta_tags(metadata),
        "extension": source_path.suffix.removeprefix(".").upper() if source_path else None,
        "source_size": source_path.stat().st_size if source_path else None,
        "hindsight_eligible": bool(source_path and source_path.suffix.casefold() in HINDSIGHT_ELIGIBLE_EXTENSIONS),
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
    cartouches = [
        item
        for item in direct
        if item.suffix.casefold() in MARKDOWN_EXTENSIONS and item.name.casefold() != "_folder.md"
    ]
    cartouche_by_stem = {item.stem.casefold(): item for item in cartouches}

    cards: list[dict[str, Any]] = []
    paired_cartouches: set[Path] = set()
    for source in sources:
        cartouche = cartouche_by_stem.get(source.stem.casefold())
        if cartouche:
            paired_cartouches.add(cartouche)
        cards.append(_document_card(workspace, root, source, cartouche))

    for cartouche in cartouches:
        if cartouche not in paired_cartouches:
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
    totals = {status: 0 for status in STATUS_NAMES}
    total_items = 0
    document_count = 0
    folder_count = 0

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

            for card in candidates[:MAX_ITEMS]:
                cards.append(card)
                totals[card["status"]] = totals.get(card["status"], 0) + 1
                total_items += 1
                if card["kind"] == "folder":
                    folder_count += 1
                else:
                    document_count += 1

        workspaces.append({"name": label, "available": root_available, "cards": cards, "errors": errors})

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


class CockpitHandler(BaseHTTPRequestHandler):
    roots: list[tuple[str, Path]] = []
    max_depth = 2
    role_trace_url = ""
    role_trace_key = ""

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

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlparse(self.path).path
        if path == "/api/health":
            self._json({"status": "ok", "read_only": True, "role_trace": bool(self.role_trace_url)})
            return
        if path == "/api/workspaces":
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
    parser.add_argument("--check", action="store_true", help="scan once, print summary, and exit")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.check:
        result = scan_workspaces(args.root, args.max_depth)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if all(workspace["available"] for workspace in result["workspaces"]) else 1
    CockpitHandler.roots = args.root
    CockpitHandler.max_depth = args.max_depth
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
