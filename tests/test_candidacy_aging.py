"""The candidacy aging signal: what it classifies, and what it refuses to accept.

The point of the signal is to separate a candidate deliberately kept as one from
a candidate nobody has revisited. These tests hold that line in both directions:
the classifier must not inflate the candidate set with documents that merely
mention candidates, and the aging reset must not be accepted without a record
that exists.
"""

from __future__ import annotations

import datetime as dt
import importlib.util
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_INDEX = ROOT / "docs/governance/AUTHORITY_INDEX.md"


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AGING = load_module("check_candidacy_aging", ".github/scripts/check_candidacy_aging.py")

TODAY = dt.date(2026, 8, 31)
A_REAL_RECORD = "ai_logs/2026/Q3/2026-07-23-cockpit-information-architecture.md"


# --- classification -------------------------------------------------------


def test_the_declared_authority_class_is_the_one_the_signal_recognizes() -> None:
    """Anchored on the class heading, not on a paragraph that may be reworded."""
    headings = [
        line.strip("# ").strip()
        for line in AUTHORITY_INDEX.read_text(encoding="utf-8").splitlines()
        if line.startswith("### ")
    ]
    candidate_headings = [h for h in headings if AGING.is_candidate(h)]
    assert candidate_headings == ["Candidate / to verify"], (
        "the candidate authority class heading moved or multiplied; the aging "
        f"signal keys off it. Headings found: {headings}"
    )


def test_a_descriptive_tail_that_mentions_candidates_is_not_a_candidate() -> None:
    assert not AGING.is_candidate("active support doctrine — workflow candidate forging")
    assert not AGING.is_candidate("support doctrine — Hermes Skill Candidate specification")
    assert not AGING.is_candidate("external reference — to verify.")
    assert not AGING.is_candidate("product direction - implementation to verify capability by capability")
    assert not AGING.is_candidate(None)


def test_the_class_head_is_read_through_either_separator() -> None:
    assert AGING.status_head("candidate support doctrine — documented non-implemented.") == (
        "candidate support doctrine"
    )
    assert AGING.status_head("active doctrine - shared rite.") == "active doctrine"
    assert AGING.is_candidate("candidate / to verify — anything at all")
    assert AGING.is_candidate("candidate governance support doctrine")
    assert AGING.is_candidate("to verify — active governance proposal")


# --- the aging reset ------------------------------------------------------


def test_a_well_formed_review_marker_restarts_the_clock() -> None:
    reviewed, record, error = AGING.parse_review_marker(
        ["# Title", "", f"Candidacy reviewed: 2026-08-20 ({A_REAL_RECORD})"], TODAY
    )
    assert error is None
    assert reviewed == dt.date(2026, 8, 20)
    assert record == A_REAL_RECORD


def test_a_reset_that_cites_nothing_real_is_refused() -> None:
    """An aging reset backed by a missing record is worse than no reset."""
    cases = {
        "malformed": "Candidacy reviewed: 2026-08-20",
        "not a date": f"Candidacy reviewed: last spring ({A_REAL_RECORD})",
        "future": f"Candidacy reviewed: 2027-01-01 ({A_REAL_RECORD})",
        "outside ai_logs": "Candidacy reviewed: 2026-08-20 (docs/governance/STATUS.md)",
        "dangling": "Candidacy reviewed: 2026-08-20 (ai_logs/2026/Q3/does-not-exist.md)",
        # Starts with the right prefix and resolves to a real file that is not a
        # record, so a candidate could reset its own clock by citing doctrine.
        "escapes via ..": "Candidacy reviewed: 2026-08-20 (ai_logs/../docs/governance/STATUS.md)",
        "absolute": "Candidacy reviewed: 2026-08-20 (/etc/hostname)",
    }
    for label, line in cases.items():
        reviewed, record, error = AGING.parse_review_marker(["# T", "", line], TODAY)
        assert error, f"{label}: expected the marker to be refused"
        assert reviewed is None and record is None


def test_a_document_without_the_marker_is_neither_reset_nor_an_error() -> None:
    assert AGING.parse_review_marker(["# T", "", "Status: candidate."], TODAY) == (None, None, None)


# --- the corpus -----------------------------------------------------------


