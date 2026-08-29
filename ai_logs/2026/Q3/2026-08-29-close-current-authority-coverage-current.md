# Close current-authority coverage baseline — current main

Date: 2026-08-29
Issue: #787
PR: #840
Base `main`: `e6f8fd854aea8f594806f73f8e4b22768219a9b0`
Branch: `codex/787-close-current-authority-baseline-current`
Supersedes stale work in: #832

## Objective

Finish the current-authority owner-coverage part of #787 by turning the staged Authority Index check into a strict invariant for every governance Markdown document whose `Status:` begins with `canonical` or `active`.

The change reuses the existing Authority Index, its registered sub-indexes and `.github/scripts/check_index_coverage.py`. It introduces no parallel registry, status taxonomy or checker.

## Diagnostic result on current main

The first strict Governance CI run on the current base found exactly 30 current-authority documents without deliberate Authority Index placement.

The earlier #787 audit had already tested these surfaces for distinct responsibility. Convergence PRs before this final slice removed or demoted the false-owner cases instead of indexing them mechanically, including the obsolete boundary, skill-lifecycle, Evidence anti-pattern and historical coordination surfaces handled by #829, #833, #834 and #838.

The strict current-base list therefore contains only retained owners.

Disposition:

```text
30 current-authority gaps
-> 28 governance-kernel placements
-> 2 runtime-adapter placements
-> 0 allowlist entries
-> 0 new authority owners
```

## Governance-kernel placements

The following already-current owners are made discoverable in `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`:

- `AGENTS.md` — canonical Pantheon Role registry;
- `ARCHITECTURE.md` — global system/layer placement;
- `CARD_PROJECTION_DEFINITION_MODEL.md` — governed projection-to-renderer mapping contract;
- `CONTEXT_PACKS.md` — governed bounded context bundle;
- `CORE_CONCEPTS_MAP.md` — concept-navigation and ownership map;
- `CORE_RECORDS_MODEL.md` — cross-domain common-record/scope model;
- `DOCTOR_MODULE_SPEC.md` — audit-only Doctor boundary;
- `ECOSYSTEM_MAP.md` — surrounding-system responsibility map;
- `EDITORIAL_LANGUAGE.md` — public editorial language;
- `ENTITY_RELATION.md` — canonical Information relation contract;
- `EVIDENCE_TOPOLOGY.md` — reviewable proof-chain topology;
- `EXECUTION_DISCIPLINE.md` — smallest-safe-path execution discipline;
- `GITHUB_REPOSITORY_GOVERNANCE.md` — repository safeguards;
- `GOVERNANCE_COLLEGE.md` — judgment/tension/arbitration structure;
- `INFORMATION_CARD_PROJECTION.md` — Information Card projection boundary;
- `KNOWLEDGE_TAXONOMY.md` — Source/Knowledge/Context/Evidence/Memory/Doctrine/Runtime State boundary;
- `PRODUCT_DIFFERENTIATION.md` — product-positioning owner;
- `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` — retrieval-to-Evidence interpretation boundary;
- `ROADMAP.md` — outcome roadmap subordinate to status authority;
- `ROLE_ACTIVATION.md` — Role/domain/skill participation and eligibility;
- `ROLE_SIGNALS.md` — structured non-executing Role signal contract;
- `RUN_GRAPH.md` — Run Trace View compatibility owner;
- `SCOPE_ISOLATION.md` — scope validity and non-propagation;
- `SOURCE_INTAKE_ADMISSION.md` — source identity/provenance admission boundary;
- `SOURCE_NEED_AND_REGISTRY.md` — source need/routes/registry/freshness;
- `VISUAL_LANGUAGE.md` — non-runtime visual/metaphor language;
- `WHAT_RUNS.md` — repository runtime-status honesty map;
- `WORKFLOW_SCHEMA.md` — Workflow Manifest compatibility owner.

## Runtime-adapter placements

The following already-current owners are made discoverable in `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`:

- `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` — generic external runtime-memory adapter boundary;
- `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` — lightweight register of concrete external-tool placement decisions.

These rows do not adopt, install, activate or authorize any external capability.

## Parallel-work check

Open PR #830 modifies `SOURCE_NEED_AND_REGISTRY.md` only by adding a workspace source-notebook specialization under that existing owner. It does not change the owner identity, status or Authority Index placement decision.

The placement in this slice is therefore compatible with that parallel work.

## Contribution rule

`CONTRIBUTING.md` is aligned with the checker population:

```text
canonical* or active*
```

A new current-authority Markdown document remains a last-resort decision. Contributors must first record which existing owners were checked, why a section/local delta/reference is insufficient, what distinct responsibility is proposed, what authority class is needed, and which Authority Index row makes the owner discoverable.

## Checker behavior

Current-authority coverage is strict:

```text
canonical* / active* current owner
-> indexed now
-> no GOVERNANCE_BASE_REF grandfathering
```

The historical baseline behavior remains unchanged for candidate and missing-path findings. This avoids converting #787 into an unrelated cleanup of candidate debt.

## Authority impact

```text
indexed != promoted
indexed != necessary owner
current authority -> discoverable owner placement
```

No authority class changes in this slice. The rows expose responsibilities already current before the PR.

## Runtime impact

None. The checker is read-only repository validation. The index and contribution changes are documentation only. No runtime, schema, scheduler, queue, provider router, approval engine, memory engine, persistence or external action is introduced.

## Preserved distinctions

```text
retrieved != truth
memory != Evidence
runtime output != Evidence
runtime success != authorization
projection != persistence
projection != approval
PDP decision != PEP execution
folder/dossier != governed identity
```

## Validation rule

Merge only after the exact final HEAD passes:

- Governance CI;
- Pantheon Architecture Audit;
- Obsolete Authority Consistency;

and after reviews, threads and comments have been inspected. A successful strict coverage run must show no remaining current-authority-not-indexed finding.
