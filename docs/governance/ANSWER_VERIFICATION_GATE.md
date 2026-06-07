# Answer Verification Gate

Status: candidate / to verify — central doctrine proposal for memory-first answers, evidence escalation and consequential response status.

This document is doctrine candidate only.

It does not implement a runtime, retrieval layer, checker, approval engine, evidence store, memory engine, scheduler, queue, MCP server, OpenWebUI extension, Hermes skill, database rule or automatic decision system.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next must not turn every remembered statement into a governed record.

Professional work needs a living memory layer. It should be able to recall context, propose associations, detect tensions and answer lightweight questions without forcing every thought through a proof procedure.

The risk is different: memory-based answers can become dangerous when they are presented as verified truth, validated choice, canonical memory or authorized action.

This document defines the gate between:

```text
memory may speak
```

and:

```text
evidence is required before assertion, decision or action
```

## Core doctrine

```text
Free memory is allowed to speak.
Verified evidence is required to assert.
Governed status is required to decide.
Approval is required to act.
```

French operational phrasing:

```text
La memoire peut parler.
La preuve permet d'affirmer.
Le statut permet de decider.
L'approbation permet d'agir.
```

## Architectural shift

The simple flow is insufficient:

```text
Question -> memory -> answer
```

A fully proof-first flow is also too heavy:

```text
Question -> evidence required for everything -> answer
```

The governed flow is:

```text
Question
-> memory-based answer candidate
-> consequence qualification
-> verification when required
-> explicit answer status
```

Pantheon does not govern every answer.

Pantheon governs answers that become consequential.

## Layer separation

The COP, administration cockpit or exposure surface may display these layers together, but they must remain separate.

| Layer | Role | Authority |
|---|---|---|
| Free Memory | Recalls, associates, hypothesizes, detects tensions | No canonical authority |
| Evidence Registry | Records sources, documents, excerpts, dates, versions, authors and proof references | Probative authority |
| Status / Choice Registry | Records the evolution of choices, claims, dependencies and statuses | Procedural authority |
| Approval Layer | Authorizes promotion, delivery or external action | Legitimacy authority |

The memory may suggest.

The evidence may support.

The status may govern.

The approval may authorize.

## Verification levels

Every consequential response should be able to declare its verification level.

| Level | Name | Source posture | Allowed use |
|---|---|---|---|
| V0 | free | memory, session context or reasoning only | brainstorming, informal orientation |
| V1 | memory-based | memory recalls a prior context but no evidence is attached | low-risk reminder with explicit caution |
| V2 | to verify | memory or retrieved context suggests an answer but evidence is missing or incomplete | working hypothesis, not decision-ready |
| V3 | evidence-verified | answer is supported by identified evidence references | reviewable assertion, subject to status |
| V4 | approved | evidence, status and required approval are present | delivery, promotion or external action within scope |

The gate does not forbid V0 or V1 answers.

It forbids presenting V0, V1 or V2 as V3 or V4.

## Consequence levels

The verification requirement depends on possible consequence.

| Consequence level | Description | Minimum posture |
|---|---|---|
| C0 | casual thought, ideation, style, non-binding wording | V0 allowed |
| C1 | low-risk reminder or orientation | V1 allowed with visible qualifier |
| C2 | useful claim that could affect work but does not yet commit the dossier | V2 minimum; evidence recommended |
| C3 | claim that affects truth, cost, scope, compliance, status or coordination | V3 required |
| C4 | decision, memory promotion, delivery, instruction or external action | V4 required |

Approval level names remain owned by `APPROVALS.md`; this document only defines the answer-verification posture.

## Gate questions

Before a memory-based response is treated as reliable, the gate asks:

```text
1. Is the answer merely conversational or exploratory?
2. Could it create a false project truth?
3. Could it change a choice, status, cost, scope, deadline or responsibility?
4. Could it reactivate an obsolete or superseded memory?
5. Could it contradict a validated status?
6. Could it trigger or justify an external action?
7. Could a professional rely on it in a way that creates liability?
```

If the answer to all consequence questions is no, memory may answer freely.

If any answer is yes, the response must escalate to evidence, status and possibly approval.

## Answer status object

The cockpit or runtime may represent the result with a reviewable status object.

