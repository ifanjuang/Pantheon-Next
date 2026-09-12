#!/usr/bin/env python3
"""Read-only local Cockpit projection for LiveSync filesystem mirrors."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import os
from pathlib import Path
import sys
from typing import Any, Iterable
from urllib.parse import urlparse

import yaml


APP_ROOT = Path(__file__).resolve().parent
STATIC_ROOT = APP_ROOT / "static"
MANIFEST_NAMES = ("document.yaml", "document.yml", "manifest.yaml", "manifest.yml")
PACKAGE_CHILDREN = {"archives", "assets", "images", "tableaux", "tables", "annexes"}
MARKDOWN_EXTENSIONS = {".md", ".markdown"}
PDF_EXTENSIONS = {".pdf"}
IMAGE_EXTENSIONS = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".tif", ".tiff", ".webp"}
TABLE_EXTENSIONS = {".csv", ".ods", ".tsv", ".xls", ".xlsx"}
DOCUMENT_EXTENSIONS = MARKDOWN_EXTENSIONS | PDF_EXTENSIONS | IMAGE_EXTENSIONS | TABLE_EXTENSIONS | {
    ".doc",
    ".docx",
    ".dwg",
    ".dxf",
    ".ifc",
    ".odt",
    ".ppt",
    ".pptx",
}
MAX_MANIFEST_BYTES = 256 * 1024
MAX_FILES_PER_PACKAGE = 4_000
MAX_PACKAGES = 5_000


def _visible(path: Path) -> bool:
    return not path.name.startswith(".") and not path.is_symlink()


def _direct_files(path: Path) -> list[Path]:
    try:
        return [item for item in path.iterdir() if item.is_file() and _visible(item)]
    except OSError:
        return []


def _manifest_paths(path: Path) -> list[Path]:
    by_name = {item.name.casefold(): item for item in _direct_files(path)}
    return [by_name[name] for name in MANIFEST_NAMES if name in by_name]


def _same_named_markdown(path: Path) -> Path | None:
    expected = {f"{path.name}{suffix}".casefold() for suffix in MARKDOWN_EXTENSIONS}
    return next((item for item in _direct_files(path) if item.name.casefold() in expected), None)


def _read_manifest(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        if path.stat().st_size > MAX_MANIFEST_BYTES:
            return None, "Manifeste trop volumineux"
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError):
        return None, "Manifeste YAML illisible"
    if not isinstance(value, dict):
        return None, "Le manifeste doit contenir un objet YAML"
    return value, None


def _nested(mapping: dict[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _declared_file_exists(package: Path, declared: Any) -> bool:
    """Accept only regular files that remain inside their package directory."""
    if not isinstance(declared, str) or not declared.strip():
        return False
    candidate = package / declared
    try:
        if candidate.is_symlink():
            return False
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(package.resolve(strict=True))
        return resolved.is_file()
    except (OSError, RuntimeError, ValueError):
        return False


def _resource_counts(path: Path) -> tuple[dict[str, int], int, str | None, str | None]:
    counts = {"markdown": 0, "pdf": 0, "images": 0, "tables": 0, "other": 0}
    seen = 0
    newest = 0.0
    try:
        for directory, names, files in os.walk(path, followlinks=False):
            names[:] = [name for name in names if not name.startswith(".")]
            for name in files:
                if name.startswith("."):
                    continue
                seen += 1
                if seen > MAX_FILES_PER_PACKAGE:
                    return counts, seen - 1, None, "Inventaire limité aux 4 000 premiers fichiers"
                item = Path(directory) / name
                try:
                    if item.is_symlink():
                        continue
                    newest = max(newest, item.stat().st_mtime)
                except OSError:
                    continue
                suffix = item.suffix.casefold()
                if suffix in MARKDOWN_EXTENSIONS:
                    counts["markdown"] += 1
                elif suffix in PDF_EXTENSIONS:
                    counts["pdf"] += 1
                elif suffix in IMAGE_EXTENSIONS:
                    counts["images"] += 1
                elif suffix in TABLE_EXTENSIONS:
                    counts["tables"] += 1
                elif name.casefold() not in MANIFEST_NAMES:
                    counts["other"] += 1
    except OSError:
        return counts, seen, None, "Dossier partiellement illisible"
    modified = (
        datetime.fromtimestamp(newest, tz=timezone.utc).isoformat().replace("+00:00", "Z")
        if newest
        else None
    )
    return counts, seen, modified, None


def inspect_package(workspace: str, root: Path, path: Path) -> dict[str, Any]:
    manifests = _manifest_paths(path)
    manifest_data: dict[str, Any] = {}
    manifest_error = None
    if manifests:
        manifest_data, manifest_error = _read_manifest(manifests[0])
        manifest_data = manifest_data or {}

    primary = _same_named_markdown(path)
    direct_document_files = [item for item in _direct_files(path) if item.suffix.casefold() in DOCUMENT_EXTENSIONS]
    declared_markdown = _nested(manifest_data, "representation", "markdown", "file")
    declared_exists = _declared_file_exists(path, declared_markdown)

    warnings: list[str] = []
    if len(manifests) > 1:
        warnings.append("Plusieurs manifestes concurrents")
    if manifests and primary is None:
        warnings.append(f"Markdown principal attendu : {path.name}.md")
    if declared_markdown and not declared_exists:
        warnings.append("La représentation Markdown déclarée est introuvable")

    if manifest_error:
        status = "INVALID"
        warnings.append(manifest_error)
    elif manifests and primary and len(manifests) == 1:
        status = "COHERENT"
    elif manifests:
        status = "CHECK"
    elif primary or direct_document_files:
        status = "QUALIFIABLE"
    else:
        status = "FREE"

    counts, file_count, modified_at, inventory_note = _resource_counts(path)
    if inventory_note:
        warnings.append(inventory_note)
        if status == "COHERENT":
            status = "CHECK"

    full_name = _nested(manifest_data, "display", "full_name")
    family_id = _nested(manifest_data, "identity", "document_family_id")
    relative_path = path.relative_to(root).as_posix()
    return {
        "workspace": workspace,
        "path": relative_path,
        "name": path.name,
        "subtitle": full_name if isinstance(full_name, str) and full_name.strip() else "Dossier non qualifié",
        "status": status,
        "manifest": manifests[0].name if manifests else None,
        "primary_markdown": primary.name if primary else None,
        "declared_markdown": declared_markdown if isinstance(declared_markdown, str) else None,
        "document_family_id": family_id if isinstance(family_id, str) else None,
        "resources": counts,
        "file_count": file_count,
        "modified_at": modified_at,
        "warnings": warnings,
    }


def _iter_package_paths(root: Path, max_depth: int) -> Iterable[Path]:
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
            if child.name.casefold() in PACKAGE_CHILDREN:
                continue
            yield child
            is_boundary = bool(_manifest_paths(child) or _same_named_markdown(child))
            if not is_boundary and depth < max_depth:
                yield from visit(child, depth + 1)

    yield from visit(root, 1)


def scan_workspaces(roots: list[tuple[str, Path]], max_depth: int = 2) -> dict[str, Any]:
    workspaces: list[dict[str, Any]] = []
    totals = {status: 0 for status in ("COHERENT", "CHECK", "INVALID", "QUALIFIABLE", "FREE")}
    total_packages = 0
    for label, root in roots:
        cards: list[dict[str, Any]] = []
        errors: list[str] = []
        root_available = root.is_dir() and os.access(root, os.R_OK | os.X_OK)
        if not root_available:
            errors.append("Miroir local indisponible")
        else:
            try:
                for path in _iter_package_paths(root, max_depth):
                    if total_packages >= MAX_PACKAGES:
                        errors.append("Inventaire global limité à 5 000 dossiers")
                        break
                    card = inspect_package(label, root, path)
                    cards.append(card)
                    totals[card["status"]] += 1
                    total_packages += 1
            except OSError:
                errors.append("Lecture du miroir interrompue")
        workspaces.append({"name": label, "available": root_available, "cards": cards, "errors": errors})
    return {
        "generated_at": datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z"),
        "read_only": True,
        "totals": totals,
        "workspace_count": len(workspaces),
        "package_count": total_packages,
        "workspaces": workspaces,
    }


class CockpitHandler(BaseHTTPRequestHandler):
    roots: list[tuple[str, Path]] = []
    max_depth = 2

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

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        path = urlparse(self.path).path
        if path == "/api/health":
            self._json({"status": "ok", "read_only": True})
            return
        if path == "/api/workspaces":
            self._json(scan_workspaces(self.roots, self.max_depth))
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
