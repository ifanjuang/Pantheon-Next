#!/usr/bin/env python3
"""Read-only governance check: every governance Markdown file declares a Status header.

Scans docs/governance/**/*.md, excluding README.md files, and requires a Status:
line in the first 10 lines. Accepted vocabulary follows AUTHORITY_INDEX.md.

Use --list to print checked files and detected statuses without changing files.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "governance"
ACCEPTED = (
    "canonical",
    "active doctrine",
    "active support",
    "support",
    "candidate",
    "validation-only",
    "reference",
    "stub",
    "obsolete",
    "example",
)


def iter_docs() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.md") if p.name.lower() != "readme.md")


def detect_status(path: Path) -> tuple[int | None, str | None]:
    lines = path.read_text(encoding="utf-8").splitlines()
    for idx, line in enumerate(lines[:10], start=1):
        if line.strip().lower().startswith("status:"):
            return idx, line.split(":", 1)[1].strip()
    return None, None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    rows: list[str] = []
    for path in iter_docs():
        rel = path.relative_to(ROOT).as_posix()
        line_no, status = detect_status(path)
        if status is None:
            failures.append(f"{rel}: missing Status: line in first 10 lines")
            rows.append(f"{rel}: <missing>")
            continue
        rows.append(f"{rel}:{line_no}: {status}")
        if not any(token in status.lower() for token in ACCEPTED):
            failures.append(f"{rel}:{line_no}: unsupported Status value: {status!r}")

    if args.list:
        print("\n".join(rows))
    if failures:
        print("Status header check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
