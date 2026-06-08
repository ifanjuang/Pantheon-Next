# AI log — E2: reframe MEMORY.md under the Registre Probatoire direction

Date: 2026-06-07.

## Intent

Second downstream step (E2) of the Registre Probatoire direction. Reframe
`MEMORY.md` so "memory" belongs to Hermès (free, self-evolving runtime memory,
ungoverned) and the governed durable object is the Registre Probatoire, in place
of "Canonical Memory".

## Change

Reframed `docs/governance/MEMORY.md` (same structure and doctrine, ownership
inverted and the two terms renamed):

- new opening: memory belongs to Hermès and carries no authority; Pantheon
  governs the Registre Probatoire; the document draws that boundary;
- added an explicit `Bridge rule` section (Hermès memory may speak; only a
  Registre Probatoire entry may be cited for a consequential decision);
- renamed `Memory Candidate` -> `Register Candidate` and `Canonical Memory`
  -> `Registre Probatoire entry` throughout, keeping one "former name" note for
  each so migration stays traceable;
- added the `E0–E4` certainty field to the candidate and entry definitions
  (owner: `GLOSSARY.md`);
- reframed the Hermès relationship: Hermès keeps its own free runtime memory,
  Pantheon governs neither its content nor its evolution;
- preserved every still-valid distinction (Knowledge / Context / Session State /
  Runtime State), scope, status, revocation and forbidden-drift rule;
- recorded that the schema rename is deferred protected-path work (E6).

## Boundary

Documentation only. No schema, test, runtime or protected-path change.
`MEMORY.md` stays a CI-mandatory file and is lint-clean. The "Memory Candidate"
and "Canonical Memory" names survive only as explicit former-name notes; the
`schemas/memory_candidate.schema.yaml` rename remains deferred and protected.
The reframe strengthens the existing boundary (Pantheon now governs no memory of
its own) rather than loosening it.
