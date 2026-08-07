#!/usr/bin/env python3
"""Read-only referential-integrity check for the worked APU dossier.

Project Anatomy V0.2 has one canonical identity/value/relation path. The worked
fixture also keeps a bounded set of V0.1 files as compatibility evidence. This
check validates both surfaces while preventing compatibility-only carriers from
being counted as canonical V0.2 output.

It never mutates files, executes adapters, routes providers, admits Evidence or
promotes memory.
"""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import jsonschema
import yaml
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = ROOT / "docs/examples/architecture_project_understanding_dossier"
SCHEMA_DIR = ROOT / "schemas/architecture-project-understanding"
COMPATIBILITY_REGISTRY = SCHEMA_DIR / "compatibility.registry.yaml"

CANONICAL_FILE_SCHEMA = {
    "program.yaml": "program.schema.yaml",
    "requirement_area.yaml": "requirement.schema.yaml",
    "requirement_count.yaml": "requirement.schema.yaml",
    "calibration.yaml": "calibration.schema.yaml",
    "derivation_area.yaml": "derivation.schema.yaml",
    "attribute_claim_area.yaml": "attribute_claim.schema.yaml",
    "stable_object_chambre.yaml": "stable_object.schema.yaml",
    "stable_object_sdb.yaml": "stable_object.schema.yaml",
    "stable_object_door.yaml": "stable_object.schema.yaml",
    "source_representation_door.yaml": "source_representation.schema.yaml",
    "relation_claim_door_identity.yaml": "relation_claim.schema.yaml",
    "relation_claim_opens.yaml": "relation_claim.schema.yaml",
}

# Retained solely to prove that historical files are still readable. These
# carriers are not canonical V0.2 output.
COMPATIBILITY_FILE_SCHEMA = {
    "evidence_area.yaml": "evidence.schema.yaml",
    "object_identity_door.yaml": "object_identity.schema.yaml",
    "object_relation_opens.yaml": "object_relation.schema.yaml",
    "spatial_node_level.yaml": "spatial_node.schema.yaml",
    "space_group_t2.yaml": "space_group.schema.yaml",
    "deviation_area.yaml": "deviation.schema.yaml",
    "human_override_door.yaml": "human_override.schema.yaml",
}

ID_FIELDS = {
    "program.schema.yaml": "program_id",
    "requirement.schema.yaml": "requirement_id",
    "calibration.schema.yaml": "calibration_id",
    "derivation.schema.yaml": "derivation_id",
    "attribute_claim.schema.yaml": "attribute_claim_id",
    "stable_object.schema.yaml": "stable_object_id",
    "source_representation.schema.yaml": "representation_id",
    "relation_claim.schema.yaml": "relation_claim_id",
    "evidence.schema.yaml": "evidence_id",
    "object_relation.schema.yaml": "relation_id",
    "spatial_node.schema.yaml": "spatial_node_id",
    "space_group.schema.yaml": "space_group_id",
    "deviation.schema.yaml": "deviation_id",
    "human_override.schema.yaml": "human_override_id",
    # object_identity.stable_id is a reference to stable_object, not a second id.
}

