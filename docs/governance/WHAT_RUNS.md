# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-07-17

This document states what currently runs, what is static documentation, what is partial or to verify, and what is intentionally absent.

It is a status-honesty map. It does not create runtime behavior, approve any tool, install an adapter, authorize external action, create a scheduler, create a queue, create an approval engine or promote memory.

Runtime boundary in this file is expressed as operational fields, not by repeating the doctrine slogan.

```text
exposed_by  -> display or publication surface
executed_by -> runtime or implementation artifact, when one exists
governed_by -> Pantheon boundary and status rule
approved_by -> human approval where consequential
forbidden   -> behavior that must not be inferred
```

## Purpose

Pantheon governs status. Therefore the repository must state its own operational status plainly.

A static prototype is not a live cockpit.
A read-only checker is not an approval engine.
A documented workflow is not an implemented workflow.
A candidate adapter is not an installed capability.
A repository implementation is not proof of host installation.
A demo fixture is not a production data platform.

## Status vocabulary

Use these labels in this file:

```text
runs
implemented in repository
static prototype
static synthetic demo
partial / to verify
implemented read-only / to verify
documented non-implemented
candidate only
voluntarily absent
protected review required
external / outside Pantheon
host-specific / to verify
```

## Runs or exists now

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| Repository documentation | runs | Markdown doctrine, support doctrine, candidates, examples and logs exist in the repo. | Documentation does not implement execution. |
| GitHub Pages landing | runs / static documentation | Public documentation pages are served as static files. | Static publication is not product availability. |
| `docs/index.html` | static documentation | Public-facing landing page. | Must not imply live runtime capabilities beyond status docs. |
| `docs/rag-probatoire.html` | static documentation | Public explanatory page for RAG probatoire. | Demonstrates doctrine, not a running RAG engine. |
| Hermes Modules dashboard plugin | implemented in repository / external adapter | A bounded dashboard plugin and its data projection exist in the repository for Hermes-hosted use. | Hermes hosts and executes it. Repository presence does not prove installation, reachability, health, activation, safety or approval on any host. |
| Shared Pantheon Control renderer | implemented in repository / bounded presentation layer | A shared renderer supports the Hermes dashboard binding and the static demonstration bundle. | Rendering supplied status data is not runtime discovery, governance approval or execution. |
| `docs/assets/pantheon-control/` | static synthetic demo / partial projection | GitHub Pages-compatible Pantheon Control bundle uses synthetic fixtures and the shared renderer, including `DEMO`, `LIVE` and `LIVE_PARTIAL` presentation semantics. | It is not proof of a connected Hermes host and is not a live cockpit, approval engine, memory engine or runtime. |
| `schemas/` | partial / protected review required | Validation artifacts may exist. Exact status must be checked before relying on them. | Schemas validate structure; they do not execute or approve. |
| `tests/` | partial / protected review required | Validation tests exist where present. Exact coverage must be checked before relying on them. | Tests do not promote doctrine by themselves. |
| `mcp-server/` | implemented read-only / partial / protected path | Repository contains a bounded read-only MCP policy / verification surface. PR #239 was reviewed and merged as a protected-path read-only fix. The broader server remains partial/to verify until full-suite status is reconciled. | The surface may return status data only; it must not execute, approve, send, schedule, route providers, install, update or promote memory. |
| `ai_logs/` | runs as trace | Intervention logs exist as validation-only trace. | Logs are not doctrine and do not approve changes. |
| Notion Kanban | external / outside Pantheon | Project tracking exists outside the repo. | Notion is pilotage only; GitHub remains canonical. |

## External or host-specific runtime state

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| Hermes runtime | external / outside Pantheon | Hermes is the execution runtime named by doctrine. | Pantheon does not install, run, update or approve Hermes. |
| Hermes dashboard installation | host-specific / to verify | The repository contains a plugin candidate/implementation, but installation and activation belong to each Hermes host. | Installed ≠ approved; healthy ≠ safe; repository code ≠ live host evidence. |
| OpenWebUI integration | external / host-specific / to verify | OpenWebUI may expose Hermes and Pantheon-governed views when separately configured. | No repository document proves a live OpenWebUI connection on a given host. |
| Pantheon MCP installation inside Hermes | external / host-specific / to verify | The read-only MCP package may be installed and configured in an external Hermes environment. | The repository does not infer installation, transport reachability, activation or authorization from package existence. |

