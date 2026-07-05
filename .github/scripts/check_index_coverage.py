#!/usr/bin/env python3
"""Read-only governance check: candidate docs are visible in the authority map.

The authority map is AUTHORITY_INDEX.md plus the sub-indexes under
docs/governance/authority/ that it registers (AUTHORITY_INDEX_DECOMPOSITION_PLAN.md).
A candidate doc counts as indexed when it is mentioned in a Markdown table row of
the master index or of any sub-index, or when a grouped row in either covers it.
Prose mentions do not count: indexing is a deliberate row, not a passing
reference. The master index alone still defines the authority vocabulary;
sub-indexes only list placement.

Baseline policy, dated 2026-06-11: when GOVERNANCE_BASE_REF is set, index
coverage violations already present on that ref are treated as baseline
exceptions. The check fails only on new violations outside that baseline.

The script never modifies files.
"""

from __future__ import annotations

import argparse
import fnmatch
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS_PREFIX = "docs/governance"
INDEX_REL = "docs/governance/AUTHORITY_INDEX.md"
SUBINDEX_DIR = "docs/governance/authority"
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


def git_text(ref: str, rel: str) -> str:
    try:
        return subprocess.check_output(["git", "show", f"{ref}:{rel}"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return ""


def git_docs(ref: str | None) -> list[str]:
    if ref is None:
        root = ROOT / DOCS_PREFIX
        return sorted(p.relative_to(ROOT).as_posix() for p in root.rglob("*.md"))
    try:
        raw = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", ref, DOCS_PREFIX], cwd=ROOT, text=True)
    except subprocess.CalledProcessError:
        return []
    return sorted(p for p in raw.splitlines() if p.endswith(".md"))


def read_lines(rel: str, ref: str | None) -> list[str]:
    if ref is None:
        return (ROOT / rel).read_text(encoding="utf-8").splitlines()
    return git_text(ref, rel).splitlines()


def file_exists(rel: str, ref: str | None) -> bool:
    if ref is None:
        return (ROOT / rel).exists()
    try:
        subprocess.check_output(["git", "cat-file", "-e", f"{ref}:{rel}"], cwd=ROOT, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False


def detect_status(lines: list[str]) -> str | None:
    for line in lines[:10]:
        if line.strip().lower().startswith("status:"):
            return line.split(":", 1)[1].strip()
    return None


def candidate_docs(ref: str | None) -> list[str]:
    rows: list[str] = []
    for rel in git_docs(ref):
        if rel.lower().endswith("/readme.md"):
            continue
        status = detect_status(read_lines(rel, ref))
        if status and "candidate" in status.lower():
            rows.append(rel)
    return rows


def subindex_rels(ref: str | None) -> list[str]:
    """Sub-index files under docs/governance/authority/ at `ref` (or the tree)."""
    if ref is None:
        subdir = ROOT / SUBINDEX_DIR
        if not subdir.is_dir():
            return []
        return sorted(p.relative_to(ROOT).as_posix() for p in subdir.glob("*.md"))
    try:
        raw = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", ref, SUBINDEX_DIR],
            cwd=ROOT, text=True, stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return []
    return sorted(p for p in raw.splitlines() if p.endswith(".md"))


def index_text(ref: str | None) -> str:
    """Combined table rows of the master index and its registered sub-indexes.

    Only Markdown table-row lines (starting with '|') count as indexing: a row
    is a deliberate act; a prose mention is not."""
    rows: list[str] = []
    for rel in [INDEX_REL, *subindex_rels(ref)]:
        for line in read_lines(rel, ref):
            if line.lstrip().startswith("|"):
                rows.append(line)
    return "\n".join(rows)


def indexed_paths(ref: str | None) -> set[str]:
    return {m.group(1).strip() for m in PATH_RE.finditer(index_text(ref))}


def _grouped_covers(groups: set[str], rel: str) -> bool:
    """A grouped index row (directory path ending in '/', or a '*' glob) covers
    every governance doc it matches, so members need no individual row."""
    for group in groups:
        if "*" in group:
            if fnmatch.fnmatch(rel, group):
                return True
        elif group.endswith("/") and rel.startswith(group):
            return True
    return False


def violations(ref: str | None) -> dict[str, str]:
    text = index_text(ref)
    paths = indexed_paths(ref)
    # Grouped rows are directory/glob entries *under* the governance docs tree and
    # strictly deeper than its root, so a prose mention of the root itself
    # (`docs/governance/`) never masks every candidate.
    group_root = DOCS_PREFIX + "/"
    groups = {
        p
        for p in paths
        if (p.endswith("/") or "*" in p) and p.startswith(group_root) and p != group_root
    }
    found: dict[str, str] = {}

    for rel in candidate_docs(ref):
        if rel not in text and not _grouped_covers(groups, rel):
            found[f"candidate-not-indexed|{rel}"] = f"candidate doc not indexed in AUTHORITY_INDEX.md: {rel}"

    for target in sorted(paths):
        if target in FUTURE_OR_GROUPED or "*" in target:
            continue
        if target.endswith("/"):
            if ref is None:
                ok = (ROOT / target).is_dir()
            else:
                # Git cannot cat-file an empty directory; treat grouped slash paths as covered above.
                ok = target in FUTURE_OR_GROUPED
            if not ok:
                found[f"missing-dir|{target}"] = f"AUTHORITY_INDEX.md references missing directory: {target}"
        elif not file_exists(target, ref):
            found[f"missing-path|{target}"] = f"AUTHORITY_INDEX.md references missing path: {target}"
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()

    base_ref = os.environ.get("GOVERNANCE_BASE_REF") or None
    current = violations(None)
    baseline = violations(base_ref) if base_ref and base_ref != "HEAD" else {}
    new_keys = sorted(set(current) - set(baseline))

    if args.list:
        print("Candidate docs:")
        print("\n".join(candidate_docs(None)))
        print("\nIndexed paths:")
        print("\n".join(sorted(indexed_paths(None))))
        if base_ref:
            print(f"\nBaseline ref: {base_ref} ({len(baseline)} exception(s))")

    if new_keys:
        print("Authority index coverage check failed:", file=sys.stderr)
        if base_ref:
            print(f"Baseline ref: {base_ref}; existing baseline violations are ignored.", file=sys.stderr)
        for key in new_keys:
            print(f"- {current[key]}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
