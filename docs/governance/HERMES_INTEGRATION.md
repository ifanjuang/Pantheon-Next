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

## Kernel and Hermes adapter boundary

Hermes version changes are adapter events by default.

They do not rewrite the Pantheon kernel unless they reveal a missing tool-agnostic governance distinction.

```text
Pantheon kernel:
  truth status
  memory status
  approval status
  evidence status
  scope status
  external-action legitimacy
  capability placement

Hermes adapter:
  profiles
  skills
  tools
  MCP connections
  subagents
  background tasks
  automation blueprints
  messaging channels
  runtime memory mechanics
  dashboard controls
  execution traces
```

The kernel states what may become true, remembered, approved, transmitted or retained.

The Hermes adapter maps each Hermes feature to that kernel.

Hermes may express more runtime power without Pantheon becoming more runtime-like.

## Consequential effects route through Pantheon — the chokepoint

This is the rule that makes Pantheon master in fact, not only in advice (see `UNIFORM_CAPABILITY_GOVERNANCE.md`). In Policy Decision Point / Policy Enforcement Point terms, Pantheon is the PDP and Hermes is the PEP.

```text
Before producing a consequential effect, Hermes asks Pantheon's policy check.
A consequential effect is one that, if wrong, can produce a false truth, an
unapproved external action, a wrong register entry, an invalid approval or an
illegitimate scope expansion (the placement test, AUTHORITY_INDEX.md).
```

Routing rule:

```text
Non-consequential effect (display, format, draft, helper) -> Hermes proceeds freely.
Consequential effect -> Hermes requests the policy check first; it proceeds only
  on an allow / allow_with_gate decision, under the capability passport's
  required_envelope: task_contract_in -> candidate_out -> evidence_pack_out.
```

The decision is data, not execution. Pantheon returns allow, allow_with_gate, block, needs_revision, needs_evidence or needs_approval; it never runs the capability, selects a provider or sends anything.

A consequential effect that reaches the world without passing this check is a bypass. A bypassable check makes Pantheon master only in advice. Hermes honouring the check is what makes Pantheon master in fact.

```text
Hermes may install or host a capability (skill, function, plugin, MCP tool) in its
own runtime, in Langfuse or behind OpenWebUI.
The moment that capability would produce a consequential effect, it resolves
through Pantheon's check. No per-capability rule is added; the passport carries
the specifics, the check is the same for all.
```

This is the doctrine of the chokepoint. Wiring it (the Phase 3 consumption in `MCP_POLICY_SERVER_CANDIDATE.md`) lives in the execution runtime, outside Pantheon.

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
Evidence Pack Candidate
Patch Candidate
Register Candidate
Capability Gap
Risk Escalation
Review Note
Output Artifact Reference
Outcome Observation Candidate
Runtime Trace Reference
```

All returned artifacts remain candidates until governed review is complete.

Hermes done does not mean Pantheon approved.

Hermes output does not become canonical memory.

Hermes evidence does not approve itself.

Hermes transport success does not mean task success.

Hermes task success does not mean governance success.

## Hermes 0.17 runtime surface review

Hermes Agent v0.17 increases runtime reach. Pantheon does not absorb that reach. It maps each new surface to the existing governance model.

| Hermes 0.17 surface | Placement | Pantheon rule |
|---|---|---|
| Background / async subagents | execution runtime | may run under Task Contract; result returns as candidate with trace references; no silent scope expansion |
| Live subagent watch windows | exposure / runtime visibility | observability aid only; streamed activity is not Evidence Pack or approval |
| Image edit through `image_generate` | execution runtime | may create Output Artifact Reference; architectural, legal or client-facing use remains candidate until reviewed |
| Automation Blueprints | execution runtime configuration | may schedule or parameterize runtime work outside Pantheon; Pantheon owns eligibility, approval and external-effect rules, not scheduling |
| Dashboard profile builder | runtime administration | profile creation does not create Pantheon Role authority or tool authorization |
| Skills Hub previews and security scan | runtime capability surface | installation and security scan do not equal capability approval; manifest/passport and Task Contract still govern consequential use |
| Memory batch operations | runtime memory mechanic | may propose Register Candidates or memory edits; cannot promote canonical memory, even atomically |
| iMessage / WhatsApp / Telegram / Raft channels | external communication surfaces | inbound items are source candidates; outbound items are external effects and require approval where consequential |
| Remote media and attachments | runtime transport | context minimization, source admission and scope isolation still apply |
| Secure dashboard login | runtime hardening | authentication improvement does not replace governance, approval or evidence requirements |

Default posture:

```text
More Hermes reach -> more adapter mapping.
Not more Pantheon runtime.
```

## Version-change review rule

Every major Hermes version change is reviewed against the same table before use in governed workflows.

```text
hermes_version_change_review:
  hermes_version:
  changed_surface:
  effect_class: read_only | internal_state_change | external_effect | canonical_effect
  task_contract_required:
  evidence_pack_candidate_required:
  approval_required:
  memory_candidate_allowed:
  adapter_change_required:
  kernel_change_required: false by default
  decision: accepted | refused | to_verify | to_arbitrate
