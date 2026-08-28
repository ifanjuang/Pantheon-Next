# Request Coordination

Status: active doctrine — conceptual stabilization.

This file keeps the historical name `REQUEST_ORCHESTRATION.md` for repository compatibility.

The canonical concept is `Request Coordination`.

Request Coordination is governance-side classification, attention routing, review sequencing and escalation guidance.

It is not runtime orchestration.

It is not a scheduler.

It is not a queue.

It is not a message bus.

It is not a workflow runner.

It is not a LangGraph runtime.

```text
Optional runtime clients may expose interaction.
Hermes Agent executes external admitted work.
Pantheon Cockpit projects governed intake, review and decision state.
Pantheon Next governs.
The human decides consequential effects.
```

## Purpose

Request Coordination helps Pantheon Next decide how a user request should be governed before it is delegated to an external runtime or reviewed as documentation.

It may help identify:

- user intent;
- scope;
- domain;
- risk;
- protected areas;
- required role viewpoints;
- Task Contract need;
- Evidence Pack expectations;
- approval level;
- memory rules;
- output category;
- escalation conditions.

Request Coordination organizes governance attention.

It does not execute the request.

## Naming and compatibility

The word `orchestration` is legacy vocabulary.

It must not be read as runtime orchestration.

Pantheon Next should prefer:

```text
Request Coordination
Governance Intake
Review Sequencing
Escalation Guidance
```

The file name may remain until repository references are reconciled.

## Core principle

Coordination is not execution.

Pantheon Next may coordinate review logic.

Pantheon Next must not coordinate runtime workers.

Pantheon Next may decide what governance artifacts are required.

Pantheon Next must not become the system that performs the work.

## Minimal structure

A Request Coordination note may contain:

```text
Request Summary
Intent
Scope
Domain
Risk
Protected Areas
Suggested Role Viewpoints
Task Contract Need
Evidence Expectations
Approval Estimate
Memory Rules
Output Expectations
Escalation Conditions
```

Anything beyond this requires justification.

## Intake classes

A request may be classified as one or more of the following:

```text
clarification
analysis
source review
governance review
implementation candidate
quality review
arbitration
formulation
memory candidate review
```

These are governance classifications.

They are not commands.

They are not worker assignments.

They are not runtime steps.

## Coordination path

A normal governance path may be described as:

```text
Intake
Scope check
Risk check
Role viewpoints
Task Contract
Evidence expectations
Approval estimate
Memory rules
Output review
```

This path is documentary.

It is not executable.

It does not define a scheduler, a graph or a dispatcher.

## Role viewpoints

Request Coordination may suggest role viewpoints.

Examples:

```text
ATHENA for decomposition
ARGOS for source review
THEMIS for risk and approvals
APOLLO for quality
ZEUS for arbitration
IRIS for formulation
HEPHAISTOS for implementation candidate
```

Suggested role viewpoints are candidate review perspectives.

They are not autonomous agent launches.

They do not self-approve.

They do not self-canonize.

## Task Contract need

Request Coordination may determine that a Task Contract is required.

A Task Contract is required when execution, external effects, repository mutation, protected areas, memory proposals or significant risk are involved.

Request Coordination may guide the contract draft.

It does not replace the Task Contract.

## Evidence expectations

Request Coordination may define expected evidence before work begins.

Examples:

```text
source references required
assumptions must be listed
risk notes required
output references required
approval state required
memory candidates must remain candidates
```

Evidence expectations guide review.

They do not create runtime tracing.

## Approval estimate

Request Coordination may estimate an approval level.

The estimate is not the approval.

Approval remains governed by `APPROVALS.md`.

When uncertainty exists, escalate.

## Memory rules

Request Coordination must identify whether memory behavior is relevant.

Default rule:

```text
no canonical memory by default
```

A request may allow Register Candidate proposals.

It must not allow automatic memory promotion.

## Output expectations

Request Coordination may identify expected output categories.

Examples:

```text
answer
review note
Evidence Pack
Task Contract draft
risk note
patch candidate
memory candidate
context pack
```

Output categories are not commands.

They are review expectations.

## Escalation conditions

Escalate when:

- scope is unclear;
- evidence is missing;
- risk is non-trivial;
- protected areas are touched;
- memory promotion is requested;
- doctrine may change;
- external effects are possible;
- runtime drift is detected;
- role candidates conflict.

Escalation is a governance action.

It is not a runtime interrupt.

## Relationship to Workflow Manifests

A Workflow Manifest governs a recurring class of work.

Request Coordination governs the intake and review path of a specific request.

Request Coordination may select or reference a Workflow Manifest.

It must not execute the workflow.

## Relationship to Task Contracts

Request Coordination may lead to a Task Contract.

The Task Contract defines the governed execution boundary.

Request Coordination does not authorize execution by itself.

## Relationship to Evidence Packs

Request Coordination may define expected evidence.

The Evidence Pack records actual evidence.

A coordination note does not prove anything by itself.

## Relationship to Approvals

Request Coordination may estimate approval level and escalation need.

Approval remains a distinct governance decision.

Coordination cannot approve itself.

## Relationship to Memory

Request Coordination may identify memory relevance.

It may require that outputs remain Register Candidates.

It must not promote memory.

## Relationship to Hermes Agent

Hermes Agent may receive coordination context through a Task Contract or Context Pack.

Pantheon Next does not define Hermes internal execution sequence.

Pantheon Next does not spawn Hermes workers.

Pantheon Next does not run the coordination path.

## Relationship to runtime clients and Cockpit

An optional runtime client, including Hermes WebUI if separately selected and qualified, may expose intake questions, technical interaction and candidate outputs.

Pantheon Cockpit may project governed coordination notes, Evidence gaps, approval prompts and linked decisions.

Neither client display nor Cockpit projection canonizes the coordination result, grants approval or transfers authority.

```text
Hermes WebUI available != Hermes WebUI selected
client display != authority
projection != persistence
```

## Relationship to schemas

A future schema may validate Request Coordination notes.

It may validate:

- request summary;
- scope;
- risk;
- role viewpoint suggestions;
- evidence expectations;
- approval estimate;
- memory rules;
- escalation conditions.

It must not validate runtime orchestration behavior.

It must not define worker assignment, queue progression, scheduling, provider routing, graph state or tool dispatch.

## Forbidden drift

Request Coordination must never become:

- runtime orchestration;
- agent dispatcher;
- scheduler;
- queue manager;
- message bus;
- provider router;
- hidden LangGraph;
- automatic role spawning;
- automatic memory promotion;
- self-evolution loop.

If Request Coordination becomes necessary to run the system, governance drift has occurred.

## Final rule

Request Coordination organizes governance attention.

It does not orchestrate execution.