Specification only. This is not an executable schema.

```yaml
answer_status:
  source_mode: memory_based | retrieved_context | evidence_pack | approved_record
  verification_level: V0_free | V1_memory_based | V2_to_verify | V3_evidence_verified | V4_approved
  consequence_level: C0 | C1 | C2 | C3 | C4
  evidence_required: true | false
  evidence_refs: []
  status_refs: []
  approval_required: true | false
  approval_ref: null
  confidence_note: "Memory suggests this, but no evidence has been attached yet."
  allowed_use: brainstorming | working_hypothesis | reviewable_assertion | approved_action
```

The shape above is a documentary contract candidate. Any executable schema must be proposed separately under the protected `schemas/` path and requires explicit approval.

## Examples

### Lightweight memory answer

```text
The client seemed interested in a continuous terrace.
```

Allowed posture:

```text
V1 memory-based.
Use: low-risk reminder.
Qualifier: d'apres memoire / to verify before design decision.
```

### Consequential assertion

```text
The continuous terrace is validated in the project.
```

Required posture:

```text
V3 evidence-verified minimum.
Evidence: client email, meeting report, validated plan or decision record.
```

### External action

```text
Send the modified plan to the contractor.
```

Required posture:

```text
V4 approved.
Evidence: current drawing, recipient scope, delivery status, approval reference.
```

## Memory, evidence and status are not interchangeable

A memory can remember that a client mentioned abandoning a pool.

That memory is not proof.

The Evidence Registry may contain a dated email or meeting report confirming the abandonment.

The Status / Choice Registry may then record:

```text
pool: validated -> abandoned
pool heat pump: candidate -> obsolete
terrace compatibility: candidate -> to verify
foundation assumption linked to pool: to verify -> to arbitrate
```

The registry records the transition.

The memory may keep the whole history.

A contradiction does not erase history; it opens a transition to qualify.

## Relationship to existing doctrine

### Relationship to `MEMORY.md`

`MEMORY.md` governs Memory Candidates and Canonical Memory.

This document adds a response-level gate before memory is used as an assertion.

Free memory may support V0 and V1 answers. Canonical Memory remains governed by `MEMORY.md`.

No automatic memory promotion is introduced.

### Relationship to `EVIDENCE_PACK.md`

`EVIDENCE_PACK.md` governs the proof package produced after external execution.

This document defines when an answer must escalate from memory-based response to evidence-supported assertion.

Evidence remains governed justification, not runtime activity.

### Relationship to `CAPABILITY_PLACEMENT.md`

The gate follows the placement rule:

```text
If this goes wrong, can it produce a false truth,
an unapproved external effect,
a wrong memory,
an invalid approval,
an illegitimate scope expansion,
or an unauthorized action?
```

When yes, Pantheon governs the decision.

The execution still belongs outside Pantheon.

### Relationship to domain packs

Domain packs should define professional triggers that raise the required verification level.

Examples:

```text
architecture: budget, surface, regulatory compliance, client validation, contractor instruction
law: deadline, jurisdiction, legal position, filing, client advice
medicine: diagnosis, medication, urgent symptom, patient instruction
accounting: tax treatment, filing obligation, financial statement claim
```

A domain pack may adjust risk triggers and delivery gates, but it must not lower the general rule that consequential assertions require evidence.

## COP display rule

The COP must not collapse memory, evidence and status into one object.

It may display them together only if their authority remains visible.

Minimum display posture:

```text
answer text
verification level
consequence level
memory signals used
attached evidence refs
current status refs
approval state
allowed use
remaining uncertainty
```

The COP is a cockpit of qualification.

It is not the memory itself.

It is not the Evidence Registry.

It is not the approval authority.

## Forbidden drift

This doctrine must not become:

- a universal proof requirement for every answer;
- a hidden runtime classifier;
- an automatic approval engine;
- an automatic memory promotion engine;
- a replacement for `MEMORY.md`;
- a replacement for `EVIDENCE_PACK.md`;
- a database schema by implication;
- a COP implementation spec;
- a reason to store hidden chain-of-thought;
- a way to treat memory as proof.

## Final rule

```text
Memory first.
Evidence when consequential.
Status when deciding.
Approval when acting.
```

The validated remains.
