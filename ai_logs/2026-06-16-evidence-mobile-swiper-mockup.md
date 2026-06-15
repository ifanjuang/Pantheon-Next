# 2026-06-16 — Evidence mobile Swiper mockup

## Status

Documented non-implemented.

This intervention updates the static Pantheon Control asset only. It does not add a runtime, endpoint, queue, scheduler, connector, database table, approval engine, Registre Probatoire writer, memory promotion engine or external action.

## Files changed

- `docs/assets/pantheon-control/evidence.html`
- `docs/assets/pantheon-control/README.md`

## What changed

- Replaced the former card/grid evidence mockup with a mobile-first Swiper.js review surface.
- Added vertical swipe for matters / affaires.
- Added horizontal swipe for evidence subjects inside each matter.
- Added a two-second long-press interaction that opens four round action buttons:
  - promote upward;
  - archive downward;
  - modify left;
  - detail right.
- Added tap-to-expand behavior for additional information.
- Added urgency colors: critical, high, medium, low and information.
- Added a visible fallback `Options` button for users who cannot or do not want to use long press.
- Kept all actions as local UI intentions only. They write to the mock journal and do not mutate the Registre Probatoire.

## Governance boundary

The gesture layer is an exposure-surface pattern. It may show, warn, label, expand detail and prepare an intention candidate.

It must not:

- promote a source into a Registre Probatoire entry;
- archive as a final governed act;
- modify a governed record;
- bypass detail-before-yes for high or critical items;
- create external action;
- imply that swipe equals approval.

The mockup therefore uses candidate language and repeats that no probative status is changed by display or gesture.

## Related repository context checked

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/REVIEW_QUEUE.md`
- `docs/governance/URGENT_REVIEW_TRIAGE.md`
- `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md`
- `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`
- `docs/assets/README.md`
- PR #117, which established the current multi-page Pantheon Control mockup and the propose-only evidence posture.
- Issue #90, which warns against Registre Probatoire vocabulary regression and asks backlog work to avoid old Memory Candidate / Canonical Memory terminology.

## Limitation

The Swiper dependency is loaded from CDN for the static mockup. If the CDN is unavailable, the page remains readable and shows a warning, but the mobile swipe behavior is not active.

No browser-based visual regression test was added.
