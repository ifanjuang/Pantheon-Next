# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-07-22

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
A demo fixture is not a production data platform.

## Status vocabulary

Use these labels in this file:

```text
runs
static prototype
partial / to verify
implemented read-only / to verify
documented non-implemented
candidate only
obsolete / superseded
voluntarily absent
protected review required
external / outside Pantheon
```

## Runs or exists now

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| Repository documentation | runs | Markdown doctrine, support doctrine, candidates, examples and logs exist in the repo. | Documentation does not implement execution. |
| GitHub Pages landing | runs / static documentation | Public documentation pages are served as static files. | Static publication is not product availability. |
| `docs/index.html` | static documentation | Public-facing landing page. | Must not imply live runtime capabilities beyond status docs. |
| `docs/rag-probatoire.html` | static documentation | Public explanatory page for RAG probatoire. | Demonstrates doctrine, not a running RAG engine. |
| `docs/assets/pantheon-control/` | static prototype / partial read-only mirror | Static Pantheon Control prototype assets and pages. PR #239 confirms at least the update verifier mirror can remain aligned with the Python read-only verifier. | Prototype display is not a live cockpit, approval engine, memory engine or runtime. |
| `templates/hermes/dashboard-plugins/pantheon-modules/` | installable external Hermes plugin template / inactive here | After separate operator installation and enablement, the plugin reads native Hermes inventories and produces partial live operational observations. Its public preview uses synthetic data. | It has no Pantheon backend. Hermes state, Pantheon governance and task authorization remain separate; the MCP does not duplicate its runtime inventory. |
| `schemas/` | partial / protected review required | Validation artifacts may exist. Exact status must be checked before relying on them. | Schemas validate structure; they do not execute or approve. |
| `tests/` | partial / protected review required | Validation tests exist where present. Exact coverage must be checked before relying on them. | Tests do not promote doctrine by themselves. |
| `mcp-server/` | implemented read-only / partial / protected path | Repository contains a bounded read-only MCP policy / verification / consultation surface. In addition to existing validation, it can list honest consultation availability, explain allowlisted architecture placement from governed sources and qualify a caller-provided nine-axis capability-status candidate. The broader server remains partial/to verify. | It performs no Hermes runtime inventory or probe and implements no HTTP API, private knowledge retrieval, scoped permission service or remote MCP transport. It must not execute, approve, send, schedule, route providers, install, update or promote memory. |
| `ai_logs/` | runs as trace | Intervention logs exist as validation-only trace. | Logs are not doctrine and do not approve changes. |
| Notion Kanban | external / outside Pantheon | Project tracking exists outside the repo. | Notion is pilotage only; GitHub remains canonical. |

