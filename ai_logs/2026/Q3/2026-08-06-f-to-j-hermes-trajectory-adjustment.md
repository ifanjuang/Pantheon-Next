# F-to-J Hermes trajectory adjustment

Date: 2026-08-06
Status: documented candidate roadmap adjustment

## Request

Review whether the active F-to-J development trajectory must change after a complete reading of the current Hermes documentation and the latest Pantheon convergence work.

## Repository observations

The review found that the execution spine needed to prevent incompatible F-to-I runtime contracts already exists:

- `docs/governance/HERMES_EXECUTION_ADMISSION_BRIDGE.md` defines bounded execution admission, exact WorkIssue and Context Pack binding, separate effect authorization, scoped runtime reads and normalized candidate return;
- `docs/governance/HERMES_RUN_LAUNCH_JUNCTION.md` specializes the bridge for the Hermes Runs API without turning Pantheon into a dispatcher;
- `catalog/schemas/execution-result-candidate.schema.json` defines a candidate-result envelope whose governance fields state that runtime success is not Evidence and human review remains required;
- recent Source, Information, EntityRef relation, WorkIssue scope and DecisionRequest/Decision convergence provides the required business-side boundaries.

Therefore a new `ExecutionRequest` abstraction or intermediate F-to-J execution tranche would duplicate existing responsibility.

## Decision

Keep the F-to-J order and tighten its boundaries:

```text
F  ProjectClaims remain governed consequential values;
   Hermes output remains candidate material.

G  variants reuse the existing candidate-result spine;
   no universal InformationBranch is created without demonstrated need.

H  Hermes may produce Anatomy candidates only;
   APU authority is changed only through governed review and application.

I  Pantheon owns Capability identity, implementation candidates, releases,
   runtime bindings, admission, scope activation and observed compatibility;
   Hermes keeps native Skill, plugin, MCP, profile, provider, sandbox,
   session and automation mechanics.

J  remains the final adapter and end-to-end consolidation tranche,
   while real-project validation begins after F, G, H and I rather than waiting.
```

## Key correction to the preliminary analysis

The preliminary discussion proposed a small runtime-neutral execution contract before I. Repository inspection showed that this would be a duplicate unless a concrete uncovered responsibility is demonstrated.

The accepted rule is therefore:

```text
reuse existing execution admission, launch and candidate-result contracts first
extend them when the responsibility is the same
generalize only for demonstrated multi-runtime need
create a new concept only for a genuinely distinct responsibility
```

## Artifact

Added:

- `docs/roadmaps/F_TO_J_HERMES_TRAJECTORY_ADJUSTMENT.md`

## Runtime impact

None.

No schema, migration, API, adapter, Cockpit projection, Hermes configuration, capability admission, execution launch, Project mutation or Evidence admission is changed by this documentation tranche.
