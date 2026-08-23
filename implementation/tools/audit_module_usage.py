#!/usr/bin/env python3
"""Build a report-only Python module usage inventory for Pantheon repositories.

The report corrects a known limitation of the broad architecture inventory: Python
relative imports such as ``from . import agency_directory`` and
``from .app_lifecycle import install`` must be resolved against the importing
package before a module can be described as unreferenced.

A ``candidate_unreferenced`` result is not deletion proof. It is reserved for an
implementation module for which no static Python importer, route, main entry,
package entry, dynamic module reference or non-historical configuration reference
was found. Runtime/deployment review and an explicit human decision remain required
before removal.

Test modules and tooling are classified separately. A test file is not dead code
because no other test imports it, and an unreferenced maintenance script requires
an operational review rather than automatic deletion.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable

PYTHON_EXCLUDED_PARTS = {
    ".git",
    ".pytest_cache",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}
TEXT_REFERENCE_SUFFIXES = {".toml", ".yaml", ".yml", ".json", ".sh"}
ROUTE_METHODS = {"get", "post", "put", "patch", "delete", "options", "head"}
HISTORICAL_PARTS = {"ai_logs", "archive", "archives", "history"}
REFERENCE_PARTS = {"vendor", "vendored"}


@dataclass(frozen=True)
class RepositorySpec:
    name: str
    role: str
    root: Path


@dataclass
class ModuleRecord:
    repository: str
    repository_role: str
    module: str
    path: str
    posture: str
    imports: list[str] = field(default_factory=list)
    imported_by_runtime: list[str] = field(default_factory=list)
    imported_by_tests: list[str] = field(default_factory=list)
    config_references: list[str] = field(default_factory=list)
    dynamic_references: list[str] = field(default_factory=list)
    route_count: int = 0
    has_main: bool = False
    package_entry: bool = False
    parse_error: str | None = None
    usage_state: str = "unknown"
    removal_candidate: bool = False
    limits: list[str] = field(default_factory=list)


def repository_spec(value: str) -> RepositorySpec:
    try:
        name, role, raw_root = value.split("=", 2)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected NAME=ROLE=PATH") from exc
    root = Path(raw_root).expanduser().resolve()
    if not root.is_dir():
        raise argparse.ArgumentTypeError(f"repository root does not exist: {root}")
    return RepositorySpec(name=name, role=role, root=root)


def _iter_python(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.py")
        if path.is_file()
        and not any(part in PYTHON_EXCLUDED_PARTS for part in path.parts)
    )


def _module_name(root: Path, path: Path) -> str:
    parts = list(path.relative_to(root).with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def _posture(root: Path, path: Path) -> str:
    relative = path.relative_to(root)
    parts = {part.lower() for part in relative.parts}
    if parts & HISTORICAL_PARTS:
        return "history"
    if parts & REFERENCE_PARTS:
        return "reference"
    if "tests" in parts or path.name.startswith("test_"):
        return "test"
    if "migrations" in parts:
        return "migration"
    if "tools" in parts or "scripts" in parts or ".github" in parts:
        return "tooling"
    return "implementation"


def _package_for(module: str, path: Path) -> str:
    if path.name == "__init__.py":
        return module
    return module.rsplit(".", 1)[0] if "." in module else ""


def _relative_base(package: str, level: int, module: str | None) -> str:
    parts = package.split(".") if package else []
    climb = max(level - 1, 0)
    if climb > len(parts):
        return module or ""
    prefix = parts[: len(parts) - climb] if climb else parts
    if module:
        prefix.extend(module.split("."))
    return ".".join(part for part in prefix if part)


def _call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def _string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _inspect_python(
    root: Path,
    path: Path,
) -> tuple[list[str], int, bool, list[str], str | None]:
    module = _module_name(root, path)
    package = _package_for(module, path)
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, UnicodeError, SyntaxError) as exc:
        return [], 0, False, [], str(exc)

    imports: set[str] = set()
    dynamic: set[str] = set()
    routes = 0
    has_main = path.name == "__main__.py"

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = _relative_base(package, node.level, node.module)
            else:
                base = node.module or ""
            if node.module:
                if base:
                    imports.add(base)
            else:
                for alias in node.names:
                    if alias.name != "*":
                        imports.add(
                            ".".join(part for part in (base, alias.name) if part)
                        )
        elif isinstance(node, ast.If):
            if (
                isinstance(node.test, ast.Compare)
                and isinstance(node.test.left, ast.Name)
                and node.test.left.id == "__name__"
                and any(
                    _string(item) == "__main__" for item in node.test.comparators
                )
            ):
                has_main = True
        elif isinstance(node, ast.Call):
            name = _call_name(node.func)
            if (
                name in ROUTE_METHODS
                and node.args
                and _string(node.args[0]) is not None
            ):
                routes += 1
            if name in {"import_module", "find_spec"} and node.args:
                value = _string(node.args[0])
                if value:
                    dynamic.add(value)
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            value = node.value.strip()
            if re.fullmatch(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)+", value):
                dynamic.add(value)

    return sorted(imports), routes, has_main, sorted(dynamic), None


def _local_targets(imported: str, local_modules: set[str]) -> set[str]:
    return {
        module
        for module in local_modules
        if imported == module or imported.startswith(module + ".")
    }


def _configuration_references(
    spec: RepositorySpec,
    path_by_module: dict[str, Path],
) -> dict[str, list[str]]:
    references: dict[str, list[str]] = defaultdict(list)
    needles: dict[str, tuple[str, ...]] = {}
    for module, python_path in path_by_module.items():
        relative = python_path.relative_to(spec.root).as_posix()
        without_suffix = relative.removesuffix(".py")
        needles[module] = tuple(
            value
            for value in {
                module,
                relative,
                without_suffix,
                module.replace(".", "/") + ".py",
            }
            if value
        )

    for path in sorted(spec.root.rglob("*")):
        if (
            not path.is_file()
            or path.suffix.lower() not in TEXT_REFERENCE_SUFFIXES
            or any(part in PYTHON_EXCLUDED_PARTS for part in path.parts)
            or {part.lower() for part in path.parts} & HISTORICAL_PARTS
        ):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        relative = path.relative_to(spec.root).as_posix()
        for module, module_needles in needles.items():
            for needle in module_needles:
                if "/" in needle:
                    found = needle in text
                else:
                    found = bool(
                        re.search(
                            rf"(?<![\w.]){re.escape(needle)}(?![\w.])",
                            text,
                        )
                    )
                if found:
                    references[module].append(relative)
                    break
    return references


def inspect_repository(spec: RepositorySpec) -> list[ModuleRecord]:
    paths = _iter_python(spec.root)
    path_by_module = {_module_name(spec.root, path): path for path in paths}
    local_modules = {module for module in path_by_module if module}
    records: dict[str, ModuleRecord] = {}
    imports_by_module: dict[str, list[str]] = {}
    dynamic_by_module: dict[str, list[str]] = {}

    for module, path in path_by_module.items():
        imports, route_count, has_main, dynamic, parse_error = _inspect_python(
            spec.root, path
        )
        relative = path.relative_to(spec.root).as_posix()
        records[module] = ModuleRecord(
            repository=spec.name,
            repository_role=spec.role,
            module=module,
            path=relative,
            posture=_posture(spec.root, path),
            imports=imports,
            route_count=route_count,
            has_main=has_main,
            package_entry=path.name in {"__main__.py", "setup.py"},
            parse_error=parse_error,
            limits=[
                "static usage evidence != runtime deployment proof",
                "candidate_unreferenced != deletion authorization",
            ],
        )
        imports_by_module[module] = imports
        dynamic_by_module[module] = dynamic

    for importer, imported_names in imports_by_module.items():
        importer_record = records[importer]
        for imported in imported_names:
            for target in _local_targets(imported, local_modules):
                target_record = records[target]
                if importer_record.posture == "test":
                    target_record.imported_by_tests.append(importer)
                else:
                    target_record.imported_by_runtime.append(importer)

    for importer, referenced_names in dynamic_by_module.items():
        for referenced in referenced_names:
            for target in _local_targets(referenced, local_modules):
                records[target].dynamic_references.append(importer)

    config = _configuration_references(spec, path_by_module)
    for module, paths_for_module in config.items():
        records[module].config_references.extend(paths_for_module)

    for module, record in records.items():
        path = path_by_module[module]
        if path.name == "__init__.py":
            record.usage_state = "package_initializer"
        elif record.parse_error:
            record.usage_state = "parse_error"
        elif record.posture == "test":
            record.usage_state = "test_module"
        elif record.route_count or record.has_main or record.package_entry:
            record.usage_state = "active_entrypoint"
        elif record.imported_by_runtime:
            record.usage_state = "active_imported"
        elif record.dynamic_references or record.config_references:
            record.usage_state = "active_dynamic_or_configured"
        elif record.imported_by_tests:
            record.usage_state = "test_only"
        elif record.posture in {"history", "reference", "migration"}:
            record.usage_state = record.posture
        elif record.posture == "tooling":
            record.usage_state = "tooling_unreferenced_review"
        else:
            record.usage_state = "candidate_unreferenced"
            record.removal_candidate = True

        record.imported_by_runtime = sorted(set(record.imported_by_runtime))
        record.imported_by_tests = sorted(set(record.imported_by_tests))
        record.dynamic_references = sorted(set(record.dynamic_references))
        record.config_references = sorted(set(record.config_references))

    return sorted(records.values(), key=lambda item: item.path)


def render_markdown(
    specs: list[RepositorySpec],
    records: list[ModuleRecord],
) -> str:
    counts: dict[str, int] = defaultdict(int)
    for record in records:
        counts[record.usage_state] += 1
    candidates = [record for record in records if record.removal_candidate]
    test_only = [record for record in records if record.usage_state == "test_only"]
    tooling_review = [
        record
        for record in records
        if record.usage_state == "tooling_unreferenced_review"
    ]

    lines = [
        "# Pantheon Python module usage inventory",
        "",
        "> Report-only: static usage evidence is not deletion proof or an authority decision.",
        "",
        "## Repositories",
        "",
    ]
    lines.extend(
        f"- **{spec.name}** — {spec.role} — `{spec.root}`" for spec in specs
    )
    lines.extend(["", "## Summary", ""])
    lines.extend(
        f"- {state}: **{count}**" for state, count in sorted(counts.items())
    )
    lines.extend(["", "## Candidate unreferenced implementation modules", ""])
    if not candidates:
        lines.append("None detected.")
    for record in candidates:
        lines.append(f"- `{record.repository}:{record.path}` (`{record.module}`)")

    lines.extend(["", "## Test-only implementation modules", ""])
    if not test_only:
        lines.append("None detected.")
    for record in test_only:
        lines.append(
            f"- `{record.repository}:{record.path}` — imported by "
            + ", ".join(f"`{item}`" for item in record.imported_by_tests)
        )

    lines.extend(["", "## Tooling requiring operational review", ""])
    if not tooling_review:
        lines.append("None detected.")
    for record in tooling_review:
        lines.append(f"- `{record.repository}:{record.path}` (`{record.module}`)")

    lines.extend(
        [
            "",
            "## Review rule",
            "",
            "A module may be removed only after runtime/deployment references are checked, its consumers are proven absent, the change passes full CI, and an explicit human decision reviews the removal. A candidate state alone never authorizes deletion.",
        ]
    )
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repository",
        action="append",
        type=repository_spec,
        required=True,
        help="NAME=ROLE=PATH (repeatable)",
    )
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--markdown-output", type=Path, required=True)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    records = [
        record
        for spec in args.repository
        for record in inspect_repository(spec)
    ]
    payload = {
        "schema_id": "pantheon.module_usage_inventory",
        "revision": 1,
        "repositories": [
            {"name": spec.name, "role": spec.role, "root": str(spec.root)}
            for spec in args.repository
        ],
        "summary": {
            "modules": len(records),
            "candidate_unreferenced": sum(
                item.removal_candidate for item in records
            ),
            "test_only": sum(
                item.usage_state == "test_only" for item in records
            ),
            "test_modules": sum(
                item.usage_state == "test_module" for item in records
            ),
            "tooling_unreferenced_review": sum(
                item.usage_state == "tooling_unreferenced_review"
                for item in records
            ),
        },
        "modules": [asdict(record) for record in records],
        "limits": [
            "static usage evidence != runtime deployment proof",
            "candidate_unreferenced != deletion authorization",
            "tooling reference absence != deletion authorization",
            "CI success != semantic or operational authority",
        ],
    }
    args.json_output.parent.mkdir(parents=True, exist_ok=True)
    args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
    args.json_output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.markdown_output.write_text(
        render_markdown(args.repository, records),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
