# AI Log — Negation Vocabulary Extension and Branch Protection Priority

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

Follow-up explicitly requested by the user after the PR #276/#277 review:
"protection et vocabulaire d'abord" — apply the branch-protection
recommendation and extend the runtime-phrase negation vocabulary before
any further Authority Index decomposition work.

Background (see `2026-07-04_authority_index_decomposition_plan_review.md`):
the runtime-phrase guard and its mcp-server mirror flagged a legitimate
negation ("None of these objects is a runtime task...") because "None of"
was missing from the NEGATION vocabulary; the doctrine sentence was
reworded as a workaround. Separately, two merges landed on a red `main`,
truncating the tail of `AUTHORITY_INDEX.md`.

## Changes made

```text
1. Added "none of" to the NEGATION regex in both mirrors:
   - .github/workflows/governance-ci.yml (inline phrase guard);
   - mcp-server/pantheon_mcp/doctor.py (runtime_phrases check).
   The two regexes remain byte-identical alternations. This is a
   vocabulary extension of a read-only check; no new capability,
   runtime or execution path.

2. GITHUB_REPOSITORY_GOVERNANCE.md:
   - the required-checks list now names both CI jobs
     ("Read-only governance checks" and "mcp-server module tests");
   - recorded the 2026-07-04 evidence that missing required checks
     let doctrine-truncating merges land, and marked
     "Require status checks before merging" as the priority setting.
```

## Explicitly not done

```text
- The GitHub branch-protection settings themselves: they live in the
  GitHub UI/API, not in repository files, and require owner action.
  They remain documented non-implemented until applied by the owner.
- No revert of the TRIPARTITE_INTERFACE_SPEC.md rewording (the current
  sentence is fine); the vocabulary fix prevents future occurrences.
- No change to check_index_coverage.py, schemas/, tests/, operations/,
  platform/, Docker files, pyproject.toml or .env files.
```

## Decision classification

```text
Accepté (explicit user decision):
- Extending the negation vocabulary in both checker mirrors.
- Prioritizing branch protection over decomposition follow-ups.

À vérifier:
- Owner application of the branch-protection settings in GitHub UI.
```

## Repo state

```text
Vocabulary extension: implemented (read-only check change).
Branch protection: documented non-implemented (owner action pending).
```
