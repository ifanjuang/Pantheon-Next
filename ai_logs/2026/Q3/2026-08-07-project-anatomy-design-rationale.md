# AI log — Project Anatomy design rationale preservation

Date: 2026-08-07
Repository: Pantheon-Next

## Context

PR #587 stabilized active Project Anatomy artifact identities and made `PROJECT_ANATOMY_MODEL.md` the sole active conceptual authority. During final review, the removed design-review document was found to contain substantial historical reasoning and rejected alternatives not fully duplicated in the frozen model.

## Change

Restore that material under the stable filename `docs/domain-packs/architecture/PROJECT_ANATOMY_DESIGN_REVIEW.md` with an explicit non-authoritative banner.

## Authority rule

`PROJECT_ANATOMY_MODEL.md` remains the sole active conceptual authority.

`PROJECT_ANATOMY_DESIGN_REVIEW.md` is historical design rationale only and must not be used as an implementation contract.

## Non-effects

This change does not alter schemas, validation rules, persistence, runtime, approval, Evidence, Revit behavior, Hermes behavior, or external effects.