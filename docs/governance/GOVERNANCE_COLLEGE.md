# Governance College

Status: active doctrine — role separation, governed tension and procedural arbitration.

This document defines the Pantheon Governance College.

It clarifies why Pantheon Roles are separated, how they create useful disagreement, and how conflicts become reviewable governance decisions.

It does not add a runtime.

It does not add agents.

It does not add a message bus.

It does not add orchestration.

It does not add a scheduler, queue, LangGraph runtime, hidden workflow runner, automatic memory system or autonomous decision loop.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core thesis

Pantheon does not multiply agents.

Pantheon separates responsibilities of judgment.

The Greek figures are not autonomous workers.

They are governance roles, magistratures and controlled viewpoints.

Their value is not that they all help.

Their value is that they may disagree usefully.

```text
A role has value only if it can reveal, preserve or escalate a useful tension.
```

## Why separate roles

A single assistant often produces a smooth answer.

A smooth answer may hide weak sources, unresolved contradictions, premature delivery, broad memory claims or scope drift.

Pantheon separates roles to prevent that collapse.

The separation exists to distinguish:

```text
well structured
well sourced
well verified
well written
well fabricated
well transmitted
well arbitrated
well approved
well remembered
```

These are not the same state.

A text may be clear and still unsafe.

A deliverable may be produced and still not be deliverable.

A source may be retrieved and still not be evidence.

A memory proposal may be useful and still be too broad.

## College model

Pantheon Roles form a governance college.

A governance college is a set of separated review functions that can apply different pressures to the same task.

It is not a multi-agent runtime.

It is not a committee that talks forever.

It is a structured way to surface tensions before approval.

```text
Exploration may be flexible.
Review must be disciplined.
Validation must remain explicit.
```

## Roles, rites and Agora

Pantheon Roles carry stable responsibilities of judgment.

Rites organize temporary shared methods between roles.

Agora is the visible deliberation space where positions, tensions and unresolved conflicts may be exposed.

These layers must not collapse into each other.

```text
Roles judge.
Rites coordinate.
Agora deliberates.
ZEUS arbitrates status and procedure.
The human decides.
```

A rite may call ATHENA, ARGOS, THEMIS, APOLLO, HEPHAISTOS, IRIS or ZEUS in a defined order.

That order is a governance method, not an execution graph.

A rite may help Agora structure a disagreement.

It must not replace Agora when human legitimacy, professional preference, value conflict or explicit arbitration is required.

A rite may produce:

```text
option clusters
contradiction notes
source concordance notes
hidden-premise notes
refoundation notes
ZEUS status
User Decision Gate recommendation
```

A rite must not produce:

```text
runtime execution
automatic approval
hidden role debate
automatic memory promotion
external action without Task Contract and approval
```

## Role biases

Each role carries a useful bias.

The bias is not a defect.

It is a controlled deformation that makes one class of risk visible.

| Role | Useful bias | Risk if unchecked |
|---|---|---|
| ATHENA | order, structure, decomposition | over-simplification or premature abstraction |
| ARGOS | sources, versions, provenance, traceability | slowing the task or drowning the output in references |
| THEMIS | risk, contradiction, policy, approval boundary | excessive blocking or over-caution |
| APOLLO | clarity, completeness, readability, delivery quality | making fragile conclusions look too smooth |
| HEPHAISTOS | fabrication, patch, artifact, concrete output | producing before the task is legitimate to deliver |
| IRIS | transmission, formatting, recipient adaptation | sending or exposing material too early |
| ZEUS | status arbitration and procedure selection | over-centralized decision if trace is poor |

A role must not hide its bias.

A role should expose what its bias detected and what it may be missing.

## Negative powers

A role is not defined only by what it can produce.

It is also defined by what it can prevent.

This is the governance value of the college.

