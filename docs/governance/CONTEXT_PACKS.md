# Context Packs

Status: active doctrine — governed context boundary.

A Context Pack is a scoped, governed context bundle prepared for an assistant, cockpit, runtime or review surface.

A Context Pack prepares work.

It does not execute work.

It is not memory.

It is not evidence.

It is not doctrine by itself.

It is not runtime state.

It is not a system prompt dump.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Context Packs solve the recurring problem of assistants starting without enough project context.

They provide a bounded way to give an assistant or external runtime the context it needs without turning prior chat history, retrieved knowledge or tool output into a Registre Probatoire entry.

They can support:

- Claude Code through `CLAUDE.md` or imported instructions;
- ChatGPT through project instructions or pinned context;
- OpenWebUI through system prompts, folders, Knowledge Bases and cockpit display;
- Hermes Agent through profiles, Task Contracts and scoped context;
- other external assistants through adapter-specific instructions.

The canonical object is the Context Pack.

Tool-specific files are adapters.

## Core principle

Context prepares action.

Evidence supports review.

Approval legitimizes change.

Memory preserves what was validated.

A Context Pack gives a tool enough bounded context to behave usefully.

It must not become a hidden source of truth.

## Canonical structure

A Context Pack should define:

```text
Identity
Purpose
Scope
Target tool or surface
Included doctrine
Included context
Included memory excerpts
Included knowledge references
Task constraints
Protected areas
Evidence expectations
Approval expectations
Output expectations
Forbidden assumptions
Staleness notes
Risk notes
```

The exact shape may vary by adapter.

The governance meaning must remain stable.

## Identity

A Context Pack should have a stable identifier when it is reused or referenced.

The identifier is a governance identifier.

It is not a runtime session ID.

It is not an OpenWebUI folder ID.

It is not a Claude session ID.

It is not a Hermes worker ID.

## Purpose

Purpose explains why the Context Pack exists.

Good examples:

```text
prepare Claude Code to work safely on governance Markdown
prepare Hermes Agent to execute under a Task Contract
prepare OpenWebUI to expose project-scoped Knowledge without canonizing it
prepare ChatGPT to answer according to Pantheon doctrine
```

Bad example:

```text
load all previous context so the assistant can continue automatically
```

## Scope

Every Context Pack must declare scope.

Allowed scope types are defined in `SCOPE_ISOLATION.md`.

Common scopes include:

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

A Context Pack must not mix scopes silently.

If it combines project context, user preferences, domain knowledge and system doctrine, the distinction must remain visible.

## Target surface

A Context Pack should identify its intended target.

Examples:

```text
Claude Code
ChatGPT project
OpenWebUI folder
OpenWebUI Knowledge Base
Hermes profile
Hermes Task Contract
external assistant
human reviewer
```

Target surface does not determine authority.

Pantheon doctrine determines authority.

## Included doctrine

A Context Pack may include excerpts or references to active Pantheon doctrine.

Examples:

```text
OpenWebUI exposes
Hermes Agent executes
Pantheon Next governs
approval rules
memory rules
scope isolation rules
external tools policy
protected file rules
```

Doctrine excerpts must not be silently edited inside adapters.

If doctrine changes, the source governance document must change first.

## Included context

Included context is task-bounded information.

Examples:

```text
current objective
active project
active dossier
user intent
known constraints
accepted approach
rejected approach
relevant file paths
current branch or PR
```

Included context is not a Registre Probatoire entry by default.

If it should persist, it must become a Register Candidate.

## Included memory excerpts

A Context Pack may include a Registre Probatoire entry excerpts when they are relevant and scoped.

Each memory excerpt should preserve:

- claim;
- scope;
- source or evidence link;
- approval state;
- staleness or review status.

A Context Pack must not include unapproved memory as if it were canonical.

Register Candidates must be labeled as candidates.

## Included knowledge references

A Context Pack may include Knowledge Items or Source References.

These references inform work.

They do not become truth by inclusion.

A Context Pack may say:

```text
use this as a source
```

It must not imply:

```text
this is automatically valid doctrine
```

## Task constraints

A Context Pack may include constraints such as:

```text
only modify docs/governance files
avoid protected directories
read ai_logs before significant work
ask before schemas changes
no runtime architecture
no provider routing
no memory auto-promotion
```

Constraints help prevent tool drift.

They do not replace Task Contracts when a Task Contract is required.

## Protected areas

A Context Pack should surface protected areas when relevant.

Examples:

```text
schemas/
tests/
operations/
platform/
Docker
.env
CLAUDE.md
pyproject.toml
```

If a task touches protected areas, the assistant or runtime must escalate according to repository policy.

## Evidence expectations

A Context Pack may define expected evidence.

Examples:

```text
cite source files
record assumptions
record risks
list files changed
add ai_log after significant intervention
verify actual diff after important commit
```

Evidence expectations do not replace an Evidence Pack.

They prepare the task for evidence discipline.

## Approval expectations

A Context Pack may remind a tool of approval expectations.

Examples:

```text
ask before protected files
ask before destructive operations
ask before external side effects
ask before memory promotion
ask before doctrine mutation when not already authorized
```

Approval expectations must align with `APPROVALS.md`.

A Context Pack cannot approve itself.

## Output expectations

