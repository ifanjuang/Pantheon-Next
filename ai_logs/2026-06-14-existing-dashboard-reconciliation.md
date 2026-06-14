# AI Log — Existing dashboard reconciliation

Date: 2026-06-14

## Context

After a static standalone cockpit mock was created under `templates/`, the user clarified that Pantheon Next already has a dashboard page.

## Finding

The existing dashboard is under:

- `docs/assets/pantheon-control/`

It was introduced / redesigned in PR #119 as a usage-focused Pantheon Control multi-page mockup.

Relevant files:

- `docs/assets/pantheon-control/README.md`
- `docs/assets/pantheon-control/index.html`
- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/data.js`
- `docs/assets/pantheon-control/machines.html`
- `docs/assets/pantheon-control/services.html`
- `docs/assets/pantheon-control/ia.html`
- `docs/assets/pantheon-control/skills.html`
- `docs/assets/pantheon-control/evidence.html`
- `docs/assets/pantheon-control/files.html`
- `docs/assets/pantheon-control/base-memory.html`
- `docs/assets/pantheon-control/surveillance.html`

## Correction made

Deleted the duplicate standalone mock:

- `templates/pantheon_cockpit_ux_mock.html`

Reason: the cockpit UX should be integrated into the existing Pantheon Control dashboard rather than maintained as a parallel template.

## Boundary state

The canonical work product from this pass remains:

- `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`

The HTML integration remains not done.

No real runtime, UI route, chat engine, editor, connector, approval engine, memory promotion or external action was implemented.

## Follow-up

Recommended next step:

1. Read the existing `docs/assets/pantheon-control/` pages.
2. Apply the UX spec as a targeted follow-up to the existing dashboard, not as a new mockup.
3. Likely additions:
   - add Discussion / Rédaction assistée pages to `nav.js`;
   - add Workflow proposé card to `index.html`;
   - rename or clarify Preuves as `Preuves & sources`;
   - replace any action wording that looks like real validation/execution with candidate wording;
   - keep Services / IA / Skills grouped by function;
   - preserve the static, documented-non-implemented status.
