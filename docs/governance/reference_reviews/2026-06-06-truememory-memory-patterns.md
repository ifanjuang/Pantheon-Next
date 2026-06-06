# TrueMemory Reference Review — Evidence Memory Patterns

Status: external reference / support review  
Scope: memory governance, evidence admission, retrieval discipline, project facts, contradiction handling, dependency graph, local-first memory patterns  
Runtime status: non-executable  
Reviewed source: https://github.com/buildingjoshbetter/TrueMemory  
Review date: 2026-06-06

## Boundary

This document reviews TrueMemory as an external reference.

It does not import TrueMemory, approve TrueMemory as a dependency, implement a memory engine, create an automatic promotion system, create a scheduler, create a queue, modify schemas, modify tests, modify operations, modify platform code, or grant runtime authority.

```text
External reference informs Pantheon.
It does not govern Pantheon by itself.
```

Pantheon Next remains governance-first.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Executive decision

TrueMemory is useful for Pantheon Next, but not as a direct dependency or central engine.

It should be treated as a reference pattern for:

```text
session capture
-> fact extraction
-> admission gate
-> deduplication
-> local SQLite storage
-> hybrid retrieval
-> reranking
-> MCP exposure
-> ingestion traces
```

The useful lesson is structural: a memory system must not store everything, must not retrieve without scope, and must not confuse remembered text with governed truth.

The dangerous interpretation would be to copy it as a general agent memory layer and attach it to Pantheon. Pantheon does not need a personal-memory engine. Pantheon needs a project evidence memory doctrine.

```text
personal agent memory
!=
project evidence memory
```

TrueMemory asks:

```text
Should this fact be remembered by the agent?
```

Pantheon must ask:

```text
May this assertion become a scoped, sourced, status-bearing project memory?
What does it depend on?
What does it invalidate?
What authority supports it?
What time interval makes it true?
Can it be used in a professional output?
```

## Why this matters for Pantheon

Pantheon already states that memory must be validated, scoped and evidence-linked. The TrueMemory review strengthens that doctrine with a more precise ingestion model.

The immediate value is not vector search. The value is the pipeline discipline before search:

```text
raw conversation or document
-> candidate fact
-> gate decision
-> duplicate / update / conflict check
-> status assignment
-> trace
-> only then retrievable memory
```

Without this gate, project memory becomes a landfill. Repeated chat fragments, obsolete decisions, draft ideas, unverified assumptions and contradictory versions all get embedded together. Retrieval then produces fluent but unsafe answers.

For professional dossiers, that failure mode is not cosmetic. It can create:

```text
wrong client commitment
wrong planning assumption
wrong technical premise
wrong lot responsibility
wrong regulatory answer
wrong cost basis
wrong contentieux chronology
wrong memory reused across projects
```

Pantheon must therefore govern not only outputs, but the creation and later use of memory.

## What TrueMemory appears to do well

Based on the repository structure and documentation, TrueMemory is more than a small MCP wrapper. It combines several memory subsystems:

```text
local storage
fact extraction
encoding gate
deduplication
FTS retrieval
vector retrieval
hybrid rank fusion
reranking
salience
consolidation
temporal metadata
MCP tools
CLI hooks
model-tier switching
```

The main useful pattern is the separation between:

```text
capture
ingestion
storage
retrieval
injection
```

Pantheon should keep the same separation, but change the meaning of each stage.

## Pattern 1 — Capture hooks

TrueMemory uses agent/client hooks to capture sessions and later ingest candidate memories.

Pantheon should reuse the pattern, not the exact behavior.

Candidate Pantheon hooks:

```text
on_chat_session_end
on_document_upload
on_email_thread_import
on_site_report_added
on_quote_added
on_invoice_added
on_plan_revision_added
on_user_correction
on_human_validation
on_external_source_refresh
```

Each hook should create candidates, not active memory.

```text
capture creates candidates
validation creates active memory
```

### Required Pantheon guardrail

No hook may silently promote memory.

Every captured item must remain a candidate until it receives:

```text
project scope
source reference
status
confidence
authority level
validity interval when applicable
```

## Pattern 2 — Encoding gate becomes Evidence Admission Gate

TrueMemory uses an encoding gate to decide whether information deserves long-term memory.

Pantheon should define an Evidence Admission Gate.

The gate should answer:

```text
Should this assertion be stored as a governed evidence atom?
```

Candidate scoring dimensions:

