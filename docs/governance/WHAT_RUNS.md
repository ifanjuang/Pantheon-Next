# What Runs

Status: active support note — repository runtime-status map — implemented as documentation.
Boundary profile: active_support_doctrine.

Date: 2026-08-26

This file distinguishes repository implementation, external observations, target selection and production adoption. It creates no runtime behavior or authorization.

```text
implemented != installed
installed != activated
activated != task-authorized
runtime success != Evidence
projection != persistence
repository presence != selected architecture
```

## Runs or exists in this repository

| Area | Current status | Meaning / boundary |
|---|---|---|
| Governance/documentation corpus | runs as repository content | Markdown doctrine, support documents, references and logs exist. Documentation does not execute work. |
| GitHub Pages/static assets | static documentation/prototypes | Public/static pages may explain or demonstrate concepts; static publication is not product/runtime availability. |
| Governance and implementation CI | implemented read-only | Repository checks/tests can fail closed on structural/contracts regressions. Green CI is not adoption, approval or professional validation. |
| `mcp-server/` | implemented read-only / partial | Shared Pantheon policy/verification service with bounded consultation/preflight/decision-validation surfaces. It does not execute Hermes work, send, schedule, install, route providers or promote memory. |
| `implementation/` | executable candidate implementation / co-located / not adopted | Co-located implementation contains persistence, APIs, Cockpit, Hermes seams and residual historical compatibility code. Co-location does not grant governance authority or production activation. |
| Pantheon Cockpit under `implementation/mvp_vertical/cockpit/` | executable candidate / tested / not adopted | Registry-backed navigation, Card projection/renderer and bounded product projections exist. The Cockpit is not a second general-purpose Hermes chat frontend. |
| Catalog/contracts | declarative / CI-checked / to verify per object | Capability/resource/binding/decision candidate records exist. A catalog record is not a live registry, installer or authorization. |
| Architecture Project Understanding validation | implemented read-only / partial | Candidate structures can be validated where schemas and checkers exist. Schema validity does not canonize professional state. |
| `ai_logs/` | validation/provenance trace | Historical intervention records exist. They are not doctrine or current architecture authority. |

## External/runtime surfaces

| Area | Current status | Meaning / boundary |
|---|---|---|
| Hermes Agent | external execution runtime / target deployment state must be observed separately | Hermes owns runtime interaction/execution capabilities. Pantheon governs consequential status and admission boundaries; repository code does not prove target enforcement. |
| Hermes Web/dashboard | selected interaction baseline | Current target client for chat, sessions and runtime controls. Client operation does not create Pantheon governance state. |
| `willscott-v2/hermes-mobile-pwa` | external client candidate / compatible by source review / not selected or installed by this repo | Thin mobile/PWA client using Hermes dashboard REST/WebSocket/auth surfaces. Replaceable client only; deployment/auth/network posture remains separate. |
| Obsidian workspace | selected workspace direction / external | Human-authored Markdown notes and editable working projections. Obsidian is not a DMS, Evidence store, governed Project identity or Registre Probatoire. |
| Hindsight | external derived-memory/index candidate with prior bounded qualification | Recall/index layer only where selected. Memory/retrieval does not become truth or Evidence. |

## Implemented/qualified candidate paths not proven in production

| Area | Current status | Remaining proof |
|---|---|---|
| Hermes policy/PEP integration | co-located candidate / target round-trip not established here | Demonstrate mandatory target-runtime invocation, signed/qualified decision handling and real deployment boundary. |
| Core local/NAS document ingestion | co-located implementation candidate | Prove selected target paths, permissions, real-dossier authorization and operational rollback before production use. |
| Pantheon Cockpit adoption | executable candidate / not adopted | Live deployment, data bindings and operational acceptance remain separate decisions. |
| Obsidian/Hindsight synchronization topology | partially qualified / external stabilization work remains | Real client/offline/conflict and deployment hardening remain separate from repository CI. |
| Hermes external dashboard/plugin helpers | existing templates and candidates where present | Installation/enablement and live target state must be observed externally. |

## Refused target integrations and historical residue

### OpenWebUI

```text
architecture_status: refused
current_target_role: none
implementation_adapter_status: removed from executable candidate
replacement responsibilities:
  runtime interaction -> Hermes Web/dashboard + compatible Hermes clients
  governed projections -> Pantheon Cockpit
```

The product-specific Python package, capability routes/registry and their dedicated implementation tests have been removed after consumer verification. Native document/Knowledge APIs and Cockpit projections remain under `mvp_vertical`.

Historical OpenWebUI templates and documentation may still exist as reference/provenance until their incoming links are converged; they are not executable target architecture.

```text
historical template present != architecture dependency
```

### Paperless-ngx

```text
architecture_status: refused
current_target_role: none
replacement responsibilities:
  exact source/provenance -> existing document/source owners
  local/NAS intake -> bounded core ingestion path
  Markdown workspace -> Obsidian
```

The repository still contains historical Paperless gateway, ingestion, Compose, catalog and runbook material. It must be removed only after consumer, test and schema implications are checked in its protected implementation slice.

Obsidian does not replace Paperless as a DMS; the DMS dependency itself is no longer required by the target architecture.

## Voluntarily absent from Pantheon core

```text
Pantheon internal general-purpose agent runtime
second general-purpose chat frontend
required DMS product
hidden autonomous approval engine
automatic durable-memory promotion engine
scheduler
queue
provider router
plugin marketplace
automatic external sender
unrestricted connector gateway
ERP
production data platform authority
```

External runtimes may contain their own schedulers, queues or provider mechanics. Their existence does not transfer those responsibilities into Pantheon.

## Current target composition

```text
Hermes Web/dashboard
  + optional replaceable Hermes mobile/PWA client
        |
Hermes Agent
        |
Pantheon governance/admission boundaries
        |
Pantheon Cockpit for governed projections

Obsidian -> human Markdown workspace
Hindsight/runtime memory -> optional derived recall
Professional source files -> existing source/document owners
```

See `TARGET_ARCHITECTURE.md` for the directional map and `CORE_CONCEPTS_MAP.md` for ownership navigation.

## Protected-path rule

`implementation/`, `mcp-server/`, schemas, tests, CI, Docker/environment material and other protected paths require their normal review discipline. A documentation decision to refuse a dependency does not authorize deleting protected implementation code without consumer/test verification.

## Next reconciliation

The next safe implementation slice is now Paperless-specific:

1. enumerate current imports, routes, tests, Compose/catalog/skill configuration referencing Paperless;
2. separate generic source/provenance, document ingestion and policy/PEP capabilities from Paperless-specific compatibility code;
3. remove only product-specific code with no surviving target consumer;
4. update catalog, runbooks, docs and tests accordingly;
5. run full relevant CI before merge.

OpenWebUI template/document cleanup can then remove remaining non-executable historical references once incoming links are converged.

## Final rule

```text
State what exists.
State what is selected.
State what is only historical compatibility.
Do not confuse any of those with production adoption or authorization.
```
