# Workflow Manifest

Status: active doctrine — conceptual stabilization.

A Workflow Manifest is a governed declaration.

It is not an execution graph.

It is not a scheduler object.

It is not a queue definition.

It is not a hidden orchestration layer.

It describes how a class of work should be governed, reviewed, evidenced and approved.

It does not make Pantheon Next execute that work.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Naming and compatibility

This file keeps the historical name `WORKFLOW_SCHEMA.md` for repository compatibility.

The canonical concept is `Workflow Manifest`.

A Workflow Manifest is a governance artifact.

It is not a runtime workflow.

Clarification is preferred over renaming until schema references and governance references are reconciled.

## Purpose

A Workflow Manifest defines reusable governance expectations for a recurring class of work.

It may describe:

- intended use;
- domain scope;
- entry criteria;
- role viewpoints;
- required Task Contracts;
- expected Evidence Packs;
- approval expectations;
- allowed outputs;
- memory rules;
- risk review requirements;
- completion criteria.

It must remain human-readable.

## Core principle

A workflow in Pantheon Next is not what runs.

A workflow is what governs the legitimacy of a repeated process.

Hermes Agent or another external runtime may decide how to operate.

Pantheon Next defines the governance envelope only.

## Minimal structure

A Workflow Manifest should remain structurally small.

Canonical components:

```text
Identity
Purpose
Scope
Entry Criteria
Governed Phases
Role Viewpoints
Task Contract Requirements
Evidence Requirements
Approval Requirements
Allowed Outputs
Memory Rules
Risk Notes
Completion Criteria
```

Anything beyond this requires justification.

## Identity

A Workflow Manifest must define a stable identifier and a clear title.

The identifier is a governance identifier.

It is not a runtime job identifier.

It is not a graph node identifier.

## Purpose

Purpose explains the type of work the workflow governs.

Good purpose:

```text
review quote and CCTP consistency before issuing a recommendation
```

Bad purpose:

```text
run a multi-agent autonomous execution graph
```

## Scope

Scope defines where the workflow applies.

It must define:

- included domains;
- excluded domains;
- authority limits;
- expected inputs;
- expected outputs.

If scope is unclear, the workflow cannot govern reliably.

## Entry criteria

Entry criteria define when the workflow may be used.

Examples:

```text
source documents are available
user intent is clear
protected areas are identified
approval level has been estimated
```

Entry criteria are governance checks.

They are not runtime triggers.

## Governed phases

A Workflow Manifest may describe phases.

Phases are review and governance stages.

They are not executable steps.

A phase may describe:

- purpose;
- responsible role viewpoint;
- expected input;
- expected output;
- evidence expectation;
- approval expectation;
- risk condition.

A phase must not describe:

- worker scheduling;
- queue progression;
- provider routing;
- retry policy;
- runtime state transition;
- tool dispatch.

## Role viewpoints

A workflow may request candidate viewpoints from Pantheon Roles.

Examples:

```text
ATHENA for planning
ARGOS for source review
THEMIS for risk
APOLLO for quality
ZEUS for arbitration
IRIS for formulation
HEPHAISTOS for implementation candidate
```

Roles provide governance perspectives.

They are not autonomous workers inside Pantheon Next.

## Task Contract requirements

A Workflow Manifest may require one or more Task Contracts.

The Task Contract defines the governed execution boundary.

The Workflow Manifest does not replace the Task Contract.

The Workflow Manifest does not authorize execution by itself.

## Evidence requirements

A Workflow Manifest must define the expected Evidence Pack pattern.

It may require:

- assumptions;
- source references;
- risk notes;
- output references;
- review notes;
- memory candidates;
- approval references.

Evidence requirements make the workflow auditable.

They do not create an observability backend.

## Approval requirements

A Workflow Manifest may define expected approval levels.

Approvals validate legitimacy.

Approvals do not make Pantheon execute.

Approval escalation is required when scope, risk, memory effect or external effect increases.

## Allowed outputs

Allowed outputs define artifact categories.

Examples:

```text
review note
risk assessment
context pack
patch candidate
memory candidate
Evidence Pack
```

Allowed outputs are not commands.

They are governance categories.

## Memory rules

A Workflow Manifest must define memory expectations.

Default rule:

```text
workflow outputs are not canonical memory
```

The workflow may propose Memory Candidates.

Only approval can promote Canonical Memory.

## Risk notes

A Workflow Manifest must expose risk conditions.

Examples:

```text
source uncertainty
scope ambiguity
protected area touched
external runtime dependency
memory promotion requested
runtime drift risk
```

Risk notes are part of governance.

They are not failure handling logic.

## Completion criteria

Completion criteria define when a workflow output is reviewable.

Examples:

```text
Evidence Pack produced
risks recorded
approval state recorded
outputs listed
memory candidates marked as candidates
```

