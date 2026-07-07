# OpenWebUI Integration

Status: active doctrine — integration boundary stabilization.

OpenWebUI is the user cockpit for Pantheon Next.

OpenWebUI exposes.

It does not govern.

It does not execute Pantheon doctrine.

It does not canonize knowledge or memory.

It does not become the source of truth.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

This document defines the governance boundary between Pantheon Next and OpenWebUI.

It describes what OpenWebUI may display, request, collect and transmit in a governed Pantheon workflow.

It is not an OpenWebUI installation guide.

It is not a plugin specification.

It is not a function, pipe, filter, action or pipeline runtime specification.

It is not a provider configuration guide.

It is not a Docker, environment variable or endpoint document.

## Canonical boundary

OpenWebUI is the cockpit surface.

Pantheon Next is the governance layer.

Hermes Agent is the execution runtime.

OpenWebUI may expose the interaction between user, governance artifacts, evidence and candidate outputs.

OpenWebUI must not become the place where governance truth is created silently.

## Allowed OpenWebUI surfaces

OpenWebUI may expose:

```text
chat interaction
user intent capture
source upload or source reference
Knowledge Base consultation
Task Contract display
rite proposal display
rite status display
rite review note display
approval prompt
approval response capture
Evidence Pack display
Run Trace View display
candidate output display
Register Candidate display
Registre Probatoire entry excerpt display
revision request
escalation request
final delivery display
```

These are cockpit surfaces.

They are not governance authority by themselves.

## Display is not authority

Displaying an artifact in OpenWebUI does not make it canonical.

Displaying a Knowledge Base result does not make it memory.

Displaying an Evidence Pack does not approve the evidence.

Displaying a candidate output does not validate the output.

Displaying a role viewpoint does not make it an approved decision.

Displaying a rite status does not execute, approve or complete the rite.

Authority comes from governed approval, evidence and memory rules.

## User action capture

OpenWebUI may capture user actions such as:

```text
approve
reject
request revision
request more evidence
escalate
mark source relevant
mark source irrelevant
accept delivery
reject delivery
```

A user action is governance-relevant only when the record is clear enough.

The record should identify:

- what was approved or rejected;
- who acted, when available;
- when the action occurred;
- what scope the action covered;
- which evidence was visible;
- which approval level was involved;
- whether memory promotion was included or excluded.

A vague click is not enough for high-risk approval.

Approval remains governed by `APPROVALS.md`.

## Knowledge Base rule

OpenWebUI Knowledge Bases are consultable Knowledge.

They are not a Registre Probatoire entry.

They are not a source of truth by default.

They may support:

- retrieval;
- user context;
- evidence discovery;
- drafting;
- source comparison;
- task scoping.

They must not silently create:

- a Registre Probatoire entry;
- policy updates;
- doctrine updates;
- user preference memory;
- project memory;
- workflow truth.

A Knowledge Base item may become a source in an Evidence Pack.

It may become a Register Candidate if the task and approval rules allow it.

It does not become memory merely because it was uploaded, indexed, embedded, retrieved or repeatedly used.

## Governed Knowledge handoff to Hermes

OpenWebUI may organize user-side folders, files, Notes and Knowledge Bases.

This organization may inform task scope.

It does not grant Hermes Agent free access to OpenWebUI data.

The canonical handoff rule is:

```text
OpenWebUI organizes user knowledge.
Pantheon turns that organization into a bounded task scope.
Hermes consults only the authorized scope and returns candidates with evidence.
```

OpenWebUI may expose user selection of:

- dossier;
- project;
- folder;
- Knowledge Base;
- file;
- Note;
- source subset;
- conversation or channel excerpt.

Pantheon must translate that selection into a bounded governance artifact before execution.

Allowed handoff artifacts include:

```text
Task Contract
Context Pack
allowed_knowledge_ids
allowed_file_ids
allowed_note_ids
source references
retrieved excerpts
exclusion list
approval ceiling
memory rule
```

OpenWebUI must preserve the distinction between:

```text
available knowledge
selected knowledge
retrieved knowledge
evidence candidate
Register Candidate
Registre Probatoire entry
```

A user selecting a Knowledge Base does not authorize global cross-dossier access.

A model discovering an accessible Knowledge Base does not make that Knowledge Base part of the current task.

