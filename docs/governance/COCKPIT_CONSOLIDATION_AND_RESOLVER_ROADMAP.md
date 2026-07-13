# Cockpit Consolidation and Resolver Roadmap

Status: candidate implementation roadmap — documented non-implemented.
Boundary profile: candidate_support_note.

This roadmap sequences the remaining consolidation work before Pantheon Next introduces a Current Decision Resolver. It records intent, dependencies and acceptance criteria. It does not authorize implementation, activation, runtime execution, installation, approval automation or durable-memory promotion.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides.
```

## Objective

Move from a coherent governance corpus and static cockpit candidates to a bounded operational governance projection without turning Pantheon into the engine.

The sequence is intentionally:

```text
remove documentary contradictions
→ stabilize external-runtime status language
→ stabilize cockpit visual language
→ audit controlled terms across the repository
→ implement a read-only Current Decision Resolver
→ reconnect the existing pantheon-mvp vertical
```

## Non-goals

This program does not create:

```text
an approval engine;
a workflow engine;
a scheduler or queue;
a connector runtime;
a provider router;
a memory engine;
a plugin manager;
an MCP host;
a Docker or Portainer orchestrator;
a hidden Hermes command path;
a production OpenWebUI extension.
```

## Phase A — zero documentary debt

### A1 — Card Stack single-source reconciliation

Scope:

- remove the retired `CARD_STACK_HARDENING_NOTE.md` row from the registered authority sub-index;
- replace the obsolete exhaustive Work Scene rule in `docs/governance/README.md`;
- retain `CARD_STACK_MODEL.md` as the sole owner of card, Scene, Deck, Constellation and navigation grammar;
- verify no live document presents a deleted companion note as active doctrine.

Required invariant:

```text
Work Scene = complete enough for governed review
Work Scene != exhaustive graph
```

Acceptance criteria:

- no repository reference treats `CARD_STACK_HARDENING_NOTE.md` as active;
- no active navigation document says the Work Scene is exhaustive;
- Governance CI is green;
- merge does not promote `CARD_STACK_MODEL.md` beyond candidate support doctrine.

### A2 — Source and retrieval status reconciliation

Reconstruct the source/retrieval proposal on current `main` and correct the status boundary around the external `pantheon-mvp` repository.

Required classification:

```text
implemented in Pantheon Next:
- documentation and declarative catalogue material;
- validation traces and static projections.

externally observed or verified candidate:
- pantheon-mvp scoped retrieval and candidate-production loop.

partial integration:
- evidence that the external loop conforms to selected contracts;
- local fixtures and pgvector-backed retrieval demonstration.

