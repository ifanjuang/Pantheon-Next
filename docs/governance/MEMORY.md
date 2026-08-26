# Memory

Status: active doctrine — Registre Probatoire boundary owner.

Pantheon does not own a conversational-memory engine.

Hermes owns its runtime memory and may use its native facilities or one separately selected external provider. The provider choice is an execution-runtime concern unless it changes a Pantheon governance boundary.

Current Hermes native facilities include bounded persistent `MEMORY.md` / `USER.md`, session history/search and project/context files. They are sufficient for a valid deployment when they satisfy the user's needs.

```text
Hermes native memory sufficient
-> no external memory provider required

external provider selected
-> optional runtime binding
-> not a Pantheon dependency
```

Pantheon governs the `Registre Probatoire`, not Hermes memory.

## Core boundary

```text
memory != Evidence
retrieved != true
remembered != approved
runtime persistence != Pantheon persistence
provider selection != governance authority
```

Hermes memory may store, recall, rank, summarize and propose. It carries no professional authority.

```text
Memory first. Evidence when consequential. Status when deciding. Approval when acting.
```

Nothing remembered or retrieved becomes probative automatically.

## Categories

Pantheon distinguishes:

```text
Knowledge
Context
Session State
Runtime State
Register Candidate
Registre Probatoire entry
```

They must not be collapsed.

### Knowledge

Knowledge is consultable material under existing Knowledge/source owners. It may support reasoning but is not automatically Evidence.

The implementation used to retrieve or display Knowledge may be Hermes-native or external and remains replaceable.

### Context

Context is bounded information assembled for a task. A Context Pack is not memory and does not become durable merely because Hermes consumed it.

### Session State

Session State is transient conversation or task-local information. Hermes may persist conversation history operationally, but that does not create Pantheon durable state.

### Runtime State

Runtime State belongs to the execution runtime.

Examples include:

- Hermes native memory;
- an external Hermes memory provider;
- session/history databases;
- worker/tool execution state;
- temporary caches and provider state.

Pantheon does not treat Runtime State as Evidence or Registre Probatoire state.

## Provider-agnostic rule

Pantheon does not prescribe Hindsight, Mnemosyne, Mem0 or another memory product.

Hindsight has substantial qualification evidence in this repository and can be a useful optional binding. Mnemosyne and other providers have historical or comparison evidence. None is a Pantheon prerequisite.

```text
qualified provider != mandatory provider
recommended provider != authority
same provider for two functions != same responsibility
```

Workspace/document retrieval and conversational/workstream memory remain conceptually distinct even if one product implements both. Their scopes must stay distinguishable.

The machine-checkable `external_runtime_memory` Capability Binding may remain `unbound` when Hermes native memory is sufficient.

## Register Candidate

A Register Candidate is a proposed durable Assertion. It is not probative.

It should identify at least:

```text
Claim
Scope
Source / Evidence link
Certainty
Risk
Required approval
Status
```

A candidate may originate from user instruction, validated project work, Evidence Pack output, Hermes observation or governance review. Raw model confidence is not sufficient.

## Registre Probatoire entry

A Registre Probatoire entry is durable, reviewed evidence for future consequential use.

It requires:

- a clear scoped claim;
- certainty level;
- exhibits, dates and citations;
- Evidence linkage;
- the required approval;
- reviewability;
- revocation or supersession path.

## Promotion rule

```text
candidate until approved
```

No Hermes profile, memory provider, retrieval engine, workspace, repeated observation or successful runtime operation may promote a Registre Probatoire entry automatically.

Promotion requires the existing Evidence and approval owners.

## Scope rule

Durable Assertions remain explicitly scoped, for example:

```text
user
project
domain
repository
governance
system
```

A project memory or note must not silently become agency/system doctrine. A filesystem folder or provider bank does not define governed identity by itself.

## Status rule

Register governance may use:

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

Those are governance states, not runtime-memory states.

## Final rule

```text
Hermes may remember with native or optional external facilities.
Pantheon does not need to know which provider is fashionable.
Pantheon cares when memory crosses into consequential context, Evidence, approval or durable governed Assertions.
Memory never crosses that boundary automatically.
```