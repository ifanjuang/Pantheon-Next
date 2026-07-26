# 2026-07-25 — Project claim validation seam

Status: validation-only intervention trace.

## Request

Following the card-deck composition contract
(`PROJECT_CARD_DECK_COMPOSITION.md`), the maintainer approved building the
implementation seam that lets a displayed project claim cite the card that
backs it — the `project_claim` linking record — while keeping Pantheon Next a
governance layer that admits no Evidence and mutates no system of record.

## Documents consulted

- `docs/domain-packs/architecture/PROJECT_CARD_DECK_COMPOSITION.md`;
- `docs/governance/AGENCY_DATA_SYSTEM_OF_RECORD.md`;
- `docs/governance/CARD_STACK_MODEL.md`;
- `schemas/register_link.schema.yaml` (closest existing linking-schema pattern);
- `schemas/shared_defs.schema.yaml`;
- `tests/test_governance_schemas.py` (schema/example/boundary contract).

## Decision recorded

The seam is a **validation schema in the governance core**, not a runtime
table. Schemas are explicitly part of the governance core; a physical table and
read path, if built, belong to `pantheon-mvp` and would conform to this
contract.

Added:

- `schemas/project_claim.schema.yaml` — a `project_claim` carries `claim_id`,
  `project_id`, `claim_type`, `value`, `backing_card_ref` (card family + id),
  `provenance`, lifecycle `status`
  (`asserted → source_backed → verified → contested → retired`), `observed_at`
  and an optimistic `revision`;
- `schemas/examples/project_claim.example.yaml` — a fictional Zone PLU claim
  citing a published Knowledge card;
- registration in `tests/test_governance_schemas.py` (`SCHEMA_TO_EXAMPLE`) and
  `schemas/README.md`;
- a validation-seam section (§6) in `PROJECT_CARD_DECK_COMPOSITION.md`.

## Non-equivalences recorded

```text
schema present != table exists
claim validates != claim approved
source_backed != verified != opposable
displayed value != backing-card authority
retirement != deletion of the backing card
```

## Classification

```text
authority class: implemented validation baseline (schema)
repository state: implemented (validation contract) — no runtime, no table
runtime state: unchanged
protected paths touched: none
schema or test change: schema added + registered; example added; test map extended
installation or activation: none
```

The schema declares `x-boundary` with `runtime_execution`, `provider_routing`,
`memory_promotion`, `evidence_admission`, `automatic_ingestion` and
`system_of_record_mutation` all false. `tests/test_governance_schemas.py`
passes (5/5): the example validates and the boundary markers are present.

## Non-effects

This intervention creates no:

- PostgreSQL table, migration or query runtime;
- Agency Data API or write adapter;
- ingestion, extraction or OCR runtime;
- Evidence admission;
- Cockpit component or Hermes Skill;
- external action.
