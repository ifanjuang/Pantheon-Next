# Data Platform Reconciliation

Status: candidate reconciliation support doctrine  
Scope: boundary reconciliation for data-platform, workflow, knowledge-ingestion and architecture-domain-pack documents  
Runtime status: non-executable

## Purpose

This document reconciles the data-platform candidate layer with the existing Pantheon Next doctrine.

It exists because the data-platform documents introduce strong operational vocabulary: Postgres, Directus, storage, connectors, workflows, OCR, Markdown, vectorization, contact synchronization, finance follow-up and architecture-agency registers.

That vocabulary is useful, but it can create a false impression that Pantheon is becoming an ERP, workflow engine, document runtime or database implementation repository.

This document prevents that drift.

## Core reconciliation

```text
Pantheon does not become the data platform.
Pantheon governs the legitimacy, status, scope, memory and approval rules of data-platform behavior.
```

Operational systems may exist outside the Pantheon repository:

```text
Postgres may record.
Directus or another cockpit may expose and control.
Storage may keep files.
Connectors may retrieve.
Hermes or another execution runtime may execute bounded jobs.
Pantheon governs whether a result, memory, action or workflow is legitimate.
```

## Uploaded Postgres / architecture data-platform analysis

Candidate source reconciled:

```text
Structuration évolutive d’un schéma Postgres et d’une plateforme de données Pantheon Next pour la maîtrise d’œuvre architecturale en France
```

The source is valuable because it correctly frames the architecture-domain data platform as a documentary, contractual and operational proof system rather than a classic agency ERP.

Useful candidate posture:

```text
Postgres records structured facts and governance metadata.
Object storage keeps originals and heavy derivatives.
pgvector supports assisted search over derived text only.
A provenance graph relates document versions, sources, validations, signatures, references and decisions.
```

Pantheon accepts this as a candidate support posture.

Pantheon does not automatically promote the proposed table names, SQL schemas, cockpit views, RLS policies, retention durations or extension set to canonical doctrine.

## Accepted from the data-platform discussion

The following ideas are accepted as candidate support posture:

1. A professional system needs structured registers, not only prompts and retrieval.
2. General memory, agency memory, country memory, project memory, derived memory and validated memory must stay separated.
3. Incoming documents start as candidates.
4. OCR, Markdown conversion, chunking and vectorization are preparation activities, not proof.
5. Workflows should have lifecycle modes: off, draft, test, shadow, assisted, active_guarded and active_durable.
6. A workflow should propose before it executes consequential actions.
7. Domain packs should describe professional method without becoming profession-specific agents.
8. The architecture-agency pack is a deep example, not the system's whole identity.
9. Directus is a cockpit/admin candidate, not a governance authority.
10. Postgres is a record layer candidate, not a decision authority.
11. Original files must remain distinct from OCR, Markdown, preview, embedding and summary derivatives.
12. Retrieval should filter by exact scope before any vector search.
13. A source hierarchy is needed before a retrieved chunk can be used in a professional decision.
14. Phase gates should require evidence packs, not only generated outputs.
15. Reception, reserves, DOE, GPA and signed/contradictory site evidence deserve first-class modelling in an architecture-domain data platform.

## Source authority hierarchy

Accepted as candidate doctrine:

```text
law and regulation
operation contract
approved phase decisions
site evidence
derived documents
semantic search results
```

Governance implication:

```text
A vectorized chunk must never outrank a signed PDF, approved DOE, contradictory PV or approved client decision.
```

This supports `DOCUMENT_INTELLIGENCE.md`:

```text
A document does not become knowledge.
A fragment may support an interpretation candidate.
An interpretation candidate may enter an Evidence Pack Candidate.
An Evidence Pack Candidate may support a governed status.
Only a governed status can support a decision.
```

## Scope hierarchy

Accepted as candidate structure:

```text
global reference knowledge
agency library
project / affair data
external project subset
```

Pantheon rule:

```text
Storage may be shared.
Scope must not be shared.
```

A shared database is acceptable only if the governed perimeter remains compartmentalized.

## Architecture-domain objects worth preserving as candidates

The uploaded analysis identifies useful objects for architecture practice:

```text
CCTP clause
quote
quote line
work contract
order service
meeting minute
action item
reserve
reception PV
DOE pack
DOE item
GPA issue
planning snapshot
risk snapshot
heritage snapshot
signature event
approval event
verification event
admission event
```

Pantheon may govern these objects by:

```text
scope
source authority
status
evidence requirement
approval requirement
memory behavior
external-action boundary
retention posture
```

Pantheon should not assume that their final physical table names are fixed.

