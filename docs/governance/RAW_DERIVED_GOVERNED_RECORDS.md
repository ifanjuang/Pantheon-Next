# Raw, Derived and Governed Records

Status: candidate data-platform support doctrine  
Scope: separation between raw content, derived content, governed records, retrieval objects, provenance objects, evidence and approvals  
Runtime status: non-executable

## Purpose

This document answers a practical data-platform question:

```text
If Postgres cannot contain every subtlety of documents and discussions, where do those subtleties live?
```

It defines a layered content model for Pantheon-compatible professional systems.

It does not implement storage, OCR, Markdown conversion, vector search, graph storage, database tables, Directus collections or workflow execution.

## Core rule

```text
The database does not hold the whole knowledge.
It holds the governed handles: identity, scope, status, provenance, links, extracted facts, approvals and decisions.
```

Postgres or any equivalent database should not become a dumping ground for every document, transcript, image, email body, OCR artifact, embedding, discussion nuance or professional interpretation.

## Layer model

A professional system should distinguish at least seven layers.

```text
1. Raw content
2. Derived content
3. Governed records
4. Retrieval objects
5. Provenance objects
6. Evidence objects
7. Approval and decision records
```

Each layer has a different job.

## 1. Raw content

Raw content is the material source.

Examples:

```text
PDF quote
PDF invoice
PDF site report
email body
email attachment
photo
plan
scan
voice transcript
chat transcript
contract
CCTP
CERFA PDF
public API response payload
```

Raw content should usually live in storage:

```text
NAS
local folder
Google Drive
SFTP
S3-compatible storage
OpenWebUI upload area
secure document repository
```

The database records raw content identity, not the whole raw content by default.

Candidate governed handles:

```text
storage_object_id
original_filename
storage_provider
path_or_uri
hash
mime_type
source_system
confidentiality
project_id or scope_id
created_at
imported_at
status
```

## 2. Derived content

Derived content is produced from raw content.

Examples:

```text
OCR text
extracted text
Markdown conversion
cleaned transcript
summary
structured metadata candidate
table extraction
image description
chunk set
embedding payload reference
```

Derived content is useful, but it is not the source itself and not proof by itself.

Core rule:

```text
OCR is not truth.
Markdown is not the original.
Summary is not evidence.
Embedding is not memory.
```

Derived content should keep links back to raw content:

```text
source_document_id
source_hash
source_page
source_region
extraction_method
extraction_version
confidence
created_at
status
```

## 3. Governed records

Governed records are structured database records used for control, review and action.

Examples:

```text
project
organization
contact
document record
message record
quote record
invoice record
site meeting
site point
task
project fact
workflow run
action proposal
memory candidate
approval record
```

Governed records belong in Postgres or another structured record layer.

They should carry:

```text
identity
scope
status
source reference
owner or responsible role
created_at
updated_at
confidence or review state
approval state where applicable
```

The database should prefer explicit, reviewable records over large unstructured blobs.

## 4. Retrieval objects

Retrieval objects make content findable.

Examples:

```text
full-text index
vector index
chunk metadata
search index
entity index
keyword index
```

Retrieval is not proof.

Core rule:

```text
Retrieved means found.
Found does not mean true.
True enough for action requires governed evidence and approval.
```

Retrieval objects must inherit scope and confidentiality from their source.

Minimum metadata:

```text
document_id
chunk_id
scope_id
project_id
library_id
confidentiality
source_page
heading_path
status
validity
```

A project document must not be retrievable for another project unless explicitly promoted under a governed memory policy.

## 5. Provenance objects

Provenance objects connect sources, derived content, claims, decisions and outputs.

Examples:

```text
this email produced this quote
this quote belongs to this project
this quote line relates to this CCTP article
this CCTP article is missing from this quote
this missing item produced this action proposal
this action proposal was reviewed in this meeting
this meeting produced this decision
this decision produced this change order
this change order modified this budget
```

Provenance may be represented as relational links, a graph, or both.

But provenance is still not proof by itself.

Core rule:

```text
A relation explains connection.
It does not validate the connected claim.
```

## 6. Evidence objects

Evidence objects are selected, bounded and reviewable support for a claim or output.

Examples:

```text
Evidence Candidate
Evidence Item
Evidence Pack Candidate
Evidence Pack
contradiction candidate
source excerpt with page reference
source comparison table
```

Evidence objects should answer:

```text
What is claimed?
Which source supports it?
Which passage supports it?
What is the status of the source?
What assumptions remain?
What contradictions exist?
What approval is required before use?
```

