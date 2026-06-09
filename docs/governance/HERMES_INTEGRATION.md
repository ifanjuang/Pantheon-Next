# Hermes Integration

Status: active doctrine — integration boundary stabilization.

Hermes Agent is the external execution runtime for Pantheon Next.

Pantheon Next does not implement Hermes Agent.

Pantheon Next does not install Hermes Agent.

Pantheon Next does not deploy Hermes profiles.

Pantheon Next does not own Hermes internal runtime state.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This document defines the governance boundary between Pantheon Next and Hermes Agent.

It explains what Pantheon may send to Hermes, what Hermes may return to Pantheon, and what Hermes must never do on Pantheon’s behalf.

It is not a Hermes installation guide.

It is not a runtime specification.

It is not an endpoint contract.

It is not a queue, worker, scheduler, provider router or tool runtime design.

## Canonical boundary

Pantheon Next governs legitimacy.

Hermes Agent performs execution externally.

OpenWebUI exposes the interaction, evidence, outputs and approval surfaces to the user.

The boundary is documentary and operational.

It is not embedded execution.

## What Pantheon may provide to Hermes

Pantheon may provide governed context to Hermes through explicitly bounded artifacts.

Allowed outbound artifacts include:

```text
Task Contract
Context Pack
Role viewpoint request
Approval expectation
Tool policy excerpt
Evidence expectation
Memory rule
Risk note
Output format expectation
```

These artifacts constrain execution.

They do not run execution.

They do not assign internal Hermes workers.

They do not define Hermes queues, retries, provider routes or tool dispatch.

## What Hermes may return to Pantheon

Hermes may return candidate outputs and evidence.

Allowed inbound artifacts include:

```text
Result Candidate
Evidence Pack
Patch Candidate
Register Candidate
Capability Gap
Risk Escalation
Review Note
Output Artifact Reference
```

All returned artifacts remain candidates until governed review is complete.

Hermes done does not mean Pantheon approved.

Hermes output does not become canonical memory.

Hermes evidence does not approve itself.

## Task Contract bridge

Hermes execution must be bounded by a Task Contract when the task includes:

- repository mutation;
- external tools;
- protected areas;
- memory proposals;
- policy-sensitive work;
- doctrine-sensitive work;
- non-trivial risk;
- externally visible effects.

The Task Contract defines the governance envelope.

Hermes may choose how to operate internally, but only within that envelope.

If execution requires a broader scope than the contract allows, Hermes must report a scope gap rather than expanding the task silently.

## Evidence Pack bridge

Hermes must return reviewable evidence for governed work.

An Evidence Pack should identify:

- linked Task Contract;
- sources used;
- assumptions;
- actions at governance-relevant level;
- risks;
- outputs;
- memory candidates;
- approval state or approval gap.

Pantheon governs the evidence structure.

Hermes may produce evidence.

Hermes does not canonize evidence.

## OpenWebUI Knowledge handoff

Hermes may consult content organized in OpenWebUI only through a governed handoff.

Hermes must not freely browse OpenWebUI folders, Notes, Knowledge Bases, files, Postgres tables, pgvector stores or internal storage.

The canonical rule is:

```text
OpenWebUI organizes user knowledge.
Pantheon turns that organization into a bounded task scope.
Hermes consults only the authorized scope and returns candidates with evidence.
```

Allowed handoff forms:

```text
Context Pack
selected excerpts
source references
allowed_knowledge_ids
allowed_file_ids
allowed_note_ids
read-only scoped gateway result
Evidence Candidate references
```

Hermes may perform:

- scoped retrieval;
- source comparison;
- extraction;
- contradiction analysis;
- citation audit;
- coherence review;
- candidate synthesis;
- Evidence Pack preparation.

Hermes must preserve the distinction between:

```text
available knowledge
selected knowledge
retrieved knowledge
evidence candidate
Register Candidate
Registre Probatoire entry
```

Hermes must not infer that every user-accessible Knowledge Base is authorized for the current task.

Hermes must not infer that a retrieved item is evidence.

