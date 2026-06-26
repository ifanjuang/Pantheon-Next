# Architecture Role Facets

Status: candidate — architecture-domain model for role facets, role-owned reflexes, consultations, rites, gates and limits.

This document is not canonical doctrine yet.

It does not implement agents, role executors, multi-agent loops, workflow engine, router, scheduler, queue, message bus, UI, approval engine, memory engine, rite runner, sender, checker, legal review or professional validation.

It defines how roles may be described as multi-faceted guardians in architecture-domain governance.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Roles must not become decorative mythological labels.

They must also not become autonomous agents.

A role is useful only if it has a clear jurisdiction, detection logic, reflexes, limits and coordination behavior.

This document defines a role-facet model for architecture-domain methods.

## Core rule

```text
A role guards a consequence domain.
A role has facets.
A role may emit reflexes.
A role may consult another role.
A role may request a rite.
A role may ask Zeus for arbitration.
A role does not execute, approve automatically, send, memorize canonically or replace the architect.
```

## Role facet model

| Facet | Meaning | Question answered |
|---|---|---|
| Jurisdiction | Domain guarded by the role. | What consequence does this role protect? |
| Detection | Situations the role is sensitive to. | What does this role notice? |
| Disciplines | Standing rules the role watches. | Which constraints does this role enforce? |
| Strategies | Route preferences the role recommends. | How does this role orient the work? |
| Procedures | Ordered checks the role may request. | What sequence may this role ask for? |
| Tactics | Local moves the role may propose. | What small correction can be applied now? |
| Reflexes | Triggered warnings owned by the role. | What alert fires when the domain is threatened? |
| Consultations | Other roles commonly consulted. | Whose view is needed? |
| Rites | Structured tension resolutions the role may request. | What recurring conflict needs a rite? |
| Gates | Status thresholds the role may request or block. | What cannot pass without validation? |
| Output trace | What should appear in the compact response card. | How is the role activity visible? |
| Limit | What the role must not decide alone. | Where does this role stop? |

## Role is not agent

```text
Role = governance lens / guardian.
Agent = execution/runtime behavior.
```

Pantheon roles may classify, warn, request evidence, request review, request a gate, request a rite or propose a tactic.

They must not become hidden workers.

## Role table — candidate architecture set

| Role | Jurisdiction | Primary detection | Reflex examples | Typical tactics | Consults | Gates / rites | Limit |
|---|---|---|---|---|---|---|---|
| Zeus | Status, arbitration, approval ceiling, promotion | Status jump, external action, validation ambiguity | approval-ceiling warning; status-promotion caution; external-action arbitration | classify candidate / to_verify / blocked / gate_required | all | User Decision Gate; status arbitration rite | Does not approve automatically. |
| Athena | Coherence, evidence, reasoning, contradictions | Weak proof, contradiction, overconfident conclusion | contradiction warning; weak-proof warning; overconfidence warning | change “it is true” into “the source states”; ask for source | Mnemosyne, Themis, Apollo | evidence sufficiency check; contradiction rite | Does not decide legal, contractual or memory status alone. |
| Themis | Mission, scope, responsibility, contract | Hors-mission issue, forbidden wording, responsibility implication | mission-boundary warning; responsibility warning; forbidden-wording warning | insert scope limitation; refuse to pronounce; refer to competent party | Iris, Athena, Zeus | mission boundary gate; responsibility rite | Does not replace lawyer, insurer, BET or contract arbitration. |
| Mnemosyne | Memory, recall, project history, prior decisions | Duplicate point, stale recall, unvalidated write | duplicate-memory warning; stale-recall warning; unvalidated-memory-write warning | maintain existing point; cite last CR; mark memory candidate | Athena, Zeus, Hestia | memory / Notion gate; recall reconciliation | Does not canonize memory by itself. |
| Hermes | Handoff, execution boundary, connector/external tool risk | External effect, runtime handoff, connector capability risk | handoff-boundary warning; execution-scope warning; connector-risk warning | prepare draft/handoff; do not send; request governed execution handoff | Zeus, Themis, Athena | external action gate; handoff gate | Does not execute as Pantheon. Execution remains outside. |
| Hephaestus | Production, deliverable structure, readiness | Missing template, incomplete deliverable, wrong granularity | missing-template warning; production-readiness warning; deliverable-structure warning | produce structured candidate; create missing-info slots | Athena, Themis, Apollo | production readiness gate | Does not validate substance. |
| Iris | Expression, tone, external wording, client readability | Ambiguous wording, tone risk, implicit admission | tone-risk warning; ambiguity warning; external-wording caution | soften / sharpen wording; separate facts from requests | Themis, Athena, Apollo | external wording gate | Does not change substance without authority. |
| Hestia | Stable context, project situation, dossier frame | Unknown project, phase, mission, address, status | context-gap warning; wrong-dossier warning; phase-unknown warning | ask 1-3 context questions; build Context Pack Candidate | Mnemosyne, Athena | context sufficiency gate | Does not invent context. |
| Apollo | Clarity, synthesis, decision readability | Dense answer, no verdict, unusable output | unclear-summary warning; decision-card missing warning | produce flash summary; create action card | Iris, Athena, Hephaestus | summary readiness check | Does not simplify away risk. |

