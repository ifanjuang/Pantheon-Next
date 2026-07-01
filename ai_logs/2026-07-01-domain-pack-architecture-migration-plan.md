# AI log — architecture domain pack migration plan (B-4, table before move)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-4 (accepted): move the architecture-domain docs into
`docs/domain-packs/architecture/`, generic rules staying in `docs/governance/`.
Per the maintainer's own guardrail ("do not move the architecture docs without an
old → new path table"), deliver the table first; move nothing yet.

## What was produced

- `docs/audits/2026-07-01-domain-pack-architecture-migration-plan.md` (validation-only):
  the old → new path table for the **24** `docs/governance/ARCHITECTURE_*.md` files
  (proposed target `docs/domain-packs/architecture/<name>` with the `ARCHITECTURE_`
  prefix dropped), with per-file live-reference counts. Records the sweep scope
  (**154 inbound reference locations** across `docs/` + `README.md`; `ai_logs/` left
  as history) and flags the one choice for the maintainer (drop the prefix or keep it).

## Not done here (deliberate)

No file is moved and no reference is rewritten. The generic rules
(`DOMAIN_PACK_SPEC.md`, `CAPABILITY_PLACEMENT.md`, `METHOD_CARD_MODEL.md`,
`METHOD_CARD_HERMES_HANDOFF_SPECIALIZATION.md`) stay in `docs/governance/`. On
approval, a separate PR runs `git mv` + the full reference sweep + `AUTHORITY_INDEX`
updates in one reference-complete commit, keeping the CI internal-link check green.

## Boundary

Plan only. Moves nothing, promotes nothing, changes no schema/test/runtime.
