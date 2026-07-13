# Pantheon Next Cockpit Consolidation Roadmap

Status: validation-only roadmap — documented non-implemented.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## Purpose

This roadmap sequences the remaining consolidation work before the Current Decision Resolver and the next executable vertical slice. It is a planning artifact, not governance authority. It creates no runtime, renderer, scheduler, queue, approval engine, memory engine, connector, installer or external action.

It distinguishes:

```text
implemented in Pantheon Next
externally observed or verified candidate
partial
documented non-implemented
to verify
obsolete
not applicable
```

## Sequence

```text
Phase A — zero documentary debt
Phase B — cockpit visual language
Phase C — deterministic current-state projections
Phase D — return to the executable vertical
```

A later phase must not silently stabilize terms or behavior that remain unresolved in an earlier phase.

# Phase A — Zero documentary debt

## A1 — Card Stack single-source reconciliation

Goal: one current Card Stack rule set.

Actions:

1. remove active-index references to retired `CARD_STACK_HARDENING_NOTE.md`;
2. replace the obsolete exhaustive Workflow Scene wording in governance navigation;
3. preserve:

```text
A Scene is a bounded, filtered and ordered projection
complete enough for governed review.
A Scene is not an exhaustive graph.
```

4. keep Card, Scene, Deck, Cluster and Constellation as UX projections, not governance entities;
5. keep Gate and Decision distinct;
6. keep UI intent separate from Hermes execution.

Acceptance criteria:

```text
retired file absent from active indexes;
no active exhaustive-Scene instruction;
Governance CI green;
no status promotion;
no runtime or renderer added.
```

## A2 — Source / ingestion / retrieval reconciliation

Goal: finish the clean replacement for historical PR #341.

Required classification:

```text
implemented in Pantheon Next:
- documentation model;
- catalogue declarations;
- validation traces and static projections.

externally observed or verified candidate:
- pantheon-mvp scoped retrieval and candidate-production loop.

partial:
- integration evidence posture;
- local fixtures and pgvector-backed executable candidate behavior;
- bounded external handoff assumptions.

documented non-implemented in Pantheon Next:
- generic Source Registry;
- live connector framework;
- live Google Drive ingestion;
- Docling live binding;
- OCR orchestration;
- generic multi-source retrieval resolver;
- production OpenWebUI source cockpit.
```

Required invariants:

```text
Source != Evidence
retrieved != true
high score != authority
ingested != Register Entry
binding selected != dependency adopted
runtime success != evidence
externally implemented != adopted by Pantheon
```

Acceptance criteria:

```text
no implemented/partial contradiction;
correct authority-index placement;
no unresolved review comments;
Governance CI green;
merge without promotion.
```

## A3 — Transverse terminology audit

Search and review at minimum:

```text
exhaustive
implemented
runtime
memory
register
approval
run
workflow
gate
decision
source
evidence
healthy
safe
installed
approved
activated
```

Classify findings as:

```text
valid owner usage
valid local alias
ambiguous
contradictory
obsolete
not applicable
```

Preserve:

```text
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
binding_selected != dependency_adopted
watchlist_item != install_instruction
recorded != current
approved != activated
```

Deliverable: validation-only audit log and minimal corrective PRs. Do not create a new vocabulary owner unless an existing owner cannot absorb the rule.

# Phase B — Cockpit visual language

## B1 — Complete the current Card Stack prototype

Required corrections:

1. distinguish project-scene navigation from global-space navigation;
2. replace clipped cards with an explicit compact-card anatomy;
3. show that `recorded` does not imply `current` for decisions;
4. retain one shared card anatomy;
5. vary only accent, border weight, glyph, typography emphasis, density and consequence indicator;
6. preserve accessibility independent of colour.

The prototype remains static and illustrative.

## B2 — Card Visual Language

Create one bounded owner document before splitting into multiple specifications:

```text
CARD_VISUAL_LANGUAGE.md
```

