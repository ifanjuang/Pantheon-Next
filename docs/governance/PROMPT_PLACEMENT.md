# Prompt Placement

Status: active support doctrine — prompt placement, authority separation and non-runtime prompt architecture.

This document defines where prompts, system prompts, profile prompts, skill prompts and flow prompts may live across Pantheon Next, OpenWebUI, Hermes Agent, Langflow, LangGraph and observability layers.

It does not implement prompt injection, prompt routing, prompt registry, prompt versioning backend, provider routing, OpenWebUI Function, Hermes skill installation, Langflow flow, LangGraph runtime or Langfuse prompt management.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core rule

```text
Do not copy the whole doctrine into every prompt.
Distill the minimum operational instruction required by that layer.
```

A prompt should never gain more authority than the layer where it lives.

## Why placement matters

The same sentence has different status depending on where it lives.

Example:

```text
Found source is not proof.
```

- in Pantheon doctrine, it is a canonical governance rule;
- in OpenWebUI, it is a display and warning instruction;
- in Hermes, it is an execution constraint;
- in Langflow, it is a bounded transformation constraint;
- in Langfuse, it is trace metadata only.

Those meanings must not collapse.

## Prompt layers

### Pantheon doctrine prompt

Pantheon may hold long-form canonical doctrine, governance constraints, role definitions, approval rules, evidence rules, memory rules and placement rules.

Pantheon prompts are source doctrine for distillation.

They are not runtime prompts by default.

They must not become agent runtime prompts, provider router prompts, auto-orchestration prompts, hidden workflow prompts, auto-approval prompts or auto-memory prompts.

### OpenWebUI cockpit prompt

OpenWebUI prompts should be short, user-facing and status-oriented.

They may instruct the cockpit to:

```text
display candidate status
distinguish draft from deliverable
distinguish retrieved knowledge from evidence
distinguish Memory Candidate from Canonical Memory
ask for approval before external effect
open User Decision Gate when required
avoid presenting candidates as validated
```

They must not decide approval, canonize memory, route providers, run tools freely, mutate a repository, execute the Governance College, silently rewrite user intent or become a source of truth.

### Hermes profile prompt / soul

Hermes profile prompts may constrain execution style and output status.

They may map to Pantheon Roles, but they do not inherit Pantheon Role authority.

They may instruct Hermes to:

```text
execute under Task Contract
return candidates only
report capability gaps
preserve source and risk notes
produce patch candidates, not merges
produce Memory Candidates, not Canonical Memory
produce Evidence Pack Candidates, not approval
```

They must not approve final output, promote memory, mutate doctrine, bypass approval, merge directly, change scope silently or hide unresolved conflict.

### Hermes skill prompt

Hermes skill prompts should be narrow and task-specific.

They may define input expectations, output format, forbidden outputs and escalation conditions for one capability.

Examples:

```text
source_audit
repo_patch_candidate
evidence_pack_builder
pdf_ingestion_review
architecture_devis_analysis
memory_candidate_extractor
```

A skill prompt must return bounded outputs.

It must not change governance status by itself.

### Langflow flow prompt

Langflow prompts may support deterministic or repeatable preparation: extraction, normalization, redaction preparation, chunk review or skeleton generation.

They must not approve, arbitrate, canonize or create durable memory.

### LangGraph runtime prompt

LangGraph prompts, if used, belong to external runtime execution behind Hermes or a governed bridge.

They may support durable interrupted work, but their state is Runtime State.

A LangGraph prompt must not become Pantheon doctrine, Evidence Pack, Canonical Memory or approval.

### Langfuse prompt record

Langfuse may record prompt versions or trace metadata for observability.

A Langfuse prompt record is not governance doctrine.

A Langfuse trace is not an Evidence Pack.

### GraphRAG prompt

GraphRAG or graph-query prompts may support provenance search, relationship discovery and contradiction review.

They must not treat graph connectivity as truth.

Graph retrieval becomes evidence only when selected and represented in an Evidence Pack.

## Distillation model

```text
Pantheon doctrine
-> OpenWebUI cockpit instruction
-> Hermes profile constraint
-> Hermes skill instruction
-> Langflow transformation prompt
-> trace metadata
```

Distillation must be lossy by design.

Each layer receives only what it needs.

## Minimal prompt declaration

A prompt template should declare:

```text
owner_layer
purpose
allowed_inputs
allowed_outputs
forbidden_outputs
memory_behavior
approval_behavior
scope_behavior
escalation_behavior
status
```

For non-executable templates, these fields are documentation scaffolding only.

They are not runtime configuration.

## Placement matrix

| Prompt type | Where it belongs | Authority | Must not do |
|---|---|---|---|
| Doctrine prompt | Pantheon docs | Canonical governance | execute |
| Cockpit prompt | OpenWebUI template | Display / decision capture | approve or execute |
| Profile soul | Hermes profile | Candidate execution style | govern |
| Skill prompt | Hermes skill candidate | Narrow execution constraint | canonize |
| Flow prompt | Langflow candidate | Deterministic preparation | decide |
| Runtime prompt | LangGraph behind Hermes / bridge | External execution state | become memory |
| Trace prompt record | Langfuse | Observability | replace evidence |
| Graph prompt | GraphRAG candidate | Retrieval / relation discovery | decide truth |

## Rejected patterns

Reject:

```text
single global Pantheon mega-prompt
OpenWebUI system prompt as governance source of truth
Hermes soul redefining Pantheon Role authority
skill prompt approving its own output
Langflow prompt performing final judgment
LangGraph prompt promoting checkpoint to memory
Langfuse prompt version treated as approval
Graph prompt treated as proof
```

## Example distillation

Canonical Pantheon doctrine:

```text
Retrieved knowledge is not evidence.
```

OpenWebUI cockpit distillation:

```text
Show retrieved material as retrieved until it is selected into an Evidence Pack.
```

Hermes Argos distillation:

```text
Return retrieved sources with source status and evidence_candidate flags. Do not mark them as validated.
```

Langflow distillation:

```text
Extract candidate source references and supported claims. Do not validate claims.
```

Langfuse metadata:

```text
retrieval_status=retrieved
```

## Final rule

```text
Doctrine governs.
Prompts operationalize only the part of doctrine their layer is allowed to carry.
No prompt may promote its own output into truth, approval or memory.
```
