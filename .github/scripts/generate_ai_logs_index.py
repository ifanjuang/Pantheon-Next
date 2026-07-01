#!/usr/bin/env python3
"""Regenerate ai_logs/INDEX.md — a read-only navigation table over the ai_logs.

It reads every dated ai_logs/*.md entry, pulls the date from the filename and the
subject from the first `# ` heading, and writes a table sorted newest-first. It
edits nothing else and decides nothing; it is a pure index generator.

Usage: python3 .github/scripts/generate_ai_logs_index.py
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AI_LOGS = ROOT / "ai_logs"
SKIP = {"README.md", "INDEX.md", "migration-mapping.md"}
DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")


def subject(md: Path) -> str:
    for line in md.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return "(no title)"


def main() -> None:
    rows = []
    for md in AI_LOGS.glob("*.md"):
        if md.name in SKIP:
            continue
        m = DATE_RE.match(md.name)
        date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else "—"
        rows.append((date, md.name, subject(md)))
    # newest first, then by filename
    rows.sort(key=lambda r: (r[0], r[1]), reverse=True)

    out = [
        "# ai_logs — Index",
        "",
        "Status: validation-only / generated navigation index over the AI intervention logs.",
        "",
        "Every significant AI intervention adds an `ai_logs/` entry (see `CLAUDE.md`). This",
        "table is a read-only map of them, newest first. It is **generated** — do not edit by",
        "hand; run `.github/scripts/generate_ai_logs_index.py` after adding a log.",
        "",
        "## Convention going forward",
        "",
        "```text",
        "New logs are dated (YYYY-MM-DD-<slug>.md) and, once the quarterly archive lands,",
        "grouped as ai_logs/<year>/Q<n>/. The mass move of the existing flat logs is a",
        "separate follow-up PR so its diff stays readable and reversible; this index already",
        "covers the flat files in the meantime.",
        "```",
        "",
        f"Total indexed entries: **{len(rows)}**.",
        "",
        "| Date | Log | Subject |",
        "|---|---|---|",
    ]
    for date, name, subj in rows:
        subj = subj.replace("|", "\\|")
        out.append(f"| {date} | `{name}` | {subj} |")
    out.append("")
    (AI_LOGS / "INDEX.md").write_text("\n".join(out), encoding="utf-8")
    print(f"wrote ai_logs/INDEX.md with {len(rows)} entries")


if __name__ == "__main__":
    main()
