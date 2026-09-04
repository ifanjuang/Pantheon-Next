from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

ACTIVE_ROOTS = (
    ROOT / "implementation",
    ROOT / "deployment",
    ROOT / "templates",
    ROOT / "docs/governance",
    ROOT / "docs/roadmaps",
    ROOT / "docs/assets",
    ROOT / "schemas",
    ROOT / "scripts",
    ROOT / "tests",
    ROOT / "revit-plugin",
    ROOT / ".github/scripts",
    ROOT / ".github/workflows",
)
HISTORICAL_PREFIXES = ("ai_logs/", "implementation/ai_logs/", "docs/audits/")
HISTORICAL_EXACT = {
    "CHANGELOG.md",
    "CHANGELOG_ARCHIVE.md",
    "implementation/CHANGELOG.md",
    "implementation/IMPORT_PROVENANCE.md",
    "docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md",
}
TEXT_SUFFIXES = {
    ".py", ".md", ".toml", ".yaml", ".yml", ".json", ".js", ".html",
    ".css", ".sql", ".sh", ".txt", ".env", ".lock", ".ini", ".cfg", ".xml",
}
TEXT_NAMES = {"Dockerfile", "Makefile", ".gitmodules"}
PATTERN = re.compile(r"(?i)(?<![A-Za-z0-9])mvp(?![A-Za-z0-9])|mvp_|mvp-")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def historical(path: Path) -> bool:
    value = rel(path)
    return ".git" in path.parts or value in HISTORICAL_EXACT or value.startswith(HISTORICAL_PREFIXES)


hits: list[str] = []
seen: set[Path] = set()
for root in ACTIVE_ROOTS:
    if not root.exists():
        continue
    for path in root.rglob("*"):
        if path in seen or path == SELF or not path.is_file() or historical(path):
            continue
        seen.add(path)
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_NAMES:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for number, line in enumerate(lines, 1):
            if PATTERN.search(line):
                hits.append(f"{rel(path)}:{number}: {line.strip()}")

print("\n".join(hits))
print(f"ACTIVE_MVP_HIT_COUNT={len(hits)}")