A retrieved chunk becomes useful only when selected and represented as evidence.

## 7. Approval and decision records

Approval and decision records are the point where responsibility is attached.

Examples:

```text
approve project attribution
approve memory promotion
approve quote classification
approve site report publication
approve email sending
approve invoice analysis
approve form export
reject source
revoke previous validation
```

These records belong in the governed record layer.

Core rule:

```text
Preparing is not approving.
Recording is not deciding.
Approval is a distinct record.
```

## Where subtleties live

Subtleties do not live in one place.

| Subtlety type | Best home |
|---|---|
| exact legal or professional wording | raw document + Markdown derivative |
| document layout nuance | raw document + layout metadata |
| long discussion context | transcript Markdown + summary |
| important meeting nuance | meeting notes + selected points |
| project-specific fact | governed project fact |
| reusable method | knowledge document or memory candidate |
| semantic similarity | retrieval index |
| causal relationship | provenance graph or relational links |
| proof for a claim | Evidence Pack |
| professional decision | approval / decision record |

## Conversation handling

A conversation should not be flattened into Postgres.

Use three levels:

```text
1. Raw transcript
   Full conversation, chat export, meeting transcript or email thread.

2. Structured summary
   Decisions, open questions, assumptions, risks, candidate actions, unresolved tensions.

3. Governed extracts
   Project facts, tasks, memory candidates, workflow build requests, decisions or schema-change proposals.
```

Only the third level becomes structured governed records.

The raw conversation and structured summary remain available as document content.

## Document handling example

Incoming contractor quote:

```text
raw content
  PDF quote stored in project storage.

derived content
  OCR text, Markdown conversion, extracted tables, chunks.

governed records
  document record, quote candidate, contractor link, lot candidate, amount candidate.

retrieval objects
  full-text index and scoped vector chunks.

provenance objects
  email -> attachment -> quote -> lot -> CCTP version -> analysis.

evidence objects
  selected CCTP article excerpts and quote-line excerpts.

approval records
  human validates project attribution, quote status, comments and any external transmission.
```

## Knowledge handling example

User drops a professional guide:

```text
raw content
  Original PDF stored in knowledge inbox.

derived content
  OCR text, Markdown candidate, summary, chunks.

governed records
  knowledge document candidate, library candidate, scope classification, similarity check.

retrieval objects
  scoped index entries only after approval.

provenance objects
  original PDF -> Markdown version -> active guide version.

evidence objects
  selected excerpts only when used for a task.

approval records
  human validates whether it is general knowledge, agency knowledge, project-only or rejected.
```

## What Postgres should contain

Postgres should contain:

```text
identities
statuses
scopes
links
metadata
facts
candidates
approvals
decisions
provenance edges if relational
workflow states
action proposals
audit events
```

Postgres should generally not contain, by default:

```text
large binary files
complete PDF payloads
full image payloads
raw embeddings as primary knowledge
unbounded chat histories
unreviewed memory dumps
all OCR text without document-layer purpose
all semantic nuance flattened into columns
```

Exceptions may exist for small payloads or controlled local deployments, but the governance model should not assume the database holds everything.

## Directus posture

Directus or another cockpit may expose governed records and selected derived content.

It should help the user:

```text
inspect metadata
correct classifications
review extracted facts
open raw documents
compare Markdown derivatives
approve or reject candidates
navigate provenance links
see evidence status
```

It should not imply that a database row is professional truth.

## Relation to RAG

RAG should be understood as retrieval support, not memory authority.

```text
RAG retrieves possible support.
Evidence selection turns support into a candidate proof chain.
Approval decides whether the proof chain can support delivery or action.
```

## Boundary with implementation

This document does not require one specific technology.

Possible implementations may use:

```text
Postgres for governed records
file storage for raw content
Markdown files for derived text
Meilisearch / PostgreSQL full-text / OpenSearch for text search
pgvector / Qdrant / Weaviate / other vector stores for retrieval
Neo4j / RDF / relational edges for provenance
Directus for cockpit exposure
Hermes / workers for extraction and conversion
```

These are implementation choices, not Pantheon doctrine.

## Operating principle

```text
Do not ask one layer to do every job.
```

More explicitly:

```text
Files preserve materiality.
Markdown preserves readability.
Indexes preserve findability.
Graphs preserve relationships.
Postgres preserves governed handles.
Evidence Packs preserve proof chains.
Approvals preserve responsibility.
```
