# AI log — E1: GLOSSARY owns the Registre Probatoire vocabulary and the three axes

Date: 2026-06-07.

## Intent

First downstream step (E1) of the Registre Probatoire direction
(`REGISTRE_PROBATOIRE_DIRECTION.md`): make `GLOSSARY.md` the single owner of the
renamed vocabulary and of the three certainty / decision axes, so that the later
steps (reframe `MEMORY.md`, promote the register doc) can reference one source.

## Change

In `docs/governance/GLOSSARY.md` only:

- the opening note now records the one governed rename (memory reserved to
  Hermès; Pantheon governs the `Registre Probatoire` in place of "Canonical
  Memory") and declares this file the owner of the three axes;
- added `Registre Probatoire` and `Hermès memory` terms;
- reframed `Memory Candidate` as `Register Candidate` (former name retained
  where not yet migrated);
- added a `Certainty and decision axes` section that owns the three distinct
  axes: `E0–E4` probative certainty (defined here, carried by the register),
  `V0–V4` answer verification (name owned here, levels owned by the Answer
  Verification Gate candidate), `C0–C5` approval ceiling (owned by
  `APPROVALS.md`, not redefined);
- updated the critical distinctions to use the register vocabulary.

## Boundary

Documentation only. No schema, test, runtime or protected-path change.
`C0–C5` is not redefined (it stays owned by `APPROVALS.md`); the answer-gate `V`
axis is named but its detailed levels stay with the candidate `ANSWER_VERIFICATION_GATE.md`.
The "Memory Candidate" name is retained where the corpus and `schemas/` are not
yet migrated; those are later steps (E2–E6), the schema rename being protected.
Verified clean against the governance forbidden-phrase lint.
