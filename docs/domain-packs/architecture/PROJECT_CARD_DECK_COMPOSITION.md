# Architecture Project Card Deck Composition

Status: candidate support doctrine — documented non-implemented.
Boundary profile: candidate_support_note.

This document owns the architecture-domain composition rule for the agency Cockpit.
It reconciles the source-backed Project Claim seam with a deliberately small visual card vocabulary.

```text
OpenWebUI / Cockpit exposes.
Hermes executes bounded admitted work.
Pantheon Next governs consequential status, scope, provenance, approval and effects.
The human decides.
```

## 1. Core rule

The Cockpit user experience and the backend semantic model are deliberately different layers.

```text
UX card family != backend semantic entity
```

The first architecture-facing Cockpit uses six primary visual families:

```text
Project
Information
Contacts
Work
Decision
Tool
```

This is a projection vocabulary, not an ontology. Backend semantic entities may include Project, Information, ProjectClaim, Evidence, Knowledge, WorkIssue, ChangeCandidate, Capability, runtime observations and other governed objects without each becoming a visible card family.

Former candidate visual families such as Surface, Fact, Claim, Jalon and Participation are not required as architecture-facing cards.

```text
hidden semantic entity != deleted semantic entity
projection simplification != provenance simplification
```

## 2. Project record and Project Card

The durable Project record stays focused on identity, operational state and flexible non-consequential description.

Typical direct fields include:

```text
project_id
code
display_name
status
phase
location
revision + audit
```

Flexible descriptive values may live in a bounded attributes store when they do not require source-backed professional reliance.

Examples:

```text
architectural style
programme summary
internal categories
presentation preferences
agency observations
```

The Project Card is a projection. It may display concise business values such as budget, surfaces, PLU zone, parcel references, permit information or ERP type without requiring Claim to appear as a visible card.

For consequence-bearing values, the displayed value SHOULD resolve through a ProjectClaim rather than becoming an unqualified Project attribute.

```text
Project Card
  displays value
      ↓
ProjectClaim
      ↓
backing_ref
      ↓
Information / Evidence / Knowledge / Decision / other governed semantic entity
```

Therefore:

```text
project display != source authority
project attribute != ProjectClaim
ProjectClaim != Evidence
ProjectClaim != approval
verified claim != opposable value
```

## 3. Three classes of Project information

### 3.1 Core identity

Stored directly on the Project record.

```text
project_id
code
display_name
status
phase
location
revision
```

### 3.2 Flexible descriptive attributes

Stored as ordinary extensible Project attributes when source-backed reliance is not required.

```text
style
programme summary
preferences
internal observations
presentation metadata
```

### 3.3 Source-backed Project claims

Professional values whose error, staleness or provenance can materially affect work SHOULD use `project_claim` semantics.

Typical examples:

```text
budget / market amount
surface values
emprise
PLU / PLUi zone
parcel reference
ERP classification
permit reference / permit dates
administrative milestone dates
reception date
```

A claim may begin as `asserted` from a human or bounded external projection. It becomes `source_backed` only when a backing semantic entity is declared. `verified` remains a claim qualification, not an approval or Evidence admission.

## 4. Information Card

Information is the principal flexible professional visual family.

It may represent:

```text
PLU / PLUi note
email
meeting report
internal note
contract
CCTP / CCAP
supplier document
technical study
received dossier
administrative document
regulatory analysis
question
hypothesis
professional synthesis
source-backed memo
```

The underlying semantic status is not collapsed by the visual family. An Information card can project content originating from a document, note, email, knowledge-derived synthesis or other source while Evidence, Knowledge and Decision distinctions remain governed separately.

Recommended visible fields:

```text
title
category
source_type
source_ref optional
source_version optional
index
date
author
summary
details
status
limits / postures
type_tags
subject_tags
technical revision + lineage hidden when appropriate
```

`category != source_type`.

The visible Information index changes only when the professional source/version changes. Editorial rewrites of the same working source do not consume a new visible index.

```text
visible source index != technical revision
```

An acted Information version is immutable. A material new source/version derives a new working Information while retaining the prior acted version as reference.

Hermes context for a working Information SHOULD distinguish both:

```text
last acted Information
+
current working Information
```

This is scoped context construction, not memory promotion.

## 5. ProjectClaim backing semantics

`schemas/project_claim.schema.yaml` governs the linking seam.

A ProjectClaim references a semantic entity, not a visual card family:

```yaml
backing_ref:
  entity_type: information
  entity_id: info-...
  observed_status: acted
```

Typical backing entity types may include:

```text
information
evidence
knowledge
decision
document
```

The vocabulary is semantic and extensible by owner doctrine. The Cockpit decides how a referenced entity is projected visually.

```text
backend semantic reference
        ↓
projection
        ↓
UX family
```

Never the reverse.

A claim without `backing_ref` may exist only in states that do not assert source backing, such as `asserted` or `contested`. `source_backed` and `verified` require a backing reference.

### 5.1 Candidate-to-Claim transition

`schemas/project_claim_candidate.schema.yaml` governs one runtime-produced proposal.
The proposal remains an immutable typed item inside the existing Execution Result
contract. It is not promoted into a Claim.

```text
ProjectClaimCandidate
→ human review
→ separate append-only ProjectClaim creation
```

The new Claim retains the exact `execution_id`, `result_id` and optional review
disposition in `provenance.candidate_ref`. It also carries the canonical certainty
axis and may distinguish `effective_at` from `observed_at`.

```text
candidate stored != Claim created
Claim created != Evidence admitted
certainty != status
observed_at != effective_at
runtime success != professional validation
```

An implication that requires action remains a WorkIssue; an arbitration remains a
DecisionRequest; a rejected recommendation remains in the Result Candidate. F does
not introduce a generic Derivation or Consequence authority.

## 6. Contacts, Work and Decision

A Project exposes one grouped Contacts card rather than one visible Participation card per person.

Work is a visible professional work projection: objective, milestones, responsibilities, skills, functions, tools and linked Information may be shown. It is not a scheduler, queue or workflow runtime.

Decision is a human review/orientation surface. It may project a Work review or a ChangeCandidate review without making those backend entities the same object.

```text
Work card != WorkIssue runtime
Decision card != ChangeCandidate
Decision card != Pantheon automatic approval
```