## Facet example — Themis

| Facet | Content |
|---|---|
| Jurisdiction | Mission, scope, responsibility, contractual boundary. |
| Detection | Potential prescription, validation, OPC posture, financial acceptance, fault recognition, mission extension. |
| Disciplines | Mission / Responsibility Boundary Discipline. |
| Strategies | Boundary-first reply; competent-party referral; no pronouncement if outside mission. |
| Procedures | Mission scope check; external reply approval path; mission-complement check. |
| Tactics | Limitation wording; “cannot pronounce” posture; request BET / insurer / economist confirmation. |
| Reflexes | Mission-boundary warning; responsibility warning; forbidden-wording warning. |
| Consultations | Iris for wording; Athena for factual accuracy; Zeus for status. |
| Rites | Responsibility rite; formal notice escalation rite; client reproach rite. |
| Gates | External email gate; mission complement gate; responsibility status gate. |
| Output trace | Role: Themis; Reflex: mission-boundary warning; Tactic: limitation wording; Gate: required. |
| Limit | Does not provide legal advice or replace contract / insurer / BET review. |

## Facet example — Mnemosyne

| Facet | Content |
|---|---|
| Jurisdiction | Memory, trace, recall, previous decisions, CR history. |
| Detection | Duplicate observation, stale decision, unsupported memory write, conflict between old and new record. |
| Disciplines | Memory / Notion Write Discipline; Evidence Discipline. |
| Strategies | Latest CR first; last validated decision first; preserve candidate/validated distinction. |
| Procedures | Recall reconciliation; Notion write candidate review; evidence-link check. |
| Tactics | Maintain existing point; mark as updated; ask whether new point or continuation. |
| Reflexes | Duplicate-memory warning; stale-recall warning; unvalidated-memory-write warning. |
| Consultations | Athena for contradiction; Zeus for promotion; Hestia for context. |
| Rites | Memory reconciliation rite; observation closure rite. |
| Gates | Memory gate; Notion write gate; close-point gate. |
| Output trace | Role: Mnemosyne; Reflex: duplicate-memory warning; Proposed action: maintain point instead of duplicate. |
| Limit | Does not make a candidate memory canonical by itself. |

## Facet example — Iris

| Facet | Content |
|---|---|
| Jurisdiction | Expression, tone, readability, external wording. |
| Detection | Ambiguous wording, aggressive tone, implicit admission, overstatement, client misunderstanding. |
| Disciplines | External Action Discipline; Mission Boundary Discipline when wording is external. |
| Strategies | Say less but safer; distinguish fact / request / reservation / next step. |
| Procedures | External wording review; email candidate review. |
| Tactics | Replace dangerous verbs; soften without weakening; add reservation. |
| Reflexes | Tone-risk warning; ambiguity warning; external-wording caution. |
| Consultations | Themis for responsibility; Athena for truth; Apollo for clarity. |
| Rites | Client response rite; external wording tension rite. |
| Gates | External wording gate before sending. |
| Output trace | Role: Iris; Reflex: forbidden ambiguity warning; Tactic: safer formulation. |
| Limit | Does not alter substance to improve tone. |

## Output visibility

When role activity matters, the compact card may show:

```text
Triggered role reflexes:
Consulted roles:
Tactic applied:
Rite requested:
Zeus arbitration:
Gate:
```

The first answer must remain short. Detailed role dialogue is second-layer.

## Anti-patterns

```text
Do not turn roles into autonomous agents.
Do not let every role comment on every request.
Do not use role names as decoration without jurisdiction.
Do not let role consultation become hidden chain-of-thought.
Do not let roles decide outside their limits.
Do not use a reflex to hide a full procedure.
Do not let a tactic become doctrine without review.
```

## Relationship with method taxonomy

This document depends on `ARCHITECTURE_METHOD_TAXONOMY.md`.

The key distinction remains:

```text
Approaches handle work.
Disciplines constrain work.
Strategies choose routes.
Procedures order steps.
Tactics handle local moves.
Roles guard consequence domains.
Reflexes interrupt with necessary cadrage.
Some reflexes are owned by roles.
Gates expose decisions.
The architect decides.
```

## Relationship with role-reflex coordination

This document complements `ARCHITECTURE_ROLE_REFLEX_COORDINATION.md`.

That document explains how role-owned reflexes may consult roles, request rites and invoke Zeus.

This document defines what each role is made of.

## Final rule

```text
A role is a guardian with facets, not a worker.
A role may detect, warn, consult, request, propose and block unsafe status transitions.
It does not execute, approve automatically or replace the architect.
```
