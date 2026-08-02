#!/usr/bin/env python3
"""Check that Pantheon architecture debt only decreases from a reviewed baseline."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ACTIVE_GENERATION_EXCLUSIONS = {"history", "migration", "reference"}
VERSIONED_ROUTE_POSTURES = {"implementation", "projection"}


@dataclass(frozen=True)
class DebtSnapshot:
    generation_named_artifacts: tuple[str, ...]
    internal_versioned_routes: tuple[str, ...]


def _artifact_ref(artifact: dict[str, object]) -> str:
    return f"{artifact['repository']}:{artifact['path']}"


def _route_ref(artifact_ref: str, route: str) -> str:
    return f"{artifact_ref}::{route}"


def collect_debt(inventory: dict[str, object]) -> DebtSnapshot:
    generation: set[str] = set()
    routes: set[str] = set()
    artifacts = inventory.get("artifacts")
    if not isinstance(artifacts, list):
        raise ValueError("inventory must contain an artifacts list")

    for raw in artifacts:
        if not isinstance(raw, dict):
            raise ValueError("inventory artifact must be an object")
        ref = _artifact_ref(raw)
        posture = str(raw.get("posture", ""))
        if raw.get("generation_named") and posture not in ACTIVE_GENERATION_EXCLUSIONS:
            generation.add(ref)
        versioned_routes = raw.get("versioned_routes", [])
        if posture in VERSIONED_ROUTE_POSTURES:
            if not isinstance(versioned_routes, list):
                raise ValueError(f"versioned_routes must be a list for {ref}")
            routes.update(_route_ref(ref, str(route)) for route in versioned_routes)

    return DebtSnapshot(tuple(sorted(generation)), tuple(sorted(routes)))


def _decode_route_segments(value: object, *, artifact: str) -> str:
    if not isinstance(value, list) or not value or not all(
        isinstance(segment, str) and segment for segment in value
    ):
        raise ValueError(f"route segments must be a non-empty string list for {artifact}")
    return "/" + "/".join(value)


def load_baseline(path: Path) -> DebtSnapshot:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("baseline_id") != "pantheon.architecture_debt":
        raise ValueError("unexpected architecture debt baseline id")
    if int(payload.get("revision", 0)) < 1:
        raise ValueError("architecture debt baseline revision must be positive")
    if payload.get("status") != "active_decreasing_baseline":
        raise ValueError("architecture debt baseline is not active")

    allowed = payload.get("allowed")
    if not isinstance(allowed, dict):
        raise ValueError("architecture debt baseline must contain allowed")

    generation_raw = allowed.get("generation_named_artifacts", [])
    if not isinstance(generation_raw, list) or not all(
        isinstance(item, str) and item for item in generation_raw
    ):
        raise ValueError("generation_named_artifacts must be a string list")

    routes_raw = allowed.get("internal_versioned_routes", {})
    if not isinstance(routes_raw, dict):
        raise ValueError("internal_versioned_routes must be an object")
    routes: set[str] = set()
    for artifact, route_groups in routes_raw.items():
        if not isinstance(artifact, str) or not artifact:
            raise ValueError("route artifact key must be a non-empty string")
        if not isinstance(route_groups, list):
            raise ValueError(f"route groups must be a list for {artifact}")
        for segments in route_groups:
            routes.add(_route_ref(artifact, _decode_route_segments(segments, artifact=artifact)))

    generation = tuple(sorted(set(generation_raw)))
    if len(generation) != len(generation_raw):
        raise ValueError("generation_named_artifacts contains duplicates")
    return DebtSnapshot(generation, tuple(sorted(routes)))


def compare(current: DebtSnapshot, baseline: DebtSnapshot) -> list[str]:
    errors: list[str] = []
    current_generation = set(current.generation_named_artifacts)
    allowed_generation = set(baseline.generation_named_artifacts)
    current_routes = set(current.internal_versioned_routes)
    allowed_routes = set(baseline.internal_versioned_routes)

    additions = sorted(current_generation - allowed_generation)
    resolved = sorted(allowed_generation - current_generation)
    route_additions = sorted(current_routes - allowed_routes)
    route_resolved = sorted(allowed_routes - current_routes)

    if additions:
        errors.append("new generation-named artifacts:\n  - " + "\n  - ".join(additions))
    if route_additions:
        errors.append("new internal versioned routes:\n  - " + "\n  - ".join(route_additions))
    if resolved:
        errors.append(
            "resolved generation debt remains in the baseline; remove it:\n  - "
            + "\n  - ".join(resolved)
        )
    if route_resolved:
        errors.append(
            "resolved versioned routes remain in the baseline; remove them:\n  - "
            + "\n  - ".join(route_resolved)
        )
    return errors


def current_payload(snapshot: DebtSnapshot) -> dict[str, object]:
    routes: dict[str, list[str]] = {}
    for route_ref in snapshot.internal_versioned_routes:
        artifact, route = route_ref.split("::", 1)
        routes.setdefault(artifact, []).append(route)
    return {
        "generation_named_artifacts": list(snapshot.generation_named_artifacts),
        "internal_versioned_routes": {
            artifact: sorted(values) for artifact, values in sorted(routes.items())
        },
        "summary": {
            "generation_named_artifacts": len(snapshot.generation_named_artifacts),
            "internal_versioned_route_files": len(routes),
            "internal_versioned_route_declarations": len(snapshot.internal_versioned_routes),
        },
    }


def route_catalogue(inventory: dict[str, object]) -> dict[str, object]:
    entries: list[dict[str, object]] = []
    artifacts = inventory.get("artifacts", [])
    if not isinstance(artifacts, list):
        raise ValueError("inventory must contain an artifacts list")
    for raw in artifacts:
        if not isinstance(raw, dict):
            continue
        routes = raw.get("routes", [])
        if not routes:
            continue
        entries.append(
            {
                "repository": raw.get("repository"),
                "path": raw.get("path"),
                "posture": raw.get("posture"),
                "routes": sorted(str(route) for route in routes),
                "versioned_routes": sorted(
                    str(route) for route in raw.get("versioned_routes", [])
                ),
            }
        )
    entries.sort(key=lambda item: (str(item["repository"]), str(item["path"])))
    return {
        "route_files": len(entries),
        "route_declarations": sum(len(item["routes"]) for item in entries),
        "entries": entries,
    }


def _write_json(path: Path | None, payload: dict[str, object]) -> None:
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--current-output", type=Path)
    parser.add_argument("--route-catalogue-output", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)

    inventory = json.loads(args.inventory.read_text(encoding="utf-8"))
    current = collect_debt(inventory)
    baseline = load_baseline(args.baseline)
    _write_json(args.current_output, current_payload(current))
    _write_json(args.route_catalogue_output, route_catalogue(inventory))

    errors = compare(current, baseline)
    if errors:
        print("Architecture debt baseline mismatch:")
        for error in errors:
            print(f"\n{error}")
        return 1

    print(
        "Architecture debt baseline matched: "
        f"generation={len(current.generation_named_artifacts)}, "
        f"versioned_routes={len(current.internal_versioned_routes)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
