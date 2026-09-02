# Google Drive read qualification lab

Issue: #929

Status: qualification-only. No provider selected, installed or activated.

## Purpose

Exercise the existing `google_drive_read` capability behind one narrow read-only contract while comparing direct Google Drive API request semantics with Nango-proxied request semantics.

The lab now has two deliberately separate slices:

1. provider listing and bounded metadata normalization;
2. exact content download/export planning, byte hashing and preparation of a Source-intake draft.

Neither slice admits or persists a Pantheon Source.

```text
Google Drive API or Nango proxy
        -> explicit folder/drive scope
        -> provider response
        -> bounded read candidate + stable remote locator
        -> exact download or reviewed Google-native export
        -> SHA-256 of the bytes actually returned
        -> Source-intake draft compatible with existing owner fields
        -> [STOP: governance fields + Source admission remain external to this lab]
```

## Invariants

- explicit folder scope before list;
- Shared Drive id preserved when supplied;
- out-of-scope provider material fails closed;
- trashed material fails closed;
- `incompleteSearch=true` fails closed;
- no provider metadata is promoted to a Pantheon `source_digest`;
- `md5Checksum` is retained only as provider metadata when present;
- SHA-256 is computed only from the exact downloaded/exported bytes;
- changing provider metadata without changing bytes does not change that content SHA-256;
- changing bytes changes SHA-256 even when provider metadata/version does not;
- Google-native files use an explicit reviewed export MIME profile before hashing;
- unsupported Google-native types fail closed rather than choosing an export implicitly;
- the exact export MIME remains visible because an export representation is not the remote document itself;
- no credential value is returned by normalization/materialization;
- no write/upload/delete surface exists;
- direct Google and Nango paths reuse the same Drive resource/request semantics;
- provider success is neither Source admission nor authorization nor Evidence.

## Source-intake boundary

The materialization slice produces only fields already understood by the existing `source_intake.create_source` owner:

```text
source_kind
origin_system
origin_external_ref
raw_source_ref
mime_type
checksum
metadata
```

It deliberately does **not** provide or choose:

```text
source_id
received_at
actor / actor_kind
idempotency_key
Project link
professional currentness
Evidence status
```

Those remain the responsibility of existing Pantheon owners and the authorized caller. The lab never calls `source_intake.create_source`, `store.ingest` or `storage_retention`.

`store.ingest` is intentionally not used as the Drive intake boundary. Current repository review records that its `replace_dossier` parameter is retained for compatibility and is not an active guard. The Drive slice must not acquire a false safety property by composing through that parameter.

## Content identity

For ordinary Drive binaries the materialization plan uses the file media bytes. For reviewed Google-native types it uses an explicit export representation:

```text
Google Docs   -> DOCX
Google Sheets -> XLSX
Google Slides -> PPTX
Google Drawing -> PDF
```

The SHA-256 therefore identifies the exact representation bytes received by Pantheon. It does not claim to be a logical content identity for the remote Google document. `provider_version`, `modified_time`, original MIME type and `export_mime_type` remain separate provenance fields.

## Direct versus Nango

Direct Google API has the smallest runtime dependency but leaves OAuth lifecycle, token refresh, retries, pagination and connector maintenance to the Hermes-side integration.

Nango can centralize OAuth/connection lifecycle and provides Google Drive proxy/sync facilities, but adds an external connector runtime and secret/connection-handle boundary. Passing this lab does not justify selecting it.

The semantic comparison is intentionally neutral: both paths must address the same Google file and use the same bounded query/download/export parameters. The remaining decision gate is operational and must be measured on real authorized connectivity:

```text
OAuth consent + refresh lifecycle
pagination / retry / rate-limit handling
Shared Drive behavior
secret and connection-handle operations
multi-connector reuse
runtime footprint and failure modes
```

Nango should be selected only if that measured connector lifecycle benefit justifies the extra runtime.

## Explicitly deferred

- real OAuth credentials;
- live production Drive download/export;
- Source persistence/admission;
- exact-byte retention in local/NAS storage;
- scheduling, syncs, webhooks or change subscriptions;
- writes/uploads/deletes;
- Hermes tool exposure;
- retrieval changes;
- Nango activation.
