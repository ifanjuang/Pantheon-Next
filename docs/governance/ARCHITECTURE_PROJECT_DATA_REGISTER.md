# Architecture Project Data Register

Status: candidate domain-support doctrine — to verify  
Scope: architecture project identity, facts, derived candidates, professional decisions, regulatory triggers and evidence boundaries  
Runtime status: non-executable

This document records a candidate discipline for classifying architecture-project information without turning Pantheon Next into a database product, ERP, runtime, scheduler, connector gateway or automatic regulatory decision system.

It refines the architecture-agency domain pack at the project-data level. It does not define a database schema, table set, cockpit collection, connector implementation, public-source workflow, OCR pipeline, form engine or automatic memory promotion.

```text
The database records.
The workflow proposes.
The evidence supports.
The approval validates.
The human decides.
```

## Purpose

Architecture dossiers need a controlled project register because the same information is reused in several liability-sensitive contexts:

```text
client discussion
municipality / instruction service
ABF or other external reviewer
CCTP and consultation package
site report and reserve tracking
insurer / MAF context
claim or fee-dispute chronology
```

A project name, informal alias, client statement, measured surface, regulatory source, extracted PDF value, automatically detected risk signal and professional conclusion do not have the same authority.

## Core rule

```text
A project data item is never only a value.
It is a value, a source, a scope, a status, an authority class and a review path.
```

The system may assist with extraction, normalization, comparison and candidate derivation. It must not silently validate facts, promote memory, complete professional reasoning or transmit conclusions externally.

## Data families

The project register separates at least the following families.

```text
project_identity
project_aliases
project_sources
project_facts
program_requirements
derived_candidates
regulatory_check_candidates
decision_records
evidence_pack_candidates
transmission_records
audit_events
```

These names are conceptual. They are not approved table names.

### Project identity

The identity layer carries stable dossier boundaries.

Candidate fields:

```text
project code
canonical project name
informal names / aliases
client / project owner
address
commune
parcel references
administrative references
mission scope
contract reference
current phase
confidentiality level
retention profile
```

Aliases are important. The same dossier may be known by a client name, street name, informal office nickname, company name, operation label or permit reference. Alias matching may propose a link; it must not silently merge two dossiers when the consequence would affect memory, billing, insurance, regulatory position or external transmission.

### Project sources

Sources are first-class objects.

Typical source classes:

```text
client email
client meeting note
signed contract
amendment
plan / drawing
survey
photo
CERFA draft
municipal request
permit or prior declaration decision
PLU extract
ABF or heritage note
CCTP version
quote
site report
OPR / reception record
public-source snapshot
specialist report
```

Each source needs at least:

```text
source identity
origin
received date
source date
version / revision signal
author or issuer if known
scope
authority class
confidentiality flag
validity or supersession signal
link to stored object if any
```

A retrieved public-source result is an observation before it becomes a project fact. A source snapshot is useful because public rules, pages, maps and municipal documents can change.

### Project facts

Project facts are values that may be reused inside the dossier.

Examples:

```text
site address
parcel area
existing floor area
proposed floor area
emprise au sol
publicly accessible area
number of levels
basement / mezzanine
use or destination
client-declared capacity
number of seats
maximum staff count
opening type in existing structure
roofing material
facade material
mission phase
budget target
insurance-sensitive chronology item
```

A project fact should record:

```text
value
unit if any
source reference
extraction method
confidence
status
validity date
scope
reviewer if validated
supersedes / superseded_by link if applicable
```

Extraction from email, OCR or drawing remains candidate until reviewed. Manual entry is not automatically verified; it still needs source or explicit professional assumption status.

## Status ladder

Recommended status vocabulary:

```text
raw_received
extracted_candidate
normalized_candidate
derived_candidate
needs_review
verified
approved_for_project
superseded
rejected
transmitted
```

Interpretation:

```text
raw_received: received but not classified.
extracted_candidate: extracted by user, OCR, parsing or model.
normalized_candidate: converted to a standard field, unit or vocabulary.
derived_candidate: inferred from other records or external observations.
needs_review: blocked pending human or specialist check.
verified: checked against adequate source.
approved_for_project: usable for this dossier and scope.
superseded: replaced by a later source, version or decision.
rejected: false, irrelevant, duplicate or intentionally not retained.
transmitted: used in an external communication, filing or deliverable.
```

No item should move from candidate to approved-for-project without an explicit review path.

## Fact classes and authority

The register should distinguish the kind of assertion being made.

```text
raw_source_value
user_statement
client_choice
professional_observation
measured_fact
computed_value
public_source_observation
derived_candidate
specialist_input
professional_decision
external_decision
```

Examples:

```text
client_choice: client wants 49 people maximum.
derived_candidate: likely ERP classification based on use and declared capacity.
public_source_observation: seismic zoning retrieved from a dated public-source snapshot.
specialist_input: structural engineer confirms opening feasibility assumption.
professional_decision: architect approves using the value in a filing draft.
external_decision: municipality issues permit, refusal, request for additional information or favorable opinion.
```

The same sentence may create several records. For example, a client asking for a restaurant with 80 seats creates a program requirement, a capacity fact candidate and one or more regulatory check candidates.

## Derived candidates

A derived candidate is a proposed conclusion generated from known records.

Typical derived candidates:

```text
seismic zone candidate from address / commune / public-source snapshot
planning-zone candidate from parcel and planning snapshot
ERP type candidate from use
ERP category candidate from effectif assumptions
accessibility trigger candidate
fire-safety notice trigger candidate
structural-engineering trigger candidate from opening size
energy and environmental regulation trigger candidate
clean-room / healthcare technical trigger candidate
heritage constraint candidate
```

Rules:

