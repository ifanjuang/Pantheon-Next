# AI intervention trace — Optional Paperless Compose overlay alignment

Date: 2026-07-26
Status: validation-only trace
Boundary profile: validation_only_trace.

## Human direction

The repository owner confirmed that Paperless should remain optional and asked to continue implementation on that basis.

The active repository doctrine already classified:

```text
document_ingestion              core capability
governed local/NAS source       default supported path
document_source_management      optional Capability Slot
preferred binding               paperless_ngx
```

The work therefore did not reopen that governance decision. It hardened the external deployment mechanism and reconciled Pantheon Next with the merged implementation.

## External implementation state rechecked

Before the follow-up, `pantheon-mvp#84` had already merged optional Paperless semantics using a Compose profile.

A deployment concern remained: Paperless-only `${VAR:?…}` expressions still lived in the core Compose file. Because required Compose interpolation belongs to file/model processing rather than Pantheon governance, the safer separation is a distinct optional overlay whose Paperless-only variables are absent from the core file entirely.

External hardening was implemented and merged as:

```text
pantheon-mvp #85
merge: 35a112d03d0ffe2ea848abd4976ba7692ce0927a
```

## External runtime result

```text
compose.phase-b.yaml
  core only
  no Paperless service
  no Paperless-only required image/path/secret variable
  observer defaults to governed_local_source

compose.paperless.yaml
  optional Paperless DB/broker/runtime/gateway
  bounded Hermes Paperless configuration
  observer binding override -> paperless_ngx
```

Observer binding semantics became explicit:

```text
MVP_DOCUMENT_SOURCE_BINDING=governed_local_source
  -> no Paperless probe
  -> Paperless not_selected / not_applicable

MVP_DOCUMENT_SOURCE_BINDING=paperless_ngx
  -> bounded Paperless gateway probe

unsupported binding
  -> unsupported_binding / not_observed
```

The full external CI passed before merge.

## Pantheon placement

Pantheon Next governs only the qualification of this external state:

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
overlay loaded != binding activated
Paperless installed != approved
```

Hermes continues to execute. OpenWebUI continues to expose. The human/operator selects the optional DMS binding and approves consequential activation/use.

Pantheon does not become a Compose engine, installer, Portainer controller or runtime.

## Target status

```text
optional capability doctrine          merged previously
external separate Compose overlay     merged in pantheon-mvp #85
Next doctrine/runbook reconciliation  candidate in this branch
target Paperless installation         not established
target local/NAS ingestion proof      not established
target Paperless exact-version proof  not run
activation                            not authorized
real-dossier use                      not authorized
production adoption                   not decided
```

This trace creates no authority and records no target deployment claim.
