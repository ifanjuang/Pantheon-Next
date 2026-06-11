#!/usr/bin/env python3
"""Read-only governance check: candidate docs are visible in AUTHORITY_INDEX.md.

Baseline policy, dated 2026-06-11: when GOVERNANCE_BASE_REF is set, index
coverage violations already present on that ref are treated as baseline
exceptions. The check fails only on new violations outside that baseline.

The script never modifies files.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
DOCS_PREFIX = "docs/governance"
INDEX_REL = "docs/governance/AUTHORITY_INDEX.md"
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


def index_text(ref: str | None) -> str:
    if ref is None:
        return (ROOT / INDEX_REL).read_text(encoding="utf-8")
    return git_text(ref, INDEX_REL)


def indexed_paths(ref: str | None) -> set[str]:
    return {m.group(1).strip() for m in PATH_RE.finditer(index_text(ref))}


def violations(ref: str | None) -> dict[str, str]:
    text = index_text(ref)
    paths = indexed_paths(ref)
    found: dict[str, str] = {}

    for rel in candidate_docs(ref):
        if rel not in text:
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
