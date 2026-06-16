# AI Log — Pantheon Control Langfuse observability page

Date: 2026-06-16

## Trigger

User chose option 2: integrate the Langfuse Dashboard card into `docs/assets/pantheon-control`.

## Doctrine and repo checks

Checked before editing:

- `docs/governance/STATUS.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/assets/pantheon-control/index.html`
- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/README.md`
- `templates/langfuse-hermes/dashboard-card.langfuse.example.html`
- `templates/langfuse-hermes/dashboard-module.langfuse.example.yaml`

Relevant boundary retained:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

`docs/assets/pantheon-control` is treated as a static cockpit mockup. It may expose status and links; it must not become runtime, approval engine, source of truth, memory engine or Evidence Pack engine.

## Change

Added / updated:

```text
docs/assets/pantheon-control/observability.html
docs/assets/pantheon-control/nav.js
docs/assets/pantheon-control/index.html
docs/assets/pantheon-control/README.md
```

## What was added

- New `Observabilité` page under the Infrastructure section.
- Langfuse link-only card.
- Health-check button targeting `http://localhost:3000/api/public/health`.
- Explicit warning that trace success is not proof, approval or canonical memory.
- Synthetic first-trace expectations: `synthetic-demo`, `synthetic-langfuse-health`, `read_only`, `C0`, `memory_behavior: none`.
- Home page card linking to `observability.html`.
- README page index update.

## Classification

```text
Accepted:
- Static Pantheon Control integration.
- Link-only access to Langfuse.
- Browser-side health check for mockup/testing.
- Synthetic trace refs only.
- Visible runtime/governance boundary.

Refused:
- iframe.
- Langfuse API key in frontend.
- client trace listing.
- client dossier trace emission.
- automatic Evidence Pack creation.
- automatic approval.
- automatic memory promotion.
- external action based on health or trace success.

To verify:
- whether health check must later move to backend due to CORS / network exposure;
- whether actual Langfuse URL remains localhost or becomes LAN/VPN host;
- whether OpenWebUI or another cockpit should later consume the same card pattern.
```

## Boundary

Documented non-implemented.

No Langfuse service was installed.
No container was started.
No `.env`, secret, platform code, Hermes integration, approval engine, Evidence Pack engine or memory engine was added.
