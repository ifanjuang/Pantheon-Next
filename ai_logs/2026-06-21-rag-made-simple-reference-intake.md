# AI log — RAG Made Simple reference intake

Date: 2026-06-21
Repository: `ifanjuang/Pantheon-Next`

Issue: #179
Follow-up issue: #183
Related PR: #176

## Request

User asked to integrate `RAG Made Simple`, expose it in HTML docs, improve the RAG section, continue, factor cockpit references so dashboard and references share the same CSS/data pattern, continue the same factorization for the cockpit pages, then clarify the cockpit information architecture around IA, services, connections, machines, secure external access and cockpit labels.

## Files read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/index.html`
- `docs/assets/pantheon-control/index.html`
- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/style.css`
- `docs/assets/pantheon-control/data.js`
- `docs/assets/pantheon-control/connections-data.js`
- `docs/assets/pantheon-control/connections-ui.js`
- `docs/assets/pantheon-control/references.html`
- `docs/assets/pantheon-control/services.html`
- `docs/assets/pantheon-control/machines.html`
- `docs/assets/pantheon-control/ia.html`
- `docs/assets/pantheon-control/skills.html`
- `docs/assets/pantheon-control/files.html`
- `docs/assets/pantheon-control/base-memory.html`
- `docs/assets/pantheon-control/surveillance.html`
- `docs/assets/pantheon-control/discussion.html`
- `docs/assets/pantheon-control/drafting.html`
- `docs/assets/pantheon-control/evidence.html`
- `docs/assets/pantheon-control/evidence-render.js`
- `docs/assets/pantheon-control/evidence-interactions.js`
- `docs/assets/pantheon-control/ui.js`
- `docs/assets/pantheon-control/decision-ui.js`
- `docs/assets/pantheon-control/evidence-ui.js`
- `docs/assets/pantheon-control/evidence.css`
- `docs/assets/landing-docs-core.css`
- `docs/assets/landing-docs-components.css`
- `docs/assets/landing-docs-responsive.css`

## Decisions

Decision Zeus: Accepté, with strict boundary.

PR #176 remains draft. It was not merged. A short review comment marked it `À arbitrer before merge`.

`docs/index.html` was not edited directly because it is dense and needs a safer refactor first.

Cockpit pages now use shared data, shared navigation and shared render helpers.

For consequential interaction pages, a dedicated `decision-ui.js` layer was added instead of growing `ui.js` into a monolith.

For the evidence page, the existing separation between `evidence-data.js`, `evidence-render.js` and `evidence-interactions.js` was preserved. The inline mobile style and template boot were extracted into `evidence.css` and `evidence-ui.js`.

The standalone `IA` navigation model was rejected as a primary cockpit category. Cloud AI accounts are now classified as external connections under Services & connexions. Local models are classified by machine / local instance under Machines & instances. Secure external access is modeled generically as candidate access routes, not as a fixed VPN/Synology/subdomain architecture.

Cockpit labels were clarified:

- `Surveillance` / `Journal` -> `Journal & contrôles`
- `Discussion` -> `Branches de décision`
- `Rédaction assistée` -> `Rédaction candidate`
- `Base & mémoire` -> `Registres & mémoire`

Filenames were kept stable to avoid breaking links.

## Changes made

Created:

- `docs/governance/reference_reviews/RAG_MADE_SIMPLE_REFERENCE_REVIEW.md`
- `docs/governance/reference_reviews/index.html`
- `docs/rag-probatoire.html`
- `docs/assets/pantheon-control/references.html`
- `docs/assets/pantheon-control/ui.js`
- `docs/assets/pantheon-control/decision-ui.js`
- `docs/assets/pantheon-control/evidence.css`
- `docs/assets/pantheon-control/evidence-ui.js`
- `docs/assets/pantheon-control/connections-data.js`
- `docs/assets/pantheon-control/connections-ui.js`
- issue #183, `Docs HTML refactor: landing index and shared components`

Updated:

- `docs/rag-probatoire.html`
- `docs/assets/pantheon-control/index.html`
- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/data.js`
- `docs/assets/pantheon-control/connections-data.js`
- `docs/assets/pantheon-control/connections-ui.js`
- `docs/assets/pantheon-control/references.html`
- `docs/assets/pantheon-control/services.html`
- `docs/assets/pantheon-control/machines.html`
- `docs/assets/pantheon-control/ia.html`
- `docs/assets/pantheon-control/skills.html`
- `docs/assets/pantheon-control/files.html`
- `docs/assets/pantheon-control/base-memory.html`
- `docs/assets/pantheon-control/surveillance.html`
- `docs/assets/pantheon-control/discussion.html`
- `docs/assets/pantheon-control/drafting.html`
- `docs/assets/pantheon-control/evidence.html`
- `docs/assets/pantheon-control/ui.js`
- `docs/governance/reference_reviews/index.html`
- this AI log

Issue #179 was commented and closed after completion.

Issue #183 was updated with cockpit reference page, shared data progress, shared UI helper progress, core cockpit page extraction, decision-page extraction and evidence page extraction.

## Boundary preserved

No protected path changed.
No schema changed.
No test changed.
No runtime created.
No PDF binary committed.
No RAG ingestion pipeline created.
No vector database selected.
No approval engine created.
No memory engine created.
No external transmission created.
No evidence register write created.
No VPN, gateway, DNS, reverse proxy, NAS or account was configured.

## Result

Documented non-implemented.
Candidate-only external reference.
Visible from cockpit, reference index, and `docs/rag-probatoire.html`.

Cockpit pages now share:

- `style.css` for base styling;
- `data.js` for mock governance/reference data;
- `nav.js` for shell and navigation;
- `ui.js` for general rendering;
- `decision-ui.js` for decision/rédaction candidate rendering;
- `evidence.css` for evidence mobile styling;
- `evidence-ui.js` for evidence mobile boot/template;
- `connections-data.js` for external connections, secure access candidates and local instance candidates;
- `connections-ui.js` for Services & connexions / Machines & instances rendering.

Thin entrypoints now include:

- `docs/assets/pantheon-control/index.html`
- `docs/assets/pantheon-control/references.html`
- `docs/assets/pantheon-control/services.html`
- `docs/assets/pantheon-control/machines.html`
- `docs/assets/pantheon-control/surveillance.html`
- `docs/assets/pantheon-control/discussion.html`
- `docs/assets/pantheon-control/drafting.html`
- `docs/assets/pantheon-control/evidence.html`

Remaining large item:

- public landing `docs/index.html`, intentionally untouched.
