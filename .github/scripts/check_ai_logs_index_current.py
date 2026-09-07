#!/usr/bin/env python3
"""Fail if ai_logs/INDEX.md does not match what the generator would produce.

The index states its own contract: it is generated, and `generate_ai_logs_index.py`
must be run after adding a log. Nothing enforced that — 39 of 245 Q3 entries were
found missing on 2026-09-06, discovered only by reading the file, not by any
check. This closes that gap the same way the rest of this workflow works: import
the generator's own logic rather than reimplementing it, so the two can never
silently diverge from each other.

    generated != enforced
    stated contract != checked contract

Usage: python3 .github/scripts/check_ai_logs_index_current.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_ai_logs_index import AI_LOGS, collect_rows, render_index  # noqa: E402


def main() -> int:
    expected = render_index(collect_rows())
    index_path = AI_LOGS / "INDEX.md"
    if not index_path.exists():
        print("FAIL: ai_logs/INDEX.md is missing.")
        return 1
    actual = index_path.read_text(encoding="utf-8")
    if actual == expected:
        print("OK: ai_logs/INDEX.md matches the generator output.")
        return 0
    print(
        "FAIL: ai_logs/INDEX.md is stale.\n"
        "Run `python3 .github/scripts/generate_ai_logs_index.py` and commit the result."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
