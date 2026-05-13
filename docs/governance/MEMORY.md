# Memory

Status: active doctrine — conceptual stabilization.

Memory in Pantheon Next is governed continuity.

Memory is not retrieval.

Memory is not embedding storage.

Memory is not runtime state.

Memory is not repeated model confidence.

Memory becomes canonical only through evidence, review and approval.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next governs what may become durable knowledge for future use.

It separates:

- knowledge that can be consulted;
- context that can be injected;
- observations that can be proposed;
- Memory Candidates that can be reviewed;
- Canonical Memory that has been approved.

This separation prevents accidental canonization.

## Core principle

No memory is canonical by default.

A model output is not memory.

A retrieved document is not memory.

An embedding match is not memory.

A repeated observation is not memory.

A high-confidence answer is not memory.

A useful result is not memory.

Memory requires governance.

## Memory categories

Pantheon distinguishes the following categories.

```text
Knowledge
Context
Session State
Runtime State
Memory Candidate
Canonical Memory
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

Knowledge does not become memory automatically.

Knowledge may produce Memory Candidates only through an Evidence Pack.

## Context

Context is information temporarily injected to support a task.

Examples:

- user-provided instructions;
- project context;
- role context;
- policy context;
- domain context;
- approved memory excerpts.

Context is not automatically durable.

Context may be reused only if it is already canonical or if a new Memory Candidate is approved.

## Session State

Session State is transient conversation or task-local information.

It may help complete the current interaction.

It must not be treated as Canonical Memory.

Session State can generate a Memory Candidate when the information appears durable, useful and safe to retain.

## Runtime State

Runtime State belongs outside Pantheon Next.

Examples:

- worker state;
- queue state;
- scheduler state;
- tool execution state;
- provider routing state;
- LangGraph state;
- agent scratchpad state;
- temporary execution cache.

Pantheon Next does not own Runtime State.

Runtime State must not become Canonical Memory.

Runtime State may be summarized as evidence only when it is relevant to review, audit or risk analysis.

## Memory Candidate

A Memory Candidate is a proposed durable memory item.

It is not canonical.

It must remain explicitly marked as candidate until approved.

A Memory Candidate should define:

```text
Claim
Scope
Source
Evidence link
Confidence
Risk
Proposed durability
Required approval
Status
```

A Memory Candidate may come from:

- user instruction;
- project pattern;
- repeated validated usage;
- Evidence Pack output;
- governance review;
- domain review.

A Memory Candidate must not come directly from raw model confidence.

## Canonical Memory

Canonical Memory is durable memory approved for future use.

Canonical Memory requires:

- clear claim;
- defined scope;
- Evidence Pack linkage;
- approval path;
- reviewability;
- revocation or supersession path.

Canonical Memory must be specific enough to be useful and bounded enough to avoid overreach.

## Promotion rule

Default rule:

```text
candidate until approved
```

Promotion to Canonical Memory requires:

- evidence;
- explicit review;
- approval at the required level;
- scope definition;
- status update.

No runtime may promote memory automatically.

No OpenWebUI Knowledge Base may promote memory automatically.

No Hermes profile may promote memory automatically.

No repeated observation may promote memory automatically.

## Rejection rule

A Memory Candidate must be rejected or deferred when it is:

- unsupported;
- too broad;
- private without clear need;
- unsafe to retain;
- contradicted by stronger evidence;
- derived from runtime state only;
- dependent on a temporary condition;
- likely to become stale without review.

Rejected candidates may remain referenced in Evidence Packs for audit, but they do not become Canonical Memory.

## Scopes

Memory must declare scope.

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

A project memory must not silently become system memory.

A user memory must not silently become domain doctrine.

A domain memory must not silently override governance doctrine.

## Status values

Memory governance may use the following statuses:

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

Memory without evidence is not Canonical Memory.

Evidence linkage may include:

- Evidence Pack identifier;
- source reference;
- review note;
- approval note;
- supersession note.

If evidence is missing, the item remains candidate or must be rejected.

## Approval linkage

Memory promotion must define approval expectations.

Low-risk working memory may require light review.

Doctrine-level or system-level memory requires stronger approval.

Anything that changes future behavior, permissions, safety posture, user assumptions or governance doctrine requires explicit approval.

## Revocation and supersession

Canonical Memory must remain revisable.

Corrections should not silently rewrite history.

Use:

```text
superseded
revoked
archived
```

when a memory item is no longer valid.

Append or link the correction rather than erasing the historical record.

## Relationship to Evidence Packs

Evidence Packs are the preferred source for Memory Candidates.

An Evidence Pack may propose memory.

It does not canonize memory.

Memory promotion is a separate governance act.

## Relationship to Task Contracts

A Task Contract may specify memory behavior.

It may authorize:

- no memory output;
- Memory Candidate proposal;
- review of existing memory;
- revocation proposal;
- supersession proposal.

It must not authorize automatic memory promotion.

## Relationship to OpenWebUI

OpenWebUI may expose:

- Knowledge Bases;
- Memory Candidates;
- Canonical Memory excerpts;
- approval prompts;
- Evidence Packs;
- review status.

OpenWebUI does not canonize memory.

OpenWebUI is not the source of truth.

An OpenWebUI Knowledge Base is consultable knowledge.

It is not Canonical Memory.

## Relationship to Hermes Agent

Hermes Agent may generate Memory Candidates under Task Contract.

Hermes Agent does not promote memory.

Hermes Agent does not own Canonical Memory.

Hermes Agent may consume approved memory through Context Packs.

Hermes runtime state remains outside Pantheon.

## Relationship to schemas

Memory schemas validate governance structure.

They may validate:

- candidate structure;
- scope;
- status;
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

## Forbidden drift

Memory governance must never become:

- vector database policy;
- automatic long-term memory;
- runtime cache management;
- agent scratchpad persistence;
- self-promoting memory;
- user profiling without approval;
- hidden behavioral steering;
- implicit doctrine mutation.

If memory changes future behavior without review, governance drift has occurred.

## Final rule

Knowledge can be consulted.

Context can be injected.

Memory can be proposed.

Only approved memory can govern future behavior.
