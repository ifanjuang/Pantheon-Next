# Close current-authority coverage baseline

Date: 2026-08-29
Issue: #787
PR: #840
Base `main`: `e6f8fd854aea8f594806f73f8e4b22768219a9b0`

## Objective

Close the staged current-authority coverage debt introduced by #825 without creating another authority map, allowlist or documentation hierarchy.

Every governance Markdown path whose `Status:` begins with `canonical` or `active` must be explicitly discoverable through the already registered Authority Index corpus.

## Current-main diagnostic

The strict existing coverage checker was run against the exact current base before owner placement. It reported 30 current-authority paths outside the effective Authority Index.

The diagnostic was treated as an owner-test backlog, not as an instruction to index mechanically.

## Owner-test result

All 30 paths were re-read against current `main` and compared with their neighboring/current owners after the convergence already merged through #829, #833, #834 and #838.

No remaining path was demonstrated to be a duplicate current authority. Each retained path still owns a distinct responsibility in one of these bounded families:

- architecture, product positioning, concept/ecosystem navigation, visual/editorial language and runtime-status description;
- governed Card/Information projection and bounded Context Packs;
- Role identity, Role participation, Role Signals, Governance College tension/arbitration and Doctor audit;
- common records, scope isolation and explicit Information relations;
- Source intake, Source need/routes/freshness and Knowledge taxonomy;
- retrieval-to-Evidence interpretation, Evidence topology and external runtime-memory adapter boundaries;
- execution discipline, concrete external-tool placement decisions, GitHub repository safeguards, roadmap sequencing and Workflow Manifest governance.

The retained set is:

```text
AGENTS.md
ARCHITECTURE.md
CARD_PROJECTION_DEFINITION_MODEL.md
CONTEXT_PACKS.md
CORE_CONCEPTS_MAP.md
CORE_RECORDS_MODEL.md
DOCTOR_MODULE_SPEC.md
ECOSYSTEM_MAP.md
EDITORIAL_LANGUAGE.md
ENTITY_RELATION.md
EVIDENCE_TOPOLOGY.md
EXECUTION_DISCIPLINE.md
EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md
EXTERNAL_TOOL_PLACEMENT_REGISTER.md
GITHUB_REPOSITORY_GOVERNANCE.md
GOVERNANCE_COLLEGE.md
INFORMATION_CARD_PROJECTION.md
KNOWLEDGE_TAXONOMY.md
PRODUCT_DIFFERENTIATION.md
RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md
ROADMAP.md
ROLE_ACTIVATION.md
ROLE_SIGNALS.md
RUN_GRAPH.md
SCOPE_ISOLATION.md
SOURCE_INTAKE_ADMISSION.md
SOURCE_NEED_AND_REGISTRY.md
VISUAL_LANGUAGE.md
WHAT_RUNS.md
WORKFLOW_SCHEMA.md
```

## Placement decision

- 28 governance/kernel, navigation, projection, source, Evidence, Role and repository owners are placed in the existing `authority/GOVERNANCE_AUTHORITY_INDEX.md`.
- `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` and `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` are placed in the existing `authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.
- no new sub-index is created;
- index placement does not promote or broaden any document's authority;
- candidate/missing-path historical baseline behavior remains unchanged.

## Permanent guard

The existing `.github/scripts/check_index_coverage.py` is tightened so a `canonical*` or `active*` governance document can no longer remain outside the registered Authority Index through baseline grandfathering.

`CONTRIBUTING.md` uses the same `canonical*` / `active*` owner-test boundary for future governance Markdown.

```text
indexed != promoted
indexed != necessary owner
existing owner first
new current-authority Markdown = exceptional
```

## MCP consumer alignment

After `ARCHITECTURE.md` became explicitly indexed, one MCP consultation test still encoded the former transitional state by expecting that source to report `authority: not indexed`.

`mcp-server/tests/test_consultation.py` is updated only to assert the new real state (`active doctrine`) while continuing to verify that the file's own declared `Status:` and content digest are exposed. The authority resolver's separate tests continue to cover missing/unregistered paths explicitly.

No MCP production code or consultation behavior is changed. The test update is a consumer-alignment change required by the authority-map correction.

## Preserved boundaries

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
PDP decision != PEP execution
folder/dossier != governed identity
```

## Net effect

```text
current-authority coverage debt before this PR: 30
retained after current owner test:              30
explicitly indexed by existing maps:            30
new governance owners:                           0
new authority indexes:                           0
allowlists:                                       0
```

This is the closure slice for current-authority discoverability. It does not claim that candidate-document convergence is complete; #787 closure still requires final criterion review after exact-head CI and merge verification.
