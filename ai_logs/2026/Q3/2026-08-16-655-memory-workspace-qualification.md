# #655 memory/workspace qualification — convergence record

Date: 2026-08-16

Status: qualification record and handoff. This file records observed results and explicit decisions from Pantheon-Next #655; it does not install, activate or authorize a runtime.

## Objective

Bring the five-day memory/workspace qualification back into the repository so the durable record does not depend on GitHub issue comments alone, reconcile doctrine with the tested deployment, and separate future work from the completed Hindsight/TencentDB comparison.

## Repository state checked before this intervention

`Pantheon-Next` main was at `ce4926a6c60787611c3ec2a007bc612d0600ecf6` (2026-08-12, merge #656). The only newer open PR observed was #657 and it is landing-page work; no current main change altered the memory/workspace authority model.

`pantheon-mvp` main was at `acb6ef0264712d124b58a68c89bf7248c7d21020` (2026-08-11, #314). The existing O3 Hindsight/Obsidian/Hermes lab still pins Hindsight `0.8.5` as a historical reproducibility fixture.

The canonical binding record remains:

```text
catalog/bindings/external-runtime-memory-unbound.yaml
metadata.status = unbound
spec.binding_role = unbound
dependency_adopted = false
installation_authorized = false
activation_authorized = false
task_authorized = false
```

No new Capability Slot is justified by the observed work.

## Observed Hindsight / Synology result

The Synology is the persistent service host. Hermes and Hindsight are containerized there; the Windows workstation carries native Obsidian clients and the GPU workstation remains the candidate host for heavy inference/document processing.

Hindsight was migrated from `0.9.0` to `0.9.1`. The running API reported `api_version=0.9.1`; persistence and post-migration recall were verified. A cold pre-migration backup plus checksum exists. The inputs needed for rollback were captured, but a full restore drill has **not** been executed, so `restore tested` must not be claimed.

Durable banks qualified in the live topology are:

```text
ifja-agency
ifja-projects
ifja-sandbox
```

`ifja-personal` remains a possible future trust domain from the earlier workspace model but was not created or qualified in this campaign.

Synthetic bank-isolation tests passed: each marker was retrieved only from its own bank and all synthetic markers were removed afterward.

```text
bank isolation != authorization
stored != validated
retrieved != truth
memory != Evidence
```

## Observed Obsidian result

The current durable vault/bank mapping qualified on Windows is:

```text
IFJA-Agence   -> ifja-agency
IFJA-Projets  -> ifja-projects
IFJA-Sandbox  -> ifja-sandbox
```

The official `vectorize-io/hindsight-obsidian` code/assets used in the current qualification correspond to release `0.2.1`. The upstream `0.2.1` release manifest still reports `0.2.0`; this was observed as a packaging/version-display inconsistency, not as evidence that the installed code remained `0.2.0`.

Create/edit/rename/delete/reconcile behavior was exercised. Document listing was used for deterministic deletion verification because Hindsight recall extracts semantic facts and is not a raw-source echo.

For the durable vaults, conversation retention remains off and prefixed document IDs remain enabled. Obsidian/Markdown remains the intentional source; Hindsight remains a derived memory/index.

## Observed Hermes -> Hindsight change

The current live integration no longer relies only on the historical `local_external` memory-provider path. Hermes `v2026.8.3` was also qualified against Hindsight through three single-bank MCP endpoints:

```text
hindsight-sandbox  -> ifja-sandbox
hindsight-agency   -> ifja-agency
hindsight-projects -> ifja-projects
```

Tool filtering was verified in the Hermes release code and at runtime. `agency` is read-only from Hermes. `projects` was technically tested with `sync_retain`; a synthetic marker written by Hermes appeared only in `ifja-projects` and was then deleted.

That write test proves routing only:

```text
runtime write success != ingestion authority
bank isolation != authorization
```

The durable posture is therefore corrected to **read-only Hermes access until one ingestion authority per bank is explicitly decided**. The live `sync_retain` exposure is operational debt and is tracked in #659; its prior synthetic proof remains useful compatibility evidence but is not authorization for durable writes.

## Security / exposure status

The Hindsight MCP/API path tested in #655 had no authentication configured and the service ports were published on the LAN. This was acceptable for bounded synthetic qualification but is not sufficient evidence for broader professional-data use.

Because durable agency/project vaults now exist, exposure/authentication is a blocker rather than a later enhancement. #659 owns this hardening together with Portainer pin reconciliation, ingestion-authority choice, removal of the durable Hermes write surface, outage/recovery testing and an isolated full restore drill.

## TencentDB decision

TencentDB Agent Memory is **deferred/rejected for the current Hermes topology**, not left as an unresolved co-equal candidate for activation.

The campaign observed useful pieces — Gateway/Core startup, L0/L1/L2 behavior at synthetic scale, persistence, outage detection and passive recovery — but the tested combination failed on state-consistency properties that matter more than feature breadth:

- the prefetch circuit-breaker path recorded success after complete recall failures, leaving failure count at zero and the breaker closed;
- watchdog recovery failure left `_gateway_available=True`;
- L3/persona failure could leave a written persona and an advanced checkpoint despite reporting failure;
- Hermes did not provide TencentDB team/agent/user tenancy identifiers, causing live activation to collapse to `default/default/default` and lose the isolation dimensions qualified independently;
- persisted non-secret Hermes provider configuration and the TencentDB plugin environment-variable loader did not align cleanly.

Classification:

```text
TencentDB current activation = deferred
reason = failure-state consistency + tenancy integration incompatibility
external_runtime_memory = unbound
```

This is not a permanent product rejection. Re-evaluation requires a materially changed upstream/downstream state and a new bounded qualification.

## Hybrid Obsidian topology decision

The agreed direction is hybrid; it is not `NAS replaces native Obsidian`.

```text
native Obsidian clients
        │
        │ future Self-hosted LiveSync
        ▼
CouchDB on always-on Synology
        │
        └─ optional Obsidian Web/Docker client
           for always-available/browser access

Obsidian Markdown -> Hindsight derived memory -> Hermes/other bounded clients
Pantheon remains professional authority
```

Native Obsidian remains the preferred everyday/offline client where installed. Obsidian Web/NAS is optional. Multiple independent clients must not write directly into one shared NAS vault directory; synchronization is a separate responsibility.

LiveSync/CouchDB has **not** been qualified yet. The target and test matrix are moved to #660 instead of extending #655.

## Additional future integrations split out

- #661: qualify Rowboat as a bounded, initially read-only Hindsight MCP workspace client. Rowboat's local graph/background agents remain Rowboat context, not Pantheon truth, IFJA canonical memory or a replacement Hermes scheduler.
- #662: qualify Marker as a replaceable `document_structural_analysis` adapter against the existing Docling direction on the same representative corpus. Marker is a converter, not memory or document authority; no second permanent pipeline is justified without comparative gain.

## macOS status

The macOS profile from the original #655 body was not executed in this campaign. The qualified result is therefore Windows + Synology specific. This does not invalidate the observed topology; it means macOS remains explicitly deferred/unqualified rather than being silently implied by the Windows result.

## Authority and governance conclusion

The qualification changes no Pantheon owner:

```text
Obsidian Markdown != Pantheon governed state
Hindsight memory != Evidence
Hindsight recall != truth
Hermes tool availability != task authorization
MCP routing success != dependency adoption
CouchDB sync != memory authority
NAS persistence != Pantheon authority
```

`external_runtime_memory` remains `unbound`. Hindsight is an external, replaceable workspace-memory service qualified on the observed Windows+Synology topology, with security/ingestion hardening still required before broader durable use.

## Work split after #655

1. #659 — Hindsight durable deployment hardening: Portainer pin, private/auth posture, one ingestion authority per bank, remove durable Hermes write surface, outage/recovery, isolated restore drill.
2. #660 — Self-hosted LiveSync + CouchDB + optional Obsidian Web qualification.
3. #661 — Rowboat bounded Hindsight client qualification.
4. #662 — Marker vs Docling document-analysis qualification.

A later Cockpit/Hindsight read-only seam remains separate and should be considered only after the workspace/runtime boundaries are stable. It must reuse existing Pantheon concepts before any new slot/schema is proposed.

## Verification / remaining limitations

Completed in #655:

- Synology/Hermes/Hindsight inventory;
- Hindsight `0.9.1` migration and persistence;
- cold backup capture/checksum;
- durable bank creation and strict synthetic isolation;
- official Obsidian source-path qualification and cleanup;
- Hermes single-bank MCP connectivity/tool filtering;
- synthetic Hermes -> projects routing proof and cleanup;
- TencentDB bounded qualification sufficient to defer activation.

Not completed and therefore not claimed:

- Hindsight full restore drill;
- security/auth qualification for broader professional data;
- authoritative Portainer redeploy proof of the `0.9.1` pin;
- one final durable ingestion-authority decision and corresponding live Hermes write-surface removal;
- LiveSync/CouchDB;
- Obsidian Web/NAS;
- macOS profile;
- Rowboat;
- Marker;
- Cockpit read-only workspace projection.

## Closure rule

#655 should close on the observed Hindsight/TencentDB responsibility decision rather than remain open for future providers/platforms. The extracted issues above own the remaining independent work. Closing #655 does not mark #659/#660/#661/#662 complete and does not convert a qualified external service into a Pantheon dependency or production authorization.
