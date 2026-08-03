# Stable Paperless resource routes

Date: 2026-08-03

Status: architecture convergence validation trace.

## Scope

The bounded Paperless gateway is an optional and replaceable binding for `document_source_management`.

Its internal routes now make that binding ownership explicit:

```text
GET  /resources/paperless/documents
GET  /resources/paperless/documents/{document_id}
GET  /resources/paperless/documents/{document_id}/capture
GET  /resources/paperless/tasks/{task_id}
POST /resources/paperless/intakes
POST /resources/paperless/documents/{document_id}/metadata
```

The former `/v1/paperless/...` routes are removed in the same change. No aliases are retained.

## Why `resources/paperless`

Paperless is not the owner of Pantheon Documents, Knowledge, Evidence or business classification.

```text
Paperless document != Pantheon Document
Paperless metadata != canonical business classification
Paperless task success != Evidence
Paperless selected != dependency adopted globally
```

The route family therefore exposes the selected external resource binding instead of claiming a generic `/documents` authority.

## Preserved read boundary

Read operations:

- keep the Paperless token server-side;
- accept only configured Cockpit/Hermes read keys;
- strip derived OCR content from the bounded document projection;
- expose search scores only as retrieval metadata;
- mark business classification, Knowledge, Evidence and approval authority as false.

## Preserved exact-capture boundary

The capture route returns identity and provenance metadata, not source bytes:

```text
paperless document id
exact version id
source_ref
storage_reference
content_hash
media type
byte size
```

A capture remains a source candidate and is not automatically Knowledge or Evidence.

## Preserved consequential-effect boundary

Intake and metadata mutation still require:

```text
Hermes credential
Task Contract
exact source in declared scope
approval ceiling
expected object identity
expected digest
human decision payload
Pantheon policy preflight
PEP binding before effect
```

Metadata mutation rechecks that the exact capture and live source bytes have not changed before applying the root-document patch.

```text
captured != still current
matching decision != reusable after source change
write success != professional validation
```

## Result boundaries

Project intake continues to return:

```text
knowledge_published = false
evidence_admitted = false
```

Metadata mutation continues to return:

```text
canonical_business_classification_changed = false
```

## Baseline reduction

```text
generation-named active artifacts:     0
internal versioned route files:        4 -> 3
internal versioned route declarations: 20 -> 14
```

## Boundaries

This change does not install or select Paperless, expose its token, broaden its scope, approve a binding, authorize a task, create Evidence, promote Knowledge or memory, schedule work, route providers or turn Pantheon into a document runtime.

## Deferred slice

Only Hermes-facing route debt remains:

```text
hermes_handoff_api.py
hermes_execution_api.py
hermes_project_change_candidate_api.py
```
