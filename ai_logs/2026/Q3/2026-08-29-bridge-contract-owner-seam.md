# Bridge Contract — owner-seam convergence — 2026-08-29

## Objective

Continue #787 from exact `main` `149fcad93c6805fd7e3925fd79b72b1ad1a8489a` by separating the bridge-specific adapter responsibility from generic Hermes/PDP/PEP/Evidence/approval/memory doctrine.

## Repository observations

- `HERMES_INTEGRATION.md` is the indexed owner of the stable runtime/client/PDP/PEP/Cockpit boundary.
- `ADAPTERS_AND_BINDINGS.md` owns the generic blueprint-in-Pantheon / runnable-adapter-outside dependency rule.
- `HERMES_INTEGRATION_MODELS_RECONCILIATION.md` is separately indexed and owns the distinction between run-scoped Execution Admission and per-effect chokepoint authorization.
- `REFERENCE_BOUNDARIES.md` and `EXECUTION_MINIMALISM.md` were audited but are not Hermes bridge owners: they own reference-distillation boundary and reliability/minimalism respectively.
- `BRIDGE_CONTRACT.md` declared active support doctrine but had no row in either `GOVERNANCE_AUTHORITY_INDEX.md` or `RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`.

## Observed overlap

The previous Bridge Contract repeated substantial doctrine already owned by:

- `HERMES_INTEGRATION.md` for client/runtime/PDP/PEP/Cockpit placement;
- `ADAPTERS_AND_BINDINGS.md` for adapter dependency direction;
- `TASK_CONTRACTS.md` for task scope;
- `UNIFORM_CAPABILITY_GOVERNANCE.md` for capability/effect eligibility;
- `EVIDENCE_PACK.md`, `APPROVALS.md`, `USER_DECISION_GATE.md` and `MEMORY.md` for downstream governed objects;
- product/binding owners for Langflow, LangGraph, Langfuse, graph and concrete executor choices.

## Narrowed responsibility

The retained bridge owner now defines only the non-authoritative adapter seam:

```text
structural adapter preflight
refuse malformed adapter input
normalize request for Pantheon policy consultation
convey PDP disposition without widening it
handoff to an already admissible executor/binding
normalize runtime return into existing candidate families
bridge-specific adapter status vocabulary
fail conservatively when translation cannot preserve the boundary
dependency direction: Pantheon contracts -> bridge -> external runtime/binding
```

It explicitly does not own generic Evidence, approval, memory, Task Contract or client/Cockpit doctrine.

## Owner test

After removing repeated rules, enough distinct normative responsibility remains to justify an independent specialization.

The bridge seam is not the same responsibility as:

```text
HERMES_INTEGRATION = who governs / enforces / executes
ADAPTERS_AND_BINDINGS = where tool-specific runnable configuration lives
BRIDGE_CONTRACT = how a future translation adapter may convey governed contracts without widening authority
```

Absorbing the bridge seam into `HERMES_INTEGRATION.md` would regrow the stable integration owner with a speculative adapter protocol, contrary to the current convergence goal.

## Authority correction

The slice adds one row to `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`:

```text
BRIDGE_CONTRACT.md
active support doctrine
documented non-implemented
specialized non-authoritative adapter seam
```

This records the document's declared class; it does not promote a bridge implementation or adoption.

## Quantitative convergence

Before this ai_log:

```text
BRIDGE_CONTRACT.md                    +120 / -162
RUNTIME_ADAPTERS_AUTHORITY_INDEX.md   +1 / -0
```

Net doctrine reduction: 42 lines plus removal of multi-owned responsibility.

The reduction is below the repository net-truncation threshold; no truncation acknowledgement is required.

## Authority impact

No new authority class. The Bridge remains documentation-only and non-authoritative. Pantheon policy service remains PDP; the external runtime/PEP enforces consequential effects; the bridge may only adapt and convey.

## Runtime impact

None. No bridge API, endpoint, scheduler, queue, provider router, runtime, PDP, PEP or product adapter is implemented.

## Preserved invariants

```text
bridge structural preflight != policy decision
bridge handoff != authority transfer
bridge return != Evidence admission
bridge success != authorization
PDP decision != PEP execution
runtime success != authorization
projection != approval
provider selected != authority transfer
```

## Verification rule

The PR must pass Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on its exact final HEAD. The final patch, reviews, threads and comments must be read before merge. Any later HEAD modification invalidates earlier evidence.
