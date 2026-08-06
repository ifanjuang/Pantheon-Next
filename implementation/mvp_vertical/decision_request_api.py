"""Human attention and Decision record API.

Decision Request creation and resolution require the editor key and a human
actor. Hermes may later project a typed Execution Result through a separately
reviewed adapter; it cannot call these canonical write routes directly.
"""

from __future__ import annotations

from typing import Any, Callable, Literal

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field, model_validator

from . import decision_requests


DecisionType = Literal["question", "validation", "approval", "arbitration"]
Priority = Literal["low", "normal", "high", "urgent"]
ResponseMode = Literal[
    "decision_value", "single_option", "multiple_options", "free_text"
]
DecisionValue = Literal[
    "approve", "refuse", "request_revision", "request_more_evidence"
]
IdentityAssurance = Literal["declared", "authenticated"]
RequestStatus = Literal["pending", "resolved", "cancelled"]


class DigestBody(BaseModel):
    algorithm: Literal["sha256"] = "sha256"
    value: str = Field(pattern=r"^[a-f0-9]{64}$")


class DecisionOptionBody(BaseModel):
    option_id: str = Field(pattern=r"^[a-z0-9][a-z0-9._-]*$")
    label: str = Field(min_length=1, max_length=1000)
    consequence: str = Field(min_length=1, max_length=10000)
    limitations: list[str] = Field(default_factory=list, max_length=50)


class DecisionRequestCreateBody(BaseModel):
    request_id: str = Field(pattern=r"^[a-z0-9][a-z0-9._-]*$")
    decision_type: DecisionType
    question: str = Field(min_length=1, max_length=20000)
    priority: Priority = "normal"
    response_mode: ResponseMode
    options: list[DecisionOptionBody] = Field(default_factory=list, max_length=50)
    recommendation_candidate: str | None = Field(default=None, min_length=1)
    blocking: bool = False
    project_ref: str | None = Field(
        default=None,
        pattern=r"^[a-z0-9][a-z0-9._-]*$",
    )
    work_issue_ref: str | None = Field(
        default=None,
        pattern=r"^[a-z0-9][a-z0-9._-]*$",
    )
    conversation_ref: str | None = Field(default=None, min_length=1)
    candidate_ref: str = Field(min_length=1)
    candidate_digest: DigestBody
    evidence_pack_ref: str | None = Field(default=None, min_length=1)
    evidence_pack_digest: DigestBody | None = None
    source_refs: list[str] = Field(default_factory=list, max_length=200)
    evidence_gaps: list[str] = Field(default_factory=list, max_length=200)
    blocked_action: str | None = Field(default=None, max_length=20000)
    next_safe_action: str | None = Field(default=None, max_length=20000)
    decision_surface: str = Field(min_length=1, max_length=500)
    decision_owner: str = Field(min_length=1, max_length=500)
    idempotency_key: str = Field(min_length=8, max_length=200)

    @model_validator(mode="after")
    def validate_request_shape(self):
        if self.blocking and not self.work_issue_ref:
            raise ValueError("blocking Decision Request requires work_issue_ref")
        if self.response_mode in {"single_option", "multiple_options"}:
            if len(self.options) < 2:
                raise ValueError("option response mode requires at least two options")
        elif self.options:
            raise ValueError("decision_value and free_text requests cannot carry options")
        option_ids = {option.option_id for option in self.options}
        if len(option_ids) != len(self.options):
            raise ValueError("Decision option identifiers must be unique")
        if self.recommendation_candidate and self.recommendation_candidate not in option_ids:
            raise ValueError("recommendation_candidate must reference one option")
        if bool(self.evidence_pack_ref) != bool(self.evidence_pack_digest):
            raise ValueError("Evidence Pack reference and digest must be supplied together")
        return self


class AuthenticatedPrincipalBody(BaseModel):
    user_id: str = Field(min_length=1, max_length=500)
    display_name: str | None = Field(default=None, min_length=1, max_length=500)
    identity_provider: str = Field(min_length=1, max_length=500)


class ResolveDecisionRequestBody(BaseModel):
    decision_id: str = Field(pattern=r"^[a-z0-9][a-z0-9._-]*$")
    decision: DecisionValue
    identity_assurance: IdentityAssurance = "declared"
    authenticated_principal: AuthenticatedPrincipalBody | None = None
    expected_revision: int = Field(ge=1)
    idempotency_key: str = Field(min_length=8, max_length=200)
    selected_option_ids: list[str] = Field(default_factory=list, max_length=50)
    response_text: str | None = Field(default=None, max_length=20000)
    rationale: str | None = Field(default=None, max_length=20000)

    @model_validator(mode="after")
    def validate_identity_shape(self):
        if self.identity_assurance == "authenticated" and self.authenticated_principal is None:
            raise ValueError("authenticated assurance requires authenticated_principal")
        if self.identity_assurance == "declared" and self.authenticated_principal is not None:
            raise ValueError("declared assurance cannot carry authenticated_principal")
        return self


