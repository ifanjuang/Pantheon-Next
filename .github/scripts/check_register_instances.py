#!/usr/bin/env python3
"""Validate register_link / impact_review / register_candidate instances.

Read-only governance check. It validates each instance file under
docs/examples/cascade_register/ against its schema, verifies link_ids
referential integrity, and applies the cascade rule (critical impacts must
route to arbitration; a resolved review must record a decision per target).

The cascade rule is imported from the mcp-server doctor so there is a single
source of truth. The script never edits, fixes or decides.
"""

from __future__ import annotations

import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "mcp-server"))
from pantheon_mcp.doctor import evaluate_impact_review  # noqa: E402

INSTANCES = ROOT / "docs" / "examples" / "cascade_register"
SCHEMAS = ROOT / "schemas"

KEY_TO_SCHEMA = {
    "candidate_id": "register_candidate.schema.yaml",
    "link_id": "register_link.schema.yaml",
    "impact_review_id": "impact_review.schema.yaml",
}


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def main() -> int:
    if not INSTANCES.exists():
        print("OK: no register instances directory; nothing to validate.")
        return 0

    schemas = {key: load(SCHEMAS / name) for key, name in KEY_TO_SCHEMA.items()}
    for schema in schemas.values():
        jsonschema.Draft202012Validator.check_schema(schema)
    checker = jsonschema.FormatChecker()

    errors: list[str] = []
    checked = 0
    known_link_ids: set[str] = set()
    candidate_link_refs: list[tuple[str, str]] = []

    for path in sorted(INSTANCES.rglob("*.y*ml")):
        data = load(path)
        if not isinstance(data, dict):
            continue
        key = next((k for k in KEY_TO_SCHEMA if k in data), None)
        if key is None:
            continue
        checked += 1
        rel = path.relative_to(ROOT).as_posix()

        validator = jsonschema.Draft202012Validator(schemas[key], format_checker=checker)
        schema_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        for err in schema_errors:
            location = ".".join(str(p) for p in err.path) or "<root>"
            errors.append(f"{rel}: schema: {location}: {err.message}")
        if schema_errors:
            continue

        if key == "link_id":
            known_link_ids.add(data["link_id"])
        elif key == "candidate_id":
            for ref in data.get("link_ids", []):
                candidate_link_refs.append((rel, ref))
        elif key == "impact_review_id":
            for message in evaluate_impact_review(data):
                errors.append(f"{rel}: cascade rule: {message}")

    for rel, ref in candidate_link_refs:
        if ref not in known_link_ids:
            errors.append(f"{rel}: link_ids references unknown register_link '{ref}'")

    if errors:
        print("Register instance check failed:", file=sys.stderr)
        for message in errors:
            print(f" - {message}", file=sys.stderr)
        return 1

    print(f"OK: {checked} register instance(s) valid; link_ids resolve; cascade rule satisfied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
