# Scope Isolation

Status: active doctrine — memory and context compartmentalization.

Scope isolation is the governance rule that prevents information from leaking between sessions, tasks, dossiers, projects, users, domains and system doctrine.

This document is inspired by folder-scoped memory isolation patterns in OpenWebUI, but it does not import an OpenWebUI filter, plugin or runtime behavior.

It defines Pantheon governance doctrine only.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next must prevent accidental cross-contamination between contexts.

A memory-like item must never be globally reusable by default.

A source uploaded in one folder must not silently affect another folder.

A project fact must not become organization doctrine.

A session assumption must not become project memory.

A retrieved Knowledge Base item must not become Canonical Memory.

Scope isolation makes those boundaries explicit.

## Core rule

Every memory-like or context-like artifact must declare scope.

Default rule:

```text
no global memory by default
```

A scoped artifact may be used only within its declared scope unless a governed review explicitly broadens that scope.

## Scope types

Allowed scope types:

```text
session
task
dossier
project
domain
user
organization
repository
governance
system
```

These scope types are governance categories.

They are not storage backends.

They are not OpenWebUI implementation details.

They are not runtime partitions.

## Scope identity

A scoped artifact should declare:

```text
scope_type
scope_id
scope_label
source
status
evidence_link
approval_state
created_at or observed_at
staleness or review rule
```

For low-risk working context, a lighter record may be acceptable.

For Memory Candidates and Canonical Memory, explicit scope is mandatory.

## Scope hierarchy

A narrower scope must not silently leak into a broader scope.

Examples:

```text
session -> project requires review
project -> domain requires review
domain -> system requires review
user -> organization requires review
folder -> project requires mapping
Knowledge Base -> memory requires approval
```

Scope expansion is a governance act.

It is not a retrieval effect.

It is not a UI effect.

It is not a runtime effect.

## OpenWebUI folders

OpenWebUI folders may provide useful UI scoping.

A folder can help identify a working perimeter.

A folder can help select relevant Knowledge Base material.

A folder can help separate chats, files and project contexts.

But an OpenWebUI folder is not Canonical Memory.

An OpenWebUI folder is not a governance scope by itself until mapped into a Pantheon scope.

The mapping must be explicit when the distinction matters.

Recommended mapping:

```text
OpenWebUI folder -> dossier or project scope
OpenWebUI chat -> session scope
OpenWebUI Knowledge Base -> Knowledge Item scope
OpenWebUI upload -> Raw Source or Source Reference
OpenWebUI memory-like feature -> Memory Candidate at most
```

## Chat scope

A chat is normally session-scoped.

Chat content may support the current task.

Chat content must not become durable memory by default.

A chat observation may become a Memory Candidate only when:

- the claim is explicit;
- the scope is defined;
- evidence or user confirmation exists;
- approval rules allow it.

## Project and dossier scope

Project and dossier scope are high-value boundaries.

They prevent one client, project, legal matter, architectural file or technical dossier from polluting another.

Project-scoped material may include:

- project facts;
- project constraints;
- project-specific sources;
- project decisions;
- project Memory Candidates;
- project deliverables;
- project Evidence Packs.

Project memory must not become user, organization, domain or system memory without review.

## Domain scope

Domain scope applies to reusable professional or technical knowledge.

Examples:

```text
architecture_fr
software
governance
legal_reference
```

Domain knowledge may inform many projects.

It must not override project-specific evidence.

It must not become system doctrine without governance review.

## User scope

User scope applies to durable user-specific preferences, constraints or recurring patterns.

User-scoped memory must be handled carefully.

It can influence future interactions only when approved and bounded.

It must not become organization doctrine.

It must not become project fact.

It must not become hidden behavioral steering.

## System and governance scope

System and governance scopes are the most protected.

They include:

- Pantheon doctrine;
- approval rules;
- memory policy;
- evidence policy;
- role authority;
- integration boundaries;
- external tools policy.

System or governance scope changes require strong evidence and explicit approval.

No session, project, folder, runtime output or repeated observation may mutate these scopes automatically.

## Context Packs

Context Packs must preserve scope isolation.

A Context Pack should declare:

- intended scope;
- included scopes;
- excluded scopes;
- source boundaries;
- memory status;
- staleness warnings;
- approval state when relevant.

A Context Pack must not mix scopes silently.

If it combines project memory, domain knowledge and system doctrine, the difference must remain visible.

## Evidence Packs

Evidence Packs should preserve scope.

An Evidence Pack should identify the scope of its sources, assumptions, outputs and Memory Candidates.

Evidence from one project must not be reused in another project without review.

A source used as evidence in one task does not become universal evidence.

## Memory Candidates

Every Memory Candidate must declare scope.

Required fields include:

```text
claim
scope_type
scope_id
source
evidence_link
risk
approval_state
status
```

A Memory Candidate without scope must remain invalid or incomplete.

Scope-less memory is a governance risk.

## Canonical Memory

Canonical Memory must remain scoped.

Canonical Memory does not mean global memory.

A project-scoped Canonical Memory governs only that project.

A user-scoped Canonical Memory governs only that user context.

A domain-scoped Canonical Memory governs only that domain.

A system-scoped Canonical Memory requires the highest discipline because it may affect all future behavior.

## Scope expansion

Scope expansion requires review.

Examples:

```text
project fact -> reusable domain rule
user preference -> organization practice
session insight -> project memory
project method -> system doctrine
folder context -> canonical project memory
```

Scope expansion should produce an Evidence Pack or review note.

It should identify what changes, why it changes, and what risks follow.

## Scope narrowing

Scope narrowing is allowed when a memory or context item was too broad.

Examples:

```text
system -> domain
domain -> project
project -> dossier
user -> session
```

Scope narrowing may be used as mitigation when overreach is detected.

## Scope conflicts

When two scopes conflict, do not silently merge them.

Escalate or mark the conflict.

Useful conflict states:

```text
scope_conflict
cross_project_conflict
user_project_conflict
domain_project_conflict
system_domain_conflict
stale_scope
unknown_scope
```

A conflict is not a failure.

It is a review signal.

## Deletion and cleanup

Automatic deletion of memory-like items is risky.

Cleanup may be useful for working context, stale candidates or orphaned artifacts, but it must not silently erase governance history.

For governed artifacts, prefer:

```text
revoked
superseded
archived
rejected
expired
```

instead of silent deletion.

If a UI or runtime cleanup mechanism removes items, the governance record must preserve what matters.

## Relationship to OpenWebUI

OpenWebUI may expose folder, chat and Knowledge Base boundaries.

OpenWebUI may help users select the active scope.

OpenWebUI may display scope labels and warnings.

OpenWebUI must not canonize scope.

OpenWebUI must not promote folder memory into Pantheon memory by itself.

OpenWebUI must not delete governed memory without a governance record.

## Relationship to Hermes Agent

Hermes Agent may receive scoped Context Packs.

Hermes may produce scoped outputs and scoped Memory Candidates.

Hermes must not broaden scope silently.

Hermes must report when a task requires access outside the declared scope.

Hermes runtime state remains outside Pantheon memory.

## Relationship to Knowledge Taxonomy

`KNOWLEDGE_TAXONOMY.md` defines the categories of source, knowledge, context, evidence, memory and doctrine.

This document defines how those categories are scoped.

The two documents must be read together.

## Relationship to Memory

`MEMORY.md` defines memory promotion and Canonical Memory.

This document adds the rule:

```text
memory is never global unless explicitly approved as global
```

## Forbidden drift

Scope isolation must never become:

- automatic memory promotion;
- hidden user profiling;
- silent cross-project context sharing;
- automatic folder memory canonization;
- UI-driven source of truth;
- runtime-managed Canonical Memory;
- silent deletion of governance history;
- global memory by convenience.

If folder scoping becomes canonical memory without approval, the boundary has failed.

If one project silently changes another project’s context, the boundary has failed.

If OpenWebUI or Hermes can broaden scope without Pantheon approval, the boundary has failed.

## Final rule

Every durable memory-like claim must answer:

```text
What is the claim?
Where is it valid?
Who or what approved it?
What evidence supports it?
When should it be reviewed?
```

Without scope, there is no governed memory.
