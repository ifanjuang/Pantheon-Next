# Work Context Composer Specification

Status: candidate — to verify.

This document defines the candidate UX and governance shape for the Pantheon work context composer.

It does not implement a UI, runtime, connector, router, queue, scheduler, OpenWebUI integration, oikb sync, Google Drive integration, Google Docs add-on, Google Sheets add-on, Hermes skill, approval engine, memory engine or Registre Probatoire write.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Professional users should not have to select Knowledge Bases, vector stores, folders, modules or connectors manually.

They should validate a reviewable professional perimeter:

```text
work request
→ proposed work context
→ included sources
→ excluded sources
→ missing evidence
→ risk signal
→ human decision
```

The user-facing object is therefore not a `KB selection`. It is a:

```text
Contexte de travail proposé
```

or, for stricter professional wording:

```text
Périmètre documentaire proposé
```

## Core rule

```text
The user validates a documentary perimeter, not a technical Knowledge Base list.
```

Technical mappings to OpenWebUI Knowledge, Google Drive folders, local folders, oikb sync jobs, vector indexes or other retrieval systems must remain behind the perimeter card unless the user opens details.

## Composition responsibility

```text
Hermes Agent composes a candidate context.
Pantheon Next validates and displays it.
The user decides.
```

Detection, classification and composition are inference. They are a Hermes candidate, not a governance-core function. The governance core does not identify the project, classify the request, score the risk or rank sources: doing so would recreate an agent runtime and an LLM router, which the non-negotiable boundaries forbid.

The governance core only:

```text
validates the candidate work_context_proposal against schema and policy
  (target posture: schema validation applies once work_context_proposal
  exists as a schema candidate — see "Suggested object shape"; until then
  only policy/boundary display applies);
displays risk, exclusions, reservations and missing evidence;
records that a human decision is required;
returns the policy decision as data.
```

The "Allowed posture" below describes the composer surface as a whole (Hermes proposing, Pantheon governing), not work performed inside the governance core.

## Boundary

Allowed posture:

```text
identify likely project;
classify request type;
classify risk;
propose context mode;
show included source families;
show excluded source families;
show missing evidence;
show why the context was proposed;
allow user correction;
lock an accepted context for one response or workflow;
prepare a governed retrieval handoff to an execution runtime.
```

Forbidden posture:

```text
automatically make a source canonical;
automatically activate an archived document;
automatically promote memory;
automatically approve a response;
silently include old versions;
silently include AI-produced drafts as sources;
hide the chosen source perimeter;
treat retrieval success as proof.
```

## Context modes

The cockpit should start with three user-facing modes.

### Rapide

For low-risk requests.

Default perimeter:

```text
project active documents only;
archives excluded;
old versions excluded;
draft discussions excluded;
documents to verify excluded.
```

### Prudent

For regulatory, contractual, technical or professional-liability-sensitive requests.

Default perimeter:

```text
project active documents;
relevant general documentation;
responsibility / mission references where relevant;
documents to verify shown with reservation, not silently used;
archives excluded by default;
old versions excluded;
AI-produced drafts excluded.
```

### Contentieux

For insurer, dispute, reception, non-payment, liability, claim or chronology work.

Default perimeter:

```text
project active documents;
important archives;
chronology sources;
prior decisions;
communications;
relevant responsibility references;
old versions included only when explicitly useful and labeled;
AI-produced drafts excluded as sources unless explicitly reviewed.
```

## Suggested object shape

```text
work_context_proposal:
  proposal_id:
  request_summary:
  detected_project:
    project_id:
    confidence:
    alternatives:
  detected_request_type:
  detected_risk_level:
  recommended_mode: rapide | prudent | contentieux
  included_source_sets:
    - label:
      technical_refs:
      reason:
      status:
  excluded_source_sets:
    - label:
      reason:
  missing_evidence:
    - label:
      why_it_matters:
      safe_fallback:
      confidence:
  source_reservations:
    - label:
      reservation:
  proposed_workflow:
  allowed_outputs:
  forbidden_outputs:
  human_decision_required: true
  accepted_context_lock:
    scope:
    expires_at:
    linked_branch:
```

`technical_refs` may point to OpenWebUI Knowledge IDs, Google Drive folder IDs, local folder paths, vector collection filters or other adapter references. These are implementation details. The user sees the professional labels first.

The shape above is illustrative pseudo-structure, not a validatable contract. `work_context_proposal` stays ungoverned until it exists as a JSON Schema candidate in the governance core, alongside the other schemas. Promoting this object to a real schema is a prerequisite before any consumer relies on it; it is tracked under "To verify".

`missing_evidence` is the hardest and least reliable field. Naming what is absent (a fire classification report, a missing junction detail) is domain inference, not retrieval — it depends on professional knowledge the composer may not hold. It must therefore carry a `confidence` and always be presented as a prompt for human judgement, never as an authoritative checklist. An empty or low-confidence `missing_evidence` is not evidence that nothing is missing.

