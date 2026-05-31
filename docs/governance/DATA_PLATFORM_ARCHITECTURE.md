# Data Platform Architecture

Status: candidate governance support doctrine  
Scope: Postgres, Directus, storage, connectors, professional data registers  
Runtime status: non-executable

## Purpose

This document defines the candidate data-platform posture for Pantheon Next when it is used as a professional dossier governance layer above ordinary work tools.

It does not define an ERP implementation. It does not define an agent runtime. It does not prescribe a final database schema.

It defines a controlled architecture for organizing professional data so that future modules, workflows and domain packs can be proposed, tested, reviewed, activated, disabled and audited.

## Core rule

```text
Postgres records.
Directus exposes and controls.
Storage keeps files.
Connectors observe and retrieve.
Hermes may execute bounded jobs.
Pantheon governs the status, scope, proof and approval model.
```

A database row is not a decision. A workflow output is not an approval. A generated document is not a transmitted document. A stored memory is not globally reusable by default.

## Why this layer exists

Professional AI work needs more than prompts and retrieval. It needs stable registers for:

- matters, projects or dossiers;
- users, organizations, contacts and roles;
- documents, files, versions and storage locations;
- messages, attachments and source events;
- extracted facts, observations and evidence candidates;
- approvals, decisions and transmission gates;
- workflows, workflow modes, proposed actions and actual executions;
- knowledge libraries, domain packs and project memory;
- audit trails and reversibility metadata.

The data platform is therefore a controlled professional memory and trace layer, not an autonomous operator.

## Layer model

```text
User tools
  - email
  - chat
  - Drive / SFTP / NAS / local folders
  - calendars
  - contacts
  - office documents

Ingestion and connector layer
  - import files
  - read emails and attachments
  - sync contacts
  - query public APIs
  - detect source type and scope

Data platform
  - Postgres tables
  - controlled statuses
  - object links
  - evidence and validation records
  - workflow definitions and runs

Cockpit layer
  - Directus or equivalent admin UI
  - views, dashboards, manual correction
  - permissioned review and approval

Execution support
  - Hermes jobs
  - OCR / Markdown conversion
  - extraction
  - comparison
  - draft generation
  - indexing

Governance layer
  - Pantheon doctrine
  - task boundaries
  - approval policies
  - memory scope
  - audit and rollback expectations
```

## Stable core versus domain packs

The platform must not be designed around one profession only.

The stable core contains reusable objects:

```text
core_projects
core_scopes
core_modules
core_capabilities
core_users
core_organizations
core_contacts
core_party_roles
doc_documents
storage_objects
message_threads
message_items
workflow_definitions
workflow_versions
workflow_runs
workflow_action_proposals
approval_records
audit_events
knowledge_libraries
knowledge_documents
project_facts
external_sources
external_source_queries
```

Domain packs add profession-specific objects.

For an architecture agency, a domain pack may add:

```text
architecture_lots
architecture_cctp_versions
architecture_cctp_articles
architecture_quotes
architecture_quote_lines
architecture_quote_cctp_matches
site_meetings
site_points
site_point_updates
site_progress_by_lot
site_reserves
finance_contracts
finance_change_orders
finance_invoices
finance_payments
form_templates
form_instances
```

For another profession, the domain pack changes while the core governance model remains.

## Directus posture

Directus is a cockpit over the data model. It may be used to:

- inspect records;
- correct classification;
- review proposed actions;
- approve or reject data promotions;
- manage metadata;
- expose dashboards;
- manage low-risk administrative transitions.

Directus must not become:

- the canonical governance doctrine;
- a hidden approval engine;
- a professional decision-maker;
- an uncontrolled workflow runtime;
- the only source of truth for documents and proof.

Directus collections should expose readable data objects. The canonical governance definitions remain in the repository until a later implementation explicitly changes that boundary.

## Storage posture

Files should not be treated as database blobs by default.

The platform stores file metadata, hashes, source links, access policy and storage location. The physical file may live in:

```text
local folder
NAS
Google Drive
SFTP
S3-compatible object storage
OpenWebUI upload area
domain-specific secure repository
```

Candidate tables:

```text
storage_providers
storage_mounts
storage_objects
storage_access_policies
file_rename_proposals
```

The same logical object can therefore be deployed locally, on a NAS, on a hosted server, or in a hybrid setting.

## Status discipline

Every important object needs a status. Suggested baseline status families:

```text
candidate
needs_review
verified
active
rejected
superseded
deprecated
archived
```

For outputs and actions:

```text
proposed
approved
rejected
executed
failed
revoked
```

For documents:

```text
received
classified
processed
indexed
validated
published
transmitted
archived
```

No object should silently move from candidate to active memory.

## Data scope discipline

Every reusable fact should be scoped.

Candidate scope levels:

```text
global
domain
country
agency
project
matter
session
task
```

A project fact is not global knowledge. A guide or model may be general knowledge. A project document may become general knowledge only after explicit review, anonymization if needed, and validation.

## Candidate core table families

### Modules and capabilities

```text
core_modules
core_capabilities
module_dependencies
module_installations
```

These describe what the system can do without forcing every user to activate every feature.

### Projects and scopes

```text
core_projects
core_scopes
project_settings
project_storage_policies
```

Projects hold contextual boundaries. Scopes govern reuse and confidentiality.

### Parties and contacts

```text
core_organizations
core_contacts
core_party_roles
external_contact_links
contact_update_proposals
```

The local database keeps the professional role model even when contacts are synchronized with Google Contacts or another provider.

### Documents and messages

```text
doc_documents
doc_document_versions
doc_document_relations
message_threads
message_items
message_attachments
```

Emails and attachments are sources. Documents are classified, versioned and linked to projects, workflows, contacts and evidence.

### Knowledge and facts

```text
knowledge_libraries
knowledge_documents
knowledge_document_versions
knowledge_chunks
project_facts
external_observations
```

The system separates general knowledge from project-specific facts.

### Workflows

```text
workflow_definitions
workflow_versions
workflow_runs
workflow_steps
workflow_test_cases
workflow_action_proposals
workflow_action_executions
```

Workflows are versioned, testable, observable and reversible where possible.

### Approvals and audit

```text
approval_policies
approval_records
audit_events
rollback_records
schema_change_proposals
```

The platform records what was proposed, what was accepted, what was executed and what can be reversed.

## Deployment profiles

### Local / NAS profile

```text
Postgres + Directus + workers in Docker
Files on NAS
Backups local and external
Limited remote access
```

This profile prioritizes control and confidentiality.

### Hosted profile

```text
Hosted Postgres or VPS
Hosted Directus
External object storage or Drive/SFTP
Workers deployed as services
```

This profile prioritizes access and collaboration.

### Hybrid profile

```text
Hosted database and cockpit
Sensitive files on user-controlled storage
Connectors per project or per module
```

This profile is likely the most adaptable for professional usage.

## Non-goals for the first implementation

The first implementation should not attempt to build:

- a full ERP;
- a universal schema for every profession;
- an autonomous decision engine;
- automatic external sending;
- automatic memory promotion;
- automatic schema mutation;
- a single vector index containing all project and general knowledge without scope separation.

## First viable platform slice

A useful first slice should include:

```text
core_projects
core_scopes
core_organizations
core_contacts
doc_documents
storage_objects
workflow_definitions
workflow_runs
workflow_action_proposals
approval_records
knowledge_libraries
knowledge_documents
project_facts
audit_events
```

Domain-specific tables can then be added as candidate packs, not as hardcoded doctrine.

## Operating principle

```text
Build the system that lets workflows and domain structures be proposed, tested, reviewed and stabilized.
Do not hardcode the profession before the platform can govern change.
```

The database is not the authority by itself. It is the maintained register through which authority, evidence, scope and approvals remain visible.
