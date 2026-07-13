# MVP Governed Task Loop

Status: candidate support doctrine — minimal vertical loop specification; documented non-implemented.

Date: 2026-07-07

Schema reconciliation: 2026-07-13 — issue #359.

This document specifies the smallest complete governed loop between OpenWebUI, Hermes Agent and a pgvector retrieval store: `mvp-governed-task-loop`. It is documentation only. It adds no runtime, no scheduler, no queue, no provider router, no plugin manager, no automatic memory promotion and no automatic approval; every consequential step routes through the existing governance chokepoint and the User Decision Gate.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

One dossier, one request, one complete pass. The MVP exists to be falsifiable: it is the first place where the doctrine meets a real request end to end. If a step cannot be carried as written, the finding routes back as a doctrine correction — the loop is the test, not the exception.

The reference scenario is the recovery quote (`docs/examples/architecture_devis_reprise/`): a client email asks for a reply that could commit the practitioner.

## The loop — nine steps

1. **OpenWebUI captures and exposes.** The practitioner writes the request and selects the working documents from their usual screen. OpenWebUI captures; it decides nothing.
2. **Pantheon produces or validates a Task Contract.** The request is classified (consequence, certainty, approval ceiling) and a Task Contract candidate is produced or validated — declared scope, forbidden scope, expected output status, evidence expectations. See `docs/governance/examples/mvp_task_contract.yaml`.
3. **Hermes executes inside the authorized perimeter.** Hermes works only within the contract's declared scope: reads the selected sources, prepares, masks, drafts. Anything outside the perimeter is a refusal, reported as such.
4. **pgvector serves retrieval only — not proof, not truth.** The vector store returns candidate passages with their source references. An indexed chunk is not evidence; a retrieved passage is not a fact. Every retrieved item enters the loop as a citation-bearing candidate that still needs its status.
5. **Hermes returns a Result Candidate plus an Evidence Pack Candidate.** The draft answer carries its sources, assumptions, limits, contradictions and open risks. See `docs/governance/examples/mvp_evidence_pack_candidate.yaml`. Runtime completion is a fact about execution, not a verdict about the content.
6. **OpenWebUI displays sources, limits, risks and the possible decisions.** The exposure surface shows the candidate with its Evidence Pack and the decision options. Display is exposure, not authority.
7. **The human decides.** The closed decision vocabulary is `approve`, `refuse`, `request_revision`, `request_more_evidence`. No candidate may define or widen it. No other actor holds this decision; no timeout, default or score takes it in the human's place.
8. **Pantheon writes a Decision Record.** The record binds the decision to the exact reviewed candidate and, when present, Evidence Pack Candidate through SHA-256 digests. It records a distinct `decision_id`, `recorded_at`, optional supersession and an honest identity-assurance level. See `docs/governance/examples/mvp_decision_record.yaml`.
9. **A governed memory proposal requires a separate retention authorization.** An `approve` decision does not by itself authorize retention. A Register Candidate may be prepared only when a human also provides an explicit `retention_authorization`; it remains subject to the register's own admission gate. See `docs/governance/examples/mvp_memory_candidate.yaml`.

## Canonical MVP decision vocabulary

The schema is the single machine-readable source for the closed vocabulary:

```text
approve
refuse
request_revision
request_more_evidence
```

Semantics:

- `approve` accepts the candidate for the declared review scope only. It does not authorize external action, retention or memory admission.
- `refuse` rejects the candidate and authorizes no downstream consequence.
- `request_revision` requires a new candidate; the reviewed candidate remains unapproved.
- `request_more_evidence` pauses review until additional evidence or a revised Evidence Pack Candidate is supplied.

The values live in `schemas/mvp_governed_loop_objects.schema.yaml#/$defs/decision_value`. An external binding vendors the schema and reads that enum; it must not accept a vocabulary supplied by a candidate and does not need a second standalone vocabulary file.

## Decision identity boundary

The decision surface must state what it can prove:

```text
terminal stand-in -> identity_assurance: declared
authenticated cockpit session -> identity_assurance: authenticated + authenticated_principal
```

