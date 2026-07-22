# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-07-22

This document states what currently runs, what is static documentation, what is partial or to verify, and what is intentionally absent.

It is a status-honesty map. It does not create runtime behavior, approve any tool, install an adapter, authorize external action, create a scheduler, create a queue, create an approval engine or promote memory.

Runtime boundary in this file is expressed as operational fields, not by repeating the doctrine slogan.

```text
exposed_by   -> display or publication surface
executed_by  -> runtime or implementation artifact, when one exists
governed_by  -> Pantheon boundary and status rule
approved_by  -> human approval where consequential
forbidden    -> behavior that must not be inferred
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
| `mcp-server/` | implemented read-only / partial / protected path | Repository contains one transport-neutral `PantheonPolicyService`, a local stdio MCP consultation projection and an authenticated internal HTTP policy/preflight projection. The service can list governed sources, explain allowlisted architecture placement, classify requests, evaluate candidate-work preflight, prepare candidate contracts/evidence, validate governed structures and classify caller-provided evidence. | Neither transport performs Hermes runtime inventory, external execution, approval, sending, scheduling, provider routing, installation, update or memory promotion. Private knowledge retrieval and scoped identity/permission enforcement remain absent. |
| `Dockerfile.policy-api`, `compose.policy-api.yaml` | deployment candidate / not activated | Hardened internal-network candidate for `pantheon-policy-api`: no host port, read-only repository mount, read-only filesystem, dropped capabilities, no Docker socket and `ai-net` attachment. | Image/Compose presence is not installation, health, activation, approval or production authorization. |
| `ai_logs/` | runs as trace | Intervention logs exist as validation-only trace. | Logs are not doctrine and do not approve changes. |
| Notion Kanban | external / outside Pantheon | Project tracking exists outside the repo. | Notion is pilotage only; GitHub remains canonical. |

## Documented but not implemented

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| OpenWebUI integration | external read-only candidate / not installed | Doctrine describes OpenWebUI as exposure surface. The external `pantheon-mvp` repository now contains a tested Project Document Card Rich UI Tool candidate. | No OpenWebUI extension is installed by this repo. Committed external plugin code is not deployment, adoption or authorization for real dossier data. |
| Hermes execution integration | documented non-implemented / external | Doctrine describes Hermes as execution runtime; the dashboard-plugin template and policy API do not implement task execution integration or the Policy Enforcement Point. | Hermes execution and mandatory preflight enforcement remain outside Pantheon unless separately configured. |
| Hermes policy HTTP enforcement binding | adapter configuration candidate / not installed | `mcp-server/docs/HTTP_API_CONTRACT.md` defines fail-closed behavior for consequential preflight and temporary legacy-route compatibility. | The API returns policy data only. Hermes must enforce the result; no current repo artifact proves that the live Hermes container calls or obeys it. |
| Hermes runtime governance card | candidate only / documented non-implemented | `HERMES_RUNTIME_GOVERNANCE.md` classifies Hermes Agent as an external runtime Capability Slot and cockpit card candidate. | It does not install, configure, activate, update, roll back or run Hermes; it only governs status, gates, evidence expectations and non-equivalence warnings. |
| Hermes installation assistance | candidate only / documented non-implemented | `HERMES_INSTALLATION_ASSISTANCE.md` defines human-facing installation assistance, command-candidate review, redacted output review and read-only check classifications. | It does not install, run commands, store secrets, configure providers, enable tools or gateways, update, roll back, declare safety or approve activation. |
| Install module catalog | candidate only / documented non-implemented | `INSTALL_MODULE_CATALOG.md` defines a candidate grammar for module records, preset records, dependency roles, conflict classes, source trust, provisioning, gates, health, rollback and update policy. | It does not create live `modules.json`, `presets.json`, schemas, tests, registry, installer, plugin marketplace, Docker/Portainer stack, shell runner, provider router, approval engine or memory engine. |
| Pantheon MVP Vertical binding | external executable candidate / observed at pinned SHA / not adopted | `PANTHEON_MVP_VERTICAL_BINDING.md` classifies `ifanjuang/pantheon-mvp` as an external candidate binding, observed at commit `af5ce4b552db8de1a90b53fdb40b810074dbc4dc` on 2026-07-20. In addition to the governed task loop and Work Issues, it implements the vendored Document → Knowledge contract, frozen chunk provenance, versioned Knowledge publication, a mobile offline editor candidate and a proposal-only Hermes edit seam. | Pantheon does not import, install, execute, activate or adopt this binding. PR #41 head `8507afc9` passed PostgreSQL/pgvector workflow run `29764430187` with `155 passed`. Test success is not adoption or professional validation. Real-dossier use, live Hermes binding, installation, activation and production use remain blocked. |
| Hermes skills from Pantheon | documented non-implemented | Skill governance and templates may exist. | Pantheon does not install or run Hermes skills. |
| Multi-model deliberation | external Hermes capability / candidate configuration / inactive here | Hermes Agent 0.18.2 natively exposes named Mixture of Agents presets. Pantheon provides a disabled-by-default configuration fragment plus bounded handoff and Deliberation Candidate templates for one required analysis pass and at most one challenge pass. | No preset is installed, configured, enabled or run by this repository. Model agreement is not evidence; the aggregator is not ZEUS; outputs cannot approve, merge, mutate doctrine, promote memory or authorize external effects. |
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

### MCP / policy HTTP / dashboard / Pantheon Control

Current position after the policy HTTP implementation candidate:

```text
mcp-server/ contains one shared read-only service.
Local stdio MCP consultation is implemented.
Authenticated internal HTTP classification/preflight is implemented as a candidate.
The Compose deployment is declared but not activated.
Live Hermes enforcement, remote MCP and private data-source access remain absent.
```

Status implication:

```text
AUTHORITY_INDEX.md and MODULES.md should classify both transports as protected read-only implementation artifacts, not as a general runtime or approval authority.
```

Boundary to keep:

```text
MCP helps agents consult and prepare.
HTTP provides deterministic policy/preflight data.
Hermes remains the Policy Enforcement Point and execution runtime.
Neither projection executes, approves, sends, schedules, routes providers, installs, updates or promotes memory.
```

### Pantheon MVP Vertical

Current position after the 2026-07-19 bounded verification:

```text
external repository observed at af5ce4b552db...
external implementation present in repository
Work Issue persistence slice present and tested
bounded Docling extraction and strict NAS intake present and tested
Project Document Card API and OpenWebUI Rich UI Tool candidate present and tested
Document → Knowledge publication and mobile offline editor candidate present and tested
reviewed latest workflow run: 29764430187 (155 passed with PostgreSQL/pgvector)
Pantheon binding not adopted
activation not authorized
production use forbidden
```

The next steps are separate environment authorization and a live Hermes proposal binding. Real identities, deployment credentials, browser-facing routing, real-dossier data posture, offline-device security and rollback must be reviewed before activation. Full coherence review, inline governance annotations and concurrent multi-user editing remain later capabilities.

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
