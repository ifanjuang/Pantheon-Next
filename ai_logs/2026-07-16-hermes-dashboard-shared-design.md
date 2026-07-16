# Hermes dashboard shared design

Date: 2026-07-16

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: the `control-v1` visual contract to the native Hermes plugin bundle.
- Updated: the generated Pantheon Control preview bundle with the same hero,
  toolbar, cards, badges, nine-state grid and responsive layout.
- Removed: no runtime capability or governance artifact; the duplicate preview
  renderer had already been removed by the single-renderer integration.

## Why

The native Hermes renderer needed to adopt the Pantheon Control visual language.
The GitHub Pages preview now receives that change through the existing generated
copy of the exact plugin bundle, without introducing a second renderer.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: presentation only in the existing Hermes dashboard plugin.
Authority impact: none.
Schema/test/CI impact: design markers added to existing bundle tests; no schema
or CI workflow change.
External action: none performed or newly authorized.
Memory behavior: none.

## Local distinctions

```text
same visual contract != same runtime surface
DEMO data != LIVE inventory
Hermes operation != Pantheon governance activation
enabled != authorized
```

## Validation

- JavaScript syntax checks passed for the single native renderer.
- Plugin-focused tests and exact preview-bundle equality checks passed.
- Root repository tests passed.
