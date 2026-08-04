"""Bounded API routes for execution results and review dispositions."""

from __future__ import annotations

from typing import Any, Callable

from fastapi import Depends, Header, HTTPException, Query

from . import execution_results


def _translate_error(exc: Exception) -> HTTPException:
    if isinstance(exc, execution_results.ExecutionResultNotFound):
        return HTTPException(status_code=404, detail=str(exc))
    if isinstance(exc, execution_results.ExecutionResultConflict):
        return HTTPException(status_code=409, detail=str(exc))
    if isinstance(exc, execution_results.ExecutionResultError):
        return HTTPException(status_code=422, detail=str(exc))
    return HTTPException(status_code=500, detail="execution result operation failed")


def install_execution_result_routes(
    app,
    *,
    with_connection: Callable[[Callable[..., Any]], Any],
    require_read_key,
    require_hermes_key,
) -> None:
    @app.post("/execution-results", dependencies=[Depends(require_hermes_key)])
    def submit_execution_result(
        payload: dict[str, Any],
        idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
    ) -> dict[str, Any]:
        try:
            stored = with_connection(
                lambda conn: execution_results.store_execution_result(
                    conn,
                    execution_result=payload,
                    idempotency_key=idempotency_key or "",
                )
            )
        except Exception as exc:  # translated into bounded HTTP errors
            raise _translate_error(exc) from exc
        return {
            "status": "recorded",
            "execution": stored,
            "result_stored": True,
            "result_accepted": False,
            "apu_mutated": False,
            "evidence_admitted": False,
            "memory_promoted": False,
            "external_effect_authorized": False,
        }

    @app.get(
        "/execution-results/{execution_result_id}",
        dependencies=[Depends(require_read_key)],
    )
    def read_execution_result(execution_result_id: str) -> dict[str, Any]:
        try:
            return with_connection(
                lambda conn: execution_results.get_execution_result(conn, execution_result_id)
            )
        except Exception as exc:
            raise _translate_error(exc) from exc

    @app.get(
        "/projects/{project_ref}/execution-results",
        dependencies=[Depends(require_read_key)],
    )
    def list_execution_results(
        project_ref: str,
        limit: int = Query(default=50, ge=1, le=200),
    ) -> dict[str, Any]:
        try:
            items = with_connection(
                lambda conn: execution_results.list_project_execution_results(
                    conn, project_ref=project_ref, limit=limit
                )
            )
        except Exception as exc:
            raise _translate_error(exc) from exc
        return {"project_ref": project_ref, "items": items, "count": len(items)}

    @app.post(
        "/execution-results/{execution_result_id}/results/{result_ref}/dispositions",
        dependencies=[Depends(require_read_key)],
    )
    def review_result_candidate(
        execution_result_id: str,
        result_ref: str,
        payload: dict[str, Any],
        human_actor: str | None = Header(default=None, alias="X-Pantheon-Human-Actor"),
        idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
    ) -> dict[str, Any]:
        actor = (human_actor or "").strip()
        if not actor:
            raise HTTPException(status_code=422, detail="X-Pantheon-Human-Actor is required")
        try:
            current = with_connection(
                lambda conn: execution_results.get_execution_result(conn, execution_result_id)
            )
            if result_ref not in {item["result_id"] for item in current["results"]}:
                raise execution_results.ExecutionResultNotFound(
                    "result candidate does not belong to execution result"
                )
            stored = with_connection(
                lambda conn: execution_results.append_review_disposition(
                    conn,
                    result_ref=result_ref,
                    disposition=str(payload.get("disposition") or ""),
                    reviewer=actor,
                    reviewer_kind="human",
                    note=payload.get("note"),
                    idempotency_key=idempotency_key or "",
                )
            )
        except Exception as exc:
            raise _translate_error(exc) from exc
        return {
            "status": "recorded",
            "execution": stored,
            "review_disposition_recorded": True,
            "human_decision_recorded": False,
            "apu_mutated": False,
            "evidence_admitted": False,
            "memory_promoted": False,
            "external_effect_authorized": False,
        }