not implemented in Pantheon Next:
- live connector framework;
- generic ingestion runtime;
- Docling live binding;
- production source cockpit.
```

Required distinctions:

```text
external implementation != Pantheon implementation
verified != adopted
installed != approved
healthy != safe
runtime success != evidence
retrieved != true
ingested != Register Entry
```

Acceptance criteria:

- no item appears under both `implemented` and `partial`;
- `pantheon-mvp` is explicitly external and not adopted by implication;
- owner-document jurisdiction remains with `RAW_DERIVED_GOVERNED_RECORDS.md`, catalogue documents, evidence documents and Register documents;
- Governance CI is green;
- historical PR #355 is closed when its clean replacement is ready.

### A3 — repository-wide terminology audit

Audit active and candidate documents for controlled terms that commonly drift:

```text
exhaustive;
implemented;
integrated;
activated;
adopted;
runtime;
Run;
workflow;
Gate;
Decision;
approval;
Evidence;
memory;
Register;
current;
authorized.
```

For every finding classify:

```text
fact;
local alias;
owner-defined term;
contradiction;
obsolete wording;
non-applicable.
```

Acceptance criteria:

- every correction points to an owner document;
- no bulk rename changes schema or runtime behavior implicitly;
- remaining intentional aliases are documented as UX aliases;
- no new canonical vocabulary is introduced by the audit itself.

## Phase B — Pantheon Cockpit Design Language

### B1 — visual-language owner document

Create one candidate owner document, tentatively `COCKPIT_VISUAL_LANGUAGE.md`, before splitting into narrower companions.

It should define only visual projection rules:

```text
shared card anatomy;
type recognition;
density;
emphasis;
compact and expanded states;
status presentation;
consequence presentation;
accessibility;
interaction affordances;
Scene and Deck composition.
```

It must not redefine object schemas, lifecycles, authorization or evidence.

### B2 — controlled type variations

Every governed type keeps one shared card anatomy while varying a bounded set of visual variables.

| Type | Visual emphasis | Must not imply |
|---|---|---|
| Source | provenance and original-material posture | Evidence or truth |
| Evidence Candidate | support, contradiction and verification posture | accepted Evidence |
| Candidate Output | answer-first reading and declared limits | deliverable or approval |
| Action Candidate | external-effect preview and missing authorization | execution |
| Gate | blocking condition and consequence level | human Decision |
| Human Decision | scope, effective time, expiry, supersession and currentness | perpetual authorization |
| Trace | chronology and runtime observation | proof |
| Reference | reusable advisory material | active method execution |

Required rule:

```text
recognizable by structure and emphasis
not by color alone
```

### B3 — Scene, Deck and Cluster projection

`Cluster` may be introduced only as a local visual grouping:

```text
Deck
→ visual Cluster
→ Card
```

```text
Cluster != governance object
Cluster != workflow stage
Cluster != stored truth
```

The first-level cockpit remains small:

```text
Work
Evidence
Assets
Decisions
Trace
Reference Space
```

The Constellation remains a global relational mode, not a peer Scene.

### B4 — interaction and accessibility prototype

Extend the static prototype to demonstrate, without runtime effects:

```text
vertical scroll = Deck depth;
horizontal movement = sibling cards at one level;
tap = governed detail;
action menu = bounded UI intent or Action Candidate preparation;
keyboard focus and accessible controls;
compact cards as explicit variants, not clipped full cards.
```

Required corrections to the current prototype:

- separate the meaning of the top Scene rail and bottom global dock, or remove one;
- replace clipped `overflow:hidden` previews with an explicit compact-card anatomy;
- display Decision currentness separately from `recorded`;
- expose expiry, revocation or supersession where relevant;
- use semantic buttons, links and ARIA states;
- keep status readable without color.

Acceptance criteria:

- static illustrative prototype only;
- no hidden execution path;
- no production design-system package yet;
- Governance CI is green;
- human visual review occurs before promotion or merge of normative visual rules.

## Phase C — Current Decision Resolver

### C1 — resolver boundary

The resolver answers one question:

> Which recorded human Decision is currently applicable to this exact object, scope and time?

It does not decide, approve, execute, activate, install or promote memory.

Inputs:

```text
HandoffDecision records;
exact subject or handoff candidate identity;
scope dimensions;
effective time;
expiry;
revocation;
supersession;
decision type;
validation timestamp.
```

Output should be a derived read-only projection such as `CurrentDecisionProjection`, not an executable token.

Required non-equivalences:

```text
recorded != current
current != execution_started
current approval != activation
valid at time T != perpetual permission
scope match != global scope
runtime success != evidence
revoked != rolled_back
expired != revoked
```

### C2 — deterministic resolution rules

The resolver must:

1. reject records whose subject or exact scope does not match;
2. order records by effective time and explicit supersession, not file order;
3. exclude decisions not yet effective;
4. exclude expired approvals;
5. apply revocation and refusal within their declared reviewed scope;
6. detect ambiguous concurrent current approvals rather than selecting silently;
7. return `none`, `current`, `blocked`, `ambiguous` or `invalid-record-set` as projection outcomes;
8. preserve references to all records used in the resolution.

### C3 — verification slice

The first implementation remains read-only and local:

- schema for the derived projection;
- deterministic validator/resolver;
- fixtures for approve, refuse, revoke, expire, supersede, mismatch and ambiguity;
- CI;
- static review projection;
- no API, daemon, scheduler, queue, identity provider, signature service or runtime callback.

Acceptance criteria:

- identical inputs produce identical output;
- no decision is synthesized;
- ambiguous inputs fail closed;
- the resolver never calls Hermes or a provisioner;
- the cockpit consumes the projection but does not own its logic.

## Phase D — return to the existing vertical

After Phase C, reconnect the already implemented external MVP loop rather than starting a competing vertical.

Sequence:

```text
Task Contract
→ bounded external retrieval and drafting
→ Evidence Pack Candidate
→ Human Decision
→ Register Candidate
→ Current Decision Projection where authorization is queried
```

Then progressively replace stand-ins:

```text
terminal gate stand-in
→ authenticated OpenWebUI decision surface

deterministic drafter
→ Hermes-side bounded Drafter

local fixtures
→ one scoped external Source adapter

basic PDF representation
→ Docling Derived Representation Candidate
```

Each replacement requires its own Pantheon gate and does not imply adoption of the next dependency.

## Merge order

```text
1. Card Stack index and README reconciliation
2. source/retrieval clean replacement
3. repository-wide terminology audit
4. Card Stack visual prototype corrections
5. cockpit visual-language candidate
6. Current Decision Resolver contracts and tests
7. existing vertical integration
```

## Human decision points

Explicit human approval remains required before:

- promoting any candidate doctrine;
- introducing a canonical visual vocabulary;
- adding a new schema under protected paths where repo rules require approval;
- enabling a runtime adapter;
- activating a connector or resource;
- treating external verification as dependency adoption;
- merging a production OpenWebUI or Hermes integration.

## Definition of done for this roadmap

This roadmap is complete when:

```text
all listed phases have linked PRs or explicit defer decisions;
status is reported as implemented / partial / documented non-implemented;
no phase silently expands Pantheon into a runtime;
Current Decision resolution is deterministic and read-only;
the existing pantheon-mvp vertical is reused rather than duplicated.
```
