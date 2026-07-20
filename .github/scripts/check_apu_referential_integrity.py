#!/usr/bin/env python3
"""Read-only referential-integrity check for an Architecture Project Understanding dossier.

It addresses issue #169 ("add referential-integrity controls for ids and refs,
otherwise provenance chains cannot be trusted") without changing any schema.

For the worked dossier under
docs/examples/architecture_project_understanding_dossier/ it:

1. validates every instance against its real schema in
   schemas/architecture-project-understanding/ (Draft 2020-12, self-contained);
2. builds one dossier-wide id index and fails closed on duplicate ids;
3. checks that internal cross-references resolve, tolerating known external
   prefixes (source artifacts, raw detections, equipment, systems, source
   candidates) that live outside this governance dossier.

It never mutates files, runs a workflow, routes a provider or promotes memory.
"""

from __future__ import annotations

from pathlib import Path
import sys

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[2]
DOSSIER = ROOT / "docs/examples/architecture_project_understanding_dossier"
SCHEMA_DIR = ROOT / "schemas/architecture-project-understanding"

# dossier file -> schema file (same family)
FILE_SCHEMA = {
    "program.yaml": "program.schema.yaml",
    "requirement_area.yaml": "requirement.schema.yaml",
    "requirement_count.yaml": "requirement.schema.yaml",
    "calibration.yaml": "calibration.schema.yaml",
    "evidence_area.yaml": "evidence.schema.yaml",
    "derivation_area.yaml": "derivation.schema.yaml",
    "attribute_claim_area.yaml": "attribute_claim.schema.yaml",
    "stable_object_chambre.yaml": "stable_object.schema.yaml",
    "stable_object_sdb.yaml": "stable_object.schema.yaml",
    "stable_object_door.yaml": "stable_object.schema.yaml",
    "object_identity_door.yaml": "object_identity.schema.yaml",
    "object_relation_opens.yaml": "object_relation.schema.yaml",
    "spatial_node_level.yaml": "spatial_node.schema.yaml",
    "space_group_t2.yaml": "space_group.schema.yaml",
    "deviation_area.yaml": "deviation.schema.yaml",
    "human_override_door.yaml": "human_override.schema.yaml",
}

# id field carried by each schema family member
ID_FIELDS = {
    "program.schema.yaml": "program_id",
    "requirement.schema.yaml": "requirement_id",
    "calibration.schema.yaml": "calibration_id",
    "evidence.schema.yaml": "evidence_id",
    "derivation.schema.yaml": "derivation_id",
    "attribute_claim.schema.yaml": "attribute_claim_id",
    "stable_object.schema.yaml": "stable_object_id",
    "object_relation.schema.yaml": "relation_id",
    "spatial_node.schema.yaml": "spatial_node_id",
    "space_group.schema.yaml": "space_group_id",
    "deviation.schema.yaml": "deviation_id",
    "human_override.schema.yaml": "human_override_id",
    # object_identity reuses an existing stable_object id (stable_id), checked separately
}

# id prefixes that are deliberately external to this governance dossier
EXTERNAL_PREFIXES = ("SRC-", "DET-", "EQ-", "SYS-", "OP-CAND-")


