# OpenWebUI Templates

Status: active support doctrine — cockpit templates and dependency exposure only.

This document defines how future OpenWebUI surfaces may expose Pantheon governance without becoming governance authority or runtime.

It does not implement OpenWebUI templates.

It does not implement OpenWebUI Functions, Tools, Pipes, Filters, Actions or Pipelines.

It does not authorize plugin installation.

It does not create a module registry.

It does not create a UI runtime.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

OpenWebUI should expose the governance state of Pantheon in a way users can understand and act on.

Future UI templates should show:

- what is enabled;
- what is disabled;
- what is blocked by dependencies;
- what rules are mandatory;
- what options are activable;
- what evidence is visible;
- what approval is required;
- what memory implication exists;
- what cannot be done because a parent module is disabled.

OpenWebUI must not make the underlying governance true.

It only exposes governed state and captures user decisions.

## OpenWebUI technical boundary

OpenWebUI supports Functions, Tools and Pipelines that can extend the product.

This matters because some of those extension points execute code or expose tool surfaces.

Pantheon must treat them as capability surfaces, not as governance authority.

OpenWebUI cockpit templates should prefer non-executable display and decision surfaces before any Function, Tool, Pipe, Filter, Action or Pipeline is considered.

## Core rule

```text
OpenWebUI templates make governance visible.
They do not make governance true.
```

Operational version:

```text
OpenWebUI may display, collect, label, select, warn and ask.
OpenWebUI must not execute, approve, canonize, promote memory or expand scope.
```

## Relationship to Module Activation

`MODULE_ACTIVATION.md` defines detection, activation, task authorization and Effective Policy.

This document defines how those states may be exposed to users.

A UI control must not bypass the Effective Policy.

A UI toggle must not disable mandatory rules.

A UI state must not grant runtime authority.

## Dependency hierarchy principle

Some modules are parent modules.

Disabling a parent module must automatically disable, block or degrade dependent child functions.

This is not runtime execution.

It is governance visibility.

```text
Parent disabled
→ child blocked
→ UI explains why
→ user may request review or reactivation
```

A dependency block should preserve traceability.

It should not silently disappear.

## Dependency state vocabulary

Recommended UI dependency states:

```text
available
enabled
disabled_by_user
blocked_by_parent
blocked_by_scope
blocked_by_missing_evidence
blocked_by_missing_approval
blocked_by_policy
blocked_by_capability_gap
suspended_by_risk
read_only_degraded
hidden_by_confidentiality
rejected
```

## Dependency record

A dependency record should remain declarative.

Recommended fields:

```yaml
module_id: approval_prompt
parent_modules:
  - evidence_pack_display
  - task_contract_display
requires:
  - visible_object_under_review
  - visible_evidence_state
  - approval_level
blocks_when_parent_disabled: true
fallback_ui: show_dependency_blocker
user_action:
  - request_review
  - enable_parent_if_allowed
  - narrow_scope
```

## Parent module hierarchy

Recommended high-level hierarchy:

```text
Pantheon Cockpit Root
├─ Task Contract Surface
│  ├─ Intake Template
│  ├─ Scope Review Template
│  ├─ Context Pack Template
│  └─ Hermes Dispatch Template
├─ Knowledge and Source Surface
│  ├─ Source Selection Template
│  ├─ Knowledge Scope Template
│  ├─ Source Freshness Template
│  └─ Retrieved Knowledge Review Template
├─ Evidence Surface
│  ├─ Evidence Pack Display Template
│  ├─ Evidence Completeness Template
│  ├─ Contradiction Template
│  └─ Run Trace Summary Template
├─ Decision Surface
│  ├─ Approval Prompt Template
│  ├─ User Decision Gate Template
│  ├─ Delivery Gate Template
│  └─ External Transmission Gate Template
├─ Memory Surface
│  ├─ Memory Candidate Review Template
│  ├─ Scope-limited Memory View Template
│  └─ Canonical Memory Read Template
├─ Module Control Surface
│  ├─ Module Status Template
│  ├─ Effective Policy Template
│  ├─ Dependency Graph Template
│  └─ Suspension Review Template
└─ Runtime Candidate Surface
   ├─ Hermes Status Template
   ├─ LangGraph Run Status Template
   ├─ Human Interrupt Template
   └─ Capability Gap Template
```

