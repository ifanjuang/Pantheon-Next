# AI Log — Pantheon Cockpit UX mock

Date: 2026-06-14

## Context

After creating `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`, the user asked to continue.

The next safe step was to produce a non-executable mockup rather than modify the deployed `docs/index.html` directly. The existing landing page was inspected, but not edited.

## Change made

Created:

- `templates/pantheon_cockpit_ux_mock.html`

The mockup expresses the cockpit candidate in a static HTML file:

- cabinet navigation;
- workflow proposal card;
- risk and missing-evidence display;
- decision buttons ordered by review path;
- hierarchical discussion branches;
- assisted drafting panel;
- Proofs and sources panel;
- Capability Gap panel;
- system health view for non-technical users;
- local / external AI cost summary.

## Boundary state

This is a static template only.

It does not implement:

- a UI route;
- a runtime;
- a chat engine;
- branching logic;
- an editor;
- a connector;
- Google Apps Script;
- Office add-in;
- approval workflow;
- memory promotion;
- external action.

No protected paths were changed.

## Rationale

`docs/index.html` is a real published landing page and was left untouched in this pass.

The template can be reviewed first and later projected into the landing page or a future cockpit mock if accepted.

## Follow-up

Recommended next steps:

1. Review the mockup wording against `PANTHEON_COCKPIT_UX_SPEC.md`.
2. Decide whether to adapt `docs/index.html` or create a dedicated `docs/cockpit.html` page.
3. If a real UI is later created, keep the labels candidate/proposed/to verify/human decision required.
4. Avoid saying implemented until the cockpit exists outside this static template.