A retrieved chunk does not become evidence until selected and represented as such.

A retrieved or cited item does not become memory without governed memory review.

### Context Pack handoff

The preferred MVP handoff is a bounded Context Pack.

OpenWebUI may help collect the selected content.

Pantheon governs what is included, excluded and marked uncertain.

Hermes receives only the authorized material needed for the task.

This avoids coupling Hermes to OpenWebUI internals.

### Read-only gateway handoff

A future implementation may expose a read-only governed knowledge gateway.

Such a gateway may provide scoped operations such as:

```text
list_scopes_for_user
list_knowledge_for_scope
search_scoped_knowledge
fetch_source_excerpt
fetch_source_metadata
create_evidence_candidate
```

Any such gateway must remain read-only by default and must include scope, user, task and approval context.

### Direct database access

Direct Hermes access to OpenWebUI database tables, vector stores, Postgres, pgvector or internal storage should be avoided for normal workflows.

If ever used for diagnostics or controlled administration, it must be:

- read-only;
- scoped;
- logged;
- restricted to governed views rather than raw tables where possible;
- forbidden from writing memory;
- forbidden from bypassing approvals.

OpenWebUI remains cockpit and knowledge organization surface.

It does not become the knowledge authority for Pantheon.

## Candidate output display

OpenWebUI may display outputs returned by Hermes Agent or another external runtime.

These outputs must be labeled according to governance state.

Useful labels include:

```text
candidate
under_review
approved
rejected
blocked_by_scope
blocked_by_evidence
blocked_by_approval
blocked_by_capability_gap
superseded
```

OpenWebUI display must not erase uncertainty.

If evidence is partial, the interface should preserve that limitation.

## Evidence Pack display

OpenWebUI may display Evidence Packs to the user.

The display may include:

- linked Task Contract;
- sources;
- assumptions;
- actions summary;
- rite summary when relevant;
- risks;
- outputs;
- memory candidates;
- approval state;
- limitations.

OpenWebUI display does not replace the Evidence Pack.

OpenWebUI must not hide missing evidence.

## Task Contract display

OpenWebUI may display Task Contracts before execution or review.

The user may approve, reject or request revision through the cockpit.

OpenWebUI may display a rite recommended by the Task Contract.

OpenWebUI must not trigger that rite automatically.

OpenWebUI must not expand Task Contract scope automatically.

If the user asks for additional work, the Task Contract must be revised or a new contract must be created when governance requires it.

## Rite display

OpenWebUI may display rite information as a governance surface.

Useful rite display labels include:

```text
rite_proposed
rite_not_needed
rite_under_review
rite_active
rite_completed
rite_rejected
rite_superseded
rite_escalated_to_user_decision_gate
```

OpenWebUI may display:

- rite identifier;
- trigger reason;
- linked Task Contract;
- roles expected to contribute;
- current ZEUS status;
- required Evidence Pack entries;
- User Decision Gate impact;
- memory impact.

OpenWebUI must not display a rite as an executable workflow.

OpenWebUI must not run a rite by UI state alone.

OpenWebUI must not treat rite completion as approval.

OpenWebUI must not treat rite output as a Registre Probatoire entry.

OpenWebUI must not hide unresolved tensions exposed by a rite.

## Memory display

OpenWebUI may display Register Candidates and a Registre Probatoire entry excerpts.

Register Candidate display is not promotion.

A Registre Probatoire entry display is not modification.

OpenWebUI must not infer memory promotion from:

- repeated chat content;
- user convenience;
- retrieval success;
- model confidence;
- interface affordance;
- Knowledge Base indexing.

Memory promotion remains governed by `MEMORY.md`.

## Functions, tools, pipes, filters, actions and pipelines

OpenWebUI may expose or host capability surfaces such as functions, tools, pipes, filters, actions or pipelines.

Pantheon Next treats these as external capability surfaces when they can affect a result, call a service, transform data, trigger execution, write data, publish data or influence memory.

They must be governed by:

- Task Contract scope;
- `EXTERNAL_TOOLS_POLICY.md`;
- Evidence Pack requirements;
- approval level;
- memory rules.

They must not become hidden Pantheon runtime.

They must not bypass Hermes when Hermes is the intended execution runtime.

