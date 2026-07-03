# AI log — open branch landing roadmap update

Date: 2026-07-03

## Scope

Updated the existing `docs/governance/OPEN_BRANCH_LANDING_PLAN.md` after human acceptance of the proposed roadmap.

## Source of truth read

Before the update, the active governance docs were checked again:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

The existing `OPEN_BRANCH_LANDING_PLAN.md` was used rather than creating a new roadmap document.

## Change summary

Inserted the current landing roadmap:

1. Post-Claude cleanup.
2. Reduce old draft noise for #189 / #190.
3. Qualify external-reference PRs #265 / #260.
4. Review #269 runtime-health prototype under a strict static/read-only boundary.
5. Keep #264 as maintainer / external-infra block.
6. After cleanup, prove the external OpenWebUI -> Hermes loop outside the repository.

Also moved recent merged PRs #268, #267, #266, #263, #259, #258, #256, #255, #254, #253, #252, #251 and #250 into the historical landing table with status notes.

## Decision classification

Accepted:

- A -> B -> C order: repository landing, then visible UX, then external proof loop.
- Keep runtime proof outside this repository.
- Treat #264 as maintainer/external-infra, not ordinary docs landing.

To verify:

- #269 must remain static/read-only before merge.
- #260/#265 must remain external references / candidates only.
- #190/#189 require split, extraction or closure before any landing.

Refused:

- Adding more doctrine before reducing existing draft noise.
- Treating runtime-health display as live monitoring/control.
- Treating the external OpenWebUI -> Hermes run as implemented in the repo.

## Repo state

- Roadmap/documentation coordination: implemented.
- Runtime implication: non applicable.
- Protected paths touched: none.
