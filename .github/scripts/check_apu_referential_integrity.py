#!/usr/bin/env python3
"""Read-only referential-integrity check for the canonical APU V0.2 dossier.

The check validates the V0.2 worked dossier under
``docs/examples/architecture_project_understanding_v02_dossier/``. The former
V0.1 dossier remains available as historical migration material but is no longer
the canonical CI target.

The check:

1. validates each V0.2 instance against its governed schema;
2. builds one dossier-wide id index and fails closed on duplicate ids;
3. checks internal entity/claim/provenance references;
4. verifies that the worked identity relation links a source representation to a
   stable object without granting canonical identity.

It never mutates files, executes a workflow, routes a provider, promotes memory
or authorizes a source/model write.
"""

from __future__ import annotations

from pathlib import Path
import sys

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = ROOT / "docs/examples/architecture_project_understanding_v02_dossier"
SCHEMA_DIR = ROOT / "schemas/architecture-project-understanding"

FILE_SCHEMA = {
    "program.yaml": "program.schema.yaml",
    "requirement_clear_width.yaml": "requirement.schema.yaml",
    "stable_object_door.yaml": "stable_object.schema.yaml",
    "source_representation_revit_door.yaml": "source_representation.schema.yaml",
    "attribute_claim_clear_width.yaml": "attribute_claim.schema.yaml",
    "relation_claim_identity.yaml": "relation_claim.schema.yaml",
    "derivation_identity.yaml": "derivation.schema.yaml",
}

ID_FIELDS = {
    "program.schema.yaml": "program_id",
    "requirement.schema.yaml": "requirement_id",
    "stable_object.schema.yaml": "stable_object_id",
    "source_representation.schema.yaml": "representation_id",
    "attribute_claim.schema.yaml": "attribute_claim_id",
    "relation_claim.schema.yaml": "relation_claim_id",
    "derivation.schema.yaml": "derivation_id",
}

EXTERNAL_PREFIXES = (
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
    "REVIT-",
    "SNAPSHOT-",
)


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def is_external(value: str) -> bool:
    return any(value.startswith(prefix) for prefix in EXTERNAL_PREFIXES)


def build_id_index(docs: dict[str, dict]) -> tuple[dict[str, str], list[str]]:
    id_index: dict[str, str] = {}
    errors: list[str] = []

    for filename, schema_name in FILE_SCHEMA.items():
        instance = docs.get(filename)
        if not instance:
            continue
        id_field = ID_FIELDS[schema_name]
        value = str(instance[id_field])
        previous = id_index.get(value)
        if previous is not None:
            errors.append(
                f"duplicate id '{value}': first declared by {previous}, repeated by {filename}"
            )
            continue
        id_index[value] = filename

    return id_index, errors


