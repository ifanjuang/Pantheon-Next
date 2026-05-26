# Module Activation

Status: active support doctrine — modular activation and effective policy only.

This document defines how Pantheon Next should reason about detected, enabled and task-authorized modules or capabilities.

It does not implement a UI.

It does not implement a module registry.

It does not implement plugin loading.

It does not implement runtime behavior.

It does not authorize automatic installation, automatic activation, automatic execution, automatic approval or automatic memory promotion.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next should remain modular without becoming a plugin manager.

Future UI work may need to show whether a capability is available, disabled, enabled for a scope, suspended, rejected or authorized for a specific task.

This document defines the governance vocabulary for that UI.

It answers:

```text
If a capability is detected, what rules become effective before it can be used?
```

## Core distinction

```text
Detected does not mean enabled.
Enabled does not mean authorized for a task.
Authorized for a task does not mean sovereign.
```

A capability may exist in Hermes, OpenWebUI or an external environment without being governed for use by Pantheon.

## Module meaning

A Pantheon module is a governance area or governed capability declaration.

It is not:

- runtime package;
- plugin;
- installed skill;
- autonomous agent;
- tool dispatcher;
- scheduler;
- queue;
- provider router;
- memory engine;
- approval engine.

A module may define:

- status;
- scope;
- rules;
- required artifacts;
- forbidden actions;
- risk classes;
- UI exposure expectations;
- Hermes candidate constraints;
- OpenWebUI cockpit controls;
- evidence expectations;
- memory implications.

## Three-stage model

Every activable capability should be evaluated through three stages.

```text
capability detection
→ governance activation
→ task authorization
```

### 1. Capability detection

Detection reports that a capability exists somewhere.

Examples:

- Hermes detects that LangGraph is installed in a sandbox;
- OpenWebUI has a Function available;
- a Knowledge Base exists;
- a connector is configured;
- a candidate skill is present in a Hermes directory;
- a reference review exists.

Detection must not authorize use.

### 2. Governance activation

Activation means Pantheon has a governed policy for using a detected capability within a defined scope.

Activation may be:

- disabled;
- sandbox only;
- project-scoped;
- dossier-scoped;
- domain-scoped;
- organization-scoped;
- suspended;
- rejected.

Activation must define mandatory rules and optional switches.

### 3. Task authorization

Task authorization means a specific Task Contract permits use of the capability for a specific task.

A capability may be detected and enabled but still unauthorized for the current task.

Task authorization requires scope fit, approval fit, allowed tool fit, memory fit and evidence fit.

## Status vocabulary

Recommended statuses:

```text
unavailable
detected
disabled
watch
candidate
sandbox_enabled
project_enabled
dossier_enabled
domain_enabled
organization_enabled
task_authorized
suspended
deprecated
rejected
```

## Status semantics

| Status | Meaning |
|---|---|
| unavailable | not detected or not available |
| detected | available somewhere, not enabled |
| disabled | deliberately unavailable for use |
| watch | interesting but not ready for activation |
| candidate | reviewed as possible future activation |
| sandbox_enabled | allowed only for sandbox or fictional/non-critical tasks |
| project_enabled | allowed for a named project under conditions |
| dossier_enabled | allowed for a named dossier under conditions |
| domain_enabled | allowed for a domain of work under conditions |
| organization_enabled | allowed broadly, rare and high-governance |
| task_authorized | allowed for the current Task Contract only |
| suspended | temporarily blocked pending review |
| deprecated | should be phased out |
| rejected | forbidden under current doctrine |

## Activation scope

Activation must be scoped.

Allowed scope levels:

```text
session
task
dossier
project
domain
user
organization
system
```

Default posture:

```text
no global activation by default
```

System-level activation should remain rare and should not disable mandatory rules.

## Mandatory rules

Mandatory rules are automatically effective when a capability is enabled.

They are not optional UI switches.

They cannot be disabled merely for convenience.

Common mandatory rules:

