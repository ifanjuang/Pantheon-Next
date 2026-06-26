#!/usr/bin/env python3
"""Tripwire: long canonical governance files must not be silently truncated.

A recurring failure mode (see ai_logs/2026-06-26-modules-index-runtime-review-and-
truncation-repair.md) is a connector returning a *partial* read of a long file,
which is then written back as a full-file replacement — silently dropping the tail.
MODULES.md was cut from 481 to 302 lines this way, losing every section from the
Approval module body through the Final rule.

This check fails CI when a curated long file falls below a minimum line count or
loses its required end-sentinel (a stable doctrine line that lives near the end of
the file). It is deliberately a tripwire: if one of these files legitimately shrinks
or its ending changes, update the MANIFEST below in the same PR.

It does not edit, fix or rewrite anything. It only reports.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]

# relative path -> (minimum line count, tail sentinel that must appear near the end)
MANIFEST = {
    "docs/governance/MODULES.md": (450, "left Pantheon governance scope."),
    "docs/governance/AUTHORITY_INDEX.md": (300, "explicit approval in their own work package."),
}

# How many trailing lines the sentinel must appear within.
TAIL_WINDOW = 20


def main() -> int:
    failures = []
    for rel, (min_lines, sentinel) in MANIFEST.items():
        path = ROOT / rel
        if not path.exists():
            failures.append(f"{rel}: file is missing")
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) < min_lines:
            failures.append(
                f"{rel}: {len(lines)} lines, below minimum {min_lines} "
                f"(possible truncation; if intentional, lower the minimum in "
                f".github/scripts/check_no_truncation.py)"
            )
        tail = "\n".join(lines[-TAIL_WINDOW:])
        if sentinel not in tail:
            failures.append(
                f"{rel}: required end-sentinel not found in the last {TAIL_WINDOW} "
                f"lines: {sentinel!r} (the tail may have been truncated; if the "
                f"ending changed on purpose, update the sentinel in "
                f".github/scripts/check_no_truncation.py)"
            )

    if failures:
        print("FAIL: long governance files may have been truncated:")
        for f in failures:
            print(f"  {f}")
        print("")
        print("A connector that returns a partial read of a long file must not be")
        print("used as full-file replacement content. Edit long files in place")
        print("(anchored replacement), or restore a lost tail from git history.")
        return 1

    print("OK: curated long governance files retain their length and end-sentinel.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
