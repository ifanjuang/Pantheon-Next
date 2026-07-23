#!/usr/bin/env python3
"""Require newly added AI logs to use ``ai_logs/<year>/Q<n>/``.

Historical flat files are intentionally outside this check. The script inspects
only files added relative to a supplied Git base and never moves or edits them.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
from datetime import date
from pathlib import Path
from typing import Iterable

SUPPORT_PATHS = {
    "ai_logs/README.md",
    "ai_logs/INDEX.md",
    "ai_logs/LOG_FORMAT.md",
    "ai_logs/migration-mapping.md",
}
LOG_RE = re.compile(
    r"^ai_logs/(?P<year>\d{4})/Q(?P<quarter>[1-4])/"
    r"(?P<dated>\d{4}-\d{2}-\d{2})-(?P<slug>[a-z0-9][a-z0-9._-]*)\.md$"
)


def validate_added_paths(paths: Iterable[str]) -> list[str]:
    findings: list[str] = []
    for raw in sorted(set(paths)):
        path = Path(raw).as_posix()
        if not path.startswith("ai_logs/") or path in SUPPORT_PATHS:
            continue

        match = LOG_RE.fullmatch(path)
        if not match:
            findings.append(
                f"new AI log must match ai_logs/<year>/Q<n>/YYYY-MM-DD-<slug>.md: {path}"
            )
            continue

        try:
            dated = date.fromisoformat(match.group("dated"))
        except ValueError:
            findings.append(f"new AI log has an invalid calendar date: {path}")
            continue

        directory_year = int(match.group("year"))
        directory_quarter = int(match.group("quarter"))
        expected_quarter = ((dated.month - 1) // 3) + 1
        if directory_year != dated.year:
            findings.append(
                f"AI log year directory {directory_year} does not match filename date {dated.year}: {path}"
            )
        if directory_quarter != expected_quarter:
            findings.append(
                f"AI log Q{directory_quarter} does not match month {dated.month:02d} (Q{expected_quarter}): {path}"
            )
    return findings


def added_paths(base_ref: str) -> list[str]:
    merge_base = subprocess.run(
        ["git", "merge-base", base_ref, "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    output = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=A", merge_base, "HEAD", "--", "ai_logs"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return [line.strip() for line in output.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base",
        default=os.environ.get("GOVERNANCE_BASE_REF") or os.environ.get("GITHUB_BASE_REF") or "origin/main",
        help="Git base ref used to identify newly added files (default: env or origin/main)",
    )
    args = parser.parse_args()

    try:
        paths = added_paths(args.base)
    except subprocess.CalledProcessError as exc:
        print(f"FAIL: could not determine newly added AI logs from base {args.base!r}: {exc}")
        return 2

    findings = validate_added_paths(paths)
    if findings:
        print("FAIL: newly added AI logs do not follow the quarterly path rule:")
        for finding in findings:
            print(f"  - {finding}")
        return 1

    checked = [path for path in paths if path not in SUPPORT_PATHS]
    print(f"OK: {len(checked)} newly added AI log(s) use year/quarter paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
