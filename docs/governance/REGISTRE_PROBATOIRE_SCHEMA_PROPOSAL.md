# Registre Probatoire — schema rename proposal (E6)

Status: validation-only proposal — protected-path change. Requires explicit approval before any edit under `schemas/` or `tests/`.

This note specifies the sixth downstream step (E6) of the Registre Probatoire direction (see `REGISTRE_PROBATOIRE_DIRECTION.md`, `GLOSSARY.md`). It proposes renaming the `memory_candidate` schema to `register_candidate` and aligning its fields to the Registre Probatoire.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

This document does not modify any protected path. It changes no file under `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml`, Docker or `.env`. It only specifies, for review, the change to apply once approved. The proposed schema below is a proposal printed inside a governance note; it is not an executable schema file.

## Why

After E1–E3 and E5, the governance prose uses `Register Candidate` and `Registre Probatoire entry`, and certainty uses the `E0–E4` axis owned by `GLOSSARY.md`. The schema baseline still carries the old name (`memory_candidate`) and a three-level `confidence` field. E6 aligns the schema so the machine-checkable contract matches the doctrine.

## Files affected (apply only after approval)

```text
RENAME  schemas/memory_candidate.schema.yaml        -> schemas/register_candidate.schema.yaml
RENAME  schemas/examples/memory_candidate.example.yaml -> schemas/examples/register_candidate.example.yaml
EDIT    tests/test_governance_schemas.py   line ~22  (schema -> example mapping key)
EDIT    tests/test_schema_examples.py       line ~15  (example/schema pair)
EDIT    schemas/README.md                   line ~18  (listing)
```

## Field mapping

```text
KEEP (unchanged):
  candidate_id, created_at, proposed_by, claim, scope, source,
  evidence_link, evidence_pack_id, risk, proposed_durability,
  required_approval (C0–C5 — already correct), status, reviewer,
  reviewed_at, supersedes_candidate_id, governance_refs, x-boundary

RENAME:
  confidence (low|medium|high)  ->  certainty (E0|E1|E2|E3|E4)   [GLOSSARY axis]

ADD (optional — Registre Probatoire provenance: exhibits, dates, citation):
  source_date, received_date, effective_date   (dates)
  author_detected, page_or_location, origin_channel, source_excerpt  (citation)
  linked_files                                  (exhibits / pièces)

DEPRECATE (keep as aliases during migration, then drop in a later step):
  content (alias of claim)        -> already deprecated
  validation_state (alias status) -> already deprecated
  confidence                      -> mark deprecated, superseded by certainty

GOVERNANCE_REFS default — add:
  docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md
  docs/governance/GLOSSARY.md
```

## Proposed schema (for approval)

The schema stays governance-only. It must not enable runtime, scheduler, queue, provider routing or memory promotion; the x-boundary block keeps every such flag false.

```yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: Pantheon Next Register Candidate
description: >-
  Governance schema for a proposed Registre Probatoire entry awaiting scoped
  review, evidence and approval. Formerly "memory_candidate".
type: object
required:
  - candidate_id
  - created_at
  - proposed_by
  - claim
  - scope
  - source
  - evidence_link
  - risk
  - proposed_durability
  - required_approval
  - status
properties:
  candidate_id: { type: string, pattern: "^[a-z0-9._-]+$" }
  created_at: { type: string, format: date-time }
  proposed_by: { type: string }
  claim: { type: string, minLength: 10 }
  content:
    type: string
    deprecated: true
    description: Legacy alias for claim. Prefer claim.
  scope:
    type: object
    required: [scope_type, scope_id]
    properties:
      scope_type:
        type: string
        enum: [session, task, dossier, project, domain, user, organization, repository, governance, system]
      scope_id: { type: string, minLength: 1 }
      scope_label: { type: string }
    additionalProperties: false
  source: { type: string, minLength: 1 }
  evidence_link: { type: string, minLength: 1 }
  evidence_pack_id: { type: string, pattern: "^[a-z0-9._-]+$" }
  certainty:
    type: string
    description: Probative certainty axis owned by GLOSSARY.md.
    enum: [E0, E1, E2, E3, E4]
    default: E1
  confidence:
    type: string
    deprecated: true
    description: Superseded by certainty (E0–E4).
    enum: [low, medium, high]
  source_date: { type: [string, "null"], format: date }
  received_date: { type: [string, "null"], format: date }
  effective_date: { type: [string, "null"], format: date }
  author_detected: { type: [string, "null"] }
  page_or_location: { type: [string, "null"] }
  origin_channel: { type: [string, "null"] }
  source_excerpt: { type: [string, "null"] }
  linked_files:
    type: array
    items: { type: string }
    default: []
  risk:
    type: object
    required: [level, notes]
    properties:
      level: { type: string, enum: [low, medium, high, critical] }
      notes: { type: string }
    additionalProperties: false
  proposed_durability:
    type: string
    enum: [session_only, task, dossier, project, domain, user, organization, repository, governance, system]
  required_approval:
    type: string
    enum: [C0, C1, C2, C3, C4, C5]
  status:
    type: string
    enum: [candidate, under_review, approved, rejected, deferred, superseded, revoked, archived]
  validation_state:
    type: string
    deprecated: true
    enum: [candidate, under_review, approved, rejected, deferred, superseded, revoked, archived]
  reviewer: { type: [string, "null"] }
  reviewed_at: { type: [string, "null"], format: date-time }
  supersedes_candidate_id: { type: [string, "null"] }
  governance_refs:
    type: array
    items: { type: string }
    default:
      - docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md
      - docs/governance/GLOSSARY.md
      - docs/governance/MEMORY.md
      - docs/governance/EVIDENCE_PACK.md
      - docs/governance/SCOPE_ISOLATION.md
additionalProperties: false
x-boundary:
  runtime_execution: false
  autonomous_loop: false
  provider_routing: false
  scheduler: false
  queue_system: false
  memory_promotion: false
  automatic_canonization: false
```

## Proposed example (for approval)

```yaml
candidate_id: example.register-candidate
created_at: "2026-06-08T10:00:00Z"
proposed_by: HEPHAISTOS
claim: Pantheon schema files are validation contracts only, not runtime components.
scope:
  scope_type: repository
  scope_id: pantheon-next
  scope_label: Pantheon Next repository
source: docs/governance/STATUS.md
evidence_link: example.evidence-pack
evidence_pack_id: example.evidence-pack
certainty: E2
source_date: "2026-06-01"
received_date: "2026-06-01"
author_detected: null
origin_channel: repository
source_excerpt: "Pantheon Next is a governance-first repository."
linked_files: []
risk:
  level: low
  notes: The claim repeats active repository doctrine but still remains a candidate in this example.
proposed_durability: repository
required_approval: C3
status: candidate
reviewer: null
reviewed_at: null
supersedes_candidate_id: null
governance_refs:
  - docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md
  - docs/governance/GLOSSARY.md
  - docs/governance/MEMORY.md
  - docs/governance/EVIDENCE_PACK.md
  - docs/governance/SCOPE_ISOLATION.md
```

## Migration approach

```text
Option A (clean rename, recommended):
  rename both files, update the two tests and the README, add a CHANGELOG entry.
  External references to "memory_candidate" are internal only (tests + README),
  so a clean rename is safe.

Option B (rename with deprecated alias):
  add register_candidate as canonical and keep a thin memory_candidate alias
  schema for one cycle, then drop it. Heavier; only if an external consumer
  depends on the old filename.
```

Recommended: Option A.

## Approval checklist

```text
[ ] confirm certainty replaces confidence (E0–E4 vs low/medium/high)
[ ] confirm the added provenance fields (dates, citation, exhibits) are wanted in v1
[ ] confirm Option A (clean rename) vs Option B (alias)
[ ] authorize the protected-path edits under schemas/ and tests/
[ ] after approval: apply rename + field changes, update the two tests and README,
    run the schema tests, add a CHANGELOG entry and an ai_logs trace
```

## Current repo state

Documented non-implemented. No protected path changed. The rename is applied only after explicit approval of this proposal.