def load(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def is_external(value: str) -> bool:
    return any(value.startswith(p) for p in EXTERNAL_PREFIXES)


def build_id_index(docs: dict[str, dict]) -> tuple[dict[str, str], list[str]]:
    """Build the dossier-wide id index and report duplicate declarations.

    Cross-schema identifiers share one namespace inside a dossier because
    references are plain strings. Silent overwrite would make later reference
    checks appear green while provenance points to an ambiguous object.
    """

    id_index: dict[str, str] = {}
    errors: list[str] = []

    for filename, schema_name in FILE_SCHEMA.items():
        inst = docs.get(filename)
        if not inst:
            continue
        id_field = ID_FIELDS.get(schema_name)
        if not id_field or id_field not in inst:
            continue

        value = str(inst[id_field])
        previous = id_index.get(value)
        if previous is not None:
            errors.append(
                f"duplicate id '{value}': first declared by {previous}, "
                f"repeated by {filename}"
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

    # Registry so factored cross-file refs ("shared.schema.yaml#/$defs/X") resolve.
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    shared = Resource.from_contents(
        load(SCHEMA_DIR / "shared.schema.yaml"), default_specification=DRAFT202012
    )
    registry = Registry().with_resource(uri="shared.schema.yaml", resource=shared)

    # 1. schema validation
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
        for e in sorted(
            validator_cls(
                schema, format_checker=fmt, registry=registry
            ).iter_errors(instance),
            key=lambda x: list(x.path),
        ):
            path = ".".join(str(p) for p in e.path) or "<root>"
            errors.append(f"{filename}: schema: {path}: {e.message}")

    # 2. dossier-wide id uniqueness
    id_index, id_errors = build_id_index(docs)
    errors.extend(id_errors)

    def must_resolve(value: str, where: str) -> None:
        if value is None:
            return
        value = str(value)
        if value in id_index or is_external(value):
            return
        errors.append(f"{where}: unresolved reference '{value}'")

    # 3. cross-reference checks
    for filename, inst in docs.items():
        schema_name = FILE_SCHEMA[filename]
        if schema_name == "requirement.schema.yaml":
            must_resolve(inst.get("from_program"), f"{filename}.from_program")
        elif schema_name == "derivation.schema.yaml":
            must_resolve(
                (inst.get("produces") or {}).get("stable_object_id"),
                f"{filename}.produces",
            )
            for i in inst.get("inputs", []):
                must_resolve(i, f"{filename}.inputs")
        elif schema_name == "attribute_claim.schema.yaml":
            must_resolve(
                (inst.get("about") or {}).get("stable_object_id"),
                f"{filename}.about",
            )
            for d in inst.get("derived_from", []):
                must_resolve(d, f"{filename}.derived_from")
            for ev in inst.get("evidence_refs", []):
                must_resolve(ev.get("evidence_id"), f"{filename}.evidence_refs")
        elif schema_name == "stable_object.schema.yaml":
            for m in inst.get("matches", []):
                must_resolve(
                    m.get("source_candidate_id"),
                    f"{filename}.matches.source_candidate_id",
                )
        elif schema_name == "object_identity.schema.yaml":
            must_resolve(inst.get("stable_id"), f"{filename}.stable_id")
        elif schema_name == "object_relation.schema.yaml":
            must_resolve(inst.get("from"), f"{filename}.from")
            must_resolve(inst.get("to"), f"{filename}.to")
        elif schema_name == "spatial_node.schema.yaml":
            must_resolve(inst.get("parent_id"), f"{filename}.parent_id")
            for m in inst.get("member_object_ids", []):
                must_resolve(m, f"{filename}.member_object_ids")
        elif schema_name == "space_group.schema.yaml":
            for m in inst.get("members", []):
                must_resolve(m, f"{filename}.members")
        elif schema_name == "deviation.schema.yaml":
            must_resolve(inst.get("requirement_id"), f"{filename}.requirement_id")
            must_resolve(inst.get("observed_target"), f"{filename}.observed_target")
        elif schema_name == "human_override.schema.yaml":
            tgt = inst.get("target") or {}
            must_resolve(
                tgt.get("stable_object_id"),
                f"{filename}.target.stable_object_id",
            )

    # 4. one invariant: a deviation's requirement is required-modality
    req_modality = {
        inst["requirement_id"]: inst.get("modality")
        for fn, inst in docs.items()
        if FILE_SCHEMA[fn] == "requirement.schema.yaml" and "requirement_id" in inst
    }
    for fn, inst in docs.items():
        if FILE_SCHEMA[fn] == "deviation.schema.yaml":
            rid = inst.get("requirement_id")
            if rid in req_modality and req_modality[rid] != "required":
                errors.append(
                    f"{fn}: deviation targets non-required requirement '{rid}'"
                )

    if errors:
        print(
            "Architecture Project Understanding referential-integrity check failed:",
            file=sys.stderr,
        )
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1
    print(
        f"OK: {len(docs)} dossier instances valid; ids are unique and references resolve."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