## Parent disable effects

| Parent | Disabled effect |
|---|---|
| Task Contract Surface | Blocks Hermes dispatch and approval prompts for consequential tasks. |
| Knowledge and Source Surface | Blocks Evidence Pack completion and source-based approvals. |
| Evidence Surface | Blocks approval, delivery, memory promotion and external transmission. |
| Decision Surface | Blocks validation, delivery and external effect. |
| Memory Surface | Blocks memory promotion and memory edits. |
| Module Control Surface | Blocks user-side activation changes but not read-only status display. |
| Runtime Candidate Surface | Blocks runtime status display and resume controls, but not Evidence Pack review. |

These are UI-level governance effects.

They are not runtime enforcement.

## Mandatory blockers

Certain blockers must be automatic and non-overridable from normal UI controls.

```yaml
mandatory_blockers:
  no_task_contract:
    blocks:
      - hermes_dispatch
      - runtime_candidate_use
      - approval_prompt_for_consequential_task
  no_context_pack:
    blocks:
      - hermes_dispatch_with_external_context
      - langgraph_run_start
  no_visible_evidence:
    blocks:
      - approval_prompt
      - memory_candidate_approval
      - external_transmission
  no_approval_level:
    blocks:
      - approval_capture
      - external_effect
  memory_policy_missing:
    blocks:
      - memory_candidate_review
      - memory_promotion
  parent_suspended_by_risk:
    blocks:
      - child_activation
      - external_effect
  unresolved_user_decision_gate:
    blocks:
      - delivery
      - external_transmission
      - memory_promotion
```

## Template anatomy

Every OpenWebUI template should define:

```yaml
template_id: evidence_pack_display
surface: openwebui
module_class: cockpit_template
status: support_doctrine_only
parent_modules:
  - evidence_surface
depends_on:
  - task_contract_display
  - source_selection
use_when:
  - evidence_material_exists
do_not_use_when:
  - no_task_contract
  - no_visible_output_candidate
may_capture:
  - user_request_more_evidence
  - user_mark_source_irrelevant
  - user_request_revision
must_not_capture_as:
  - canonical_memory
  - automatic_approval
  - doctrine_update
mandatory_rules:
  - display_evidence_state
  - display_limitations
  - display_approval_state
fallback_when_blocked: dependency_blocker
```

## Core cockpit templates

### 1. Intake Template

Purpose: collect user intent and help prepare a Task Contract Candidate.

Must expose:

- request;
- expected output;
- dossier or project;
- sensitivity;
- source availability;
- external effect expectation;
- memory sensitivity.

Must not start execution by itself.

Dependencies:

```yaml
parent: task_contract_surface
requires:
  - user_request
blocks_children_if_disabled:
  - scope_review
  - context_pack
  - hermes_dispatch
```

### 2. Scope Review Template

Purpose: show what is in scope, out of scope and uncertain.

Must not expand scope by implication.

Dependencies:

```yaml
parent: task_contract_surface
requires:
  - task_contract_candidate
blocks_children_if_disabled:
  - context_pack
  - hermes_dispatch
  - approval_prompt
```

### 3. Source Selection Template

Purpose: expose selected sources, Knowledge Items and exclusions.

Must not treat retrieval as evidence.

Dependencies:

```yaml
parent: knowledge_source_surface
requires:
  - source_or_knowledge_candidates
blocks_children_if_disabled:
  - evidence_pack_completion
  - source_based_approval
```

### 4. Context Pack Template

Purpose: show bounded context before Hermes execution.

Must not become memory or Task Contract substitute.

Dependencies:

```yaml
parent: task_contract_surface
requires:
  - scope_review
  - selected_sources_when_needed
blocks_children_if_disabled:
  - hermes_dispatch
  - runtime_candidate_use
```

### 5. Hermes Dispatch Template

Purpose: let the user request external execution under Task Contract.

Must not execute inside OpenWebUI.

Dependencies:

```yaml
parent: task_contract_surface
requires:
  - task_contract
  - context_pack
  - approval_ceiling
  - allowed_tools
blocks_when_missing:
  - task_contract
  - context_pack
```

### 6. Evidence Pack Display Template

