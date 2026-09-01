# What Runs

Status: active support note — repository runtime-status map — implemented as documentation.
Boundary profile: active_support_doctrine.

Date: 2026-09-02

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
| `implementation/` | executable candidate implementation / co-located / not adopted | Co-located implementation contains persistence, APIs, Cockpit and Hermes seams. Co-location does not grant governance authority or production activation. |
| Pantheon Cockpit under `implementation/mvp_vertical/cockpit/` | executable candidate / tested / not adopted | Registry-backed navigation, Card projection/renderer and bounded product projections exist. The Cockpit is not a second general-purpose Hermes chat frontend. |
| Catalog/contracts | declarative / CI-checked / to verify per object | Capability/resource/binding/decision candidate records exist. A capability may remain intentionally unbound; a catalog record is not a live registry, installer or authorization. |
| Architecture Project Understanding validation | implemented read-only / partial | Candidate structures can be validated where schemas and checkers exist. Schema validity does not canonize professional state. |
| `ai_logs/` | validation/provenance trace | Historical intervention records exist. They are not doctrine or current architecture authority. |

## External/runtime surfaces

| Area | Current status | Meaning / boundary |
|---|---|---|
| Hermes Agent | external execution runtime / current candidate target 0.21.0 / target deployment state must be observed separately | Hermes owns runtime interaction/execution capabilities. Pantheon governs consequential status and admission boundaries; repository code does not prove target enforcement. |
| Hermes Desktop | selected rich interaction direction / external / deployment not observed by this repo | Current target host for rich chat/runtime interaction, including a topology where Desktop controls an authenticated Hermes backend on another machine. Client reachability does not qualify the remote runtime or create Pantheon governance state. |
| Hermes Web/dashboard | selected browser/admin fallback and remote-backend service surface | Browser interaction, runtime administration and the remotely reachable Hermes service surface remain useful where selected. It is no longer the sole preferred rich interaction client and it does not become a Pantheon projection owner. |
| A2UI on Hermes Desktop | qualification direction / not implemented on current `main` | Candidate declarative presentation layer for generated UI inside the Hermes interaction surface. The former Cockpit-targeted lab PR #882 was closed unmerged after the host decision changed. `A2UI surface != governed object`; `UI action != authorization`. |
| `willscott-v2/hermes-mobile-pwa` | external client candidate / compatible by source review / not selected or installed by this repo | Thin mobile/PWA client using Hermes dashboard REST/WebSocket/auth surfaces. Replaceable client only; deployment/auth/network posture remains separate. |
| Obsidian workspace | selected workspace direction / external | Human-authored Markdown notes and editable working projections. Obsidian is not a DMS, Evidence store, governed Project identity or Registre Probatoire. |
| Hindsight | external derived-memory/index candidate with prior bounded qualification | Recall/index layer only where selected. Memory/retrieval does not become truth or Evidence. |

## Implemented/qualified candidate paths not proven in production

