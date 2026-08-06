"""FastAPI routes for semantic ProjectClaims.

Global Claim reads use the normal Agency Data read gate. Direct Claim creation is
human only and cannot cite an Execution Result; that path is owned by the reviewed
candidate transition in execution_result_api.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Callable, Literal

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import agency_claims


class ClaimBackingRefBody(BaseModel):
    entity_type: str = Field(min_length=1, max_length=120)
    entity_id: str = Field(min_length=1, max_length=500)
    observed_status: str | None = Field(default=None, max_length=120)


class ProjectClaimCreateBody(BaseModel):
    claim_type: str = Field(min_length=1, max_length=120)
    value: Any
    source_kind: Literal[
        "information",
        "document",
        "human_assertion",
        "derived",
        "external_projection",
    ] = "human_assertion"
    backing_ref: ClaimBackingRefBody | None = None
    source_ref: str | None = Field(default=None, max_length=2000)
    derivation_note: str | None = Field(default=None, max_length=10_000)
    status: Literal["asserted", "source_backed", "verified", "contested", "retired"] = "asserted"
    certainty: Literal["E0", "E1", "E2", "E3", "E4"] = "E0"
    observed_at: datetime | None = None
    effective_at: datetime | None = None
    supersedes: str | None = Field(default=None, max_length=200)
    note: str | None = Field(default=None, max_length=10_000)


def install_agency_claim_routes(
    app: FastAPI,
    *,
    with_connection: Callable,
    require_global_agency_read: Callable,
    require_human_agency_writer: Callable,
    require_actor: Callable,
) -> None:
    def claim_operation(operation):
        try:
            return with_connection(operation)
        except agency_claims.ClaimNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except agency_claims.AgencyClaimError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.get("/agency/projects/{project_id}/claims")
    def list_project_claims(
        project_id: str,
        _authorized: None = Depends(require_global_agency_read),
    ) -> dict:
        claims = claim_operation(lambda conn: agency_claims.list_project_claims(conn, project_id))
        values, refs = claim_operation(lambda conn: agency_claims.project_claim_projection(conn, project_id))
        return {
            "system_of_record": "postgres",
            "project_id": project_id,
            "claims": claims,
            "claim_values": values,
            "claim_refs": refs,
            "claim_is_visible_card_family": False,
            "authorization_inferred": False,
        }

    @app.post("/agency/projects/{project_id}/claims", status_code=201)
    def create_project_claim(
        project_id: str,
        body: ProjectClaimCreateBody,
        _writer_kind: Literal["human"] = Depends(require_human_agency_writer),
        actor: str = Depends(require_actor),
    ) -> dict:
        values = body.model_dump(exclude_none=True)
        if body.backing_ref is not None:
            values["backing_ref"] = body.backing_ref.model_dump(exclude_none=True)
        claim = claim_operation(
            lambda conn: agency_claims.record_claim(
                conn,
                project_id=project_id,
                actor=actor,
                **values,
            )
        )
        return {
            "system_of_record": "postgres",
            "claim": claim,
            "project_mutated": False,
            "evidence_admitted": False,
            "approval_inferred": False,
        }
