"""Read-only Architecture Project Understanding (APU) validation surface.

Canonical validation targets the Project Anatomy V0.2 core. Legacy V0.1 dossiers
are first projected through the explicit compatibility adapter; deprecated
carriers remain compatibility-only and can never become canonical output merely
because their old schema still validates.

Nothing here executes, persists, canonizes, admits Evidence or approves a claim.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import jsonschema
import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

from .apu_compat import adapt_v01_dossier, compatibility_only_types
from .repo import find_repo_root, read_repo_text

SCHEMA_DIR = "schemas/architecture-project-understanding"

TYPE_SCHEMA = {
    # V0.2 canonical/support surface.
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
    # V0.1 compatibility-only carriers. They remain readable but are never
    # canonical V0.2 emission types.
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

# Identity declarations used for dossier-wide reference resolution. object_identity
# deliberately has no entry: its ``stable_id`` is a V0.1 alias/reference to the
# canonical stable object, not a second V0.2 identity declaration.
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
    "DOC-",
    "IDS-",
)


def _load_schema(name: str, root: Path) -> dict[str, Any]:
    return yaml.safe_load(read_repo_text(f"{SCHEMA_DIR}/{name}", root))


def _registry(root: Path) -> Registry:
    shared = _load_schema("shared.schema.yaml", root)
    resource = Resource.from_contents(shared, default_specification=DRAFT202012)
    return Registry().with_resource(uri="shared.schema.yaml", resource=resource)


def _iter_objects(dossier: dict[str, Any]):
    for otype, payload in dossier.items():
        if otype not in TYPE_SCHEMA:
            yield otype, None, payload, f"unknown object type: {otype}"
            continue
        items = payload if isinstance(payload, list) else [payload]
        for idx, obj in enumerate(items):
            yield otype, idx, obj, None


def validate_apu_dossier(dossier: dict[str, Any]) -> dict[str, Any]:
    """Validate canonical V0.2 material and explicitly qualify V0.1 input."""
    if not isinstance(dossier, dict):
        return {
            "result": "error",
            "problems": ["dossier must be a mapping of object_type -> object(s)"],
        }

    root = find_repo_root()
    registry = _registry(root)
    fmt = jsonschema.FormatChecker()
    validator_cls = jsonschema.Draft202012Validator

    try:
        adapted = adapt_v01_dossier(dossier)
    except ValueError as exc:
        return {
            "result": "error",
            "validated": 0,
            "schema_errors": [],
            "reference_errors": [],
            "gate": {
                "posture": "compatibility-only",
                "canonical_effect": False,
                "canonical_emission_allowed": False,
                "regulatory_claims_without_approval": [],
                "human_decisions_required": [],
            },
            "compatibility": {
                "legacy_detected": True,
                "canonical_emission_allowed": False,
                "authority_transfer": False,
                "errors": [str(exc)],
            },
        }

    canonical_dossier = adapted["canonical_dossier"]
    compatibility_records = adapted["compatibility_records"]
    compatibility = dict(adapted["compatibility"])

    schema_errors: list[str] = list(compatibility.get("errors") or [])
    reference_errors: list[str] = []
    regulatory_without_approval: list[str] = list(
        compatibility.get("regulatory_claims_without_approval") or []
    )
    human_decisions_required: list[str] = list(
        compatibility.get("human_decisions_required") or []
    )
    id_index: dict[str, str] = {}
    canonical_objects: list[tuple[str, int, dict[str, Any]]] = []
    compatibility_objects: list[tuple[str, int, dict[str, Any]]] = []
    schema_cache: dict[str, dict[str, Any]] = {}
    canonical_validated = 0
    compatibility_validated = 0

    def validate_group(
        payload: dict[str, Any],
        *,
        compatibility_only: bool,
    ) -> None:
        nonlocal canonical_validated, compatibility_validated
        objects = compatibility_objects if compatibility_only else canonical_objects
        for otype, idx, obj, err in _iter_objects(payload):
            if err:
                schema_errors.append(err)
                continue
            if not isinstance(obj, dict):
                schema_errors.append(f"{otype}[{idx}]: not a mapping")
                continue
            if compatibility_only and otype not in compatibility_only_types(root):
                schema_errors.append(
                    f"{otype}[{idx}]: carrier is not registered compatibility_only"
                )
                continue
            objects.append((otype, idx, obj))
            schema = schema_cache.get(otype)
            if schema is None:
                schema = _load_schema(TYPE_SCHEMA[otype], root)
                schema_cache[otype] = schema
            for error in sorted(
                validator_cls(
                    schema,
                    format_checker=fmt,
                    registry=registry,
                ).iter_errors(obj),
                key=lambda item: list(item.path),
            ):
                path = ".".join(str(part) for part in error.path) or "<root>"
                prefix = "compatibility" if compatibility_only else "canonical"
                schema_errors.append(
                    f"{prefix}:{otype}[{idx}].{path}: {error.message}"
                )
            if compatibility_only:
                compatibility_validated += 1
            else:
                canonical_validated += 1

            id_field = _ID_FIELD.get(otype)
            if id_field and id_field in obj:
                value = str(obj[id_field])
                previous = id_index.get(value)
                if previous is not None:
                    schema_errors.append(
                        f"duplicate APU id '{value}': {previous} and {otype}[{idx}]"
                    )
                else:
                    id_index[value] = f"{otype}[{idx}]"

    validate_group(canonical_dossier, compatibility_only=False)
    validate_group(compatibility_records, compatibility_only=True)

    def _resolves(value: Any) -> bool:
        if value is None:
            return True
        text = str(value)
        return text in id_index or any(text.startswith(prefix) for prefix in _EXTERNAL_PREFIXES)

    def _ref(value: Any, label: str) -> None:
        if value is None or value == "":
            return
        if not _resolves(value):
            reference_errors.append(f"{label} '{value}' unresolved")

    def _refs(values: Any, label: str) -> None:
        for value in values or []:
            _ref(value, label)

    def _entity_ref(value: Any, label: str) -> None:
        if not isinstance(value, dict):
            return
        _ref(value.get("entity_id"), f"{label}.entity_id")

    # V0.2 canonical/support reference checks. Evidence refs intentionally do not
    # resolve against local APU evidence: Architecture Proof Register owns them.
    for otype, idx, obj in canonical_objects:
        tag = f"{otype}[{idx}]"
        if otype == "attribute_claim":
            _entity_ref(obj.get("subject_ref"), f"{tag}.subject_ref")
            _refs(
                obj.get("source_representation_refs"),
                f"{tag}.source_representation_refs",
            )
            _refs(obj.get("derivation_refs"), f"{tag}.derivation_refs")
            _ref(obj.get("supersedes_claim_ref"), f"{tag}.supersedes_claim_ref")
        elif otype == "relation_claim":
            _entity_ref(obj.get("subject_ref"), f"{tag}.subject_ref")
            _entity_ref(obj.get("object_ref"), f"{tag}.object_ref")
            _refs(
                obj.get("source_representation_refs"),
                f"{tag}.source_representation_refs",
            )
            _refs(obj.get("derivation_refs"), f"{tag}.derivation_refs")
            _ref(obj.get("supersedes_claim_ref"), f"{tag}.supersedes_claim_ref")
            if obj.get("relation_type") == "identity.represents" and obj.get(
                "proof_status"
            ) in {"candidate", "requires_more_evidence", "contradictory_evidence"}:
                human_decisions_required.append(
                    f"{tag}: identity relation remains candidate/review material"
                )
        elif otype == "requirement":
            source = obj.get("source") or {}
            if source.get("source_type") == "program":
                _ref(source.get("source_ref"), f"{tag}.source.source_ref")
            target = obj.get("target") or {}
            _entity_ref(target.get("entity_ref"), f"{tag}.target.entity_ref")
            constraint = obj.get("constraint") or {}
            related = constraint.get("related_target") or {}
            _entity_ref(
                related.get("entity_ref"),
                f"{tag}.constraint.related_target.entity_ref",
            )
        elif otype == "source_representation":
            _ref(obj.get("calibration_ref"), f"{tag}.calibration_ref")
        elif otype == "derivation":
            for produced in obj.get("produces") or []:
                if isinstance(produced, dict):
                    _ref(produced.get("claim_id"), f"{tag}.produces.claim_id")
            _refs(obj.get("inputs"), f"{tag}.inputs")

    # V0.1 compatibility-only references remain auditable. These checks never
    # promote the carrier into the V0.2 project-world model.
    for otype, idx, obj in compatibility_objects:
        tag = f"compatibility:{otype}[{idx}]"
        if otype == "object_identity":
            _ref(obj.get("stable_id"), f"{tag}.stable_id")
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
        elif otype == "deviation":
            _ref(obj.get("requirement_id"), f"{tag}.requirement_id")
            _ref(obj.get("observed_target"), f"{tag}.observed_target")
        elif otype == "human_override":
            target = obj.get("target") or {}
            _ref(target.get("stable_object_id"), f"{tag}.target.stable_object_id")

    result = (
        "ok"
        if not (
            schema_errors
            or reference_errors
            or regulatory_without_approval
        )
        else "error"
    )
    legacy_detected = bool(compatibility.get("legacy_detected"))
    compatibility["validated_records"] = compatibility_validated
    compatibility["canonical_validated_records"] = canonical_validated
    compatibility["errors"] = list(compatibility.get("errors") or [])

    return {
        "result": result,
        "validated": canonical_validated + compatibility_validated,
        "canonical_validated": canonical_validated,
        "compatibility_validated": compatibility_validated,
        "schema_errors": schema_errors,
        "reference_errors": reference_errors,
        "gate": {
            "posture": "compatibility-only" if legacy_detected else "candidate-only",
            "canonical_effect": False,
            "canonical_emission_allowed": bool(
                compatibility.get("canonical_emission_allowed", True)
            ),
            "regulatory_claims_without_approval": regulatory_without_approval,
            "human_decisions_required": human_decisions_required,
        },
        "compatibility": compatibility,
    }