## Documented but not implemented

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| OpenWebUI integration | external read-only candidate / not installed | Doctrine describes OpenWebUI as exposure surface. The external `pantheon-mvp` repository now contains a tested Project Document Card Rich UI Tool candidate. | No OpenWebUI extension is installed by this repo. Committed external plugin code is not deployment, adoption or authorization for real dossier data. |
| Hermes execution integration | documented non-implemented / external | Doctrine describes Hermes as execution runtime; the dashboard-plugin template does not implement task execution integration. | Hermes execution remains outside Pantheon unless separately configured. |
| Hermes runtime governance card | candidate only / documented non-implemented | `HERMES_RUNTIME_GOVERNANCE.md` classifies Hermes Agent as an external runtime Capability Slot and cockpit card candidate. | It does not install, configure, activate, update, roll back or run Hermes; it only governs status, gates, evidence expectations and non-equivalence warnings. |
| Hermes installation assistance | candidate only / documented non-implemented | `HERMES_INSTALLATION_ASSISTANCE.md` defines human-facing installation assistance, command-candidate review, redacted output review and read-only check classifications. | It does not install, run commands, store secrets, configure providers, enable tools or gateways, update, roll back, declare safety or approve activation. |
| Common installation baseline | candidate support doctrine / documented non-implemented | `COMMON_INSTALLATION_BASELINE.md` defines the single required component baseline shared by supported deployments. | It creates no installer, stack, database, binding or activation. Required presence does not authorize use. |
| Common installation runbook | candidate operator artifact / documented non-implemented | `docs/install/COMMON_BASELINE_RUNBOOK.md` documents the manual SSH/Docker/Portainer handoff, pinned checkout, MCP configuration, acceptance and rollback sequence. | Commands remain operator-executed. The file does not run them, store secrets, change a host or authorize production use. |
| Install module catalog | candidate only / documented non-implemented | `INSTALL_MODULE_CATALOG.md` defines independent module records for source trust, provisioning, dependencies, conflicts, configuration, gates, health, exposure, backup, rollback and updates. | It does not compose alternative installations or create live catalog files, registry, installer, plugin marketplace, shell runner, provider router, approval engine or memory engine. |
| Legacy installation-composition material | obsolete / removed | The former composition document, manifests and schema are absent from the working tree and remain available only in Git history. | They must not determine, render or install a Pantheon environment. The obsolete index is the current status source. |
| Pantheon MVP Vertical binding | external executable candidate / implemented externally / tested / not adopted | `PANTHEON_MVP_COCKPIT_RECONCILIATION.md` is the current observation record for merged `pantheon-mvp#44`, pinned at `7f8989a670c6c476d55366bb0016a19dda3ebb6c`. It records the cards-first cockpit, proposal-only effect/site/navigation previews, signed Knowledge UPDATE gate and six resolved review findings. `PANTHEON_MVP_VERTICAL_BINDING.md` remains the detailed historical baseline for the earlier task-loop and Document → Knowledge slice. | Pantheon does not import, install, execute, activate or adopt this binding. CI success and merge establish repository implementation only. Target-runtime health, live Hermes binding, real-dossier use, activation and production use remain blocked. |
| Hermes skills from Pantheon | documented non-implemented | Skill governance and templates may exist. | Pantheon does not install or run Hermes skills. |
| Multi-model deliberation | external Hermes capability / candidate configuration / inactive here | Hermes Agent 0.18.2 natively exposes named Mixture of Agents configurations. Pantheon provides a disabled-by-default configuration fragment plus bounded handoff and Deliberation Candidate templates for one required analysis pass and at most one challenge pass. | No configuration is installed, enabled or run by this repository. Model agreement is not evidence; the aggregator is not ZEUS; outputs cannot approve, merge, mutate doctrine, promote memory or authorize external effects. |
| Architecture domain pack | candidate only / to verify | Architecture pack and method documents may frame professional method. | Domain pack does not advise, validate, execute, send or remember by itself. |
| Architecture document vertical | first Document → Knowledge slice implemented externally / not adopted | Pantheon Next defines the transport-neutral contract; external commit `af5ce4b` proves declared-source extraction, Project Document Card display, versioned `generated_unreviewed` Knowledge publication and conflict-safe mobile Markdown synchronization. | This does not prove a live Docling/Hermes deployment, automatic Evidence admission, full dossier coherence review, real-time collaboration or production readiness. |
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

## Next reconciliations

### MCP / dashboard / Pantheon Control

Current position after PR #239:

```text
mcp-server/ is no longer only a future candidate in repository terms.
It is an implemented read-only verification artifact, still partial / to verify as a whole.
Its consultation contract is transport-neutral, but only the local stdio MCP
projection is implemented; HTTP, remote MCP and live data-source access remain
documented non-implemented.
```

Status implication:

```text
AUTHORITY_INDEX.md and MODULES.md should classify the MCP surface as a protected read-only implementation artifact / active support surface, not as a general runtime.
```

Boundary to keep:

```text
The MCP surface may validate structure/status and return status data.
It must not execute, approve, send, schedule, route providers, install, update or promote memory.
```

### Pantheon MVP Vertical

Current position after `pantheon-mvp#44` merged on 2026-07-22:

```text
external repository pinned at 7f8989a670c6c476d55366bb0016a19dda3ebb6c
cards-first cockpit implemented externally
Document, Knowledge and Work Issue projections present
resource profiles present
proposal-only effect, site-manifest and navigation-profile previews present
signed and explicitly confirmed Knowledge UPDATE gate present
six review findings resolved before merge
reviewed CI run 29949615601 succeeded
Pantheon binding not adopted
installation and target-runtime health not established
activation not authorized
production use forbidden
```

The next steps remain separate environment authorization, installation, health verification, identity and secret review, a live bounded Hermes binding, rollback evidence and an explicit adoption/activation decision. Real identities, deployment credentials, browser-facing routing, real-dossier data posture, offline-device security and professional correctness must be reviewed before activation.

### Static prototype language

`docs/index.html` and Pantheon Control pages must not imply that target behavior is already a live product capability.

Required wording pattern:

```text
prototype / target behavior / documented non-implemented
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
