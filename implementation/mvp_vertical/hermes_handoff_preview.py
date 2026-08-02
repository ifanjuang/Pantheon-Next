"""Deterministic preview of a scoped Cockpit -> Hermes handoff.

This module prepares governance-facing candidate objects only. It does not
persist a Work Issue, dispatch Hermes, authorize execution, create Evidence or
promote memory.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

MAX_CONTEXT_REFS = 250
MAX_SOURCE_REFS = 500
MAX_TAG_CONTEXT_ENTITIES = 250


class HandoffPreviewError(ValueError):
    pass


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _entity_ref(value: dict, *, label: str) -> dict:
    entity_id = str(value.get("entity_id") or "").strip()
    entity_type = str(value.get("entity_type") or "").strip()
    if not entity_id or not entity_type:
        raise HandoffPreviewError(f"{label} requires stable entity_id and entity_type")
    return {"entity_id": entity_id, "entity_type": entity_type}


def _unique_refs(values: list[dict], *, label: str) -> list[dict]:
    if len(values) > MAX_CONTEXT_REFS:
        raise HandoffPreviewError(f"{label} exceeds {MAX_CONTEXT_REFS} entries")
    output: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for raw in values:
        ref = _entity_ref(raw, label=label)
        key = (ref["entity_type"], ref["entity_id"])
        if key in seen:
            continue
        seen.add(key)
        output.append(ref)
    return output


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
        ref = _entity_ref(raw.get("entity_ref") or {}, label="tag_context.entity_ref")
        key = (ref["entity_type"], ref["entity_id"])
        if key in seen:
            raise HandoffPreviewError("tag_context contains a duplicate entity")
        seen.add(key)

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
                "entity_ref": ref,
                "tags": normalized_tags,
                "unregistered_tags": normalized_unregistered,
                "subject_limit": 5,
                "limits": [str(item) for item in limits if str(item).strip()],
            }
        )
    return output


def build_preview(
    *,
    question: str,
    card_context_envelope: dict,
    selected_context: list[dict] | None = None,
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

    excluded_keys = {(item["entity_type"], item["entity_id"]) for item in explicit_exclusions}
    admitted: list[dict] = []
    admitted_keys: set[tuple[str, str]] = set()
    for item in [root, *descendants, *explicit_additions, *selected]:
        key = (item["entity_type"], item["entity_id"])
        if key in excluded_keys or key in admitted_keys:
            continue
        admitted_keys.add(key)
        admitted.append(item)

    context_core = {
        "purpose": "answer one Cockpit question within the visible Card context",
        "target_surface": "hermes_task_contract",
        "root_entity": root,
        "included_entities": admitted,
        "excluded_entities": explicit_exclusions,
        "source_refs": sources,
        "tag_context": tag_context,
        "scope_widened_implicitly": False,
        "staleness_note": "runtime must re-read current owner records when freshness is consequential",
        "forbidden_assumptions": [
            "selected context is Evidence",
            "runtime success establishes truth",
            "a read-only question authorizes a write or external effect",
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
        "expected_evidence": ["source_refs", "trace_refs", "limitations", "assumptions"],
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
        ],
    }
    preview["preview_digest"] = _digest(preview)
    return preview