Purpose: display evidence, assumptions, risks, limitations and output status.

Must not approve the output.

Dependencies:

```yaml
parent: evidence_surface
requires:
  - output_candidate
  - evidence_notes_or_pack
blocks_children_if_disabled:
  - approval_prompt
  - delivery_gate
  - memory_candidate_review
  - external_transmission_gate
```

### 7. Run Trace Summary Template

Purpose: expose Hermes or LangGraph run state as review material.

Must not treat raw trace as evidence.

Dependencies:

```yaml
parent: evidence_surface
requires:
  - run_trace_summary
  - task_contract
blocks_when_missing:
  - evidence_mapping
fallback: show_trace_not_evidence_warning
```

### 8. Approval Prompt Template

Purpose: capture explicit approval, rejection or request for more evidence.

Must show object, scope, evidence state and approval level.

Dependencies:

```yaml
parent: decision_surface
requires:
  - task_contract_display
  - evidence_pack_display
  - approval_level
blocks_when_missing:
  - visible_evidence
  - approval_level
```

### 9. User Decision Gate Template

Purpose: expose unresolved conflict to the user.

Must show options and consequences.

Dependencies:

```yaml
parent: decision_surface
requires:
  - conflict_object
  - role_positions_or_risk_positions
  - options
blocks_children_until_resolved:
  - delivery_gate
  - external_transmission_gate
  - memory_promotion
```

### 10. Delivery Gate Template

Purpose: distinguish draft, candidate, validated deliverable and transmitted output.

Must not transmit externally by itself.

Dependencies:

```yaml
parent: decision_surface
requires:
  - evidence_state
  - approval_state
  - output_status
blocks_when_missing:
  - approval_required_but_missing
  - unresolved_user_decision_gate
```

### 11. External Transmission Gate Template

Purpose: expose send, publish, file, deploy or notify decisions.

Must require explicit approval for external effect.

Dependencies:

```yaml
parent: decision_surface
requires:
  - delivery_gate
  - approval_state
  - recipient_or_external_target
blocks_when_missing:
  - delivery_approval
  - external_effect_approval
```

### 12. Memory Candidate Review Template

Purpose: review a Memory Candidate.

Must not promote memory by display.

Dependencies:

```yaml
parent: memory_surface
requires:
  - memory_candidate
  - evidence_pack_display
  - scope
  - risk
blocks_when_missing:
  - visible_evidence
  - scope
  - approval_level
```

### 13. Module Status Template

Purpose: show detected, enabled, disabled, suspended or rejected capabilities.

Must not activate anything by itself.

Dependencies:

```yaml
parent: module_control_surface
requires:
  - module_activation_record_or_detection_record
child_templates:
  - effective_policy
  - dependency_graph
  - suspension_review
```

### 14. Effective Policy Template

Purpose: show the computed governance posture for a module.

Must not enforce policy by itself.

Dependencies:

```yaml
parent: module_control_surface
requires:
  - detection_state
  - activation_state
  - task_authorization_state
blocks_children_if_disabled:
  - module_enable_controls
  - runtime_candidate_controls
```

### 15. Dependency Graph Template

Purpose: show parent and child relationships.

Must explain why a feature is blocked.

Dependencies:

```yaml
parent: module_control_surface
requires:
  - module_dependency_record
must_show:
  - parent_status
  - child_status
  - blocker_reason
  - allowed_user_actions
```

### 16. LangGraph Run Status Template

Purpose: expose a Hermes LangGraph candidate run.

Must not host LangGraph.

Dependencies:

```yaml
parent: runtime_candidate_surface
requires:
  - task_contract
  - context_pack
  - langgraph_effective_policy
  - hermes_run_status
blocks_when_missing:
  - task_authorization
  - context_pack
  - evidence_return_path
```

### 17. Human Interrupt Template

Purpose: expose a runtime interrupt requiring human input.

Must not treat a click as approval unless approval fields are explicit.

Dependencies:

```yaml
parent: runtime_candidate_surface
requires:
  - interrupt_reason
  - visible_options
  - risk_effects
  - approval_implications
routes_to:
  - user_decision_gate_when_conflict_exceeds_runtime_choice
```

### 18. Capability Gap Template

Purpose: show that Hermes or a runtime candidate cannot proceed.

