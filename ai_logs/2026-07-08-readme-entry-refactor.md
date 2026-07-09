# 2026-07-08 — README entry refactor

## Status

Validation-only trace.

This log records a documentation and navigation intervention. It does not create doctrine, runtime behavior, approval, memory promotion, provider routing, scheduling, installation, update execution or external action.

## Scope

The intervention refactored the repository entry layer after the public-facing content in the README was judged too long and too close to the HTML landing page.

Files changed or added:

```text
README.md
README.fr.md
CONTRIBUTING.md
docs/intro-professionnelle.md
docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md
docs/governance/README.md
```

## What changed

- `README.md` was sharpened as a concise GitHub repository entry.
- `README.fr.md` was aligned with the same short structure.
- The long professional explanation was moved into `docs/intro-professionnelle.md` as reference / public explanation.
- `CONTRIBUTING.md` was added as an active-support contribution guardrail.
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` indexed the new root and public-explanation documents.
- `docs/governance/README.md` was updated to include `WHAT_RUNS.md`, `CONTRIBUTING.md`, root README files and the public introduction in the governance read path.

## Why

The root README must act as a repository entry, not a landing page duplicate.

The new structure separates:

```text
README.md / README.fr.md        -> repository entry
CONTRIBUTING.md                 -> contribution guardrail
docs/intro-professionnelle.md   -> public explanatory material
docs/governance/README.md       -> governance read path
docs/governance/* status files  -> status and authority truth
```

This reduces the risk that narrative, diagrams, prototypes or public wording are misread as implementation status.

## Boundary kept

The refactor keeps the active doctrine boundary:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The intervention did not add or authorize:

```text
runtime
agent loop
scheduler
queue
provider router
MCP host
plugin manager
installer
updater
automatic approval
automatic memory promotion
external sender
```

## Risks and limitations

- Markdown links were updated by inspection but no full repository link checker or CI run was executed in this intervention.
- `docs/intro-professionnelle.md` is explanatory reference material and must not be treated as implementation status.
- `CONTRIBUTING.md` is a guardrail. It does not approve protected-path changes by itself.
- The governance index now references root documents, but `AUTHORITY_INDEX.md` remains the authority interpreter.

## Result

The repository now has a cleaner separation between:

```text
public explanation
repository entry
governance read path
contribution discipline
authority/status truth
```

The validated boundary remains:

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```
