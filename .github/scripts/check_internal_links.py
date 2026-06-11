#!/usr/bin/env python3
"""Read-only governance check: internal path references must resolve or be explicit.

Scans docs/governance/**/*.md for Markdown links and path-like mentions such as
`docs/...`, `schemas/...`, `templates/...`, `ai_logs/...` and `hermes/...`.
The check is conservative: URLs, anchors and documented future module prefixes
are ignored. The script never modifies files.

Use --list to print findings.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs" / "governance"
PATH_RE = re.compile(r"(?P<path>(?:docs|schemas|templates|ai_logs|hermes)/[A-Za-z0-9_./-]+)")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

# Future or intentionally external surfaces documented before implementation.
EXCLUDED_PREFIXES = (
    "mcp-server/",
    "dashboard/",
    "operations/",
    "platform/",
)

# Explicit known future docs / historical placeholders. Keep small and visible.
EXCLUDED_PATHS = {
    "docs/governance/ANSWER_VERIFICATION_GATE.md",
    "docs/governance/SHARED_AXES_PROPOSAL.md",
    "schemas/shared_axes.yaml",
    "schemas/register_candidate.schema.yaml",
}


def normalize_candidate(raw: str, source: Path) -> str | None:
    raw = raw.strip().strip("`'\".,;:)]}")
    if not raw or raw.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if any(raw.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
        return None
    if raw in EXCLUDED_PATHS:
        return None
    if raw.startswith("../") or raw.startswith("./"):
        candidate = (source.parent / raw).resolve()
        try:
            return candidate.relative_to(ROOT).as_posix()
        except ValueError:
            return raw
    if raw.startswith(("docs/", "schemas/", "templates/", "ai_logs/", "hermes/")):
        return raw
    return None


def find_refs(path: Path) -> list[tuple[int, str]]:
    refs: list[tuple[int, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for idx, line in enumerate(lines, start=1):
        for match in LINK_RE.finditer(line):
            ref = normalize_candidate(match.group(1), path)
            if ref:
                refs.append((idx, ref))
        for match in PATH_RE.finditer(line):
            ref = normalize_candidate(match.group("path"), path)
            if ref:
                refs.append((idx, ref))
    return refs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    rows: list[str] = []
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        for line_no, ref in find_refs(path):
            rows.append(f"{rel}:{line_no}: {ref}")
            if not (ROOT / ref).exists():
                failures.append(f"{rel}:{line_no}: missing internal reference: {ref}")

    if args.list:
        print("\n".join(rows))
    if failures:
        print("Internal link/path check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
