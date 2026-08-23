# 2026-08-23 — history-preserving pantheon-mvp monorepo import

Status: migration trace — candidate branch / protected review required.

## Objective

Consolidate the executable `ifanjuang/pantheon-mvp` candidate implementation into the canonical `Pantheon-Next` repository without collapsing governance authority into executable code and without creating a second implementation trajectory.

## Verified source state

At migration cutoff:

```text
Pantheon-Next/main = 7971a7f4694b9f0214d1ffdb3c657df028f94ad1
pantheon-mvp/main  = d960862dd0e23b7003a0f3e4ee0ea630ffc12af9
```

No competing monorepo/implementation migration branch was found. `pantheon-mvp` had no open PR. `Pantheon-Next` drafts #685 and #686 were unrelated to repository consolidation. Workspace/vault issue #684 remained a design/convergence issue and was not used as authorization to implement its professional-document slice through this migration.

Both source `main` refs were rechecked during the migration and remained unchanged.

## Decision

Use one Git repository with explicit internal responsibility boundaries:

```text
canonical governance surfaces
        ↓ consumed by
mcp-server/ and implementation/
        ↓ integrated with
external runtimes / private deployment
```

The executable candidate implementation is placed under `implementation/`.

```text
same repository != same authority
implementation success != authorization
schema conformance != professional approval
projection != persistence
workspace folder != governed identity
retrieved data != truth
memory != Evidence
```

The former sibling-repository placement decision is superseded by `docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md`. Historical references remain in Git and dated status/reconciliation records where they describe the state that was true when recorded.

## History import

The local execution environment could not resolve `github.com`, so the history rewrite was executed by a one-shot GitHub Action on branch `chore/monorepo-absorb-mvp`.

The action:

1. cloned `ifanjuang/pantheon-mvp`;
2. checked out exact cutoff `d960862dd0e23b7003a0f3e4ee0ea630ffc12af9`;
3. ran `git filter-repo --force --to-subdirectory-filter implementation`;
4. merged the rewritten history into the branch with unrelated histories allowed;
5. recorded `implementation/IMPORT_PROVENANCE.md`;
6. remapped the Radix Icons submodule in root `.gitmodules`;
7. deleted the one-shot import workflow after completion.

The resulting branch retained the rewritten implementation commit graph rather than flattening it into one copy commit. Therefore PR #690 must be integrated by merge commit, not squash or rebase merge.

The former `pantheon-mvp` repository remains the historical reference for original PRs, issues and original commit SHAs. Archival is deferred until the merged monorepo is stable.

## Runtime/package boundary

The repository root remains intentionally non-distributable.

```text
root pyproject.toml       = tooling/governance workspace only
mcp-server/pyproject.toml = bounded policy/verification distribution
implementation/pyproject.toml = executable candidate implementation distribution
```

No `mvp_vertical` rename, PostgreSQL redesign, Cockpit redesign or schema-semantics change is part of this import tranche.

## CI/workflow convergence

Imported workflows under `implementation/.github/workflows/` are inert because GitHub activates workflows only from repository-root `.github/workflows/`.

Active root equivalents were added for:

- primary implementation CI;
- permanent architecture-convergence audit;
- Hermes 0.20.0 lab acceptance;
- Hermes 0.20.0 Project Variant lab;
- Hindsight Hermes O1 sandbox;
- Hindsight Obsidian O2 sync;
- Hindsight Obsidian Hermes O3 shared-bank lab;
- transitional schema-drift monitor.

The architecture audit intentionally keeps the old logical repository names during this first tranche while rooting implementation scans at `implementation/`. Repo-identity → zone/component-identity migration is deferred.

## Live-lab compatibility finding

Several imported live-lab scripts intentionally assumed the old GitHub Actions sibling path:

```text
$GITHUB_WORKSPACE/pantheon-mvp
```

A transitional Actions-only symlink maps that path to `monorepo/implementation` so historical scripts continue to exercise the same behavior.

The Hermes plugin installer also performs a real `git clone file://...`; a symlinked subdirectory is not itself a Git repository. `run_hermes_020_lab_acceptance.sh` was therefore made layout-aware: it resolves the containing Git worktree and constructs the plugin source with the correct monorepo subdirectory. In the old standalone layout the calculation resolves to the original plugin path.

During this adjustment, an incomplete rewrite of the lab shell temporarily replaced the canonical `observe → launch → wait-run → reconcile` sequence with a nonexistent helper command. The discrepancy was detected by the live lab, compared against exact `pantheon-mvp@d960862`, and corrected by restoring the cutoff sequence while retaining only the layout-aware plugin-source resolution.

Observed after correction on commit `27dcc2f76824730dcf583c65e7c44aa843ca813e`:

```text
Hermes 0.20.0 Lab Acceptance        success
Hermes 0.20.0 Project Variant Lab success
Governance CI                        success
```

Earlier migration heads also established successful primary implementation contract tests/full PostgreSQL-pgvector tests, architecture audit, Hindsight O1 and Hindsight O2 runs. Final-head checks remain the merge criterion.

## Current-status reconciliation

Current repository-facing documents were updated so the merged repository does not claim that its implementation still lives only in an external sibling repository:

- `README.md`;
- `README.fr.md`;
- `CLAUDE.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/WHAT_RUNS.md`;
- `docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md`.

Historical dated reconciliation text is preserved where it records the prior state and is explicitly distinguished from current placement.

## Deliberately deferred

The first tranche keeps behavior and contract resolution stable where possible. Follow-up convergence remains required for:

1. architecture audit repository identities → bounded zones/components;
2. Hermes distribution-lock source repository identities → component/root identities;
3. direct consumption of canonical root schemas by implementation build/test;
4. removal of committed `implementation/mvp_vertical/vendor/pantheon` duplication, provenance sidecars, revendor tooling and schema-drift monitor only after direct consumption is proven;
5. retirement of the transitional `$GITHUB_WORKSPACE/pantheon-mvp` alias after live-lab scripts become path/zone-native;
6. selective reconciliation of non-current historical/support references that still name the former repository;
7. archival/redirect of `ifanjuang/pantheon-mvp` only after merged monorepo validation.

## No authority effect

This repository migration does not:

- install or activate Hermes, OpenWebUI, Paperless or a deployment;
- authorize a task;
- approve a professional effect;
- admit Evidence;
- promote memory;
- create a governed Professional Document identity from a workspace folder;
- convert Cockpit projection into persistence;
- make PostgreSQL records authoritative merely by persisting them.

The migration changes hosting and integration topology. Governance distinctions remain unchanged.
