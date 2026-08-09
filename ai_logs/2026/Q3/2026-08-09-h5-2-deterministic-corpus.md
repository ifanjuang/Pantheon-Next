# 2026-08-09 — H5.2 deterministic Project Anatomy corpus

## Objective

Qualify the canonical Observation Bundle and the existing four Project Anatomy
primitives against a bounded source-independent adversarial corpus before any
further external-adapter expansion.

Canonical baseline:

```text
Pantheon-Next 7cef8075525e016b7554b29bf0ed2c1cf673e855
pantheon-mvp  362f22bad137d9e396a91d7faa3ebb21f1f689cf
```

## Repository truth

- H5.1 already supplies one executable Observation Bundle schema;
- the existing example and tests prove elementary contract behavior but do not
  retain one human-readable multi-scenario qualification corpus;
- MVP already owns append-only persistence and later governed application;
- Revit live qualification remains unproven and outside this slice.

## Decision

Add one deterministic YAML corpus composed from the canonical example. Scenario
arrays replace the base arrays and scenario mappings recursively override the
base mapping. This fixture-only composition introduces no runtime protocol.

The corpus covers complete observation, contradictions, partial coverage,
late receipt, byte/index ambiguity, duplicate labels, mixed granularity,
physical-versus-contractual boundaries and urgent non-authorizing observations.
Two invalid cases assert the exact governed schema path for unsafe absence
inference and prescriptive material masquerading as observation.

No schema, primitive, persistence owner, migration, adapter runtime or authority
surface is added.

## Validation

```text
targeted schema/baseline suite: 32 passed
ruff: clean
git diff --check: clean
```

Full-suite and exact-head CI evidence must be recorded before merge.
