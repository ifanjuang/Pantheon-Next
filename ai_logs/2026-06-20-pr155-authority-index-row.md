# PR155 — authority index correction

Date: 2026-06-20

Scope: documentation-only correction on PR #155.

## Context

PR #155 added `docs/governance/ARCHITECTURE_SOURCE_POLICY.md` as a candidate support doctrine document for `architecture_fr` source treatment, but the PR still lacked the corresponding `AUTHORITY_INDEX.md` row.

## Action

Added one row to `docs/governance/AUTHORITY_INDEX.md`:

```text
| `docs/governance/ARCHITECTURE_SOURCE_POLICY.md` | candidate support doctrine | documented non-implemented | Architecture-fr source treatment policy: source states, authority classes, freshness, project-source priority, Evidence Pack Candidate expectations and output status discipline. No runtime, retrieval engine, source validator, OpenWebUI config or Hermes skill. |
```

## Boundary

Documented non-implemented.

No runtime, schema, test, OpenWebUI configuration, Hermes skill, source validator, operation, platform, Docker, `.env`, `pyproject.toml` or `CLAUDE.md` change.

## Verification

Checked the PR file patch after correction. The final `AUTHORITY_INDEX.md` diff contains only the intended row addition.
