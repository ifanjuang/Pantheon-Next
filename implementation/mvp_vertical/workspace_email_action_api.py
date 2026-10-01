"""Workspace provider action API for Gmail archive and ask-only Hermes handoff.

Exactly two e-mail intents are exposed:
- ARCHIVE persists a verified HTML/attachment projection after explicit human action.
- ASK_HERMES creates bounded transient leases and reuses the existing handoff owner.

The adapter never writes Hindsight directly and never treats a folder as governed Project identity.
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
from typing import Callable, Literal

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

from . import (
    ephemeral_context,
    hermes_handoff_preview,
    hermes_handoff_store,
    workspace_email_archive,
)


class WorkspaceEmailMessageBody(BaseModel):
    provider_account_ref: str = Field(min_length=1, max_length=500)
    gmail_message_id: str = Field(min_length=1, max_length=500)
    gmail_thread_id: str = Field(min_length=1, max_length=500)
    raw_rfc822_base64url: str = Field(min_length=1, max_length=80_000_000)
    client_raw_sha256: str | None = Field(default=None, min_length=64, max_length=64)
    affaire_name: str | None = Field(default=None, min_length=1, max_length=255)
    destination_subdir: str = Field(default=workspace_email_archive.DEFAULT_DESTINATION_SUBDIR, max_length=500)
    confirm_archived_write: bool = False
    confirm_destination_change: bool = False


class WorkspaceEmailActionBody(BaseModel):
    intent: Literal["ARCHIVE", "ASK_HERMES"]
    messages: list[WorkspaceEmailMessageBody] = Field(min_length=1, max_length=50)
    question: str | None = Field(default=None, max_length=8_000)
    idempotency_key: str = Field(min_length=8, max_length=200)


class WorkspaceEmailStateMessageBody(BaseModel):
    provider_account_ref: str = Field(min_length=1, max_length=500)
    gmail_message_id: str = Field(min_length=1, max_length=500)
    gmail_thread_id: str = Field(min_length=1, max_length=500)
    raw_rfc822_base64url: str = Field(min_length=1, max_length=80_000_000)
    client_raw_sha256: str | None = Field(default=None, min_length=64, max_length=64)


class WorkspaceEmailStateBody(BaseModel):
    messages: list[WorkspaceEmailStateMessageBody] = Field(min_length=1, max_length=50)


def _case_ref(provider_account_ref: str) -> str:
    digest = hashlib.sha256(provider_account_ref.encode("utf-8")).hexdigest()[:24]
    return f"provider:gmail:{digest}"


def _transient_root_ref(messages: list[WorkspaceEmailMessageBody]) -> dict[str, str]:
    basis = "\0".join(
        sorted(
            f"{item.provider_account_ref}:{item.gmail_thread_id}:{item.gmail_message_id}"
            for item in messages
        )
    )
    digest = hashlib.sha256(basis.encode("utf-8")).hexdigest()[:32]
    return {
        "entity_id": f"gmail-selection:{digest}",
        "entity_type": "transient_context",
    }


def install_workspace_email_action_routes(
    app: FastAPI,
    *,
    require_read_key: Callable,
    require_editor_key: Callable,
    require_human_actor: Callable,
    with_connection: Callable,
    active_root: str | Path | None = None,
    archive_project_root: str | Path | None = None,
    raw_retention_root: str | Path | None = None,
    raw_storage_provider_ref: str | None = None,
    ephemeral_root: str | Path | None = None,
) -> None:
    active_root = Path(
        active_root
        or os.getenv("MVP_KROQI_AFFAIRES_ROOT", "/mnt/pantheon-affaires/KROQI/AFFAIRES")
    )
    archive_env = str(
        archive_project_root
        or os.getenv(
            "MVP_KROQI_ARCHIVE_PROJECT_ROOT",
            "/mnt/pantheon-affaires/KROQI/ARCHIVES/PROJET",
        )
    ).strip()
    archive_root = Path(archive_env) if archive_env else None
    raw_root = Path(
        raw_retention_root
        or os.getenv(
            "MVP_EMAIL_RAW_RETENTION_ROOT",
            "/var/lib/pantheon/source-retention/gmail",
        )
    )
    raw_provider = (
        raw_storage_provider_ref
        or os.getenv("MVP_EMAIL_RAW_STORAGE_PROVIDER_REF", "pantheon-local:gmail-raw")
    ).strip()
    lease_root = Path(
        ephemeral_root
        or os.getenv(
            "MVP_EPHEMERAL_CONTEXT_ROOT",
            "/tmp/pantheon-ephemeral-context",
        )
    )
    lease_store = ephemeral_context.EphemeralContextStore(lease_root)

    @app.get("/workspace/affaires")
    def get_affaires_catalogue(
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        try:
            rows = workspace_email_archive.affaires_catalogue(
                active_root=active_root,
                archive_project_root=archive_root,
            )
        except workspace_email_archive.WorkspaceEmailArchiveError as exc:
            raise HTTPException(status_code=503, detail=str(exc)) from exc
        return {
            "kind": "workspace_affaires_catalogue",
            "affaires": rows,
            "folder_is_governed_project_identity": False,
        }

    @app.post("/workspace/email/state")
    def get_email_archive_state(
        body: WorkspaceEmailStateBody,
        _authorized: None = Depends(require_read_key),
    ) -> dict:
        states = []
        for item in body.messages:
            try:
                raw = workspace_email_archive.decode_base64url_raw(
                    item.raw_rfc822_base64url
                )
                digest = hashlib.sha256(raw).hexdigest()
                if (
                    item.client_raw_sha256 is not None
                    and item.client_raw_sha256.lower() != digest
                ):
                    raise workspace_email_archive.RawChecksumMismatch(
                        "client RAW SHA-256 differs from server-verified bytes"
                    )
                state = with_connection(
                    lambda conn, item=item, digest=digest: workspace_email_archive.archive_state(
                        conn,
                        provider_account_ref=item.provider_account_ref,
                        gmail_thread_id=item.gmail_thread_id,
                        current_gmail_message_id=item.gmail_message_id,
                        current_raw_sha256=digest,
                    )
                )
                states.append(
                    {
                        "provider_account_ref": item.provider_account_ref,
                        "gmail_thread_id": item.gmail_thread_id,
                        "current_gmail_message_id": item.gmail_message_id,
                        "current_source_sha256": digest,
                        **state,
                    }
                )
            except workspace_email_archive.WorkspaceEmailArchiveError as exc:
                raise HTTPException(status_code=422, detail=str(exc)) from exc
        return {"kind": "workspace_email_archive_state", "messages": states}

    @app.post("/workspace/email/actions")
    def workspace_email_action(
        body: WorkspaceEmailActionBody,
        _authorized: None = Depends(require_editor_key),
        actor: str = Depends(require_human_actor),
    ) -> dict:
        if body.intent == "ARCHIVE":
            if body.question is not None and body.question.strip():
                raise HTTPException(
                    status_code=422,
                    detail="ARCHIVE does not accept a Hermes question",
                )
            results = []
            for index, item in enumerate(body.messages):
                if not item.affaire_name:
                    results.append(
                        {
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            "status": "destination_required",
                            "detail": "AFFAIRE is required for ARCHIVE",
                        }
                    )
                    continue
                try:
                    raw = workspace_email_archive.decode_base64url_raw(
                        item.raw_rfc822_base64url
                    )
                    result = with_connection(
                        lambda conn, item=item, raw=raw, index=index: workspace_email_archive.archive_email(
                            conn,
                            raw_rfc822=raw,
                            provider_account_ref=item.provider_account_ref,
                            gmail_message_id=item.gmail_message_id,
                            gmail_thread_id=item.gmail_thread_id,
                            affaire_name=item.affaire_name or "",
                            active_root=active_root,
                            archive_project_root=archive_root,
                            raw_retention_root=raw_root,
                            raw_storage_provider_ref=raw_provider,
                            actor=actor,
                            idempotency_key=f"{body.idempotency_key}:{index}",
                            client_raw_sha256=item.client_raw_sha256,
                            destination_subdir=item.destination_subdir,
                            confirm_archived_write=item.confirm_archived_write,
                            confirm_destination_change=item.confirm_destination_change,
                        )
                    )
                    results.append(
                        {
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            **result,
                        }
                    )
                except workspace_email_archive.ArchivedDestinationConfirmationRequired as exc:
                    results.append(
                        {
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            "status": "archived_destination_confirmation_required",
                            "detail": str(exc),
                        }
                    )
                except workspace_email_archive.DestinationChangeConfirmationRequired as exc:
                    results.append(
                        {
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            "status": "destination_change_confirmation_required",
                            "detail": str(exc),
                        }
                    )
                except (
                    workspace_email_archive.DestinationRequired,
                    workspace_email_archive.DestinationCollision,
                ) as exc:
                    results.append(
                        {
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            "status": "destination_required",
                            "detail": str(exc),
                        }
                    )
                except workspace_email_archive.WorkspaceEmailArchiveError as exc:
                    results.append(
                        {
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            "status": "refused",
                            "detail": str(exc),
                        }
                    )
            return {
                "kind": "workspace_email_action_result",
                "intent": "ARCHIVE",
                "messages": results,
                "hermes_handoff_created": False,
            }

        question = str(body.question or "").strip()
        if len(question) < 3:
            raise HTTPException(
                status_code=422,
                detail="ASK_HERMES requires a question of at least 3 characters",
            )

        descriptors: list[dict] = []
        source_refs: list[str] = []
        provider_accounts: set[str] = set()
        try:
            for item in body.messages:
                raw = workspace_email_archive.decode_base64url_raw(
                    item.raw_rfc822_base64url
                )
                raw_digest = hashlib.sha256(raw).hexdigest()
                if (
                    item.client_raw_sha256 is not None
                    and item.client_raw_sha256.lower() != raw_digest
                ):
                    raise workspace_email_archive.RawChecksumMismatch(
                        "client RAW SHA-256 differs from server-verified bytes"
                    )
                parsed = workspace_email_archive.parse_rfc822(raw)
                normalized = workspace_email_archive.normalized_ask_context(
                    parsed,
                    provider_account_ref=item.provider_account_ref,
                    gmail_message_id=item.gmail_message_id,
                    gmail_thread_id=item.gmail_thread_id,
                    raw_sha256=raw_digest,
                )
                descriptor = lease_store.create(
                    normalized,
                    media_type="application/vnd.pantheon.gmail-context+json",
                    source_provenance=[
                        {
                            "provider": "gmail",
                            "provider_account_ref": item.provider_account_ref,
                            "gmail_message_id": item.gmail_message_id,
                            "gmail_thread_id": item.gmail_thread_id,
                            "raw_sha256": raw_digest,
                        }
                    ],
                )
                descriptors.append(descriptor)
                source_refs.append(
                    f"gmail://{item.provider_account_ref}/{item.gmail_message_id}"
                )
                provider_accounts.add(item.provider_account_ref)
        except (
            workspace_email_archive.WorkspaceEmailArchiveError,
            ephemeral_context.EphemeralContextError,
        ) as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        root_ref = _transient_root_ref(body.messages)
        envelope = {
            "root_entity": root_ref,
            "descendants": [],
            "source_refs": source_refs,
            "tag_context": [],
            "explicit_additions": [],
            "explicit_exclusions": [],
            "scope_widened_implicitly": False,
        }
        try:
            preview = hermes_handoff_preview.build_preview(
                question=question,
                card_context_envelope=envelope,
                selected_context=[],
                ephemeral_context=descriptors,
            )
        except hermes_handoff_preview.HandoffPreviewError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        account_basis = "|".join(sorted(provider_accounts))
        try:
            handoff = with_connection(
                lambda conn: hermes_handoff_store.submit_handoff(
                    conn,
                    actor=actor,
                    idempotency_key=body.idempotency_key,
                    question=question,
                    preview=preview,
                    card_context_envelope=envelope,
                    selected_context=[],
                    include_declared_descendants=False,
                    case_ref_override=_case_ref(account_basis),
                )
            )
        except hermes_handoff_store.HandoffIdempotencyConflict as exc:
            raise HTTPException(status_code=409, detail=str(exc)) from exc
        except hermes_handoff_store.HandoffSubmissionError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        return {
            "kind": "workspace_email_action_result",
            "intent": "ASK_HERMES",
            "messages": [
                {
                    "gmail_message_id": item.gmail_message_id,
                    "gmail_thread_id": item.gmail_thread_id,
                    "status": "transient_context_prepared",
                    "lease_ref": descriptors[index]["lease_ref"],
                    "content_sha256": descriptors[index]["content_sha256"],
                }
                for index, item in enumerate(body.messages)
            ],
            "handoff": handoff,
            "execution_started": False,
            "affaires_written": False,
            "hindsight_written": False,
        }
