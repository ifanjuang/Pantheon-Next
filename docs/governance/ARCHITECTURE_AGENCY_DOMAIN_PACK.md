# Architecture Agency Domain Pack

Status: candidate domain-pack doctrine  
Scope: architecture agency workflows, project registers, site reports, finance follow-up, administrative forms and knowledge libraries  
Runtime status: non-executable

## Purpose

This document defines a candidate domain pack for architecture agencies.

It is not a complete product specification. It is not a final database schema. It is a domain-oriented map showing how the generic Pantheon data platform can support architecture practice without hardcoding one office's methods as universal rules.

The pack is intentionally modular. A small agency may activate only matters, documents and quotes. A construction-phase office may activate site reports, finance follow-up and AOR. Another profession may replace this pack with its own domain objects while keeping the same workflow lifecycle and memory governance.

## Core rule

```text
Architecture work is not a pile of documents.
It is a linked register of projects, sources, decisions, obligations, evidence, tasks, money and transmissions.
```

A PDF report, a quote, an invoice, a CERFA draft or a site meeting note is a publication or source object. The professional state lives in the structured register.

## Pack modules

Candidate modules:

```text
architecture_projects
architecture_parties
architecture_documents
architecture_mail_intake
architecture_cctp_and_quotes
architecture_site_meetings
architecture_finance_followup
architecture_forms_and_urbanism
architecture_knowledge_library
architecture_contacts_sync
```

Each module can be activated, disabled, tested or replaced.

## Project register

The project register is the central matter object.

Candidate fields:

```text
project code
project name
client / project owner
address
administrative identifiers
current phase
current status
mission scope
surfaces
planning constraints
MAF / insurance references
storage policy
confidentiality level
```

Common architecture phases:

```text
ESQ
APS
APD
DP / PC / DPC
PRO
DCE
ACT
DET
AOR
GPA
```

The phase is a status and organization tool. It is not by itself proof that a task is complete.

## Parties and roles

Architecture work depends on roles changing by project.

Candidate objects:

```text
organizations
contacts
project party roles
lots
contractor roles
consultant roles
administration roles
client roles
```

Examples:

```text
client
architect / MOE
BET structure
BET thermique
bureau de controle
SPS
contractor
subcontractor
supplier
municipality
urban planning service
concessionnaire
syndic
```

The local database must keep a professional copy of contact and organization information even when synchronized with Google Contacts.

Google Contacts is a contact source and optional synchronization target. It does not replace the project-role model.

## Mail intake: quote, invoice, project message

Incoming email can become a controlled source event.

Candidate flow:

```text
email received
  -> message record
  -> attachment records
  -> sender and signature extraction
  -> contact / organization matching
  -> document type classification
  -> project attribution proposal
  -> storage proposal
  -> candidate domain object creation
  -> human review
```

Possible classifications:

```text
quote
invoice
change-order request
technical question
client decision
site update
administrative notice
spam / announcement / non-project
```

The system may propose attribution. It should not silently bind a document to a project if confidence is insufficient.

## Documents and naming

The pack should support both user-readable folders and machine-readable naming.

Recommended project folder pattern:

```text
/projects/{PROJECT_CODE}_{PROJECT_NAME}/
  00_admin/
  01_client/
  02_studies/
  03_authorizations/
  04_dce/
  05_act/
    cctp/
    quotes/
    analysis/
  06_det/
    site_reports/
    photos/
    payment_applications/
    invoices/
    change_orders/
  07_aor/
    reserves/
    doe/
    reception/
  08_finance/
  09_emails/
  99_archives/
```

Recommended file pattern:

```text
{DATE}_{PROJECT_CODE}_{TYPE}_{LOT}_{ORGANIZATION}_{REFERENCE}_{VERSION}.{EXT}
```

The system should propose file renames and final storage paths. It should not silently rename or move high-value documents without authorization.

## CCTP and quote analysis

Quotes are not isolated PDFs. They should be linked to project, lot, contractor, source email, storage object and CCTP baseline.

Candidate objects:

```text
architecture_lots
architecture_cctp_versions
architecture_cctp_articles
architecture_quotes
architecture_quote_lines
architecture_quote_cctp_matches
architecture_quote_anomalies
```

Quote analysis may detect:

```text
missing CCTP article
partial coverage
variant not requested
exclusion
quantity mismatch
ambiguous wording
validity missing
insurance or administrative information missing
```

The analysis is a candidate professional comment. It is not a decision to accept, reject or negotiate the quote.

## Site meetings and reports

A site report is not the source object. It is a published view of a living register.

Candidate objects:

```text
site_meetings
site_meeting_participants
site_notes
site_points
site_point_updates
site_tasks
site_progress_by_lot
site_reserves
site_expected_documents
site_report_snapshots
site_report_publications
site_next_meeting_preparation
```

Core rule:

