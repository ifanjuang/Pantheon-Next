# Paperless-ngx — Optional Capability Installation

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook applies only when the optional `document_source_management` Capability Slot is selected with preferred binding `paperless_ngx`.

Paperless is not required for governed local/NAS document ingestion. Its absence is a valid baseline state.

It documents an operator installation. It does not install Paperless, create secrets, authorize real-dossier data, activate a Hermes binding, approve a capability or make Pantheon a runtime.

```text
Cockpit / OpenWebUI exposes document views.
Hermes executes governed document operations.
Local/NAS ingestion remains available without Paperless.
Paperless optionally stores and manages document sources externally.
Pantheon governs consequential status and gates.
The human installs, adopts and activates.
```

## 1. Selection gate

Before installation, record:

```text
Capability Slot: document_source_management
selected binding: paperless_ngx
selection owner
reviewed Paperless image tag/digest
PostgreSQL placement and dedicated role/database
Valkey/broker placement
persistent data/media/export/consume paths
secret/API-token owner
network exposure
backup target
rollback target
```

```text
binding selected != installed
installed != approved
reachable != healthy
healthy != safe
```

## 2. Network topology

When selected:

```text
ai-net
├── paperless:8000
├── paperless-broker:6379
├── PostgreSQL / paperless_app
├── paperless-gateway
├── hermes:8642
├── openwebui
└── pantheon-policy-api
```

Paperless, its DB and broker are private services. Loopback bootstrap exposure may be used when reviewed.

```text
paperless broker != Pantheon queue
paperless scheduler != Pantheon scheduler
paperless task != Hermes Task Contract
```

## 3. PostgreSQL separation

Use either a dedicated PostgreSQL instance or a dedicated database/role on a shared server.

```text
openwebui_app       -> OpenWebUI only
paperless_app       -> Paperless only, when selected
pantheon governed DB -> Agency/Knowledge projections
```

No role receives unrestricted administrative access to another application's database.

## 4. Service configuration

Use reviewed pinned references and operator-managed secrets.

Representative runtime configuration:

```text
PAPERLESS_REDIS=redis://paperless-broker:6379
PAPERLESS_DBHOST=<postgres-host>
PAPERLESS_DBENGINE=postgresql
PAPERLESS_DBNAME=paperless_app
PAPERLESS_DBUSER=paperless_app
PAPERLESS_DBPASS=<external-secret>
PAPERLESS_SECRET_KEY=<external-secret>
PAPERLESS_TIME_ZONE=Europe/Paris
PAPERLESS_OCR_LANGUAGE=fra
```

Do not enable by implication:

```text
remote OCR providers
Paperless AI / external LLM providers
Paperless vector/RAG integrations
unreviewed outgoing webhooks
```

## 5. Persistent storage

Persist and back up the Paperless equivalents of:

```text
data
media
export
consume when used
```

Database-only backup is insufficient for a document-store recovery plan.

## 6. Start the optional profile

The external `pantheon-mvp` Phase B compose carries the optional profile:

```text
paperless
```

Provide the profile-specific image, paths and secrets, set:

```text
PANTHEON_PAPERLESS_BINDING_SELECTED=true
```

then start:

```bash
docker compose -f compose.phase-b.yaml --profile paperless up -d
```

Without this profile, core Phase B remains valid and the observer must classify Paperless as `not_selected/not_applicable` rather than degraded.

## 7. Bootstrap API identity

Create the initial administrator using native Paperless tooling, then create a dedicated runtime API identity/token.

Inject only into the server-side gateway:

```text
PAPERLESS_API_URL=http://paperless:8000
PAPERLESS_API_TOKEN=<external-secret-reference>
```

Do not place the raw token in Pantheon doctrine, OpenWebUI or the Hermes skill.

## 8. Read-only acceptance

Before enabling any mutation, prove the bounded read path and retain:

```text
observed Paperless version
image digest/tag
probe timestamp
network path
API identity
result
```

A successful request establishes reachability only.

## 9. Exact-version source capture

For immutable Project Document intake, bind:

```text
Paperless document id
exact version id
original filename
storage reference
content hash
source_ref
```

```text
latest pointer != immutable provenance
Paperless Source Capture != Evidence
```

## 10. Optional Hermes binding

Install/configure `pantheon-document-intake` only when this Paperless capability is selected.

```text
Paperless installed != skill installed
skill installed != binding activated
binding activated != task authorized
```

Current PDP V0 external-effect denial remains authoritative for Paperless mutations.

## 11. Rollback

Rollback may disable the Paperless binding/profile without disabling core local/NAS document ingestion.

```text
Paperless binding -> not_selected
Paperless services -> stopped
persistent Paperless data -> retained for reviewed rollback/restore
local/NAS ingestion -> remains available
```

## Final boundary

```text
Paperless is an optional external DMS/source-management binding.
It improves source management but does not define Pantheon's document-ingestion capability.
Pantheon governs status; Hermes executes; the human decides activation.
```