def test_every_candidate_has_a_derivable_start_date() -> None:
    """'No candidate without a date' — enforced, not asserted in prose."""
    rows, errors, classes = AGING.collect(TODAY)
    assert errors == []
    assert classes["candidate"] > 0
    undated = [row["path"] for row in rows if row["since"] is None]
    assert undated == [], f"candidacy start not derivable for: {undated}"
    assert len(rows) == classes["candidate"]


def test_the_report_names_an_aged_candidate_and_stays_silent_otherwise() -> None:
    aged = {
        "path": "docs/governance/EXAMPLE.md",
        "status_head": "candidate support doctrine",
        "since": dt.date(2026, 1, 1),
        "provenance": "observed",
        "record": None,
        "age": 242,
    }
    classes = {"candidate": 1, "other": 0}

    loud = AGING.render([aged], classes, threshold=180, today=TODAY)
    assert "docs/governance/EXAMPLE.md" in loud
    assert "242" in loud

    quiet = AGING.render([aged], classes, threshold=365, today=TODAY)
    assert "docs/governance/EXAMPLE.md" not in quiet
    assert "No candidate has been unresolved" in quiet


def test_age_alone_never_reads_as_a_promotion() -> None:
    """The promotion rule is explicit that age promotes nothing; so is the report."""
    report = AGING.render([], {"candidate": 0, "other": 1}, threshold=180, today=TODAY)
    assert "Age does not promote anything." in report
    assert "referent" in report


# --- history across renames -----------------------------------------------


def _repo_with_a_renamed_candidate(root: Path) -> None:
    """A candidate created long ago, renamed recently, status untouched."""
    def git(*args: str, **env: str) -> None:
        subprocess.run(
            ["git", *args], cwd=root, check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            env={**os.environ, **env},
        )

    (root / "docs" / "governance").mkdir(parents=True)
    (root / "docs" / "governance" / "OLD.md").write_text(
        "# A\n\nStatus: candidate support doctrine — unchanged by the rename.\n",
        encoding="utf-8",
    )
    git("init", "-q", ".")
    git("config", "user.email", "t@example.invalid")
    git("config", "user.name", "t")
    git("add", "-A")
    git("commit", "-qm", "add candidate",
        GIT_AUTHOR_DATE="2026-01-10T10:00:00+00:00",
        GIT_COMMITTER_DATE="2026-01-10T10:00:00+00:00")
    git("mv", "docs/governance/OLD.md", "docs/governance/NEW.md")
    git("commit", "-qm", "rename only",
        GIT_AUTHOR_DATE="2026-08-25T10:00:00+00:00",
        GIT_COMMITTER_DATE="2026-08-25T10:00:00+00:00")


def test_a_rename_does_not_restart_the_candidacy_clock(tmp_path: Path, monkeypatch) -> None:
    """Renaming a candidate must not make a year-old one look new."""
    _repo_with_a_renamed_candidate(tmp_path)
    monkeypatch.setattr(AGING, "ROOT", tmp_path)

    commits = AGING._file_commits("docs/governance/NEW.md")
    assert len(commits) == 2, "history was not followed across the rename"

    blobs = AGING._Blobs(tmp_path)
    try:
        since, provenance = AGING.candidacy_start(
            "docs/governance/NEW.md", blobs, AGING._root_commits()
        )
    finally:
        blobs.close()

    assert since == dt.date(2026, 1, 10), (
        f"clock restarted at the rename instead of the original commit: {since}"
    )
    assert provenance in {"observed", "imported"}


def test_the_blob_is_read_under_the_name_the_file_had_then(tmp_path: Path, monkeypatch) -> None:
    """Following history is useless if the blob lookup uses today's name."""
    _repo_with_a_renamed_candidate(tmp_path)
    monkeypatch.setattr(AGING, "ROOT", tmp_path)

    commits = AGING._file_commits("docs/governance/NEW.md")
    paths = [path for _, _, path in commits]
    assert paths == ["docs/governance/NEW.md", "docs/governance/OLD.md"]

    blobs = AGING._Blobs(tmp_path)
    try:
        oldest_sha, _, oldest_path = commits[-1]
        assert blobs.read(f"{oldest_sha}:{oldest_path}"), "historical blob unreadable"
        assert blobs.read(f"{oldest_sha}:docs/governance/NEW.md") is None, (
            "the new name should not resolve at the older commit"
        )
    finally:
        blobs.close()
