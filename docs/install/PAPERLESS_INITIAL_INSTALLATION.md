# Paperless-ngx — Initial Installation

Status: candidate operator artifact — documented non-implemented.
Boundary profile: candidate_support_note.

This runbook places Paperless-ngx in the initial reference deployment as the external document source-management runtime selected by `COMMON_INSTALLATION_BASELINE.md`.

It documents an operator installation. It does not install Paperless, create secrets, authorize real-dossier data, activate a Hermes binding, approve a capability or make Pantheon a runtime.

```text
Cockpit / OpenWebUI exposes document views.
Hermes executes governed document operations.
Paperless stores and processes document sources externally.
Pantheon governs consequential status and gates.
The human installs, adopts and activates.
```

## 1. Required posture

Before installation, record:

```text
Paperless reviewed image tag or digest
PostgreSQL placement and dedicated role/database
Valkey/broker placement
persistent data path
persistent media path
export/backup path
consume path if enabled
secret owner
API token owner
network exposure
backup target
rollback target
```

Do not use an unreviewed floating image reference in the retained deployment record.

```text
image_available != update_authorized
installed != approved
reachable != healthy
healthy != safe
```

## 2. Network topology

Reference posture:

```text
ai-net
├── paperless:8000
├── paperless-broker:6379
├── PostgreSQL / paperless_app
├── hermes:8642
├── openwebui
├── pantheon-policy-api
└── pantheon-mvp cockpit adapter
```

Paperless, its database and its broker are private services. During bootstrap a loopback-only Paperless port may be exposed for local administration:

```text
127.0.0.1:8000 -> paperless:8000
```

Public Internet exposure is not an initial default.

The broker is a Paperless implementation dependency only:

```text
paperless broker != Pantheon queue
paperless scheduler != Pantheon scheduler
paperless task != Hermes Task Contract
```

## 3. PostgreSQL separation

Paperless may use either:

1. a dedicated PostgreSQL container/instance; or
2. the common PostgreSQL service with a dedicated database and role.

The reference shared-server layout is:

```text
openwebui_app     -> role openwebui_app
paperless_app     -> role paperless_app
pantheon_knowledge -> role pantheon_knowledge
```

No role receives administrative access to another application's database.

Illustrative operator SQL, adapted to the actual secret manager and PostgreSQL version:

```sql
CREATE ROLE paperless_app LOGIN PASSWORD '<external-secret>';
CREATE DATABASE paperless_app OWNER paperless_app;
```

The password is never committed to Pantheon Next or `pantheon-mvp`.

## 4. Paperless service configuration

Use a reviewed pinned image or digest:

```text
PAPERLESS_IMAGE=ghcr.io/paperless-ngx/paperless-ngx:<reviewed-pin>
```

Required runtime configuration includes the equivalent of:

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

Set `PAPERLESS_URL` only when the reviewed reverse-proxy/public origin is known.

Initial posture deliberately leaves these unconfigured:

```text
remote OCR providers
Paperless AI / external LLM providers
Paperless vector/RAG provider integrations
unreviewed outgoing webhooks
```

Local Paperless OCR is derived processing. It does not replace the original and does not establish professional truth.

## 5. Persistent storage

Persist at minimum the Paperless equivalents of:

```text
data
media
export
consume, when used
```

`media` contains the retained document files and must be part of backup/restore planning. Database-only backup is insufficient for a document-store recovery plan.

The operator records the actual host/NAS paths. Pantheon does not hard-code or own those paths.

## 6. Start Paperless

The private deployment layer owns the actual Compose/Portainer stack.

The external `ifanjuang/pantheon-mvp` repository carries an executable candidate profile named `paperless` for integration testing. It requires explicit external values for:

```text
PAPERLESS_IMAGE
PAPERLESS_DB_PASSWORD
PAPERLESS_SECRET_KEY
```

Illustrative invocation in that candidate repository:

```bash
export PAPERLESS_IMAGE='ghcr.io/paperless-ngx/paperless-ngx:<reviewed-pin>'
export PAPERLESS_DB_PASSWORD='<external-secret>'
export PAPERLESS_SECRET_KEY='<external-secret>'
docker compose --profile paperless up -d paperless
```

That profile is a reference executable candidate, not the canonical private production stack.

## 7. Bootstrap administrator and API token

Create the initial Paperless administrator using the reviewed native Paperless procedure.

Then create a dedicated API identity/token for the Pantheon/Hermes document binding. Prefer a scoped non-human account whose permissions are limited to the document corpus the runtime is allowed to access.

Paperless supports token authentication through:

```text
Authorization: Token <token>
```

The token is stored in the external runtime secret store and injected as:

```text
PAPERLESS_API_URL=http://paperless:8000
PAPERLESS_API_TOKEN=<external-secret-reference>
```

Pantheon governance records may retain the secret reference/owner, never the raw token.

## 8. Read-only acceptance probe

Before enabling any document mutation, prove the read path:

```bash
curl -fsS \
  -H "Authorization: Token $PAPERLESS_API_TOKEN" \
  "http://paperless:8000/api/documents/?page_size=1"
```

Record:

```text
observed Paperless version
image digest/tag
probe timestamp
network path
API identity
result
```

A successful request establishes reachability only.

```text
probe_success != health
health != safe
```

## 9. Exact-version Source Capture acceptance

The governed adapter must not create an immutable Source Capture from a mutable `latest` pointer alone.

For one synthetic document:

```text
1. upload/import the synthetic file into Paperless;
2. resolve the resulting document id;
3. select an exact Paperless version id;
4. download that exact version;
5. compute SHA-256;
6. retain a storage reference:
   paperless://document/<document_id>/version/<version_id>
7. compare byte count and digest after a second retrieval;
8. materialize temporarily for Docling, then remove the temporary file.
```

Expected boundary:

```text
Paperless exact version -> Source Capture
Source Capture -> Docling/OCR derived representation
Derived representation != original
```

## 10. Hermes / cockpit binding

The executable candidate adapter lives in `ifanjuang/pantheon-mvp` as:

```text
mvp_vertical.paperless.PaperlessClient
```

Initial admitted read operations:

```text
list/search documents
get document metadata
get exact version
retrieve original/preview
observe Paperless task state
```

Consequential operations use the existing policy chokepoint:

```text
upload document
update classification metadata
future delete/version replacement/permission mutation
```

Current bounded mutation helpers:

```text
governed_post_document
governed_update_document_metadata
```

They require the Pantheon preflight + valid human decision before the external effect executes.

## 11. Classification mirror

Hermes may propose a Classification Candidate such as:

```text
project
phase
document_type
subject
Knowledge destination
```

After the required gate, selected operational fields may be mirrored into Paperless tags/custom fields for search and navigation.

The canonical project relation remains outside Paperless:

```text
Document Record
-> Project Document Link
-> project / phase relation
```

Therefore:

```text
Paperless tag != Project Document Link
Paperless custom field != canonical project truth
Paperless document != Knowledge Item
```

## 12. Docling relationship

Paperless is not the preferred structured-analysis binding.

```text
Paperless
  source bytes
  versions
  local/basic OCR
  operational metadata
  native search

Docling
  structured extraction
  Markdown
  tables
  layout
  derivation provenance
```

For a selected source, Hermes may obtain the exact Paperless version and materialize it temporarily for Docling. The temporary path is never stored as the canonical source locator.

## 13. Backup and restore acceptance

Before real-dossier activation, prove a restore in a non-production target.

The backup set must cover the selected deployment's:

```text
Paperless PostgreSQL database
Paperless media/source files
Paperless data/configuration state as required by the selected version
export/archive material when relied upon for recovery
secret references and operator recovery procedure, without copying raw secrets into Pantheon
```

Record restoration evidence separately from runtime health.

```text
backup_exists != restore_proven
restore_proven != production_authorized
```

## 14. Update posture

Update detection is allowed. Automatic update is not.

Before changing Paperless version:

```text
record current image digest/tag
record target image digest/tag
read upstream migration/release notes
verify database backup
verify media/data backup
record rollback target
perform update through operator tooling
run read-only probe
run exact-version capture test
run synthetic upload/task test when mutation binding is in scope
```

```text
update_available != update_authorized
migration_success != professional_validation
```

## 15. Rollback

A rollback plan must name:

```text
previous Paperless image
compatible database restore point
media/data restore point
broker/data handling if applicable
API binding disable action
Cockpit/Hermes fail-closed posture
```

If Paperless becomes unavailable:

- existing Pantheon records and Source Capture references remain records of what was previously observed;
- new Paperless-backed source access fails unavailable;
- the runtime must not silently substitute another backing store;
- consequential effects remain blocked rather than bypassing the missing source runtime.

## 16. Activation gates

Installation acceptance establishes only that the component is present and observable.

Separate human decisions remain required for:

```text
Paperless binding activation
project/dossier scope
real client documents
classification writes
Knowledge publication
remote OCR or AI/provider features
public/reverse-proxy exposure
production adoption
```

Final status after completing only this runbook:

```text
installed          -> may be true after operator execution
healthy            -> requires observed checks
approved           -> not implied
binding activated  -> not implied
real-dossier use   -> not implied
production adopted -> not implied
```
