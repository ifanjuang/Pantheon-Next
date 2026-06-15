# AI Log — landing page documentation visual pass

**Date:** 2026-06-15
**Scope:** `docs/index.html`

## Intent

Refactor the landing page toward a documentation-style layout inspired by Langfuse Docs while keeping Pantheon Next's governance doctrine intact.

User requested:

- page layout and CSS direction similar to `https://langfuse.com/docs`;
- paragraph treatment;
- strong delimitations;
- icon language.

## Changes planned

- Light documentation shell with sticky top bar, left navigation, central article and right table of contents.
- Bordered sections, callouts, compact paragraph blocks and card delimitations.
- Inline SVG icon system, with no new external icon dependency.
- Existing D3 mount IDs retained: `#dossierFlow`, `#flow2a`, `#flow2b`, `#flow3`.
- Existing D3 script includes retained.
- Tone shifted away from informal tutoiement toward a neutral professional address.

## Boundary

Documented non implemented. This is a landing-page visual/editorial update only. It does not add runtime behavior, connectors, scheduler, queue, automatic approval, automatic memory promotion, data platform, observability backend or external action.

No protected path touched.
