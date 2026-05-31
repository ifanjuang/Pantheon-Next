# Knowledge Ingestion and Memory

Status: candidate governance support doctrine  
Scope: document ingestion, OCR, Markdown conversion, vectorization, general memory and project memory  
Runtime status: non-executable

## Purpose

This document defines how Pantheon Next should govern the ingestion of user-provided knowledge and project documents.

It does not implement OCR, vector search, Drive synchronization, OpenWebUI upload handling or contact synchronization. It defines the boundaries and registers those systems should respect.

## Core rule

```text
Every incoming document is a candidate.
Nothing becomes active memory without scope, source and status.
Nothing becomes general knowledge without review.
Nothing becomes project knowledge without project attribution.
```

## Memory layers

The platform should separate memory into layers.

```text
general memory
  Guides, methods, templates, reference notes, domain rules and reusable knowledge.

domain memory
  Profession-specific knowledge such as architecture, contracts, CCTP method, site reporting, finance follow-up or urban planning.

country memory
  Country-specific forms, administrative sources, public APIs, cadastre, risks, heritage and planning references.

agency memory
  User or agency-specific practices, templates, naming rules, preferred methods, model clauses and internal procedures.

project memory
  Documents, facts, decisions, messages, drawings, quotes, invoices, reports and constraints belonging to a specific project.

derived memory
  Extracted claims, observations, OCR text, Markdown conversions, summaries, embeddings and classifications derived from sources.

validated memory
  Candidate memory that a human or policy has accepted as usable within a defined scope.
```

These layers must not be merged into one uncontrolled vector index.

## Document ingestion pipeline

A future ingestion pipeline should follow this pattern:

```text
receive document
  -> store original candidate file
  -> compute hash
  -> extract metadata
  -> classify document type
  -> classify scope: general, project, mixed or unknown
  -> detect project, contact, organization and topic if possible
  -> OCR if needed
  -> extract text
  -> convert to Markdown
  -> preserve source references
  -> compare against existing knowledge
  -> create candidate chunks
  -> vectorize only under the approved scope
  -> wait for validation before activation
```

The original file, converted Markdown and indexed chunks are distinct objects.

## Candidate tables

```text
knowledge_libraries
knowledge_documents
knowledge_document_versions
knowledge_chunks
knowledge_chunk_status
vector_indexes
vector_embeddings
ingestion_jobs
document_processing_outputs
document_similarity_checks
document_scope_classifications
project_facts
external_observations
```

These names are candidates, not final implementation requirements.

## Knowledge libraries

A user or agency may maintain several knowledge libraries.

Examples:

```text
/knowledge/general/architecture/cctp
/knowledge/general/architecture/contracts
/knowledge/general/architecture/site
/knowledge/general/architecture/aor
/knowledge/general/architecture/urbanism
/knowledge/general/architecture/maf
/knowledge/general/architecture/dtu
/knowledge/agency/ifja/templates
/knowledge/agency/ifja/procedures
/knowledge/countries/FR/cerfa
/knowledge/countries/FR/urbanism
/knowledge/countries/FR/risks
/knowledge/countries/FR/cadastre
/knowledge/countries/FR/heritage
```

Each library should define:

```text
owner
scope
storage provider
root path
confidentiality
indexing policy
activation policy
```

## General versus project classification

The system must classify scope before use.

Examples:

```text
DTU extract, MAF note, CCTP type, contract model
  -> likely general or domain memory.

Quote, invoice, project email, site report, drawing, client note
  -> likely project memory.

Project CCTP later reused as a model
  -> mixed at first; may become general only after explicit extraction, anonymization if needed, and validation.

Site lesson learned
  -> project first; general only after human promotion.
```

A document may be mixed. Mixed status must be visible, not silently resolved.

## Markdown conversion

Markdown is a working representation, not the source of truth.

A Markdown conversion should preserve:

```text
original file reference
hash
page numbers
headings
section hierarchy
figures or tables markers
extraction confidence
OCR warning if applicable
source timestamps
```

Suggested header:

```yaml
---
source_document_id: ...
source_filename: ...
source_hash: ...
source_pages: ...
scope: candidate
project_id: null
knowledge_domain: architecture.site
status: needs_review
created_from: ocr | text_extract | manual
---
```

## Similarity and replacement checks

The system should not accumulate uncontrolled duplicate knowledge.

When a new knowledge document is imported, the system should compare it to existing documents in the same library and nearby libraries.

Similarity outcomes:

```text
duplicate
near_duplicate
same_topic
possible_conflict
unrelated
```

