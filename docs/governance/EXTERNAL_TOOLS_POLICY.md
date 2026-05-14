# External Tools Policy

Status: active doctrine — external capability governance.

External tools are capabilities.

They are not authority.

They are not governance.

They are not memory.

They are not proof by themselves.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This document defines how Pantheon Next governs external tools and capability surfaces.

It does not define a tool runtime.

It does not define a provider router.

It does not define a plugin manager.

It does not define installation behavior.

It does not authorize hidden execution.

## Definition

An external tool is any capability outside the canonical Pantheon governance documents that can read, transform, generate, write, send, publish, delete, install, configure, execute, retrieve, call another service, alter a repository, alter a project artifact, affect a user-visible output or influence memory.

This includes but is not limited to:

- web search;
- browser retrieval;
- file read and write tools;
- repository tools;
- email tools;
- calendar tools;
- document tools;
- spreadsheet tools;
- diagram tools;
- image tools;
- code execution;
- controlled terminal use;
- MCP servers;
- OpenWebUI functions, tools, pipes, filters, actions or pipelines;
- Hermes tools and skills;
- provider gateways;
- cloud APIs;
- local services;
- import, export or conversion tools;
- installers and configuration tools.

A capability being available does not mean it is authorized.

## Core rule

Tool use must be justified by the task.

Tool use must stay inside the Task Contract when a Task Contract is required.

Tool output must be treated as candidate evidence until reviewed.

Tool availability must never bypass approval.

## Default posture

Default posture:

```text
not authorized unless scope, evidence and approval allow it
```

This default protects Pantheon Next from becoming a free tool runtime.

It also protects the user from silent external effects.

## Tool risk classes

Tool risk is evaluated by capability effect.

These classes guide approval expectations.

Final approval remains governed by `APPROVALS.md`.

### T0 — no external effect

Examples:

```text
local display
formatting without persistence
local non-sensitive transformation
read-only review of already supplied content
```

Expected governance:

```text
low evidence burden
no durable effect
no memory promotion
```

### T1 — read-only retrieval

Examples:

```text
web retrieval
repository read
document read
email read
calendar read
Knowledge Base retrieval
```

Expected governance:

```text
source recorded
freshness considered
sensitive access checked
no write effect
```

### T2 — transformation or candidate artifact generation

Examples:

```text
summarization
classification
diagram draft
document draft
patch draft
local file generation
```

Expected governance:

```text
output marked candidate
sources and assumptions recorded when relevant
no external publication
no automatic memory promotion
```

### T3 — governed project mutation candidate

Examples:

```text
repository file update candidate
governance document update
project artifact revision
structured data transformation that may affect later decisions
```

Expected governance:

```text
Task Contract expected
Evidence Pack expected
diff or output review expected
approval checked
protected areas checked
```

### T4 — external write or communication effect

Examples:

```text
send email
create calendar event
publish document
write to external system
delete or archive external content
share file
change live configuration
```

Expected governance:

```text
explicit user intent
approval required
evidence recorded
rollback or correction path considered
```

### T5 — privileged, irreversible or doctrine-sensitive effect

Examples:

```text
credential handling
secret access
production configuration
runtime installation
plugin installation
provider routing change
memory promotion
doctrine mutation
protected repository area
irreversible deletion
financial or legal external effect
```

Expected governance:

```text
high approval burden
scope must be explicit
evidence must be strong
rollback or mitigation must be addressed
no silent execution
```

## Authorization gates

Before using an external tool, check:

```text
purpose
scope
risk class
input sensitivity
external effect
write effect
memory implication
approval need
evidence need
rollback need
```

For governed work, these checks should appear in the Task Contract or Evidence Pack.

## Least capability principle

Use the smallest capability that can satisfy the task.

Prefer:

```text
read before write
candidate before mutation
local transformation before external write
explicit approval before external effect
source reference before memory proposal
```

Do not use a broad tool when a narrow tool is sufficient.

Do not use a write-capable tool for a read-only task.

## Evidence requirements

