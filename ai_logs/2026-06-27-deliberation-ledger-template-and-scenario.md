# AI Log — Constraint & Decision Ledger template + CR chantier scenario

Date: 2026-06-27

Actor: Claude (claude-opus-4-8)

## Context

Follow-up to PR #231 (Iterative Deliberation Lifecycle note). The maintainer
accepted, as arbitration, a candidate Markdown template for the Constraint &
Decision Ledger (template yes, schema not now) and a CR chantier validation run
covering: 10 corrections, 1 old pinned constraint, 1 factual correction, 1
backtrack, 1 contradiction, 1 draft, 1 finalization, 1 candidate email, 1 Notion
gate. This delivers both, plus a card-stack design critique returned in chat.

## Change made

Created:

- `templates/deliberation/constraint_decision_ledger_candidate.md` — generic
  (non-domain) candidate template for the pinned working-state ledger. Encodes
  recto (five-second read) / verso (governed detail), constraints and decisions
  as entities with status (not as separate card families), surfaced
  contradictions, and a hard promotion boundary: governed working state, never
  canon, never bypasses the Registre Probatoire; finalize opens a diff-review
  gate, transmission/memory/external effect open separate gates.
- `examples/architecture/cr_chantier_deliberation_fictif/run_walkthrough.md` —
  fictional turn-by-turn run exercising the lifecycle taxonomy: 8 of 13 turns
  carry zero governance friction; the governance clock ticks only at the
  contract gate, the surfaced contradiction, the diff-review finalize gate, and
  the separate transmission and Register gates.

## Boundary preserved

Template and example only, both candidate. `templates/` and `examples/` are
grouped rows in `AUTHORITY_INDEX.md`, so no individual index row is required. No
conversation engine, chat memory, summarizer, email send, Notion write, schema,
runtime, approval engine or memory engine. No `schemas/`, `tests/`,
`operations/`, `platform/`, Docker, `.env`, `pyproject.toml` or `CLAUDE.md`
change. No external action. No Registre Probatoire entry. Nothing promoted.

## Repo state

Documented non-implemented (template + fictional example).

## Decision status

Accepted:

- a candidate ledger template (no schema);
- a fictional CR chantier validation scenario.

Left to the human (raised in chat):

- whether to fold the card-stack navigation / deck / card-family model into
  `CARD_STACK_MODEL.md` (resolving its open navigation questions) rather than a
  parallel doc;
- whether to consolidate lifecycle-state card families (Draft / Memory
  Candidate / Register / Promotion / Obsolete) into one Record family with a
  status field, consistent with the "one object, N revisions" invariant;
- whether the Workflow deck should default to answer-first (draft + gate + top
  evidence) with the full deck on demand.
