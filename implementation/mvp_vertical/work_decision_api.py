"""Human decision endpoints over Work Issues already waiting for review.

A Decision card is only a Cockpit projection of a governed Work Issue. Accepting
closes that issue as answered; refusing returns it to in_progress. This module
adds no workflow engine and grants no authority to Hermes.
"""

from __future__ import annotations

from typing import Callable

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import work_issue_read, work_issues


class WorkDecisionBody(BaseModel):
    expected_version: int = Field(ge=1)
    idempotency_key: str = Field(min_length=8, max_length=200)


def install_work_decision_routes(
    app: FastAPI,
    *,
    require_editor_key: Callable,
    require_human_actor: Callable,
    with_connection: Callable,
) -> None:
    def decide(operation):
        try:
            return with_connection(operation)
        except work_issues.IssueNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except work_issues.StaleWrite as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except (work_issues.TransitionRefused, work_issues.WorkIssueError) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.get("/work/issues/{issue_id}/decision")
    def get_work_decision(
        issue_id: str,
        _authorized: None = Depends(require_editor_key),
    ) -> dict:
        issue = decide(lambda conn: work_issue_read.get_issue_record(conn, issue_id))
        return {
            "work_issue": issue,
            "decision_available": issue.get("status") == "review",
        }

    @app.post("/work/issues/{issue_id}/decision/validate")
    def validate_work_decision(
        issue_id: str,
        body: WorkDecisionBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        projection = decide(
            lambda conn: work_issues.close_issue(
                conn,
                issue_id=issue_id,
                decided_by=actor,
                close_reason="answered",
                expected_version=body.expected_version,
                idempotency_key=body.idempotency_key,
            )
        )
        return {
            "effect": "work_decision_validated",
            "approval_inferred": False,
            "work_issue": projection,
        }

    @app.post("/work/issues/{issue_id}/decision/refuse")
    def refuse_work_decision(
        issue_id: str,
        body: WorkDecisionBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        projection = decide(
            lambda conn: work_issues.transition_issue(
                conn,
                issue_id=issue_id,
                to_status="in_progress",
                actor=actor,
                actor_kind="human",
                expected_version=body.expected_version,
                idempotency_key=body.idempotency_key,
            )
        )
        return {
            "effect": "work_decision_refused_for_rework",
            "approval_inferred": False,
            "work_issue": projection,
        }
