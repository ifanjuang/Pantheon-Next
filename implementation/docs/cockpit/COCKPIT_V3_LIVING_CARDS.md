# Cockpit V3 — Living Cards

Status: candidate implementation in `pantheon-mvp`.

## Purpose

Cockpit V3 gives the operational Cockpit a recognisable physical-card language without changing Pantheon authority, data ownership or governance semantics.

The visual projection remains downstream of the server-authoritative card model:

```text
entity / governed state
→ projection
→ renderer
→ material assignment
→ DOM
```

A gradient is presentation metadata only. It is not a status, an authorization, Evidence, a claim or a source-of-truth marker.

## Canonical page

`mvp_vertical/cockpit/index.html` is the single cockpit page, served at `/cockpit/`. The repository root redirects the GitHub Pages demo to `mvp_vertical/cockpit/index.html?mode=demo`.

The page keeps current V2 element identifiers and operational modules as a compatibility seam while exposing a dedicated `v3_bootstrap.js` entrypoint and V3 page state. The parallel `v2.html` and `v3.html` pages were removed once the cockpit was consolidated onto this single page; the shared `v2_*` modules remain — they are the live renderer.

The visible navigation button row is removed from the V3 surface but retained as an off-screen compatibility bridge because the current Swiper adapter still delegates navigation to those controls. This is temporary implementation compatibility, not the target navigation architecture.

## Interaction contract

- horizontal swipe: move between siblings through the existing spatial navigation bridge;
- vertical gesture/navigation bridge: ascend or descend through the existing navigation stack;
- tap or keyboard activation on a non-interactive card area: flip front/back;
- front: reading surface;
- back: technical details and actions already supplied by the current renderer;
- Hermès remains opt-in through the existing dock button.

## Material registry

`mvp_vertical/cockpit/v3/materials.json` is a versioned presentation registry.

Assignment is deterministic from stable projected identity where available. The same card therefore receives the same material without storing a consequential value in the backend.

The registry does not encode card family, status, approval, health, safety or task authorization.

## Current implementation slice

This branch deliberately reuses the existing V2 card DOM and flip model. It adds:

- a first-class V3 page and bootstrap entrypoint;
- a dark, neutral Cockpit background;
- multicolour organic card materials;
- deterministic material assignment;
- direct card flip by tap, Enter or Space while preserving embedded controls;
- reduced-motion and keyboard focus handling;
- progressive enhancement: registry failure leaves the V2 Cockpit operational.

## Navigation boundary

This section described `v2_swiper.js`, which rebuilt its shell after every projected card change. That adapter has been replaced: navigation now goes through `NavigationState` and a thin `MotionAdapter` (see `docs/architecture/cockpit-navigation-lifecycle.md`), and Swiper is no longer rebuilt. The regression concerns it listed remain the ones to watch when the presentation changes again:

- sibling cursor synchronisation;
- first-card create action;
- disabled previous/next boundaries;
- mobile/desktop media changes;
- nested collection ownership;
- focus and form controls;
- no duplicate ids in neighbouring projections.

The target remains:

```text
SpatialNavigation / future NavigationEngine
→ ProjectionWindow
→ stable Swiper shell
→ recycled previous/current/next slides
```

This visual PR does not claim that migration is complete.

## Preserved distinctions

```text
projection != governed value
material != status
UI state != authorization
runtime success != Evidence
installed != approved
healthy != safe
activated != task_authorized
```
