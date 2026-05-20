# Roadmap CI Wording Alignment

Date: 2026-05-19

## Scope

Follow-up correction on PR #17 after Governance CI failure.

The CI failed on `docs/governance/ROADMAP.md` because an existing risk sentence used the exact forbidden term `scheduler` outside a section context that the read-only guard recognized as negated or excluded.

## Change

Reworded the risk sentence from a direct `scheduler` reference to `autonomous timing loops`.

This preserves the same doctrine: external pattern keepers must not be mistaken as authorization to add autonomous timing, auto-learning, auto-memory or skill marketplace behavior inside Pantheon Next.

## Doctrine boundary

Documentation wording only.

No runtime, scheduler, queue, provider router, tool runtime, workflow engine, memory writer, automatic memory promotion, schema, test, operation, platform file, Docker file, environment file or project configuration was added.

## Note

This is a CI wording alignment, not a new roadmap item and not an implementation claim.