OpenWebUI, or another reviewed cockpit replacing it, owns authentication from its session. A terminal stand-in may refuse reserved system identities, but it must not fabricate an authenticated principal. Pantheon governs the record shape and decision status; it does not authenticate the user or execute the decision consequence.

## Candidate review metadata

`commitment_flags` use structured entries `{phrase, risk}` so the cockpit can expose both the detected wording and why it matters. `grounding_review` is structured advisory visibility only. It is not a score, proof, truth verdict or approval gate.

## Retrieval boundary (pgvector)

The store is a finding aid, never an authority:

- retrieval is scoped before it is ranked — the query runs inside the contract's source perimeter, not across the whole corpus;
- every returned passage keeps its source reference and enters the Evidence Pack as a candidate citation;
- a passage that cannot be traced to a governed source is reported as a capability gap, not used silently;
- the index is rebuildable at any time from governed sources — it holds no state that the sources do not hold.

## Explicit prohibitions

None of the following equivalences is accepted anywhere in the loop:

```text
indexed            ≠ evidence
retrieved          ≠ truth
runtime_success    ≠ approval
OpenWebUI display  ≠ authority
Hermes output      ≠ Registre Probatoire entry
```

And two automatic behaviors are forbidden outright:

```text
no automatic memory promotion — step 9 requires the human decision of step 7
no automatic external action — sending, publishing or committing anything externally
                               is a separate human decision, never a loop side effect
```

## What this MVP is not

Voluntarily absent from this specification and from any implementation of it:

```text
internal execution runtime        agent loop inside Pantheon
scheduler                         queue
provider router                   plugin manager
automatic approval engine         automatic memory promotion engine
automatic external sender
```

If an implementation appears to need one of these, that is a doctrine conflict to arbitrate, not a gap to fill.

## Object shapes

The four example files under `docs/governance/examples/` remain illustrative. Their central fields are aligned with the reviewed validation contract in `schemas/mvp_governed_loop_objects.schema.yaml`; schema validity remains structural and does not authorize execution, approval, retention, external action or memory admission.

- `docs/governance/examples/mvp_task_contract.yaml` — the mission sheet (step 2);
- `docs/governance/examples/mvp_evidence_pack_candidate.yaml` — the proof folder returned with the draft (step 5);
- `docs/governance/examples/mvp_decision_record.yaml` — the human decision as data (step 8);
- `docs/governance/examples/mvp_memory_candidate.yaml` — the governed memory proposal (step 9).

Vocabulary note: the loop's plain name for the step-9 object, "memory candidate", maps to the current object term **Register Candidate** (see `docs/governance/GLOSSARY.md`); the file name keeps the plain form for readability.

## Relation to existing doctrine

This MVP composes existing doctrine; it introduces no new rule:

- `docs/governance/TASK_CONTRACTS.md` — step 2;
- `docs/governance/EVIDENCE_PACK.md` — step 5;
- `docs/governance/USER_DECISION_GATE.md` — steps 6–7;
- `schemas/mvp_governed_loop_objects.schema.yaml` — closed decision vocabulary and validation-only object shapes;
- `docs/governance/MEMORY.md` — step 9;
- `docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` — step 4;
- `docs/governance/HERMES_INTEGRATION.md` and `docs/governance/OPENWEBUI_INTEGRATION.md` — the two surfaces;
- `mcp-server/` — the read-only verification surface remains the policy plane; it validates and classifies, it does not run the loop.

## Acceptance criteria

The MVP is demonstrated (not promoted) when one real dossier completes all nine steps with:

- a Task Contract reviewed before execution;
- every retrieved passage traceable to a selected source;
- a Result Candidate that was refused or revised at least once through the gate (the gate must be exercised, not rubber-stamped);
- a Decision Record for every decision taken;
- at most one Register Candidate, created only after an explicit authorizing decision.

Demonstration produces an `ai_logs/` entry and an Evidence Pack; promotion of anything beyond that remains a separate reviewed decision.
