"""Deterministic preview of a scoped Cockpit -> Hermes handoff.

This module prepares governance-facing candidate objects only. It does not
persist a Work Issue, dispatch Hermes, authorize execution, create Evidence or
promote memory.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

from .entity_ref import EntityRef, EntityRefError, unique_entity_refs


MAX_CONTEXT_REFS = 250
MAX_SOURCE_REFS = 500
MAX_TAG_CONTEXT_ENTITIES = 250
MAX_EPHEMERAL_CONTEXT_ITEMS = 50
MAX_EPHEMERAL_CONTEXT_BYTES = 8 * 1024 * 1024


class HandoffPreviewError(ValueError):
    pass


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _entity_ref(value: dict, *, label: str) -> dict[str, str]:
    try:
        return EntityRef.from_mapping(value, label=label).as_dict()
    except EntityRefError as exc:
        raise HandoffPreviewError(str(exc)) from exc


def _unique_refs(values: list[dict], *, label: str) -> list[dict[str, str]]:
    try:
        return [
            ref.as_dict()
            for ref in unique_entity_refs(
                values,
                label=label,
                limit=MAX_CONTEXT_REFS,
            )
        ]
    except EntityRefError as exc:
        raise HandoffPreviewError(str(exc)) from exc


def _source_refs(values: list[str]) -> list[str]:
    if len(values) > MAX_SOURCE_REFS:
        raise HandoffPreviewError(f"source_refs exceeds {MAX_SOURCE_REFS} entries")
    output: list[str] = []
    seen: set[str] = set()
    for raw in values:
        ref = str(raw or "").strip()
        if not ref or ref in seen:
            continue
        seen.add(ref)
        output.append(ref)
    return output


def _tag_context(values: Any) -> list[dict[str, Any]]:
    if not isinstance(values, list):
        raise HandoffPreviewError("tag_context must be an array")
    if len(values) > MAX_TAG_CONTEXT_ENTITIES:
        raise HandoffPreviewError(
            f"tag_context exceeds {MAX_TAG_CONTEXT_ENTITIES} entity entries"
        )

    output: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for raw in values:
        if not isinstance(raw, dict):
            raise HandoffPreviewError("tag_context entries must be objects")
        try:
            ref = EntityRef.from_mapping(
                raw.get("entity_ref") or {},
                label="tag_context.entity_ref",
            )
        except EntityRefError as exc:
            raise HandoffPreviewError(str(exc)) from exc
        if ref.key in seen:
            raise HandoffPreviewError("tag_context contains a duplicate entity")
        seen.add(ref.key)

        tags = raw.get("tags")
        unregistered = raw.get("unregistered_tags")
        limits = raw.get("limits")
        if not isinstance(tags, list) or not isinstance(unregistered, list):
            raise HandoffPreviewError(
                "tag_context requires tags and unregistered_tags arrays"
            )
        if raw.get("subject_limit") != 5:
            raise HandoffPreviewError("tag_context subject_limit must be 5")
        if not isinstance(limits, list):
            raise HandoffPreviewError("tag_context requires limits")

        normalized_tags: list[dict[str, Any]] = []
        for tag in tags:
            if not isinstance(tag, dict):
                raise HandoffPreviewError("tag context definitions must be objects")
            group = str(tag.get("group") or "").strip()
            slug = str(tag.get("slug") or "").strip()
            title = str(tag.get("title") or "").strip()
            description = str(tag.get("description") or "").strip()
            hermes_context = str(tag.get("hermes_context") or "").strip()
            if group not in {"type", "subject"}:
                raise HandoffPreviewError("tag context group must be type or subject")
            if not all((slug, title, description, hermes_context)):
                raise HandoffPreviewError("registered tag context is incomplete")
            normalized_tags.append(
                {
                    "slug": slug,
                    "group": group,
                    "title": title,
                    "description": description,
                    "hermes_context": hermes_context,
                    "applies_to": [str(item) for item in tag.get("applies_to") or []],
                }
            )

        normalized_unregistered: list[dict[str, str]] = []
        for item in unregistered:
            if not isinstance(item, dict):
                raise HandoffPreviewError("unregistered tag entries must be objects")
            group = str(item.get("group") or "").strip()
            slug = str(item.get("slug") or "").strip()
            if group not in {"type", "subject"} or not slug:
                raise HandoffPreviewError("unregistered tag entry is invalid")
            normalized_unregistered.append({"group": group, "slug": slug})

        output.append(
            {
                "entity_ref": ref.as_dict(),
                "tags": normalized_tags,
                "unregistered_tags": normalized_unregistered,
                "subject_limit": 5,
                "limits": [str(item) for item in limits if str(item).strip()],
            }
        )
    return output


def _ephemeral_context(values: Any) -> list[dict[str, Any]]:
    if values is None:
        return []
    if not isinstance(values, list):
        raise HandoffPreviewError("ephemeral_context must be an array")
    if len(values) > MAX_EPHEMERAL_CONTEXT_ITEMS:
        raise HandoffPreviewError(
            f"ephemeral_context exceeds {MAX_EPHEMERAL_CONTEXT_ITEMS} entries"
        )
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    total_bytes = 0
    for raw in values:
        if not isinstance(raw, dict):
            raise HandoffPreviewError("ephemeral_context entries must be objects")
        lease_ref = str(raw.get("lease_ref") or "").strip()
        digest = str(raw.get("content_sha256") or "").strip().lower()
        media_type = str(raw.get("media_type") or "").strip()
        expires_at = str(raw.get("expires_at") or "").strip()
        byte_size = raw.get("byte_size")
        provenance = raw.get("source_provenance") or []
        if not lease_ref or len(lease_ref) > 200:
            raise HandoffPreviewError("ephemeral_context lease_ref is invalid")
        if lease_ref in seen:
            raise HandoffPreviewError("ephemeral_context contains a duplicate lease_ref")
        seen.add(lease_ref)
        if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            raise HandoffPreviewError("ephemeral_context content_sha256 must be SHA-256")
        if not isinstance(byte_size, int) or byte_size <= 0:
            raise HandoffPreviewError("ephemeral_context byte_size must be positive")
        total_bytes += byte_size
        if total_bytes > MAX_EPHEMERAL_CONTEXT_BYTES:
            raise HandoffPreviewError(
                f"ephemeral_context exceeds {MAX_EPHEMERAL_CONTEXT_BYTES} aggregate bytes"
            )
        if not media_type or len(media_type) > 200:
            raise HandoffPreviewError("ephemeral_context media_type is invalid")
        if not expires_at:
            raise HandoffPreviewError("ephemeral_context expires_at is required")
        if not isinstance(provenance, list):
            raise HandoffPreviewError("ephemeral_context source_provenance must be an array")
        output.append(
            {
                "lease_ref": lease_ref,
                "content_sha256": digest,
                "byte_size": byte_size,
                "media_type": media_type,
                "source_provenance": provenance,
                "expires_at": expires_at,
            }
        )
    return output


def build_preview(
    *,
    question: str,
    card_context_envelope: dict,
    selected_context: list[dict] | None = None,
    ephemeral_context: list[dict] | None = None,
) -> dict:
    intent = question.strip()
    if len(intent) < 3:
        raise HandoffPreviewError("Hermes handoff question must contain at least 3 characters")
    if len(intent) > 8_000:
        raise HandoffPreviewError("Hermes handoff question exceeds 8000 characters")

    root = _entity_ref(card_context_envelope.get("root_entity") or {}, label="root_entity")
    descendants = _unique_refs(card_context_envelope.get("descendants") or [], label="descendants")
    explicit_additions = _unique_refs(
        card_context_envelope.get("explicit_additions") or [],
        label="explicit_additions",
    )
    explicit_exclusions = _unique_refs(
        card_context_envelope.get("explicit_exclusions") or [],
        label="explicit_exclusions",
    )
    selected = _unique_refs(selected_context or [], label="selected_context")
    sources = _source_refs(card_context_envelope.get("source_refs") or [])
    tag_context = _tag_context(card_context_envelope.get("tag_context") or [])
    leases = _ephemeral_context(ephemeral_context)

    excluded_keys = {
        EntityRef.from_mapping(item, label="excluded_entity").key
        for item in explicit_exclusions
    }
    admitted: list[dict[str, str]] = []
    admitted_keys: set[tuple[str, str]] = set()
    for item in [root, *descendants, *explicit_additions, *selected]:
        ref = EntityRef.from_mapping(item, label="included_entity")
        if ref.key in excluded_keys or ref.key in admitted_keys:
            continue
        admitted_keys.add(ref.key)
        admitted.append(ref.as_dict())

    context_core = {
        "purpose": "answer one Cockpit question within the visible Card context",
        "target_surface": "hermes_task_contract",
        "root_entity": root,
        "included_entities": admitted,
        "excluded_entities": explicit_exclusions,
        "source_refs": sources,
        "tag_context": tag_context,
        "ephemeral_context": leases,
        "scope_widened_implicitly": False,
        "staleness_note": "runtime must re-read current owner records when freshness is consequential",
        "forbidden_assumptions": [
            "selected context is Evidence",
            "runtime success establishes truth",
            "a read-only question authorizes a write or external effect",
            "an ephemeral lease is a Source, Evidence, memory or persistence",
            "a tag description establishes truth, authority or professional validation",
            "an unregistered tag may be assigned an invented meaning",
        ],
    }
    context_digest = _digest(context_core)
    context_pack_ref = f"context-pack-candidate:{context_digest[:24]}"

    task_core = {
        "intent": intent,
        "scope_ref": context_pack_ref,
        "requested_effect": "read_only",
        "constraints": [
            "do not widen scope implicitly",
            "do not mutate Agency Data",
            "do not perform an external effect",
            "do not promote memory or Evidence automatically",
            "surface missing, stale or contradictory information",
            "use tag descriptions only as contextual orientation",
            "do not infer a meaning for unregistered tags",
        ],
        "approval_expectations": "a new gate is required before any consequential follow-up",
        "expected_evidence": ["source_refs", "ephemeral_context", "trace_refs", "limitations", "assumptions"],
        "allowed_outputs": ["answer_candidate", "source_references", "limitations", "open_questions"],
        "forbidden_outputs": ["external_effect", "canonical_effect", "memory_promotion", "agency_data_mutation"],
    }
    task_digest = _digest(task_core)
    task_contract_ref = f"task-contract-candidate:{task_digest[:24]}"

    preview = {
        "kind": "hermes_handoff_preview",
        "status": "candidate",
        "requested_effect": "read_only",
        "execution_authorized": False,
        "task_contract": {
            "task_contract_ref": task_contract_ref,
            "digest": task_digest,
            **task_core,
        },
        "context_pack": {
            "context_pack_ref": context_pack_ref,
            "digest": context_digest,
            **context_core,
        },
        "non_equivalences": [
            "preview != Task Contract admission",
            "context selection != Evidence",
            "tag context != source authority",
            "execution_authorized=false",
            "handoff preview != Hermes run",
            "ephemeral lease != Source admission",
            "ephemeral lease != AFFAIRES persistence",
            "ephemeral lease != Hindsight memory",
        ],
    }
    preview["preview_digest"] = _digest(preview)
    return preview
