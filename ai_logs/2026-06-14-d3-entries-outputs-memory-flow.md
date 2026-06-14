# AI Log — D3 entries / outputs / memory flow

Date: 2026-06-14

## Trigger

User asked to implement the improved `Entrées · Sorties · Mémoire` schema in D3.js in the repository.

## Doctrine read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

## Related discussion checked

- Open PR search for dashboard / D3 / landing / cockpit.
- PR #126 uses `D3` for schema reconciliation, not D3.js rendering.
- PR #127 concerns a PaddleOCR dashboard install candidate and has an unrelated indexing review.
- No open issue matching the landing flow diagram request was found.

## Change

Added a standalone D3.js documentation page:

- `docs/assets/pantheon-flow/entries-outputs-memory-d3.html`

The diagram narrows the `PÉRIMÈTRE DE TRAVAIL IA` rectangle to keep the lateral return arrows legible, updates the doctrinal wording from `hors cadre` to `hors exécution`, and separates human arbitration, external action and memory promotion.

## Boundary

Documentation / visual asset only.

No runtime, queue, scheduler, approval engine, memory engine, provider router, connector, external action, schema, test, platform, operation or Docker change.

## Repo state

Documented non implemented: the page visualizes the governance path but does not execute it.

## Verification

Expected diff limited to:

- `docs/assets/pantheon-flow/entries-outputs-memory-d3.html`
- `ai_logs/2026-06-14-d3-entries-outputs-memory-flow.md`
