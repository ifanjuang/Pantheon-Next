# Architecture

Status: active doctrine — independently maintained in Pantheon Next — implemented as documentation.
Boundary profile: documentation_only.

Historical provenance is preserved in git history; current architecture follows observed owners and executable boundaries rather than historical product choices.

## Doctrine

```text
Hermes client surfaces handle runtime interaction.
Pantheon Cockpit exposes governed projections.
Hermes Agent executes externally.
Pantheon Next governs consequential status.
The human decides.
```

Pantheon Next is governance-first. It defines authority, contracts, Evidence expectations, approvals, allowed transitions, memory/Register rules and integration boundaries. It must remain simpler than the runtimes and clients it governs.

## Layered anatomy

```text
Hermes clients
  official Hermes Web/dashboard baseline
  optional compatible mobile/PWA clients
  chat, sessions, runtime controls and attachments

Pantheon Cockpit
  governed projections
  project/navigation composition
  Cards, status, decision and review surfaces
  not a second general-purpose chat frontend

Obsidian workspace
  human-authored Markdown
  working notes and editable projections
  source/workspace organization

Pantheon Next
  governance source of truth
  Task Contracts and Context Packs
  Evidence and approval rules
  governed identities and relations
  capability placement / binding / activation rules
  Knowledge and Registre Probatoire boundaries

Hermes Agent
  external execution runtime
  executable skills and tools
  sessions and provider runtime
  operational/runtime memory
  candidate and observation emission

Optional external adapters
  connectors, extraction tools, memory providers and clients
  selected only through existing governance owners
```

No placement line transfers authority by itself.

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder != governed identity
```

## Runtime boundary

Pantheon Next must not reimplement Hermes subsystems such as the agent loop, prompt assembly, provider resolution, executable tool registry, terminal, browser, web actions, scheduler, gateways, session storage or optional runtime skills.

Hermes may execute bounded work after the applicable contract, policy and approval path. A successful run returns candidates and observations; it does not approve itself or canonize Evidence or memory.

Reference: `HERMES_INTEGRATION.md`.

## Client boundary

The user-facing runtime client is not a Pantheon authority.

The official Hermes Web/dashboard surface is the current baseline for Hermes interaction. Compatible clients may be selected as replaceable adapters. A mobile PWA can be useful when it talks directly to supported Hermes dashboard contracts and preserves authentication/network boundaries, but client compatibility does not make it a Pantheon dependency.

Pantheon does not require OpenWebUI. The former OpenWebUI integration path is superseded and must not remain an architectural owner.

The Pantheon Cockpit remains distinct because its responsibility is governed projection, not generic conversation/runtime control.

Reference: `PANTHEON_COCKPIT_STRUCTURED_AGENCY_INTERFACE.md`.

## Workspace and knowledge boundary

Obsidian is the current human workspace direction for Markdown notes and editable knowledge/work projections. It does not become the authority for professional source identity, Evidence, governed Project identity or Registre Probatoire memory.

Hindsight may provide derived associative recall when selected. Recall remains memory, not truth or Evidence.

Professional source files keep their own source/provenance owners. A local/NAS ingestion path may preserve exact source identity without requiring a separate DMS product.

Paperless is therefore not a required architecture component. The former Paperless candidate path is superseded; its useful source/version/provenance invariants remain owned by the tool-agnostic document lifecycle and source contracts.

Reference: `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` and the document lifecycle owners.

## Task Contracts

Reference: `TASK_CONTRACTS.md`.

A Task Contract bounds a task by declaring purpose, scope, allowed/forbidden capabilities, outputs, approval ceiling, memory impact and Evidence expectations.

```text
Task Contract != runtime task
contract valid != effect authorized
runtime success != approval
```

## Evidence and approval

References: `EVIDENCE_PACK.md`, `APPROVALS.md`, `USER_DECISION_GATE.md`.

Consequential results must remain reviewable. Evidence Packs expose relevant sources, assumptions, actions, limitations and outputs. Approval remains a distinct governed decision.

No interface click, runtime completion, health check or model agreement is approval by implication.

## Memory and Register

Reference: `MEMORY.md`.

Runtime memory, workspace notes, Knowledge and the Registre Probatoire remain distinct.

```text
workspace note != governed memory
Hermes memory != Registre Probatoire entry
Hindsight recall != truth
repeated retrieval != promotion
```

Durable governed assertions use the existing Register Candidate and promotion path.

## Capabilities and external tools

References: `CAPABILITY_PLACEMENT.md`, `UNIFORM_CAPABILITY_GOVERNANCE.md`, `ADAPTERS_AND_BINDINGS.md`, `EXTERNAL_TOOLS_POLICY.md`.

Before adding or selecting a runtime, client, connector, skill or tool:

1. verify whether an existing owner/capability already covers the need;
2. classify the abstract Capability Slot;
3. evaluate the concrete binding/client separately;
4. preserve installation, health, activation and task authorization as distinct states;
5. keep the binding replaceable.

Pantheon must not create a parallel registry, installer, provider router or plugin marketplace merely to manage an optional external product.

## Domain packages and methods

Domain Packs, Roles, Rites and Workflow Manifests are governance content. They may constrain or frame external work but do not execute it.

A professional result remains subject to the applicable human/professional review even when schemas, tests or runtime checks pass.

## Current convergence decision

The target composition is intentionally smaller than the historical stack:

```text
Hermes Web/dashboard
  current general runtime interaction baseline

compatible Hermes mobile/PWA client
  optional replaceable client when selected and verified

Pantheon Cockpit
  governed projections only

Obsidian
  human Markdown workspace / knowledge-working surface

Hindsight / Hermes memory
  optional derived/runtime recall under separate boundaries

Pantheon Next
  governance and consequential status
```

OpenWebUI and Paperless are not target architecture components. Historical code and documents may remain temporarily only while incoming references, compatibility surfaces and protected implementation paths are retired safely.

## Final rule

Pantheon Next governs what matters without owning what it does not need to own.

```text
reuse existing owners
keep clients replaceable
keep sources distinct from projections
keep memory distinct from Evidence
keep execution distinct from authorization
remove superseded architecture instead of maintaining parallel paths
```
