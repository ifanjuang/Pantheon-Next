"""Cockpit API for previewing and submitting a scoped Hermes handoff.

Preview prepares exact Task Contract / Context Pack candidates. Explicit human
submission may persist those exact snapshots and create a Work Issue assigned to
Hermes. This module never starts an Hermes run.
"""

from __future__ import annotations

import hmac
from typing import Callable

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

from . import card_scope, hermes_handoff_preview, hermes_handoff_store
from .app_lifecycle import install_post_start_initializer
from .hermes_execution_api import install_hermes_execution_routes
from .work_decision_api import install_work_decision_routes


class EntityRefBody(BaseModel):
    entity_id: str = Field(min_length=1, max_length=500)
    entity_type: str = Field(min_length=1, max_length=200)


class CardContextEnvelopeBody(BaseModel):
    root_entity: EntityRefBody
    descendants: list[EntityRefBody] = Field(default_factory=list, max_length=250)
    source_refs: list[str] = Field(default_factory=list, max_length=500)
    explicit_additions: list[EntityRefBody] = Field(default_factory=list, max_length=250)
    explicit_exclusions: list[EntityRefBody] = Field(default_factory=list, max_length=250)
    scope_widened_implicitly: bool = False


class HermesHandoffPreviewBody(BaseModel):
    question: str = Field(min_length=3, max_length=8_000)
    card_context_envelope: CardContextEnvelopeBody
    selected_context: list[EntityRefBody] = Field(default_factory=list, max_length=250)
    include_declared_descendants: bool = False


class HermesHandoffSubmitBody(HermesHandoffPreviewBody):
    expected_preview_digest: str = Field(min_length=32, max_length=128)
    expected_task_contract_ref: str = Field(min_length=16, max_length=200)
    expected_context_pack_ref: str = Field(min_length=16, max_length=200)
    idempotency_key: str = Field(min_length=8, max_length=200)


def _bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        return ""
    return authorization.removeprefix("Bearer ").strip()