```text
novelty
source authority
project impact
professional risk
cost impact
planning impact
technical impact
legal / contractual impact
contradiction potential
dependency potential
temporal permanence
reuse risk
scope clarity
```

Negative signals:

```text
small talk
style preference with no project effect
duplicate wording
unverified model inference
unattributed summary
source missing
project unknown
ambiguous actor
speculative statement
confidential content with unclear scope
```

### Candidate gate output

The gate should never return only yes or no.

It should return:

```yaml
decision: admit | reject | hold_for_review | link_only
reason: short explanation
scores:
  novelty: 0.0
  source_authority: 0.0
  project_impact: 0.0
  professional_risk: 0.0
  contradiction_potential: 0.0
  dependency_potential: 0.0
  scope_clarity: 0.0
required_next_action:
  - classify_project
  - attach_source
  - human_review
  - compare_existing
  - detect_dependencies
```

The important point is that the gate must explain itself. A future dashboard should be able to show why a fact was admitted, rejected, held or linked.

## Pattern 3 — Deduplication is not enough

TrueMemory uses an ADD / UPDATE / SKIP style decision pattern for duplicate and near-duplicate facts.

Pantheon needs a richer decision vocabulary.

Required Pantheon memory decisions:

```text
ADD          create a new evidence atom
MERGE        combine near-duplicates under one governed atom
UPDATE       add a newer version while preserving history
SUPERSEDE    replace an older valid statement with a newer one
INVALIDATE   mark a statement as no longer valid because its premise collapsed
DOWNGRADE    keep the statement historically visible but remove default active use
LINK_ONLY    do not create a new fact, but connect it to an existing one
DISPUTE      mark a conflict requiring human arbitration
REJECT       do not store as project memory
ARCHIVE      keep for history, exclude from active retrieval by default
```

This is essential because project truth evolves. Old facts are not always false. They may be true at an earlier phase, useful for contentieux, or relevant to why a decision was made.

```text
obsolete does not mean useless
superseded does not mean deleted
historical does not mean active
```

## Pattern 4 — Evidence atoms instead of memory blobs

TrueMemory is centered around remembered messages and facts. Pantheon should be centered around evidence atoms.

A bad memory record:

```text
Client talked about terrace, swimming pool, foundations and heat pump.
```

A better Pantheon decomposition:

```text
E1: The client no longer wants a swimming pool.
E2: The pool heat-pump choice depends on the swimming-pool assumption.
E3: The terrace option was initially designed to remain compatible with a pool.
E4: A foundation-depth assumption had been considered in relation to the pool.
E5: The terrace design must be reviewed if the pool assumption is abandoned.
```

Each atom should have its own status, source, confidence and dependencies.

## Pattern 5 — Dependency graph

Pantheon should exceed TrueMemory by making dependencies explicit.

Every evidence atom should be able to express:

```text
depends_on
supports
contradicts
supersedes
invalidates
downgrades
requires_review_of
is_source_for
is_derived_from
```

Candidate edge model:

```yaml
edge_id: dep_...
project_id: ...
from_evidence_id: ...
to_evidence_id: ...
relationship: depends_on | invalidates | supersedes | contradicts | supports | downgrades | requires_review_of
confidence: 0.0
source_id: ...
created_by: human | policy | extraction | model_candidate
status: candidate | accepted | disputed | rejected
```

This is the difference between remembering and reasoning over a dossier.

A vector search can retrieve related fragments. A dependency graph can say:

```text
This premise collapsed, therefore these downstream assumptions are no longer active.
```

## Worked example — abandoned swimming pool

Input event:

```text
The client no longer wants a swimming pool.
```

Pantheon should not merely store this as a preference.

Expected extraction:

```yaml
assertion: The client no longer wants a swimming pool.
type: decision_change
project_scope: active_project_required
actor: client
status: candidate_until_source_attached
impact: high
```

Expected graph review:

```text
Find active or candidate memories containing:
- pool
- swimming-pool equipment
- pool heat pump
- terrace compatible with pool
- foundations coordinated with pool
- drainage related to pool
- garden / landscape options tied to pool
```

Expected memory decisions:

```text
ADD decision: pool abandoned
DOWNGRADE previous pool assumption
INVALIDATE pool heat-pump selection if no independent use remains
REVIEW terrace compatibility assumptions
REVIEW foundation-depth assumptions linked to pool
REVIEW drainage / network / outdoor lot assumptions
KEEP historical design trace
```

Expected Evidence Pack:

