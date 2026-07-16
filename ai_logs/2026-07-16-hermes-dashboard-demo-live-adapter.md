# AI log — Hermes dashboard demo/live adapter

Date: 2026-07-16

## Scope

Added a GitHub Pages preview that uses one read-only dashboard data contract with
two explicit sources:

- a synthetic JSON fixture when served as static documentation;
- the audited native Hermes dashboard SDK when the same page is hosted with that
  SDK available.

## Files

- `docs/assets/pantheon-control/hermes-modules.html`
- `docs/assets/pantheon-control/hermes-modules-adapter.js`
- `docs/assets/pantheon-control/hermes-modules-demo.json`
- `docs/assets/pantheon-control/hermes-modules.css`
- `docs/assets/pantheon-control/pages/hermes-modules.js`
- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/README.md`

## Safety boundary

The preview is read-only. It exposes no install, enable, disable, trigger, edit,
delete, secret or Cron mutation action.

Demo data is accepted only when `meta.synthetic === true`. The UI displays a
permanent source badge. If live mode is requested without the Hermes SDK, or if
all live reads fail, the page fails closed and never silently substitutes demo
data.

The operational JSON is produced in memory from the Hermes SDK and is never
committed to GitHub. Hermes enablement remains distinct from Pantheon governance
activation and task authorization.

## Validation

- JavaScript syntax checks passed for the adapter and renderer.
- The demo fixture parses as JSON.
- A Node smoke test confirmed live SDK selection.
- A negative smoke test confirmed that forced live mode cannot fall back to demo.
