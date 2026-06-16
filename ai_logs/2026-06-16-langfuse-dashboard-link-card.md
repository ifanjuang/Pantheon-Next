# AI Log — Langfuse Dashboard link card candidate

Date: 2026-06-16

## Trigger

User asked whether Langfuse could be integrated into the Dashboard and then approved proceeding.

## Doctrine read first

Read or checked before the change:

- `docs/governance/STATUS.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- existing Langfuse manifest `templates/langfuse-hermes/dashboard-module.langfuse.example.yaml`

Relevant rule retained:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The exposure surface may display status, warnings, links, candidate status and Task Contract / Evidence Pack references. It must not become runtime, automatic approval, source of truth or automatic memory promotion.

## Change

Added / updated:

```text
docs/governance/reference_reviews/LANGFUSE_DASHBOARD_LINK_CARD_CANDIDATE.md
templates/langfuse-hermes/dashboard-module.langfuse.example.yaml
templates/langfuse-hermes/dashboard-card.langfuse.example.html
```

## Classification

```text
Accepted:
- Dashboard card candidate.
- Link-only Langfuse access.
- Health-check display.
- Synthetic trace refs only.
- Governance status remains distinct from runtime status.

Refused:
- iframe for first test.
- Langfuse API key in frontend.
- Client trace listing.
- Client dossier trace emission.
- Automatic Evidence Pack creation.
- Automatic approval.
- Automatic memory promotion.
- External action based on health or trace success.

To verify:
- actual Dashboard runtime path;
- config location;
- backend-vs-browser health check execution context;
- CORS/auth behavior once Langfuse is installed;
- whether the card is copied into OpenWebUI, a static cockpit, or another exposure surface.
```

## Boundary

Documented non-implemented.

No Dashboard runtime code was identified or modified.
No platform code was changed.
No Langfuse service was installed.
No container was started.
No `.env`, secret, Hermes integration, approval engine, Evidence Pack engine or memory engine was added.
