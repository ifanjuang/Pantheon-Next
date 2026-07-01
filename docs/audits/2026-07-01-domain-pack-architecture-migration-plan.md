# Migration plan — architecture domain pack (B-4, table before move)

Status: validation-only / migration plan — to approve before any move. Delivers the
old→new path table so no reference breaks silently. It moves nothing; the actual
`git mv` + reference sweep is a separate PR run only after this table is approved.

Date: 2026-07-01.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Decision (B-4)

`docs/governance/` = generic rules; `docs/domain-packs/architecture/` = the first deep
professional method pack. The 24 `ARCHITECTURE_*` documents move into the pack. Generic
rules (`DOMAIN_PACK_SPEC.md`, `CAPABILITY_PLACEMENT.md`, `METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`,
`METHOD_CARD_MODEL.md`) are **not** `ARCHITECTURE_*`-prefixed and **stay** in `docs/governance/`.

One choice for you: **drop the `ARCHITECTURE_` prefix** in the pack (recommended —
the folder already namespaces it) or keep it. The table below drops it.

## Scope of the reference sweep

Moving these files touches **94 live reference locations** (matching lines) across
`docs/` and `README.md`; `ai_logs/` are history and are left as-is. The counts below are
reference **locations** (matching lines), not referring files, so the follow-up sweep can
use them as acceptance criteria and rewrite every occurrence — including multiple
references in one file. `AUTHORITY_INDEX.md` grouped-row coverage and the CI internal-link
check must stay green, so the move PR rewrites every live reference in the same commit.

## Old → new path table (prefix dropped)

| Old path | New path | Live ref locations |
|---|---|---|
| `docs/governance/ARCHITECTURE_AGENCY_DOMAIN_PACK.md` | `docs/domain-packs/architecture/AGENCY_DOMAIN_PACK.md` | 15 |
| `docs/governance/ARCHITECTURE_DOCUMENT_REVIEW.md` | `docs/domain-packs/architecture/DOCUMENT_REVIEW.md` | 6 |
| `docs/governance/ARCHITECTURE_FINANCIAL_LOT_INSURANCE_REVIEW.md` | `docs/domain-packs/architecture/FINANCIAL_LOT_INSURANCE_REVIEW.md` | 0 |
| `docs/governance/ARCHITECTURE_INDEX_EFFECT_MATRIX.md` | `docs/domain-packs/architecture/INDEX_EFFECT_MATRIX.md` | 5 |
| `docs/governance/ARCHITECTURE_KNOWLEDGE_REGISTRY_BLUEPRINT.md` | `docs/domain-packs/architecture/KNOWLEDGE_REGISTRY_BLUEPRINT.md` | 2 |
| `docs/governance/ARCHITECTURE_MATERIAL_CHOICE_REFLEX.md` | `docs/domain-packs/architecture/MATERIAL_CHOICE_REFLEX.md` | 0 |
| `docs/governance/ARCHITECTURE_METHOD_DECK.md` | `docs/domain-packs/architecture/METHOD_DECK.md` | 4 |
| `docs/governance/ARCHITECTURE_METHOD_RUN_TESTS.md` | `docs/domain-packs/architecture/METHOD_RUN_TESTS.md` | 1 |
| `docs/governance/ARCHITECTURE_METHOD_TAXONOMY.md` | `docs/domain-packs/architecture/METHOD_TAXONOMY.md` | 8 |
| `docs/governance/ARCHITECTURE_MISSION_RESPONSIBILITY_BOUNDARY_REFLEX.md` | `docs/domain-packs/architecture/MISSION_RESPONSIBILITY_BOUNDARY_REFLEX.md` | 1 |
| `docs/governance/ARCHITECTURE_OS_RECONCILIATION.md` | `docs/domain-packs/architecture/OS_RECONCILIATION.md` | 4 |
| `docs/governance/ARCHITECTURE_PROBATIVE_INSTRUCTION.md` | `docs/domain-packs/architecture/PROBATIVE_INSTRUCTION.md` | 1 |
| `docs/governance/ARCHITECTURE_PROJECT_OBJECT_MODEL.md` | `docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md` | 2 |
| `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING.md` | `docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md` | 5 |
| `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md` | `docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md` | 3 |
| `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md` | `docs/domain-packs/architecture/PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md` | 3 |
| `docs/governance/ARCHITECTURE_PROOF_REGISTER.md` | `docs/domain-packs/architecture/PROOF_REGISTER.md` | 10 |
| `docs/governance/ARCHITECTURE_PROOF_REGISTER_IMPLEMENTATION_SPEC.md` | `docs/domain-packs/architecture/PROOF_REGISTER_IMPLEMENTATION_SPEC.md` | 3 |
| `docs/governance/ARCHITECTURE_REFLEX_OPERATING_MODEL.md` | `docs/domain-packs/architecture/REFLEX_OPERATING_MODEL.md` | 1 |
| `docs/governance/ARCHITECTURE_ROLE_ACTIVATION_MODEL.md` | `docs/domain-packs/architecture/ROLE_ACTIVATION_MODEL.md` | 6 |
| `docs/governance/ARCHITECTURE_ROLE_FACETS.md` | `docs/domain-packs/architecture/ROLE_FACETS.md` | 4 |
| `docs/governance/ARCHITECTURE_ROLE_REFLEX_COORDINATION.md` | `docs/domain-packs/architecture/ROLE_REFLEX_COORDINATION.md` | 6 |
| `docs/governance/ARCHITECTURE_SOURCE_POLICY.md` | `docs/domain-packs/architecture/SOURCE_POLICY.md` | 1 |
| `docs/governance/ARCHITECTURE_TARGET_WORKFLOWS.md` | `docs/domain-packs/architecture/TARGET_WORKFLOWS.md` | 3 |

Two files (`ARCHITECTURE_FINANCIAL_LOT_INSURANCE_REVIEW.md`, `ARCHITECTURE_MATERIAL_CHOICE_REFLEX.md`)
have zero live references today; they still move, but no reference rewrite is needed for them.

## Not done here

No file is moved and no reference is rewritten in this PR. On approval, a follow-up PR
runs `git mv` for the 24 files, creates `docs/domain-packs/architecture/`, rewrites the
94 live reference locations, updates the `AUTHORITY_INDEX.md` rows and index coverage, and
keeps CI green. Generic rules stay in `docs/governance/`.

## Boundary

Plan only. Moves nothing, promotes nothing, changes no schema, test, `mcp-server/` or
runtime. The move is a separate, reviewable, reference-complete PR.
