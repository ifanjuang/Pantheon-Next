# AI Log — local installation and governed channels framing

Date: 2026-05-16

## Scope

Added product-direction documentation for how Pantheon Next should describe local installation, controlled infrastructure, model choice and everyday governed channels.

## Files changed

- `README.md`
- `docs/governance/LOCAL_INSTALLATION_AND_CHANNELS.md`

## Intended but not completed

- `README.fr.md`

A full French README replacement was attempted but blocked by connector safety controls. A later verification confirmed that the French README was not modified in this pass.

The dedicated governance document includes French reader-facing wording so the concept is still documented bilingually.

## Changes

### README English

Added a new section explaining where Pantheon lives:

- around professional dossiers, not above them;
- on controlled infrastructure such as NAS, local server or dedicated workstation;
- with local, cloud or mixed model strategies depending on dossier sensitivity;
- exposed through a dedicated chat cockpit such as OpenWebUI;
- potentially extended through future governed channels such as email, WhatsApp, Telegram, Slack, Trello, Notion, Google Drive, Google Docs, Google Sheets, Outlook or Office.

Expanded the everyday tools table to include:

- Email / Gmail / Outlook;
- Google Drive / Docs / Sheets;
- Office documents;
- Notion / Trello / Slack;
- WhatsApp / Telegram.

### Governance document

Created `docs/governance/LOCAL_INSTALLATION_AND_CHANNELS.md` to clarify:

- infrastructure posture;
- hardware sizing variables;
- local, cloud and mixed model posture;
- OpenWebUI cockpit posture;
- Hermes external runtime posture;
- everyday channels as governed entry points;
- local data posture;
- external boundary conditions;
- wording to use and wording to avoid;
- current implementation status.

## Boundary check

This is documentation-only.

No installer was introduced.

No Docker stack was added.

No runtime behavior was introduced.

No autonomous execution engine, agent runtime, tool runtime, provider router, scheduler, queue, message bus, automatic memory promotion, self-evolution mechanism, plugin installer or hidden orchestration layer was introduced.

No connector was implemented.

No claim was made that Gmail, Outlook, WhatsApp, Telegram, Slack, Google Drive, Notion, Trello, Office or any other external service is currently integrated in Pantheon Next.

The guidance continues to follow the doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Status

Documented but not implemented.

Implementation must be verified capability by capability before any public claim of operational availability.