| Role | May propose | May challenge | May block or escalate |
|---|---|---|---|
| ATHENA | structure, plan, decomposition | unclear scope, incoherent sequence | scope too broad or task not framed |
| ARGOS | source map, provenance notes, traceability | missing source, stale source, wrong version | source gap, unsupported claim, unknown provenance |
| THEMIS | risk review, approval boundary, contradiction status | unsafe conclusion, policy breach, liability risk | blocking contradiction, trust-boundary risk, approval mismatch |
| APOLLO | clarity review, completeness review, delivery readiness note | confusing output, missing section, tone mismatch | delivery-readiness failure when meaning or evidence is unclear |
| HEPHAISTOS | artifact candidate, patch candidate, build note | impractical deliverable, missing implementation condition | unsafe build, unreviewed mutation, premature production |
| IRIS | transmission candidate, recipient wording, format | unclear recipient, channel mismatch, over-disclosure | external transmission before approval |
| ZEUS | arbitration candidate, status decision, next procedure | unresolved disagreement, competing variants | no valid procedure, escalation required |

No role may self-promote its conclusion into a Registre Probatoire entry.

No role may bypass approval.

No role may treat its own output as final truth.

## Governed tension

A governed tension is an explicit disagreement between legitimate requirements.

Pantheon should preserve these tensions instead of smoothing them away.

Common tensions:

```text
clarity versus precision
speed versus proof
production versus approval
retrieval versus evidence
memory versus confidentiality
source breadth versus scope isolation
generalization versus dossier specificity
synthesis versus contradiction
external action versus human validation
```

A tension is not a failure.

A tension is review material.

It should be marked, classified and either resolved, carried with a warning or escalated.

## Dissent statuses

Roles should not only produce prose.

They should return a status when reviewing candidate work.

Recommended statuses:

```text
ok
ok_with_reserve
source_insufficient
scope_too_broad
contradiction_detected
risk_detected
delivery_premature
transmission_blocked
memory_forbidden
memory_candidate_possible
approval_required
escalation_required
```

These statuses make disagreement machine-readable without making it executable runtime state.

They are review signals, not dispatch commands.

## Activation proportionality

The full college must not be activated for every task.

Pantheon should use the minimum effective governance required by risk, scope, external effect and memory impact.

```text
low risk      -> one role may be enough
medium risk   -> two or three roles may review
high risk     -> several roles plus arbitration
critical risk -> full review, Evidence Pack and explicit approval
```

Examples:

| Task type | Suggested review |
|---|---|
| simple reformulation | APOLLO or IRIS |
| plan or outline | ATHENA + APOLLO |
| source-backed synthesis | ATHENA + ARGOS + APOLLO |
| quote versus specification analysis | ATHENA + ARGOS + THEMIS + HEPHAISTOS + ZEUS |
| external professional communication | ARGOS + THEMIS + APOLLO + IRIS + human approval |
| memory promotion | ARGOS + THEMIS + ZEUS + explicit memory approval |
| doctrine change | THEMIS + ZEUS + human approval, with evidence or review note |

The rule is:

```text
More risk means more college.
More external effect means stronger approval.
More durable memory means stronger evidence and narrower scope.
```

## Procedural arbitration

ZEUS does not decide truth.

ZEUS decides status, risk posture and next procedure when roles conflict.

Possible arbitration outcomes:

```text
proceed_as_draft
proceed_with_reserve
request_source
request_user_clarification
narrow_scope
split_task
escalate_approval
block_delivery
block_transmission
reject_memory_candidate
allow_memory_candidate_review
```

ZEUS must not erase dissent.

If a contradiction remains, the trace must keep it visible.

## Status over truth

Pantheon should avoid asking whether an AI output is simply true.

The more useful question is:

```text
What is the governance status of this claim?
```

Recommended claim statuses:

```text
unsupported
source_needed
sourced_not_verified
sourced_coherent
sourced_but_contradicted
assumption_only
usable_for_draft
blocked_for_delivery
validated_for_scope
memory_candidate
canonical_memory
superseded
revoked
obsolete
```

Pantheon does not make AI an oracle.

Pantheon makes claim status visible.

## Contradiction tribunal

Contradictions should not be smoothed into a clean answer.

For serious tasks, Pantheon should preserve a contradiction ledger.

A contradiction record may include:

```text
contradiction_id
claim_a
source_a
claim_b
source_b
conflict_type
severity
detected_by
resolution_status
human_decision
impact_on_output
impact_on_memory
```