def install_hermes_handoff_preview_routes(
    app: FastAPI,
    *,
    require_read_key: Callable,
    require_editor_key: Callable | None = None,
    require_human_actor: Callable | None = None,
    with_connection: Callable | None = None,
) -> None:
    def use_connection(operation):
        if with_connection is not None:
            return with_connection(operation)
        conn = app.state.connect_fn()
        try:
            return operation(conn)
        finally:
            conn.close()

    if require_editor_key is None:
        def require_editor_key(authorization: str | None = Header(default=None)) -> None:
            expected = getattr(app.state, "editor_api_key", "")
            if not expected:
                raise HTTPException(status_code=503, detail="editor API key is not configured")
            if not hmac.compare_digest(_bearer_token(authorization), expected):
                raise HTTPException(status_code=401, detail="invalid editor API key")

    if require_human_actor is None:
        def require_human_actor(
            x_pantheon_human_actor: str | None = Header(default=None, alias="X-Pantheon-Human-Actor"),
        ) -> str:
            if not x_pantheon_human_actor or not x_pantheon_human_actor.strip():
                raise HTTPException(
                    status_code=422,
                    detail="X-Pantheon-Human-Actor is required for Hermes handoff submission",
                )
            return x_pantheon_human_actor.strip()

    connect_fn = getattr(app.state, "connect_fn", None)
    if (
        getattr(connect_fn, "__module__", "") == "mvp_vertical.cockpit_shell"
        and getattr(connect_fn, "__name__", "") == "connect_cockpit"
    ):
        def initialize_handoff_schema() -> None:
            conn = connect_fn()
            try:
                conn.execute(hermes_handoff_store.MIGRATION.read_text(encoding="utf-8"))
                conn.commit()
            finally:
                conn.close()

        install_post_start_initializer(app, initialize_handoff_schema)

    def prepare(body: HermesHandoffPreviewBody) -> dict:
        requested = body.card_context_envelope
        if requested.scope_widened_implicitly:
            raise HTTPException(
                status_code=422,
                detail="Card Context Envelope may not widen scope implicitly",
            )
        if requested.descendants or requested.source_refs or requested.explicit_additions:
            raise HTTPException(
                status_code=422,
                detail=(
                    "descendants, source_refs and explicit_additions are server-controlled; "
                    "use selected_context and include_declared_descendants"
                ),
            )

        def resolve_scope(conn):
            root = card_scope.validate_entity_ref(
                conn,
                entity_ref=requested.root_entity.model_dump(),
            )
            selected = card_scope.resolve_explicit_context(
                conn,
                entity_refs=[item.model_dump() for item in body.selected_context],
            )
            exclusions = card_scope.resolve_explicit_context(
                conn,
                entity_refs=[item.model_dump() for item in requested.explicit_exclusions],
            )

            envelope = {
                "root_entity": {
                    "entity_id": root["entity_id"],
                    "entity_type": root["entity_type"],
                },
                "descendants": [],
                "source_refs": list(selected["source_refs"]),
                "explicit_additions": [],
                "explicit_exclusions": exclusions["entities"],
                "scope_widened_implicitly": False,
            }
            scope_resolution = {
                "requested": body.include_declared_descendants,
                "policy": "root_only",
                "descendants_added": 0,
                "source_refs_added": len(selected["source_refs"]),
                "selected_entities_validated": len(selected["entities"]),
                "counts": {},
            }
            if body.include_declared_descendants:
                descendants = card_scope.resolve_declared_descendants(
                    conn,
                    root_entity=envelope["root_entity"],
                )
                envelope["descendants"].extend(descendants["descendants"])
                for source_ref in descendants["source_refs"]:
                    if source_ref not in envelope["source_refs"]:
                        envelope["source_refs"].append(source_ref)
                scope_resolution = {
                    "requested": True,
                    "policy": descendants["policy"],
                    "descendants_added": len(descendants["descendants"]),
                    "source_refs_added": len(envelope["source_refs"]),
                    "selected_entities_validated": len(selected["entities"]),
                    "counts": descendants["counts"],
                }
            return envelope, selected["entities"], scope_resolution

        try:
            envelope, selected_context, scope_resolution = use_connection(resolve_scope)
        except card_scope.CardScopeError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        try:
            preview = hermes_handoff_preview.build_preview(
                question=body.question,
                card_context_envelope=envelope,
                selected_context=selected_context,
            )
        except hermes_handoff_preview.HandoffPreviewError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {
            **preview,
            "scope_resolution": scope_resolution,
            "resolved_card_context_envelope": envelope,
            "resolved_selected_context": selected_context,
        }

    @app.post("/v1/cockpit/hermes-handoffs/preview")
    def preview_hermes_handoff(
        body: HermesHandoffPreviewBody,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        return prepare(body)

    @app.post("/v1/cockpit/hermes-handoffs/submit", status_code=201)
    def submit_hermes_handoff(
        body: HermesHandoffSubmitBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        preview_body = HermesHandoffPreviewBody(
            question=body.question,
            card_context_envelope=body.card_context_envelope,
            selected_context=body.selected_context,
            include_declared_descendants=body.include_declared_descendants,
        )
        current = prepare(preview_body)
        stale = (
            current["preview_digest"] != body.expected_preview_digest
            or current["task_contract"]["task_contract_ref"] != body.expected_task_contract_ref
            or current["context_pack"]["context_pack_ref"] != body.expected_context_pack_ref
        )
        if stale:
            raise HTTPException(
                status_code=409,
                detail="Hermes handoff preview is stale; prepare the scope again before submission",
            )

        try:
            return use_connection(
                lambda conn: hermes_handoff_store.submit_handoff(
                    conn,
                    actor=actor,
                    idempotency_key=body.idempotency_key,
                    question=body.question,
                    preview=current,
                    card_context_envelope=current["resolved_card_context_envelope"],
                    selected_context=current["resolved_selected_context"],
                    include_declared_descendants=body.include_declared_descendants,
                )
            )
        except hermes_handoff_store.HandoffIdempotencyConflict as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except (hermes_handoff_store.HandoffSubmissionError, card_scope.CardScopeError) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    install_hermes_execution_routes(
        app,
        require_editor_key=require_editor_key,
        require_human_actor=require_human_actor,
        with_connection=use_connection,
    )
    install_work_decision_routes(
        app,
        require_editor_key=require_editor_key,
        require_human_actor=require_human_actor,
        with_connection=use_connection,
    )
