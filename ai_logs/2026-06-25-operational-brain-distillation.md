# AI log — operational Brain / second-brain distillation

Date: 2026-06-25
Actor: ChatGPT
Scope: governance coordination, memory/probatoire track

## Source

User-provided field note describing a Markdown external "Brain" for Hermes Agent company use:

```text
native memory keeps stable facts;
external Brain keeps living company context;
timeline, clients, calls, projects, proposals, concepts, ai_drafts and indexes make context navigable;
progressive retrieval avoids reading everything;
AI drafts must not be confused with reliable sources.
```

## Canon read before action

Read active repository sources:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MEMORY.md`
- `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md`

Checked related GitHub coordination:

- #68 — Evidence / Memory canonicalization note
- #90 — Registre Probatoire vocabulary sweep / backlog sequencing
- #41 — prefer PRs and pause doctrine sprawl
- open PR list, no active open PR found specifically for operational Brain / second-brain memory.

Checked Notion Kanban:

- updated existing card `Evidence → Memory canonicalization note` rather than creating a new card.

## Decision

Decision Zeus: À vérifier.
Repo state: documented non-implemented.

## Accepted

- The distinction is valid: runtime memory can recall stable facts, but company work needs a navigable operational context corpus.
- The useful abstraction is retrieval over typed sources, chronology, decisions, proposals, drafts and follow-ups, not simply "more memory".
- A timeline is useful when treated as chronological/probative context, not proof by itself.
- Explicit separation between raw sources, derived notes, AI drafts, candidates, validated decisions and rejected positions strengthens the Registre Probatoire posture.
- Progressive retrieval matches the existing discipline: first scope, then search, then rank, then compose evidence.

## Refused

- No "Brain" as Pantheon memory engine.
- No Markdown folder, timeline, tag or index as source of truth by itself.
- No automatic promotion from runtime memory, AI draft, call note, proposal note or timeline entry to Registre Probatoire entry.
- No unscoped global vector index across project material.
- No confusion between an operational note and a validated professional position.

## To verify

- Whether the new `Operational context corpus` section should remain in `KNOWLEDGE_INGESTION_AND_MEMORY.md` or later move into an architecture-domain workflow example.
- Whether the cockpit should display this as Context Pack / Source Pack / Register Candidate review rather than as "memory".
- How practical folders such as `timeline/`, `clients/`, `calls/`, `projects/`, `proposals/`, `ai_drafts/` map to existing Pantheon objects without creating a parallel authority model.

## To arbitrate

- Whether the architecture domain pack needs a worked agency example showing project timeline + correspondence + devis + AI draft + validated response.
- Whether this belongs in the candidate memory track (#68), the architecture target workflows track, or a future external-runtime adapter note.

## Distilled rule

```text
Runtime memory recalls.
The operational context corpus retrieves.
Sources support.
Candidates propose.
Pantheon qualifies status.
The Registre Probatoire alone carries governed reliance.
The human validates.
```

## Repository changes made on PR branch

Branch:

```text
chatgpt/operational-brain-distillation-20260625
```

PR:

```text
#217 — docs(ai-log): record operational Brain distillation
```

Files changed:

- `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md`
  - added section `Operational context corpus`;
  - classifies external Brain / second-brain patterns as retrieval and orientation layer;
  - refuses folder, tag, timeline, AI draft or runtime recall as authority;
  - adds minimum metadata, separations, example timeline entry and progressive retrieval modes.
- `ai_logs/2026-06-25-operational-brain-distillation.md`
  - records this intervention.

## External updates made

- Added a follow-up comment to GitHub issue #68.
- Updated the Notion Kanban card `Evidence → Memory canonicalization note` with the 2026-06-25 review, next action and placement question.

## Boundary

This intervention is documentation only.
It does not add schema, database, vector index, runtime, connector, scheduler, approval engine, cockpit feature, folder creation, Hermes skill or automatic memory promotion.
