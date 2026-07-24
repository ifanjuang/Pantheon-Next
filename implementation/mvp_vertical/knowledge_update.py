"""Signed, human-confirmed UPDATE gate for one existing Knowledge item.

This module adds no generic effect engine. It previews one exact Knowledge
revision, signs its immutable inputs and delegates the final transactional write
to ``knowledge.revise_knowledge``.
"""

from __future__ import annotations

import difflib
import hashlib
import hmac
import json
import time
from datetime import datetime, timezone
from typing import Any

from . import knowledge
from .policy_gate import PolicyClient, enforce_consequential

CONFIRMATION_PHRASE = "CONFIRMER UPDATE"
DEFAULT_TTL_SECONDS = 300


class KnowledgeUpdateError(ValueError):
    """The bounded Knowledge update cannot be previewed or applied safely."""


class KnowledgeUpdateExpired(KnowledgeUpdateError):
    pass


def _material_markdown(value: str) -> str:
    """Normalize only for material-change detection, never for persistence."""
    return value.strip()


def _digest(value: str) -> str:
    return f"sha256:{hashlib.sha256(value.encode('utf-8')).hexdigest()}"


def _canonical_payload(value: dict[str, Any]) -> bytes:
    return json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")


def _signature(secret: str, payload: dict[str, Any]) -> str:
    return hmac.new(secret.encode("utf-8"), _canonical_payload(payload), hashlib.sha256).hexdigest()


def _validate_actor(actor: str) -> str:
    actor = actor.strip()
    if len(actor) < 2 or len(actor) > 200:
        raise KnowledgeUpdateError("a declared human actor between 2 and 200 characters is required")
    return actor


def _validate_scope(card: dict, *, parent_project_id: str, knowledge_id: str) -> None:
    if card.get("knowledge_id") != knowledge_id:
        raise KnowledgeUpdateError("Knowledge identity does not match the requested target")
    if card.get("parent_project_id") != parent_project_id:
        raise KnowledgeUpdateError("Knowledge does not belong to the exact opened project")


def _validate_preserved_review_status(card: dict, review_status: str | None) -> None:
    if review_status is not None and review_status != card.get("review_status"):
        raise KnowledgeUpdateError(
            "review status changes require a separate governed decision path"
        )


def _effect_payload(
    *,
    parent_project_id: str,
    knowledge_id: str,
    expected_version: int,
    base_markdown_digest: str,
    proposed_markdown_digest: str,
    review_status: str | None,
    actor: str,
    expires_at: int,
) -> dict[str, Any]:
    return {
        "effect": "UPDATE",
        "object_type": "knowledge",
        "parent_project_id": parent_project_id,
        "knowledge_id": knowledge_id,
        "expected_version": expected_version,
        "base_markdown_digest": base_markdown_digest,
        "proposed_markdown_digest": proposed_markdown_digest,
        "review_status": review_status,
        "actor": actor,
        "expires_at": expires_at,
    }


