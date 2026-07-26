"""Read-only Work Issue projections for the cards-first cockpit.

The adapter reads the governed Work Issue aggregate plus optional Work Card
presentation metadata. It creates no card record, changes no issue status and
grants no Hermes authority.
"""

from __future__ import annotations

import psycopg
from psycopg.rows import dict_row

from . import work_issues


_STATUS_ORDER = {
    "review": 0,
    "waiting": 1,
    "open": 2,
    "in_progress": 3,
    "done": 4,
    "cancelled": 5,
}


def _metadata(conn: psycopg.Connection, issue_id: str) -> dict:
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            "SELECT workflow, information_ref, result_ref, decision_request "
            "FROM work_card_metadata WHERE issue_id = %s",
            (issue_id,),
        )
        row = cur.fetchone()
    if row is None:
        return {
            "workflow": {},
            "information_ref": None,
            "result_ref": None,
            "decision_request": {},
        }
    return dict(row)


def _card_projection(issue: dict, metadata: dict) -> dict:
    """Expose workflow metadata without changing the governed Work Issue object."""
    projected = dict(issue)
    workflow = metadata.get("workflow") if isinstance(metadata.get("workflow"), dict) else {}
    decision = (
        metadata.get("decision_request")
        if isinstance(metadata.get("decision_request"), dict)
        else {}
    )

    projected["objective"] = workflow.get("objective") or issue.get("description")
    projected["milestones"] = workflow.get("milestones") or []
    projected["responsibilities"] = workflow.get("responsibilities") or []
    projected["skills"] = workflow.get("skills") or []
    projected["functions"] = workflow.get("functions") or []
    projected["tools"] = workflow.get("tools") or []
    projected["information_ref"] = metadata.get("information_ref")
    projected["result_ref"] = metadata.get("result_ref")
    projected["decision_title"] = decision.get("title")
    projected["decision_question"] = decision.get("question")
    projected["result_summary"] = decision.get("result_summary")
    projected["decision_options"] = decision.get("options") or []
    return projected


def get_issue_record(conn: psycopg.Connection, issue_id: str) -> dict:
    """Return the Work Issue record with read-only Card metadata projected on top."""
    projection = work_issues.get_issue(conn, issue_id)
    issue = projection.get("work_issue")
    if not isinstance(issue, dict):
        raise work_issues.WorkIssueError(
            "stored Work Issue projection is missing its work_issue record"
        )
    return _card_projection(issue, _metadata(conn, issue_id))


def list_issue_projections(
    conn: psycopg.Connection,
    case_ref: str,
    *,
    include_terminal: bool = True,
    limit: int = 100,
) -> list[dict]:
    """Return governed Work Issue aggregates for one exact case reference.

    `case_ref` is matched exactly. The function does not infer project identity,
    traverse parents or broaden scope. Work Card metadata is joined only for the
    Cockpit read projection; it does not schedule, dispatch or authorize.
    """
    if not case_ref.strip():
        raise work_issues.WorkIssueError("case_ref is required")
    if limit < 1 or limit > 500:
        raise work_issues.WorkIssueError("limit must be between 1 and 500")

    terminal_filter = "" if include_terminal else "AND status NOT IN ('done', 'cancelled')"
    with conn.cursor() as cur:
        cur.execute(
            f"""
            SELECT issue_id
              FROM work_issues
             WHERE case_ref = %s
               {terminal_filter}
             ORDER BY updated_at DESC, issue_id ASC
             LIMIT %s
            """,
            (case_ref, limit),
        )
        issue_ids = [row[0] for row in cur.fetchall()]

    projections = [work_issues.get_issue(conn, issue_id) for issue_id in issue_ids]
    for projection in projections:
        issue = projection.get("work_issue")
        if isinstance(issue, dict):
            projection["work_issue"] = _card_projection(
                issue,
                _metadata(conn, issue["issue_id"]),
            )

    projections.sort(
        key=lambda projection: _STATUS_ORDER.get(
            projection["work_issue"]["status"], 99
        )
    )
    return projections