| Area | Current status | Remaining proof |
|---|---|---|
| Hermes policy/PEP integration | co-located candidate / internal decision-client assembly exists / target enforcement not established | The Cockpit can assemble the real Pantheon decision client for one internal consequential Knowledge path. This does not establish mandatory invocation in the selected Hermes/runtime deployment. Demonstrate the target-runtime boundary, authenticated/qualified decision references and actual deployment configuration separately. |
| Internal consequential-write chokepoint | partial — one reviewed application boundary wired; wider surface remains open | The mutation inventory now enumerates 92 entry points: 71 have been individually reviewed and 21 remain explicitly unreviewed. The Cockpit Knowledge UPDATE apply route resolves the Pantheon decision client under a fail-closed default posture; an unconfigured decision point refuses that route, while local-guards-only operation must be selected explicitly. The underlying `knowledge_update.apply_knowledge_update` primitive still accepts an optional policy client for bounded direct/test use, so the inventory continues to describe that function-level fact rather than overclaiming universal enforcement. When a client is supplied, the Knowledge owner re-binds intent, write status, project scope and decision expectation from the exact signed UPDATE, so a caller-supplied candidate cannot broaden the effect Pantheon validates. Its existing `knowledge.revise_knowledge` transaction remains the persistence owner and validates before commit. Nine reviewed entries are currently `gate_required_not_wired`; that debt is tracked by the mutation inventory and must not grow silently. Remaining proof: review the 21 unknown entries, wire only consequential application boundaries that actually require the PDP, and observe the selected deployment. A validated decision is not the applied effect; the returned effect-binding trace is not Evidence, approval or production proof. |
| Core local/NAS document ingestion | co-located implementation candidate | Prove selected target paths, permissions, real-dossier authorization and operational rollback before production use. |
| Pantheon Cockpit adoption | executable candidate / not adopted | Live deployment, data bindings and operational acceptance remain separate decisions. |
| Obsidian/Hindsight synchronization topology | partially qualified / external stabilization work remains | Real client/offline/conflict and deployment hardening remain separate from repository CI. |
| Hermes external dashboard/plugin helpers | existing templates and candidates where present | Installation/enablement and live target state must be observed externally. |
| Hermes Desktop remote-runtime topology | source-supported deployment direction / not live-qualified here | Observe the exact Desktop build, exact remote Hermes artifact, authentication, network exposure, backend identity, tool envelope and disconnect/reconnect behavior before governed use. `connection succeeds != governed runtime qualified`. |

## Refused target integrations and historical provenance

### OpenWebUI

```text
architecture_status: refused
current_target_role: none
implementation_adapter_status: removed from executable candidate
replacement responsibilities:
  rich runtime interaction -> Hermes Desktop
  browser/admin/runtime service -> Hermes Web/dashboard + compatible Hermes clients
  governed projections -> Pantheon Cockpit
```

The product-specific executable adapter has been removed after consumer verification. Native document/Knowledge APIs and Cockpit projections remain under `mvp_vertical`.

Residual non-executable templates, documentation or compatibility pointers may still exist pending their own incoming-link audit; their presence is historical/reference material, not target architecture.

### Paperless-ngx

```text
architecture_status: refused
current_target_role: none
implementation_adapter_status: retired
replacement responsibilities:
  exact source/provenance -> existing Source/document owners
  local/NAS intake -> bounded core ingestion path
  Markdown workspace -> Obsidian
```

The Paperless client, gateway, ingestion binding, Compose paths, catalog resource, SQL binding migration, Hermes Paperless skill and dedicated document-runtime observer path have been retired after consumer audit. No replacement DMS abstraction was introduced.

The `document_source_management` capability remains provider-agnostic and may be intentionally unbound. Obsidian does not become a DMS or source authority.

```text
source capture != Evidence
folder/path != governed identity
provider selected != authority transfer
```

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
Hermes Desktop
  selected rich interaction host
        |
        | local or authenticated remote Hermes backend
        v
Hermes Agent
        |
Pantheon governance/admission boundaries
        |
Pantheon Cockpit for governed projections

Hermes Web/dashboard
  -> browser/admin fallback and remote-backend service surface

A2UI
  -> presentation candidate to qualify inside Hermes Desktop, not Cockpit authority

Obsidian -> human Markdown workspace
Hindsight/runtime memory -> optional derived recall
Professional source files -> existing Source/document owners
```

See `TARGET_ARCHITECTURE.md` for the directional map and `CORE_CONCEPTS_MAP.md` for ownership navigation.

## Protected-path rule

`implementation/`, `mcp-server/`, schemas, tests, CI, Docker/environment material and other protected paths require their normal review discipline. A documentation decision to refuse a dependency or select a client direction does not authorize protected implementation changes, installation or activation.

## Next reconciliation

The next bounded implementation qualification for generated UI is the Hermes Desktop host seam: reuse only the protocol guard/render observations still relevant from closed PR #882, verify the exact current Hermes pin and Desktop plugin/transcript contribution contract, and prove that generated UI produces only bounded intent until the existing effect gate admits more.

Do not create a replacement chat frontend, second Cockpit UI owner, DMS, observer, registry or runtime merely to preserve historical shape.

## Final rule

```text
State what exists.
State what is selected.
State what is only historical provenance.
Do not confuse a remote connection, rendered UI or green qualification lab with production adoption or authorization.
```
