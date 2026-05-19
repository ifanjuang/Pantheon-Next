# Evidence Topology Gate

Status: active doctrine — reasoning topology, evidence preservation and Hermes swarm constraint.

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

## Core thesis

The unit of reasoning is not the agent.

The unit of reasoning is the proof chain.

```text
Preserve the proof chain before distributing reasoning.
```

A task should not be split into specialist agents merely because the system can split it.

A task should be split only when the shape of the evidence justifies distribution.

## Purpose

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

## Canonical rule

When a task requires cross-source inference, preserve one primary reasoning context.

Workers may collect, filter, normalize or verify bounded evidence.

Workers must not replace the inference chain unless their domains, artifacts or stages are genuinely independent.

No summary-only handoff is allowed for decision-critical work.

Every handoff must preserve source references, claim scope, uncertainty, limitations and open questions.

Persistent role teams are allowed only when role boundaries are explicit and the handoff artifact is reviewable.

## Default posture

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

## Allowed topologies

### 1. Single primary reasoning context

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

### 2. Fan-out extraction, single synthesis

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

### 3. Parallel independent workers

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

### 4. Router

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

### 5. Sequential handoff

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

### 6. Persistent role-team handoff

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

That role memory is not Pantheon Canonical Memory.

Auto-captured knowledge is not approved doctrine.

Agent-to-agent handoff is not approval.

A visible canvas is not an Evidence Pack by itself.

The value of this topology is continuity, not automatic truth.

### 7. Bounded Hermes swarm

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

## Forbidden topology

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

## Handoff contract

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

## Evidence Item shape

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

## Handoff Artifact shape

A persistent role-team handoff should produce a bounded artifact.

Example:

```yaml
handoff_artifact:
  type: api_contract_note
  from_role: backend
  to_role: frontend
  scope: "New billing endpoint for dashboard display only"
  artifact_ref: "docs/contracts/billing-api-draft.md"
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

## Task Contract expectation

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

## Topology decision matrix

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

## Relationship to Hermes

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

## Relationship to the Governance College

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

## Relationship to Evidence Packs

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

## Relationship to OpenWebUI

OpenWebUI may expose the topology choice, evidence state, worker checkpoints, Handoff Artifacts, Evidence Items, blocked handoffs, User Decision Gates and approval requests.

OpenWebUI does not choose topology as authority by itself.

OpenWebUI display does not validate the topology.

A visible agent conversation canvas is useful operational UI.

It is not governance validation by itself.

The user may be asked to decide when the topology choice changes scope, risk, cost, timing, external effect or memory impact.

## Relationship to memory

Topology traces, worker summaries, runtime state, role memory and repeated observations are not memory.

A topology outcome may propose a Memory Candidate only when the Evidence Pack supports it and memory rules allow it.

No worker, swarm, role, role-team, retrieval result or repeated conclusion may promote Canonical Memory automatically.

Role memory may be useful for voice, procedure or project continuity.

Pantheon must still treat it as runtime-side memory unless promoted through governed Memory Candidate review.

## Relationship to external inspirations

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
role-team memory means Canonical Memory.
runtime trace means Evidence Pack.
critic approval means final approval.
visible canvas means governance validation.
```

## Anti-patterns

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
role memory as Canonical Memory
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

## Final rule

```text
Do not distribute judgment before preserving the proof chain.

Swarm for collection.
Role-team handoff for bounded artifact stages.
Single context for inference when evidence must connect.
Governance College for review.
User Decision Gate for unresolved stakes.
Human decision for consequential approval.
```
