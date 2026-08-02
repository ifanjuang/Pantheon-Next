#!/usr/bin/env python3
"""Inventory Python modules and surface architecture cleanup candidates.

This tool is deliberately report-only. It never edits, renames or deletes code.
It gives maintainers a deterministic view of modules, imports, public symbols,
FastAPI routes and generation-named paths before any structural refactor.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCAN_ROOTS = ("mvp_vertical", "openwebui", "scripts", "tools")
EXCLUDED_PARTS = {".git", ".pytest_cache", ".venv", "venv", "__pycache__"}
_VERSION_TOKEN = re.compile(r"(?:^|[_./-])v(?:1|2|3)(?:$|[_./-])", re.IGNORECASE)
_ROUTE_DECORATORS = {"get", "post", "put", "patch", "delete", "options", "head"}


@dataclass(frozen=True)
class ModuleRecord:
    path: str
    module: str
    lines: int
    imports: tuple[str, ...]
    public_symbols: tuple[str, ...]
    routes: tuple[str, ...]
    version_named: bool
    parse_error: str | None = None


def iter_python_files(root: Path, scan_roots: Iterable[str] = DEFAULT_SCAN_ROOTS) -> list[Path]:
    files: list[Path] = []
    for relative in scan_roots:
        base = root / relative
        if not base.exists():
            continue
        for path in base.rglob("*.py"):
            if not any(part in EXCLUDED_PARTS for part in path.parts):
                files.append(path)
    return sorted(files)


def module_name(root: Path, path: Path) -> str:
    relative = path.relative_to(root).with_suffix("")
    parts = list(relative.parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def _import_name(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Import):
        return [alias.name for alias in node.names]
    if isinstance(node, ast.ImportFrom):
        prefix = "." * node.level
        return [prefix + (node.module or "")]
    return []


def _route(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    for decorator in node.decorator_list:
        if not isinstance(decorator, ast.Call) or not isinstance(decorator.func, ast.Attribute):
            continue
        if decorator.func.attr.lower() not in _ROUTE_DECORATORS or not decorator.args:
            continue
        first = decorator.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            return f"{decorator.func.attr.upper()} {first.value}"
    return None


def inspect_file(root: Path, path: Path) -> ModuleRecord:
    text = path.read_text(encoding="utf-8")
    relative = path.relative_to(root).as_posix()
    try:
        tree = ast.parse(text, filename=relative)
    except SyntaxError as exc:
        return ModuleRecord(
            path=relative,
            module=module_name(root, path),
            lines=len(text.splitlines()),
            imports=(),
            public_symbols=(),
            routes=(),
            version_named=bool(_VERSION_TOKEN.search(relative)),
            parse_error=f"{exc.msg} at line {exc.lineno}",
        )

    imports: set[str] = set()
    symbols: set[str] = set()
    routes: set[str] = set()
    for node in ast.walk(tree):
        imports.update(name for name in _import_name(node) if name)
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.name.startswith("_"):
                symbols.add(node.name)
            route = _route(node)
            if route:
                routes.add(route)

    return ModuleRecord(
        path=relative,
        module=module_name(root, path),
        lines=len(text.splitlines()),
        imports=tuple(sorted(imports)),
        public_symbols=tuple(sorted(symbols)),
        routes=tuple(sorted(routes)),
        version_named=bool(_VERSION_TOKEN.search(relative)),
    )


def build_inventory(root: Path = ROOT) -> list[ModuleRecord]:
    return [inspect_file(root, path) for path in iter_python_files(root)]


def incoming_import_counts(records: Iterable[ModuleRecord]) -> dict[str, int]:
    modules = {record.module for record in records}
    counts = {module: 0 for module in modules}
    for record in records:
        for imported in record.imports:
            normalized = imported.lstrip(".")
            for module in modules:
                if normalized == module or normalized.startswith(module + "."):
                    counts[module] += 1
    return counts


def render_markdown(records: list[ModuleRecord]) -> str:
    incoming = incoming_import_counts(records)
    total_lines = sum(record.lines for record in records)
    version_named = [record for record in records if record.version_named]
    parse_errors = [record for record in records if record.parse_error]
    orphan_candidates = [
        record for record in records
        if incoming.get(record.module, 0) == 0
        and not record.routes
        and not record.path.startswith("scripts/")
        and not record.path.startswith("tools/")
        and not record.path.endswith("/__init__.py")
    ]

    lines = [
        "# Python architecture inventory",
        "",
        "> Generated by `python tools/audit_python_architecture.py --format markdown`.",
        "> Report-only: an orphan candidate is not proof that a module is unused.",
        "",
        "## Summary",
        "",
        f"- Python modules: **{len(records)}**",
        f"- Python lines: **{total_lines}**",
        f"- FastAPI route declarations: **{sum(len(record.routes) for record in records)}**",
        f"- Generation-named paths: **{len(version_named)}**",
        f"- Modules without detected incoming imports or routes: **{len(orphan_candidates)}**",
        f"- Parse errors: **{len(parse_errors)}**",
        "",
        "## Generation-named paths",
        "",
    ]
    lines.extend(f"- `{record.path}`" for record in version_named)
    if not version_named:
        lines.append("None detected.")

    lines.extend(["", "## Review candidates", ""])
    lines.extend(
        f"- `{record.path}` — {record.lines} lines, no detected incoming import or route"
        for record in sorted(orphan_candidates, key=lambda item: (-item.lines, item.path))
    )
    if not orphan_candidates:
        lines.append("None detected.")

    lines.extend(["", "## Modules", ""])
    for record in records:
        details = [f"{record.lines} lines", f"{incoming.get(record.module, 0)} incoming imports"]
        if record.routes:
            details.append(f"{len(record.routes)} routes")
        if record.parse_error:
            details.append(f"parse error: {record.parse_error}")
        lines.append(f"- `{record.path}` — " + ", ".join(details))
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--fail-on-version-names",
        action="store_true",
        help="return 1 when a Python path contains a generation token v1, v2 or v3",
    )
    args = parser.parse_args()

    records = build_inventory(args.root.resolve())
    if args.format == "json":
        rendered = json.dumps([asdict(record) for record in records], indent=2, sort_keys=True) + "\n"
    else:
        rendered = render_markdown(records)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    if any(record.parse_error for record in records):
        return 2
    if args.fail_on_version_names and any(record.version_named for record in records):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
