# Pantheon graph model intervention

Date: 2026-07-11

Status: validation-only intervention trace.

## Request

Formalize the candidate graph model discussed for Pantheon Next: typed governance objects, governed relations, relation lifecycle, cardinalities, invariants and cockpit projections.

## Repository read before change

Reviewed the active repository spine before writing:

- `README.md`
- `docs/governance/STATUS.md`
- `docs/governance/WHAT_RUNS.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MODULES.md`
- `CONTRIBUTING.md`
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`
- `docs/governance/CAPABILITY_REGISTRY.md`

## Change

Created:

- `docs/governance/PANTHEON_GRAPH_MODEL.md`

Indexed it in:

- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`

The document is explicitly `candidate support doctrine — documented non-implemented`.

It defines:

- candidate node classes without requiring one implementation type per class;
- governed relation records;
- controlled relation types;
- an independent relation lifecycle;
- scope and cardinality rules;
- ten governance invariants;
- role, cockpit, constellation and Capability Slot projections;
- bounded treatment of coverage and confidence;
- storage neutrality and a staged adoption sequence.

## Boundary

The change adds documentation only.

```text
exposed_by  -> future exposure surface projection only
executed_by -> external runtime, if separately configured and authorized
governed_by -> Pantheon relation, evidence, status, scope and approval rules
approved_by -> human authority for consequential adoption or activation
forbidden   -> graph runtime, workflow engine, scheduler, queue, router, approval engine, memory engine, installer, updater or automatic action
```

No protected path was modified.

No schema, test, MCP surface, runtime, database, UI, adapter or executable skill was created.

## Classification

```text
implemented:                 Markdown candidate document and authority-index row on the branch
documented non-implemented: graph registry, storage, API, validators and cockpit projections
partial / to verify:         alignment with Capability Registry and register-link candidates
to verify:                   review and potential future promotion path
not applicable:              runtime health
```

## Indexing result

The candidate document now has an explicit row in the registered governance authority sub-index. This provides repository visibility only and does not promote the document beyond candidate support doctrine.

## Result

The model preserves the active boundary:

```text
The graph governs relations.
It does not become the engine.
The human decides.
```
