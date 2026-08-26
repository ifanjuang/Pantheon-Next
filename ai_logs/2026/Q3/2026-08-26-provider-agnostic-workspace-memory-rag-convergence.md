# Provider-agnostic workspace, memory and RAG convergence — 2026-08-26

Related: #666

## Objective

Remove accidental Pantheon ownership of workspace, RAG/retrieval and runtime-memory product choices while preserving the external composition already demonstrated to work.

## Observed repository facts

- `catalog/bindings/external-runtime-memory-unbound.yaml` already keeps `external_runtime_memory` unbound and does not adopt/install/activate a dependency.
- Hermes upstream currently provides native bounded `MEMORY.md` / `USER.md`, session history/search and project/context-file facilities.
- Pantheon-Next qualification work has demonstrated an Obsidian/Markdown + Self-hosted LiveSync/CouchDB + filesystem mirror + `hindsight-obsidian-sync` + Hindsight + Hermes path.
- Regression coverage protects the qualified long-running LiveSync daemon topology and its authority boundaries.
- The co-located `implementation/mvp_vertical/store.py` candidate already demonstrates scope-first local/NAS ingestion and retrieval with source/contract/ingestion provenance using Docling/direct text, PostgreSQL chunks and pgvector ranking.
- OpenWebUI and Paperless were already removed/refused as target architecture dependencies in preceding #666 convergence slices.

## Interpretation

The working Obsidian/Hindsight composition should not be erased or downgraded to an unqualified example. It is the strongest demonstrated external workspace/retrieval recommendation currently in the repository.

That recommendation is nevertheless not a Pantheon prerequisite. A user may legitimately use Hermes-native context/files/memory only, or select another compatible workspace/retrieval/memory implementation, without changing Pantheon governance authority.

Likewise, the co-located PostgreSQL/pgvector document retrieval path is current tested implementation, not a universal architecture requirement.

## Convergence decision

Use the following hierarchy:

```text
Pantheon architecture
  requires governance boundaries and invariants, not product names

Hermes-native context/files/memory
  valid zero-extra-provider baseline

Obsidian + LiveSync + Hindsight
  qualified and recommended external reference composition
  preferred recommendation when its additional workspace/retrieval capabilities are wanted

other providers
  replaceable alternatives selected only for demonstrated needs
```

RAG remains provider-agnostic. Direct bounded source access is valid when sufficient. Retrieval implementation must preserve source identity, bounded scope and provenance; retrieval success does not create Evidence or authorization.

## Preserved qualification details

The reference profile retains the demonstrated topology:

```text
native Obsidian clients
-> Self-hosted LiveSync
-> CouchDB synchronization state
-> one long-running Self-hosted LiveSync CLI daemon
-> dedicated local LiveSync DB
-> dedicated filesystem vault mirror
-> designated hindsight-obsidian-sync producer
-> Hindsight
-> bounded Hermes consumer
```

The rejected repeated one-shot `sync` + `mirror` topology remains recorded as rejected because it left stale rename state in qualification.

The reference also preserves:

```text
external_runtime_memory.preferred_binding = unbound
synchronization qualified != Hindsight ingestion authorized
filesystem materialized != Evidence
vault path != governed identity
memory != Evidence
retrieved != truth
```

## Files converged

- `docs/governance/TARGET_ARCHITECTURE.md`
- `docs/governance/ARCHITECTURE.md`
- `docs/governance/CORE_CONCEPTS_MAP.md`
- `docs/governance/MEMORY.md`
- `docs/governance/HERMES_CAPABILITY_BINDINGS.md`
- `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`
- `docs/governance/RAG_INGESTION_PIPELINE.md`
- `docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`
- `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`
- `.github/scripts/truncation_ack.txt`

## Explicit non-decisions

- No Obsidian, Hindsight, LiveSync, CouchDB, vector-store or external-memory provider is adopted by Pantheon through this slice.
- No runtime configuration or production activation is changed.
- No qualification evidence is promoted into Evidence or authorization.
- Paperless implementation removal is not performed in this slice; it remains a separate protected-path convergence task.
- Historical `ai_logs/` are not rewritten.

## Remaining uncertainty

The qualified Obsidian/Hindsight reference still has deployment-specific security/operational hardening work tracked by its existing qualification issues. Those gaps apply only when that optional stack is selected; they do not block a Hermes-native deployment.

CI and repository guards remain required before merge.