```yaml
mandatory_rules:
  task_contract_required: true
  context_pack_required_when_external_execution: true
  evidence_pack_return_required: true
  approval_ceiling_required: true
  scope_required: true
  memory_rule_required: true
  external_tool_policy_required: true
  canonical_memory_write_forbidden_by_default: true
  automatic_approval_forbidden: true
  automatic_memory_promotion_forbidden: true
  doctrine_mutation_forbidden_without_review: true
  raw_runtime_trace_is_not_evidence: true
  runtime_state_is_not_canonical_memory: true
  user_decision_gate_required_for_unresolved_conflict: true
```

## Optional rules

Optional rules may be activated or deactivated within a governed scope.

They must not override mandatory rules.

Examples:

```yaml
optional_rules:
  allow_checkpoint_resume: true_or_false
  allow_streaming_status: true_or_false
  allow_human_interrupts: true_or_false
  allow_limited_retry: true_or_false
  allow_read_only_tools: true_or_false
  allow_write_tools: true_or_false_with_approval
  allow_patch_candidate_workflow: true_or_false
  allow_rag_ingestion_workflow: true_or_false
  allow_repo_analysis_workflow: true_or_false
  allow_sandbox_execution: true_or_false
  allow_project_execution: true_or_false
```

## Effective Policy

An Effective Policy is the computed governance posture for a capability at a given moment.

It answers:

```text
Given what is detected, enabled, scoped and requested, what is actually allowed now?
```

Recommended structure:

```yaml
module_id: langgraph_runtime_candidate
capability_class: hermes_runtime_candidate

detection:
  detected: true
  detected_by: hermes
  version: unknown
  health: unknown
  last_checked: null

governance_activation:
  status: sandbox_enabled
  scope: project
  approved_by: user_or_admin
  approval_level: C2
  review_after: null

task_authorization:
  task_contract_required: true
  context_pack_required: true
  allowed_for_current_task: false
  denial_reason: no_task_contract

mandatory_rules:
  task_contract_required: true
  context_pack_required: true
  evidence_pack_required: true
  memory_candidate_only: true
  automatic_approval_forbidden: true

optional_rules:
  checkpoint_resume: false
  streaming_status: true
  human_interrupts: true
  limited_retry: false

forbidden:
  pantheon_runtime: true
  openwebui_runtime: true
  canonical_memory_write: true
  auto_approval: true
```

Effective Policy is a governance artifact.

It is not a runtime engine.

## UI control model

A future OpenWebUI cockpit may expose module controls.

Allowed controls:

- view detection status;
- view effective policy;
- enable for sandbox;
- enable for project;
- enable for dossier;
- disable;
- suspend;
- request review;
- require approval;
- show evidence;
- show risk;
- show capability gaps;
- show last Evidence Pack;
- restore previous governance status.

Forbidden controls:

- bypass mandatory rules;
- grant automatic approval;
- promote memory;
- mutate doctrine;
- install plugins automatically;
- install skills automatically;
- start hidden runtime jobs;
- grant broad OpenWebUI Knowledge access;
- grant write tools without approval;
- turn detection into authorization.

## Layer split

| Layer | Role in activation |
|---|---|
| Pantheon | defines statuses, mandatory rules, optional rules, scopes, approvals and effective policy |
| Hermes | detects and executes capabilities only when task-authorized |
| OpenWebUI | displays status, controls, evidence, approvals and User Decision Gates |

## Capability classes

Recommended classes:

```text
governance_module
hermes_runtime_candidate
hermes_skill_candidate
openwebui_cockpit_template
openwebui_capability_surface
evidence_template
memory_policy
approval_gate
external_tool_candidate
reference_review
read_only_doctor_candidate
```

Each class may have its own mandatory rules.

## LangGraph example

LangGraph is a Hermes runtime candidate.

Detection:

```text
Hermes may detect LangGraph availability.
```

Mandatory rules if enabled:

```yaml
task_contract_required: true
context_pack_required: true
evidence_pack_return_required: true
approval_ceiling_required: true
memory_promotion_forbidden: true
pantheon_runtime_forbidden: true
openwebui_runtime_forbidden: true
direct_openwebui_db_access_forbidden: true
raw_trace_is_not_evidence: true
graph_state_is_runtime_state: true
user_decision_gate_required_for_unresolved_conflict: true
```