def main() -> int:
    errors: list[str] = []
    docs: dict[str, dict] = {}

    if not DOSSIER.exists():
        print(f"FAIL: dossier missing: {DOSSIER.relative_to(ROOT)}", file=sys.stderr)
        return 1

    validator_cls = jsonschema.Draft202012Validator
    fmt = jsonschema.FormatChecker()

    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    shared = Resource.from_contents(
        load(SCHEMA_DIR / "shared.schema.yaml"), default_specification=DRAFT202012
    )
    registry = Registry().with_resource(uri="shared.schema.yaml", resource=shared)

    # 1. Schema validation.
    for filename, schema_name in FILE_SCHEMA.items():
        fpath = DOSSIER / filename
        spath = SCHEMA_DIR / schema_name
        if not fpath.is_file():
            errors.append(f"missing dossier file: {filename}")
            continue
        if not spath.is_file():
            errors.append(f"missing schema: {schema_name}")
            continue
        instance = load(fpath)
        docs[filename] = instance
        schema = load(spath)
        validator_cls.check_schema(schema)
        for error in sorted(
            validator_cls(schema, format_checker=fmt, registry=registry).iter_errors(instance),
            key=lambda item: list(item.path),
        ):
            path = ".".join(str(part) for part in error.path) or "<root>"
            errors.append(f"{filename}: schema: {path}: {error.message}")

    # 2. Dossier-wide id uniqueness.
    id_index, id_errors = build_id_index(docs)
    errors.extend(id_errors)

    def must_resolve(value: object, where: str) -> None:
        if value is None:
            return
        text = str(value)
        if text in id_index or is_external(text):
            return
        errors.append(f"{where}: unresolved reference '{text}'")

    def entity_ref(value: object, where: str) -> None:
        if not isinstance(value, dict):
            return
        entity_id = value.get("entity_id")
        entity_type = value.get("entity_type")
        must_resolve(entity_id, f"{where}.entity_id")
        filename = id_index.get(str(entity_id)) if entity_id is not None else None
        if filename is None or entity_type is None:
            return
        schema_name = FILE_SCHEMA[filename]
        actual_type = {
            "stable_object.schema.yaml": "stable_object",
            "source_representation.schema.yaml": "source_representation",
        }.get(schema_name)
        if actual_type is not None and actual_type != entity_type:
            errors.append(
                f"{where}: '{entity_id}' declares {entity_type} but resolves to {actual_type}"
            )

    # 3. V0.2 cross-reference checks.
    for filename, instance in docs.items():
        schema_name = FILE_SCHEMA[filename]

        if schema_name == "requirement.schema.yaml":
            origin = instance.get("origin") or {}
            if origin.get("origin_kind") == "program":
                must_resolve(origin.get("origin_ref"), f"{filename}.origin.origin_ref")
            for field in ("target", "related_target"):
                target = instance.get(field) or {}
                entity_ref(target.get("entity_ref"), f"{filename}.{field}.entity_ref")

        elif schema_name == "source_representation.schema.yaml":
            must_resolve(instance.get("calibration_ref"), f"{filename}.calibration_ref")

        elif schema_name == "attribute_claim.schema.yaml":
            entity_ref(instance.get("subject_ref"), f"{filename}.subject_ref")
            for ref in instance.get("source_representation_refs", []):
                must_resolve(ref, f"{filename}.source_representation_refs")
            for ref in instance.get("derivation_refs", []):
                must_resolve(ref, f"{filename}.derivation_refs")
            must_resolve(instance.get("supersedes_claim_ref"), f"{filename}.supersedes_claim_ref")

        elif schema_name == "relation_claim.schema.yaml":
            entity_ref(instance.get("subject_ref"), f"{filename}.subject_ref")
            entity_ref(instance.get("object_ref"), f"{filename}.object_ref")
            for ref in instance.get("source_representation_refs", []):
                must_resolve(ref, f"{filename}.source_representation_refs")
            for ref in instance.get("derivation_refs", []):
                must_resolve(ref, f"{filename}.derivation_refs")
            must_resolve(
                instance.get("supersedes_relation_claim_ref"),
                f"{filename}.supersedes_relation_claim_ref",
            )

        elif schema_name == "derivation.schema.yaml":
            for ref in instance.get("produces_claim_refs", []):
                must_resolve(ref, f"{filename}.produces_claim_refs")
            for ref in instance.get("input_refs", []):
                must_resolve(ref, f"{filename}.input_refs")

    # 4. Worked identity relation remains candidate-only and source -> project.
    identity = docs.get("relation_claim_identity.yaml") or {}
    if identity.get("relation_type") != "identity.represents":
        errors.append("relation_claim_identity.yaml: expected identity.represents")
    if (identity.get("subject_ref") or {}).get("entity_type") != "source_representation":
        errors.append("relation_claim_identity.yaml: subject must be source_representation")
    if (identity.get("object_ref") or {}).get("entity_type") != "stable_object":
        errors.append("relation_claim_identity.yaml: object must be stable_object")
    if identity.get("proof_status") == "accepted_as_support":
        errors.append("relation_claim_identity.yaml: worked identity relation must remain candidate")

    if errors:
        print("Architecture Project Understanding V0.2 referential-integrity check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"OK: {len(docs)} V0.2 dossier instances valid; ids are unique and references resolve."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