Useful conflict types:

```text
source_conflict
version_conflict
scope_conflict
legal_or_policy_conflict
technical_conflict
professional_practice_conflict
delivery_conflict
memory_conflict
```

Contradiction preservation is a core differentiator.

Most AI systems optimize for smoothness.

Pantheon should optimize for reviewable friction.

## Economy of doubt

Pantheon should not sell certainty.

It should qualify doubt.

Types of useful doubt:

```text
source_doubt
version_doubt
scope_doubt
calculation_doubt
legal_or_policy_doubt
professional_doubt
recipient_doubt
memory_doubt
freshness_doubt
```

Every doubt should suggest a next action:

```text
find_source
check_version
ask_user
narrow_scope
mark_assumption
preserve_contradiction
block_delivery
escalate_approval
reject_memory
schedule_review_note
```

Doubt is useful only when it changes the next procedure.

## Slowdown rule

Pantheon is not only an acceleration layer.

It must know when to slow down.

Slowdown is required when:

```text
source is missing
version is uncertain
scope is expanding
external action is requested
memory is proposed
professional liability may be affected
contradiction remains unresolved
approval level is unclear
```

This may be represented narratively by time, thresholds or review gates.

No new canonical role is introduced by this document.

## Production versus delivery

Pantheon must preserve the distinction between producing an artifact and authorizing its use.

```text
produced
ready_for_review
usable_for_draft
validated_for_delivery
transmitted
memory_candidate
canonical_memory
```

A produced artifact may still be blocked for delivery.

A clear artifact may still be unsupported.

A transmitted artifact may still not become memory.

HEPHAISTOS may fabricate.

IRIS may prepare transmission.

THEMIS, ZEUS and human approval govern whether the artifact may be delivered or retained.

## Anti-collusion rule

The roles must not collapse into mutual agreement by default.

If several roles review the same task, their outputs should preserve distinct responsibility.

Avoid:

```text
all roles restate the same conclusion
all roles praise the output
all risks softened into style comments
all contradictions converted into recommendations
```

Prefer:

```text
role-specific status
role-specific risk
role-specific missing condition
role-specific next action
explicit unresolved dissent
```

## Relationship to Task Contracts

A Task Contract should indicate which role viewpoints are relevant to the task.

Role activation should be proportional to risk.

The Task Contract may ask for a specific viewpoint, but it must not create runtime agents inside Pantheon.

## Relationship to Evidence Packs

Evidence Packs should preserve role-relevant findings when they affect output legitimacy.

Examples:

- ARGOS source gap;
- THEMIS contradiction;
- APOLLO delivery-readiness reserve;
- IRIS transmission warning;
- ZEUS arbitration outcome.

Evidence Packs must not include hidden chain-of-thought or raw scratchpad.

## Relationship to Run Trace View

A Run Trace View may show role statuses, tensions, contradictions and arbitration outcomes.

It must not become runtime state.

It must not replay the role process.

It must not expose hidden chain-of-thought.

## Relationship to Memory

A role may propose memory review.

No role may promote memory alone.

Memory promotion requires explicit scope, evidence linkage and approval under `MEMORY.md` and `SCOPE_ISOLATION.md`.

## Relationship to Hermes

Hermes may execute role-aligned profiles under Task Contract.

Those profiles produce candidates.

They do not become Pantheon Roles.

They do not hold Pantheon authority.

They do not self-approve.

## Relationship to Rites

Rites may coordinate several roles around a recurring methodological tension.

They remain governed methods.

They are not role authorities.

They are not Hermes profiles.

They are not executable workflow manifests.

They are not Run Trace Views.

A rite may be exposed through Agora, OpenWebUI or an Evidence Pack when its result affects review, delivery, memory or arbitration.

## Final rule

Pantheon does not seek to eliminate uncertainty.

Pantheon makes uncertainty visible, qualified and arbitrable.

```text
AI opens possibilities.
Roles organize tensions.
Rites coordinate methods.
Evidence constrains.
ZEUS arbitrates status and procedure.
The human decides.
The validated remains.
```