```

Kernel change is exceptional.

A Hermes feature requires a kernel change only if the existing concepts of truth, memory, approval, evidence, scope, external effect or capability placement cannot classify it.

If the feature can be classified, it belongs in the Hermes adapter.

## Task Contract bridge

Hermes execution must be bounded by a Task Contract when the task includes:

- repository mutation;
- external tools;
- protected areas;
- memory proposals;
- policy-sensitive work;
- doctrine-sensitive work;
- non-trivial risk;
- externally visible effects;
- background or delegated subagent work that may affect a governed output;
- automation blueprints that may trigger repeated or delayed work.

The Task Contract defines the governance envelope.

Hermes may choose how to operate internally, but only within that envelope.

If execution requires a broader scope than the contract allows, Hermes must report a scope gap rather than expanding the task silently.

## Background subagent bridge

Background subagents are runtime workers.

They may continue work after the initiating turn, but they do not change the status of what they produce.

Minimum return discipline:

```text
background_subagent_result:
  linked_task_contract:
  delegated_scope:
  runtime_task_status: success | partial | failed | blocked | unknown
  produced_candidates:
  evidence_refs:
  trace_refs:
  scope_gaps:
  approval_still_required:
  memory_promotion_allowed: false
```

A background result is not accepted merely because it re-enters the conversation later.

Any result that affects truth, memory, external action, repository mutation or professional status returns to the User Decision Gate or governed review path.

## Automation blueprint bridge

Hermes Automation Blueprints are executable runtime affordances.

Pantheon may define non-executable blueprint expectations, activation conditions and approval requirements.

Hermes may hold the runnable automation.

```text
Pantheon owns:
  whether the automation is legitimate;
  what scope it may use;
  what evidence it must return;
  what approvals are needed before external effects;
  what may remain as memory.

Hermes owns:
  schedule mechanics;
  runtime invocation;
  retries;
  channel delivery;
  tool execution;
  implementation-specific configuration.
```

A scheduled automation is still bounded by the original Task Contract or by a renewed one when scope, source policy, tool permissions or external-effect status changes.

## Messaging-channel bridge

Hermes may receive or send through channels such as WhatsApp, Telegram, iMessage or an agent network.

Inbound content is source material, not proof.

Outbound content is an external effect unless it is explicitly draft-only.

Required distinctions:

```text
received_message -> source candidate
prepared_reply -> draft / Result Candidate
approved_send -> external effect with approval reference
sent_message -> Outcome Observation Candidate
```

Hermes must not infer professional approval from the fact that the user is chatting in the same channel.

A user saying yes in a channel may be an approval signal only if the relevant User Decision Gate, scope, recipient, effect, revision and approval level are unambiguous and recorded.

## Memory batch bridge

Hermes runtime memory mechanics may improve how Hermes edits its own memory store.

That does not change Pantheon memory rules.

```text
Hermes memory operation -> runtime state or Register Candidate proposal.
Pantheon memory promotion -> governed validation path only.
```

Atomic batch operations may make proposals safer at the runtime level, but they do not make those proposals canonical.

A batch may include add, replace or remove candidates only if each proposed memory effect carries scope, evidence, source, reason and approval requirement.

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

Dashboard-created profiles, imported skills and MCP attachments remain runtime configuration. They do not alter this binding.

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
adapter_version_unreviewed
background_result_unlinked
channel_effect_unclassified
automation_scope_expired
memory_candidate_unscoped
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

## Boundary phrase

```text
Hermes may gain reach.
Pantheon does not become the engine.
The adapter maps the reach.
The kernel governs the consequence.
```
