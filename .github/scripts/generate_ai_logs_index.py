#!/usr/bin/env python3
"""Regenerate ai_logs/INDEX.md as read-only navigation over AI logs.

The generator indexes both the historical flat corpus and new quarterly paths
under ``ai_logs/<year>/Q<n>/``. It edits only INDEX.md and decides nothing.

Usage: python3 .github/scripts/generate_ai_logs_index.py
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AI_LOGS = ROOT / "ai_logs"
SKIP_RELATIVE = {"README.md", "INDEX.md", "migration-mapping.md"}
DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")


def subject(md: Path) -> str:
    for line in md.read_text(encoding="utf-8").splitlines():
        value = line.strip()
        if value.startswith("# "):
            return value[2:].strip()
    return "(no title)"


def collect_rows(ai_logs: Path = AI_LOGS) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    for md in ai_logs.rglob("*.md"):
        relative = md.relative_to(ai_logs).as_posix()
        if relative in SKIP_RELATIVE:
            continue
        match = DATE_RE.match(md.name)
        date = (
            f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
            if match
            else "—"
        )
        rows.append((date, relative, subject(md)))
    rows.sort(key=lambda row: (row[0], row[1]), reverse=True)
    return rows


def render_index(rows: list[tuple[str, str, str]]) -> str:
    out = [
        "# ai_logs — Index",
        "",
        "Status: validation-only / generated navigation index over the AI intervention logs.",
        "",
        "Every significant AI intervention adds an `ai_logs/` entry (see `CLAUDE.md`). This",
        "table is a read-only map of them, newest first. It is **generated** — do not edit by",
        "hand; run `python3 .github/scripts/generate_ai_logs_index.py` after adding a log.",
        "",
        "## Current placement rule",
        "",
        "```text",
        "New logs -> ai_logs/<year>/Q<n>/YYYY-MM-DD-<slug>.md",
        "Existing flat logs -> remain valid and indexed in place; no retroactive mass move.",
        "Removal from the working tree -> reviewed separately; Git history remains the archive.",
        "```",
        "",
        f"Total indexed entries: **{len(rows)}**.",
        "",
        "| Date | Log | Subject |",
        "|---|---|---|",
    ]
    for date, relative, title in rows:
        safe_title = title.replace("|", "\\|")
        out.append(f"| {date} | `{relative}` | {safe_title} |")
    out.append("")
    return "\n".join(out)


def main() -> None:
    rows = collect_rows()
    (AI_LOGS / "INDEX.md").write_text(render_index(rows), encoding="utf-8")
    print(f"wrote ai_logs/INDEX.md with {len(rows)} entries")


if __name__ == "__main__":
    main()
