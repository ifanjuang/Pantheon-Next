# AI Log — Iterative Deliberation Lifecycle note

Date: 2026-06-27

Actor: Claude (claude-opus-4-8)

## Context

A theoretical question from the architect: working with an AI is iterative —
many corrections, clarifying questions and partial drafts before a draft CR,
then more round-trips, then a finalized CR. How does that long conversational
back-and-forth sit alongside Pantheon, whose unit is the governed candidate
routed through the chokepoint?

The discussion converged on an event-sourcing reading and, on a second pass
("think harder, every situation, optimization"), on three points the first
answer had missed: a full turn taxonomy with cost-proportional routing, a
*three*-persistence model (the pinned constraint/decision ledger as the
load-bearing layer), and optimization invariants. The constraint-ledger point
is the conversational cousin of the AUTHORITY_INDEX truncation repaired earlier
today: state must never be rebuilt from a partial view — at the file, the CR,
or the dialogue.

## Change made

Created:

- `docs/governance/ITERATIVE_DELIBERATION_LIFECYCLE.md` — candidate support
  doctrine. Models multi-turn deliberation as an append-only event log, the CR
  as a projection, the constraint ledger as reduced state, the gate as a
  command and the Registre Probatoire entry as the commit. Defines the two
  clocks (deliberation vs governance), a turn taxonomy with optimal routing,
  the three persistences, optimization principles (shift-left, gate-the-
  contract, front-load uncertainty, diff-everything, idempotent finalize,
  per-assertion status), invariants, edge situations and the card-stack
  representation.

Updated:

- `docs/governance/AUTHORITY_INDEX.md` — index the new note as candidate
  support doctrine / documented non-implemented (one additive row).

## Boundary preserved

Documentation only. No conversation engine, chat memory, summarizer, workflow
engine, scheduler, queue, router, approval engine or memory engine. No
`schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`,
`pyproject.toml` or `CLAUDE.md` change. No external action. No Registre
Probatoire entry. Nothing promoted to canonical doctrine.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- formalize the iterative-deliberation lifecycle as a candidate note;
- treat the constraint/decision ledger as a first-class governed object that
  survives summarization and session end.

To verify / to arbitrate (left to the human):

- whether the lifecycle stays generic Pantheon doctrine or specializes per
  domain;
- whether the constraint ledger deserves its own schema proposal later;
- whether finalize/diff-review should be specified against TASK_CONTRACT_REVISIONS.md.

## Review integration (PR #231)

Maintainer review ("plutôt accepté, garder candidate") integrated as small,
boundary-tightening refinements (no canonical promotion, no schema):

- bounded the `command` analogy — a Gate exposes a threshold and collects a
  human decision; it does not actuate;
- stated the Constraint & Decision Ledger stays candidate / non-canonical,
  governed working state, never a parallel memory bypassing the Registre
  Probatoire;
- refined finalize: opens at minimum a diff-review gate; transmission, canonical
  memory or external effect opens a separate, additional gate;
- added articulation notes (TASK_CONTRACT_REVISIONS.md owns revision identity, no
  competing vocabulary; vocabulary compatible with AUTHORITY_INDEX.md and
  EVIDENCE_MEMORY_CANONICALIZATION.md; ledger as pinned working-state card per
  CARD_STACK_ROLE_QUALITY_ALIGNMENT.md);
- recorded the three arbitrations with the maintainer's leanings and a CR
  chantier validation plan before any promotion.