def preview_knowledge_update(
    conn,
    *,
    parent_project_id: str,
    knowledge_id: str,
    proposed_markdown: str,
    expected_version: int,
    actor: str,
    signing_secret: str,
    review_status: str | None = None,
    ttl_seconds: int = DEFAULT_TTL_SECONDS,
    now: int | None = None,
) -> dict:
    """Return a stateless diff and signed confirmation challenge."""
    actor = _validate_actor(actor)
    if not signing_secret:
        raise KnowledgeUpdateError("Knowledge update signing secret is not configured")
    if not proposed_markdown.strip():
        raise KnowledgeUpdateError("proposed Markdown must not be empty")
    if expected_version < 1:
        raise KnowledgeUpdateError("expected_version must be at least 1")
    if review_status is not None and review_status not in knowledge.REVIEW_STATUSES:
        raise KnowledgeUpdateError("invalid Knowledge review status")
    if ttl_seconds < 30 or ttl_seconds > 900:
        raise KnowledgeUpdateError("confirmation TTL must be between 30 and 900 seconds")

    card = knowledge.get_knowledge_card(conn, knowledge_id)
    _validate_scope(card, parent_project_id=parent_project_id, knowledge_id=knowledge_id)
    _validate_preserved_review_status(card, review_status)
    if card.get("version") != expected_version:
        raise knowledge.StaleKnowledgeWrite(
            f"stale Knowledge version: expected {expected_version}, current {card.get('version')}"
        )

    current_markdown = knowledge.get_knowledge_markdown(conn, knowledge_id)
    if _material_markdown(proposed_markdown) == _material_markdown(current_markdown):
        raise KnowledgeUpdateError("the proposed UPDATE has no material change")

    base_digest = _digest(current_markdown)
    proposed_digest = _digest(proposed_markdown)
    current_time = int(time.time()) if now is None else int(now)
    expires_at = current_time + ttl_seconds
    signed_payload = _effect_payload(
        parent_project_id=parent_project_id,
        knowledge_id=knowledge_id,
        expected_version=expected_version,
        base_markdown_digest=base_digest,
        proposed_markdown_digest=proposed_digest,
        review_status=review_status,
        actor=actor,
        expires_at=expires_at,
    )
    diff = "".join(
        difflib.unified_diff(
            current_markdown.splitlines(keepends=True),
            proposed_markdown.splitlines(keepends=True),
            fromfile=f"{knowledge_id}@v{expected_version}",
            tofile=f"{knowledge_id}@candidate-v{expected_version + 1}",
            lineterm="\n",
        )
    )

    return {
        "status": "confirmation_required",
        "effect": "UPDATE",
        "target": {
            "object_type": "knowledge",
            "object_id": knowledge_id,
            "parent_project_id": parent_project_id,
            "title": card.get("title"),
            "current_version": expected_version,
            "current_review_status": card.get("review_status"),
            "proposed_review_status": card.get("review_status"),
        },
        "diff": diff,
        "base_markdown_digest": base_digest,
        "proposed_markdown_digest": proposed_digest,
        "confirmation": {
            "phrase": CONFIRMATION_PHRASE,
            "token": _signature(signing_secret, signed_payload),
            "expires_at": expires_at,
        },
        "identity": {
            "declared_actor": actor,
            "binding": "editor_credential_plus_declared_human_actor",
            "assurance": "partial",
        },
        "apply_route": (
            f"/v1/projects/{parent_project_id}/knowledge/{knowledge_id}/updates/apply"
        ),
        "limits": [
            "The preview is not persisted.",
            "Terminal whitespace-only changes are not material in this first gate.",
            "The exact confirmed Markdown is preserved when a material change is applied.",
            "The Knowledge review status is preserved by this first UPDATE path.",
            "The declared actor is bound to the shared editor credential, not an individual SSO identity.",
            "Knowledge remains editorial content, not Evidence, governed memory or doctrine.",
        ],
    }


