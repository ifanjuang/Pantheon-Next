# GitHub repository governance guards

Date: 2026-06-23

## Context

After Governance CI dependency centralization, direct pinning and lightweight lockfile setup, the next repository-level improvement was to expose GitHub-native safeguards for Pantheon Next.

The goal is not to make GitHub a governance authority. The goal is to use GitHub as a procedural guardrail around `main`.

## Change

This intervention adds:

```text
.github/CODEOWNERS
.github/dependabot.yml
docs/governance/GITHUB_REPOSITORY_GOVERNANCE.md
ai_logs/2026-06-23-github-repository-governance-guards.md
```

## Scope

- `CODEOWNERS` requests review on sensitive repo areas.
- Dependabot proposes dependency updates on a weekly, low-volume cadence.
- The governance doc records the recommended branch protection settings for `main`.

## Not performed

Branch protection settings were not changed through the GitHub UI in this intervention.

Those settings must still be applied manually in repository Settings unless a future tool exposes branch protection configuration.

## Governance classification

Status: documented and partially implemented repository procedure.

Authority: support / validation-only.

Decision Zeus: accepted for repo guardrails; GitHub Settings still to verify after manual configuration.

Repository state: partial.

Implemented:

```text
CODEOWNERS
Dependabot config
GitHub repository governance support document
ai_log
```

Not implemented:

```text
GitHub branch protection UI settings
```

This does not change Pantheon doctrine, schemas, tests, runtime behavior, approval behavior, memory rules or execution boundaries.

## Risk and limitations

Dependabot proposals are candidates, not accepted changes.

CODEOWNERS requests review, but it only becomes merge-blocking if GitHub branch protection requires Code Owner review.

No changes were made under `schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker or `.env`.
