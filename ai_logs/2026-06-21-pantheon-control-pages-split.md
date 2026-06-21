# 2026-06-21 — Pantheon Control pages split

Status: documented UI refactor — static mockup only.

## Context

Issue #182 tracks the refactor of Pantheon Control static cockpit modules. Earlier work already introduced a shared `ui.js` helper file and modularized `evidence.html` through `evidence_data.json`, `evidence-data.js`, `evidence-render.js` and `evidence-interactions.js`.

The remaining debt was not to create sharing from scratch, but to prevent `ui.js` from becoming a page-rendering bucket.

## Doctrine checked

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Boundary retained:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

This change keeps Pantheon Control as a static exposure surface. It does not add runtime execution, connector execution, approval behavior, memory promotion, schema changes, tests, Docker, operations or platform code.

## Change

`ui.js` is reduced to reusable helpers:

```text
panel()
card()
kv()
queue()
safeName()
depotLien()
```

Page-specific renderers move to:

```text
docs/assets/pantheon-control/pages/home.js
docs/assets/pantheon-control/pages/services.js
docs/assets/pantheon-control/pages/machines.js
docs/assets/pantheon-control/pages/ia.js
docs/assets/pantheon-control/pages/skills.js
docs/assets/pantheon-control/pages/files.js
docs/assets/pantheon-control/pages/base-memory.js
docs/assets/pantheon-control/pages/surveillance.js
docs/assets/pantheon-control/pages/references.js
```

The standard HTML pages now load:

```text
data.js
optional page data file
nav.js
ui.js
pages/<page>.js
```

`evidence.html`, `decision-ui.js`, `observability-ui.js` and the evidence modules are left unchanged because they are already separate or intentionally specialized.

## Validation performed

- `node --check` on `ui.js` and all new `pages/*.js` modules.
- Manual review of script load order in updated HTML shells.

## Repo state

Partiel / documented UI mockup. No implementation claim beyond static HTML/JS refactor.