Possible recommendations:

```text
create_new
compare
merge
replace
reject
archive_old
```

No replacement should occur without review.

## Vectorization discipline

Vector indexes must respect scope.

Suggested index families:

```text
general_domain_index
agency_index
country_index
project_index
mixed_candidate_index
```

A project document should not be retrievable in another project unless it has been explicitly promoted to general or agency memory.

Chunk metadata should include:

```text
document_id
project_id
library_id
scope
status
source_page
heading_path
confidentiality
validity status
```

Retrieval without scope filters is not Pantheon-compatible.

## Chat drop workflow

Dropping a document into a chat should create an ingestion candidate, not an active memory item.

Expected response pattern:

```text
I detected the probable document type.
I detected the probable scope.
I found possible matching projects or libraries.
I found similar existing documents if any.
Here are the proposed actions.
Nothing has been activated yet.
```

Example for a general guide:

```text
Document type: site best-practice guide.
Probable scope: general agency knowledge.
Similar document: Guide chantier IFJA v2, similarity 0.74.
Proposed actions:
- convert to Markdown;
- compare with existing guide;
- keep as candidate;
- index only after validation.
```

Example for a project quote:

```text
Document type: contractor quote.
Probable scope: project.
Probable project: LIEUREY, confidence 0.91.
Probable company: HK, confidence 0.86.
Proposed actions:
- classify as project document;
- propose file rename;
- create candidate quote record;
- extract quote metadata;
- compare with CCTP if available.
```

## Project facts

Project facts are structured facts about a project.

Candidate table:

```text
project_facts
- project_id
- fact_key
- label
- value_text
- value_number
- value_date
- value_json
- unit
- source_type
- source_id
- confidence
- status
- valid_from
- valid_until
```

Examples:

```text
terrain_address
commune_code_insee
cadastral_parcels
project_owner_name
surface_existing
surface_created
urbanism_zone
risk_clay
heritage_nearby
planning_form_candidate
```

A project fact should answer:

```text
Where did it come from?
Which project does it belong to?
When was it last checked?
Who validated it?
Can it be reused?
```

## External observations

Public API results are observations before they are project facts.

Candidate tables:

```text
external_sources
external_connectors
external_source_queries
external_observations
source_packs
country_profiles
country_source_catalog
knowledge_refresh_rules
```

External observations should include source, query time, payload reference, freshness and status.

They may become project facts only through mapping and validation.

## Form preparation

Administrative forms should be handled as structured templates.

Candidate tables:

```text
form_templates
form_fields
form_field_mappings
form_instances
form_instance_values
```

A form instance should show:

```text
filled fields
candidate fields
missing fields
conflicting fields
source facts
last source refresh
human review status
```

A generated form is a draft until validated.

## Contact and organization memory

The system may sync with Google Contacts or another contact system, but Postgres keeps the professional relationship model.

Candidate tables:

```text
core_organizations
core_contacts
core_party_roles
external_contact_links
external_organization_links
contact_update_proposals
```

Google Contacts is a contact source and synchronization target. It is not sufficient to represent project roles, lots, responsibilities, quote senders, invoice senders or site meeting responsibilities.

Contact creation and updates should be proposed before execution.

## Naming and classification support

File and folder names should help classification but must not be the only source of truth.

Recommended file pattern:

```text
{DATE}_{PROJECT_CODE}_{TYPE}_{LOT}_{ORGANIZATION}_{REFERENCE}_{VERSION}.{EXT}
```

Examples:

```text
2026-05-31_LIEUREY_QUOTE_02-MASONRY_HK_DEV-2026-014_V01.pdf
2026-05-31_LIEUREY_INVOICE_03-PLUMBING_BPC_FAC-2026-044_V01.pdf
2026-06-04_LIEUREY_SITE-REPORT_CR08_IFJA_V01.pdf
2026-06-04_LIEUREY_CHANGE-ORDER_02-MASONRY_HK_AVT-01_V01.pdf
```

The system should propose renames, not silently apply them.

## Security and confidentiality

Rules:

```text
Project data stays project-scoped.
General knowledge must not contain confidential project data unless explicitly allowed.
OCR output is not automatically reliable.
Vectorized data inherits the highest confidentiality of its source.
Rejected or deprecated knowledge should remain traceable but not used by default.
```

## Operating principle

```text
The system must know where a document belongs before it uses the document.
```

This applies to uploaded guides, project documents, quotes, invoices, site notes, CCTP models, MAF notes, DTU extracts, public API results and administrative forms.
