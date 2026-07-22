"""Read-only Work Issue cockpit projection tests."""

from __future__ import annotations

import uuid

import pytest

from mvp_vertical import work_issue_read, work_issues


@pytest.fixture
def conn():
    try:
        connection = work_issues.connect()
    except Exception as exc:  # pragma: no cover - local unit-only environment
        pytest.skip(f"PostgreSQL unreachable: {exc}")
    connection.execute(
        "TRUNCATE issue_events, hermes_runs, issue_comments, work_issues RESTART IDENTITY CASCADE"
    )
    connection.commit()
    yield connection
    connection.close()


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex}"


def _create(conn, *, case_ref: str, title: str) -> dict:
    return work_issues.create_issue(
        conn,
        issue_id=_id("issue"),
        case_ref=case_ref,
        title=title,
        description="Review one bounded project matter without broadening its declared case.",
        created_by="human-reviewer",
        idempotency_key=_id("create"),
    )


def test_list_issue_projections_matches_exact_case_and_prioritizes_waiting(conn) -> None:
    open_projection = _create(
        conn,
        case_ref="project-maison-a",
        title="Review the current project document",
    )
    waiting_projection = _create(
        conn,
        case_ref="project-maison-a",
        title="Clarify one missing project source",
    )
    _create(
        conn,
        case_ref="project-other",
        title="Unrelated project matter",
    )

    waiting_issue = waiting_projection["work_issue"]
    work_issues.transition_issue(
        conn,
        issue_id=waiting_issue["issue_id"],
        to_status="waiting",
        actor="human-reviewer",
        actor_kind="human",
        expected_version=waiting_issue["version"],
        idempotency_key=_id("wait"),
    )

    listed = work_issue_read.list_issue_projections(conn, "project-maison-a")

    assert [item["work_issue"]["status"] for item in listed] == ["waiting", "open"]
    assert {item["work_issue"]["case_ref"] for item in listed} == {"project-maison-a"}
    assert open_projection["work_issue"]["issue_id"] in {
        item["work_issue"]["issue_id"] for item in listed
    }


def test_list_issue_projections_refuses_unbounded_limit(conn) -> None:
    with pytest.raises(work_issues.WorkIssueError, match="limit"):
        work_issue_read.list_issue_projections(conn, "project-maison-a", limit=501)
