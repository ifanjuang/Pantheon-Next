"""Read-only Work Issue projections for the cards-first cockpit.

The adapter reads the existing Work Issue aggregate and append-only events. It
creates no card record, changes no issue status and grants no Hermes authority.
"""

from __future__ import annotations

import psycopg

from . import work_issues


_STATUS_ORDER = {
    "review": 0,
    "waiting": 1,
    "open": 2,
    "in_progress": 3,
    "done": 4,
    "cancelled": 5,
}


def list_issue_projections(
    conn: psycopg.Connection,
    case_ref: str,
    *,
    include_terminal: bool = True,
    limit: int = 100,
) -> list[dict]:
    """Return governed Work Issue projections for one exact case reference.

    `case_ref` is matched exactly. The function does not infer project identity,
    traverse parents or broaden scope. Full aggregate projections are returned so
    the cockpit can show comments, Hermes runs and append-only event history.
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
    # Python sort is stable: status priority changes grouping while preserving
    # the database's newest-first order inside each status group.
    projections.sort(
        key=lambda projection: _STATUS_ORDER.get(
            projection["work_issue"]["status"], 99
        )
    )
    return projections
