# AI Log — Schema Test Dependencies Present

Date: 2026-05-30

## Summary

The user selected option B: add schema test dependencies first.

On inspection, `pyproject.toml` already contains the required optional test dependencies:

```toml
[project.optional-dependencies]
test = [
  "pytest>=8.0",
  "PyYAML>=6.0",
  "jsonschema>=4.22",
]
```

No `pyproject.toml` rewrite was performed because the requested dependency state is already present.

## Scope

Read-only inspection plus this ai_log.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

This does not implement CI, Doctor tooling, runtime validation service, approval engine, memory promotion engine, provider router, scheduler, queue, OpenWebUI plugin or Hermes runtime integration.

## Remaining work

- run the read-only schema tests in an environment where the optional test dependencies are installed;
- reconcile any stale `STATUS.md` wording that still says the dependencies need to be declared;
- decide separately whether to add Doctor read-only tooling under protected `operations/`.
