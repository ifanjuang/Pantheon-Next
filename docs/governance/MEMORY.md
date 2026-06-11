# Memory

Status: active doctrine — reframed under the Registre Probatoire direction (see `GLOSSARY.md`, `REGISTRE_PROBATOIRE_DIRECTION.md`).

"Memory" belongs to Hermès, the execution runtime. Hermès keeps its own memory (mem0 or another system): free, self-evolving and ungoverned by Pantheon.

Pantheon governs no memory of its own. What Pantheon governs is the `Registre Probatoire` — the evidence register with certainty levels, exhibits (pièces), dates and citations. This document draws that boundary.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Bridge rule

Hermès memory may store, recall, rank, summarize and propose.

It carries no authority.

Only a Registre Probatoire entry may be cited or relied upon for a consequential decision. This is the Answer Verification Gate posture:

```text
Memory first. Evidence when consequential. Status when deciding. Approval when acting.
```

Pantheon never performs automatic memory promotion: nothing Hermès remembers becomes probative on its own.

## Purpose

Pantheon Next governs what may become durable, citeable evidence for future use.

It separates:

- knowledge that can be consulted;
- context that can be injected;
- Hermès observations that can be proposed;
- Register Candidates that can be reviewed;
- Registre Probatoire entries that have been approved.

This separation prevents accidental canonization.

## Core principle

No register entry is probative by default.

A model output is not a register entry.

A retrieved document is not a register entry.

An embedding match is not a register entry.

A repeated observation is not a register entry.

A high-confidence answer is not a register entry.

A useful result is not a register entry.

A register entry requires governance.

## Categories

Pantheon distinguishes the following categories.

```text
Knowledge
Context
Session State
Runtime State
Register Candidate
Registre Probatoire entry
```

These categories must not be merged.

## Knowledge

Knowledge is consultable material.

Examples:

- documents;
- repository files;
- external references;
- OpenWebUI Knowledge Base content;
- uploaded files;
- domain documentation;
- official documentation.

Knowledge can support reasoning.

Knowledge does not become a register entry automatically.

Knowledge may produce Register Candidates only through an Evidence Pack.

## Context

Context is information temporarily injected to support a task.

Examples:

- user-provided instructions;
- project context;
- role context;
- policy context;
- domain context;
- approved register excerpts.

Context is not automatically durable.

Context may be reused only if it is already a Registre Probatoire entry or if a new Register Candidate is approved.

## Session State

Session State is transient conversation or task-local information.

It may help complete the current interaction.

It must not be treated as a Registre Probatoire entry.

Session State can generate a Register Candidate when the information appears durable, useful and safe to retain.

## Runtime State

Runtime State belongs to Hermès, outside Pantheon Next.

Examples:

- Hermès memory;
- worker state;
- queue state;
- scheduler state;
- tool execution state;
- provider routing state;
- LangGraph state;
- agent scratchpad state;
- temporary execution cache.

Pantheon Next does not own Runtime State.

Runtime State must not become a Registre Probatoire entry.

Runtime State may be summarized as evidence only when it is relevant to review, audit or risk analysis.

## Register Candidate

A Register Candidate is a proposed Registre Probatoire entry. ("Memory Candidate" is the former name, retained where the corpus is not yet migrated.)

It is not probative.

It must remain explicitly marked as candidate until approved.

A Register Candidate should define:

```text
Claim
Scope
Source
Evidence link
Certainty (E0–E4)
Risk
Proposed durability
Required approval
Status
```

A Register Candidate may come from:

- user instruction;
- project pattern;
- repeated validated usage;
- Evidence Pack output;
- a Hermès observation;
- governance review;
- domain review.

A Register Candidate must not come directly from raw model confidence.

## Registre Probatoire entry

A Registre Probatoire entry is durable, approved evidence for future use. (It replaces the former term "Canonical Memory".)

A Registre Probatoire entry requires:

- a clear claim;
- a defined scope;
- a certainty level (E0–E4);
- exhibits, dates and citation;
- Evidence Pack linkage;
- an approval path;
- reviewability;
- a revocation or supersession path.

A Registre Probatoire entry must be specific enough to be useful and bounded enough to avoid overreach.

## Promotion rule

Default rule:

```text
candidate until approved
```

Promotion to a Registre Probatoire entry requires:

- evidence;
- explicit review;
- approval at the required level;
- scope definition;
- a certainty level;
- status update.

No runtime may promote a register entry automatically.

No OpenWebUI Knowledge Base may promote a register entry automatically.

No Hermes profile may promote a register entry automatically.

No repeated observation may promote a register entry automatically.

## Rejection rule

A Register Candidate must be rejected or deferred when it is:

- unsupported;
- too broad;
- private without clear need;
- unsafe to retain;
- contradicted by stronger evidence;
- derived from runtime state only;
- dependent on a temporary condition;
- likely to become stale without review.

Rejected candidates may remain referenced in Evidence Packs for audit, but they do not become Registre Probatoire entries.

## Scopes

A Registre Probatoire entry must declare scope.

Allowed scopes include:

```text
user
project
domain
repository
governance
system
```

Scope controls reuse.

A project entry must not silently become a system entry.

A user entry must not silently become domain doctrine.

A domain entry must not silently override governance doctrine.

## Status values

Register governance may use the following statuses:

```text
candidate
under_review
approved
rejected
deferred
superseded
revoked
archived
```

Status changes are governance events.

They are not runtime events.

## Evidence linkage

An entry without evidence is not a Registre Probatoire entry.

Evidence linkage may include:

- an Evidence Pack identifier;
- a source reference;
- exhibits, dates and citation;
- a review note;
- an approval note;
- a supersession note.

If evidence is missing, the item remains a candidate or must be rejected.

## Approval linkage

Register promotion must define approval expectations.

Low-risk working entries may require light review.

Doctrine-level or system-level entries require stronger approval.

Anything that changes future behavior, permissions, safety posture, user assumptions or governance doctrine requires explicit approval.

## Revocation and supersession

A Registre Probatoire entry must remain revisable.

Corrections should not silently rewrite history.

Use:

```text
superseded
revoked
archived
```

when an entry is no longer valid.

Append or link the correction rather than erasing the historical record.

## Relationship to Evidence Packs

Evidence Packs are the preferred source for Register Candidates.

An Evidence Pack may propose a register entry.

It does not canonize one.

Register promotion is a separate governance act.

## Relationship to Task Contracts

A Task Contract may specify register behavior.

It may authorize:

- no register output;
- Register Candidate proposal;
- review of existing register entries;
- a revocation proposal;
- a supersession proposal.

It must not authorize automatic promotion.

## Relationship to OpenWebUI

OpenWebUI may expose:

- Knowledge Bases;
- Register Candidates;
- Registre Probatoire excerpts;
- approval prompts;
- Evidence Packs;
- review status.

OpenWebUI does not canonize a register entry.

OpenWebUI is not the source of truth.

An OpenWebUI Knowledge Base is consultable knowledge.

It is not a Registre Probatoire entry.

## Relationship to Hermes Agent

Hermès keeps its own runtime memory (mem0 or another system). It is free, self-evolving and outside Pantheon. Pantheon does not govern its content or its evolution.

Hermes Agent may generate Register Candidates under Task Contract.

Hermes Agent does not promote a register entry.

Hermes Agent does not own the Registre Probatoire.

Hermes Agent may consume approved register entries through Context Packs.

Hermès memory carries no authority and may not be cited for a consequential decision.

## Relationship to schemas

Register schemas validate governance structure.

They may validate:

- candidate structure;
- scope;
- status;
- certainty;
- evidence linkage;
- approval linkage;
- source references;
- risk notes.

They must not define:

- runtime memory stores;
- vector database behavior;
- embedding index behavior;
- automatic retrieval rules;
- agent scratchpad persistence;
- autonomous promotion logic.

The schema rename is applied: `schemas/register_candidate.schema.yaml` (formerly `memory_candidate`) is the schema for Register Candidates, with `certainty` on the E0–E4 axis.

## Forbidden drift

Register governance must never become:

- vector database policy;
- automatic long-term memory;
- runtime cache management;
- agent scratchpad persistence;
- self-promoting memory;
- Hermès memory treated as authority;
- user profiling without approval;
- hidden behavioral steering;
- implicit doctrine mutation.

If a register entry changes future behavior without review, governance drift has occurred.

## Final rule

Knowledge can be consulted.

Context can be injected.

Hermès remembers freely.

Pantheon keeps the proof.

Only an approved Registre Probatoire entry can govern future behavior.
