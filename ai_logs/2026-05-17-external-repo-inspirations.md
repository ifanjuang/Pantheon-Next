# AI Log — External repository inspiration map

Date: 2026-05-17

## Scope

Created a governance support document mapping external open-source repositories that may inspire Pantheon Next design.

The work distills patterns from existing projects without adopting them as dependencies, integrations or runtime components.

## Files changed

- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`
- `docs/governance/README.md`
- `docs/governance/STATUS.md`
- `CHANGELOG.md`
- `ai_logs/2026-05-17-external-repo-inspirations.md`

## Why

Issue #12 accumulated several architecture notes about governed OpenWebUI Knowledge handoff, scoped retrieval, optional Postgres optimization, modularity and external inspiration.

The user asked to look for existing repositories for inspiration.

The goal was to preserve the research in a concise canonical support document while preventing dependency drift.

## External repositories reviewed as inspiration

The document maps patterns from:

- `infiniflow/ragflow`;
- `onyx-dot-app/onyx`;
- `Mintplex-Labs/anything-llm`;
- `khoj-ai/khoj`;
- `langgenius/dify`;
- `FlowiseAI/Flowise`;
- `Permify/permify`;
- `ory/keto`;
- `apache/casbin`;
- `terminusdb/terminusdb`;
- `dolthub/dolt`;
- `guardrails-ai/guardrails`;
- `open-policy-agent/opa`.

## Distillation rule

The document reinforces that Pantheon Next should distill patterns, not copy platforms.

Stable chain:

```text
Raw Source
→ Source Reference
→ Retrieved Knowledge
→ Working Context
→ Evidence Candidate
→ Evidence Item
→ Evidence Pack
→ Output Candidate
→ Approval Event
→ Memory Candidate
→ Canonical Memory
```

## Changes

Added `EXTERNAL_REPO_INSPIRATIONS.md` with:

- repository inspiration map;
- useful patterns;
- Pantheon distillation notes;
- risks and anti-patterns;
- mapping to Pantheon concerns;
- MVP versus optional advanced path;
- external adoption decision rule;
- explicit non-implementation status.

Updated `docs/governance/README.md` to register the file as inspiration/support doctrine.

Updated `docs/governance/STATUS.md` to classify the inspiration map as documentation-level support doctrine and explicitly mark external dependencies as not implemented.

Updated `CHANGELOG.md` under `0.1.3 - 2026-05-17`.

## Boundary check

This intervention is documentation-only.

It does not implement:

- external repository dependency;
- RAG platform integration;
- enterprise search integration;
- OpenWebUI plugin;
- Hermes tool;
- knowledge gateway;
- authorization service;
- workflow runtime;
- provider router;
- versioned database;
- validation library;
- scheduler;
- queue;
- automatic memory promotion.

External repositories remain inspiration only until a separate governed adoption decision exists.

## Status

Implemented as support doctrine.

Implementation not started.
