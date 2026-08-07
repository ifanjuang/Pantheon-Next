"""Read-only Architecture Project Understanding (APU) validation surface.

The V0.2 canonical project-understanding core is deliberately small:

- ``stable_object``: one durable project identity;
- ``source_representation``: one source-bound occurrence;
- ``attribute_claim``: one value assertion;
- ``relation_claim``: one relationship assertion.

Programme/requirement objects and supporting provenance records remain separate.
Selected V0.1 carriers are still readable during migration but are reported as
legacy compatibility objects so adapters cannot mistake them for the canonical
write shape.

Validation executes nothing, canonizes nothing and approves nothing.
"""

from __future__ import annotations

from pathlib import Path

import jsonschema
import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

from .repo import find_repo_root, read_repo_text

SCHEMA_DIR = "schemas/architecture-project-understanding"

TYPE_SCHEMA = {
    # Canonical V0.2 project/world + intent/provenance.
    "program": "program.schema.yaml",
    "requirement": "requirement.schema.yaml",
    "classification_scheme": "classification_scheme.schema.yaml",
    "stable_object": "stable_object.schema.yaml",
    "source_representation": "source_representation.schema.yaml",
    "attribute_claim": "attribute_claim.schema.yaml",
    "relation_claim": "relation_claim.schema.yaml",
    "calibration": "calibration.schema.yaml",
    "derivation": "derivation.schema.yaml",
    "contradiction": "contradiction.schema.yaml",
    # V0.1 legacy-read compatibility only. New adapters must not emit these.
    "classification": "classification.schema.yaml",
    "space_group": "space_group.schema.yaml",
    "program_change": "program_change.schema.yaml",
    "deviation": "deviation.schema.yaml",
    "evidence": "evidence.schema.yaml",
    "doubt": "doubt.schema.yaml",
    "human_override": "human_override.schema.yaml",
    "canonization": "canonization.schema.yaml",
    "spatial_node": "spatial_node.schema.yaml",
    "object_identity": "object_identity.schema.yaml",
    "object_relation": "object_relation.schema.yaml",
    "object_group": "object_group.schema.yaml",
    "property_set": "property_set.schema.yaml",
    "instance_override": "instance_override.schema.yaml",
    "object_note": "object_note.schema.yaml",
    "phase_state": "phase_state.schema.yaml",
    "analysis_context_candidate": "analysis_context_candidate.schema.yaml",
}

CANONICAL_WRITE_TYPES = frozenset(
    {
        "program",
        "requirement",
        "classification_scheme",
        "stable_object",
        "source_representation",
        "attribute_claim",
        "relation_claim",
        "calibration",
        "derivation",
        "contradiction",
    }
)

LEGACY_TYPES = frozenset(TYPE_SCHEMA) - CANONICAL_WRITE_TYPES

# ID field per type so in-dossier references can be checked. Legacy identifiers
# remain indexed only to keep historical dossiers inspectable during migration.
_ID_FIELD = {
    "program": "program_id",
    "requirement": "requirement_id",
    "classification_scheme": "scheme_id",
    "stable_object": "stable_object_id",
    "source_representation": "representation_id",
    "attribute_claim": "attribute_claim_id",
    "relation_claim": "relation_claim_id",
    "calibration": "calibration_id",
    "derivation": "derivation_id",
    "contradiction": "contradiction_id",
    "classification": "classification_id",
    "space_group": "space_group_id",
    "program_change": "program_change_id",
    "deviation": "deviation_id",
    "evidence": "evidence_id",
    "doubt": "doubt_id",
    "human_override": "human_override_id",
    "canonization": "canonization_id",
    "spatial_node": "spatial_node_id",
    "object_identity": "stable_id",
    "object_relation": "relation_id",
    "object_group": "object_group_id",
    "property_set": "property_set_id",
    "instance_override": "instance_override_id",
    "object_note": "note_id",
    "phase_state": "phase_state_id",
    "analysis_context_candidate": "analysis_context_id",
}

_EXTERNAL_PREFIXES = (
    "SRC-",
    "DET-",
    "EQ-",
    "SYS-",
    "OP-CAND-",
    "REV-",
    "MAIL-",
    "CAL-",
    "DOC-",
    "INFO-",
    "DEC-",
    "IDS-",
)


