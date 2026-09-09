#!/usr/bin/env python3
"""Fail if ai_logs/INDEX.md does not match what the generator would produce.

Temporary branch diagnostic: on mismatch, print the exact expected generated index
between stable markers so the PR can reconcile the generated file without changing
its generator or governance semantics. This diagnostic must be reverted before merge.
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
    print("FAIL: ai_logs/INDEX.md is stale.")
    print("---BEGIN-EXPECTED-AI-LOG-INDEX---")
    print(expected, end="")
    print("---END-EXPECTED-AI-LOG-INDEX---")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
