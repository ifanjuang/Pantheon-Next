"""Read-only Architecture Project Understanding (APU) validation surface.

Given a dossier of candidate APU objects, this validates each object against its
schema in the governance core and returns the gate posture as data: nothing is
executed, canonized or approved. The gate decides; the human decides.

The dossier is a mapping of object_type -> object or list of objects, e.g.::

    program: {...}
    attribute_claim: [{...}, {...}]
    contradiction: [{...}]

Object types map to schemas under
schemas/architecture-project-understanding/. Shared definitions are resolved
through a registry exposing that family's shared.schema.yaml.
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
    "program": "program.schema.yaml",
    "requirement": "requirement.schema.yaml",
    "classification": "classification.schema.yaml",
    "classification_scheme": "classification_scheme.schema.yaml",
    "space_group": "space_group.schema.yaml",
    "program_change": "program_change.schema.yaml",
    "deviation": "deviation.schema.yaml",
    "stable_object": "stable_object.schema.yaml",
    "attribute_claim": "attribute_claim.schema.yaml",
    "calibration": "calibration.schema.yaml",
    "derivation": "derivation.schema.yaml",
    "evidence": "evidence.schema.yaml",
    "doubt": "doubt.schema.yaml",
    "contradiction": "contradiction.schema.yaml",
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

# id field per type (for the id index) and external prefixes to tolerate.
# Covers every object type so any in-dossier reference can resolve; an unindexed
# type would make valid references look dangling. object_identity (object model)
# and stable_object (belief contract) are distinct identities and both index.
_ID_FIELD = {
    "program": "program_id",
    "requirement": "requirement_id",
    "classification": "classification_id",
    "classification_scheme": "scheme_id",
    "space_group": "space_group_id",
    "program_change": "program_change_id",
    "deviation": "deviation_id",
    "stable_object": "stable_object_id",
    "attribute_claim": "attribute_claim_id",
    "calibration": "calibration_id",
    "derivation": "derivation_id",
    "evidence": "evidence_id",
    "doubt": "doubt_id",
    "contradiction": "contradiction_id",
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
_EXTERNAL_PREFIXES = ("SRC-", "DET-", "EQ-", "SYS-", "OP-CAND-", "REV-", "MAIL-")


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
    """Validate a candidate APU dossier and return the gate posture as data."""
    if not isinstance(dossier, dict):
        return {"result": "error", "problems": ["dossier must be a mapping of object_type -> object(s)"]}

    root = find_repo_root()
    registry = _registry(root)
    fmt = jsonschema.FormatChecker()
    validator_cls = jsonschema.Draft202012Validator

    schema_errors: list[str] = []
    reference_errors: list[str] = []
    regulatory_without_approval: list[str] = []
    human_decisions_required: list[str] = []
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
        schema = schema_cache.get(otype)
        if schema is None:
            schema = _load_schema(TYPE_SCHEMA[otype], root)
            schema_cache[otype] = schema
        for e in sorted(
            validator_cls(schema, format_checker=fmt, registry=registry).iter_errors(obj),
            key=lambda x: list(x.path),
        ):
            path = ".".join(str(p) for p in e.path) or "<root>"
            schema_errors.append(f"{otype}[{idx}].{path}: {e.message}")
        validated += 1
        id_field = _ID_FIELD.get(otype)
        if id_field and id_field in obj:
            id_index[str(obj[id_field])] = otype

    def _resolves(value) -> bool:
        if value is None:
            return True
        value = str(value)
        return value in id_index or any(value.startswith(p) for p in _EXTERNAL_PREFIXES)

    def _ref(value, label) -> None:
        if not _resolves(value):
            reference_errors.append(f"{label} '{value}' unresolved")

    def _refs(values, label) -> None:
        for v in values or []:
            if not _resolves(v):
                reference_errors.append(f"{label} '{v}' unresolved")

    # gate posture + light cross-reference checks. References tolerate documented
    # external prefixes and absent fields; only an in-dossier-looking id that does
    # not resolve is an error.
    for otype, idx, obj in objects:
        tag = f"{otype}[{idx}]"
        if otype == "attribute_claim":
            if "regulatory_claim" in (obj.get("allowed_use") or []):
                approved = obj.get("approval_state") == "approved_for_contractual_action"
                has_evidence = bool(obj.get("evidence_refs"))
                if not (approved and has_evidence):
                    regulatory_without_approval.append(tag)
            _ref((obj.get("about") or {}).get("stable_object_id"), f"{tag}.about.stable_object_id")
            _refs(obj.get("derived_from"), f"{tag}.derived_from")
        elif otype == "requirement":
            _ref(obj.get("from_program"), f"{tag}.from_program")
        elif otype == "deviation":
            _ref(obj.get("requirement_id"), f"{tag}.requirement_id")
            if obj.get("resolution") == "pending_human":
                human_decisions_required.append(f"{tag}: deviation pending human resolution")
        elif otype == "contradiction":
            if obj.get("resolution") == "pending_human":
                human_decisions_required.append(f"{tag}: contradiction pending human resolution")
        elif otype == "stable_object":
            for m in obj.get("matches", []) or []:
                if m.get("status") in ("candidate", "presumed"):
                    human_decisions_required.append(f"{tag}: object identity match needs human confirmation")
                    break
        # --- object model (Architecture Project Object Model) references ---
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

    result = "ok" if not (schema_errors or reference_errors or regulatory_without_approval) else "error"
    return {
        "result": result,
        "validated": validated,
        "schema_errors": schema_errors,
        "reference_errors": reference_errors,
        "gate": {
            "posture": "candidate-only",
            "canonical_effect": False,
            "regulatory_claims_without_approval": regulatory_without_approval,
            "human_decisions_required": human_decisions_required,
        },
    }