## Architecture phase and gate mapping

Accepted as candidate architecture-domain alignment:

```text
DIAG / existing-condition studies
APS
APD
PRO
DCE / ACT
EXE / VISA
DET / OPC
AOR / reception
DOE / reserve closeout / GPA
```

Important nuance:

```text
DCE is an operational container, not necessarily a legal mission element equivalent to PRO or ACT.
```

Pantheon may govern phase gates and evidence expectations.

It must not become the project-management runtime.

## Document metadata candidate core

Accepted as candidate metadata vocabulary:

```text
identity
version
actors / authors
integrity
provenance
legal references
security
retention
```

Typical candidate fields may include:

```text
document_uuid
document_type
deliverable_type
phase_code
affair_id
lot_id
discipline_code
revision_label
supersedes_version_id
approval_state
sha256
storage_uri
source_doc_version_id
norm_ref_ids
signature_level
retention_class
access_scope
```

These are not approved schema fields. They are candidate vocabulary for future schema or adapter design.

## What remains candidate

The following are not yet active implementation decisions:

```text
actual database schema
schema migration format
Directus project structure
Directus permission model
storage layout
connector gateway choice
Gmail intake design
Google Drive integration
Google Contacts synchronization
OCR tool choice
vector store choice
worker runtime
workflow engine
architecture-agency module implementation
concrete SQL schemas
specific table names
specific Postgres extension set
specific partitioning strategy
specific Directus cockpit views
specific retention durations by class
specific signature-level matrix
implementation of RLS policies
implementation of pgvector indexes
implementation of provenance graph tables
```

These must not be treated as implemented or approved.

## Forbidden interpretation

The data-platform documents must not be read as authorizing:

- building a runtime inside Pantheon;
- adding a scheduler or queue to Pantheon;
- making Directus the source of governance truth;
- making Postgres the source of professional truth by itself;
- automatically promoting memory;
- automatically approving workflows;
- sending emails automatically by default;
- filing administrative submissions automatically;
- approving quotes, invoices, change orders or payments automatically;
- converting the architecture-agency pack into a hidden ERP specification;
- hardcoding one agency's habits as universal professional doctrine.

## Placement by layer

| Object or capability | Placement |
|---|---|
| Data-platform doctrine | Pantheon governance docs |
| Actual database tables | implementation layer outside Pantheon, or future schema proposal after approval |
| Schema proposal | Pantheon candidate doctrine or approved `schemas/` change only with explicit review |
| Directus collections | adapter/config outside Pantheon |
| Directus permissions | adapter/config governed by Pantheon rules |
| Data entry UI | exposure surface or admin cockpit |
| Workflow lifecycle rules | Pantheon doctrine |
| Workflow execution | execution runtime |
| Workflow run status | data platform record |
| Workflow approval | Pantheon-governed approval record |
| OCR execution | execution runtime or worker |
| Markdown output | storage plus document metadata |
| Vectorization | retrieval layer under scope rules |
| Evidence selection | governed evidence process |
| Memory promotion | Pantheon memory and approval policy |
| Contact sync | connector / integration layer |
| Local contact role model | data platform record |
| Architecture method | Pantheon domain pack |
| IFJA-specific settings | user or agency configuration, not generic doctrine |
| External sending | human-approved action unless explicitly bounded by policy |

## Relation to active placement doctrine

This reconciliation follows the active placement rule:

```text
A capability belongs where its primary effect belongs.
```

Consequences:

- visibility and correction live in the exposure surface or cockpit;
- execution lives in Hermes or another execution runtime;
- storage lives in storage;
- records live in the data platform;
- legitimacy, scope, memory, approval and acting boundary live in Pantheon.

## Relation to modular domain doctrine

A domain pack is a governed method, not a worker.

The architecture-agency pack may define professional vocabulary, source policy, evidence expectations, risk triggers, output statuses, delivery gates, memory rules, review angles and templates.

It must not:

- execute workflows;
- approve outputs;
- send documents;
- validate professional conclusions;
- promote memory;
- replace the human architect or practitioner.

The pack may parameterize tools and workflows that produce candidates.

## Relation to workflow lifecycle

`WORKFLOW_LIFECYCLE.md` governs the lifecycle of workflow authority.

It does not implement the engine that runs workflows.

A workflow may become durable only after it has produced enough proof of reliable behavior under the relevant approval policy. Even then, external effects remain bounded by the authorization level granted to that workflow.

Default external-action rule:

```text
Preparing is not sending.
Classifying is not filing.
Extracting is not validating.
Generating is not approving.
Recording is not deciding.
```

## Relation to knowledge ingestion

