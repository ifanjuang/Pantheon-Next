# OpenWebUI Integration

Status: active doctrine — integration boundary stabilization.

OpenWebUI is the user cockpit for Pantheon Next.

OpenWebUI exposes.

It does not govern.

It does not execute Pantheon doctrine.

It does not canonize knowledge or memory.

It does not become the source of truth.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This document defines the governance boundary between Pantheon Next and OpenWebUI.

It describes what OpenWebUI may display, request, collect and transmit in a governed Pantheon workflow.

It is not an OpenWebUI installation guide.

It is not a plugin specification.

It is not a function, pipe, filter, action or pipeline runtime specification.

It is not a provider configuration guide.

It is not a Docker, environment variable or endpoint document.

## Canonical boundary

OpenWebUI is the cockpit surface.

Pantheon Next is the governance layer.

Hermes Agent is the execution runtime.

OpenWebUI may expose the interaction between user, governance artifacts, evidence and candidate outputs.

OpenWebUI must not become the place where governance truth is created silently.

## Allowed OpenWebUI surfaces

OpenWebUI may expose:

```text
chat interaction
user intent capture
source upload or source reference
Knowledge Base consultation
Task Contract display
approval prompt
approval response capture
Evidence Pack display
Run Trace View display
candidate output display
Memory Candidate display
Canonical Memory excerpt display
revision request
escalation request
final delivery display
```

These are cockpit surfaces.

They are not governance authority by themselves.

## Display is not authority

Displaying an artifact in OpenWebUI does not make it canonical.

Displaying a Knowledge Base result does not make it memory.

Displaying an Evidence Pack does not approve the evidence.

Displaying a candidate output does not validate the output.

Displaying a role viewpoint does not make it an approved decision.

Authority comes from governed approval, evidence and memory rules.

## User action capture

OpenWebUI may capture user actions such as:

```text
approve
reject
request revision
request more evidence
escalate
mark source relevant
mark source irrelevant
accept delivery
reject delivery
```

A user action is governance-relevant only when the record is clear enough.

The record should identify:

- what was approved or rejected;
- who acted, when available;
- when the action occurred;
- what scope the action covered;
- which evidence was visible;
- which approval level was involved;
- whether memory promotion was included or excluded.

A vague click is not enough for high-risk approval.

Approval remains governed by `APPROVALS.md`.

## Knowledge Base rule

OpenWebUI Knowledge Bases are consultable Knowledge.

They are not Canonical Memory.

They are not a source of truth by default.

They may support:

- retrieval;
- user context;
- evidence discovery;
- drafting;
- source comparison;
- task scoping.

They must not silently create:

- Canonical Memory;
- policy updates;
- doctrine updates;
- user preference memory;
- project memory;
- workflow truth.

A Knowledge Base item may become a source in an Evidence Pack.

It may become a Memory Candidate if the task and approval rules allow it.

It does not become memory merely because it was uploaded, indexed, embedded, retrieved or repeatedly used.

## Governed Knowledge handoff to Hermes

OpenWebUI may organize user-side folders, files, Notes and Knowledge Bases.

This organization may inform task scope.

It does not grant Hermes Agent free access to OpenWebUI data.

The canonical handoff rule is:

```text
OpenWebUI organizes user knowledge.
Pantheon turns that organization into a bounded task scope.
Hermes consults only the authorized scope and returns candidates with evidence.
```

OpenWebUI may expose user selection of:

- dossier;
- project;
- folder;
- Knowledge Base;
- file;
- Note;
- source subset;
- conversation or channel excerpt.

Pantheon must translate that selection into a bounded governance artifact before execution.

Allowed handoff artifacts include:

```text
Task Contract
Context Pack
allowed_knowledge_ids
allowed_file_ids
allowed_note_ids
source references
retrieved excerpts
exclusion list
approval ceiling
memory rule
```

OpenWebUI must preserve the distinction between:

```text
available knowledge
selected knowledge
retrieved knowledge
evidence candidate
Memory Candidate
Canonical Memory
```

A user selecting a Knowledge Base does not authorize global cross-dossier access.

A model discovering an accessible Knowledge Base does not make that Knowledge Base part of the current task.

A retrieved chunk does not become evidence until selected and represented as such.

A retrieved or cited item does not become memory without governed memory review.

### Context Pack handoff

The preferred MVP handoff is a bounded Context Pack.

OpenWebUI may help collect the selected content.

Pantheon governs what is included, excluded and marked uncertain.

Hermes receives only the authorized material needed for the task.

This avoids coupling Hermes to OpenWebUI internals.

### Read-only gateway handoff

A future implementation may expose a read-only governed knowledge gateway.

Such a gateway may provide scoped operations such as:

```text
list_scopes_for_user
list_knowledge_for_scope
search_scoped_knowledge
fetch_source_excerpt
fetch_source_metadata
create_evidence_candidate
```

Any such gateway must remain read-only by default and must include scope, user, task and approval context.

### Direct database access

Direct Hermes access to OpenWebUI database tables, vector stores, Postgres, pgvector or internal storage should be avoided for normal workflows.

If ever used for diagnostics or controlled administration, it must be:

- read-only;
- scoped;
- logged;
- restricted to governed views rather than raw tables where possible;
- forbidden from writing memory;
- forbidden from bypassing approvals.

