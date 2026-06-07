# AI log — Memory becomes Hermès-owned; Pantheon governs the Registre Probatoire

Date: 2026-06-07.

## Intent

The maintainer decided to reframe the memory model: give "memory" to Hermès as
its own free, self-evolving runtime memory (mem0 or another system), and have
Pantheon govern an evidence register with certainty levels, exhibits, dates and
citations instead of a "Canonical Memory".

## Decisions (maintainer)

- Name of the governed object: **Registre Probatoire** (replaces "Canonical
  Memory").
- The word **"memory" is reserved to Hermès**; Pantheon no longer uses it for
  anything it governs.

## What was produced

- `docs/governance/REGISTRE_PROBATOIRE_DIRECTION.md` (validation-only direction
  record): the model (Hermès memory vs Registre Probatoire), the bridge rule
  (free memory may speak; only the register may be cited for consequential
  decisions — the Answer Verification Gate posture), three orthogonal certainty
  axes (E0–E4 register / V0–V4 answer / C0–C5 approval, GLOSSARY-owned), the
  register entry's required fields, the vocabulary migration and the list of
  corpus documents to realign.
- A file-by-file execution checklist for the executor (steps E1–E6): GLOSSARY
  owns the three scales; reframe MEMORY.md; promote the Registre Probatoire doc;
  the bridge rule in the Answer Verification Gate (dependent on PR #71); a single
  reindex pass; and the deferred protected schema rename. It includes a surgical
  rename map (what changes vs what stays) and a whole-effort acceptance gate.

## Rationale

The split sharpens the boundary rather than loosening it. Hermès memory is
operational, subjective recall with no authority; the Registre Probatoire is the
objective, dated, cited record one may rely on. Free memory stays compatible
with the red lines (no self-learning loop, no auto-promoted memory) only via the
bridge rule, which is stated explicitly.

## Boundary

Direction record only. No doctrine file rewritten, no schema, test or runtime
added, no protected path touched. The schema rename
(`schemas/memory_candidate.schema.yaml` and related) is deferred protected-path
work. Verified clean against the governance forbidden-phrase lint.
