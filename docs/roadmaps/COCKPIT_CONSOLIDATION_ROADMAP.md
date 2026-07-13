# Pantheon Next — Consolidation, Cockpit and Resolver Roadmap

Status: validation-only roadmap — documented non-implemented.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## Purpose

This roadmap is the product sequence after the repository audit. It does not replace technical issues, owner documents or human decisions. It orders them.

```text
roadmap != authority
issue closed != doctrine promoted
CI green != safe
external implementation != Pantheon adoption
```

## Two-level work governance

Only two programme-level trackers remain:

```text
#377 = remediation gate for audit findings and repository controls
this roadmap = product sequence after the relevant remediation gates
```

Technical issues remain the units of work. A roadmap issue must not duplicate a stricter audit issue.

## Status vocabulary

Every work item must distinguish:

```text
implemented in Pantheon Next
implemented externally and observed at a pinned revision
verified within a declared review scope
partially integrated
adopted by explicit human decision
activated under a valid authorization
 documented non-implemented
to verify
obsolete
not applicable
```

## Phase 0 — Audit remediation gate

Owner: #377.

No Phase B or C change may merge while a relevant audit gate remains unresolved or has not been explicitly deferred by a human.

Priority controls include:

```text
#362 — Governance Doctor fail-closed
#363 — authority-index resolution and test coverage
#361 / PR #375 — strict evidence validation
```

Common exit rules:

- all required checks are green on the latest head;
- external claims include repository, commit SHA, observation date and review scope;
- unresolved review threads are either fixed or explicitly rejected with rationale;
- `observed`, `verified`, `integrated`, `adopted` and `activated` are not collapsed.

## Phase 1 — Card Stack single-source reconciliation

### 1A — active doctrine cleanup

Delivery PR: #376. Tracking issue: #371.

Required result:

```text
CARD_STACK_MODEL.md = sole active Card Stack owner
CARD_STACK_HARDENING_NOTE.md = obsolete historical record
Scene = bounded filtered ordered projection
Scene != exhaustive graph
Gate != Decision
UI intent != Hermes execution
```

The obsolete note must be absent from active indexes and present in the obsolete/superseded index.

### 1B — prototype compliance gate

Owner: #364.

#371 closes only the narrow README/index task. #364 remains open until the Card Stack asset and prototype satisfy:

- asset registry and authority coverage;
- static/non-functional controls are explicit;
- no clipped full cards masquerade as compact cards;
- semantic and accessible controls;
- `recorded != current` is visible;
- no active exhaustive-Scene wording;
- full governance checks green.

Legacy PR #358 must not merge. It is replaced only after a clean current-main prototype PR exists.

## Phase 2 — Source, ingestion and retrieval reconciliation

Owner: #366.

Issue #372 is not an independent gate; it is a roadmap decomposition of #366 and should be closed as duplicate/superseded.

Required model:

```text
Source
→ Derived Representation Candidate
→ bounded retrieval object
→ Retrieval Trace
→ Evidence Candidate when deliberately selected for one scoped Assertion
```

Owner documents remain:

- `RAW_DERIVED_GOVERNED_RECORDS.md` for the layered data model;
- catalogue documents for Capability, Resource, Preset and Binding;
- evidence documents for Evidence semantics;
- Register documents for durable validated memory.

Required status matrix:

```text
implemented in Pantheon Next:
- documentation;
- declarative catalogue entries;
- validation traces and static projections.

implemented externally and observed:
- pantheon-mvp bounded retrieval/candidate loop at a pinned commit.

partial integration:
- bounded conformance evidence;
- fixture-backed demonstration;
- declared but non-adopted handoff assumptions.

not implemented in Pantheon Next:
- live connector framework;
- generic ingestion runtime;
- Docling live binding;
- production source cockpit.
```

Required distinctions:

```text
Source != Evidence
retrieved != true
high score != authority
runtime success != evidence
ingested != Register Entry
binding selected != dependency adopted
verified != adopted
```

Legacy PR #355 must not merge. Close it only when the clean replacement PR is open and traceable.

## Phase 3 — External vertical truth and status reconciliation

Owner: #367.

After Phase 2, re-observe `pantheon-mvp` at an exact commit and reconcile in one change set:

- `WHAT_RUNS.md`;
- `PANTHEON_MVP_VERTICAL_BINDING.md`;
- its reference review;
- runtime-adapters authority index;
- remaining adoption blockers.

