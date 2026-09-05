"""Bounded, read-only context slicing over Project Anatomy projections.

This module does not own project facts, relations, requirements, memory or
execution. It composes an already-built Project Anatomy projection into one
small object-centred read model for contextual reasoning.

A Context Pack or caller remains responsible for admitting identities. Relation
semantics may explain how an already-present relation behaves; they never create
a relation claim, widen scope, establish compliance or authorize an effect.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Iterable


RELATION_SEMANTICS_VERSION = "apu-relation-semantics-candidate-v1"
CONTEXT_SLICE_VERSION = "apu-object-context-v1"

# Minimal candidate semantics for relation names already present in the Project
# Anatomy doctrine. These properties are proposals until a governed relation
# registry admits them. Absence from this mapping means "opaque", not invalid.
_RELATION_SEMANTICS: dict[str, dict[str, Any]] = {
    "identity.represents": {
        "directionality": "directed",
        "inverse_relation": None,
        "symmetric": False,
        "transitive": False,
        "subject_entity_types": ["source_representation"],
        "object_entity_types": ["stable_object"],
    },
    "spatial.adjacent_to": {
        "directionality": "undirected",
        "inverse_relation": "spatial.adjacent_to",
        "symmetric": True,
        "transitive": False,
        "subject_entity_types": ["stable_object"],
        "object_entity_types": ["stable_object"],
    },
    "spatial.contains": {
        "directionality": "directed",
        "inverse_relation": "spatial.located_in",
        "symmetric": False,
        "transitive": False,
        "subject_entity_types": ["stable_object"],
        "object_entity_types": ["stable_object"],
    },
    "spatial.located_in": {
        "directionality": "directed",
        "inverse_relation": "spatial.contains",
        "symmetric": False,
        "transitive": False,
        "subject_entity_types": ["stable_object"],
        "object_entity_types": ["stable_object"],
    },
    "architecture.opens_to": {
        "directionality": "directed",
        "inverse_relation": None,
        "symmetric": False,
        "transitive": False,
        "subject_entity_types": ["stable_object"],
        "object_entity_types": ["stable_object"],
    },
    "architecture.hosted_by": {
        "directionality": "directed",
        "inverse_relation": None,
        "symmetric": False,
        "transitive": False,
        "subject_entity_types": ["stable_object"],
        "object_entity_types": ["stable_object"],
    },
    "assembly.part_of": {
        "directionality": "directed",
        "inverse_relation": None,
        "symmetric": False,
        "transitive": False,
        "subject_entity_types": ["stable_object"],
        "object_entity_types": ["stable_object"],
    },
}


class ProjectAnatomyContextError(ValueError):
    pass


def relation_semantics(relation_type: str) -> dict[str, Any]:
    """Return candidate relation metadata without inferring a relation fact."""
    relation_type = str(relation_type or "").strip()
    if not relation_type:
        raise ProjectAnatomyContextError("relation_type is required")
    semantics = _RELATION_SEMANTICS.get(relation_type)
    if semantics is None:
        return {
            "relation_type": relation_type,
            "status": "opaque_unregistered",
            "semantics_version": RELATION_SEMANTICS_VERSION,
            "creates_relation_claim": False,
            "authority_effect": False,
        }
    return {
        "relation_type": relation_type,
        "status": "candidate_projection_semantics",
        "semantics_version": RELATION_SEMANTICS_VERSION,
        **deepcopy(semantics),
        "creates_relation_claim": False,
        "authority_effect": False,
    }


def _entity_id(ref: Any, entity_type: str = "stable_object") -> str | None:
    if not isinstance(ref, dict) or ref.get("entity_type") != entity_type:
        return None
    value = str(ref.get("entity_id") or "").strip()
    return value or None


def _objects_by_id(projection: dict[str, Any]) -> dict[str, dict[str, Any]]:
    structure = projection.get("structure")
    if not isinstance(structure, dict):
        return {}
    objects = structure.get("objects")
    if not isinstance(objects, list):
        return {}
    return {
        str(item.get("object_id")): item
        for item in objects
        if isinstance(item, dict) and str(item.get("object_id") or "").strip()
    }


def _direct_requirements(
    root: dict[str, Any],
    requirements: Iterable[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Match only deterministic target shapes; preserve unresolved selectors."""
    root_id = str(root.get("object_id") or "").strip()
    root_family = str(root.get("object_family") or "").strip()
    attribute_keys = {
        str(claim.get("attribute_key"))
        for claim in root.get("attribute_claims") or []
        if isinstance(claim, dict) and str(claim.get("attribute_key") or "").strip()
    }

    matched: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    for requirement in requirements:
        if not isinstance(requirement, dict):
            continue
        target = requirement.get("target")
        if not isinstance(target, dict):
            unresolved.append({"requirement": deepcopy(requirement), "reason": "missing_target"})
            continue

        target_id = _entity_id(target.get("entity_ref"))
        if target_id is not None:
            if target_id == root_id:
                matched.append(
                    {
                        "requirement": deepcopy(requirement),
                        "match_basis": "exact_entity_ref",
                    }
                )
            continue

        selector = target.get("selector")
        if not isinstance(selector, dict):
            unresolved.append({"requirement": deepcopy(requirement), "reason": "unsupported_target"})
            continue

        deterministic_parts = []
        if selector.get("object_family") is not None:
            deterministic_parts.append(str(selector.get("object_family")) == root_family)
        if selector.get("attribute_key") is not None:
            deterministic_parts.append(str(selector.get("attribute_key")) in attribute_keys)

        classification_requested = bool(
            selector.get("classification_scheme") or selector.get("classification_value")
        )
        if classification_requested:
            unresolved.append(
                {
                    "requirement": deepcopy(requirement),
                    "reason": "classification_selector_requires_explicit_resolution",
                }
            )
            continue

        if deterministic_parts and all(deterministic_parts):
            matched.append(
                {
                    "requirement": deepcopy(requirement),
                    "match_basis": "deterministic_selector",
                }
            )

    return matched, unresolved


