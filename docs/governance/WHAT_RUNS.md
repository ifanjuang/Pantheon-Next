# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-07-26

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
| `docs/assets/pantheon-control/` | orientation pointer plus bounded validation support / to verify | The former local Pantheon Control pages, project fixtures, navigation and interactive dashboard renderers are removed. `README.md` and `index.html` point to the external `pantheon-mvp` cockpit. A mutation-disabled synthetic Hermes renderer preview and six read-only JavaScript classifier mirrors remain because protected tests validate parity with external/plugin or Python implementations. | The pointer, preview and parity mirrors are not a live Pantheon cockpit, runtime probe, inventory, approval engine, memory engine or fallback implementation. |
| `templates/hermes/dashboard-plugins/pantheon-modules/` | installable external Hermes plugin template / inactive here | After separate operator installation and enablement, the plugin reads native Hermes inventories and produces partial live operational observations. Its public preview uses synthetic data. | It has no Pantheon backend. Hermes state, Pantheon governance and task authorization remain separate; the MCP does not duplicate its runtime inventory. |
| `schemas/` | partial / protected review required | Validation artifacts may exist. Exact status must be checked before relying on them. | Schemas validate structure; they do not execute or approve. |
| `tests/` | partial / protected review required | Validation tests exist where present. Exact coverage must be checked before relying on them. | Tests do not promote doctrine by themselves. |
| `mcp-server/` | implemented read-only / partial / protected path | Repository contains one transport-neutral `PantheonPolicyService`, a local stdio MCP consultation projection and an authenticated internal HTTP policy/preflight projection. The service can list governed sources, explain allowlisted architecture placement, classify requests, evaluate candidate-work preflight, validate a human decision against scope/ceiling/expiry/object/digest requirements and, when a read-only issuer registry is configured, verify the decision issuer signature and report `issuer_authenticated`. It can also prepare candidate contracts/evidence, validate governed structures and classify caller-provided evidence. | Neither transport executes Hermes work, approves an effect, sends, schedules, routes providers, installs, updates or promotes memory. `issuer_authenticated != approval`, and a valid decision verdict is not an effect authorization. Private knowledge retrieval and scoped identity/permission enforcement remain absent. |
| `Dockerfile.policy-api`, `compose.policy-api.yaml` | deployment candidate / not activated | Hardened internal-network candidate for `pantheon-policy-api`: no host port, read-only repository mount, read-only filesystem, dropped capabilities, no Docker socket and `ai-net` attachment. | Image/Compose presence is not installation, health, activation, approval or production authorization. An issuer registry is an optional operator-provided read-only deployment input, not repository identity authority. |
| `ai_logs/` | runs as trace | Intervention logs exist as validation-only trace. | Logs are not doctrine and do not approve changes. |
| `catalog/` capability / resource / decision records | candidate declarative / CI-checked / to verify | Non-executable candidate capability and resource records, plus current-decision projection, handoff-decision and provisioner-handoff candidate schemas, validated by `catalog-ci`, `current-decision-resolver-ci`, `handoff-decision-ci` and `provisioner-handoff-ci`. | Declarative records only. Not a live registry, installer, provisioner, connector, scheduler, queue, approval or memory engine. Only the former installation-composition manifests were removed; the directory itself is active. |
| Governance CI checks (`.github/scripts/`, `.github/workflows/`) | implemented read-only / runs on push and pull request | Roughly two dozen read-only repository-governance checks (index coverage, internal links, register instances, runtime-boundary language, status headers, axis vocabulary, obsolete-authority consistency, predecessor independence, packaging contract, vertical slice, capability catalog, current-decision resolver, provisioner/handoff contracts, ai-log paths) enforce doctrine on every push and pull request. | Read-only enforcement. Checks fail closed but never execute, install, send, approve, promote memory or modify protected paths. Governed by `GITHUB_REPOSITORY_GOVERNANCE.md`. |
| Architecture Project Understanding (APU) validation | implemented read-only / partial / to verify | `mcp-server/pantheon_mcp/apu.py` validates candidate APU objects against the schemas under `schemas/architecture-project-understanding/`, and `.github/scripts/check_apu_referential_integrity.py` checks referential integrity; both return gate posture as data. | Schema/structure validation only. It canonizes nothing, approves nothing and promotes no memory. Project Understanding promotion remains a governed human decision (ROADMAP R2 / issue #169). |
| Notion Kanban | external / outside Pantheon | Project tracking exists outside the repo. | Notion is pilotage only; GitHub remains canonical. |

## Documented but not implemented here

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| OpenWebUI integration | external read-only candidate / not installed | Doctrine describes OpenWebUI as exposure surface. The external `pantheon-mvp` repository contains tested Document, Knowledge, Work Issue and optional Paperless source surfaces. | No OpenWebUI extension is installed by this repo. Committed external code is not deployment, adoption or authorization for real dossier data. |
| Hermes execution integration | external implementation candidate / not installed | Doctrine describes Hermes as execution runtime. External `pantheon-mvp` contains the bounded policy/PEP seams, Runs binding candidates and optional Paperless document skill. | Repository implementation does not prove target installation, mandatory invocation, live PDP round-trip, skill/plugin selection, adoption or activation. Pantheon does not execute Hermes. |
| Hermes policy HTTP enforcement binding | external implementation candidate / not connected to a target | `mcp-server/docs/HTTP_API_CONTRACT.md` defines fail-closed consequential preflight/decision semantics; external `pantheon-mvp` implements the PEP enforcement seam. | Pantheon returns policy data/verdicts only; external runtimes enforce them. `PDP ready != effect authorized`. |
| Human decision issuer authentication | implemented conditionally in PDP / external producer implemented / target proof absent | PDP can verify configured issuer signatures; the external runtime supplies the matching signing producer. | Target registry, signed-decision delivery and `issuer_authenticated` round-trip remain unproven. |
| Core local/NAS document ingestion | external implementation candidate / not deployed | Declared source paths can be read from a bounded `MVP_DOCUMENT_ROOT`, checked against Task Contract scope/path boundaries, digested, extracted through reviewed bindings and persisted as Project Document candidates. | Local-source availability does not bypass Task Contract scope, Evidence rules or Knowledge publication gates. |
| Paperless document source runtime | optional candidate support doctrine / external implementation merged / not installed | `document_source_management` is optional; Paperless-ngx is the preferred binding. External `pantheon-mvp#84` establishes optional semantics and `pantheon-mvp#85` moves all Paperless-only services/required variables into `compose.paperless.yaml`. | Paperless absence is a valid baseline state and does not disable core document ingestion. When selected, Paperless installation/health/activation remain separately governed. |
| Hermes `pantheon-document-intake` skill | external implementation merged / optional / not installed | Paperless-specific exact-version source/intake skill. | Applies only when Paperless is selected. Skill available != installed != approved != task-authorized. |
| Hermes runtime governance card | candidate only / documented non-implemented | `HERMES_RUNTIME_GOVERNANCE.md` classifies Hermes Agent as an external runtime Capability Slot and cockpit runtime-card candidate. | It does not install, configure, activate, update, roll back or run Hermes. |
| Hermes installation assistance | candidate only / documented non-implemented | Human-facing installation assistance and read-only check classifications. | It does not execute commands or approve activation. |
| Common installation baseline | candidate support doctrine / documented non-implemented | `COMMON_INSTALLATION_BASELINE.md` defines one required core. Document ingestion is core; `document_source_management` is optional with preferred binding Paperless-ngx. | One architecture, variable selected services. Paperless absence is not degradation. |
| Common installation runbook | candidate operator artifact / documented non-implemented | Manual SSH/Docker/Portainer handoff. | Commands remain operator-executed. |
| Paperless installation runbook | candidate operator artifact / optional / documented non-implemented | `docs/install/PAPERLESS_INITIAL_INSTALLATION.md` applies only when Paperless is selected. | It executes nothing and grants no activation. |
| Hermes document intake skill runbook | candidate operator artifact / optional / documented non-implemented | Native installation/acceptance for the Paperless-specific skill. | It executes no install and grants no activation. |
| Install module catalog | candidate only / documented non-implemented | Independent module-record grammar. | No installer, marketplace, provider router, approval or memory engine. |
| Legacy installation-composition material | obsolete / removed | Former composition documents/manifests remain only in history. | Must not determine current deployment. |
| Pantheon MVP Vertical binding | external executable candidate / implemented externally / tested / not adopted | Historical cockpit baseline plus later external runtime increments. | CI/merge establish implementation only; target health/adoption/activation remain unproven. |
| Hermes skills from Pantheon | documented non-implemented | Skill governance and operator runbooks may exist. | Pantheon does not install or run Hermes skills. |
| Multi-model deliberation | external Hermes capability / candidate configuration / inactive here | Hermes provides external deliberation capability. | Model agreement is not Evidence or approval. |
| Architecture domain pack | candidate only / to verify | Architecture pack and method documents may frame professional method. | Domain pack does not execute/send/remember by itself. |
| Architecture document vertical | first Document → Knowledge slice implemented externally / not adopted | Transport-neutral document lifecycle supports governed local/NAS source ingestion. Paperless exact-version intake is an optional additional source-management path, not a second Knowledge/RAG authority. | No automatic Evidence admission or production readiness is implied. |
| Data platform | candidate only / to verify | Candidate records/evidence/approval boundaries. | Must not become ERP, scheduler, queue, runtime, approval or memory engine. |
| Capability registry / skill lifecycle | candidate only / to verify | Candidate governance vocabulary. | Capability declaration is not authorization. |
| Register integrity review by shadow reconstruction | documented non-implemented / candidate only | Non-destructive integrity review doctrine plus external candidate controls. | No automatic discrepancy resolution or register mutation. |
| Method Cards and Card Stack | candidate only / documented non-implemented | Candidate cockpit/method grammar. | Cards are not agents/runtime/approval/memory. |
| Governed form filling | candidate only / to verify | Candidate field-as-claim form method. | No form runtime/sender is implemented by doctrine. |
| Revit Gate | candidate only / documented non-implemented | Future local add-in boundary. | No active Revit runtime in Pantheon. |
| `revit-plugin/` | documented non-implemented / skeleton only | Future local Revit adapter skeleton. | Implementation remains to verify. |

## Voluntarily absent

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

## Next reconciliations

### MCP / policy HTTP / dashboard / Pantheon Control

```text
mcp-server/ contains one shared read-only service.
Local stdio MCP consultation is implemented.
Authenticated internal HTTP classification/preflight/decision validation is implemented as a candidate.
Optional configured issuer-signature verification is implemented.
The Compose deployment is declared but not activated.
Live target enforcement and private data-source wiring remain unproven.
```

```text
MCP helps agents consult and prepare.
HTTP provides deterministic policy/preflight/decision-validation data.
Configured issuer verification authenticates a bounded decision issuer; it does not approve the decision.
Hermes remains the Policy Enforcement Point and execution runtime.
Neither Pantheon transport executes, approves, sends, schedules, routes providers, installs, updates or promotes memory.
```

### Document source → Hermes → Project Document vertical

Current repository implementation status:

```text
core local/NAS ingestion                 implemented externally / target proof not established
optional document_source_management      selected as Capability Slot
preferred binding paperless_ngx          external implementation merged
pantheon-mvp #84                         optional Paperless semantics merged
pantheon-mvp #85                         separate optional Paperless Compose overlay merged
Paperless target installation            not established
Hermes Paperless skill target install    not established
Pantheon PDP target deployment           not established
live signed-decision round-trip          not established
real-dossier scope                       not authorized
activation                               not authorized
production adoption                      not decided
```

The next admissible core proof is a controlled non-production local/NAS synthetic ingestion. Paperless exact-version acceptance is additional and applies only if that optional binding is selected.

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
implemented != installed
installed != approved
reachable != healthy
healthy != safe
issuer_authenticated != approval
PDP ready != effect authorized
runtime_success != Evidence
synthetic pass != production adoption
```

### Pantheon MVP Vertical historical baseline

Earlier cockpit reconciliation remains historical implementation evidence only; later external changes do not turn it into a deployment/adoption record.

### Static exposure language

Static/public surfaces must continue to distinguish orientation/prototype/external implementation from live product availability.

## Final rule

```text
Documentation may describe.
Static pages may expose.
Read-only checks may verify structure or status.
External runtimes may execute under contract.
Pantheon governs consequential status.
The human decides.
```
