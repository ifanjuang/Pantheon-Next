# Document to Knowledge Slice Contract

Status: candidate support doctrine — schema implemented / external persistence not adopted.
Boundary profile: candidate_support_note.

This document defines the minimum transport-neutral contract linking one project source, one extraction observation, provenance-bearing chunks, one Project Document Card and optional reusable Knowledge publication.

The machine-readable contract is `schemas/document_knowledge_slice.schema.yaml`.

It validates records. It does not parse documents, mount a NAS, write PostgreSQL, synchronize a mobile client, edit Markdown, admit Evidence, promote memory or approve professional truth.

```text
Pantheon Next defines and validates the contract.
The external adapter persists and enforces writes.
Hermes invokes bounded operations.
OpenWebUI exposes exact status.
The human controls consequential reliance and promotion.
```

## Contract boundary

The slice contains six record families:

```text
source_document
extraction
chunk[]
project_document_card
knowledge_publication[]
version_event[]
```

All identifiers are transport-neutral. A repository path, PostgreSQL table, REST route, Docling deployment or editor implementation may bind them externally but does not redefine them.

## Source document

A Source Document preserves:

- stable `document_id`;
- required `parent_project_id`;
- root-relative `source_ref`;
- SHA-256 source digest;
- media type and byte size;
- analysis status;
- optimistic version and timestamps.

The original remains in the caller-controlled source system, normally the NAS. The contract stores a reference, not a copy.

```text
source_ref != permission to read any path
document_id != duplicated original
analysis ready != source true
```

The external adapter must resolve the declared reference below an explicitly supplied root and refuse absolute paths, traversal, undeclared sources and implicit directory crawling.

## Extraction observation

Every extraction records:

- source digest;
- converter and version;
- configuration digest;
- explicit `observation_kind`;
- status, quality flags and timestamp.

The allowed observation kinds are:

```text
direct_text   deterministic reading of a declared text source
fixture       simulated or test-only parser observation
live_parser   response observed from a configured parser binding
```

A test double may prove behavior but must remain `fixture`. A `live_parser` observation means a parser endpoint was actually invoked for this extraction; it does not prove production deployment, extraction quality or professional validity.

## Chunks and provenance

Every chunk carries stable document and extraction references, an ordinal, a text digest and a provenance locator.

At least one of page or structural locator is required. Provenance always repeats the source reference, source digest and extraction identity.

```text
chunk != Evidence
retrievable != true
embedding != provenance
```

## Project Document Card

The Project Document Card is a projection. It requires `parent_project_id`, points to the original reference and records the exact source version it projects.

Its authority block is closed:

```text
is_source: false
is_evidence: false
is_memory: false
```

No UI may widen these values.

## Knowledge publication

Publication creates reusable editorial Knowledge, normally as Markdown. It does not replace or mutate the source document.

Every publication records:

- stable `knowledge_id`;
- source document and chunk references;
- free subject title;
- one of the five selected knowledge families;
- Markdown digest;
- review status;
- version, author and timestamps;
- a closed non-authority block.

Allowed families:

```text
referentiels
responsabilite
methodologie
techniques
reglementations
```

Allowed review states:

```text
generated_unreviewed
needs_review
reviewed
superseded
```

Human validation is not required for initial publication as `generated_unreviewed`. That state must remain visible in search, retrieval, cards and editing.

The authority block is always:

```text
is_evidence: false
is_memory: false
is_doctrine: false
```

Human review is required before destructive replacement, semantic merge, Evidence admission, Registre Probatoire promotion or consequential reliance on contractual, legal, regulatory or safety content.

## Version and idempotency contract

Every material write appends a Version Event with:

- aggregate kind and reference;
- event type;
- actor and actor kind;
- caller-observed `expected_version`;
- `resulting_version`;
- globally unique idempotency key;
- occurrence time.

The external persistence adapter must enforce:

```text
resulting_version = expected_version + 1
current_version = expected_version before write
one idempotency_key = one immutable effect
replay of the same key = same result, no duplicate write
same key with different payload or aggregate = refusal
stale expected_version = refusal, no partial effect
```

JSON Schema validates fields but cannot enforce transactional equality, uniqueness or concurrency. Those guarantees belong to the separately tested adapter.

## Publication and revision effects

The first slice allows these event types:

```text
document_created
extraction_recorded
knowledge_published
knowledge_revised
knowledge_review_status_changed
```

Editing and mobile synchronization must use the same version rules. An offline operation is a proposed write against an exact base version, not permission to overwrite a newer value.

## Required non-equivalences

```text
card != source
card != evidence
knowledge publication != evidence admission
generated_unreviewed != reviewed
reviewed != governed memory
parser success != professional truth
fixture != live parser observation
cached extraction != new source observation
runtime success != approval
offline replay != overwrite permission
```

## First implementation acceptance

An external adapter may be recorded as implementing this contract only when positive and negative tests demonstrate:

- strict source containment;
- explicit parser observation kind;
- per-chunk provenance;
- required Project Document Card parent;
- visible `generated_unreviewed` Knowledge Card;
- idempotent replay;
- stale-write refusal without partial effects;
- refusal of Evidence, memory and doctrine authority claims.

Implementation remains external, not adopted or activated, until separately reconciled.