```text
A site report is a temporary publication of the current site register.
```

A point should live across multiple reports.

Example:

```text
CR03: point created, contractor response expected.
CR04: still open, delay noted.
CR05: marked as completed by contractor, to verify on site.
CR06: closed after verification.
```

The system may generate next-meeting preparation from:

```text
open points
overdue tasks
points requiring verification
missing documents
unanswered contractor questions
pending client decisions
financial alerts
unclosed reserves
```

## Kanban and Gantt views

Kanban and Gantt should be views over structured tasks, not separate truth sources.

Candidate task statuses:

```text
backlog
todo
in_progress
to_verify
blocked
done
cancelled
```

Candidate planning fields:

```text
planned_start
planned_due
actual_start
actual_end
progress_percent
dependency links
lot
responsible organization
source point
```

A workflow may propose status changes. It should not close professional site points without review unless explicitly authorized by policy.

## Finance follow-up

Construction progress has a financial trajectory.

Candidate objects:

```text
finance_budgets
finance_budget_lines
finance_contracts
finance_change_orders
finance_change_order_lines
finance_payment_applications
finance_payment_application_lines
finance_invoices
finance_payments
finance_deductions
finance_alerts
finance_meeting_preparation_items
```

Core rule:

```text
A financial row is not just an amount.
It is an engagement, a modification, a payment request, a validation state and a trace.
```

The system should distinguish:

```text
quote received
quote retained
contract / market
change order
payment application
invoice
payment
retention / deduction / penalty
```

Alerts may include:

```text
invoice without contract
invoice exceeds revised contract
change order invoiced but not validated
payment application inconsistent with previous situation
amount mismatch HT / VAT / TTC
financial progress ahead of site progress
missing client validation
```

These alerts prepare review. They do not approve or reject payment.

## Administrative forms and public-source data

The pack may support project fact gathering and form preparation.

Candidate objects:

```text
project_facts
external_sources
external_connectors
external_source_queries
external_observations
form_templates
form_fields
form_field_mappings
form_instances
form_instance_values
```

Use cases:

```text
pre-fill CERFA draft
prepare missing field list
query public source candidates
attach source timestamps
flag uncertainty
prepare administrative completeness review
```

A generated form is a draft until reviewed.

## Knowledge library

An architecture user may provide their own knowledge base:

```text
best-practice guides
CCTP methods
CCTP article models
DTU extracts if permitted
MAF notes
contract templates
site report templates
AOR procedures
urban-planning notes
agency naming rules
```

The system should ingest, OCR, convert to Markdown, compare, classify and index these documents only under the approved scope.

General knowledge and project knowledge must stay separated.

## Workflow examples

### Incoming quote workflow

Initial mode: test or shadow.

```text
trigger: incoming email with attachment
steps:
- classify document as quote candidate
- detect project
- detect contractor
- detect lot
- save original candidate
- propose file name and storage path
- extract metadata and lines
- compare to CCTP if available
- create action proposals
```

Blocked until approval:

```text
final project attribution
final quote record
final storage move
client or contractor email
quote acceptance or rejection
```

### Site report workflow

```text
trigger: meeting notes, transcript or manual request
steps:
- parse notes into candidate points
- retrieve previous open points
- propose status updates
- identify missing responsible parties
- generate next-meeting preparation
- draft report
- prepare PDF candidate
```

Blocked until approval:

```text
published report
email to participants
closing points
binding decisions
```

### Finance follow-up workflow

```text
trigger: invoice, payment application or change-order request
steps:
- classify financial document
- match contractor and contract
- extract amounts
- compare to contract and validated change orders
- flag anomalies
- prepare meeting questions or client note
```

Blocked until approval:

```text
payment approval
penalty application
contractor dispute email
client transmission
```

### Knowledge drop workflow

```text
trigger: user drops a document in chat or storage inbox
steps:
- classify general/project/mixed
- detect existing similar knowledge
- OCR and convert to Markdown
- propose library or project folder
- propose indexing scope
```

Blocked until approval:

```text
activation as general knowledge
replacement of existing guide
project-to-general promotion
```

## Minimal first architecture pack

A first useful slice should include:

```text
projects
organizations
contacts
project party roles
documents
storage objects
messages
attachments
lots
quotes
invoices
site meetings
site points
workflow proposals
knowledge libraries
project facts
approvals
audit events
```

This enables quote intake, simple finance follow-up, site-point tracking and knowledge ingestion without building a full ERP.

## Non-goals

The architecture agency pack should not initially attempt to:

- automate professional judgment;
- replace accounting software;
- replace legal review;
- replace official urban-planning verification;
- auto-send site reports;
- auto-approve quotes, invoices or change orders;
- infer universal practice from one agency's habits.

## Operating principle

```text
The pack models professional objects so that workflows can help maintain them.
It does not turn professional responsibility into automation.
```