```yaml
active_decision:
  - client abandoned swimming pool
impacted_assumptions:
  - pool heat pump
  - terrace compatibility
  - foundation-depth coordination
  - drainage / external works
status:
  pool: inactive
  heat_pump: invalidated_candidate
  terrace: requires_review
  foundations: requires_review
human_action:
  - confirm source
  - update project assumptions
  - notify affected lot review if needed
```

This is the target behavior for Pantheon Evidence Memory.

## Pattern 6 — Chronology must be hard, not semantic

TrueMemory appears to include temporal features, but Pantheon cannot let semantic retrieval decide event order.

For professional dossiers, chronology is a first-class object.

Every evidence atom should include, when available:

```text
source_date
event_date
document_date
received_at
extracted_at
validated_at
valid_from
valid_until
superseded_at
phase_index
revision_index
```

The system should be able to answer:

```text
What was true on this date?
What became true later?
Which version was active when this email was sent?
Which assumption was active when the quote was reviewed?
Which site-report issue appeared first?
When did it disappear from reports?
When was it treated as resolved?
```

Temporal ordering must be done through explicit metadata and event records before vector retrieval.

```text
chronology is not an embedding problem
```

## Pattern 7 — Retrieval must be scoped before it is ranked

A memory system must not search globally and then filter the results after ranking.

Pantheon retrieval must begin with hard scope filters:

```text
project_id
memory_layer
source_status
confidentiality
validity_status
phase
lot
date interval
```

Only after scope filtering should the system apply:

```text
FTS / BM25
vector search
rank fusion
reranking
salience
```

Target retrieval path:

```text
L0 — active project and actor scope
L1 — task contract and requested output status
L2 — exact search / FTS / BM25 inside scope
L3 — semantic search inside scope
L4 — source authority and validity filter
L5 — dependency and contradiction graph
L6 — chronology / active-at-date resolver
L7 — Evidence Pack composer
```

The Evidence Pack must show what was used, not silently inject memories.

## Pattern 8 — Visible Evidence Pack instead of opaque memory injection

TrueMemory-style memory injection is useful for personal agents, but dangerous for Pantheon if it is invisible.

Pantheon should expose injected context as a visible Evidence Pack.

Example:

```yaml
evidence_pack:
  project_id: ...
  task_contract_id: ...
  active_decisions: 7
  candidate_facts: 4
  contradictions: 2
  downgraded_assumptions: 3
  source_documents: 5
  excluded_memories:
    - reason: wrong project
    - reason: superseded
    - reason: unvalidated
    - reason: confidential beyond task scope
```

The user or reviewer should be able to inspect:

```text
what entered the context
what was excluded
why it was excluded
which facts are active
which facts are candidates
which facts are disputed
```

## Pattern 9 — Ingestion traces

TrueMemory tracks ingestion decisions. Pantheon should make this a core governance requirement.

Each ingestion run should record:

```text
input source
extraction method
candidate assertions
admission gate result
similarity checks
conflicts found
dependencies proposed
human decisions
final memory status
```

Candidate trace table:

```text
ingestion_runs
- id
- source_id
- project_id
- trigger
- started_at
- completed_at
- extractor
- model_used
- status
- warning_count

extraction_candidates
- id
- ingestion_run_id
- assertion_text
- proposed_type
- proposed_scope
- confidence
- source_locator
- gate_decision
- gate_reason

memory_decision_log
- id
- candidate_id
- decision
- reviewer
- decided_at
- reason
- affected_evidence_ids
```

The trace is not merely technical logging. It is part of professional reviewability.

## Candidate data model

This is not an implementation requirement. It is a governance-oriented target model for later schema work.

```text
projects
actors
project_roles
source_documents
document_revisions
source_locators
evidence_atoms
evidence_versions
evidence_sources
evidence_dependencies
evidence_conflicts
evidence_status_events
decision_records
ingestion_runs
extraction_candidates
memory_decision_log
retrieval_traces
evidence_packs
```

### evidence_atoms

```yaml
evidence_id: ...
project_id: ...
assertion: ...
type: decision | constraint | request | preference | assumption | risk | cost | deadline | technical_fact | regulatory_fact | contractual_fact | site_issue
status: candidate | accepted | confirmed | active | superseded | invalidated | downgraded | disputed | archived | rejected
confidence: 0.0
authority_level: low | medium | high | binding
source_count: 0
valid_from: null
valid_until: null
phase: null
lot: null
created_at: ...
updated_at: ...
```

