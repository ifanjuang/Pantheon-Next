# Google Drive read qualification lab

Issue: #929

Status: qualification-only. No provider selected, installed or activated.

## Purpose

Exercise the existing `google_drive_read` capability behind one narrow read-only contract while comparing direct Google Drive API request semantics with Nango-proxied request semantics.

This lab does not ingest into Pantheon Sources. It produces provider read candidates only.

```text
Google Drive API or Nango proxy
        -> explicit folder/drive scope
        -> provider response
        -> this normalizer
        -> read candidates with stable remote locator
        -> later content fetch/export + hash
        -> existing Pantheon Source intake/currentness owners
```

## Invariants

- explicit folder scope before list;
- Shared Drive id preserved when supplied;
- out-of-scope provider material fails closed;
- trashed material fails closed;
- `incompleteSearch=true` fails closed;
- no provider metadata is promoted to a Pantheon `source_digest`;
- `md5Checksum` is retained only as provider metadata when present;
- actual content/export must still be hashed before Source admission;
- no credential value is returned by normalization;
- no write/upload/delete surface exists;
- direct Google and Nango paths reuse the same Drive API query semantics;
- provider success is neither Source admission nor authorization nor Evidence.

## Direct versus Nango

Direct Google API has the smallest runtime dependency but leaves OAuth lifecycle, token refresh, retries, pagination and connector maintenance to the Hermes-side integration.

Nango can centralize OAuth/connection lifecycle and provides Google Drive proxy/sync facilities, but adds an external connector runtime and secret/connection-handle boundary. Passing this lab does not justify selecting it.

The comparison gate is operational, not semantic: both paths must preserve the same Google file/folder/drive identity and the same Pantheon scope boundary. Nango should be selected only if measured connector lifecycle burden justifies the extra runtime.

## Explicitly deferred

- real OAuth credentials;
- production Drive downloads/Google-native export;
- Source persistence;
- scheduling, syncs, webhooks or change subscriptions;
- writes/uploads/deletes;
- Hermes tool exposure;
- retrieval changes;
- Nango activation.