They must not canonize memory or doctrine.

They must not become a free plugin manager for Pantheon Next.

## Communication channels

OpenWebUI may be one communication cockpit among others.

Other channels may include email, messaging platforms, documents, spreadsheets, forms or project tools.

A channel is not governance by itself.

The governance record must still preserve scope, evidence, approval, output status and memory state.

## Source upload and source reference

OpenWebUI may allow users to upload or reference sources.

Uploaded sources remain source material until reviewed.

A source can be:

- relevant;
- irrelevant;
- partial;
- contradicted;
- stale;
- superseded;
- approved as reference;
- rejected.

Upload does not equal validation.

Retrieval does not equal validation.

## Context Packs

OpenWebUI may display or transmit Context Packs.

A Context Pack is a bounded context artifact.

It is not a Registre Probatoire entry.

It is not runtime state.

It should declare:

- purpose;
- scope;
- included references;
- excluded references;
- memory status;
- staleness or uncertainty;
- approval state when relevant.

## Relationship to Hermes Agent

OpenWebUI may be the visible interface through which the user requests work that Hermes Agent executes.

OpenWebUI does not execute Hermes work by itself.

OpenWebUI may display Hermes results.

OpenWebUI does not approve Hermes results by displaying them.

OpenWebUI does not canonize Hermes memory candidates.

OpenWebUI may expose a scoped Knowledge handoff to Hermes only when Pantheon has framed the task scope.

OpenWebUI must not grant Hermes broad access to every Knowledge Base, Note, folder, file or vector store merely because the user can access them in the cockpit.

If a rite leads to Hermes-side work, that work still requires a Task Contract and Evidence Pack expectations.

OpenWebUI rite display does not authorize Hermes execution.

## Relationship to Pantheon Next

Pantheon Next governs the doctrine, artifacts, approvals, memory rules and evidence expectations.

OpenWebUI may expose those artifacts to the user.

OpenWebUI must not become the canonical governance repository.

If a decision matters beyond the current interaction, it must be recorded in governed Pantheon artifacts.

## Forbidden integration drift

OpenWebUI integration must never become:

- Pantheon execution runtime;
- governance source of truth;
- canonical memory store;
- hidden workflow runner;
- hidden scheduler;
- provider router;
- autonomous agent runtime;
- automatic rite trigger engine;
- automatic memory promoter;
- uncontrolled plugin manager;
- doctrine mutation surface without approval;
- approval bypass;
- unrestricted knowledge gateway to Hermes;
- direct global database access path for Hermes.

If OpenWebUI display is treated as canonical governance truth, the boundary has failed.

If an OpenWebUI capability surface runs Pantheon work without Task Contract and Evidence Pack, the boundary has failed.

If OpenWebUI rite display is treated as execution, the boundary has failed.

If Hermes can freely browse OpenWebUI Knowledge without a bounded task scope, the boundary has failed.

## Implementation note

This document intentionally avoids operational details such as OpenWebUI version, endpoints, environment variables, Docker configuration, provider configuration, plugin installation, function syntax, pipe syntax, filter syntax, action syntax or pipeline behavior.

Those details must be verified against current official OpenWebUI documentation before any operational configuration is proposed.

## Final rule

OpenWebUI makes governance visible and actionable for the user.

It does not make governance true by itself.

OpenWebUI may organize user knowledge.

It does not authorize unbounded execution access to that knowledge.

## Domain mapping (absorbed from OPENWEBUI_DOMAIN_MAPPING.md)

The former stub declared this intended scope; it is owned here now, still documented and not implemented until each item is reviewed:

- governance mapping between Pantheon domain objects and OpenWebUI display surfaces;
- which Pantheon concepts may be shown in chat;
- which Pantheon concepts may be shown in Knowledge Bases;
- which Pantheon concepts may trigger user-facing approval requests;
- which Pantheon concepts may surface as Evidence Pack viewers;
- forbidden surfaces (no canonical memory, no execution control, no doctrine mutation through OpenWebUI);
- review rules before any new surface is exposed.

These items remain candidates. None of them is implemented by this section.

## Plugin policy (absorbed from OPENWEBUI_PLUGIN_POLICY.md)

The former stub declared this intended scope; it is owned here now, still documented and not implemented until each item is reviewed:

- governance policy for OpenWebUI functions, pipes, filters, actions and pipelines;
- candidate-only status of any OpenWebUI plugin until reviewed;
- review and approval requirements before activation;
- forbidden plugin behaviors (governance mutation, canonical memory writes, doctrine change, self-approval, execution backdoors);
- evidence requirements for plugin outputs;
- audit and revocation rules;
- separation between user-facing convenience and Pantheon governance.

These items remain candidates. None of them is implemented by this section.

## Upstream reference — OpenWebUI (external cockpit)

Reference version at time of writing: OpenWebUI `0.10.2`. Pantheon Next neither installs
nor runs it; this records the exposure surface.

- **Extension model.** Functions (Pipes, Filters, Actions) plus Tools, configured through
  Valves / UserValves. The connection to Hermes is an OpenAI-compatible provider (see
  `templates/hermes/connection/`).
- **Event / webhook system (0.10.x).** OpenWebUI can emit 28+ typed events (`auth.*`,
  `chat.*`, `admin.*`, `knowledge.*`) and run an Event function on them. Pantheon may
  consume these read-only as an audit / evidence trail (`templates/openwebui/events/`); it
  decides nothing and blocks nothing there. The User Decision Gate still decides, and an
  audit event candidate is not a Registre Probatoire entry.

---

## Absorbed: Openwebui Templates (2026-07-07)

Formerly `docs/governance/OPENWEBUI_INTEGRATION.md`; absorbed verbatim during the governance cleanup (pass B). Headings demoted one level; content unchanged.

Original status: active support doctrine — cockpit templates and dependency exposure only.

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

### Purpose

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

### OpenWebUI technical boundary

OpenWebUI supports Functions, Tools and Pipelines that can extend the product.

This matters because some of those extension points execute code or expose tool surfaces.

Pantheon must treat them as capability surfaces, not as governance authority.

OpenWebUI cockpit templates should prefer non-executable display and decision surfaces before any Function, Tool, Pipe, Filter, Action or Pipeline is considered.

### Core rule

```text
OpenWebUI templates make governance visible.
They do not make governance true.
```

Operational version:

```text
OpenWebUI may display, collect, label, select, warn and ask.
OpenWebUI must not execute, approve, canonize, promote memory or expand scope.
```

### Relationship to Module Activation

`MODULE_ACTIVATION.md` defines detection, activation, task authorization and Effective Policy.

This document defines how those states may be exposed to users.

A UI control must not bypass the Effective Policy.

A UI toggle must not disable mandatory rules.

A UI state must not grant runtime authority.

### Dependency hierarchy principle

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

### Dependency state vocabulary

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

### Dependency record

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

### Parent module hierarchy

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
│  ├─ Register Candidate Review Template
│  ├─ Scope-limited Memory View Template
│  └─ Registre Probatoire entry Read Template
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

### Parent disable effects

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

### Mandatory blockers

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

### Template anatomy

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

### Core cockpit templates

#### 1. Intake Template

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

#### 2. Scope Review Template

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

#### 3. Source Selection Template

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

#### 4. Context Pack Template

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

#### 5. Hermes Dispatch Template

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

#### 6. Evidence Pack Display Template

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

#### 7. Run Trace Summary Template

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

#### 8. Approval Prompt Template

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

#### 9. User Decision Gate Template

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

#### 10. Delivery Gate Template

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

#### 11. External Transmission Gate Template

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

#### 12. Register Candidate Review Template

Purpose: review a Register Candidate.

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

#### 13. Module Status Template

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

#### 14. Effective Policy Template

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

#### 15. Dependency Graph Template

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

#### 16. LangGraph Run Status Template

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

#### 17. Human Interrupt Template

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

#### 18. Capability Gap Template

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

### Dependency matrix

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

### Degraded mode

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

### UI control rules

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

### OpenWebUI extension warning

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

### Native Mode boundary

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

### Effective Policy display example

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

### Relationship to future implementation

A future implementation may translate these templates into UI components.

That implementation must remain separate from this document and must not be assumed to exist.

If future implementation requires code, schemas, operations or Docker changes, the protected-file confirmation rules apply.

### Final rule

```text
A disabled parent must make its children visibly unavailable.
A visible child must never imply its parent is satisfied.
```