Hermes must not infer that repeated retrieval creates memory.

Hermes must not access OpenWebUI storage directly in normal workflows.

If direct database or vector-store access is ever used for diagnostics or controlled administration, it must be:

- read-only;
- scoped;
- logged;
- restricted to governed views where possible;
- forbidden from writing OpenWebUI data;
- forbidden from writing Pantheon memory;
- forbidden from bypassing approvals.

A governed read-only knowledge gateway may be considered later, but it remains an external capability surface under `EXTERNAL_TOOLS_POLICY.md`.

It must not become a hidden Pantheon runtime or unrestricted Hermes bridge.

## Role and profile binding

Pantheon Roles are governance authorities.

Hermes profiles are execution profiles.

A Hermes profile may align with a Pantheon Role, but it does not inherit governance authority.

Canonical mapping lives in `AGENTS.md`.

If a Hermes profile conflicts with `AGENTS.md`, `AGENTS.md` wins.

Allowed profile behavior:

```text
produce planning candidates
produce source review candidates
produce risk review candidates
produce quality review candidates
produce arbitration candidates
produce formulation candidates
produce patch candidates
```

Forbidden profile behavior:

```text
approve final action
promote canonical memory
mutate governance doctrine without approval
merge code directly
bypass Task Contracts
bypass approval levels
become source of truth
```

## Profile identity layer

A Hermes profile may use a SOUL-like identity layer to stabilize execution posture.

This pattern is reviewed in `reference_reviews/SOUL_MD_HERMES_PROFILE.md`.

Allowed profile identity content:

```text
identity posture
communication tone
uncertainty behavior
pushback behavior
capability-gap behavior
candidate-output discipline
evidence discipline
hard stops
```

Forbidden profile identity content:

```text
Pantheon Role authority
approval authority
memory promotion authority
Task Contract substitution
Evidence Pack substitution
tool authorization
doctrine mutation
hidden policy override
```

A SOUL-like file may shape how Hermes executes.

It must not alter what Hermes is authorized to do.

If a profile identity conflicts with the Task Contract, Context Pack, External Tools Policy, approvals, memory policy or `AGENTS.md`, the governance artifact wins.

Profile identity is execution context.

It is not a Registre Probatoire entry.

It is not approval.

It is not evidence by itself.

It is not a source of truth.

OpenWebUI may expose selected profile identity metadata to the user, such as selected profile, purpose, scope and limits.

Such exposure remains cockpit display only.

## Capability gap signaling

Hermes must surface capability gaps rather than hiding them.

Capability gaps may include:

```text
missing source
missing tool
missing permission
missing context
missing approval
unsupported task
protected area touched
scope exceeds contract
external dependency not verified
```

A capability gap is not failure by itself.

It is a governance signal.

Pantheon may revise the Task Contract, request human approval, reduce scope or reject the task.

## Approval bridge

Hermes may report that approval is required.

Hermes may include approval state received from Pantheon.

Hermes must not create approval.

Hermes must not infer approval from user silence, successful execution, confidence or repeated usage.

Approval remains governed by `APPROVALS.md`.

## Memory bridge

Hermes may propose Register Candidates.

Hermes must not promote memory.

Hermes runtime state must not become Pantheon memory.

Hermes scratchpads, queues, execution traces, tool caches and agent internals must not be stored as a Registre Probatoire entry.

Memory promotion remains governed by `MEMORY.md`.

## Patch and repository mutation

Hermes may produce Patch Candidates when authorized by a Task Contract.

A Patch Candidate is not a merge decision.

Repository mutation remains governed by:

- protected-file rules;
- approval expectations;
- Evidence Pack review;
- actual diff verification;
- human or governance approval where required.

Hermes must not auto-merge.

Hermes must not self-approve doctrine changes.

## Tool use

Hermes may use tools only when the Task Contract and external tools policy allow them.

Tool outputs must be reflected in the Evidence Pack when they affect the result.

Hermes must not install tools, skills or plugins into Pantheon Next.

Hermes must not create a tool runtime inside Pantheon Next.
