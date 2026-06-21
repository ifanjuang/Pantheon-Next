# 2026-06-20 Pantheon Control cache-buster

Status: static UI delivery correction — no runtime, no external action, no governance behavior implemented.

Reason:

The mobile drawer correction was present on `main`, but the published GitHub Pages URL could still serve stale `style.css` / `nav.js` because the cockpit HTML referenced local assets without a version parameter.

Changed:

- Added `?v=20260620-mobile-drawer-2` to local `style.css`, `data.js` and `nav.js` references across Pantheon Control HTML pages.
- Added the same version parameter to local evidence modules (`evidence-data.js`, `evidence-render.js`, `evidence-interactions.js`) on `evidence.html`.
- Repaired `drafting.html` typographic JavaScript quotes while touching the file, because the current main copy still contained invalid ECMAScript string delimiters.
- Adjusted `services.html` microcopy to safer candidate wording (`Préparer ajout`, no real service change).

Affected area:

- `docs/assets/pantheon-control/*.html`

Boundary:

- Static mockup delivery only.
- No Pages workflow, runtime, service state change, approval, memory, Evidence Pack or register behavior changed.
- Version query strings are cache invalidation markers only.

Verification:

- Confirmed `index.html` on `main` now references `style.css?v=20260620-mobile-drawer-2`, `data.js?v=20260620-mobile-drawer-2`, and `nav.js?v=20260620-mobile-drawer-2`.
- Confirmed `services.html` on `main` carries the same cache-busted asset references.
- Confirmed `drafting.html` no longer uses typographic quotes as JavaScript string delimiters in the rendered script section.