class CancelDecisionRequestBody(BaseModel):
    expected_revision: int = Field(ge=1)
    idempotency_key: str = Field(min_length=8, max_length=200)
    rationale: str = Field(min_length=1, max_length=20000)


def install_decision_request_routes(
    app: FastAPI,
    *,
    with_connection: Callable,
    require_read_key: Callable,
    require_editor_key: Callable,
    require_human_actor: Callable,
) -> None:
    def execute(operation):
        try:
            return with_connection(operation)
        except (
            decision_requests.DecisionRequestNotFound,
            decision_requests.DecisionRecordNotFound,
        ) as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except (
            decision_requests.StaleDecisionRequest,
            decision_requests.DecisionRequestConflict,
        ) as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except decision_requests.DecisionRequestError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post("/decision-requests", status_code=201)
    def create_decision_request(
        body: DecisionRequestCreateBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict[str, Any]:
        values = body.model_dump()
        values["candidate_digest"] = values["candidate_digest"]["value"]
        if values.get("evidence_pack_digest"):
            values["evidence_pack_digest"] = values["evidence_pack_digest"]["value"]
        values["options"] = [option.model_dump() for option in body.options]
        projection = execute(
            lambda conn: decision_requests.create_request(
                conn,
                created_by=actor,
                **values,
            )
        )
        return {
            "effect": "decision_request_created",
            "request_is_not_decision": True,
            "runtime_continuation_authorized": False,
            **projection,
        }

    @app.get("/decision-requests")
    def list_decision_requests(
        status: RequestStatus | None = "pending",
        project_ref: str | None = None,
        work_issue_ref: str | None = None,
        limit: int = 100,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        items = execute(
            lambda conn: decision_requests.list_requests(
                conn,
                status=status,
                project_ref=project_ref,
                work_issue_ref=work_issue_ref,
                limit=limit,
            )
        )
        return {
            "decision_requests": items,
            "attention_only_when_pending": True,
        }

    @app.get("/agency/projects/{project_id}/decision-requests")
    def list_project_decision_requests(
        project_id: str,
        status: RequestStatus | None = "pending",
        limit: int = 100,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        items = execute(
            lambda conn: decision_requests.list_requests(
                conn,
                status=status,
                project_ref=project_id,
                limit=limit,
            )
        )
        return {
            "project_ref": project_id,
            "decision_requests": items,
            "projection_only": True,
        }

    @app.get("/work/issues/{issue_id}/blocking-decision-request")
    def get_work_issue_blocking_decision(
        issue_id: str,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        items = execute(
            lambda conn: decision_requests.list_requests(
                conn,
                status="pending",
                work_issue_ref=issue_id,
                limit=100,
            )
        )
        blocking = [
            item
            for item in items
            if item["decision_request"]["blocking"] is True
        ]
        return {
            "work_issue_ref": issue_id,
            "blocking_decision_request": blocking[0] if blocking else None,
            "work_issue_transitioned": False,
        }

    @app.get("/decision-requests/{request_id}")
    def get_decision_request(
        request_id: str,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        return execute(lambda conn: decision_requests.get_request(conn, request_id))

    @app.post("/decision-requests/{request_id}/resolve")
    def resolve_decision_request(
        request_id: str,
        body: ResolveDecisionRequestBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict[str, Any]:
        values = body.model_dump()
        principal = values.get("authenticated_principal")
        if principal is not None:
            values["authenticated_principal"] = principal
        projection = execute(
            lambda conn: decision_requests.resolve_request(
                conn,
                request_id=request_id,
                decided_by=actor,
                **values,
            )
        )
        return {
            "effect": "decision_recorded",
            "work_issue_transitioned": False,
            "runtime_continuation_authorized": False,
            "action_executed": False,
            **projection,
        }

    @app.post("/decision-requests/{request_id}/cancel")
    def cancel_decision_request(
        request_id: str,
        body: CancelDecisionRequestBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict[str, Any]:
        projection = execute(
            lambda conn: decision_requests.cancel_request(
                conn,
                request_id=request_id,
                cancelled_by=actor,
                **body.model_dump(),
            )
        )
        return {
            "effect": "decision_request_cancelled",
            "decision_recorded": False,
            "runtime_continuation_authorized": False,
            **projection,
        }

    @app.get("/decisions/{decision_id}")
    def get_decision_record(
        decision_id: str,
        _authorized: None = Depends(require_read_key),
    ) -> dict[str, Any]:
        return execute(lambda conn: decision_requests.get_decision(conn, decision_id))