### evidence_sources

```yaml
evidence_id: ...
source_document_id: ...
source_revision_id: ...
source_locator: page | line | email_message | site_report_item | plan_revision | quote_line
source_excerpt_hash: ...
source_role: primary | supporting | contradictory | superseding
```

### evidence_status_events

```yaml
evidence_id: ...
previous_status: candidate
new_status: accepted
reason: ...
actor: human | policy | system_candidate
created_at: ...
```

### retrieval_traces

```yaml
retrieval_trace_id: ...
task_contract_id: ...
project_id: ...
query: ...
filters_applied:
  project_id: ...
  status:
    - active
    - confirmed
  excluded_status:
    - superseded
    - rejected
    - wrong_project
candidate_count: 0
selected_evidence_ids: []
excluded_evidence_ids: []
created_at: ...
```

## Candidate status vocabulary

Pantheon should not reduce status to active/inactive.

Recommended statuses:

```text
candidate       extracted, not yet usable as active memory
accepted        accepted for limited scoped use
confirmed       verified by high-authority source or human review
active          currently usable in its defined scope
superseded      replaced by newer evidence
invalidated     premise collapsed or contradiction resolved against it
downgraded      historically useful but excluded from default active retrieval
disputed        unresolved contradiction
archived        kept for record, not used by default
rejected        not retained as project memory
```

Status must be visible in the answer.

A Pantheon response should not say only:

```text
The project includes a swimming pool.
```

It should say, when relevant:

```text
The swimming-pool assumption is superseded. The active decision is that the client abandoned the pool. Terrace and foundation assumptions linked to the pool require review.
```

## Candidate authority levels

Memory should include source authority.

Suggested order, from lower to higher authority:

```text
model inference
unattributed note
conversation fragment
user statement in chat
internal draft
email from participant
site-report item
validated meeting minutes
signed quote / contract document
permit / administrative decision
human validated project fact
```

Authority is contextual. A client email may be high authority for a client preference, but low authority for structural feasibility. A contractor quote may be high authority for price offered, but low authority for planning law.

The authority model must therefore include:

```text
authority_domain
```

Examples:

```text
client_preference
architectural_design
technical_feasibility
urban_planning
contractual_commitment
cost
site_execution
legal_procedure
```

## Candidate contradiction handling

Contradiction is not an error to hide. It is a governance object.

When a new assertion conflicts with an existing memory, Pantheon should create a conflict record:

```yaml
conflict_id: ...
project_id: ...
evidence_a: ...
evidence_b: ...
conflict_type: direct_contradiction | temporal_replacement | scope_mismatch | source_authority_conflict | unit_mismatch | version_conflict
status: candidate | accepted | resolved | disputed
resolution: null | prefer_newer | prefer_higher_authority | split_by_date | split_by_scope | human_decision
```

Typical professional conflicts:

```text
old quote vs revised quote
old plan vs new plan
meeting decision vs later email
client preference vs regulatory constraint
contractor claim vs site-report observation
permit assumption vs final administrative response
CCTP description vs quote omission
```

Pantheon should not flatten these into one answer. It should present them as conflicts with status.

## Candidate promotion rule

No extracted memory should become reusable knowledge merely because it was repeated.

Promotion requires:

```text
scope clarity
source trace
status review
confidentiality review
project boundary review
human or policy acceptance
```

Promotion paths:

```text
project candidate -> project active memory
project active memory -> project confirmed memory
project lesson learned -> agency candidate memory
agency candidate memory -> agency validated memory
agency validated memory -> domain support material, only after anonymization and review
```

The reverse path must also exist:

```text
active -> downgraded
active -> disputed
active -> superseded
confirmed -> superseded
candidate -> rejected
```

## How this should update the current Pantheon doctrine

This reference review should inform future edits to `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md`.

Recommended future additions to that document:

```text
1. Add Evidence Admission Gate as an explicit stage after extraction.
2. Replace simple project_facts with evidence_atoms + evidence_versions + evidence_sources.
3. Add memory decision vocabulary: ADD, MERGE, SUPERSEDE, INVALIDATE, DOWNGRADE, LINK_ONLY, DISPUTE, REJECT, ARCHIVE.
4. Add dependency graph requirements.
5. Add explicit chronology requirements.
6. Add retrieval trace requirements.
7. Add visible Evidence Pack requirement for memory injection.
8. Add non-goal: no automatic memory promotion.
```

