# Evidence Topology

Status: active doctrine — consolidated evidence topology corpus. Each section keeps its original status note; consolidation changes no rule.

This document consolidates the former `EVIDENCE_TOPOLOGY_*` family into one file, per the consolidation step of `TARGET_ARCHITECTURE.md` and the sprawl pause (issue #41). The former files remain as redirect notes so existing references keep resolving.

| Former file | Section below |
|---|---|
| `EVIDENCE_TOPOLOGY_GATE.md` | Core doctrine — topology gate |
| `EVIDENCE_TOPOLOGY_BRIDGES.md` | Bridges |
| `EVIDENCE_TOPOLOGY_CHECKLIST.md` | Checklist |
| `EVIDENCE_TOPOLOGY_ROADMAP.md` | Roadmap addendum |
| `EVIDENCE_TOPOLOGY_RECONCILIATION.md` | Reconciliation note |
| `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` | Schema candidate note |
| `CHANGELOG_ADDENDUM_EVIDENCE_TOPOLOGY_SCHEMA_D2.md` | Historical changelog addendum (D2) |

The `evidence_topology_antipatterns/` folder is unchanged.


---

## Core doctrine — topology gate

Original status: active doctrine — reasoning topology, evidence preservation and Hermes swarm constraint.

This document defines how Pantheon Next chooses the smallest safe reasoning topology before asking an external runtime to execute.

It is governance doctrine.

It is not a runtime router.

It is not an execution graph.

It is not a LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, Microsoft Agent Framework or Hermes Workspace implementation.

It does not add a scheduler, queue, message bus, swarm controller, worker manager, provider router, MCP runtime, hidden debate system or automatic approval loop.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Core thesis

The unit of reasoning is not the agent.

The unit of reasoning is the proof chain.

```text
Preserve the proof chain before distributing reasoning.
```

A task should not be split into specialist agents merely because the system can split it.

A task should be split only when the shape of the evidence justifies distribution.

### Purpose

Many professional and technical tasks fail when decisive details are destroyed at handoff.

A worker may see the source.

Another worker may see the code.

Another worker may see the configuration.

A supervisor may then receive only summaries and synthesize from shadows.

That pattern is unsafe when the answer depends on connecting evidence across sources.

Pantheon therefore classifies the evidence topology before execution.

A different pattern can be valid: persistent role teams where each role owns a distinct stage, artifact, surface or lane.

Those teams can reduce human copy-paste and preserve operational continuity.

They still require governed handoff artifacts, evidence locators, review gates and memory boundaries.

### Canonical rule

When a task requires cross-source inference, preserve one primary reasoning context.

Workers may collect, filter, normalize or verify bounded evidence.

Workers must not replace the inference chain unless their domains, artifacts or stages are genuinely independent.

No summary-only handoff is allowed for decision-critical work.

Every handoff must preserve source references, claim scope, uncertainty, limitations and open questions.

Persistent role teams are allowed only when role boundaries are explicit and the handoff artifact is reviewable.

### Default posture

Default topology:

```text
single_primary_reasoning_context
```

Use this default when:

- the decisive answer depends on linking evidence across sources;
- the relevant evidence fits in one context window;
- source order matters;
- scope confusion is a material risk;
- the task is diagnostic, contractual, legal, technical, regulatory, design-related, safety-related or professional;
- the likely failure mode is false synthesis from partial summaries.

### Allowed topologies

#### 1. Single primary reasoning context

Use when the answer depends on connecting sources.

Examples:

```text
Jira comment -> Java class -> XML configuration -> design note
quote -> CCTP -> site report -> contractual risk
email thread -> contract clause -> professional liability note
regulatory update -> affected dossier assumption -> decision gate
source document -> retrieved excerpt -> evidence item -> memory candidate review
```

Rule:

```text
One primary reasoning context.
All decisive evidence visible or locatable.
No specialist conclusion without evidence locator.
```

This does not mean one model must do everything.

It means the decisive inference must be made from a consolidated evidence view, not from disconnected summaries.

#### 2. Fan-out extraction, single synthesis

Use when many sources must be inspected but the final inference must remain unified.

Workers may extract:

- source references;
- candidate facts;
- contradictions;
- dates;
- code locations;
- clauses;
- risks;
- missing documents;
- scope warnings.

Workers must not produce final conclusions.

Rule:

```text
Distributed extraction.
Centralized reasoning.
Evidence Items, not opinions.
```

#### 3. Parallel independent workers

Use only when tasks are genuinely independent.

Examples:

- classifying many documents;
- extracting tables from several PDFs;
- monitoring unrelated regulatory feeds;
- preparing separate summaries for separate dossiers;
- running isolated benchmark or lab tasks.

Rule:

```text
Parallelism is allowed when outputs do not require hidden cross-source inference.
```

#### 4. Router

Use when the first problem is classification, not truth.

Examples:

- legal versus technical versus accounting question;
- urban planning versus ERP versus structural topic;
- support request category;
- source type routing.

Rule:

```text
The router classifies.
The router does not decide truth.
```

#### 5. Sequential handoff

Use only when each step produces a bounded artifact that the next step can verify.

Examples:

```text
source collection -> Evidence Pack -> risk review -> draft
OCR -> structured extraction -> quality review -> Context Pack
patch candidate -> byte-level review -> approval gate
```

Rule:

```text
Each handoff must carry traceable evidence, not just a summary.
```

#### 6. Persistent role-team handoff

Use when the work has stable lanes and each role owns a distinct artifact, surface or stage.

This topology is valid when handoffs reduce human dispatch burden without hiding evidence or approval state.

Examples:

```text
arch review -> backend implementation -> frontend adaptation -> review gate
research -> strategy brief -> writer draft -> editor review -> SEO packaging
researcher -> critic -> human review -> writer
```

Allowed role-team handoff artifacts include:

- API contract;
- architectural decision note;
- patch candidate;
- review verdict;
- campaign brief;
- research digest;
- draft article;
- editorial review note;
- metadata package;
- evidence sufficiency note.

Rule:

```text
Persistent roles may preserve operational continuity.
They must not convert role memory, team chat or handoff convenience into authority.
```

A persistent role-team may use role memory for style, recurring procedures or local execution context.

That role memory is not Pantheon a Registre Probatoire entry.

Auto-captured knowledge is not approved doctrine.

Agent-to-agent handoff is not approval.

A visible canvas is not an Evidence Pack by itself.

The value of this topology is continuity, not automatic truth.

#### 7. Bounded Hermes swarm

Use only when Hermes needs distributed execution capacity inside a Task Contract.

Examples:

- parallel evidence collection;
- bounded source inspection;
- independent checks;
- patch candidate preparation;
- document batch extraction;
- isolated lab experiments;
- QA or review lanes.

Rule:

```text
Hermes Swarm may multiply execution capacity, not decision authority.
```

A Hermes swarm may collect evidence in parallel.

A single consolidated reasoning context must connect decisive evidence.

Pantheon Roles review the resulting tensions.

Zeus arbitrates status and procedure.

The human decides when the gate requires it.

### Forbidden topology

Forbidden for decision-critical tasks:

```text
specialist agents
-> summary-only handoffs
-> supervisor synthesis
-> final answer without source-linked evidence
```

Also forbidden:

```text
persistent team chat
-> role memory confidence
-> unreviewed handoff
-> external publication, deployment or memory promotion
```

Failure mode:

```text
The supervisor reasons over shadows.
The team confuses continuity with authority.
```

This topology may look sophisticated while degrading reliability, increasing cost and hiding the decisive evidence.

### Handoff contract

A handoff must include:

```text
claim
source reference
source location
supported inference
scope of support
confidence or certainty status
limitation
uncertainty
open question
scope warning
worker scope
approval gap when relevant
handoff artifact when relevant
next intended role or lane when relevant
```

A handoff must not include only:

```text
I reviewed X
it seems that
the likely issue is
summary of findings
no blocker found
looks good
ready for next agent
```

A handoff without locators is not adequate evidence for consequential work.

A handoff without a bounded artifact is not adequate continuity for role-team work.

### Evidence Item shape

A worker output that affects a decision should be shaped as an Evidence Item.

Example:

```yaml
worker_output:
  type: evidence_item
  claim: "Class X controls behavior Y"
  source_type: "java_source"
  source_ref: "src/path/ClassX.java:L120-L156"
  supports: "ticket_intention_trace"
  scope_of_support: "Only supports behavior Y under condition Z"
  confidence: "medium"
  limitations:
    - "Runtime behavior not tested"
    - "Configuration XML still needs confirmation"
  scope_warnings:
    - "Do not apply to Ticket ABC-124"
  open_questions:
    - "Does XML condition A gate this branch?"
```

Evidence Items are not final conclusions.

They are structured material for review and synthesis.

### Handoff Artifact shape

A persistent role-team handoff should produce a bounded artifact.

Example:

```yaml
handoff_artifact:
  type: api_contract_note
  from_role: backend
  to_role: frontend
  scope: "New billing endpoint for dashboard display only"
  artifact_ref: "docs/contracts/billing-api-draft.md"  # fictional example path
  changed_surface:
    - "GET /api/billing/summary"
  assumptions:
    - "Authentication middleware unchanged"
  blockers:
    - "Response pagination not yet validated"
  evidence_refs:
    - "backend diff candidate"
    - "test output reference"
  approval_gap: "frontend may adapt UI, but deployment remains blocked pending review"
```

The artifact does not approve itself.

It makes the next stage possible without making the result canonical.

### Task Contract expectation

A Task Contract should declare reasoning topology when the task is non-trivial, evidence-sensitive, cross-source, professional, external-effect-bearing, mutation-bearing or memory-affecting.

Recommended field name for future schemas or examples:

```yaml
reasoning_topology:
  selected: single_primary_reasoning_context
  reason: cross_source_reasoning_required
  handoff_policy: no_summary_only_handoff
  evidence_policy: source_linked_evidence_items_required
```

For role-team work:

```yaml
reasoning_topology:
  selected: persistent_role_team_handoff
  reason: artifact_bound_stage_work
  handoff_policy: bounded_artifact_required
  memory_policy: role_memory_is_not_canonical_memory
  approval_policy: external_effect_requires_gate
```

This is a governance expectation.

It is not a runtime dispatch instruction.

The current schemas are not changed by this document.

### Topology decision matrix

```yaml
topology_decision:
  single_primary_reasoning_context:
    choose_when:
      - cross_source_reasoning_required
      - relevant_material_fits_context
      - root_cause_or_solution_design
      - professional_or_liability_sensitive
      - scope_confusion_risk
    avoid_when:
      - material_exceeds_context_without_extraction
      - independent_batch_processing_needed

  fanout_extract_then_single_synthesis:
    choose_when:
      - many_sources
      - each_source_can_be_reduced_to_evidence_items
      - final_reasoning_must_be_unified
    worker_output:
      - evidence_items
      - contradictions
      - missing_sources
      - scope_warnings
    forbidden_worker_output:
      - final_conclusion
      - unverifiable_summary
      - recommendation_without_source

  parallel_independent_workers:
    choose_when:
      - independent_tasks
      - no_hidden_cross_source_dependency
      - batch_or_monitoring_work
    final_step:
      - aggregate_results
      - preserve_separate_scopes

  persistent_role_team_handoff:
    choose_when:
      - stable_role_lanes
      - artifact_bound_stages
      - visible_handoffs
      - durable_style_or_project_context_needed
      - final_effect_is_gated
    must_have:
      - handoff_artifact
      - role_scope
      - memory_boundary
      - approval_gap
      - visible_review_state
    forbidden:
      - role_memory_as_canonical_memory
      - team_chat_as_evidence_pack
      - direct_publication_without_gate
      - agent_handoff_as_approval

  bounded_hermes_swarm:
    choose_when:
      - execution_capacity_is_needed
      - worker_outputs_are_evidence_items
      - task_contract_bounds_scope
      - approvals_are_declared
    must_have:
      - evidence_pack
      - source_locators
      - uncertainty
      - contradiction_handling
      - approval_gate_when_required
```

### Relationship to Hermes

Hermes may choose operational means inside the Task Contract.

Pantheon may constrain topology by declaring the evidence and handoff expectations.

Hermes may use persistent role teams, swarms or workers internally only when the Task Contract allows distributed execution.

Hermes may use role-team or swarm-like execution to:

- collect evidence;
- inspect bounded sources;
- run independent checks;
- prepare Patch Candidates;
- prepare Evidence Items;
- prepare Handoff Artifacts;
- report Capability Gaps;
- prepare review notes.

Hermes swarm and role-team execution must not:

- approve;
- canonize memory;
- expand scope silently;
- replace Pantheon Roles;
- produce final authority;
- hide worker traces;
- rely on summary-only handoffs;
- bypass User Decision Gates;
- turn worker state or role memory into Pantheon memory.

### Relationship to the Governance College

Pantheon Roles are not workers.

The Governance College separates responsibilities of judgment.

It does not fragment the proof chain.

A role may inspect the same consolidated evidence from a different governance angle.

A role must not use its viewpoint to create hidden runtime chatter or a shadow multi-agent debate.

Useful distinction:

```text
workers collect and produce candidates.
role-team workers pass bounded artifacts when stages are distinct.
roles review status, risk, tension and procedure.
```

### Relationship to Evidence Packs

Evidence Packs should preserve topology decisions when those decisions affect trust.

An Evidence Pack may record:

- selected reasoning topology;
- why the topology was chosen;
- worker outputs used as Evidence Items;
- Handoff Artifacts used between role-team stages;
- summary-only handoffs rejected or blocked;
- contradictions preserved;
- synthesis limitations;
- unresolved evidence gaps;
- User Decision Gate impact.

Evidence Packs must not store hidden chain-of-thought.

Team chat, runtime messages and canvas activity are not Evidence Packs by themselves.

### Relationship to OpenWebUI

OpenWebUI may expose the topology choice, evidence state, worker checkpoints, Handoff Artifacts, Evidence Items, blocked handoffs, User Decision Gates and approval requests.

OpenWebUI does not choose topology as authority by itself.

OpenWebUI display does not validate the topology.

A visible agent conversation canvas is useful operational UI.

It is not governance validation by itself.

The user may be asked to decide when the topology choice changes scope, risk, cost, timing, external effect or memory impact.

### Relationship to memory

Topology traces, worker summaries, runtime state, role memory and repeated observations are not memory.

A topology outcome may propose a Register Candidate only when the Evidence Pack supports it and memory rules allow it.

No worker, swarm, role, role-team, retrieval result or repeated conclusion may promote a Registre Probatoire entry automatically.

Role memory may be useful for voice, procedure or project continuity.

Pantheon must still treat it as runtime-side memory unless promoted through governed Register Candidate review.

### Relationship to external inspirations

External frameworks and repositories such as LangGraph, LangChain multi-agent patterns, OpenAI Swarm or Agents SDK, Microsoft Agent Framework, AutoGen, CrewAI, Pydantic AI, LlamaIndex, DSPy, Hermes Workspace and research orchestrator examples may inspire vocabulary.

They do not authorize importing runtime behavior into Pantheon.

Kept pattern:

```text
classify topology before execution.
preserve proof before handoff.
use structured outputs.
use explicit graph edges where a runtime owns execution.
use critic or review gates before writer, publisher, sender or deployer stages.
accumulate evidence append-only when revising.
require human or governance gates where risk rises.
```

Rejected pattern:

```text
more agents means more truth.
more orchestration means more reliability.
swarm output means approved output.
worker memory means Pantheon memory.
role-team memory means Registre Probatoire entry.
runtime trace means Evidence Pack.
critic approval means final approval.
visible canvas means governance validation.
```

### Anti-patterns

Avoid:

```text
multi-agent by default
role-as-worker confusion
summary-only supervisor synthesis
swarm as governance
conductor as Zeus
worker checkpoint as approval
role-team handoff as approval
retrieved content as evidence without selection
runtime state as memory
role memory as a Registre Probatoire entry
parallelism where continuity is required
```

Prefer:

```text
single context when evidence must be connected
fan-out only for bounded extraction
role-team handoff only for bounded artifact stages
Evidence Items over prose summaries
Handoff Artifacts over team chatter
scope warnings over broad synthesis
review lanes over self-approval
User Decision Gate over forced certainty
```

### Final rule

```text
Do not distribute judgment before preserving the proof chain.

Swarm for collection.
Role-team handoff for bounded artifact stages.
Single context for inference when evidence must connect.
Governance College for review.
User Decision Gate for unresolved stakes.
Human decision for consequential approval.
```


---

## Bridges

Original status: active bridge note — documentation-level only.

Date: 2026-05-30

This document links Evidence Topology Gate doctrine to existing Pantheon governance documents.

It is not a replacement for those documents.

It is not a schema.

It is not runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Purpose

`EVIDENCE_TOPOLOGY_GATE.md` defines how Pantheon should classify the shape of a task before external execution.

This bridge note clarifies how that doctrine relates to:

- Task Contracts;
- Evidence Packs;
- Hermes integration;
- OpenWebUI exposure;
- memory governance;
- scope isolation;
- external tools;
- Governance College;
- User Decision Gate.

### Bridge to Task Contracts

Relevant document:

- `docs/governance/TASK_CONTRACTS.md`.

Task Contracts define the governed execution boundary for external runtime work.

Evidence Topology Gate adds a pre-execution question:

```text
What topology preserves the proof chain with the smallest safe complexity?
```

Task Contract implication:

- declare topology for non-trivial, evidence-sensitive or externally consequential work;
- explain why single context, fan-out, role-team or bounded swarm is justified;
- prohibit summary-only handoffs where proof-chain continuity matters;
- specify expected Evidence Items and Handoff Artifacts;
- state approval gaps before mutation, publication, transmission or memory impact.

Boundary:

```text
Task Contract topology is governance metadata.
It is not runtime dispatch.
```

### Bridge to Evidence Packs

Relevant document:

- `docs/governance/EVIDENCE_PACK.md`.

Evidence Packs explain what was done, on what basis, with which assumptions, risks and outputs.

Evidence Topology Gate adds topology accountability:

- why the topology was chosen;
- which topologies were rejected;
- what worker outputs were used as Evidence Items;
- what Handoff Artifacts were used between role-team stages;
- what summary-only handoffs were blocked;
- what contradictions remain unresolved;
- how the topology affects approval state.

Boundary:

```text
Evidence Pack records reviewable justification.
It must not become a runtime trace or hidden chain-of-thought archive.
```

### Bridge to Hermes Integration

Relevant document:

- `docs/governance/HERMES_INTEGRATION.md`.

Hermes executes externally under Task Contract.

Evidence Topology Gate clarifies permitted Hermes-side execution patterns:

- single worker with all authorized tools;
- fan-out extraction returning Evidence Items;
- persistent role-team handoff returning Handoff Artifacts;
- bounded swarm returning reviewable candidate outputs.

Hermes may choose internal operational means, but only within Task Contract boundaries.

Hermes must not:

- treat swarm output as approval;
- treat role-team memory as Pantheon memory;
- expand scope silently;
- hide worker traces when evidence is required;
- replace Pantheon Roles;
- bypass User Decision Gates.

Boundary:

```text
Hermes may multiply execution capacity.
It must not multiply authority.
```

### Bridge to OpenWebUI Integration

Relevant document:

- `docs/governance/OPENWEBUI_INTEGRATION.md`.

OpenWebUI exposes the cockpit surface.

Evidence Topology Gate clarifies what OpenWebUI may display:

- selected topology;
- topology reason;
- evidence state;
- worker checkpoints;
- Evidence Items;
- Handoff Artifacts;
- blocked handoffs;
- approval gaps;
- User Decision Gate prompts.

OpenWebUI may expose a visible canvas or conversation surface.

That visibility is useful, but it is not validation.

Boundary:

```text
OpenWebUI display is not governance authority.
A canvas is not an Evidence Pack by itself.
```

### Bridge to Memory

Relevant document:

- `docs/governance/MEMORY.md`.

Evidence Topology Gate reinforces that topology traces, worker summaries, runtime state, role memory, swarm state and repeated observations are not a Registre Probatoire entry.

A topology outcome may support a Register Candidate only if:

- evidence supports it;
- scope is explicit;
- contradictions are handled;
- approval level is satisfied;
- memory doctrine allows it.

Boundary:

```text
Role memory may help execution continuity.
It is not Pantheon Registre Probatoire entry.
```

### Bridge to Scope Isolation

Relevant document:

- `docs/governance/SCOPE_ISOLATION.md`.

Topology selection must preserve scope boundaries.

A worker, role-team or swarm must not broaden scope because it found adjacent material.

Scope expansion requires revised contract or User Decision Gate.

Boundary:

```text
Distributed work does not dissolve scope.
```

### Bridge to External Tools Policy

Relevant document:

- `docs/governance/EXTERNAL_TOOLS_POLICY.md`.

Topology does not authorize tools.

A fan-out or swarm pattern may make tool use more likely, but each external tool remains governed by scope, evidence and approval.

Boundary:

```text
Tool availability is not tool authorization.
Topology selection is not tool approval.
```

### Bridge to Governance College

Relevant document:

- `docs/governance/GOVERNANCE_COLLEGE.md`.

Evidence Topology Gate protects the difference between workers and roles.

Workers may collect, extract, check or produce candidates.

Pantheon Roles review tensions, risks, status and procedure.

Boundary:

```text
Governance College is not a multi-agent runtime.
Roles are not workers.
```

### Bridge to User Decision Gate

Relevant document:

- `docs/governance/USER_DECISION_GATE.md`.

Topology choice may trigger a User Decision Gate when it changes:

- scope;
- risk;
- cost;
- delivery timeline;
- external transmission;
- mutation;
- memory impact;
- evidence sufficiency.

Boundary:

```text
When topology choice affects stakes, expose the choice.
The human decides when procedure is insufficient.
```

### Bridge to examples

Relevant example folder:

- `docs/examples/evidence_topology/`.

The examples show:

- single primary reasoning context;
- fan-out extraction followed by single synthesis;
- persistent role-team handoff;
- Evidence Items;
- Handoff Artifacts;
- approval gaps;
- memory boundaries.

They are fictional and non-executable.

Boundary:

```text
Examples illustrate doctrine.
They do not implement execution.
```

### Rejected bridge mistakes

Reject:

```text
Task Contract topology as runtime dispatch
Evidence Pack as runtime trace
Hermes swarm as approval authority
OpenWebUI canvas as validation
role memory as a Registre Probatoire entry
worker summary as evidence
User Decision Gate as automatic approval
Governance College as hidden debate runtime
```

### Final bridge rule

```text
Task Contract declares the boundary.
Hermes executes within it.
Evidence Pack preserves reviewable proof.
OpenWebUI exposes the state.
Pantheon governs status, approval and memory.
```


---

## Checklist

Original status: active checklist — documentation-level governance support.

Date: 2026-05-30

This checklist helps decide whether a task should use a single primary reasoning context, fan-out extraction, persistent role-team handoff or bounded Hermes swarm.

It supports `EVIDENCE_TOPOLOGY_GATE.md`.

It is not a schema.

It is not runtime configuration.

It is not a Hermes dispatch file.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Core question

```text
What topology preserves the proof chain with the smallest safe complexity?
```

Do not start from agent count.

Start from the shape of evidence.

### Fast decision table

| Situation | Preferred topology | Why |
|---|---|---|
| The answer depends on connecting evidence across sources | `single_primary_reasoning_context` | The decisive inference must not be fragmented. |
| Many sources must be inspected, but final reasoning must compare them | `fanout_extract_then_single_synthesis` | Extraction can be distributed; judgment must remain consolidated. |
| Tasks are independent and do not require hidden cross-source inference | `parallel_independent_workers` | Parallelism is useful and low-risk. |
| The first problem is category or domain selection | `router` | Routing classifies; it does not decide truth. |
| Each step produces a bounded artifact that the next step can verify | `sequential_handoff` | Handoff is safe only when artifact and evidence are reviewable. |
| Stable lanes own distinct artifacts or stages | `persistent_role_team_handoff` | Continuity is useful, but handoff must remain artifact-bound. |
| Execution needs capacity, not judgment | `bounded_hermes_swarm` | Swarm may multiply hands, not authority. |

### Twelve gating questions

Answer these before choosing topology.

#### 1. Does the answer depend on a proof chain across sources?

Examples:

```text
email -> contract -> site report -> professional risk
Jira comment -> code -> XML config -> design note
quote -> CCTP -> photos -> client instruction
```

If yes, prefer:

```text
single_primary_reasoning_context
```

or:

```text
fanout_extract_then_single_synthesis
```

Do not use summary-only specialist agents.

#### 2. Does the decisive material fit in one context window?

If yes, prefer one consolidated reasoning context.

If no, allow extraction first, then synthesize from selected Evidence Items.

#### 3. Can workers extract facts without concluding?

If yes, fan-out may be safe.

If workers must interpret the whole case to be useful, do not split too early.

#### 4. Would a summary lose decisive details?

If yes, summary-only handoff is forbidden.

Require Evidence Items with source locators.

#### 5. Is there a real parallelism benefit?

Use parallel workers only when the work is independent or source extraction is large.

Do not use multi-agent merely to make the workflow look sophisticated.

#### 6. Is the work stage-bound and artifact-bound?

If each role owns a distinct artifact, persistent role-team handoff may be useful.

Examples:

```text
architecture note -> backend contract -> frontend adaptation -> review note
research digest -> campaign brief -> draft -> editorial note -> metadata package
```

Require Handoff Artifacts.

#### 7. Does the topology create external effect risk?

External effects include:

- sending;
- publishing;
- filing;
- deploying;
- merging;
- notifying;
- modifying a repository;
- creating client-facing output.

If yes, require approval gate.

#### 8. Does the topology affect memory?

If role memory, worker state or repeated observations appear useful, keep them runtime-side unless promoted through governed Register Candidate review.

```text
role memory != Registre Probatoire entry
runtime state != Pantheon memory
```

#### 9. Does the task need a User Decision Gate?

Trigger a gate if topology changes:

- risk;
- scope;
- cost;
- delay;
- external transmission;
- mutation;
- memory impact;
- evidence sufficiency.

#### 10. Does a worker need broader scope than the Task Contract allows?

If yes, stop.

Return a scope gap.

Do not expand silently.

#### 11. Are the handoffs reviewable?

A safe handoff contains:

- claim;
- source reference;
- source location;
- scope of support;
- confidence;
- limitation;
- open question;
- approval gap;
- artifact reference when relevant.

If the handoff is only prose, it is not enough for consequential work.

#### 12. Who has authority?

Workers may collect.

Hermes may execute.

OpenWebUI may expose.

Pantheon governs status.

The human decides when approval is required.

### Decision outputs

A topology decision should produce a short record:

```yaml
topology_decision:
  selected: fanout_extract_then_single_synthesis
  reason: many_sources_but_unified_final_reasoning_required
  rejected:
    - summary_only_multi_agent_supervisor
    - direct_worker_conclusion
  required_outputs:
    - evidence_items
    - contradiction_ledger
    - approval_gap
  user_decision_gate: required_before_external_transmission
```

### Minimal safe defaults

When uncertain:

```text
single context for inference
fan-out only for extraction
role-team only for bounded artifacts
swarm only for execution capacity
User Decision Gate for unresolved stakes
```

### Red flags

Stop and review if the proposed topology contains:

```text
more agents therefore more reliable
summary-only handoff
worker final conclusion
team chat as evidence
role memory as canonical memory
visible canvas as approval
Conductor as Zeus
swarm as judgment
runtime trace as Evidence Pack
```

### Final rule

```text
Do not distribute judgment before preserving the proof chain.
```


---

## Roadmap addendum

Original status: active roadmap addendum — evidence topology, single-context default and bounded Hermes swarm.

This addendum records the roadmap consequences of `EVIDENCE_TOPOLOGY_GATE.md`.

It exists because the main `ROADMAP.md` was not safely patchable in the current tool pass.

It does not replace `ROADMAP.md`.

It does not implement runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Why this addendum exists

External multi-agent and swarm examples show a recurring failure mode:

```text
specialist workers
-> partial source views
-> summary-only handoffs
-> supervisor synthesis
-> wrong conclusion with high coordination cost
```

Pantheon must prevent this pattern from becoming doctrine.

The correct unit of reasoning is the proof chain, not the number of agents.

### Roadmap status

`EVIDENCE_TOPOLOGY_GATE.md` is active governance doctrine.

It is documentation-level only.

It does not change schemas, operations, tests, platform files, Docker, runtime code or Hermes configuration.

### Keep

Keep these roadmap principles:

- single primary reasoning context by default when decisive evidence must be connected across sources;
- fan-out extraction followed by single synthesis when many sources must be inspected;
- parallel workers only when tasks are genuinely independent;
- routers only for classification, not truth decisions;
- sequential handoff only when each step carries verifiable evidence;
- bounded Hermes swarm only as execution capacity;
- role-team handoff only when each role owns a distinct artifact, boundary or stage;
- source-linked Evidence Items rather than unverifiable worker opinions;
- append-only accumulation where evidence quality is improved across revisions;
- explicit critic or review gates before writer, publisher, deployer or sender stages;
- User Decision Gate when topology affects scope, risk, external effect, cost, delivery or memory;
- Governance College as review of tensions, not distributed execution.

### Reject

Reject these roadmap directions:

- multi-agent by default;
- swarm as intelligence multiplier by default;
- conductor as Zeus;
- role-as-worker confusion;
- hidden debate runtime;
- summary-only handoff for decision-critical work;
- worker checkpoint as approval;
- runtime trace as Evidence Pack;
- Hermes memory as Pantheon a Registre Probatoire entry;
- agent memory or auto-captured Knowledge Base as doctrine;
- direct agent-to-agent handoff without governed artifact or source locator;
- tool availability as tool authorization;
- schema field before doctrine stabilizes.

### Persistent role-team pattern

A persistent role-team can work when the roles are stage-bound and artifact-bound.

Example pattern:

```text
research -> strategy brief -> writer draft -> editor review -> SEO packaging
arch review -> backend implementation -> frontend adaptation -> review gate
```

Keep:

- explicit purpose per role;
- explicit handoff destination;
- visible team conversation or canvas;
- durable style or project constraints as candidates for scoped memory;
- handoff artifacts such as API contract, campaign brief, draft, review note or metadata package;
- human visibility before publication, deployment, external transmission or memory promotion.

Reject:

- agent-to-agent chatter as evidence;
- role memory as a Registre Probatoire entry;
- auto-captured Knowledge Base as approved doctrine;
- direct handoff as approval;
- editor, reviewer, SEO or arch agents acting as final professional authority;
- hidden scope expansion between product, code, content, marketing and governance work.

Pantheon translation:

```text
Persistent Hermes roles may keep execution continuity.
Pantheon still requires Task Contract scope, Evidence Pack review, approval thresholds and memory discipline.
```

### LangGraph research orchestrator pattern

Keep from the LangGraph clinical research orchestrator example:

- explicit graph edges;
- Researcher -> Critic -> Human Review -> Writer sequencing;
- critic loop before report writing;
- append-only evidence accumulation across revisions;
- human-in-the-loop interrupt before the writer stage;
- structured state over informal handoff;
- refusal to let a Writer act on thin or contradictory evidence.

Reject from Pantheon:

- LangGraph as Pantheon runtime;
- clinical report generation as professional advice without review;
- Critic approval as final approval;
- in-memory checkpoint as a Registre Probatoire entry;
- tool search result as Evidence Item without selection and source qualification.

Pantheon translation:

```text
Researcher may collect.
Critic may challenge sufficiency.
Human review may gate writing.
Writer may draft.
Pantheon governs the status of every step.
```

### Hermes Workspace pattern distillation

Keep from Hermes Workspace:

- SwarmBrief as an inspiration for a derived Hermes execution brief;
- proof-bearing checkpoints;
- explicit blockers;
- review lane;
- Greenlight Gate;
- role-based worker routing;
- skill-as-procedure discipline;
- Reports and Inbox as exposure surfaces.

Reject from Pantheon:

- Hermes Workspace as Pantheon cockpit;
- Conductor as governance;
- swarm as judgment;
- editable agent memory as a Registre Probatoire entry;
- skill marketplace as approval;
- MCP, terminal, dashboard, jobs, scheduler or tool runtime inside Pantheon.

### Task Contract implications

Future Task Contract examples may include a non-runtime topology declaration such as:

```yaml
reasoning_topology:
  selected: single_primary_reasoning_context
  reason: cross_source_reasoning_required
  handoff_policy: no_summary_only_handoff
  evidence_policy: source_linked_evidence_items_required
```

This is a governance expectation.

It is not a dispatch instruction.

The current schemas are unchanged.

Any future schema update is protected work.

### Evidence Pack implications

Future Evidence Pack examples may record:

- selected topology;
- why the topology was chosen;
- worker outputs treated as Evidence Items;
- summary-only handoffs rejected or blocked;
- contradictions preserved;
- synthesis limitations;
- unresolved evidence gaps;
- User Decision Gate impact.

Evidence Packs must not become runtime traces or chain-of-thought archives.

### Read-only Doctor implications

Future read-only checks may eventually flag:

- docs claiming multi-agent improves reliability by default;
- role profiles being treated as Pantheon authority;
- summary-only handoffs in examples;
- Hermes swarm described as approval authority;
- runtime state described as memory;
- topology fields described as executable dispatch instructions.

These checks must remain read-only.

They must not execute workflows or dispatch workers.

### Example sequence before schema work

Recommended next sequence:

1. Add a fictional Task Contract example using `single_primary_reasoning_context`.
2. Add a fictional Task Contract example using `fanout_extract_then_single_synthesis`.
3. Add a fictional Task Contract example using `persistent_role_team_handoff` for artifact-bound work.
4. Add a fictional Evidence Pack example showing Evidence Items from workers.
5. Add a User Decision Gate example where topology choice affects risk or cost.
6. Only then consider schema changes under the protected-file rule.

### Final rule

```text
Swarm for collection.
Role-team handoff for bounded artifact stages.
Single context for inference when evidence must connect.
Governance College for review.
User Decision Gate for unresolved stakes.
Human decision for consequential approval.
```


---

## Reconciliation note

Original status: active reconciliation note — documentation-level only.

Date: 2026-05-30

This document reconciles the new Evidence Topology Gate material with the current governance corpus without replacing the main indexes in a risky bulk edit.

It is a lightweight bridge for `README.md`, `docs/governance/STATUS.md`, `CHANGELOG.md` and `docs/governance/README.md`.

It does not replace those documents.

It does not implement runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Why this reconciliation note exists

The Evidence Topology Gate doctrine was added after analysis of single-agent, multi-agent, swarm and persistent role-team patterns.

The doctrine adds an important rule:

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

The main governance indexes should eventually point to this doctrine, but large index replacements were avoided to reduce merge and SHA-conflict risk.

This note records the reconciliation target explicitly.

### Documents to index later

The following documents should be referenced in the main governance index during a focused reconciliation pass:

- `EVIDENCE_TOPOLOGY_GATE.md` (removed; git history);
- `EVIDENCE_TOPOLOGY_ROADMAP.md` (removed; git history);
- `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` (removed; git history);
- `EVIDENCE_TOPOLOGY_BRIDGES.md` (removed; git history);
- `docs/examples/evidence_topology/README.md`.

### Recommended placement

#### `docs/governance/README.md`

Recommended additions:

- add `EVIDENCE_TOPOLOGY_GATE.md` to the core bootstrap read order after `EVIDENCE_PACK.md` or before `HERMES_INTEGRATION.md`;
- add `EVIDENCE_TOPOLOGY_ROADMAP.md`, `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` and `EVIDENCE_TOPOLOGY_BRIDGES.md` as support/reconciliation documents;
- add `docs/examples/evidence_topology/` to examples navigation.

#### `docs/governance/STATUS.md`

Recommended status entry:

```text
Evidence Topology Gate is active doctrine for reasoning topology selection, proof-chain preservation, bounded Hermes swarm and persistent role-team handoff constraints.
```

Explicit non-implementation note:

```text
It does not add a runtime, worker dispatcher, scheduler, queue, graph engine, schema, test, operation, platform component, OpenWebUI plugin or Hermes configuration.
```

#### `CHANGELOG.md`

Recommended future changelog item:

```text
Added Evidence Topology Gate doctrine, roadmap addendum, fictional examples, schema candidate note and doctrine bridges for single-context, fan-out extraction, persistent role-team handoff and bounded Hermes swarm governance.
```

#### Root `README.md`

Recommended public-facing summary:

```text
Pantheon does not choose between single-agent and multi-agent as a slogan. It first asks what shape the proof has. When evidence must be connected across sources, Pantheon preserves a single primary reasoning context. When extraction can safely be distributed, workers return evidence items, not authority.
```

### Current active content

Current active doctrine already exists in:

- `EVIDENCE_TOPOLOGY_GATE.md` (removed; git history).

Current roadmap addendum exists in:

- `EVIDENCE_TOPOLOGY_ROADMAP.md` (removed; git history).

Current fictional examples exist in:

- `docs/examples/evidence_topology/`.

### Boundary

This reconciliation note is documentation-level only.

It does not:

- add or modify schemas;
- add tests;
- add operations tooling;
- modify platform files;
- modify Docker or environment configuration;
- execute Hermes;
- define an OpenWebUI plugin;
- create a LangGraph runtime;
- create a swarm controller;
- create a message bus;
- promote memory;
- approve external tools.

### Final rule

```text
Index the doctrine carefully.
Do not turn topology governance into topology execution.
```


---

## Schema candidate note

Original status: schema candidate note — not implemented.

Date: 2026-05-30

This document proposes possible future schema fields for Evidence Topology Gate support.

It is not a schema.

It does not modify files under `schemas/`.

It is not validation logic.

It is not runtime configuration.

It is not a Hermes dispatch contract.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Purpose

`EVIDENCE_TOPOLOGY_GATE.md` defines reasoning topology doctrine.

The fictional examples under `docs/examples/evidence_topology/` show how topology metadata might appear in future Task Contract and Evidence Pack examples.

This document records candidate fields before any protected schema work.

No field below is active schema until separately reviewed and approved.

### Candidate Task Contract field

Candidate field name:

```yaml
reasoning_topology:
  selected: single_primary_reasoning_context
  reason: cross_source_reasoning_required
  handoff_policy: no_summary_only_handoff
  evidence_policy: source_linked_evidence_items_required
```

Possible `selected` values:

```text
single_primary_reasoning_context
fanout_extract_then_single_synthesis
parallel_independent_workers
router
sequential_handoff
persistent_role_team_handoff
bounded_hermes_swarm
```

This field would declare governance expectations.

It must not be interpreted as runtime dispatch.

### Candidate additional Task Contract fields

```yaml
reasoning_topology:
  selected: persistent_role_team_handoff
  reason: artifact_bound_stage_work
  handoff_policy: bounded_artifact_required
  evidence_policy: handoff_artifacts_and_evidence_items_required
  memory_policy: role_memory_is_not_canonical_memory
  approval_policy: external_effect_requires_gate
  topology_risks:
    - role_memory_confused_with_canonical_memory
    - team_chat_confused_with_evidence_pack
    - handoff_confused_with_approval
  forbidden_handoffs:
    - summary_only_handoff
    - recommendation_without_source_locator
    - direct_publication_without_gate
```

Potential requirements:

- `selected` should be required when task risk is non-trivial;
- `reason` should be human-readable;
- `handoff_policy` should block summary-only transfer for consequential work;
- `evidence_policy` should indicate whether Evidence Items or Handoff Artifacts are expected;
- `approval_policy` should identify where execution must stop.

### Candidate Evidence Item shape

```yaml
evidence_item:
  evidence_id: ei-example-001
  claim: "Class X controls behavior Y"
  source_type: java_source
  source_ref: "src/path/ClassX.java:L120-L156"
  source_location: "method renderSummary"
  supports: ticket_intention_trace
  scope_of_support: "Only supports behavior Y under condition Z"
  confidence: medium
  limitations:
    - "Runtime behavior not tested"
  open_questions:
    - "Does XML condition A gate this branch?"
  scope_warnings:
    - "Do not generalize to adjacent ticket"
```

Candidate rule:

```text
Evidence Items support review.
They are not final conclusions.
```

### Candidate Handoff Artifact shape

```yaml
handoff_artifact:
  handoff_id: ha-example-001
  type: api_contract_note
  from_role: backend
  to_role: frontend
  scope: "New billing endpoint for dashboard display only"
  artifact_ref: "docs/contracts/billing-api-draft.md"  # fictional example path
  changed_surface:
    - "GET /api/billing/summary"
  assumptions:
    - "Authentication middleware unchanged"
  blockers:
    - "Response pagination not validated"
  evidence_refs:
    - ei-example-001
  approval_gap: "Frontend may adapt UI, but deployment remains blocked pending review"
```

Candidate rule:

```text
A Handoff Artifact may preserve continuity.
It does not approve the next action.
```

### Candidate Evidence Pack topology section

```yaml
reasoning_topology_record:
  selected: fanout_extract_then_single_synthesis
  reason: many_sources_need_bounded_extraction_but_final_reasoning_must_be_unified
  rejected_topologies:
    - summary_only_supervisor_synthesis
    - unbounded_multi_agent_supervised
  worker_outputs_used:
    - ei-quote-001
    - ei-cctp-001
  handoff_artifacts_used: []
  contradictions_preserved:
    - c-quote-cctp-001
  unresolved_gaps:
    - missing_full_cctp
  approval_impact: user_decision_gate_required_before_external_transmission
```

Candidate rule:

```text
The Evidence Pack records why topology was chosen.
It must not store hidden chain-of-thought or raw runtime traces.
```

### Candidate validation constraints

Potential future validation constraints, if schemas are later changed:

- `selected` must be one of the approved topology values;
- `selected = single_primary_reasoning_context` should require evidence policy for source-linked claims;
- `selected = fanout_extract_then_single_synthesis` should forbid worker final conclusions;
- `selected = persistent_role_team_handoff` should require Handoff Artifacts and memory boundary notes;
- `selected = bounded_hermes_swarm` should require Task Contract scope and approval gap declaration;
- topology metadata must not include runtime IDs as primary governance identifiers;
- topology metadata must not imply dispatch, scheduling, queueing or provider routing.

### Protected work warning

Any real schema change requires separate confirmation because schema files are protected work.

Protected future files include, at minimum:

- `schemas/task_contract.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/workflow_manifest.schema.yaml` if topology is ever reflected there;
- schema examples under `schemas/examples/`.

This document does not authorize those changes.

### Rejected schema drift

Reject these future schema mistakes:

```text
reasoning_topology as runtime dispatcher
reasoning_topology as worker scheduler
Evidence Item as approval
Handoff Artifact as approval
role memory as a Registre Probatoire entry
runtime trace as Evidence Pack
OpenWebUI display state as governance state
Hermes worker state as Pantheon state
```

### Recommended future sequence

1. Stabilize doctrine and examples.
2. Review whether `reasoning_topology` belongs in Task Contract only, Evidence Pack only, or both.
3. Review compatibility with `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`, `HERMES_INTEGRATION.md`, `MEMORY.md` and `SCOPE_ISOLATION.md`.
4. Request explicit confirmation before touching `schemas/`.
5. Add tests only after schema structure is approved.

### Final rule

```text
Describe topology before execution.
Do not make topology description execute anything.
```


---

## Historical changelog addendum (D2)

Original status: changelog addendum.

Date: 2026-05-30


This addendum records the protected schema pass for Evidence Topology.

It exists because the main `CHANGELOG.md` is long and connector reads were truncated during this pass. A broad replacement was avoided to prevent accidental history loss.

### Summary

Evidence Topology doctrine is now reflected in the two central governance schemas:

- `schemas/task_contract.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`.

The official schema examples were updated accordingly.

### Added to Task Contract schema

Optional field:

```text
reasoning_topology
```

Supported topology values:

```text
single_primary_reasoning_context
fanout_extract_then_single_synthesis
parallel_independent_workers
router
sequential_handoff
persistent_role_team_handoff
bounded_hermes_swarm
```

Boundary:

```text
reasoning_topology is governance metadata.
It is not runtime dispatch.
```

### Added to Evidence Pack schema

Optional fields:

```text
evidence_items
handoff_artifacts
reasoning_topology_record
```

Boundary:

```text
Evidence Items support review.
Handoff Artifacts preserve continuity.
Topology Records preserve accountability.
None of them approve, dispatch, execute or promote memory.
```

### Examples updated

- `schemas/examples/task_contract.example.yaml`;
- `schemas/examples/evidence_pack.example.yaml`.

### Tests added

- `tests/test_schema_examples.py`.

The test validates schema examples and checks that Evidence Topology remains non-runtime through boundary flags:

```text
topology_dispatch: false
hidden_chain_of_thought_archive: false
```

### Explicitly not implemented

This pass does not implement:

- runtime behavior;
- topology dispatcher;
- provider routing;
- scheduler;
- queue;
- graph runtime;
- Hermes execution;
- OpenWebUI plugin behavior;
- automatic approval;
- automatic memory promotion.

It does not modify:

- `workflow_manifest.schema.yaml`;
- operations tooling;
- platform files;
- Docker files;
- environment files.

### Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

### Core rule

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```
