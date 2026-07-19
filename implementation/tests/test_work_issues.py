"""PostgreSQL acceptance tests for the minimal Work Issue vertical slice."""

from __future__ import annotations

import uuid

import psycopg
import pytest

from mvp_vertical import work_issues


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


def _create(conn) -> dict:
    return work_issues.create_issue(
        conn,
        issue_id=_id("issue"),
        case_ref="case-fictional-renovation",
        title="Verify contractor quote",
        description="Compare the quote against the declared CCTP scope.",
        created_by="human-reviewer",
        assigned_to="hermes",
        task_contract_ref="tc-fictional-001",
        context_pack_ref="cp-fictional-001",
        idempotency_key=_id("create"),
    )


def test_complete_issue_comment_hermes_review_human_close_path(conn) -> None:
    projection = _create(conn)
    issue_id = projection["work_issue"]["issue_id"]
    assert projection["work_issue"]["status"] == "open"
    assert projection["work_issue"]["version"] == 1

    projection = work_issues.add_comment(
        conn,
        issue_id=issue_id,
        comment_id=_id("comment"),
        body="Check option items separately.",
        author="human-reviewer",
        expected_version=1,
        idempotency_key=_id("comment-event"),
    )
    assert projection["work_issue"]["status"] == "open"
    assert projection["work_issue"]["version"] == 2
    assert len(projection["comments"]) == 1

    run_id = _id("run")
    projection = work_issues.start_hermes_run(
        conn,
        issue_id=issue_id,
        run_id=run_id,
        task_contract_ref="tc-fictional-001",
        context_pack_ref="cp-fictional-001",
        actor="hermes-adapter",
        expected_version=2,
        idempotency_key=_id("start"),
    )
    assert projection["work_issue"]["status"] == "in_progress"
    assert projection["hermes_runs"][0]["status"] == "running"

    projection = work_issues.record_hermes_return(
        conn,
        issue_id=issue_id,
        run_id=run_id,
        normalized_return={
            "outcome": "result_candidate",
            "summary": "One discrepancy is ready for human review.",
            "result_refs": ["result-fictional-001"],
            "evidence_candidate_refs": ["evidence-fictional-001"],
            "trace_refs": ["trace-fictional-001"],
        },
        actor="hermes-adapter",
        expected_version=3,
        idempotency_key=_id("return"),
    )
    assert projection["work_issue"]["status"] == "review"
    assert "close_reason" not in projection["work_issue"]
    assert projection["hermes_runs"][0]["status"] == "returned"

    projection = work_issues.close_issue(
        conn,
        issue_id=issue_id,
        decided_by="human-reviewer",
        close_reason="answered",
        expected_version=4,
        idempotency_key=_id("close"),
    )
    assert projection["work_issue"]["status"] == "done"
    assert projection["work_issue"]["close_reason"] == "answered"
    assert {event["event_type"] for event in projection["events"]} >= {
        "issue_created",
        "comment_added",
        "hermes_started",
        "hermes_returned",
        "review_requested",
        "issue_closed",
    }


def test_hermes_cannot_close_issue(conn) -> None:
    projection = _create(conn)
    issue = projection["work_issue"]
    with pytest.raises(work_issues.TransitionRefused):
        work_issues.transition_issue(
            conn,
            issue_id=issue["issue_id"],
            to_status="cancelled",
            actor="hermes-adapter",
            actor_kind="hermes",
            expected_version=issue["version"],
            idempotency_key=_id("forbidden-close"),
            close_reason="cancelled",
        )


def test_stale_write_is_refused_without_partial_effect(conn) -> None:
    projection = _create(conn)
    issue_id = projection["work_issue"]["issue_id"]
    work_issues.add_comment(
        conn,
        issue_id=issue_id,
        comment_id=_id("comment"),
        body="First current comment.",
        author="human-reviewer",
        expected_version=1,
        idempotency_key=_id("comment-event"),
    )
    with pytest.raises(work_issues.StaleWrite):
        work_issues.add_comment(
            conn,
            issue_id=issue_id,
            comment_id=_id("stale-comment"),
            body="Stale comment.",
            author="human-reviewer",
            expected_version=1,
            idempotency_key=_id("stale-event"),
        )
    assert len(work_issues.get_issue(conn, issue_id)["comments"]) == 1


def test_events_are_append_only_in_postgres(conn) -> None:
    projection = _create(conn)
    event_id = projection["events"][0]["event_id"]
    with pytest.raises(psycopg.errors.RaiseException, match="append-only"):
        conn.execute("UPDATE issue_events SET actor = 'rewritten' WHERE event_id = %s", (event_id,))
    conn.rollback()
    with pytest.raises(psycopg.errors.RaiseException, match="append-only"):
        conn.execute("DELETE FROM issue_events WHERE event_id = %s", (event_id,))
    conn.rollback()


def test_idempotent_replay_does_not_duplicate_comment_or_event(conn) -> None:
    projection = _create(conn)
    issue_id = projection["work_issue"]["issue_id"]
    key = _id("comment-event")
    comment_id = _id("comment")
    first = work_issues.add_comment(
        conn,
        issue_id=issue_id,
        comment_id=comment_id,
        body="One durable note.",
        author="human-reviewer",
        expected_version=1,
        idempotency_key=key,
    )
    replay = work_issues.add_comment(
        conn,
        issue_id=issue_id,
        comment_id=comment_id,
        body="One durable note.",
        author="human-reviewer",
        expected_version=1,
        idempotency_key=key,
    )
    assert replay["work_issue"]["version"] == first["work_issue"]["version"]
    assert len(replay["comments"]) == 1


def test_run_must_match_issue_contract_and_context(conn) -> None:
    projection = _create(conn)
    issue = projection["work_issue"]
    with pytest.raises(work_issues.TransitionRefused, match="Task Contract"):
        work_issues.start_hermes_run(
            conn,
            issue_id=issue["issue_id"],
            run_id=_id("run"),
            task_contract_ref="tc-other",
            context_pack_ref="cp-fictional-001",
            actor="hermes-adapter",
            expected_version=issue["version"],
            idempotency_key=_id("start"),
        )


def test_invalid_issue_is_rolled_back_before_commit(conn) -> None:
    issue_id = _id("issue")
    with pytest.raises(work_issues.WorkIssueError, match="governed contract"):
        work_issues.create_issue(
            conn,
            issue_id=issue_id,
            case_ref="case-fictional-renovation",
            title="x",
            description="Too-short title must not persist.",
            created_by="human-reviewer",
            idempotency_key=_id("create"),
        )
    with pytest.raises(work_issues.IssueNotFound):
        work_issues.get_issue(conn, issue_id)
