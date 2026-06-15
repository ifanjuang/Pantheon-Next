# AI Log — landing page documentation visual pass

**Date:** 2026-06-15
**Scope:** `docs/index.html` and `docs/assets/landing-docs-*.css`

## Intent

Refactor the landing page toward a documentation-style layout inspired by Langfuse Docs while keeping Pantheon Next's governance doctrine intact.

User requested:

- page layout and CSS direction similar to `https://langfuse.com/docs`;
- paragraph treatment;
- strong delimitations;
- icon language.

## Changes applied

- Replaced the dark landing-page composition with a documentation shell:
  - sticky top bar;
  - left documentation navigation;
  - central article surface;
  - right table of contents.
- Kept the header dark after review because the current wordmark asset is white and needs contrast.
- Moved the visual system into split CSS files:
  - `docs/assets/landing-docs-core.css`;
  - `docs/assets/landing-docs-components.css`;
  - `docs/assets/landing-docs-responsive.css`.
- Added small icon badges throughout the page: navigation, hero kicker, cards, callouts, usage blocks and details summaries.
- Reworked paragraph presentation into bordered notes, steps, callouts and compact documentation blocks.
- Preserved the existing D3 mount IDs:
  - `#dossierFlow`;
  - `#flow2a`;
  - `#flow2b`;
  - `#flow3`.
- Preserved the existing D3 script includes:
  - `js/d3-utils.js`;
  - `js/dossier-flow.js`;
  - `js/flow2a.js`;
  - `js/flow2b.js`;
  - `js/flow3.js`.
- Shifted copy away from informal tutoiement toward a neutral professional address.

## Review follow-up

Codex flagged the white wordmark on a light header as insufficiently legible. The feedback was accepted and the header was changed back to a dark surface in `docs/assets/landing-docs-core.css`.

## Boundary

Documented non implemented.

This is a landing-page visual/editorial update only. It does not add runtime behavior, connectors, scheduler, queue, automatic approval, automatic memory promotion, data platform, observability backend or external action.

No protected path touched: no `schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker, `.env` or `CLAUDE.md` change.

## Notes

The CSS was split into multiple small files to keep the patch reviewable and avoid a large inline style block in `docs/index.html`.