Optional rules:

```yaml
allow_checkpoint_resume: true_or_false
allow_streaming_status: true_or_false
allow_human_interrupts: true_or_false
allow_limited_retry: true_or_false
allow_patch_candidate_workflow: true_or_false
allow_rag_ingestion_workflow: true_or_false
allow_repo_analysis_workflow: true_or_false
```

UI meaning:

```text
Enable LangGraph for project
```

must mean:

```text
Hermes may use LangGraph only for task-authorized work in this project, under mandatory Pantheon rules.
```

It must not mean:

```text
LangGraph becomes Pantheon workflow engine.
```

## Suspension

A capability should be suspended when:

- evidence is missing;
- scope was exceeded;
- external effect occurred without approval;
- memory boundary was violated;
- runtime trace cannot be explained;
- tool behavior changed;
- dependency changed materially;
- user trust or professional risk is affected;
- a User Decision Gate blocks continuation.

Suspension is reversible only through governed review.

## Detection record

A detection record should be factual and non-authorizing.

Recommended fields:

```yaml
capability_id: langgraph
capability_class: hermes_runtime_candidate
detected: true
detected_by: hermes
detected_where: hermes_sandbox
version: unknown
health: unknown
last_checked: null
notes: available_but_not_task_authorized
```

## Activation record

An activation record should be scoped and reviewable.

Recommended fields:

```yaml
module_id: langgraph_runtime_candidate
status: sandbox_enabled
scope_type: project
scope_id: example_project
approved_by: user_or_admin
approval_level: C2
mandatory_rules_ref: docs/governance/MODULE_ACTIVATION.md
optional_rules:
  checkpoint_resume: false
  streaming_status: true
  human_interrupts: true
review_after: null
```

## Task authorization record

A task authorization record should be specific to a Task Contract.

Recommended fields:

```yaml
task_contract_id: TC-000
module_id: langgraph_runtime_candidate
authorized: true
reason: long_running_interruptible_evidence_workflow
scope_match: true
approval_ceiling: C3
allowed_tools:
  - read_only_repo_inspection
forbidden_tools:
  - external_write
  - canonical_memory_write
  - doctrine_mutation
required_return:
  - output_candidate
  - run_trace_summary
  - evidence_notes
  - memory_candidates_if_any
```

## Relationship to MODULES.md

`MODULES.md` defines governance areas.

This document defines activation semantics for capabilities that may be detected, enabled, disabled or task-authorized.

A module remains governance-first even when a related external capability is enabled.

## Relationship to external references

External references may suggest module candidates or optional capabilities.

They must pass through:

```text
WATCHLIST.md
REFERENCE_BOUNDARIES.md
ECOSYSTEM_MAP.md
DISTILLATION_REGISTRY.md or REJECTED_PATTERNS.md
TENSIONS_AND_RISKS.md when needed
```

A reference review is not an activation.

## Relationship to approvals

Activation may require approval depending on scope and risk.

Task authorization may require a different approval depending on the concrete action.

Approval to enable a capability does not approve every future use.

## Relationship to memory

No module activation may create Canonical Memory by itself.

A capability may produce Memory Candidates only when allowed by Task Contract and memory policy.

## Relationship to evidence

No module activation may treat logs, traces, scores, retrieved sources or successful completion as Evidence Pack by themselves.

Activated capabilities must return evidence material in a reviewable form.

## Forbidden drift

Module activation must never become:

- plugin marketplace;
- skill marketplace;
- automatic installer;
- provider router;
- workflow runtime;
- scheduler;
- queue;
- hidden agent loop;
- automatic approval engine;
- automatic memory engine;
- OpenWebUI capability sprawl;
- Hermes authority bypass;
- Pantheon runtime migration.

## Final rule

```text
Pantheon detects capabilities to apply policy.
It does not detect capabilities to execute them.
```