def _load_schema(name: str, root: Path) -> dict:
    return yaml.safe_load(read_repo_text(f"{SCHEMA_DIR}/{name}", root))


def _registry(root: Path) -> Registry:
    shared = _load_schema("shared.schema.yaml", root)
    resource = Resource.from_contents(shared, default_specification=DRAFT202012)
    return Registry().with_resource(uri="shared.schema.yaml", resource=resource)


def _iter_objects(dossier: dict):
    for otype, payload in dossier.items():
        if otype not in TYPE_SCHEMA:
            yield otype, None, payload, f"unknown object type: {otype}"
            continue
        items = payload if isinstance(payload, list) else [payload]
        for idx, obj in enumerate(items):
            yield otype, idx, obj, None


def validate_apu_dossier(dossier: dict) -> dict:
    """Validate a candidate APU dossier and return its non-executing gate posture."""
    if not isinstance(dossier, dict):
        return {
            "result": "error",
            "problems": ["dossier must be a mapping of object_type -> object(s)"],
        }

    root = find_repo_root()
    registry = _registry(root)
    fmt = jsonschema.FormatChecker()
    validator_cls = jsonschema.Draft202012Validator

    schema_errors: list[str] = []
    reference_errors: list[str] = []
    human_decisions_required: list[str] = []
    legacy_objects: list[str] = []
    id_index: dict[str, str] = {}
    validated = 0

    schema_cache: dict[str, dict] = {}
    objects: list[tuple[str, int, dict]] = []

    for otype, idx, obj, err in _iter_objects(dossier):
        if err:
            schema_errors.append(err)
            continue
        if not isinstance(obj, dict):
            schema_errors.append(f"{otype}[{idx}]: not a mapping")
            continue
        objects.append((otype, idx, obj))
        if otype in LEGACY_TYPES:
            legacy_objects.append(f"{otype}[{idx}]")

        schema = schema_cache.get(otype)
        if schema is None:
            schema = _load_schema(TYPE_SCHEMA[otype], root)
            schema_cache[otype] = schema
        for error in sorted(
            validator_cls(schema, format_checker=fmt, registry=registry).iter_errors(obj),
            key=lambda item: list(item.path),
        ):
            path = ".".join(str(part) for part in error.path) or "<root>"
            schema_errors.append(f"{otype}[{idx}].{path}: {error.message}")
        validated += 1

        id_field = _ID_FIELD.get(otype)
        if id_field and id_field in obj:
            object_id = str(obj[id_field])
            if object_id in id_index:
                schema_errors.append(
                    f"{otype}[{idx}].{id_field}: duplicate dossier id '{object_id}'"
                )
            else:
                id_index[object_id] = otype

    def _resolves(value) -> bool:
        if value is None:
            return True
        text = str(value)
        return text in id_index or any(text.startswith(prefix) for prefix in _EXTERNAL_PREFIXES)

    def _ref(value, label) -> None:
        if value is not None and not _resolves(value):
            reference_errors.append(f"{label} '{value}' unresolved")

    def _refs(values, label) -> None:
        for value in values or []:
            if not _resolves(value):
                reference_errors.append(f"{label} '{value}' unresolved")

    def _entity_ref(value, label) -> None:
        if not isinstance(value, dict):
            return
        entity_id = value.get("entity_id")
        entity_type = value.get("entity_type")
        if entity_id is None:
            return
        _ref(entity_id, f"{label}.entity_id")
        indexed_type = id_index.get(str(entity_id))
        if indexed_type is not None and entity_type is not None and indexed_type != entity_type:
            reference_errors.append(
                f"{label} '{entity_id}' declares {entity_type} but resolves to {indexed_type}"
            )

    # Cross-reference checks are intentionally light. Validation is a governance
    # chokepoint, not a graph runtime and not an approval engine.
    for otype, idx, obj in objects:
        tag = f"{otype}[{idx}]"

        if otype == "source_representation":
            _ref(obj.get("calibration_ref"), f"{tag}.calibration_ref")

        elif otype == "attribute_claim":
            _entity_ref(obj.get("subject_ref"), f"{tag}.subject_ref")
            _refs(obj.get("source_representation_refs"), f"{tag}.source_representation_refs")
            _refs(obj.get("derivation_refs"), f"{tag}.derivation_refs")
            _ref(obj.get("supersedes_claim_ref"), f"{tag}.supersedes_claim_ref")

        elif otype == "relation_claim":
            subject = obj.get("subject_ref") or {}
            target = obj.get("object_ref") or {}
            _entity_ref(subject, f"{tag}.subject_ref")
            _entity_ref(target, f"{tag}.object_ref")
            _refs(obj.get("source_representation_refs"), f"{tag}.source_representation_refs")
            _refs(obj.get("derivation_refs"), f"{tag}.derivation_refs")
            _ref(
                obj.get("supersedes_relation_claim_ref"),
                f"{tag}.supersedes_relation_claim_ref",
            )
            if (
                subject.get("entity_type") == target.get("entity_type")
                and subject.get("entity_id")
                and subject.get("entity_id") == target.get("entity_id")
            ):
                reference_errors.append(f"{tag}: relation cannot target the same entity")
            if obj.get("relation_type") == "identity.represents" and (
                obj.get("assertion_mode") in {"proposed", "derived"}
                or obj.get("proof_status") not in {"accepted_as_support"}
            ):
                human_decisions_required.append(
                    f"{tag}: source-to-project identity match needs governed review"
                )

        elif otype == "derivation":
            _refs(obj.get("produces_claim_refs"), f"{tag}.produces_claim_refs")

        elif otype == "requirement":
            origin = obj.get("origin") or {}
            if origin.get("origin_kind") == "program":
                _ref(origin.get("origin_ref"), f"{tag}.origin.origin_ref")
            for field in ("target", "related_target"):
                target = obj.get(field) or {}
                _entity_ref(target.get("entity_ref"), f"{tag}.{field}.entity_ref")

        elif otype == "contradiction":
            if obj.get("resolution") == "pending_human":
                human_decisions_required.append(
                    f"{tag}: contradiction pending human resolution"
                )

        # --- V0.1 legacy-read cross-reference checks ---
        elif otype == "deviation":
            _ref(obj.get("requirement_id"), f"{tag}.requirement_id")
            if obj.get("resolution") == "pending_human":
                human_decisions_required.append(
                    f"{tag}: legacy deviation pending human resolution"
                )
        elif otype == "object_relation":
            _ref(obj.get("from"), f"{tag}.from")
            _ref(obj.get("to"), f"{tag}.to")
        elif otype == "property_set":
            _ref(obj.get("applies_to"), f"{tag}.applies_to")
        elif otype == "instance_override":
            _ref(obj.get("target"), f"{tag}.target")
            overrides = obj.get("overrides")
            if isinstance(overrides, str) and overrides:
                _ref(overrides.split(".", 1)[0], f"{tag}.overrides")
        elif otype == "object_group":
            _refs(obj.get("members"), f"{tag}.members")
        elif otype == "object_note":
            _ref(obj.get("target_object"), f"{tag}.target_object")
        elif otype in ("phase_state", "analysis_context_candidate"):
            _ref(obj.get("target"), f"{tag}.target")
        elif otype == "spatial_node":
            _ref(obj.get("parent_id"), f"{tag}.parent_id")
            _refs(obj.get("member_object_ids"), f"{tag}.member_object_ids")
        elif otype == "classification":
            about = obj.get("about") or {}
            _ref(about.get("stable_object_id"), f"{tag}.about.stable_object_id")
            _ref(about.get("space_group_id"), f"{tag}.about.space_group_id")
        elif otype == "program_change":
            _ref(obj.get("target_program"), f"{tag}.target_program")
        elif otype == "space_group":
            _ref(obj.get("parent_group_id"), f"{tag}.parent_group_id")
            _refs(obj.get("members"), f"{tag}.members")
            _refs(obj.get("requirement_ids"), f"{tag}.requirement_ids")

    result = "ok" if not (schema_errors or reference_errors) else "error"
    return {
        "result": result,
        "validated": validated,
        "schema_errors": schema_errors,
        "reference_errors": reference_errors,
        "compatibility": {
            "legacy_read": bool(legacy_objects),
            "legacy_objects": legacy_objects,
            "canonical_write_types": sorted(CANONICAL_WRITE_TYPES),
        },
        "gate": {
            "posture": "candidate-only",
            "canonical_effect": False,
            # Retained empty for response compatibility; V0.2 claims cannot carry
            # self-declared use approvals at all.
            "regulatory_claims_without_approval": [],
            "human_decisions_required": human_decisions_required,
        },
    }