## Documented but not implemented

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| Hermes runtime governance card | candidate only / documented non-implemented | `HERMES_RUNTIME_GOVERNANCE.md` classifies Hermes Agent as an external runtime Capability Slot and cockpit card candidate. | It does not install, configure, activate, update, roll back or run Hermes; it only governs status, gates, evidence expectations and non-equivalence warnings. |
| Hermes installation assistance | candidate only / documented non-implemented | `HERMES_INSTALLATION_ASSISTANCE.md` defines human-facing installation assistance, command-candidate review, redacted output review and read-only check classifications. | It does not install, run commands, store secrets, configure providers, enable tools or gateways, update, roll back, declare safety or approve activation. |
| Install module catalog | candidate only / documented non-implemented | `INSTALL_MODULE_CATALOG.md` defines a candidate grammar for module records, preset records, dependency roles, conflict classes, source trust, provisioning, gates, health, rollback and update policy. | It does not create live `modules.json`, `presets.json`, schemas, tests, registry, installer, plugin marketplace, Docker/Portainer stack, shell runner, provider router, approval engine or memory engine. |
| Complete governed resource dashboard model | partial / documented non-implemented | `GOVERNED_RESOURCE_DASHBOARD_MODEL.md` defines a broader Resource Card and governed-action model. A bounded Hermes Modules vertical slice exists, but the complete model is not implemented. | The vertical slice does not promote the full candidate model or create a Pantheon runtime, installer, scheduler, queue, provider router or approval engine. |
| Pantheon MVP Vertical binding | external executable candidate / observed at pinned SHA / not adopted | `PANTHEON_MVP_VERTICAL_BINDING.md` classifies `ifanjuang/pantheon-mvp` as an external candidate binding. The current bounded review is `reference_reviews/PANTHEON_MVP_VERTICAL_CURRENT_REVIEW.md`, pinned to commit `7c6ad4893cb7300968117cdcfa5418c740c32a18` on 2026-07-13. Block 1 and the Block 2 drafting seam are declared; recent repository history also records decision/register hardening, additional scenarios and duty-of-care work. | Pantheon does not import, install, execute, activate or adopt this binding. External implementation observation is not accepted governance evidence. CI evidence was not established for the exact pinned merge commit through the available query. Real-dossier use, consequential reliance, adoption and activation remain blocked pending current schema/path/decision/register evidence and explicit human approval. |
| Hermes skills from Pantheon | documented non-implemented | Skill governance and templates may exist. | Pantheon does not install or run Hermes skills. |
| Architecture domain pack | candidate only / to verify | Architecture pack and method documents may frame professional method. | Domain pack does not advise, validate, execute, send or remember by itself. |
| Architecture vertical slice | documented non-implemented | A future `architecture_devis_reprise` proof loop is proposed. | No end-to-end slice is implemented by this status file. |
| Data platform | candidate only / to verify | Candidate orientation for records, evidence and approval boundaries. | Data platform must not become ERP, scheduler, queue, runtime, approval engine or memory engine. |
| Capability registry / skill lifecycle | candidate only / to verify | Candidate governance vocabulary may exist. | Capability declaration is not capability authorization. |
| Register integrity review by shadow reconstruction | documented non-implemented / candidate only | `MEMORY.md` defines the non-destructive integrity invariant and `EVIDENCE_MEMORY_DEV_PLAN.md` maps the default-off incremental pass to the existing external Hermes `contradiction_drift_review` operation; full milestone review stays on demand. The external Pantheon Modules plugin implements confirmed controls for one existing finite Hermes job. | The controls do not implement reconstruction. No reconstruction runtime, diff engine, register mutation or automatic discrepancy resolution is implemented here. The external Hermes operation is inactive until bounded operator configuration; consequential changes require human review. |
| Method Cards and Card Stack | candidate only / documented non-implemented | Candidate cockpit/method grammar may exist. | Cards are not agents, runtime state, approvals or memory. |
| Governed form filling | candidate only / to verify | Candidate method for field-as-claim form filling. | No PDF filler, connector, sender or form runtime is implemented by doctrine. |
| Revit Gate | candidate only / documented non-implemented | Developer dossier may describe a future local add-in boundary. | No Revit plugin is implemented by Pantheon unless separately shown in protected artifacts. |
| `revit-plugin/` | documented non-implemented / skeleton only | Future local Revit 2027 adapter prototype folder. | Current repo state is documentation and placeholder material only; future C#/.NET add-in remains to verify. |

## Voluntarily absent

These are not gaps to fill silently.

```text
Pantheon internal execution runtime
hidden agent loop
autonomous approval engine
automatic memory promotion engine
scheduler
queue
provider router
plugin marketplace
automatic external sender
unrestricted connector gateway
ERP
production data platform runtime
```

If any future proposal introduces one of these, it must be classified as a doctrine conflict or an explicitly external adapter/runtime.

## Protected-path status rule

The following paths require explicit approval before modification:

```text
schemas/
tests/
pyproject.toml
operations/
platform/
Docker files
.env files
CLAUDE.md
mcp-server/
GitHub Actions / CI scripts
```

A status mention in this file does not authorize modifying those paths.

## Read before merging branches

Before merging or closing significant branches, read this file with:

```text
docs/governance/README.md
docs/governance/STATUS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
README.md
CONTRIBUTING.md
```

A mergeable PR is not necessarily admissible.
A branch with useful content may still be superseded, overbroad, protected, contradictory or outside Pantheon.

## Current reconciliations

### MCP policy surface

Current position:

```text
mcp-server/ is an implemented read-only verification artifact.
it remains partial / to verify as a whole.
it is not a general runtime or approval surface.
```

Boundary to keep:

```text
The MCP surface may validate structure/status and return status data.
It must not execute, approve, send, schedule, route providers, install, update or promote memory.
```

### Hermes dashboard / Pantheon Control

Current position after the dashboard vertical-slice work:

```text
plugin source exists in the repository
shared renderer exists in the repository
static synthetic demo exists in the repository
host installation and activation remain external and to verify
complete governed resource model remains partial
```

Status implication:

```text
implemented in repository ≠ installed on a host
installed ≠ approved
healthy ≠ safe
DEMO/LIVE/LIVE_PARTIAL are presentation states, not governance conclusions
```

### Pantheon MVP Vertical

Current position after the 2026-07-13 pinned review:

```text
external repository observed at 7c6ad489...
external implementation present in repository
exact CI result not established by the available query
Pantheon binding not adopted
activation not authorized
production use forbidden
```

The next review must inspect current files and tests for schema alignment, path containment, decision-record integrity, retention authorization and vendored upstream freshness. Commit subjects and README claims do not close these gates by themselves.

### Static publication language

`docs/index.html` and Pantheon Control pages must not imply that target behavior is already a live product capability.

Required wording pattern:

```text
static documentation / static synthetic demo / implemented in repository / host-specific to verify
```

## Final rule

```text
Documentation may describe.
Static pages may expose.
Read-only checks may verify structure or status.
External runtimes may execute under contract.
Pantheon governs consequential status.
The human decides.
```
