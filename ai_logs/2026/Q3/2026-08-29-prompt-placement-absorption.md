# Prompt Placement — absorption into Adapters and Bindings — 2026-08-29

## Objective

Continue #787 from exact `main` `0fc01857ee543cf4f54b665993469b4a36a7e45d` by testing whether `PROMPT_PLACEMENT.md` still owns enough distinct responsibility to remain an active-support document.

## Observed need

Repository search on the exact base found no current consumer of `PROMPT_PLACEMENT.md` outside historical `ai_logs/`, and no authority-index row for the file.

Its durable rule is a specialization of `ADAPTERS_AND_BINDINGS.md`:

```text
canonical Pantheon doctrine / blueprint
-> minimum layer-specific prompt instruction
-> runnable prompt configuration remains with the external adapter/runtime layer
```

The prior satellite repeated layer boundaries already owned by `HERMES_INTEGRATION.md`, Cockpit owners, Evidence, memory and runtime adapters.

## Overlap analysis

`ADAPTERS_AND_BINDINGS.md` already owns:

- blueprint in Pantheon versus runnable configuration outside;
- dependency direction from adapter to Pantheon contracts;
- conformance rather than doctrine duplication;
- tool/version-specific adaptation outside the kernel.

Prompt placement is therefore a configuration specialization, not an independent authority responsibility.

## Changes

The useful prompt-specific delta is absorbed as a new `Prompt distillation and placement` section in `ADAPTERS_AND_BINDINGS.md`:

- distill only the minimum instruction needed by each layer;
- a prompt never gains more authority than its host layer;
- doctrine, Cockpit projection, runtime-client interaction, Hermes profile/skill, external flow/runtime and observability prompt roles remain distinct;
- minimum prompt blueprint metadata is retained;
- mega-prompt and self-authorizing prompt anti-patterns remain rejected.

`docs/governance/PROMPT_PLACEMENT.md` is then removed.

## Affected consumers

No current non-historical consumer required retargeting on the exact base. Git history and ai_logs preserve the former satellite and its rationale.

## Quantitative convergence

Before this ai_log:

```text
ADAPTERS_AND_BINDINGS.md   +59 / -0
PROMPT_PLACEMENT.md        +0 / -257
```

Net doctrine reduction: **198 lines and one active-support file**.

## Migration and rollback

No runtime or data migration. Rollback is restoring the satellite from Git history and removing the absorbed section if a future independent responsibility is demonstrated.

## Authority impact

Authority is reduced, not expanded: one unindexed active-support satellite disappears. `ADAPTERS_AND_BINDINGS.md` remains the already-indexed owner for blueprint/adapter placement; `HERMES_INTEGRATION.md` remains the runtime/client/PDP/PEP/Cockpit boundary owner.

## Runtime impact

None. No prompt registry, router, runtime prompt, client function, Hermes skill, flow, provider, observability service or executable configuration is created.

## Preserved invariants

```text
prompt placement != authority transfer
projection instruction != approval
runtime-client prompt != governance source of truth
Hermes prompt != Pantheon Role authority
runtime checkpoint != memory
trace metadata != Evidence
blueprint != runnable adapter
```

## Verification rule

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD, internal-reference checks pass after deletion, and reviews/threads/comments have been read. Any later HEAD modification invalidates earlier check evidence.
