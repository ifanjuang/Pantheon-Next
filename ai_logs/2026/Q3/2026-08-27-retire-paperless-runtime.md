# Retire Paperless runtime and document observer path

Date: 2026-08-27
Issue: #666
Change level: semantic

## Context

The active architecture no longer selects Paperless as a document-source runtime. The repository already owns generic source intake and local/NAS source identity independently of Paperless. The dedicated document runtime observer also has no demonstrated business consumer and exists primarily to aggregate the Paperless/PDP/Docling/Hermes runtime path.

## Change

- remove Paperless client, gateway, ingestion binding, compose overlay, catalog resource and binding migration;
- remove Paperless services/profile from the base implementation Compose so deleted gateway modules are not still advertised as executable;
- remove Paperless-specific Hermes document-intake skill rather than preserve a generic name over product-specific `/v1/paperless/*` calls;
- remove the dedicated document runtime observer/network observer, synthetic check, fixtures and route-specific doctrine;
- remove the observer service from the Phase B compose topology;
- remove temporary Phase B/Paperless operator pointers whose own convergence notes said to delete them after protected compatibility removal;
- convert the monorepo-placement regression from requiring Paperless/observer artifacts to requiring their continued absence and the survival of generic owners;
- allow a catalogued capability to remain intentionally unbound instead of forcing a preferred product resource;
- leave `document_source_management` provider-agnostic with no preferred binding after Paperless retirement;
- reconcile `WHAT_RUNS.md` so executable Cockpit/Card rendering and the completed Paperless retirement are described as current repository state;
- preserve generic source intake, local/NAS source handling, Docling, PostgreSQL/pgvector, PDP and the generic `runtime_observation` envelope;
- preserve the rule that source capture is not Evidence and execution/runtime success is not authorization.

## Authority

This change removes optional adapters and projections; it does not transfer document authority to Obsidian, Hindsight, Hermes, Docling or any other provider. Source identity and governed admission remain with Pantheon owners.

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder/path != governed identity
provider selected != authority transfer
source capture != Evidence
green CI != adoption
```
