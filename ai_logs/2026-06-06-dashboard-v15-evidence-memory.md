# AI Log — Dashboard v15 Evidence → Memory prototype

Date: 2026-06-06

## Action

Added a static cockpit prototype:

```text
docs/assets/pantheon-dashboard/pantheon-next-gate-page-v15-mobile-drawer.html
```

## Scope

The prototype reflects the current dashboard direction:

- mobile-first drawer navigation;
- Services installed separated from Base & Memory;
- Evidence → Memory section with Sources, Candidates, Subjects, Timeline, Impacts, Conflicts, Updates and Backend sync;
- fast / review / governance friction paths;
- backend distinction between PostgreSQL canon and pgvector / mem0 / Hermes projections;
- example impact chain for pool removal, pool heat pump, terrace, foundations and budget.

## Boundary

Documented non-implemented.

This is a static HTML prototype only. It does not implement runtime checks, database access, memory promotion, backend synchronization, OpenWebUI integration, Hermes execution, approval gates or schema migrations.

## Related docs

- `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md`
- `docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md`
- issue #68

## Repo state

Partiel / documenté non implémenté.
