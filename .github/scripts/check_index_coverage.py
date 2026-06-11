#!/usr/bin/env python3
"""Read-only governance check: candidate docs are visible in AUTHORITY_INDEX.md.

Checks two directions:
1. docs/governance files declaring Status: candidate appear in AUTHORITY_INDEX.md.
2. path-like entries in AUTHORITY_INDEX.md point to existing files, unless explicitly future/grouped.

Use --list to print candidate documents and indexed paths. The script never modifies files.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "governance"
INDEX = DOCS / "AUTHORITY_INDEX.md"
PATH_RE = re.compile(r"`((?:docs|schemas|templates|ai_logs|hermes)/[^`]+)`")
FUTURE_OR_GROUPED = {
    "docs/governance/DATA_PLATFORM_*.md",
    "docs/governance/reference_reviews/",
    "docs/governance/rites/",
    "templates/",
    "examples/",
    "ai_logs/",
    "schemas/",
    "tests/",
    "operations/",
    "platform/",
    "Docker*",
    ".env*",
}


def detect_status(path: Path) -> str | None:
    for line in path.read_text(encoding="utf-8").splitlines()[:10]:
        if line.strip().lower().startswith("status:"):
            return line.split(":", 1)[1].strip()
    return None


def candidate_docs() -> list[str]:
    rows: list[str] = []
    for path in sorted(DOCS.rglob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        status = detect_status(path)
        if status and "candidate" in status.lower():
            rows.append(path.relative_to(ROOT).as_posix())
    return rows


def indexed_paths() -> set[str]:
    text = INDEX.read_text(encoding="utf-8")
    return {m.group(1).strip() for m in PATH_RE.finditer(text)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()

    index_text = INDEX.read_text(encoding="utf-8")
    cands = candidate_docs()
    paths = indexed_paths()
    failures: list[str] = []

    for rel in cands:
        if rel not in index_text:
            failures.append(f"candidate doc not indexed in AUTHORITY_INDEX.md: {rel}")

    for ref in sorted(paths):
        if ref in FUTURE_OR_GROUPED:
            continue
        if ref.endswith("/"):
            if not (ROOT / ref).is_dir():
                failures.append(f"AUTHORITY_INDEX.md references missing directory: {ref}")
        elif "*" in ref:
            continue
        elif not (ROOT / ref).exists():
            failures.append(f"AUTHORITY_INDEX.md references missing path: {ref}")

    if args.list:
        print("Candidate docs:")
        print("\n".join(cands))
        print("\nIndexed paths:")
        print("\n".join(sorted(paths)))
    if failures:
        print("Authority index coverage check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