Recommended future standalone doctrine candidate:

```text
docs/governance/PANTHEON_EVIDENCE_MEMORY.md
```

Recommended future schema area, only after explicit review:

```text
schemas/evidence-memory/
```

No schema should be created from this review alone.

## Hermes / OpenWebUI / local model binding

This review supports the existing division of labor.

```text
OpenWebUI exposes:
- uploaded documents
- selected sources
- status labels
- Evidence Pack preview
- validation interface

Hermes Agent executes:
- extraction
- OCR / conversion calls
- candidate comparison
- dependency detection
- report preparation
- model calls

Pantheon governs:
- admission rules
- scope rules
- memory status
- dependency status
- contradiction status
- approval and external action boundaries
```

A future Hermes memory curator profile could perform candidate extraction, but it must not validate memory by itself.

Allowed:

```text
Hermes proposes candidate evidence.
Hermes proposes dependencies.
Hermes proposes conflicts.
Hermes proposes status changes.
```

Not allowed without explicit governance approval:

```text
Hermes silently promotes memory.
Hermes silently invalidates project facts.
Hermes sends external messages because memory changed.
Hermes reuses project memory in another project.
Hermes hides excluded evidence from the user.
```

## Local-first posture

TrueMemory reinforces a useful local-first direction.

Pantheon memory should prefer:

```text
local database
explicit backups
scoped vector indexes
human-readable exports
traceable source files
no default telemetry
```

For agency and professional dossiers, telemetry must be opt-in or absent.

The default posture should be:

```text
No memory content leaves the project perimeter unless the task contract explicitly allows it.
No telemetry is necessary for the governance method.
```

## Licensing and dependency caution

TrueMemory is a useful reference, but direct integration should be avoided unless licensing, telemetry and operational boundaries are reviewed.

Risks to check before any dependency decision:

```text
license compatibility
commercial-use constraints
telemetry default behavior
message-centric schema
personal-memory assumptions
scope filtering model
runtime resource requirements
model dependency weight
```

Reference patterns may be adopted. Code should not be copied into Pantheon without explicit license review.

## Acceptance checklist for future implementation

A future Pantheon Evidence Memory implementation should be considered aligned only if it satisfies the following checks.

### Scope

```text
Every retrieval is project-scoped or explicitly cross-scope authorized.
Project memory cannot leak into general memory by default.
General memory cannot override project evidence.
```

### Source

```text
Every active memory has at least one source or an explicit human assertion record.
Derived memory links back to original source material.
Converted Markdown is not treated as the source of truth.
```

### Status

```text
Every memory has a visible status.
Candidate memory is not used as confirmed fact.
Superseded memory remains traceable but is excluded by default.
```

### Time

```text
The system can answer what was active at a date.
The system records valid_from and valid_until where applicable.
Chronology is not inferred only from semantic similarity.
```

### Dependencies

```text
The system records when one memory depends on another.
If a parent assumption is invalidated, dependent assumptions are flagged.
Downstream review is proposed, not silently executed.
```

### Contradictions

```text
Contradictions are stored as reviewable objects.
Conflict resolution is explicit.
Human arbitration is required for high-risk conflicts.
```

### Retrieval

```text
Retrieval traces are stored.
Excluded evidence can be inspected.
Evidence Pack composition is visible.
Memory injection is not opaque.
```

### Promotion

```text
No automatic promotion from project memory to agency or general memory.
Promotion requires anonymization and review when project material is involved.
Rejected or deprecated memory remains traceable if needed for audit.
```

## Minimal next action

The next useful repository action is not implementation.

It is to distill this reference review into a candidate doctrine file:

```text
docs/governance/PANTHEON_EVIDENCE_MEMORY.md
```

That file should define the canonical vocabulary for:

```text
evidence atoms
memory statuses
admission gate
memory decisions
dependency edges
conflict records
retrieval traces
Evidence Packs
promotion and demotion rules
```

Only after that doctrine is reviewed should schemas or tests be proposed.

```text
Doctrine first.
Schema second.
Runtime last.
```

## Final position

TrueMemory is valuable because it demonstrates that memory is not just storage. Memory is a controlled pipeline.

Pantheon should keep that lesson, but redirect it toward professional evidence:

```text
not: the agent remembers
but: the project records, scopes, tests, traces and reviews
```

That is the improvement path.

Pantheon Evidence Memory should become the governed layer that decides what may remain, what may be reused, what has been invalidated, what is disputed, and what still requires human review.
