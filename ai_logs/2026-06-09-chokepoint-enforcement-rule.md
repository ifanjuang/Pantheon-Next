# AI log — make the consequential chokepoint explicit

Date: 2026-06-09.

## Intent

Sequence step 1 from `TARGET_ARCHITECTURE.md`: turn "Pantheon master" from an
implicit property into an explicit doctrine rule — the runtime must route
consequential effects through Pantheon's policy check (the chokepoint named in
`UNIFORM_CAPABILITY_GOVERNANCE.md`).

## Change

- `docs/governance/HERMES_INTEGRATION.md`: new section "Consequential effects
  route through Pantheon — the chokepoint". States the PDP/PEP relation (Pantheon
  = decision point, Hermès = enforcement point), the routing rule (non-consequential
  effects proceed freely; consequential effects ask the policy check first and
  proceed only on allow / allow_with_gate, under the passport's required envelope),
  that the decision is data not execution, that a bypass makes Pantheon master only
  in advice, and that no per-capability rule is added (the passport carries the
  specifics). Wiring lives in the runtime (Phase 3), outside Pantheon.
- `docs/governance/REQUEST_LIFECYCLE.md`: short "The consequential chokepoint"
  section cross-referencing the same rule — the lifecycle decides what is
  consequential, the chokepoint decides whether it may proceed; neither runs the
  work.

## Boundary

Documentation only. No runtime, schema, test, policy engine or protected-path
change; enforcement lives in the execution runtime honouring the check. No new
per-module rule. Lint-clean; no retired vocabulary.
