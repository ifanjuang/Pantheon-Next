"""Cockpit API for explicit qualification of one exact Workspace PDF with Hermes."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Mapping

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import hermes_handoff_store, workspace_qualification


class WorkspaceQualificationPreviewBody(BaseModel):
    project_id: str = Field(min_length=1, max_length=300)
    workspace_ref: str = Field(min_length=1, max_length=200)
    relative_path: str = Field(min_length=1, max_length=4096)
    prepare_markdown: bool = False
    user_instruction: str | None = Field(default=None, max_length=2_000)


class WorkspaceQualificationSubmitBody(WorkspaceQualificationPreviewBody):
    expected_preview_digest: str = Field(min_length=32, max_length=128)
    expected_task_contract_ref: str = Field(min_length=16, max_length=200)
    expected_context_pack_ref: str = Field(min_length=16, max_length=200)
    idempotency_key: str = Field(min_length=8, max_length=200)


def install_workspace_qualification_routes(
    app: FastAPI,
    *,
    workspace_roots: Mapping[str, str | Path],
    with_connection: Callable,
    require_read_key: Callable,
    require_editor_key: Callable,
    require_human_actor: Callable,
) -> None:
    """Mount the workspace->Hermes qualification bridge without adding a new owner."""

    def prepare(body: WorkspaceQualificationPreviewBody) -> dict:
        try:
            return with_connection(
                lambda conn: workspace_qualification.build_workspace_qualification_preview(
                    conn,
                    workspace_roots=workspace_roots,
                    project_id=body.project_id,
                    workspace_ref=body.workspace_ref,
                    relative_path=body.relative_path,
                    prepare_markdown=body.prepare_markdown,
                    user_instruction=body.user_instruction,
                )
            )
        except workspace_qualification.WorkspaceQualificationError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.post("/cockpit/workspace-qualifications/preview")
    def preview_workspace_qualification(
        body: WorkspaceQualificationPreviewBody,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        return prepare(body)

    @app.post("/cockpit/workspace-qualifications/submit", status_code=201)
    def submit_workspace_qualification(
        body: WorkspaceQualificationSubmitBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        current = prepare(
            WorkspaceQualificationPreviewBody(
                project_id=body.project_id,
                workspace_ref=body.workspace_ref,
                relative_path=body.relative_path,
                prepare_markdown=body.prepare_markdown,
                user_instruction=body.user_instruction,
            )
        )
        stale = (
            current["preview_digest"] != body.expected_preview_digest
            or current["task_contract"]["task_contract_ref"] != body.expected_task_contract_ref
            or current["context_pack"]["context_pack_ref"] != body.expected_context_pack_ref
        )
        if stale:
            raise HTTPException(
                status_code=409,
                detail=(
                    "workspace qualification preview is stale; the file or request basis changed, "
                    "prepare it again before submission"
                ),
            )
        try:
            result = with_connection(
                lambda conn: hermes_handoff_store.submit_handoff(
                    conn,
                    actor=actor,
                    idempotency_key=body.idempotency_key,
                    question=current["question"],
                    preview=current,
                    card_context_envelope=current["resolved_card_context_envelope"],
                    selected_context=current["resolved_selected_context"],
                    include_declared_descendants=False,
                )
            )
        except hermes_handoff_store.HandoffIdempotencyConflict as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except hermes_handoff_store.HandoffSubmissionError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {
            **result,
            "qualification_kind": current["qualification_kind"],
            "workspace_observation": current["workspace_observation"],
            "workspace_source_ref": current["workspace_source_ref"],
            "prepare_markdown_candidate": current["prepare_markdown_candidate"],
            "execution_authorized": False,
            "workspace_write_requested": False,
            "markdown_write_requested": False,
            "non_equivalences": [
                "qualification submitted != Hermes run started",
                "Work Issue created != execution authorized",
                "prepare Markdown candidate != workspace write",
                "qualification candidate != Document admission",
            ],
        }