def build_object_context_slice(
    projection: dict[str, Any],
    *,
    object_id: str,
    admitted_object_ids: Iterable[str] | None = None,
    requirements: Iterable[dict[str, Any]] = (),
) -> dict[str, Any]:
    """Build one bounded object-centred projection for contextual reasoning.

    The function can expose direct neighbouring identities from existing relation
    claims, but neighbour records are included only when their identities were
    explicitly admitted by the caller. It never performs graph traversal.
    """
    object_id = str(object_id or "").strip()
    if not object_id:
        raise ProjectAnatomyContextError("object_id is required")

    objects = _objects_by_id(projection)
    root = objects.get(object_id)
    if root is None:
        raise ProjectAnatomyContextError(f"unknown Project Anatomy object: {object_id}")

    admitted = {str(value).strip() for value in admitted_object_ids or [object_id] if str(value).strip()}
    if object_id not in admitted:
        raise ProjectAnatomyContextError("root object is outside the admitted object identities")

    relation_rows: list[dict[str, Any]] = []
    neighbour_ids: set[str] = set()
    for claim in root.get("relations") or []:
        if not isinstance(claim, dict):
            continue
        subject_id = _entity_id(claim.get("subject_ref"))
        target_id = _entity_id(claim.get("object_ref"))
        other_id = target_id if subject_id == object_id else subject_id if target_id == object_id else None
        if other_id:
            neighbour_ids.add(other_id)
        relation_rows.append(
            {
                "claim": deepcopy(claim),
                "semantics": relation_semantics(str(claim.get("relation_type") or "unknown")),
                "other_object_ref": (
                    {"entity_type": "stable_object", "entity_id": other_id}
                    if other_id
                    else None
                ),
                "other_object_materializable": bool(other_id and other_id in admitted),
            }
        )

    neighbours = []
    withheld = []
    for neighbour_id in sorted(neighbour_ids):
        if neighbour_id in admitted and neighbour_id in objects:
            neighbour = objects[neighbour_id]
            neighbours.append(
                {
                    "object_id": neighbour_id,
                    "object_family": neighbour.get("object_family"),
                    "display_name": neighbour.get("display_name"),
                    "revision": neighbour.get("revision"),
                }
            )
        else:
            withheld.append(
                {
                    "entity_ref": {"entity_type": "stable_object", "entity_id": neighbour_id},
                    "reason": "outside_explicitly_admitted_object_scope",
                }
            )

    matched_requirements, unresolved_requirements = _direct_requirements(root, requirements)
    source_refs = set(root.get("source_representation_refs") or [])
    for row in matched_requirements:
        source = (row.get("requirement") or {}).get("source") or {}
        source_artifact_ref = str(source.get("source_artifact_ref") or "").strip()
        if source_artifact_ref:
            source_refs.add(source_artifact_ref)

    return {
        "kind": "project_anatomy_object_context_slice",
        "version": CONTEXT_SLICE_VERSION,
        "project_ref": projection.get("project_ref"),
        "owner_revision": projection.get("owner_revision"),
        "root_object": {
            "object_id": object_id,
            "object_family": root.get("object_family"),
            "display_name": root.get("display_name"),
            "internal_code": root.get("internal_code"),
            "aliases": list(root.get("aliases") or []),
            "revision": root.get("revision"),
            "attribute_claims": deepcopy(root.get("attribute_claims") or []),
            "phase_refs": list(root.get("phase_refs") or []),
            "attention_claim_refs": list(root.get("attention_claim_refs") or []),
        },
        "relations": relation_rows,
        "neighbours": neighbours,
        "withheld_neighbour_refs": withheld,
        "requirements": matched_requirements,
        "unresolved_requirement_selectors": unresolved_requirements,
        "source_refs": sorted(source_refs),
        "scope": {
            "admitted_object_ids": sorted(admitted),
            "implicit_traversal_performed": False,
            "global_search_performed": False,
        },
        "authority": {
            "projection_only": True,
            "creates_project_fact": False,
            "creates_relation_claim": False,
            "resolves_compliance": False,
            "is_evidence": False,
            "is_decision": False,
            "authorizes_effect": False,
        },
        "non_equivalences": [
            "context slice != project truth",
            "relation semantics != relation claim",
            "requirement != observation",
            "requirement matched != compliance resolved",
            "neighbour reference != neighbour context admission",
            "projection != persistence",
        ],
    }
