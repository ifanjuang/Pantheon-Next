# Architecture convergence plan — governance record

Date: 2026-08-02

Status: working reconciliation record — non-authoritative, non-runtime, to be closed when the convergence program is complete.

## Purpose

Record the governed constraints for the coordinated architecture cleanup of `Pantheon-Next` and `pantheon-mvp` before implementation changes begin.

The detailed executable sequence belongs to `pantheon-mvp`:

```text
docs/architecture/ARCHITECTURE_CONVERGENCE_EXECUTION_PLAN.md
```

This log does not replace `ROADMAP.md`, `AUTHORITY_INDEX.md`, `MODULES.md`, `WHAT_RUNS.md` or `PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json`.

## Current facts

- the cross-repository audit and ownership registry are merged;
- the calibrated audit found no demonstrated P0 authority conflict;
- active debt remains around generation-named identities, internal `/v1` routes, one governance document located in `pantheon-mvp`, and modules whose consumers are not yet proven;
- `pantheon-mvp#163` currently mounts new contradictory-review routes under `/v1` and must remain draft until those routes are aligned with the stable naming rule;
- the contradictory-review doctrine and first implementation slices are merged, so the architecture audit must be rerun before the first cleanup PR.

## Ownership boundary

```text
Pantheon-Next
-> semantic ownership, doctrine, governed states, schemas, gates and non-equivalence rules

pantheon-mvp
-> persistence, APIs, bounded application services, projections and replaceable adapters

Hermes / external runtime
-> execution, tools, provider routing and runtime-local state

Cockpit / OpenWebUI
-> interaction, display and decision surfaces

Human
-> consequential decision
```

The convergence program must preserve:

```text
semantic owner != implementation owner
implementation owner != runtime owner
projection owner != authorization authority
installed != approved
healthy != safe
runtime_success != Evidence
retrieved != truth
binding_selected != dependency_adopted
activated != task_authorized
UI status != authorization
```

## Modularity objective

The refactor must make new governed rules easier to integrate without creating a dynamic plugin manager or a new runtime.

A new rule should follow one bounded path:

```text
governed definition in Pantheon-Next
-> vendored or referenced contract in pantheon-mvp
-> pure deterministic evaluator
-> explicit static registration at application startup
-> typed result or Observation
-> optional Cockpit projection
```

A rule addition must not require changes to unrelated domains, broad conditionals in a central service, direct Cockpit authority, runtime dispatch logic or a second semantic definition.

The implementation may use registries and composition roots, but these remain static, reviewable application wiring:

```text
registry != plugin manager
handler selected != dependency adopted
rule evaluated != action authorized
```

## Extension categories

Every future addition must be classified before coding:

1. **Governed rule** — semantics and statuses owned by `Pantheon-Next`.
2. **Application behavior** — deterministic orchestration owned by `pantheon-mvp`.
3. **Adapter or binding** — replaceable external integration owned by `pantheon-mvp`, execution outside Pantheon.
4. **Projection** — Cockpit/OpenWebUI representation without semantic authority.
5. **Runtime capability** — belongs to Hermes or another selected external runtime.

A proposed addition that does not fit one category must be reconciled against existing Context, Trace, Knowledge, Evidence, Claim, ChangeCandidate, Competence, Governed Resource and Observation concepts before a new permanent concept is introduced.

## Required sequence

```text
A. rerun the audit on current main branches
B. freeze new generation names and versioned internal routes
C. remove passive generation-named paths and identities
D. move misplaced governance material
E. migrate internal routes domain by domain
F. prove consumers before deleting modules
G. consolidate shared primitives
H. establish modular domain boundaries and composition roots
I. consolidate Hermes admission, launch, context and return seams
J. normalize runtime observations
K. optimize PostgreSQL, API and Cockpit projections from measurements
L. close the baseline and remove temporary compatibility guards
```

## Change discipline

Each implementation PR must:

- have one architectural responsibility;
- identify the canonical semantic owner;
- state the active consumers being migrated;
- include an audit before/after result;
- avoid permanent compatibility aliases;
- preserve a one-commit or one-PR rollback path;
- avoid hidden changes to Evidence, approvals, scope or task authorization;
- reduce or leave unchanged the number of active architectural paths.

## Exit criteria

The convergence program is complete only when:

- no active module, route, schema identity, projection or folder is named by a product generation;
- internal routes use stable responsibility-based paths;
- every governed concept has one semantic owner and one canonical implementation path;
- every retained adapter is replaceable and explicitly bounded;
- no suspected dead module remains unclassified;
- adding one rule requires only its definition, evaluator, registration, tests and optional projection;
- the calibrated cross-repository audit has no unreviewed P0, P1 or P2 finding;
- temporary baselines and this working reconciliation record are closed or removed according to repository cleanup practice.

## Non-goals

This program does not add:

- a microservice architecture;
- a dynamic plugin system;
- a workflow engine;
- a scheduler or queue;
- a provider router;
- a memory engine;
- automatic approval;
- automatic Evidence promotion;
- a new ontology layer.

The intended result is a smaller, clearer modular monolith with governed contracts and replaceable external bindings.