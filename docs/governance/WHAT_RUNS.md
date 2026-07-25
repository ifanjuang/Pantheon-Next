# What Runs

Status: active support / repository runtime-status map — to verify.

Date: 2026-07-25

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
| Notion Kanban | external / outside Pantheon | Project tracking exists outside the repo. | Notion is pilotage only; GitHub remains canonical. |

## Documented but not implemented here

| Area | Current status | Meaning | Boundary |
|---|---|---|---|
| OpenWebUI integration | external read-only candidate / not installed | Doctrine describes OpenWebUI as exposure surface. The external `pantheon-mvp` repository contains tested Document, Knowledge, Work Issue and Paperless source surfaces. | No OpenWebUI extension is installed by this repo. Committed external code is not deployment, adoption or authorization for real dossier data. |
| Hermes execution integration | external implementation candidate / not installed | Doctrine describes Hermes as execution runtime. External `pantheon-mvp#59`, now merged in that repository, contains the `pantheon-document-intake` skill candidate and the bounded PEP/PDP enforcement seam used by the Paperless document path. | Repository implementation does not prove a target Hermes installation, mandatory invocation, live PDP round-trip, skill selection, adoption or activation. Pantheon still does not execute the skill. |
| Hermes policy HTTP enforcement binding | external implementation candidate / not connected to a target | `mcp-server/docs/HTTP_API_CONTRACT.md` defines fail-closed consequential preflight/decision semantics; external `pantheon-mvp` implements an HTTP policy client, PEP normalization, PEP-owned effect expectations and effect-flag enforcement. | The Pantheon API returns policy data/verdicts only; the external PEP enforces them. No current evidence proves a live Hermes target calls and obeys this path. `PDP ready != effect authorized`. |
| Human decision issuer authentication | implemented conditionally in PDP / external producer implemented / target proof absent | The PDP can verify HMAC decision signatures when `PANTHEON_DECISION_ISSUER_KEYS_PATH` points to a reviewed read-only registry. External `pantheon-mvp#66` provides the matching signing producer. | Target registry provisioning, signed decision delivery and an observed `issuer_authenticated` round-trip are not established. `issuer_authenticated != approval`. |
| Paperless document source runtime | candidate support doctrine / external implementation merged / not installed | Paperless-ngx is selected as the reference external `document_source_management` runtime. External `pantheon-mvp#56` implements bounded source reads/search, exact-version Source Capture, task observation, gateway projection and governed mutation seams; #59 layers the Hermes intake binding and PEP hardening. | No target Paperless installation, target health, adoption, activation or real-dossier authorization is established. Paperless metadata/OCR/task success does not become Pantheon truth, Knowledge, Evidence or approval. |
| Hermes `pantheon-document-intake` skill | external implementation merged / not installed | External `pantheon-mvp#59` provides a complete AgentSkills-style package with transport script for search/inspect/capture/task, governed Project Document candidate intake and governed metadata-mirror requests. | Skill package available != installed; installed != approved; skill selected != task authorized. The skill receives neither Paperless, PDP nor issuer-signing secrets. |
| Hermes runtime governance card | candidate only / documented non-implemented | `HERMES_RUNTIME_GOVERNANCE.md` classifies Hermes Agent as an external runtime Capability Slot and cockpit runtime-card candidate. | It does not install, configure, activate, update, roll back or run Hermes; it only governs status, gates, evidence expectations and non-equivalence warnings. |
| Hermes installation assistance | candidate only / documented non-implemented | `HERMES_INSTALLATION_ASSISTANCE.md` defines human-facing installation assistance, command-candidate review, redacted output review and read-only check classifications. | It does not install, run commands, store secrets, configure providers, enable tools or gateways, update, roll back, declare safety or approve activation. |
| Common installation baseline | candidate support doctrine / documented non-implemented | `COMMON_INSTALLATION_BASELINE.md` defines the single required component baseline shared by supported deployments, including Paperless source-management presence for the reference professional installation. | It creates no installer, stack, database, binding or activation. Required presence does not authorize use. |
| Common installation runbook | candidate operator artifact / documented non-implemented | `docs/install/COMMON_BASELINE_RUNBOOK.md` documents the manual SSH/Docker/Portainer handoff, pinned checkout, MCP configuration, acceptance and rollback sequence. | Commands remain operator-executed. The file does not run them, store secrets, change a host or authorize production use. |
| Paperless initial installation runbook | candidate operator artifact / documented non-implemented | `docs/install/PAPERLESS_INITIAL_INSTALLATION.md` documents pinned runtime, private networking, storage, database/broker separation, API identity, exact-version capture, backup/restore/update/rollback. | It executes nothing and does not activate the document binding or authorize real dossier data. |
| Hermes document intake skill runbook | candidate operator artifact / documented non-implemented | `docs/install/HERMES_PANTHEON_DOCUMENT_INTAKE_SKILL.md` documents native Hermes installation, bounded secrets, read-only checks, signed-decision target proof and synthetic Project Document candidate intake. | It executes no install and grants no activation. Synthetic success remains a technical observation, not adoption. |
| Install module catalog | candidate only / documented non-implemented | `INSTALL_MODULE_CATALOG.md` defines independent module records for source trust, provisioning, dependencies, conflicts, configuration, gates, health, exposure, backup, rollback and updates. | It does not compose alternative installations or create live catalog files, registry, installer, plugin marketplace, shell runner, provider router, approval engine or memory engine. |
| Legacy installation-composition material | obsolete / removed | The former composition document, manifests and schema are absent from the working tree and remain available only in Git history. | They must not determine, render or install a Pantheon environment. The obsolete index is the current status source. |
| Pantheon MVP Vertical binding | external executable candidate / implemented externally / tested / not adopted | `PANTHEON_MVP_COCKPIT_RECONCILIATION.md` records the earlier merged cockpit baseline. The external repository has since advanced with the Paperless source adapter, Hermes document skill/PEP and decision-signing producer. Those later repository implementations are tracked by their dedicated runtime-adapter doctrine/runbooks rather than silently promoting the historical reconciliation document. | Pantheon does not import, install, execute, activate or adopt the external repository. CI success and merge establish implementation only. Target-runtime health, live Hermes/PDP/Paperless wiring, real-dossier use, activation and production use remain unproven. |
| Hermes skills from Pantheon | documented non-implemented | Skill governance and operator runbooks may exist. | Pantheon does not install or run Hermes skills. |
| Multi-model deliberation | external Hermes capability / candidate configuration / inactive here | Hermes Agent 0.18.2 natively exposes named Mixture of Agents configurations. Pantheon provides a disabled-by-default configuration fragment plus bounded handoff and Deliberation Candidate templates for one required analysis pass and at most one challenge pass. | No configuration is installed, enabled or run by this repository. Model agreement is not evidence; the aggregator is not ZEUS; outputs cannot approve, merge, mutate doctrine, promote memory or authorize external effects. |
| Architecture domain pack | candidate only / to verify | Architecture pack and method documents may frame professional method. | Domain pack does not advise, validate, execute, send or remember by itself. |
| Architecture document vertical | first Document → Knowledge slice implemented externally / not adopted | Pantheon Next defines the transport-neutral contract; the external runtime includes declared-source extraction, Project Document display, governed Knowledge publication and synchronization candidates. Paperless exact-version intake is now an additional candidate source path, not a second Knowledge/RAG authority. | This does not prove a live Docling/Hermes/Paperless deployment, automatic Evidence admission, full dossier coherence review, real-time collaboration or production readiness. |
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

