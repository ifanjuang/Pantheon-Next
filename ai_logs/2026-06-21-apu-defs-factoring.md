# 2026-06-21 APU $defs factoring + cross-file ref resolver

Status: documented non-implemented (schema refactor, approved item of #169).

Pays the "factor duplicated $defs" item of #169, with the prerequisite resolver
support that #158 flagged as blocking.

What:

- Cross-cutting definitions are factored into
  schemas/architecture-project-understanding/shared.schema.yaml (added certainty,
  claim_modality, match_axis to the existing catalogue).
- The core belief-contract schemas now reference them with cross-file
  `$ref: "shared.schema.yaml#/$defs/X"` and carry no local $defs:
  evidence, calibration, doubt, contradiction, human_override, canonization,
  stable_object, derivation, attribute_claim (~53 duplicated def blocks removed).
- Validators resolve these through a small referencing.Registry exposing the
  family shared.schema.yaml under its bare filename:
  tests/test_governance_schemas.py, tests/test_schema_examples.py and
  .github/scripts/check_apu_referential_integrity.py.
- schemas/README.md documents the mechanism.

Scope held deliberately: the program/conformance and object-model schemas keep
their schema-specific enums local for now; they can be migrated incrementally
using this established + tested mechanism. The remaining #169 item
(zone_type-when-zone) stays open.

Verified: pytest 9/9; referential-integrity 16/16; governance doctor scripts
green (baseline origin/main); mcp-server 29/29.

Boundary: schema structure factoring + test/CI resolver support only. No runtime,
no new object, no doctrine change. Refs #169.