EXTERNAL_PREFIXES = (
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


def load(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def is_external(value: str) -> bool:
    return any(value.startswith(prefix) for prefix in EXTERNAL_PREFIXES)


def build_id_index(
    docs: dict[str, dict[str, Any]],
) -> tuple[dict[str, str], list[str]]:
    """Build the dossier id namespace and fail closed on duplicate declarations.

    Kept as a small pure helper because root tests and other read-only governance
    checks use it directly. Compatibility V0.1 object_identity.stable_id is not a
    declaration and therefore never creates a second identity here.
    """
    id_index: dict[str, str] = {}
    errors: list[str] = []
    for filename, instance in docs.items():
        schema_name = CANONICAL_FILE_SCHEMA.get(filename) or COMPATIBILITY_FILE_SCHEMA.get(filename)
        if schema_name is None:
            continue
        id_field = ID_FIELDS.get(schema_name)
        if not id_field or id_field not in instance:
            continue
        value = str(instance[id_field])
        previous = id_index.get(value)
        if previous is not None:
            errors.append(
                f"duplicate id '{value}': first declared by {previous}, repeated by {filename}"
            )
        else:
            id_index[value] = filename
    return id_index, errors


def main() -> int:
    errors: list[str] = []
    canonical_docs: dict[str, dict[str, Any]] = {}
    compatibility_docs: dict[str, dict[str, Any]] = {}

    if not DOSSIER.exists():
        print(f"FAIL: dossier missing: {DOSSIER.relative_to(ROOT)}", file=sys.stderr)
        return 1

    validator_cls = jsonschema.Draft202012Validator
    fmt = jsonschema.FormatChecker()
    shared = Resource.from_contents(
        load(SCHEMA_DIR / "shared.schema.yaml"),
        default_specification=DRAFT202012,
    )
    registry = Registry().with_resource(uri="shared.schema.yaml", resource=shared)

    compatibility_registry = load(COMPATIBILITY_REGISTRY)
    compatibility_entries = compatibility_registry.get("entries") or {}
    if not isinstance(compatibility_entries, dict):
        errors.append("compatibility registry entries must be a mapping")
        compatibility_entries = {}

    def validate_files(
        mapping: dict[str, str],
        target: dict[str, dict[str, Any]],
        *,
        compatibility_only: bool,
    ) -> None:
        for filename, schema_name in mapping.items():
            fpath = DOSSIER / filename
            spath = SCHEMA_DIR / schema_name
            if not fpath.is_file():
                errors.append(f"missing dossier file: {filename}")
                continue
            if not spath.is_file():
                errors.append(f"missing schema: {schema_name}")
                continue
            instance = load(fpath)
            target[filename] = instance
            schema = load(spath)
            validator_cls.check_schema(schema)
            for error in sorted(
                validator_cls(
                    schema,
                    format_checker=fmt,
                    registry=registry,
                ).iter_errors(instance),
                key=lambda item: list(item.path),
            ):
                path = ".".join(str(part) for part in error.path) or "<root>"
                prefix = "compatibility" if compatibility_only else "canonical"
                errors.append(f"{prefix}:{filename}: schema: {path}: {error.message}")

            if compatibility_only:
                carrier = schema_name.removesuffix(".schema.yaml")
                entry = compatibility_entries.get(carrier)
                if not isinstance(entry, dict) or entry.get("status") != "compatibility_only":
                    errors.append(
                        f"compatibility:{filename}: {carrier} is not registered compatibility_only"
                    )
                elif entry.get("canonical_emission") is not False:
                    errors.append(
                        f"compatibility:{filename}: {carrier} must refuse canonical emission"
                    )

    validate_files(
        CANONICAL_FILE_SCHEMA,
        canonical_docs,
        compatibility_only=False,
    )
    validate_files(
        COMPATIBILITY_FILE_SCHEMA,
        compatibility_docs,
        compatibility_only=True,
    )

    # One reference namespace across canonical and compatibility material, but
    # object_identity.stable_id is intentionally not declared a second identity.
    id_index, duplicate_errors = build_id_index(
        {**canonical_docs, **compatibility_docs}
    )
    errors.extend(duplicate_errors)

    def must_resolve(value: Any, where: str) -> None:
        if value is None or value == "":
            return
        text = str(value)
        if text in id_index or is_external(text):
            return
        errors.append(f"{where}: unresolved reference '{text}'")

    def entity_ref(value: Any, where: str) -> None:
        if isinstance(value, dict):
            must_resolve(value.get("entity_id"), f"{where}.entity_id")

    # Canonical V0.2 refs. Evidence anchors are intentionally not resolved against
    # the retained APU evidence fixture: Architecture Proof Register is authoritative.
    for filename, instance in canonical_docs.items():
        schema_name = CANONICAL_FILE_SCHEMA[filename]
        if schema_name == "requirement.schema.yaml":
            source = instance.get("source") or {}
            if source.get("source_type") == "program":
                must_resolve(source.get("source_ref"), f"{filename}.source.source_ref")
            target = instance.get("target") or {}
            entity_ref(target.get("entity_ref"), f"{filename}.target.entity_ref")
            related = (instance.get("constraint") or {}).get("related_target") or {}
            entity_ref(
                related.get("entity_ref"),
                f"{filename}.constraint.related_target.entity_ref",
            )
        elif schema_name == "derivation.schema.yaml":
            for produced in instance.get("produces") or []:
                if isinstance(produced, dict):
                    must_resolve(
                        produced.get("claim_id"),
                        f"{filename}.produces.claim_id",
                    )
            for item in instance.get("inputs") or []:
                must_resolve(item, f"{filename}.inputs")
        elif schema_name == "attribute_claim.schema.yaml":
            entity_ref(instance.get("subject_ref"), f"{filename}.subject_ref")
            for item in instance.get("source_representation_refs") or []:
                must_resolve(item, f"{filename}.source_representation_refs")
            for item in instance.get("derivation_refs") or []:
                must_resolve(item, f"{filename}.derivation_refs")
        elif schema_name == "source_representation.schema.yaml":
            must_resolve(instance.get("calibration_ref"), f"{filename}.calibration_ref")
        elif schema_name == "relation_claim.schema.yaml":
            entity_ref(instance.get("subject_ref"), f"{filename}.subject_ref")
            entity_ref(instance.get("object_ref"), f"{filename}.object_ref")
            for item in instance.get("source_representation_refs") or []:
                must_resolve(item, f"{filename}.source_representation_refs")
            for item in instance.get("derivation_refs") or []:
                must_resolve(item, f"{filename}.derivation_refs")

    # Historical compatibility refs remain auditable without becoming canonical.
    for filename, instance in compatibility_docs.items():
        schema_name = COMPATIBILITY_FILE_SCHEMA[filename]
        if schema_name == "object_identity.schema.yaml":
            must_resolve(instance.get("stable_id"), f"{filename}.stable_id")
        elif schema_name == "object_relation.schema.yaml":
            must_resolve(instance.get("from"), f"{filename}.from")
            must_resolve(instance.get("to"), f"{filename}.to")
        elif schema_name == "spatial_node.schema.yaml":
            must_resolve(instance.get("parent_id"), f"{filename}.parent_id")
            for item in instance.get("member_object_ids") or []:
                must_resolve(item, f"{filename}.member_object_ids")
        elif schema_name == "space_group.schema.yaml":
            must_resolve(instance.get("parent_group_id"), f"{filename}.parent_group_id")
            for item in instance.get("members") or []:
                must_resolve(item, f"{filename}.members")
            for item in instance.get("requirement_ids") or []:
                must_resolve(item, f"{filename}.requirement_ids")
        elif schema_name == "deviation.schema.yaml":
            must_resolve(instance.get("requirement_id"), f"{filename}.requirement_id")
            must_resolve(instance.get("observed_target"), f"{filename}.observed_target")
        elif schema_name == "human_override.schema.yaml":
            target = instance.get("target") or {}
            must_resolve(
                target.get("stable_object_id"),
                f"{filename}.target.stable_object_id",
            )

    if errors:
        print(
            "Architecture Project Understanding referential-integrity check failed:",
            file=sys.stderr,
        )
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "OK: "
        f"{len(canonical_docs)} canonical V0.2 dossier instance(s) valid; "
        f"{len(compatibility_docs)} compatibility-only V0.1 instance(s) remain readable; "
        "ids are unique and references resolve; deprecated carriers cannot be canonical emission."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