Must not auto-install missing capabilities.

Dependencies:

```yaml
parent: runtime_candidate_surface
requires:
  - capability_gap
  - affected_task
  - recommended_next_action
blocks_children_if_unresolved:
  - execution_resume
  - delivery_gate
```

## Dependency matrix

| If disabled | Blocks |
|---|---|
| Intake | Scope, Context Pack, Hermes dispatch |
| Scope Review | Context Pack, Hermes dispatch, approval |
| Source Selection | Evidence completion, source-based approval |
| Context Pack | Hermes dispatch, runtime candidates |
| Evidence Pack Display | Approval, delivery, memory review, transmission |
| Decision Surface | Approval, delivery, transmission |
| User Decision Gate | Delivery, transmission, memory promotion |
| Memory Surface | Memory review and promotion |
| Effective Policy | Runtime candidate controls |
| Runtime Candidate Surface | Run status and resume controls |

## Degraded mode

When a parent is disabled, a child template may enter degraded mode instead of disappearing.

Degraded mode should show:

- disabled parent;
- blocker reason;
- missing artifact;
- risk;
- allowed next action;
- forbidden next action.

Example:

```text
Approval Prompt unavailable.
Reason: Evidence Pack Display is disabled.
Allowed: request evidence review.
Forbidden: approve output without visible evidence.
```

## UI control rules

Allowed UI controls:

- show status;
- show blocker;
- show dependency graph;
- request review;
- enable parent if policy allows;
- disable module;
- suspend module;
- request more evidence;
- narrow scope;
- escalate User Decision Gate;
- cancel external execution request.

Forbidden UI controls:

- bypass parent dependency;
- disable mandatory rule;
- approve without visible evidence;
- promote memory directly;
- install plugin;
- install skill;
- start runtime job without Task Contract;
- grant broad OpenWebUI Knowledge access;
- turn Native Mode into global agentic execution for Pantheon;
- treat Function, Tool, Pipe, Filter, Action or Pipeline availability as authorization.

## OpenWebUI extension warning

OpenWebUI extension points are powerful.

For Pantheon, any future Function, Tool, Pipe, Filter, Action or Pipeline must be reviewed under `EXTERNAL_TOOLS_POLICY.md` and `MODULE_ACTIVATION.md` before use.

Default posture:

```text
templates first
thin actions later
runtime never inside OpenWebUI by default
```

If an Action Function is ever used, it should be a thin cockpit action such as:

- request Hermes execution;
- show status;
- request pause;
- request resume;
- cancel candidate run;
- open Evidence Pack.

It must not contain Pantheon governance logic or LangGraph runtime logic.

## Native Mode boundary

Native or agentic tool calling may be useful in OpenWebUI.

For Pantheon workflows, it must not be globally enabled with broad tools, memory, Knowledge and web access by default.

Allowed posture:

```text
scoped task
declared tools
declared memory rule
declared evidence requirement
approval ceiling
```

Forbidden posture:

```text
global agentic mode
unbounded Knowledge access
unbounded memory access
write tools without approval
auto-selected tools as authority
```

## Effective Policy display example

```yaml
module_id: langgraph_runtime_candidate
ui_surface: langgraph_run_status
parent_surface: runtime_candidate_surface
status: blocked_by_missing_context_pack

detection:
  detected: true
  detected_by: hermes

governance_activation:
  status: sandbox_enabled
  scope: project

task_authorization:
  authorized: false
  reason: context_pack_missing

mandatory_rules_active:
  - task_contract_required
  - context_pack_required
  - evidence_pack_return_required
  - memory_promotion_forbidden
  - openwebui_runtime_forbidden

optional_rules_available:
  - checkpoint_resume
  - streaming_status
  - human_interrupts

blocked_children:
  - resume_run
  - approve_run_output
  - memory_candidate_review

allowed_user_actions:
  - create_context_pack_candidate
  - request_scope_review
  - cancel_run_request
```

## Relationship to future implementation

A future implementation may translate these templates into UI components.

That implementation must remain separate from this document and must not be assumed to exist.

If future implementation requires code, schemas, operations or Docker changes, the protected-file confirmation rules apply.

## Final rule

```text
A disabled parent must make its children visibly unavailable.
A visible child must never imply its parent is satisfied.
```