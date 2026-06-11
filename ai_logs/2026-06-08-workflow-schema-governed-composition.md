# AI log — WORKFLOW_SCHEMA governed composition (two gates) + Registre alignment

Date: 2026-06-08.

## Intent

Follow-up to the governed-composition keystone (#88): add the "two gates"
governed-composition doctrine to `WORKFLOW_SCHEMA.md`, and align the file's
remaining memory references to the Registre Probatoire vocabulary.

## Change

In `docs/governance/WORKFLOW_SCHEMA.md` only:

- added a `Governed composition` section — HÉPHAÏSTOS forges a Workflow Manifest
  candidate for a cap (held under MÈTIS, `REQUEST_LIFECYCLE.md`) from capabilities
  declared in `CAPABILITY_REGISTRY.md`; a retrieve / reuse / revise / retain loop
  mapped onto existing governance; the two gates (pre-execution eligibility
  arbitrated by ZEUS; post-execution evidence verification using V0–V4 answer
  verification and E0–E4 probative certainty); per-step governance signatures;
  `forged != authorized`, `completed != approved`, `returned != a Registre
  Probatoire entry`;
- reframed `Memory rules` as `Register rules` and `Relationship to Memory` as
  `Relationship to the Registre Probatoire`;
- renamed the remaining `Memory Candidate(s)` / `Canonical Memory` to
  `Register Candidate(s)` / `Registre Probatoire entry`.

## Boundary

Documentation only. No forge engine, compiler, scheduler, queue, provider
router or runtime; no schema, test or protected-path change. Execution stays
external under Task Contract. The section references `CAPABILITY_REGISTRY.md`
(merged via #88) and the three GLOSSARY axes. The role-registry touches
(`AGENTS.md` / `GOVERNANCE_COLLEGE.md` for HÉPHAÏSTOS) remain a separate
follow-up. Verified clean against the governance forbidden-phrase lint.
