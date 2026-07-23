from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PATHS = load_module("check_new_ai_log_paths", ".github/scripts/check_new_ai_log_paths.py")
INDEX = load_module("generate_ai_logs_index", ".github/scripts/generate_ai_logs_index.py")


def test_quarterly_path_accepts_matching_date_and_quarter() -> None:
    assert PATHS.validate_added_paths(
        ["ai_logs/2026/Q3/2026-07-23-quarterly-ai-log-paths.md"]
    ) == []


def test_support_files_and_non_log_paths_are_ignored() -> None:
    assert PATHS.validate_added_paths(
        [
            "ai_logs/README.md",
            "ai_logs/INDEX.md",
            "ai_logs/LOG_FORMAT.md",
            "docs/governance/STATUS.md",
        ]
    ) == []


def test_new_flat_log_is_rejected_without_affecting_legacy_files() -> None:
    findings = PATHS.validate_added_paths(["ai_logs/2026-07-23-new-flat-log.md"])
    assert findings and "must match" in findings[0]


def test_wrong_year_and_quarter_are_rejected() -> None:
    findings = PATHS.validate_added_paths(
        ["ai_logs/2025/Q2/2026-07-23-wrong-placement.md"]
    )
    assert any("year directory" in finding for finding in findings)
    assert any("does not match month" in finding for finding in findings)


def test_invalid_calendar_date_is_rejected() -> None:
    findings = PATHS.validate_added_paths(
        ["ai_logs/2026/Q1/2026-02-31-invalid-date.md"]
    )
    assert findings and "invalid calendar date" in findings[0]


def test_recursive_index_keeps_flat_and_quarterly_paths(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# policy", encoding="utf-8")
    (tmp_path / "INDEX.md").write_text("# generated", encoding="utf-8")
    (tmp_path / "2026-07-20-legacy-flat.md").write_text(
        "# Legacy flat trace", encoding="utf-8"
    )
    quarterly = tmp_path / "2026/Q3/2026-07-23-quarterly.md"
    quarterly.parent.mkdir(parents=True)
    quarterly.write_text("# Quarterly trace", encoding="utf-8")

    rows = INDEX.collect_rows(tmp_path)
    assert rows == [
        ("2026-07-23", "2026/Q3/2026-07-23-quarterly.md", "Quarterly trace"),
        ("2026-07-20", "2026-07-20-legacy-flat.md", "Legacy flat trace"),
    ]

    rendered = INDEX.render_index(rows)
    assert "`2026/Q3/2026-07-23-quarterly.md`" in rendered
    assert "`2026-07-20-legacy-flat.md`" in rendered
    assert "Total indexed entries: **2**" in rendered
