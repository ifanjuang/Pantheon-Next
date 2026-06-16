# AI Log — landing dark square UI pass

**Date:** 2026-06-16
**Scope:** `docs/assets/landing-docs-core.css`, `docs/assets/landing-docs-components.css`, `docs/assets/landing-docs-responsive.css`

## Intent

Apply a darker, sharper UI pass to the Pantheon Next landing page after the documentation-style landing page was merged.

User requested:

- switch to a dark UI;
- remove rounded corners;
- remove shadows;
- reduce and contain diagrams that were too large and overflowing the screen.

## Changes applied

- Switched the landing CSS palette to a dark surface system.
- Removed border radii from navigation chips, cards, notes, callouts, buttons, footer links, poster image and mobile navigation container.
- Removed visual shadows and diagram node drop shadows.
- Reworked diagram containers to use dark surfaces and `overflow: auto`.
- Removed forced mobile SVG `min-width` values that caused horizontal overflow.
- Added max-height limits for diagrams on desktop, tablet and mobile.

## Boundary

Documented non implemented.

This is a visual CSS update only. It does not add runtime behavior, connectors, scheduler, queue, automatic approval, automatic memory promotion, observability backend, data platform or external action.

No protected path touched: no `schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker, `.env` or `CLAUDE.md` change.

## Notes

This was committed directly on `main` because branch creation was blocked by the connector during this pass and the touched files are within the allowed documentation/assets scope.