def apply_knowledge_update(
    conn,
    *,
    parent_project_id: str,
    knowledge_id: str,
    proposed_markdown: str,
    expected_version: int,
    base_markdown_digest: str,
    actor: str,
    signing_secret: str,
    confirmation_token: str,
    confirmation_expires_at: int,
    confirmation_phrase: str,
    idempotency_key: str,
    review_status: str | None = None,
    now: int | None = None,
    policy_client: PolicyClient | None = None,
    required_ceiling: str = "C2",
    preflight_candidate: dict[str, Any] | None = None,
) -> dict:
    """Verify the signed preview and apply only the exact Knowledge revision.

    When ``policy_client`` is supplied, the consequential write additionally
    routes through the Pantheon chokepoint (`policy_gate.enforce_consequential`):
    the update is blocked, before any database access, unless the preflight is
    eligible and the human decision validates. When it is ``None`` the module's
    own signed checks apply unchanged."""
    actor = _validate_actor(actor)
    if confirmation_phrase != CONFIRMATION_PHRASE:
        raise KnowledgeUpdateError("exact confirmation phrase is required")
    if not signing_secret:
        raise KnowledgeUpdateError("Knowledge update signing secret is not configured")
    if not proposed_markdown.strip():
        raise KnowledgeUpdateError("proposed Markdown must not be empty")
    if len(idempotency_key.strip()) < 8 or len(idempotency_key) > 200:
        raise KnowledgeUpdateError("idempotency_key must be between 8 and 200 characters")
    current_time = int(time.time()) if now is None else int(now)
    if confirmation_expires_at > current_time + 905:
        raise KnowledgeUpdateError("confirmation expiry is outside the accepted window")

    proposed_digest = _digest(proposed_markdown)
    signed_payload = _effect_payload(
        parent_project_id=parent_project_id,
        knowledge_id=knowledge_id,
        expected_version=expected_version,
        base_markdown_digest=base_markdown_digest,
        proposed_markdown_digest=proposed_digest,
        review_status=review_status,
        actor=actor,
        expires_at=confirmation_expires_at,
    )
    expected_token = _signature(signing_secret, signed_payload)
    if not hmac.compare_digest(confirmation_token, expected_token):
        raise KnowledgeUpdateError("confirmation token does not match the immutable UPDATE effect")

    if policy_client is not None:
        scope = {"scope_type": "project", "scope_id": parent_project_id}
        object_identity = f"knowledge:{knowledge_id}:{proposed_digest}"
        decision_payload = {
            "decision": {
                "decision_id": idempotency_key,
                "decided_by": actor,
                "approval_level": required_ceiling,
                "expires_at": datetime.fromtimestamp(
                    confirmation_expires_at, tz=timezone.utc
                ).isoformat(),
                "scope": scope,
                "object_identity": object_identity,
                "content_digest": proposed_digest,
            },
            "expectation": {
                "required_ceiling": required_ceiling,
                "required_scope": scope,
                "object_identity": object_identity,
                "expected_digest": proposed_digest,
            },
        }
        candidate = preflight_candidate or {
            "request": {
                "intent": "knowledge_update",
                "external_effect": False,
                "writes_state": True,
                "scope": scope,
            }
        }
        verdict = enforce_consequential(
            policy_client, candidate=candidate, decision_payload=decision_payload
        )
        if not verdict.allowed:
            raise KnowledgeUpdateError(
                "policy chokepoint blocked the Knowledge update "
                f"({verdict.disposition}): {verdict.reasons}"
            )

    card = knowledge.get_knowledge_card(conn, knowledge_id)
    _validate_scope(card, parent_project_id=parent_project_id, knowledge_id=knowledge_id)
    _validate_preserved_review_status(card, review_status)
    current_version = card.get("version")
    if current_version == expected_version:
        if confirmation_expires_at < current_time:
            raise KnowledgeUpdateExpired("Knowledge update confirmation has expired")
        current_markdown = knowledge.get_knowledge_markdown(conn, knowledge_id)
        if _digest(current_markdown) != base_markdown_digest:
            raise knowledge.StaleKnowledgeWrite(
                "Knowledge Markdown changed after the signed preview"
            )
    elif current_version is None or current_version < expected_version:
        raise knowledge.StaleKnowledgeWrite(
            f"stale Knowledge version: expected {expected_version}, current {current_version}"
        )
    # A version above the signed base can only succeed through the adapter's
    # immutable idempotency replay. A new or altered key still fails there.

    snapshot = knowledge.revise_knowledge(
        conn,
        knowledge_id=knowledge_id,
        markdown=proposed_markdown,
        expected_version=expected_version,
        actor=actor,
        actor_kind="human",
        idempotency_key=idempotency_key,
        review_status=None,
    )
    return {
        "status": "applied",
        "effect": "UPDATE",
        "knowledge": snapshot,
        "identity": {
            "declared_actor": actor,
            "actor_kind": "human",
            "assurance": "partial",
        },
        "idempotency_key": idempotency_key,
        "distinctions": [
            "UPDATE applied != Knowledge reviewed",
            "Knowledge revised != Evidence",
            "runtime success != proof",
        ],
    }
