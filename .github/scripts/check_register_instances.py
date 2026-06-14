#!/usr/bin/env python3
"""Validate register_link / impact_review / register_candidate instances.

Read-only governance check. It validates each instance file under
docs/examples/cascade_register/ against its schema, verifies link_ids
referential integrity, and applies the cascade rule (critical impacts must
route to arbitration; a resolved review must record a decision per target).

The whole check is imported from the mcp-server doctor so there is a single
source of truth. The script never edits, fixes or decides.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "mcp-server"))
from pantheon_mcp.doctor import check_register_instances  # noqa: E402


def main() -> int:
    result = check_register_instances(ROOT)

    if result.get("informational"):
        print(f"SKIP: {result.get('note', 'register instances not evaluated.')}")
        return 0

    violations = result.get("violations", [])
    if violations:
        print("Register instance check failed:", file=sys.stderr)
        for item in violations:
            print(f" - {item['file']}: {item['message']}", file=sys.stderr)
        return 1

    checked = result.get("instances_checked", 0)
    print(f"OK: {checked} register instance(s) valid; link_ids resolve; cascade rule satisfied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