```text
1. Keep inputs visible.
2. Keep assumptions visible.
3. Keep missing inputs visible.
4. Name the review role needed.
5. Do not collapse derived candidate into verified fact.
6. Do not use derived candidate in external transmission without gate approval.
```

## Regulatory check candidates

Regulatory topics deserve their own review record because they can affect professional liability.

Candidate shape:

```text
regulatory_check_candidate:
  topic:
  trigger_fact:
  candidate_position:
  source_refs:
  assumptions:
  missing_inputs:
  consequence_if_wrong:
  required_review_role:
  output_allowed_status:
  approval_required_before_transmission:
  status:
```

Useful topics for architecture practice:

```text
urban planning / PLU
heritage / ABF
ERP type and category
fire safety
accessibility
structural modification
seismic and ground-risk context
energy and environmental regulation
sanitation / utilities
healthcare or laboratory technical constraints
public procurement / consultation rules
insurance / claim chronology
```

## ERP and public-capacity example

The register may assist with ERP reasoning, but should not finalize it autonomously.

Example input:

```text
use: bar / restaurant
client statement: 60 seats desired
staff estimate: unknown
publicly accessible area: candidate from plan
```

Candidate outputs:

```text
program_requirement: seating target = 60, source = client exchange
project_fact_candidate: public capacity assumption = 60 seats, status = needs_review
regulatory_check_candidate: ERP type/category to verify
missing_inputs: staff count, standing area, outdoor area, final operator declaration, applicable calculation rule
review_role: architect / fire-safety specialist if needed
```

The client can choose a capacity target. The professional must still determine how that target interacts with the applicable ERP rules and the final filed documents.

## Healthcare / clean-room example

A healthcare program with a surgical room, sterile preparation area, laboratory or controlled environment should trigger a specialized review path.

The register may record:

```text
program_requirement: operating room requested
regulatory_check_candidate: healthcare technical constraints likely
technical_check_candidate: clean-room classification or controlled-environment requirement to determine
missing_inputs: medical activity, infection-risk level, HVAC strategy, pressure regime, operating protocol, specialist brief
required_review_role: healthcare specialist / HVAC engineer / hygienist / competent designer
```

The system must not invent a final clean-room class from the phrase "operating room" alone.

## CCTP and deliverable use

A CCTP or notice should consume approved project facts, verified sources or explicitly marked assumptions.

Before insertion into a deliverable, a project data item should be qualified as one of:

```text
usable_as_verified_fact
usable_as_project_assumption
usable_as_client_choice
usable_as_external_decision
usable_only_as_question
not_usable
```

If a CCTP article depends on an unverified candidate, the output remains draft and should expose the gap.

## Transmission and insurer posture

External transmission changes consequence level.

Transmission targets include:

```text
client
municipality / instruction service
ABF or external reviewer
contractor / bidder
insurer / MAF
legal counsel
public platform
```

A transmission record should preserve:

```text
deliverable or message version
recipient
sent date
approval reference
facts relied on
evidence pack reference
known assumptions
known unresolved issues
```

For insurer or claim-facing material, chronology entries should distinguish:

```text
fact
client allegation
architect response
third-party position
documented proof
professional interpretation
```

## Review queue triggers

Items should enter a review queue when they are likely to affect truth, memory, approval, scope or external action.

Triggers:

```text
low confidence extraction
conflicting values for the same field
stale public-source snapshot
derived regulatory candidate
missing source for a reused fact
client choice with regulatory consequence
large opening in existing structure
ERP / healthcare / safety / accessibility trigger
insurance or fee-dispute relevance
external transmission requested
candidate memory promotion
```

A trigger may enqueue an item. It must not apply the decision.

## Boundary with tools

The register discipline is tool-agnostic.

Allowed support from external tools:

```text
capture
extract
normalize
compare
retrieve source candidates
query public sources
propose derived candidates
prepare evidence pack candidates
prepare review questions
prepare draft deliverables
```

Forbidden outcomes without governed validation:

```text
final project truth
automatic regulatory conclusion
automatic memory promotion
automatic dossier merge
automatic external filing
automatic email or notice transmission
automatic CCTP publication
automatic insurer-facing position
```

## First viable slice

A first useful slice should prove only a narrow loop:

```text
1. Create or select a project identity.
2. Attach one source.
3. Extract one project fact candidate.
4. Produce one derived regulatory candidate.
5. Show missing inputs and evidence.
6. Route to review.
7. Record approval, rejection or request for more evidence.
8. Use only the approved result in a draft deliverable.
```

Good first examples:

```text
address -> public-source snapshot -> seismic-zone candidate -> review
restaurant program -> capacity assumptions -> ERP classification candidate -> review
CCTP article -> referenced project facts -> proof-gap list -> review
insurer chronology -> dated sources -> allegation/fact/interpretation split -> review
```

## Non-goals

This note does not authorize:

```text
database schema creation
connector implementation
runtime workflow execution
public-source integration
OCR pipeline
vector index
ERP module
automatic approval
external transmission
memory promotion
schema or test changes
```

## Open reconciliation

This candidate should be reconciled with:

```text
DATA_PLATFORM_ARCHITECTURE.md / DATA_PLATFORM_STATUS.md
ARCHITECTURE_AGENCY_DOMAIN_PACK.md
REVIEW_QUEUE.md or equivalent review-queue doctrine
RAW_DERIVED_GOVERNED_RECORDS.md if kept
ARCHITECTURE_PROOF_REGISTER.md if promoted
```

It should be folded into the smallest durable location after review, rather than becoming another permanent parallel doctrine track.

## Operating principle

```text
Record the dossier precisely.
Expose what is known, guessed, derived, contradicted and approved.
Let workflows propose.
Let evidence constrain.
Let the professional decide.
Only the validated remains.
```
