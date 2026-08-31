# 2026-08-31 — consequential-mutation inventory and protocol-level read-only declaration

## Objective

Make two properties that Pantheon only asserts in prose verifiable by a check, without wiring, activating or authorizing anything.

The two properties are the same shape: a boundary that this repository genuinely respects, that no mechanism can currently detect losing.

## Exact repository state

```text
base = 07b28ce4f56469f2824d0e250f3d100c78090fff
```

## Finding that motivated the work

`CLAUDE.md` states the chokepoint invariant in the present tense:

```text
A consequential effect still routes through the governance check (the
chokepoint). No module or implementation path bypasses it.
```

Reading the code, the invariant does not hold as written:

- `policy_gate.enforce_consequential` has two non-test call sites,
  `knowledge_update.py:294` and `capability_manager.py:155`, both behind an
  optional `policy_client` parameter defaulting to `None`;
- `policy_client=` has no non-test caller anywhere in `implementation/`;
- `PolicyClient` is a `Protocol`; its only concrete non-test implementation,
  `HttpPolicyClient`, is never instantiated outside tests, and no environment
  variable or factory can enable it;
- `cockpit_shell.py:407` exposes the consequential Knowledge write over HTTP
  and calls `apply_knowledge_update` without the parameter;
- `test_no_policy_client_keeps_the_original_behavior()` codifies the omission
  as supported behavior.

Eight public mutation entry points exist under `mvp_vertical`, each defended by
its own local checks, no two sharing a guard.

Existing tooling could not see this. `audit_module_usage.py` reports 431
modules, 0 unreferenced, and `policy_gate` as reachable — correctly, because the
import edge exists. What does not exist is the argument that triggers the call.

```text
import edge != call path
module reachable != gate invoked
```

## What this change does and does not do

It does **not** wire the chokepoint. Wiring `HttpPolicyClient` into the
application factory changes runtime behavior and depends on a deployment
decision about the PDP; it is deliberately left out of this change.

It makes the surface enumerable and the current state declared.

## Existing owners reused

No new governance document and no new executable component were created.

- `policy_gate.py` remains the gate owner. It is unchanged.
- `WHAT_RUNS.md` remains the runtime-status honesty owner. One row was added
  for the internal consequential-write path, using its existing vocabulary.
  The pre-existing `Hermes policy/PEP integration` row was kept: it correctly
  describes the external round-trip and was never wrong, only incomplete —
  it located the gap on the Hermes side, while the internal Cockpit write path
  has the same gap.
- `mcp-server/pantheon_mcp/server.py` remains the MCP surface owner.

## Changes

### 1. Consequential-mutation inventory (validation artifact)

`implementation/tests/test_consequential_mutation_inventory.py` enumerates every
public `apply_* / admit_* / promote_* / approve_* / commit_*` function under
`mvp_vertical` by AST and requires each to be declared with the guard regime it
actually performs. `gate: "none"` is a permitted, honest answer; silence is not.

A `local_guards` field records what genuinely protects each path, so an ungated
entry point is never read as an unprotected one.

One test fails closed if an entry point ever claims
`gate="enforce_consequential"` while `HttpPolicyClient` has no non-test
instantiation — the claim would describe a call that cannot happen. That test is
the deliberate revisit point when the client is wired.

The guard was verified to bite: adding a ninth entry point without declaring it
fails the suite, and the failure names it.

### 2. Protocol-level read-only declaration

All 23 MCP tools were registered with bare `@mcp.tool()` and carried
`annotations: None`. The package's central property — read-only and
side-effect-free — was asserted in docstrings and verified by 226 tests, and
invisible to any client reading the tool list.

The tools now register through `_read_only_tool()`, carrying
`read_only_hint=True`, `destructive_hint=False`, `idempotent_hint=True`,
`open_world_hint=False`. `mcp-server/tests/test_tool_annotations.py` fails
closed when a tool is registered without annotations, so the declaration cannot
drift from the surface.

No tool behavior changed. An annotation is a declaration, not an enforcement.

### 3. Two monorepo-migration residues

Both are the same root cause: text or paths that were correct in the standalone
`pantheon-mvp` repository and stopped being correct after co-location.

- `test_cockpit_composed.py::test_console_entrypoint_targets_composed_cockpit`
  read `Path("pyproject.toml")` relative to the working directory. It passed
  from `implementation/` and failed from the monorepo root, where it read the
  governance `pyproject.toml`. CI did not see it because
  `implementation-ci.yml` sets `working-directory: implementation`. Now
  resolved from `__file__`, as `test_external_qualification_pins.py` already does.

- `check_internal_links.py` failed on `main`: `CAPABILITY_REGISTRY.md:74`
  contained the English phrase "Runtime implementation/release provenance",
  which the checker reads as a path reference now that `implementation/` is a
  real directory. Reworded to "Runtime implementation and release provenance".
  The phrase was verified not to be asserted by any test before editing.
  This was a blocking failure in `governance-ci.yml` line 91, pre-existing on
  `main` and not introduced here.

## Validation

```text
tests/                  554 passed
mcp-server/tests        229 passed  (226 + 3 new)
implementation/tests   1220 passed, 352 skipped (no PostgreSQL locally)
.github/scripts         23/23 checks OK, including check_internal_links
```

Before this change the implementation suite reported one failure from the
monorepo root and `check_internal_links` failed on `main`.

## Boundary

```text
inventory declared != chokepoint wired
annotation declared != effect prevented
gate implemented != gate invoked
0 unreferenced modules != 0 dead call paths
check green != adoption
documented gap != authorized gap
```

## Next admissible step

Wiring `HttpPolicyClient` in the application factory is the next step, and it is
a human decision because it changes runtime behavior and presumes a reachable
PDP. The order that matters:

1. an assembly test requiring a policy client on every consequential route —
   `test_cockpit_shell.py` and `test_cockpit_composed.py` currently contain no
   occurrence of `policy`, so the factory can be changed in either direction
   without any test reacting;
2. then the wiring;
3. then update the inventory's `gate` fields and the `WHAT_RUNS.md` row.

Wiring before step 1 would leave the same silent-regression hole that produced
the present state.
