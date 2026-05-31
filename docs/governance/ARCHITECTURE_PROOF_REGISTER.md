# Architecture Proof Register

Status: candidate support doctrine — architecture-domain proof register.

This document defines a candidate proof register for architecture practice.

It is documentation only.

It does not implement a SQL schema, migration, Directus cockpit, Postgres table, object storage, pgvector index, provenance graph, queue runtime, scheduler, OpenWebUI action, Hermes skill, connector, approval engine or memory engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

In abstract form:

```text
The exposure surface exposes.
The execution runtime executes.
Pantheon governs.
```

## Purpose

Architecture practice does not only need documents. It needs proof that can survive time, contradiction, phase changes, contractor disputes, client arbitration, reception, DOE, GPA and later liability questions.

The proof register is the conceptual layer that links:

```text
source document
source version
professional object
claim or decision
Evidence Pack Candidate
governed status
human approval
append-only event
```

It exists to prevent a weak document, missing version, derived chunk or fluent summary from becoming a professional fact.

## Core rule

```text
A document is stored.
A fragment is cited.
An evidence item supports.
A proof register entry records the relationship.
A governed status gives usable authority.
A human decision commits.
```

## Relation to existing doctrine

This document specializes:

```text
DOCUMENT_INTELLIGENCE.md
ARCHITECTURE_DOCUMENT_REVIEW.md
DATA_PLATFORM_RECONCILIATION.md
REVIEW_QUEUE.md
```

It does not replace them.

## What the proof register is

A proof register is a governed map of relationships between professional objects and their evidence.

Examples:

```text
CCTP clause -> source document version -> approved PRO package
quote line -> contractor quote version -> ACT comparison finding
service order -> signed instruction -> execution event
meeting decision -> meeting minute -> action item
reserve -> reception PV -> contractor lot -> closure evidence
DOE item -> equipment document -> completeness status
GPA issue -> notification -> contractor response -> closure decision
```

The register does not decide truth by itself.

It makes proof reviewable, scoped and reversible.

## Objects covered first

Candidate first objects:

```text
CCTP clause
quote
quote line
work contract
service order
meeting minute
meeting decision
action item
observation
non-conformity
reserve
reception PV
DOE pack
DOE item
GPA issue
signature event
approval event
verification event
admission event
risk snapshot
planning snapshot
heritage snapshot
```

These are professional objects, not approved physical table names.

## Proof entry shape

A proof register entry should answer:

```text
what object is being supported?
what claim or status is being supported?
which source version supports it?
what fragment or document anchor supports it?
who produced it?
who validated it?
what scope contains it?
what authority level does it have?
what can it be used for?
what can it not be used for?
what would make it obsolete?
```

Conceptual shape:

```text
proof_entry:
  professional_object_type
  professional_object_ref
  claim_or_status
  evidence_refs
  source_authority_level
  scope_id
  phase_code
  lot_id
  produced_by
  reviewed_by
  approval_state
  allowed_use
  forbidden_use
  supersedes
  superseded_by
  created_at
  status
```

This is not an approved schema.

## Source authority levels

Candidate authority hierarchy:

```text
law_or_regulation
operation_contract
signed_market_document
approved_phase_decision
signed_or_contradictory_site_evidence
approved_client_decision
contractor_signed_response
approved_technical_report
agency_standard
project_working_document
derived_text
semantic_search_result
model_interpretation_candidate
```

Rule:

```text
Derived text, semantic retrieval and model interpretation can support review.
They cannot outrank signed, approved or contradictory source evidence.
```

## Status vocabulary

Recommended proof statuses:

```text
candidate
source_incomplete
source_complete_for_task
requires_human_review
requires_more_evidence
requires_client_decision
requires_contractor_response
approved_for_internal_use
approved_for_meeting_preparation
approved_for_transmission_draft
approved_for_contractual_action
accepted_as_project_fact
rejected
obsolete
superseded
```

A status may be strong only inside its scope.

Example:

```text
approved_for_meeting_preparation != approved_for_contractual_action
```

## Phase-gate relation

The proof register should support phase gates.

Candidate gates:

```text
DIAG feasibility / initial programme
APS approval
APD freeze
PRO ready-for-consultation
DCE issued
ACT attribution decision
EXE / VISA status
DET monthly execution status
AOR / reception
DOE acceptance
reserve closeout
GPA issue closeout
```

Each gate should define a minimal Evidence Pack Candidate.

The proof register records whether the evidence exists and which status it has.

## Evidence pack minimums

### CCTP / DCE

Minimum evidence:

```text
source CCTP version
lot identification
clause or section anchors
approval state
related normative references when relevant
DCE package identity if issued
```

### Quote / ACT

Minimum evidence:

```text
quote source version
contractor identity
lot identity
quote line anchors
comparison finding if any
client attribution decision if any
contract signature if any
```

### Meeting minute / decision

Minimum evidence:

```text
meeting date
attendance or participants
minute version
decision text
owner
deadline
later closure event when applicable
```

### Reserve / reception

Minimum evidence:

```text
reception PV
reception date
effect date
reserve description
lot / contractor
contradictory context when available
closure evidence
closure approval
```

### DOE / handover

Minimum evidence:

```text
DOE pack version
required item list
delivered item
equipment or system reference
maintenance / warranty evidence when applicable
acceptance or missing status
```

### GPA issue

Minimum evidence:

```text
issue description
notification or report
related reserve or post-reception defect
contractor response
closure evidence
closure decision
```

## Review queue triggers

A proof register entry may generate a Review Queue item when:

```text
source version is missing
source is superseded
hash is missing
approval is missing
authority level is too low for requested use
contradictory evidence exists
scope is ambiguous
retention class is missing
signature or timestamp is missing where required
semantic result is being used as if it were proof
urgent claim lacks evidence
```

The queue exposes the decision.

It does not apply the decision.

## Memory boundary

A proof register may support Memory Candidates.

It must not promote Canonical Memory.

Examples:

```text
recurring missing quote item
recurring DOE incompleteness pattern
frequent reserve category
standard agency checklist candidate
```

Promotion requires a separate governed memory decision.

## External action boundary

The proof register must not authorize by itself:

```text
email sending
service order issuance
quote approval
contractor selection
payment validation
reserve closure
DOE acceptance
GPA closure
administrative filing
memory promotion
```

It can support an approval gate by showing evidence.

## Non-goals

This document does not authorize:

```text
creating physical database tables
stabilizing SQL schema names
building a Directus cockpit
building an ERP
running workflow automation
approving documents automatically
cross-affair search by default
using vector search as proof
replacing architect judgement
```

## Boundary phrase

```text
The proof register records what supports what.
It does not decide what is true enough to act.
Pantheon governs the status.
The human commits the decision.
```