`KNOWLEDGE_INGESTION_AND_MEMORY.md` governs document and knowledge promotion.

It does not implement ingestion.

Key reconciled rule:

```text
The system must know where a document belongs before it uses the document.
```

General knowledge, agency knowledge and project knowledge are separate by default. Project documents may become general knowledge only through explicit promotion, anonymization where needed and human validation.

## Relation to document intelligence and review queue

The uploaded analysis reinforces the need for:

```text
DOCUMENT_INTELLIGENCE.md
REVIEW_QUEUE.md
URGENT_REVIEW_TRIAGE.md
ARCHITECTURE_DOCUMENT_REVIEW.md
```

Data-platform records may produce review items when they reveal:

```text
missing hash
missing source
missing approval
stale version
unclassified retention
possible duplicate
conflicting claim
uncertain source authority
candidate memory
urgent claim without evidence
```

The review queue may expose and prioritize.

It must not apply consequential changes.

## Vector search posture

Accepted:

```text
exact filters first
semantic search second
source references always returned
retrieved chunks are not evidence until selected and represented
```

Forbidden:

```text
cross-affair vector search by default
using embeddings as truth
presenting a chunk without source authority and version
memory promotion from retrieval frequency
```

## RLS and scope posture

Accepted as strong candidate:

```text
Scope isolation should not rely only on the application prompt or runtime discipline.
```

Implementation candidate:

```text
Row-Level Security or equivalent scoped views / gateways.
```

Pantheon rule:

```text
The execution runtime does not ask storage what exists.
Pantheon tells the execution runtime what it is allowed to ask.
Storage returns only what the task scope permits.
```

## First implementation candidates

The following are candidate slices only. They are not approved implementation work.

### Candidate slice A — knowledge ingestion

Low to medium consequence if bounded correctly.

Focus:

- document drop;
- original file record;
- OCR / text extraction candidate;
- Markdown candidate;
- general/project/mixed classification;
- similarity check;
- scoped indexing proposal.

Why first:

- transversal across domains;
- useful before advanced workflows;
- lower external-action risk;
- clarifies memory boundaries.

### Candidate slice B — quote and invoice intake

Medium to high consequence.

Focus:

- email/attachment classification;
- project attribution proposal;
- contractor/contact proposal;
- quote or invoice candidate record;
- storage path proposal;
- no validation or transmission by default.

### Candidate slice C — site meeting report preparation

Medium consequence.

Focus:

- notes to points;
- previous open-point carryover;
- next-meeting preparation;
- draft report;
- no publication or email by default.

### Candidate slice D — conceptual Postgres core schema

High governance value, but should wait until the placement boundary is stable.

Focus:

- core object families;
- statuses;
- scope fields;
- approval hooks;
- no migration yet.

### Candidate slice E — architecture proof register

High professional value, medium to high consequence.

Focus:

- CCTP / quote / contract relationships;
- meeting minutes, action items and reservations;
- reception PV, DOE and GPA evidence;
- signatures and approvals;
- provenance links;
- no automatic contractual conclusion.

## Required review before implementation

Any implementation work must answer:

1. What layer owns the capability?
2. What object or action can go wrong?
3. Does failure create false truth, wrong memory, unapproved external effect or unauthorized action?
4. What status vocabulary applies?
5. What approval level is required?
6. What evidence is needed?
7. What scope contains the data?
8. What rollback or correction path exists?
9. What remains merely a candidate?
10. Where is the human decision gate?

## Promotion conditions

The data-platform candidate layer may be promoted only if it keeps the Pantheon boundary intact:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

And if it preserves this data-platform boundary:

```text
The database records.
The workflow proposes.
The evidence supports.
The approval validates.
The human decides.
```

## Open decisions

The following require explicit arbitration before promotion:

```text
Which parts become canonical governance doctrine?
Which parts become implementation design outside docs/governance?
Which schema names are allowed to stabilize?
Where should SQL candidates live?
Which cockpit technology is assumed, if any?
Which retention matrix is agency policy versus example?
Which signature-level matrix is acceptable for IFJ / architecture practice?
Which professional objects should be stabilized first?
```

## Recommended next step

Create a separate implementation-design area only after arbitration.

Possible future location, not created by this document:

```text
docs/implementation/data-platform/
```

or:

```text
docs/adapters/data-platform/
```

Until then, this file keeps the uploaded analysis as a candidate reconciliation source.

## Final rule

```text
Govern the data platform from Pantheon.
Do not build the data platform inside Pantheon.
```

## Boundary phrase

```text
The data platform may preserve, relate and expose governed records.
Pantheon governs whether those records can support status, memory, approval or action.
```
