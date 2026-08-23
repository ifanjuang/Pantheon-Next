#!/usr/bin/env python3
"""Enforce permanent architecture-convergence invariants after debt closure.

This guard consumes the report-only architecture and module-usage inventories.
It replaces the temporary decreasing-debt baseline once the measured active debt
is zero. Passing the guard does not grant semantic authority, deletion
authorization or runtime approval.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


ACTIVE_GENERATION_EXCLUSIONS = {"history", "migration", "reference"}
VERSIONED_ROUTE_POSTURES = {"implementation", "projection"}


class ConvergenceClosureError(ValueError):
    pass


def _payload(path: Path, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConvergenceClosureError(f"cannot read {label}: {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ConvergenceClosureError(f"{label} must be a JSON object")
    return value


def _repositories(payload: dict[str, Any]) -> set[str]:
    output: set[str] = set()
    for item in payload.get("repositories") or []:
        if isinstance(item, dict) and item.get("name"):
            output.add(str(item["name"]))
    return output


def evaluate(
    architecture_inventory: dict[str, Any],
    module_usage: dict[str, Any],
    *,
    expected_repositories: Iterable[str] = (),
) -> list[str]:
    violations: list[str] = []
    expected = {str(item) for item in expected_repositories}
    observed_architecture = _repositories(architecture_inventory)
    observed_usage = _repositories(module_usage)
    for repository in sorted(expected):
        if repository not in observed_architecture:
            violations.append(
                f"architecture inventory is missing expected repository: {repository}"
            )
        if repository not in observed_usage:
            violations.append(
                f"module-usage inventory is missing expected repository: {repository}"
            )

    for artifact in architecture_inventory.get("artifacts") or []:
        if not isinstance(artifact, dict):
            continue
        ref = f"{artifact.get('repository', '?')}:{artifact.get('path', '?')}"
        posture = str(artifact.get("posture") or "")
        if (
            artifact.get("generation_named") is True
            and posture not in ACTIVE_GENERATION_EXCLUSIONS
        ):
            violations.append(f"generation-named active artifact: {ref}")
        if posture in VERSIONED_ROUTE_POSTURES:
            for route in artifact.get("versioned_routes") or []:
                violations.append(f"versioned internal route: {ref}: {route}")
        if artifact.get("parse_error"):
            violations.append(f"Python parse error: {ref}: {artifact['parse_error']}")

    for module in module_usage.get("modules") or []:
        if not isinstance(module, dict):
            continue
        ref = f"{module.get('repository', '?')}:{module.get('path', '?')}"
        if module.get("usage_state") == "candidate_unreferenced" or module.get(
            "removal_candidate"
        ) is True:
            violations.append(f"unreferenced implementation candidate: {ref}")
        if module.get("usage_state") == "parse_error" or module.get("parse_error"):
            violations.append(f"module parse error: {ref}: {module.get('parse_error')}")

    return violations


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--architecture-inventory", type=Path, required=True)
    parser.add_argument("--module-usage", type=Path, required=True)
    parser.add_argument("--expected-repository", action="append", default=[])
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        architecture_inventory = _payload(
            args.architecture_inventory,
            label="architecture inventory",
        )
        module_usage = _payload(args.module_usage, label="module-usage inventory")
        violations = evaluate(
            architecture_inventory,
            module_usage,
            expected_repositories=args.expected_repository,
        )
    except ConvergenceClosureError as exc:
        print(f"Architecture convergence closure guard failed: {exc}")
        return 1

    if violations:
        print("Architecture convergence closure guard failed:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print(
        "Architecture convergence closure guard passed: "
        "no generation-named active artifact, implementation/projection internal "
        "versioned route, parse error or unreferenced implementation candidate detected."
    )
    print(
        "Limits: historical references and retired-route tests remain auditable; "
        "guard success != semantic authority; zero candidates != deletion authorization."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
