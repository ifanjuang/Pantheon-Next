# 2026-06-20 Pantheon Control mobile drawer

Status: documented/mockup UI correction — no runtime, no service action, no governance behavior implemented.

Updated the static Pantheon Control mockup after mobile review showed the desktop drawer crushing the page content on narrow screens.

Changed:

- `docs/assets/pantheon-control/style.css`
  - hides the navigation drawer by default below 720px;
  - makes the drawer a fixed overlay opened by `body.nav-open`;
  - adds a backdrop and prevents body scroll while the mobile drawer is open;
  - forces content and grids to one-column mobile layout;
  - hides the long doctrine strapline on mobile;
  - prefixes shared toast styling as `pc-toast` to avoid colliding with evidence-page toast styles.
- `docs/assets/pantheon-control/nav.js`
  - adds `closeNav()` / `toggleNav()` helpers;
  - injects a `nav-backdrop` element;
  - closes the drawer on nav click or backdrop click;
  - emits `pc-toast` instead of generic `toast` class.
- `docs/assets/pantheon-control/services.html`
  - replaces hover wording with touch-compatible wording for mobile.

Boundary:

- Static cockpit mockup only.
- No service installation, update, removal or runtime dispatch.
- No approval, memory, Evidence Pack or register behavior changed.

Review note:

This is a direct UI correction under `docs/assets/`, not a platform/runtime change. The repo remains in documented non-implemented posture for this cockpit.
