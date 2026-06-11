#!/usr/bin/env python3
"""Read-only governance check: keep E/V/K/C axes distinct.

Flags common mistakes:
- consequence fields using C0-C5 instead of K0-K4;
- approval fields using K0-K4 instead of C0-C5;
- newly introduced YAML field name confidence: where certainty: is canonical.

The check is calibrated for the current corpus and reads files only.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SCAN_ROOTS = [ROOT / "docs", ROOT / "schemas", ROOT / "templates"]
CONSEQUENCE_WITH_C = re.compile(r"(?i)(consequence|criticality|impact)[^\n]{0,80}\bC[0-5]\b")
APPROVAL_WITH_K = re.compile(r"(?i)(approval|required_approval|approval_required|ceiling)[^\n]{0,80}\bK[0-4]\b")
CONFIDENCE_FIELD = re.compile(r"^\s*confidence\s*:", re.MULTILINE)

# Existing historical/proposal contexts that are allowed until their own cleanup PR.
EXCLUDED = {
    "docs/governance/OPEN_PR_RECONCILIATION.md",
    "docs/governance/REGISTRE_PROBATOIRE_DIRECTION.md",
    "CHANGELOG.md",
    "CHANGELOG_ARCHIVE.md",
}


def iter_files() -> list[Path]:
    files: list[Path] = []
    for root in SCAN_ROOTS:
        if root.exists():
            files.extend(p for p in root.rglob("*") if p.suffix.lower() in {".md", ".yaml", ".yml"})
    return sorted(files)


def main() -> int:
    failures: list[str] = []
    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        if rel in EXCLUDED:
            continue
        text = path.read_text(encoding="utf-8")
        for idx, line in enumerate(text.splitlines(), start=1):
            if CONSEQUENCE_WITH_C.search(line):
                failures.append(f"{rel}:{idx}: consequence-like context uses C-axis: {line.strip()}")
            if APPROVAL_WITH_K.search(line):
                failures.append(f"{rel}:{idx}: approval-like context uses K-axis: {line.strip()}")
        if path.suffix.lower() in {".yaml", ".yml"}:
            for match in CONFIDENCE_FIELD.finditer(text):
                line_no = text[: match.start()].count("\n") + 1
                failures.append(f"{rel}:{line_no}: YAML field 'confidence:' should be 'certainty:' unless explicitly legacy/deprecated")

    if failures:
        print("Axis vocabulary check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print("OK: E/V/K/C axis vocabulary is not obviously conflated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
