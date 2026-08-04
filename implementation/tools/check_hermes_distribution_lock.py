#!/usr/bin/env python3
"""Validate one Hermes distribution lock against Pantheon-Next and local artifacts.

The lock is a reproducible composition record. Validation proves schema and path
consistency only; it does not install components, activate a binding, authorize a
task, dispatch a run, accept a result or admit Evidence.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

import jsonschema
import yaml


REQUIRED_COMPONENT_KINDS = {"run_binding", "context_bridge", "runtime_observer"}
REQUIRED_CHECK_KINDS = {
    "static_structure",
    "route_contract",
    "end_to_end",
    "no_authority",
}


class DistributionLockError(ValueError):
    pass


def _mapping(path: Path, *, label: str) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise DistributionLockError(f"cannot read {label}: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise DistributionLockError(f"{label} must be an object")
    return value


def _repository(value: str) -> tuple[str, Path]:
    try:
        name, raw_path = value.split("=", 1)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("repository must be NAME=PATH") from exc
    path = Path(raw_path).resolve()
    if not path.is_dir():
        raise argparse.ArgumentTypeError(f"repository root does not exist: {path}")
    return name, path


def evaluate(
    manifest: dict[str, Any],
    *,
    repository_roots: dict[str, Path],
) -> list[str]:
    errors: list[str] = []
    components = manifest.get("components") or []
    component_ids: set[str] = set()
    observed_kinds: set[str] = set()

    for index, component in enumerate(components):
        if not isinstance(component, dict):
            errors.append(f"components[{index}] must be an object")
            continue
        component_id = str(component.get("component_id") or "")
        if component_id in component_ids:
            errors.append(f"duplicate component_id: {component_id}")
        component_ids.add(component_id)
        observed_kinds.add(str(component.get("kind") or ""))

        repository = str(component.get("source_repository") or "")
        root = repository_roots.get(repository)
        if root is None:
            errors.append(f"component {component_id} has no repository root: {repository}")
            continue
        relative = str(component.get("path") or "")
        target = (root / relative).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            errors.append(f"component {component_id} escapes repository root")
            continue
        if not target.exists():
            errors.append(f"component path does not exist: {repository}:{relative}")
        if component.get("enabled_by_default") is not False:
            errors.append(f"component must remain default-off: {component_id}")

    missing_kinds = sorted(REQUIRED_COMPONENT_KINDS - observed_kinds)
    if missing_kinds:
        errors.append("missing required component kinds: " + ", ".join(missing_kinds))

    checks = manifest.get("required_checks") or []
    check_kinds = {
        str(item.get("kind") or "")
        for item in checks
        if isinstance(item, dict) and item.get("required") is True
    }
    missing_checks = sorted(REQUIRED_CHECK_KINDS - check_kinds)
    if missing_checks:
        errors.append("missing required check kinds: " + ", ".join(missing_checks))

    state = manifest.get("state") or {}
    if state.get("activation_state") != "not_activated":
        errors.append("distribution lock must not activate a binding")
    if state.get("task_authorization_state") != "not_authorized":
        errors.append("distribution lock must not authorize a task")

    authority = manifest.get("authority") or {}
    enabled_authority = sorted(key for key, value in authority.items() if value is not False)
    if enabled_authority:
        errors.append("distribution lock claims authority: " + ", ".join(enabled_authority))

    return errors


def _route_contract(manifest: dict[str, Any], roots: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    by_kind = {
        item["kind"]: roots[item["source_repository"]] / item["path"]
        for item in manifest.get("components") or []
        if isinstance(item, dict)
        and item.get("kind") in {"run_binding", "context_bridge"}
        and item.get("source_repository") in roots
    }

    run_binding = by_kind.get("run_binding")
    if run_binding and run_binding.is_file():
        source = run_binding.read_text(encoding="utf-8")
        required = {
            "/hermes/execution-admissions/{admission_id}/launch-reservations",
            "/hermes/execution-admissions/{admission_id}/runs/start",
            "/hermes/execution-admissions/{admission_id}/runs/{run_id}/return",
            '"/v1/runs"',
        }
        for marker in required:
            if marker not in source:
                errors.append(f"run binding is missing route marker: {marker}")
        if "/v1/hermes/" in source:
            errors.append("run binding reintroduces retired internal /v1/hermes routes")

    bridge = by_kind.get("context_bridge")
    bridge_tools = bridge / "tools.py" if bridge and bridge.is_dir() else None
    if bridge_tools and bridge_tools.is_file():
        source = bridge_tools.read_text(encoding="utf-8")
        if "/active-context" not in source or "/active-context/entities/" not in source:
            errors.append("context bridge is missing bounded active-context routes")
        if "/v1/hermes/" in source:
            errors.append("context bridge reintroduces retired internal /v1/hermes routes")
    else:
        errors.append("context bridge tools.py is missing")

    return errors


def validate(
    *,
    manifest_path: Path,
    schema_path: Path,
    repository_roots: dict[str, Path],
) -> dict[str, Any]:
    manifest = _mapping(manifest_path, label="distribution lock")
    schema = _mapping(schema_path, label="distribution lock schema")
    try:
        jsonschema.Draft202012Validator.check_schema(schema)
        jsonschema.Draft202012Validator(schema).validate(manifest)
    except jsonschema.SchemaError as exc:
        raise DistributionLockError(f"invalid distribution schema: {exc.message}") from exc
    except jsonschema.ValidationError as exc:
        path = ".".join(str(part) for part in exc.path) or "<root>"
        raise DistributionLockError(f"distribution lock validation failed at {path}: {exc.message}") from exc

    errors = evaluate(manifest, repository_roots=repository_roots)
    errors.extend(_route_contract(manifest, repository_roots))
    if errors:
        raise DistributionLockError("; ".join(errors))

    return {
        "schema_id": manifest["schema_id"],
        "distribution_id": manifest["distribution_id"],
        "status": manifest["status"],
        "component_count": len(manifest["components"]),
        "required_check_count": len(manifest["required_checks"]),
        "installation_state": manifest["state"]["installation_state"],
        "activation_state": manifest["state"]["activation_state"],
        "task_authorization_state": manifest["state"]["task_authorization_state"],
        "authority_effect": "none",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--repository", action="append", type=_repository, required=True)
    parser.add_argument("--output", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    roots = dict(args.repository)
    try:
        result = validate(
            manifest_path=args.manifest,
            schema_path=args.schema,
            repository_roots=roots,
        )
    except DistributionLockError as exc:
        print(f"Hermes distribution lock failed: {exc}")
        return 1

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
