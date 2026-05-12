# Repository Simplification Plan

Status: implemented — phase 1 simplification doctrine.

## Objective

Simplify Pantheon Next without removing governance.

The objective is to reduce ambiguity between:

- governance;
- execution;
- visualization;
- legacy;
- experimental tooling.

Pantheon Next must remain governance-first.

## Core doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Non goals

Pantheon Next must not become:

- an autonomous execution runtime;
- an agent runtime;
- a tool runtime;
- a provider router;
- a scheduler;
- a queue system;
- a message bus;
- a central LangGraph runtime;
- an automatic skill installer;
- an automatic Hermes profile installer;
- a self-modifying memory system;
- a hidden workflow engine.

## Simplification strategy

### Keep canonical governance centralized

Canonical governance remains under:

```text
docs/governance/
```

`docs/governance/AGENTS.md` remains the canonical Pantheon Role registry.

Hermes profiles must reference governance.

Hermes profiles must not duplicate canonical role doctrine.

## Hermes profile strategy

Hermes profiles remain lightweight:

```text
hermes/profiles/<profile>/
  README.md
  profile.yaml
  soul.md
```

No additional per-profile files are required in phase 1.

Avoid:

- `governance.md` per profile;
- local approval systems;
- local memory canonization;
- embedded orchestration logic.

## Documentation strategy

### Allowed

- governance indexes;
- glossaries;
- migration stubs;
- simplification plans;
- read-only specifications;
- schema references.

### Forbidden in phase 1

- moving governance files into deep subfolders;
- large-scale renaming;
- deleting governance documents before reference verification;
- merging multiple governance concepts into one mega-document.

## Migration policy

Pantheon-OS remains the historical source repository.

Pantheon-Next migrates selectively.

Allowed migrations:

- governance Markdown;
- schemas;
- schema examples;
- governance tests;
- read-only validators;
- AI logs;
- integration specifications.

Forbidden migrations:

- hidden runtimes;
- execution backends;
- automatic orchestration systems;
- autonomous memory promotion;
- implicit workflow engines.

## Stub policy

Missing governance files may temporarily exist as explicit stubs.

Every stub must clearly state:

```text
Status: stub — Non implémenté — à migrer depuis Pantheon-OS
```

A stub is not canonical governance content.

## Runtime boundary

Pantheon Next governs.

Hermes executes.

OpenWebUI exposes.

No repository simplification effort may violate this separation.

## Phase 1 target state

```text
Pantheon-Next/
  docs/governance/
  hermes/profiles/
  schemas/
  operations/
  tests/
  ai_logs/
```

Minimal.
Readable.
Governed.
No hidden runtime.