Tool output that affects a decision must be recorded as evidence.

Evidence should identify:

- tool category;
- purpose;
- source or target when relevant;
- assumptions;
- output reference;
- risk note;
- approval state;
- limitation or uncertainty.

Tool output must not be presented as self-validating truth.

## Read tools

Read tools may retrieve sources, project data or operational context.

Read access must still be governed when content is sensitive, private, stale, privileged or decision-critical.

Read output should be marked when it is:

```text
partial
stale
contradicted
unverified
sensitive
private
retrieved only
```

Read access does not authorize write access.

## Write tools

Write tools can create external effects.

They require stronger governance than read tools.

Write tools include actions such as:

```text
send
publish
create
update
delete
archive
share
commit
configure
install
```

A write action should not occur from hidden workflow logic.

A write action should be traceable in evidence.

## Repository tools

Repository tools are high-risk when they mutate canonical documents, code or protected areas.

Repository mutation requires:

- scope clarity;
- protected-area check;
- actual diff awareness;
- evidence record;
- rollback or correction awareness;
- approval level appropriate to the touched area.

Patch Candidates are not merge decisions.

Commits are not doctrine validation by themselves.

## Communication tools

Communication tools include email, chat, calendar, messaging and publication channels.

They create external effects.

They should preserve:

- recipient or destination;
- exact content or summary;
- intent;
- approval state;
- send or publication status.

Drafting is lower risk than sending.

Sending is a governed external effect.

## Code and terminal tools

Code execution and controlled terminal use may be useful but risky.

They must not create an internal Pantheon runtime.

They must not bypass repository policy.

They must not install dependencies, services, plugins, skills or providers without explicit authorization and the relevant approval level.

Generated outputs should remain candidates unless reviewed.

## MCP, gateways and provider-facing tools

MCP servers, provider gateways and model routing surfaces are external capability surfaces.

Pantheon Next must not become their router.

Pantheon Next may govern their authorization, evidence expectations and approval requirements.

It must not implement hidden routing, hidden dispatch, hidden scheduling or hidden provider selection.

## Installation and configuration tools

Installation and configuration tools are privileged by default.

They may alter runtime behavior, security posture, provider behavior, tool availability or execution boundaries.

They require explicit scope and approval.

Pantheon Next must not automatically install skills, plugins, tools, providers or runtimes.

## Memory-affecting tools

A tool that stores, indexes, retrieves, ranks, promotes or modifies long-lived information has memory implications.

Such tools must not promote Canonical Memory automatically.

They may produce Memory Candidates only when allowed by Task Contract and approval policy.

Memory promotion remains governed by `MEMORY.md`.

## Secrets and private data

Secrets, credentials, tokens, private data and sensitive project information require strict handling.

External tools must not expose secrets in outputs, logs, prompts, context packs, Evidence Packs or public artifacts.

If secret exposure is suspected, the tool result must be treated as a security risk, not a normal evidence item.

## Revocation and rollback

Tool authorization can be revoked.

A tool may be blocked when it becomes unsafe, stale, misconfigured, overbroad, unreviewable or incompatible with Pantheon doctrine.

For high-risk tool use, rollback or mitigation should be considered before execution.

## Forbidden drift

External tool governance must never become:

- tool runtime;
- provider router;
- automatic installer;
- free plugin manager;
- hidden workflow runner;
- hidden scheduler;
- autonomous execution engine;
- automatic skill installer;
- automatic memory promoter;
- self-evolution loop;
- approval bypass.

If tool availability becomes authorization, the boundary has failed.

If a tool can canonize memory or doctrine without approval, the boundary has failed.

## Implementation note

This policy intentionally avoids tool-specific endpoint, environment variable, Docker, provider, plugin, function, pipe, filter, action, MCP or skill installation details.

Those details must be verified against current official documentation before operational configuration is proposed.

## Final rule

A tool may help produce an output.

A tool may help produce evidence.

A tool does not decide whether the output is legitimate.

Pantheon Next governs that decision.