A Context Pack may specify output expectations.

Examples:

```text
answer directly
avoid filler openings
distinguish fact, interpretation and recommendation
list files changed after repo work
mark candidates as candidates
never say implemented when only documented
```

Output expectations are adapter guidance.

They are not a Registre Probatoire entry.

## Forbidden assumptions

A Context Pack should make forbidden assumptions explicit.

Examples:

```text
Do not assume OpenWebUI is memory.
Do not assume Hermes can canonize outputs.
Do not assume retrieved knowledge is evidence.
Do not assume evidence is approval.
Do not assume approval causes execution.
Do not assume workflow means runtime graph.
```

This is the Pantheon equivalent of ask, do not assume.

## Staleness

Context Packs can become stale.

A Context Pack should declare when it must be reviewed.

Review triggers may include:

- doctrine update;
- status update;
- schema update;
- protected-file change;
- integration change;
- project scope change;
- user decision;
- external runtime change.

Stale context must not silently govern future behavior.

## Tool-specific adapters

Adapters translate Context Packs into tool-specific formats.

Examples:

```text
CLAUDE.md
AGENTS.md import
ChatGPT project instructions
OpenWebUI system prompt
OpenWebUI folder description
Hermes profile note
Hermes Task Contract appendix
human checklist
```

Adapters are not canonical by themselves.

Governance documents remain canonical.

If an adapter conflicts with active Pantheon doctrine, Pantheon doctrine wins.

## Claude adapter

A Claude-facing adapter may use `CLAUDE.md`.

Useful rules include:

```text
Ask, do not assume.
Use the simplest safe path first.
Do not touch unrelated files.
Flag uncertainty explicitly.
```

These rules are valuable because they reduce drift.

They must be adapted to Pantheon doctrine, not copied blindly.

A root-level `MEMORY.md` or `ERRORS.md` pattern must not become parallel a Registre Probatoire entry unless explicitly governed.

For Pantheon repository work, significant decisions should be traced through `ai_logs/`, `STATUS.md`, `CHANGELOG.md`, Register Candidates or other governed artifacts as appropriate.

## ChatGPT adapter

A ChatGPT-facing adapter may use project instructions or pinned context.

It should preserve:

- current project doctrine;
- user communication preferences;
- protected file rules;
- source verification rules;
- scope boundaries;
- current task frame.

It must not treat prior conversation memory as a Registre Probatoire entry unless the claim is approved and scoped.

## OpenWebUI adapter

An OpenWebUI-facing adapter may use system prompts, folder scope, Knowledge Bases and visible approval surfaces.

OpenWebUI folders may help define working scope.

OpenWebUI Knowledge Bases may provide Knowledge Items.

Neither becomes a Registre Probatoire entry by default.

OpenWebUI exposes.

It does not canonize.

## Hermes adapter

A Hermes-facing adapter should usually be attached to a Task Contract or Context Pack export.

It may include:

- task scope;
- role viewpoint;
- allowed tools;
- forbidden actions;
- evidence expectations;
- memory rules;
- approval boundaries;
- output format.

Hermes may execute under this context.

Hermes may not broaden the scope, promote memory or approve itself.

## Relationship to Task Contracts

A Context Pack prepares context.

A Task Contract authorizes a governed execution boundary.

A Context Pack may support a Task Contract.

It does not replace a Task Contract.

When execution, external effects, repository mutation, protected areas, memory proposals or significant risk are involved, a Task Contract may still be required.

## Relationship to Evidence Packs

A Context Pack may define expected evidence.

An Evidence Pack records actual evidence.

A Context Pack is not proof.

It may become a referenced source in an Evidence Pack if it influenced the task.

## Relationship to Memory

A Context Pack is not memory.

It may contain approved memory excerpts.

It may produce Register Candidates.

It must not promote memory automatically.

Memory promotion remains governed by `MEMORY.md`.

## Relationship to Scope Isolation

A Context Pack must preserve scope isolation.

A session-scoped pack must not become project memory.

A project-scoped pack must not become system doctrine.

A user-scoped pack must not become organization doctrine.

Scope expansion requires review.

## Relationship to Knowledge Taxonomy

A Context Pack may combine Raw Sources, Knowledge Items, Retrieved Knowledge, Working Context, Evidence references and Memory excerpts.

The category of each included item must remain visible when the distinction matters.

Do not flatten all context into one truth bucket.

## Relationship to external tools

A Context Pack may authorize or forbid tool categories only when aligned with a Task Contract and `EXTERNAL_TOOLS_POLICY.md`.

Tool availability is not authorization.

Tool instructions in a Context Pack must not create a hidden tool runtime.

## Forbidden drift

Context Packs must never become:

- a Registre Probatoire entry by accumulation;
- hidden system prompt authority;
- runtime state bundle;
- unreviewed session dump;
- secret leakage path;
- automatic task launcher;
- approval substitute;
- evidence substitute;
- doctrine mutation surface;
- cross-project context leak.

If a Context Pack changes future behavior without scope, evidence and approval, the boundary has failed.

If an adapter becomes more authoritative than Pantheon doctrine, the boundary has failed.

## Final rule

Every assistant may receive context.

No assistant may invent doctrine from habit, memory or prior behavior.

Context prepares action.

Pantheon governs what survives.
