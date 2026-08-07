# External runtime memory sandbox priority

Date: 2026-08-07
Repository: `ifanjuang/Pantheon-Next`
Branch: `docs/hindsight-memory-priority`
Base observed: `a15f5c418560f292df1b915572b21a04fc9fdf23`

Status: binding-registry qualification only — documented non-implemented.

## Objective

Record the reviewed sandbox preference order for the existing
`external_runtime_memory` Capability Slot without selecting a Pantheon runtime
memory backend, adding a dependency or weakening the governed-runtime boundary.

## Repository state reviewed

The existing owners already cover the responsibility:

```text
docs/governance/HERMES_CAPABILITY_BINDINGS.md
docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md
docs/governance/MEMORY.md
docs/governance/HERMES_RUNTIME_SURFACE_REVIEW.md
tests/test_hermes_ecosystem_adaptability.py
```

No new memory concept, schema or adapter family is required.

Open PRs #579 and #580 were checked before the change. They do not modify the
memory binding registry or its ecosystem test, so this work remains isolated
from the parallel Project Anatomy / Revit documentation work.

## External state reviewed

The Hindsight review covered its current repository, documentation, Hermes
integration, cookbook, integrations and best-practice guidance.

Relevant verified Hermes state:

```text
NousResearch/hermes-agent
release: 0.20.0
release commit: 3c27eb6234bf91b8ceee9e9071591b31e9b148cb
```

The reviewed Hermes 0.20.0 tree contains a bundled Hindsight memory provider and
allows only one external memory provider to be active at a time.

The reviewed Hindsight server package identifies version `0.8.6` and remains an
external memory engine with its own persistence, retrieval, graph/consolidation
and operational lifecycle.

These observations establish availability and integration maturity. They do not
establish installation, safety, production adoption or authority.

## Decision

For `assistant-personal` sandbox evaluation, the preference order is:

```text
1. Hindsight
2. Mnemosyne
3. Mem0
```

Interpretation:

```text
Hindsight
-> first sandbox candidate.

Mnemosyne
-> second candidate and local-first fallback.

Mem0
-> third comparison candidate.
```

The Capability Slot itself remains:

```text
preferred_binding: unbound
```

because this is a profile-specific sandbox priority, not a Pantheon binding
selection.

## Preserved boundary

```text
pantheon-governed
-> external memory remains forbidden/off.

assistant-personal
-> at most one optional external provider may be evaluated.
```

No recalled memory becomes Evidence, approval, project truth, scope expansion or
an automatic project mutation.

```text
memory recalled != truth
memory observation != Evidence
provider selected != memory admitted
binding preference != dependency adoption
installed != approved
runtime success != Evidence
```

## Files changed

```text
docs/governance/HERMES_CAPABILITY_BINDINGS.md
  -> records Hindsight > Mnemosyne > Mem0 sandbox order while keeping the slot unbound.

tests/test_hermes_ecosystem_adaptability.py
  -> locks the ordering and the unbound / pantheon-governed exclusion invariants.

ai_logs/2026/Q3/2026-08-07-external-runtime-memory-sandbox-priority.md
  -> records this qualification decision.
```

## Not changed

```text
no Hermes configuration
no Hindsight installation
no Mnemosyne installation
no Mem0 installation
no Docker or Compose
no dependency lock
no Pantheon schema
no pantheon-mvp runtime
no PostgreSQL migration
no memory data
no automatic recall
no automatic retain
no Capability Slot activation
no Evidence admission
no approval path
```

## Verification criteria

The change is complete when:

```text
Hindsight is visibly first in the sandbox order.
Mnemosyne is second.
Mem0 is third.
preferred_binding remains unbound.
pantheon-governed remains forbidden.
the ecosystem regression test locks these distinctions.
repository CI passes on the branch.
```

No provider should be installed or activated by this documentation change.