It should define:

```text
shared anatomy
semantic variation axes
compact and expanded states
front and detail surfaces
status placement
consequence emphasis
accessibility constraints
relation to source-object status
prohibited visual equivalences
```

It must not redefine object truth, lifecycle or authorization.

## B3 — Scene, Deck and Cluster projection

A `Cluster` may exist only as a visual grouping primitive:

```text
Project
→ Scene
→ Deck
→ visual Cluster
→ Card projection
```

```text
Cluster != governance object
Cluster != workflow
Cluster != memory
Cluster != decision scope
Cluster ordering != authority
```

## B4 — Interaction model

Document and prototype, without runtime wiring:

```text
vertical scroll = Deck depth
horizontal swipe = sibling cards at one level
tap = bounded detail
long press or action menu = prepare intent or Action Candidate
constellation = relation overview
back = navigation history, not memory rollback
```

Accessibility requirements:

```text
keyboard focus
semantic controls
ARIA labels and selected states
minimum touch target
status not colour-only
reduced-motion mode
```

## B5 — Motion model

Motion may communicate hierarchy, transition, supersession or blocked state. It must not imply approval, truth or execution.

```text
animation success != runtime success
transition complete != decision effective
visual unlock != authorization
```

# Phase C — Deterministic current-state projections

Pantheon resolves; it does not decide.

## C1 — Current Decision Resolver

A deterministic read-only resolver computes which Decision Record is currently applicable for one exact target and scope.

Inputs may include:

```text
Decision Records
target reference
scope
effective_at
expires_at
supersedes
revocation
status
resolution time
```

Output:

```text
Current Decision Projection
```

Core invariants:

```text
recorded != current
approved != activated
current approval != execution started
scope match required
expired blocks applicability
revoked blocks applicability
superseded is historical
resolver output != human decision
```

The resolver must not approve, revoke, activate, execute, schedule, issue credentials, call a provisioner or promote memory.

## C2 — Current Gate Projection

Derive the current Gate view from owner objects, evidence posture and Current Decision Projection. Do not create an automatic approval engine.

## C3 — Current Status Projection

Compute separate axes:

```text
maturity
installation
health
safety
authorization
update
evidence
activation
```

## C4 — Current View Projection

Feed OpenWebUI-facing cards and scenes from deterministic projections.

```text
projection != source object
view cache != durable Register Entry
UI state != governance state
```

# Phase D — Return to the executable vertical

Only after Phases A-C are stable.

Sequence:

```text
finish Block 3 in pantheon-mvp
retain or persist Register Candidate under explicit governance
replace declared terminal identity with authenticated OpenWebUI review
connect Hermes-side Drafter under the existing task contract
add one bounded external source
add Docling only as a Derived Representation Candidate binding
project the loop in the governed cockpit
```

Reference path:

```text
Task Contract
→ bounded ingestion
→ scoped retrieval
→ Candidate Output
→ Evidence Pack Candidate
→ Human Decision
→ Register Candidate
```

Do not start a competing vertical or introduce a generic Source Registry, Knowledge Registry or Flow Registry before the current loop proves the required boundaries.

# Pull-request discipline

Every PR must state:

```text
what Pantheon governs
what Hermes executes
what OpenWebUI exposes
what the human approves
what remains forbidden
implemented / external / partial / documented non-implemented status
owner documents affected
non-equivalence rules preserved
```

```text
merged != promoted
prototype present != renderer implemented
documented != activated
CI green != safe
```

# Immediate work order

```text
1. Card Stack index and README reconciliation.
2. Rebuild and finish Source / Retrieval on current main.
3. Complete Card Stack prototype corrections.
4. Run transverse terminology audit.
5. Merge visual-language candidate only after human review.
6. Specify and implement the read-only Current Decision Resolver.
7. Return to pantheon-mvp vertical integration.
```

The human remains the final authority for promotion, activation and consequential action.
