# AI Log — Project document control dashboard

Date: 2026-06-15

## Context

The user wanted to keep the Kroqi-inspired documentary logic and implement it in the existing Pantheon Control dashboard for now.

The implementation remains limited to the static dashboard under `docs/assets/pantheon-control/`.

## Governance check

Active governance boundaries were reviewed:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

The implementation remains a static exposure mock. It does not add a runtime or any real integration.

## Files changed

Updated:

- `docs/assets/pantheon-control/data.js`
- `docs/assets/pantheon-control/nav.js`
- `docs/assets/pantheon-control/files.html`
- `docs/assets/pantheon-control/README.md`

## Result

The former `Fichiers` page is now surfaced as `Documents projet` in the navigation.

The page now shows:

- document folders with project, path, status, RAG usability and sync state;
- project documents with version, dossier, source status, vectorization state, Knowledge sync and IA usability;
- status distinctions between active, candidate, to verify, replaced, archived and excluded from default IA use;
- request-preparation buttons for activation, archive and RAG removal;
- a local journal of candidate requests;
- explicit wording that IA productions remain in discussion branches, not in the documentary Knowledge base.

## Boundary

This is still documented non implemented.

No real file operation, folder move, archive action, RAG update, OpenWebUI sync, oikb sync, vectorization, Ollama call, backend route, database update, external action or register write was implemented.

## Follow-up

Recommended next steps:

1. Review the dashboard visually.
2. Decide whether `files.html` should eventually be renamed to `documents.html` while preserving redirects or links.
3. If a real implementation is planned, design the document registry schema separately and request confirmation before editing protected paths.
