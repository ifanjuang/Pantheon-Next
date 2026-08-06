# Revit / Pantheon local integration contract documentation

Date: 2026-08-06
Status: documentation-only convergence record.

## Objective

Document the Revit-to-Pantheon connection in detail before implementation planning.

The pass records:

```text
responsibility boundaries
full-local operation
first-wave métier scope
component topology
capability declaration
local exposure controls
contract stack
read and write flows
context snapshot
preflight
single-use authorization
technical action report
Project Anatomy correlation
refusal and non-equivalence rules
```

It deliberately does not define implementation order, dates, milestones or repository allocation beyond the already established production-code boundary.

## State observed before the change

`docs/governance/REVIT_LOCAL_ADAPTER.md` already owned the canonical local-adapter boundary.

The repository also contained:

```text
revit-plugin/README.md
revit-plugin/docs/ARCHITECTURE.md
revit-plugin/docs/EXECUTION_MODEL.md
revit-plugin/docs/CONTEXT_PACK_CONTRACT.md
revit-plugin/docs/ACTION_LOG_CONTRACT.md
```

Those supporting files were intentionally non-executable but remained too thin to carry the interface decisions reached in the design discussion.

The open draft PR #557 concerns Project Anatomy implementation convergence. This documentation pass remains separate and does not absorb that trajectory.

## Decisions recorded

### Independence

```text
Autodesk Assistant not required
Autodesk Public MCP not required
APS not required
Internet not required for the core path
```

### Initial métier scope

```text
architecture
economy and quantities
construction site
RE2020 input preparation and consistency
ACV and carbon
```

Structure and technical networks remain observable context rather than first-wave design responsibilities.

### Components

```text
Pantheon Next
-> governance and contracts

pantheon-mvp
-> persistence, APIs, authorizations and projections

Hermes
-> métier reasoning and workflow composition

Host Agent
-> transport adapter only

Revit add-in
-> Revit API execution only

Cockpit
-> review and decision surface

human
-> consequential decisions
```

### Local exposure

The Revit menu sets a local exposure ceiling.

```text
locally_enabled != task_authorized
```

### Capability identity

Abstract Pantheon capabilities use `building_model.*` identities.

Binding-specific commands use `revit.*.vN` operation identifiers.

### Contract stack

The documented stack reuses existing Pantheon concepts and adds only Revit-specific technical envelopes inside subordinate implementation notes.

### Project Anatomy

The Revit snapshot and APU write paths remain separate from Revit model mutation.

```text
APU mapping applied != Revit model modified
Revit model modified != APU mapping accepted
```

## Files changed

```text
docs/governance/REVIT_LOCAL_ADAPTER.md
revit-plugin/README.md
revit-plugin/docs/ARCHITECTURE.md
revit-plugin/docs/EXECUTION_MODEL.md
revit-plugin/docs/CONTEXT_PACK_CONTRACT.md
revit-plugin/docs/ACTION_LOG_CONTRACT.md
```

## Impact

Documentation only.

No schema, runtime, add-in, Host Agent, endpoint, migration, workflow, installer, capability activation, task authorization, Revit transaction, Project Anatomy write or Evidence admission is implemented.

## Merge gate

The documentation was moved from draft review to active review before merge.

The repository requires its protected status checks to be attached to the current pull-request revision. A final journal clarification was therefore committed through the normal branch path so GitHub could emit a `synchronize` event and evaluate the current revision.

```text
documentation_complete != merge_authorized
mergeable != required_checks_satisfied
required_checks_satisfied != architecture_implemented
```

No branch-protection bypass, implementation change or planning decision is introduced by this synchronization commit.

## Closure

The target connection, responsibilities, interface envelopes and refusal rules are documented.

Implementation planning remains intentionally open for a later pass after review of this contract set.
