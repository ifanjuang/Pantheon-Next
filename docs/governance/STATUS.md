# Pantheon Next Status

Status: canonical — primary repository posture and active document index.

Status date: 2026-08-27

Pantheon Next is the canonical governance repository and monorepo host for bounded candidate implementation surfaces. Repository presence, executable code and green CI do not establish installation, adoption, authorization, professional validation or Evidence.

## Doctrine

```text
Hermes Web/dashboard exposes chat, sessions and runtime controls.
Hermes Agent executes externally.
Pantheon Next governs consequential state, Evidence, decisions and professional status.
Pantheon Cockpit projects governed Cards, navigation, decisions and status.
```

The Cockpit is not a second general-purpose chat frontend. Hermes clients are optional and replaceable; they do not become Pantheon structural dependencies or governance authorities.

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder/path != governed identity
provider selected != authority transfer
source capture != Evidence
green CI != adoption
```

## Current repository posture

Status: partial but structurally coherent.

The repository contains:

- canonical governance doctrine, authority indexes, contracts, schemas and tests;
- `mcp-server/`, a bounded read-only policy/verification service with local MCP and authenticated HTTP projections;
- `implementation/`, the co-located executable candidate implementation imported from the former `ifanjuang/pantheon-mvp` repository at cutoff `d960862dd0e23b7003a0f3e4ee0ea630ffc12af9`;
- PostgreSQL/pgvector, document-processing bindings such as Docling, generic Source intake and local/NAS paths where selected by implementation;
- an executable candidate Pantheon Cockpit with registry-backed navigation and Card projections;
- declarative Hermes templates and seams while Hermes runtime execution remains external;
- historical `ai_logs/`, reviews and audits as provenance rather than current doctrine.

The former `pantheon-mvp` repository and its PR/commit identifiers remain historical provenance only. Current implementation ownership is monorepo-native under `implementation/`.

## Active architecture split

```text
Pantheon governance core -> canonical governance rules, authority and contracts
mcp-server/              -> bounded read-only policy / verification projection
implementation/          -> bounded executable candidate implementation
Hermes Agent             -> external runtime / execution
Hermes Web/dashboard     -> selected chat / sessions / runtime interaction baseline
Pantheon Cockpit         -> governed projections / Cards / navigation / decisions / status
Obsidian/Markdown        -> optional human-authored workspace
Hindsight                -> optional derived memory / retrieval
professional sources     -> Source / Document identity and provenance owners
```

OpenWebUI and Paperless-ngx are refused/retired target integrations. Historical references may remain only where they carry provenance or are still being removed through an incoming-link audit; they carry no current target responsibility.

Docling, PostgreSQL, pgvector, Hindsight, Obsidian and individual clients are bindings or optional components, not universal architectural authorities.

## Runtime-status honesty

`WHAT_RUNS.md` is the support map for implementation, external runtime observations, target selection and adoption status. It does not replace authority indexes.

Current relevant classifications:

```text
mcp-server/                 = implemented read-only / partial
implementation/             = executable candidate / co-located / not adopted
Pantheon Cockpit            = executable candidate / tested / not adopted
Hermes Agent                = external execution runtime
Hermes Web/dashboard        = selected interaction baseline
OpenWebUI                   = refused / no target role
Paperless-ngx               = retired / no target role
```

The `pantheon-policy-api` projects the same bounded policy service over authenticated internal HTTP for deterministic preflight. It does not execute, approve, send, schedule, install, update, route providers or promote memory.

The `pantheon-modules` Hermes dashboard-plugin template may produce operational observations after separate installation and activation. Pantheon qualifies observations; it does not become a second runtime inventory producer.

## Active candidate / to-verify clusters

The following remain active review areas; their existence does not imply adoption:

- `ANSWER_VERIFICATION_GATE.md` — candidate answer-verification doctrine;
- `DECISION_SURFACE_SPEC.md`, `SPICE_REFERENCE_DISTILLATION.md` — candidate/reference decision-surface work;
- `DATA_PLATFORM_ARCHITECTURE.md` — data-platform boundary review;
- `DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md`, `DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`, `RAG_INGESTION_PIPELINE.md`, `REPOSITORY_PLACEMENT.md` — co-located document/Knowledge implementation posture;
- `AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md`, `WORKFLOW_LIFECYCLE.md` — candidate doctrine;
- `PROOF_REGISTER.md` and related specifications — candidate proof-register slice;
- `DOCUMENT_INTELLIGENCE.md`, `REVIEW_QUEUE.md`, `URGENT_REVIEW_TRIAGE.md`, `RAW_DERIVED_GOVERNED_RECORDS.md`, `EXTERNAL_TOOL_PLACEMENT_REGISTER.md` — candidate governed document/review model;
- `MCP_PANTHEON_MINIMAL_PROFILE.md`, `mcp-server/`, `mcp-server/docs/HTTP_API_CONTRACT.md`, `Dockerfile.policy-api`, `compose.policy-api.yaml` — implemented read-only / partial / protected path;
- `schemas/architecture-proof-register/*` — proposal pending baseline alignment.

## Repository read path

Use these owners instead of duplicating their contents here:

- `README.md` — repository entry point;
- `docs/governance/README.md` — governance entry point;
- `AUTHORITY_INDEX.md` — authority and status;
- `MODULES.md` — governance module map;
- `WHAT_RUNS.md` — runtime-status honesty;
- `CONTRIBUTING.md` — contribution and protected-path discipline.

```text
If STATUS and an index disagree on existence, the index wins.
If they disagree on authority, AUTHORITY_INDEX wins.
If WHAT_RUNS and a module disagree on runtime availability, treat the item as partial / to verify until reconciled.
```

## Historical provenance

One-shot reconciliation documents removed during earlier cleanup remain available through Git history and their `ai_logs/` mappings. Historical records may describe architectures that were valid at the time; they must not be read as current target architecture.

Do not rewrite old `ai_logs/` merely because the target architecture changed.

## Boundary reminder

Pantheon does not contain a general-purpose agent runtime, second generic chat frontend, automatic approval engine, automatic durable-memory promotion engine, provider router, unrestricted connector gateway or mandatory DMS product.

```text
Pantheon defines and governs the kernel.
Bounded implementation carries candidate behavior.
Hermes carries external execution where separately activated.
The human decides where consequence requires authority.
Validated output remains reviewable; it does not self-promote.
```