OpenWebUI remains cockpit and knowledge organization surface.

It does not become the knowledge authority for Pantheon.

## Candidate output display

OpenWebUI may display outputs returned by Hermes Agent or another external runtime.

These outputs must be labeled according to governance state.

Useful labels include:

```text
candidate
under_review
approved
rejected
blocked_by_scope
blocked_by_evidence
blocked_by_approval
blocked_by_capability_gap
superseded
```

OpenWebUI display must not erase uncertainty.

If evidence is partial, the interface should preserve that limitation.

## Evidence Pack display

OpenWebUI may display Evidence Packs to the user.

The display may include:

- linked Task Contract;
- sources;
- assumptions;
- actions summary;
- risks;
- outputs;
- memory candidates;
- approval state;
- limitations.

OpenWebUI display does not replace the Evidence Pack.

OpenWebUI must not hide missing evidence.

## Task Contract display

OpenWebUI may display Task Contracts before execution or review.

The user may approve, reject or request revision through the cockpit.

OpenWebUI must not expand Task Contract scope automatically.

If the user asks for additional work, the Task Contract must be revised or a new contract must be created when governance requires it.

## Memory display

OpenWebUI may display Memory Candidates and Canonical Memory excerpts.

Memory Candidate display is not promotion.

Canonical Memory display is not modification.

OpenWebUI must not infer memory promotion from:

- repeated chat content;
- user convenience;
- retrieval success;
- model confidence;
- interface affordance;
- Knowledge Base indexing.

Memory promotion remains governed by `MEMORY.md`.

## Functions, tools, pipes, filters, actions and pipelines

OpenWebUI may expose or host capability surfaces such as functions, tools, pipes, filters, actions or pipelines.

Pantheon Next treats these as external capability surfaces when they can affect a result, call a service, transform data, trigger execution, write data, publish data or influence memory.

They must be governed by:

- Task Contract scope;
- `EXTERNAL_TOOLS_POLICY.md`;
- Evidence Pack requirements;
- approval level;
- memory rules.

They must not become hidden Pantheon runtime.

They must not bypass Hermes when Hermes is the intended execution runtime.

They must not canonize memory or doctrine.

They must not become a free plugin manager for Pantheon Next.

## Communication channels

OpenWebUI may be one communication cockpit among others.

Other channels may include email, messaging platforms, documents, spreadsheets, forms or project tools.

A channel is not governance by itself.

The governance record must still preserve scope, evidence, approval, output status and memory state.

## Source upload and source reference

OpenWebUI may allow users to upload or reference sources.

Uploaded sources remain source material until reviewed.

A source can be:

- relevant;
- irrelevant;
- partial;
- contradicted;
- stale;
- superseded;
- approved as reference;
- rejected.

Upload does not equal validation.

Retrieval does not equal validation.

## Context Packs

OpenWebUI may display or transmit Context Packs.

A Context Pack is a bounded context artifact.

It is not Canonical Memory.

It is not runtime state.

It should declare:

- purpose;
- scope;
- included references;
- excluded references;
- memory status;
- staleness or uncertainty;
- approval state when relevant.

## Relationship to Hermes Agent

OpenWebUI may be the visible interface through which the user requests work that Hermes Agent executes.

OpenWebUI does not execute Hermes work by itself.

OpenWebUI may display Hermes results.

OpenWebUI does not approve Hermes results by displaying them.

OpenWebUI does not canonize Hermes memory candidates.

OpenWebUI may expose a scoped Knowledge handoff to Hermes only when Pantheon has framed the task scope.

OpenWebUI must not grant Hermes broad access to every Knowledge Base, Note, folder, file or vector store merely because the user can access them in the cockpit.

## Relationship to Pantheon Next

Pantheon Next governs the doctrine, artifacts, approvals, memory rules and evidence expectations.

OpenWebUI may expose those artifacts to the user.

OpenWebUI must not become the canonical governance repository.

If a decision matters beyond the current interaction, it must be recorded in governed Pantheon artifacts.

## Forbidden integration drift

OpenWebUI integration must never become:

- Pantheon execution runtime;
- governance source of truth;
- canonical memory store;
- hidden workflow runner;
- hidden scheduler;
- provider router;
- autonomous agent runtime;
- automatic memory promoter;
- uncontrolled plugin manager;
- doctrine mutation surface without approval;
- approval bypass;
- unrestricted knowledge gateway to Hermes;
- direct global database access path for Hermes.

If OpenWebUI display is treated as canonical governance truth, the boundary has failed.

If an OpenWebUI capability surface runs Pantheon work without Task Contract and Evidence Pack, the boundary has failed.

If Hermes can freely browse OpenWebUI Knowledge without a bounded task scope, the boundary has failed.

## Implementation note

This document intentionally avoids operational details such as OpenWebUI version, endpoints, environment variables, Docker configuration, provider configuration, plugin installation, function syntax, pipe syntax, filter syntax, action syntax or pipeline behavior.

Those details must be verified against current official OpenWebUI documentation before any operational configuration is proposed.

## Final rule

OpenWebUI makes governance visible and actionable for the user.

It does not make governance true by itself.

OpenWebUI may organize user knowledge.

It does not authorize unbounded execution access to that knowledge.