## Request routing examples

### Contractor facade email

```text
Request:
"Reply to the contractor email about facade execution."

Recommended mode:
Prudent

Included:
- project active documents;
- active CCTP / DCE if present;
- active facade technical documents;
- general fire / facade documentation;
- architect responsibility / mission references.

Excluded:
- archives;
- replaced plans;
- AI draft branches;
- unreviewed contractor documents unless shown as reservations.

Missing evidence:
- fire classification report;
- technical note;
- facade/slab junction detail;
- competent technical review where required.
```

### Simple project summary

```text
Recommended mode:
Rapide

Included:
- project active documents;
- latest project identity data.

Excluded:
- archives;
- general documentation;
- discussion drafts.
```

### Insurance chronology

```text
Recommended mode:
Contentieux

Included:
- active documents;
- important archives;
- received/sent communications;
- meeting minutes;
- decision records;
- proof candidates;
- insurer-facing chronology sources.

Excluded:
- unreviewed AI summaries as sources;
- irrelevant general documentation.
```

## Google projections

These projections are adjacent scope, kept here only as orientation. They belong in a dedicated external-projections document rather than in the composer spec, and should be extracted once that document exists. Nothing below is a connector, an add-on or a sync job; all of it is non-implemented and remains candidate.

### Google Drive

Google Drive should be a source projection, not the authority by itself.

The cockpit may show:

```text
Drive folder connected;
last sync;
files added;
files removed;
files modified;
indexing status;
usable-by-AI status.
```

The work context proposal may include Drive-derived sources only through professional labels such as `project active documents`, not raw folder IDs by default.

### Google Docs

Google Docs should be a drafting projection.

A selected paragraph may request a work context proposal, especially for sensitive rewriting. The add-on must not rewrite consequential wording without explicit acceptance.

### Google Sheets

Google Sheets should be a structured-data projection.

A selected range may request analysis or consistency checks. The add-on must not write back without explicit acceptance.

## UI requirements

A work context proposal card should show:

```text
request;
project detected;
mode recommended;
risk level;
included source families;
excluded source families;
missing evidence;
why this context;
buttons: use, modify, widen, narrow, refuse.
```

Recommended buttons:

```text
Use this context
Modify
Widen
Narrow
View why
Refuse
```

For high-risk work, `Use this context` should not imply approval of the final answer. It only accepts the retrieval perimeter.

## Context lock

Once accepted, a context should be locked for the response or branch it supports.

The UI should show:

```text
context locked;
source sets used;
source sets excluded;
missing evidence kept visible;
archives included or excluded;
AI drafts excluded by default.
```

A later answer should not silently change the perimeter. If the user asks to widen or narrow it, the system should create a new context proposal or branch.

The lock is data, not enforcement. `accepted_context_lock` is a recorded candidate field; the governance core does not hold a session or police retrieval across turns. Enforcement belongs to the consuming runtime (Hermes, OpenWebUI). Holding and policing a live lock inside the governance core would be session state — a runtime concern the boundaries forbid.

## Chokepoint and gate binding

This spec reuses existing governance, it does not invent a parallel decision path.

```text
human_decision_required maps to the User Decision Gate (USER_DECISION_GATE.md);
the governed retrieval handoff is a consequential effect and routes through the consequential chokepoint (PANTHEON_CONTROL_BOUNDARY.md);
accepting a context never canonizes a source: a Registre Probatoire change stays a governed candidate through the chokepoint and the gate, never a direct write.
```

Accepting a work context perimeter is a retrieval decision only. It is not approval of the final answer, not canonization of a source, and not a memory promotion.

## Microcopy

Prefer:

```text
Contexte de travail proposé;
Périmètre documentaire proposé;
Sources incluses;
Sources exclues;
Pièces manquantes;
Mode recommandé;
Contexte verrouillé;
Utiliser ce contexte.
```

Avoid:

```text
KB selected;
validated context;
trusted source set;
auto-approved sources;
use all documents;
include everything.
```

## Decision summary

Accepted as candidate orientation:

```text
users validate a work context, not a Knowledge Base list;
Hermes may propose the context;
Pantheon displays risk, exclusions, reservations and missing evidence;
accepted context is locked for the response or branch;
archives, old versions and AI drafts are excluded by default;
Contentieux mode may include important archives with labels.
```

Rejected:

```text
manual KB selection as default UX;
silent archive inclusion;
using AI-produced drafts as documentary sources by default;
retrieval success as proof;
context selection as final answer approval.
```

To verify:

```text
work_context_proposal promoted to a JSON Schema candidate in the governance core;
exact technical catalog shape;
Google projections extracted to a dedicated external-projections document;
Google Drive sync adapter;
OpenWebUI Knowledge mapping;
Hermes handoff payload;
context lock persistence and where enforcement lives (consumer, not core);
visual placement in the dashboard.
```
