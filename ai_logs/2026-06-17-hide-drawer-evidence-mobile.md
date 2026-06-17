# 2026-06-17 evidence mobile drawer fix

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/style.css` after mobile screenshot review:

- hid the global drawer when `body.ev` is active;
- forced the evidence-card layout/content to full viewport width;
- prevented the side navigation from squeezing the evidence card into a narrow column;
- changed the layered typography sizes to use `clamp()` so the fast-read signal remains large without hard clipping on narrow viewports;
- reduced typographic overlay opacity and offset to keep the echo effect while preserving legibility.

No runtime, registry write, approval, memory promotion or external action was added.