Current position after the policy HTTP implementation candidate, issuer-authentication slice and local dashboard retirement:

```text
mcp-server/ contains one shared read-only service.
Local stdio MCP consultation is implemented.
Authenticated internal HTTP classification/preflight/decision validation is implemented as a candidate.
Optional configured issuer-signature verification is implemented.
The Compose deployment is declared but not activated.
The former local Pantheon Control pages, project fixtures and interactive renderers are removed.
The retained Pantheon Control URL is an external orientation pointer.
A synthetic Hermes renderer preview remains for protected external-template parity validation.
Six read-only JavaScript classifier mirrors remain for protected Python/JavaScript verdict parity tests.
Live target Hermes enforcement, private data-source access and target issuer-registry wiring remain unproven.
```

Status implication:

```text
AUTHORITY_INDEX.md and MODULES.md classify policy transports as protected read-only implementation artifacts, not as a general runtime or approval authority.
The orientation pointer, synthetic preview and parity mirrors are not a live dashboard.
```

Boundary to keep:

```text
MCP helps agents consult and prepare.
HTTP provides deterministic policy/preflight/decision-validation data.
Configured issuer verification authenticates a bounded decision issuer; it does not approve the decision.
Hermes remains the Policy Enforcement Point and execution runtime.
Neither Pantheon transport executes, approves, sends, schedules, routes providers, installs, updates or promotes memory.
```

### Document source → Hermes → Project Document vertical

Repository implementation status after the current Paperless/Hermes merges:

```text
Pantheon Next #467  Paperless source-management placement merged
Pantheon Next #468  initial Paperless baseline/runbooks merged
pantheon-mvp #56    bounded Paperless adapter merged
pantheon-mvp #66    matching human-decision signing producer merged
pantheon-mvp #59    Hermes document skill + PEP/PDP hardening merged

Paperless target installation          not established
Hermes skill target installation       not established
Pantheon PDP target deployment         not established
Docling target binding                 not established
live signed-decision round-trip        not established
live Project Document synthetic intake not established
real-dossier scope                     not authorized
activation                             not authorized
production adoption                    not decided
```

The next admissible proof is a controlled non-production deployment and synthetic exact-version intake. It must preserve separate observations for installation, reachability, health, issuer authentication, policy authorization, runtime success and professional evidence.

```text
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

The earlier `pantheon-mvp#44` reconciliation remains a historical implementation baseline for the cards-first cockpit and Document/Knowledge/Work Issue slice. Later Paperless/Hermes/signing changes do not retroactively turn that historical trace into a deployment/adoption record.

### Static exposure language

`docs/index.html`, the Pantheon Control orientation page and retained synthetic previews must not imply that target behavior is already a live product capability.

Required wording patterns:

```text
orientation pointer / synthetic preview / read-only parity mirror / external implementation
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