Required separation:

```text
external repository verified
implementation observed
governance evidence accepted
binding adopted
runtime activated
```

Resolved historical blockers remain visible as resolved history, not active P0 findings.

## Phase 4 — Card Stack prototype and cockpit visual language

### 4A — compliant illustrative prototype

Owner: #364.

The clean prototype must demonstrate:

- one shared card anatomy;
- controlled variation by type without colour-only semantics;
- explicit compact and expanded cards;
- one unambiguous scene navigation;
- separate global modes such as Reference Space or Constellation;
- Decision currentness separate from record existence;
- keyboard focus, semantic markup and accessible labels;
- no hidden execution path.

```text
prototype present != renderer implemented
UI control != Hermes command
Action Candidate != execution
Cluster != governance object
```

### 4B — broader visual-language evolution

Owner: #373. Dependency: #364 closed.

#373 may generalize visual rules only after the prototype is compliant and reviewed by a human. It must remain subordinate to `CARD_STACK_MODEL.md` unless a separate promotion decision creates a new owner document.

Do not split prematurely into multiple canonical documents for anatomy, motion, colour and layout.

## Phase 5 — transverse terminology audit

Run after Phases 1–4, because those phases remove known contradictions.

Review at minimum:

```text
implemented
external
verified
integrated
adopted
activated
runtime
Run
workflow
Gate
Decision
approval
Evidence
memory
Register
current
authorized
healthy
safe
```

Every correction must point to an existing owner document. The audit creates no new ontology by default.

## Phase 6 — Current Decision Resolver

Owner: #374.

Hard dependencies:

```text
#364 closed
#366 closed
#367 closed or explicitly bounded by human decision
HandoffDecision contract stable
prototype no longer implies recorded = current
relevant #377 remediation gates closed
```

The resolver answers only:

> Which recorded human Decision is currently applicable to this exact subject, scope and evaluation time?

Inputs include validated Decision records, exact subject, exact scope, effective time, expiry, revocation and supersession.

Output is a read-only derived projection such as `CurrentDecisionProjection`.

Required outcomes:

```text
none
current
blocked
ambiguous
invalid-record-set
```

Required invariants:

```text
recorded != current
current != execution_started
current approval != activation
valid at time T != perpetual permission
scope match != global scope
revoked != rolled_back
expired != revoked
resolver output != human decision
```

The resolver never calls Hermes, a provisioner, a connector or an external action.

## Phase 7 — return to the existing executable vertical

Reuse the existing vertical; do not start a competing one.

```text
Task Contract
→ bounded external retrieval/drafting
→ Candidate Output
→ Evidence Pack Candidate
→ Human Decision
→ Register Candidate
→ Current Decision Projection where applicability is queried
```

Then replace stand-ins one at a time:

```text
terminal gate stand-in → authenticated OpenWebUI decision surface
deterministic drafter → bounded Hermes-side Drafter
local fixtures → one scoped external Source adapter
basic document representation → Docling Derived Representation Candidate
```

Each replacement has its own Pantheon gate. Selecting one binding does not adopt the next dependency.

## Active issue hierarchy

```text
#377 — programme remediation gate
├─ #362, #363, #361/#375 — repository controls
├─ #364 — Card Stack compliance and prototype gate
├─ #366 — Source/Retrieval truth and status gate
├─ #367 — external vertical truth/status gate
└─ #368 — iFixAi external-reference remediation

#371 — narrow subtask delivered by #376; closes at merge
#372 — duplicate/superseded by #366
#373 — visual-language evolution after #364
#374 — Current Decision Resolver after #364/#366/#367
```

## Pull-request discipline

Each PR must state:

```text
what Pantheon governs
what Hermes executes
what OpenWebUI exposes
what the human approves
what remains forbidden
owner documents affected
implemented / external / partial / non-implemented status
non-equivalence rules preserved
issue that owns the work
legacy PRs superseded
```

## Immediate work order

```text
1. finish and merge #376; close #370 and #371.
2. finish repository-control gates relevant to this programme under #377.
3. open the clean Source/Retrieval replacement; close #355 and #372; satisfy #366.
4. satisfy #367 with pinned external evidence.
5. open the clean Card Stack prototype replacement; close #358; satisfy #364.
6. continue #373 only after human visual review.
7. run the terminology audit.
8. start #374.
9. return to the existing vertical.
```

The human remains the final authority for promotion, adoption, activation and consequential action.
