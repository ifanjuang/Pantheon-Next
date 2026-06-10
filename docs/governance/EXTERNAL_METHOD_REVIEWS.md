# External Method Reviews

Status: active support doctrine — method review only.

This document reviews external reasoning, prompting, evaluation and workflow methods as governance inputs.

It does not define hidden orchestration.

It does not implement methods.

It does not approve autonomous agents.

It does not authorize a planner, executor, debate runtime, reflection loop, LLM judge, scheduler, queue, message bus, runtime graph or automatic approval mechanism inside Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Methods can improve output quality.

They can also hide authority drift.

This document answers:

```text
Does this method improve governance review, or does it merely improve autonomous performance?
```

Pantheon may borrow method vocabulary only when it strengthens visibility, evidence, review, scope or approval.

## Method review record format

Recommended fields:

```text
method_name
method_family
capability_summary
governance_value
risk_surface
allowed_distillation
forbidden_import
related_roles
related_artifacts
status
review_notes
```

## Status values

```text
observe
allowed_as_review_pattern
allowed_as_hermes_candidate_method
boundary_required
rejected_as_hidden_runtime
rejected_as_approval_drift
rejected_as_memory_drift
archived
```

## Current method reviews

| Method | Governance value | Main risk | Pantheon posture |
|---|---|---|---|
| ReAct | separates reasoning-style steps from action-style steps conceptually | hidden tool loop or tool autonomy | use only as inspiration for action/evidence separation |
| Chain-of-thought prompting | may improve model reasoning internally | storing or exposing hidden reasoning as evidence | do not store hidden chain-of-thought; use concise rationale and assumptions |
| Self-critique | useful for draft revision and limitation detection | model self-approval | allow as candidate review signal only |
| Reflection loops | can catch errors over iterations | endless self-improvement loop | allow only bounded Hermes-side candidate method under Task Contract |
| Debate | can surface disagreement | hidden multi-agent theater or collusion | replace with visible Governance College role statuses |
| Tree of Thoughts | explores alternatives | uncontrolled branching and session bloat | allow as bounded option exploration, not runtime graph |
| Planner/executor | separates plan and action | Pantheon becomes orchestrator | plan may inform Task Contract; execution remains Hermes-side |
| LLM-as-judge | useful pre-score or consistency signal | score becomes approval | judge output is signal, never final validation |
| Constitutional prompting | explicit rule layer | prompt rules mistaken for Pantheon doctrine | useful as reminder; Pantheon doctrine remains canonical |
| Retrieval-augmented generation | connects answer to sources | retrieval becomes evidence or truth | retrieval is candidate support only |
| GraphRAG-style synthesis | improves corpus-level view | graph/community summary treated as authority | graph output is retrieved context or Evidence Candidate |
| Multi-agent team | role specialization | autonomous hidden agent team | Governance College is role separation, not team runtime |
| Autonomous research agent | breadth of search | source sprawl and unapproved external browsing | Argos-style source review under scope, not autonomy |
| Memory-enhanced agent | continuity | memory without approval and scope | Register Candidate discipline only |
| Browser automation | action capability | external effect without approval | Hermes-only under tool policy and Task Contract |

## Allowed distillation patterns

### Method as review lens

A method may become a review lens when it helps classify:

- source gaps;
- assumptions;
- contradictions;
- risk;
- missing scope;
- delivery readiness;
- approval need;
- memory implication.

### Method as Hermes candidate constraint

A method may belong to Hermes or another external runtime when it controls execution technique, provided Pantheon receives only:

- Task Contract fit;
- evidence summary;
- assumptions;
- risks;
- output candidate;
- capability gaps;
- approval implications.

### Method as User Decision Gate trigger

A method may reveal conflict that should be exposed to the user.

Example:

```text
self-critique finds unsupported claim
→ ARGOS source_insufficient
→ THEMIS risk_detected
→ ZEUS request_source or human_decision_required
```

## Forbidden method imports

Pantheon must not import:

- hidden reasoning traces;
- autonomous debate loops;
- hidden planner/executor loops;
- agent self-reflection as approval;
- LLM judge as final authority;
- self-improvement loops;
- automatic retry loops;
- background research loops;
- unbounded option exploration;
- automatic external action;
- automatic memory update.

## Role mapping

| Method pressure | Pantheon role that can expose it |
|---|---|
| structure, decomposition, plan | ATHENA |
| source adequacy and provenance | ARGOS |
| risk, policy, approval boundary | THEMIS |
| clarity and delivery readiness | APOLLO |
| artifact or patch preparation | HEPHAISTOS |
| recipient and transmission framing | IRIS |
| status and next procedure | ZEUS |

A method may help one role produce a candidate view.

It must not create autonomous role execution inside Pantheon.

## Evidence rule

Method output may appear in an Evidence Pack only as governance-relevant summary.

Allowed:

```text
assumption noted
source gap found
contradiction detected
variant compared
risk escalated
approval required
```

Forbidden:

```text
raw chain-of-thought
private scratchpad
hidden debate transcript
unbounded reasoning trace
agent deliberation archive
```

## Approval rule

No method approves its own result.

A method can produce:

```text
signal
reserve
candidate review
risk note
contradiction note
next action recommendation
```

It cannot produce:

```text
final approval
memory promotion
external transmission authorization
protected file mutation authorization
professional reliance authorization
```

## Memory rule

Method outputs are not memory.

A repeated critique, score, judgment, plan or conclusion may become a Register Candidate only if it satisfies `MEMORY.md` and `SCOPE_ISOLATION.md`.

## Review questions

Before using a method as inspiration, ask:

```text
What does this method make visible?
What does it hide?
Does it improve evidence or only confidence?
Does it preserve human decision?
Does it create hidden execution state?
Does it expand scope?
Does it imply memory?
Does it require tool access?
Does it create external effect?
```

## Relationship to Watchlist

Unreviewed methods belong on `WATCHLIST.md`.

Reviewed methods belong here.

Distilled method patterns may move to `DISTILLATION_REGISTRY.md`.

Rejected method patterns should be recorded in `REJECTED_PATTERNS.md`.

## Forbidden drift

This document must never become:

- prompt library;
- hidden workflow specification;
- autonomous reasoning engine;
- debate runtime;
- LLM judge policy;
- self-improvement loop;
- planner/executor implementation;
- approval automation;
- memory promotion system.

## Final rule

```text
A method is useful when it improves reviewability.
It is dangerous when it replaces review.
```