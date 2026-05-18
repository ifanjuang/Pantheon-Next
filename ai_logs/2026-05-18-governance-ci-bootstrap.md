# Governance CI Bootstrap

Date: 2026-05-18

## Scope

This intervention introduced a minimal, read-only governance CI workflow.

Files added:

- `.github/workflows/governance-ci.yml`.

No other file was created or modified.

The following paths were not touched, in accordance with the playbook coordination rule:

- `pyproject.toml`;
- `schemas/`;
- `tests/`;
- `operations/`;
- `platform/`;
- Docker files;
- `.env*`;
- `CLAUDE.md`.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The CI is read-only by construction.

It does not introduce:

- a runtime;
- a Doctor with auto-remediation;
- a scheduler;
- a queue;
- a provider router;
- a workflow engine;
- a plugin manager;
- a skill installer;
- a memory promotion mechanism;
- an OpenWebUI bridge;
- a Hermes bridge.

It does not perform:

- runtime execution;
- automatic mutation;
- memory promotion;
- deployment;
- Docker build or run;
- schema, test, operations or platform changes.

## Checks implemented

`governance` job, single runner, GitHub Actions + shell + inline Python only. No external dependencies, no `pip install`, no separate scripts.

1. **Mandatory governance files exist** — required baseline files under `docs/governance/`, the repository root and `ai_logs/` must all be present. Fails with the missing path when one is absent.
2. **`ai_logs/` directory exists and contains `README.md`** — explicit separate check for the AI logbook.
3. **STATUS.md does not list migrated files as stub** — the workflow extracts the `## Stub present` section and verifies that `ARCHITECTURE.md`, `MODULES.md`, `CODE_AUDIT_POST_PIVOT.md` and `TASK_CONTRACT_REVISIONS.md` are absent from it. A migrated file left in the stub list fails the build with the offending filename.
4. **`migration-mapping.md` marks migrated files as `migrated`** — for the same four files, the workflow finds the corresponding row in the markdown table at `ai_logs/migration-mapping.md` and verifies its Status column equals `migrated`. A missing row or a non-`migrated` status fails the build with the offending filename.
5. **Governance files do not suggest Pantheon executes** — inline Python scans every `docs/governance/*.md`. For each occurrence of `Pantheon executes`, `Pantheon Agent Runtime`, `Pantheon tool runtime`, `automatic memory promotion`, `hidden workflow runtime`, `provider router`, `scheduler` or `queue`, the workflow checks that the surrounding section (from the nearest markdown heading up to the match line) contains an explicit negation, exclusion or external-scope indicator. An affirmative occurrence fails the build with file, line, phrase and text.

Each step prints `OK` on success and a clear `FAIL: ...` line on failure, followed by an explanation paragraph.

## Triggers

- `push` on branch `main`;
- `pull_request` against any base.

No `schedule` trigger. No cron. No webhook. No event other than push and pull_request.

## Permissions

`contents: read` only. The workflow has no write access to the repository.

## Dry-run

All five steps were dry-run locally against the current `main` HEAD before commit. All passed.

## Risks and limitations

- The stub-list and migration-mapping checks rely on the current Markdown layout of `STATUS.md` and `ai_logs/migration-mapping.md`. A structural change in either file may require updating the extraction logic.
- The runtime-phrase heuristic in step 5 inspects only the nearest markdown section. A future governance document that places an affirmative claim very far from its section header could escape detection.
- The forbidden-phrase list is fixed in the workflow. Additions or removals require a separate PR to this workflow file.
- The workflow does not validate YAML schema structure, does not run `pytest`, does not run `ruff`, does not check external markdown links, and does not deploy anything.

## Next recommended action

When `tests/` and `operations/` are introduced under Phase 4, extend this workflow with a separate `python` job for schema validation and `ruff check`, in a separate PR.
