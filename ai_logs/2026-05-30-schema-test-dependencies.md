# AI Log — Schema Test Dependencies

Date: 2026-05-30

## Summary

Declared optional test dependencies for read-only schema validation.

The user explicitly selected the protected-file path to update `pyproject.toml` before continuing toward Doctor tooling.

## File changed

- `pyproject.toml`

## Dependency scope

Added optional test dependencies under:

```toml
[project.optional-dependencies]
test = [
  "pytest>=8.0",
  "PyYAML>=6.0",
  "jsonschema>=4.22",
]
```

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

This change supports test execution only.

It does not implement:

- runtime behavior;
- CI;
- Doctor tooling;
- operations tooling;
- schema mutation service;
- approval engine;
- memory promotion engine;
- workflow engine;
- provider router;
- scheduler;
- queue;
- OpenWebUI plugin;
- Hermes runtime integration.

## Notes

The existing `tests/test_governance_schemas.py` remains read-only.

The dependencies allow full YAML and JSON Schema validation when the test extra is installed.

No tests were executed in this intervention.