Completion does not mean canonization.

Completion does not mean approval.

Completion does not mean external execution succeeded unless evidence supports that claim.

## Relationship to Task Contracts

A Workflow Manifest governs a class of work.

A Task Contract governs a specific task.

A Workflow Manifest may guide Task Contract drafting.

It must not replace task-specific scope, evidence or approval decisions.

## Relationship to Evidence Packs

A Workflow Manifest defines expected proof patterns.

The Evidence Pack records the actual evidence produced for a specific task.

The workflow does not approve its own evidence.

## Relationship to Memory

A Workflow Manifest may allow Memory Candidate proposals.

It must not allow automatic memory promotion.

## Relationship to Hermes Agent

Hermes Agent may use a Workflow Manifest as contextual guidance.

Pantheon Next does not define how Hermes executes internally.

Pantheon Next does not install, schedule or run workflows.

## Relationship to OpenWebUI

OpenWebUI may expose workflow descriptions, approval prompts, evidence and outputs.

OpenWebUI does not make the workflow canonical by displaying it.

OpenWebUI does not execute the workflow for Pantheon Next.

## Relationship to schemas

A future `workflow_manifest.schema.yaml` may validate the structure of Workflow Manifests.

The schema may validate:

- identity;
- scope;
- phase declarations;
- role references;
- evidence requirements;
- approval requirements;
- memory rules;
- risk notes.

The schema must not define:

- execution order as runtime semantics;
- scheduling;
- queueing;
- retry behavior;
- worker assignment;
- provider routing;
- tool dispatch;
- hidden graph state.

## Forbidden drift

Workflow Manifests must never become:

- execution DAGs;
- LangGraph definitions;
- scheduler inputs;
- queue definitions;
- provider routing plans;
- tool-call plans;
- autonomous agent plans;
- hidden orchestration specs;
- self-evolution loops.

If a Workflow Manifest becomes necessary to run the system, governance drift has occurred.

## Governed composition (Héphaïstos forges)

A Workflow Manifest does not have to be written by hand in advance. It may be
*forged* on the fly for a specific cap, then governed like any other manifest.

HÉPHAÏSTOS is the role that forges a recipe. He proposes a Workflow Manifest
candidate by assembling already-declared capabilities (`CAPABILITY_REGISTRY.md`)
into a topology that serves the cap held by MÈTIS (`REQUEST_LIFECYCLE.md`).

The forge proposes a recipe.

It does not run the recipe.

A forged manifest is a candidate. Being forged does not authorize it.

```text
forged != authorized
```

### Composition loop

Composition follows a retrieve / reuse / revise / retain loop. Each step maps to
governance Pantheon already defines; nothing new executes.

```text
RETRIEVE  find eligible capabilities         -> CAPABILITY_REGISTRY.md
REUSE     assemble a Workflow Manifest        -> this document
REVISE    re-read the cap as answers arrive   -> TASK_CONTRACT_REVISIONS.md
RETAIN    a recipe that held becomes reusable -> governed promotion only
```

RETRIEVE selects capabilities by their declared purpose and dependencies, not by
free text matching. REUSE assembles signatures and topology. REVISE is the cap
re-evaluation: a minor within-scope adjustment is noted and continues; a material
change of destination is a governed Task Contract revision, never a silent pivot.
RETAIN never promotes a recipe automatically; a recipe that worked is a candidate
for the library until a domain-scoped review promotes it.

### Two governance gates

A forged manifest passes two gates. Both are governance decisions, not runtime
steps. Pantheon does not execute either gate; it states the status.

```text
GATE 1  pre-execution eligibility
        Before any external execution, ZEUS arbitrates whether the cap and the
        forged manifest are eligible: scope, authority per step, risk class,
        responsibility limit. An ineligible recipe does not proceed.

GATE 2  post-execution evidence
        After the external runtime returns a Result Candidate, the Evidence Pack
        must support each claim (EVIDENCE_PACK.md). A claim that is not supported
        does not become truth. No evidence, no truth.
```

### Per-step signature

Each step in a forged manifest declares a signature: expected inputs, allowed
outputs, forbidden outputs, risk class and authority. A signature is a governance
contract for the step, not a function call. It lets a reviewer read the recipe
without running it.

### Composition boundary

Forged composition must never become an execution layer. It does not introduce a
scheduler, a queue, a provider router, retries or tool dispatch. Those belong
outside Pantheon, in the execution runtime, under Task Contract. The forge
proposes governance structure; it does not operate anything.

```text
HÉPHAÏSTOS forges the recipe.
PANTHEON governs the cap, the proof and the status.
The execution runtime executes outside.
The human engages.
```

## Final rule

A Workflow Manifest exists to govern repeatable work.

Not to execute it.
