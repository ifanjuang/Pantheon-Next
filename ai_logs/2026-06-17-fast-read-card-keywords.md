# 2026-06-17 fast-read card keyword override

Status: documented non-implemented.

Updated `docs/assets/pantheon-control/style.css`:

- added a mobile evidence-card fast-read override;
- the primary description is forced to very large `62px` / `font-weight: 950` for one-second scanning;
- the `SOL-001` recto display is overridden to the shorter keyword signal: `Fournitures MOA hors circuit`;
- the original detailed description remains in the HTML/data layer and is not promoted as a canonical evidence mutation;
- reduced-height screens use a `54px` fallback.

No runtime, registry write, approval, memory promotion or external action was added.
