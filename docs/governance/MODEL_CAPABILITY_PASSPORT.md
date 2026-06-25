# Model Capability Passport

Status: active support doctrine — model-specific passport specialization under uniform capability governance.

This document defines the governance passport for a model, model provider, model-serving surface or model-selection adapter when it is used for consequential professional work.

It specializes the general capability-passport rule. It does not replace `UNIFORM_CAPABILITY_GOVERNANCE.md`, `CAPABILITY_PLACEMENT.md`, `EXTERNAL_TOOLS_POLICY.md`, `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`, `APPROVALS.md` or `MEMORY.md`.

It is a declaration and review shape, not an implementation.

It does not create a provider router, model router, benchmark runner, model registry, evaluation harness, runtime, MCP host, OpenWebUI configuration, Hermes skill, scheduler, queue, installer, approval engine, memory engine or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A model being available does not mean it is appropriate for every professional task.

The same question may carry different risk depending on:

```text
model source
local or external processing
data exposure
retention unknowns
context capacity
modality
known failure modes
cost / latency constraints
professional-use ceiling
source and evidence requirements
approval requirement
```

The Model Capability Passport makes those conditions explicit before a runtime uses a model for consequential work.

## Core rule

```text
Model available does not mean model appropriate.
Model selected does not mean output approved.
Model confidence does not mean evidence.
```

A model may produce a Result Candidate. It may help prepare an Evidence Pack Candidate. It must not approve, validate, canonize, promote memory, resolve professional responsibility or authorize external action.

## Relationship to the universal capability passport

Pantheon uses one rulebook and one passport concept for every capability. A model is a capability.

The model passport adds model-specific fields to the uniform capability passport:

```text
base capability passport
+ model identity
+ serving posture
+ data exposure
+ modality
+ context limits
+ task-family suitability
+ professional-use ceiling
+ known failure modes
+ evidence and approval requirements
```

The governance gate remains the same:

```text
Task Contract
-> runtime uses model
-> Result Candidate + Evidence Pack Candidate
-> passport check + evidence + scope + approval ceiling
-> human decision
```

## When a model passport is required

A model passport is required when model use may affect:

```text
a professional answer
source interpretation
document analysis
regulatory or contractual claim
client-facing draft
external communication
memory proposal
repository or dossier mutation
financial, legal, architectural, medical, engineering or safety-relevant judgment
```

For low-risk drafting or formatting with no external effect and no truth claim, a light model declaration may be sufficient.

## Passport fields

Minimum fields:

```text
model_capability_passport:
  model_id:
  display_name:
  version_or_release:
  provider_or_runtime:
  local_or_external:
  serving_surface:
  adapter_ref:
  status: candidate | sandbox | project_enabled | organization_enabled | deprecated | rejected
  modality:
  context_window:
  input_classes_allowed:
  input_classes_forbidden:
  output_classes_allowed:
  output_classes_forbidden:
  data_exposure:
  retention_or_training_unknowns:
  sensitive_data_allowed: false by default
  authorized_task_families:
  forbidden_task_families:
  professional_use_ceiling:
  evidence_expectation:
  citation_or_source_expectation:
  known_failure_modes:
  uncertainty_behavior:
  comparison_required:
  approval_ceiling:
  memory_behavior:
  fallback_model_or_path:
  review_date:
  reviewed_by:
  decision: accepted | refused | to_verify | to_arbitrate
```

This is not an executable schema. If a schema is later needed, it belongs under `schemas/` and requires explicit approval before modification.

## Local, external and hybrid posture

Model processing posture must be classified:

```text
processing_posture:
  local_only
  external_api
  self_hosted_remote
  organization_hosted
  hybrid
  unknown
```

The posture affects data minimization and approval, not truth.

A local model can still be wrong. An external model can still be useful. A self-hosted model can still be overbroad or unsafe. Processing posture is a risk signal, not a validation signal.

## Data exposure

Minimum data-exposure classes:

```text
data_exposure:
  public_only
  supplied_non_sensitive
  project_sensitive
  client_private
  regulated_or_confidential
  secrets_or_credentials
  unknown
```

Default rule:

```text
Use the smallest context that can satisfy the Task Contract.
Do not send secrets or unnecessary private material to a model.
Do not treat local processing as automatic permission to over-share.
```

## Task-family suitability

The passport must declare task families.

Example vocabulary:

```text
task_family:
  brainstorming
  rewriting
  summarization
  translation
  source_extraction
  document_review
  plan_or_image_interpretation
  code_generation
  professional_risk_review
  regulatory_research
  contractual_analysis
  client_facing_draft
  external_action_preparation
  memory_candidate_preparation
```

Each task family should map to:

```text
allowed | allowed_with_evidence | allowed_with_human_review | sandbox_only | forbidden
```

## Professional-use ceiling

A model passport must state the highest status the model output may reach without additional review.

Allowed ceilings:

```text
draft_only
candidate_only
to_verify
supporting_analysis
reviewed_support
never_final_by_model
```

Default:

```text
never_final_by_model
```

No model output becomes professional validation by model choice alone.

## Evidence expectation

The passport must say what a reviewable model output must carry.

Minimum expectation for consequential work:

```text
source references where applicable
assumptions
uncertainties
known limits
freshness requirement where applicable
contradictions surfaced
output status
human review requirement
```

For source-dependent answers:

```text
retrieval is not evidence
citation display is not proof
evidence supports
approval validates
```

## Known failure modes

The passport must name known failure modes relevant to use.

Examples:

```text
hallucinated citations
overconfident synthesis
poor table extraction
weak spatial reasoning
weak code execution reasoning
poor legal freshness
poor numerical reliability
language mismatch
privacy exposure risk
instruction-following over source discipline
prompt-injection susceptibility through untrusted context
```

This list is not exhaustive. It is a review prompt.

## Comparison and escalation

A passport may require comparison when stakes are high.

Comparison is required when:

```text
the answer affects professional responsibility;
the source set is contradictory;
the model is outside its proven task family;
the result will support external communication;
the output may become a Register Candidate;
the model has known weakness for the requested modality.
```

Comparison produces a Comparison Candidate. It does not validate the result.

## Approval behavior

Approval ceiling must align with `APPROVALS.md` and the Task Contract.

Default mapping:

```text
C0 -> casual drafting / no consequence
C1 -> internal candidate preparation
C2 -> source-grounded internal review
C3 -> professional draft needing explicit human review
C4 -> external communication or project mutation support
C5 -> doctrine-sensitive, confidential, privileged or high-stakes use
```

The model passport never lowers the approval required by the task.

## Memory behavior

Default memory behavior:

```text
model output may become Register Candidate only if the Task Contract allows it
model output does not become canonical memory
model choice does not validate memory
model conversation history is not Registre Probatoire
```

Any memory promotion remains governed by `MEMORY.md` and the applicable approval path.

## Runtime and adapter placement

The passport lives in Pantheon as governance declaration.

Runnable configuration lives outside Pantheon:

```text
model download -> runtime / adapter
model serving -> runtime / adapter
model routing -> runtime / adapter
provider key handling -> runtime / adapter
benchmark execution -> runtime / adapter
UI selection -> exposure surface
passport display -> exposure surface
passport decision -> Pantheon gate
```

Pantheon defines whether the model is admissible for a task. It does not serve the model.

## Safe defaults

If the model passport is missing or incomplete:

```text
candidate-only output
no external effect
no memory promotion
no professional finalization
no sensitive data by default
comparison or human review required when consequential
surface the capability gap
```

## Boundary phrase

```text
The model proposes.
The passport constrains.
The evidence supports.
The approval validates.
The human decides.
```
