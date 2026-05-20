# Memory Event Scope Alignment

Date: 2026-05-19

## Scope

Follow-up correction on PR #17 before merge.

Updated `docs/governance/MEMORY_EVENT_SCHEMA.md` to prevent scope-taxonomy drift.

## Change

The migrated Pantheon-OS memory-event scope list is explicitly marked as a minimal memory-event reference, not the full canonical scope taxonomy.

`docs/governance/SCOPE_ISOLATION.md` is named as the prevailing document for canonical scope categories and scope-broadening rules.

`SCOPE_ISOLATION.md` was also added to the relationship section of `MEMORY_EVENT_SCHEMA.md`.

## Doctrine boundary

Documentation alignment only.

No runtime, schema, test, operation, platform, Docker, environment file or project configuration was added.

No memory writer, automatic memory promotion, scheduler, queue, provider router, tool runtime or workflow engine was introduced.

## Reason

The original migrated document listed a shorter memory-event scope set inherited from Pantheon-OS. Without clarification, it could be read as competing with the richer canonical scope taxonomy already defined in `SCOPE_ISOLATION.md`.

The correction makes the hierarchy explicit: `MEMORY_EVENT_SCHEMA.md` refines event-level structure, while `SCOPE_ISOLATION.md` governs canonical scope taxonomy.
