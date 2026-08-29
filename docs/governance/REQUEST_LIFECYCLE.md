# Request Lifecycle

Status: active support doctrine — the governed lifecycle of a request, from situated comprehension to human engagement — implemented as documentation.
Boundary profile: active_support_doctrine.

This document defines the moments a request passes through, who holds the goal (the cap), how governance depth adapts to consequence, how a Case / Situation is clarified before workflow forging, how the cap is re-evaluated, and who guards the threshold of memory. It connects the Governance College, the Task Contract, the rites and the autonomy doctrine into one lifecycle.

Runtime/client boundary: see `HERMES_INTEGRATION.md`. This document owns lifecycle choreography, proportional request activation and the documentary Case / Situation intake brief only; execution remains external and consequential memory or engagement gates remain separately governed.

## Core thesis

A request is not just executed. First its real demand is understood, a heading (the cap) is set and held, the required governance owners are activated proportionally, the professional situation is clarified enough for the next method boundary, the College works the path, the status is arbitrated, and the human engages. Most of this is autonomous; control attaches only where consequence earns it (`EXECUTION_MINIMALISM.md`).

```text
Understand the cap. Hold the cap. Clarify the situation. Activate only what consequence requires. Work the path. Arbitrate the status. The human engages.
```

The cap is the goal. The path is the method. Pantheon governs the cap; it trusts the path.

## The lifecycle

```text
request
  -> triage: direct or fuzzy?
       direct  -> act within the allowed autonomy envelope
       fuzzy   -> convene MÈTIS
  -> MÈTIS: understand the situated demand, set the cap
  -> clarify the minimum Case / Situation brief when the request must be forged into an Approach or Workflow Candidate
  -> activate only the context/source/risk/memory/evidence owners required by consequence
  -> ZEUS arbitrates the cap:
       sufficient            -> proceed
       insufficient / fuzzy  -> back to MÈTIS to deepen (bounded)
       touches engagement    -> human decision gate
  -> the College works the path (Argos, Thémis, Apollon, Héphaïstos, Iris)
       MÈTIS holds the cap and re-reads it as answers arrive
       a material change of cap -> governed revision (ZEUS / human)
  -> ZEUS arbitrates status, on evidence
  -> the execution runtime executes, outside Pantheon
  -> the human decides at cliffs and engages
CERBÈRE and CHARON guard the threshold of memory throughout.
```

## Proportional activation

The lifecycle is always the governing frame, but every request does not need every governance owner.

Use the smallest owner set that matches the request and its possible consequence:

```text
simple, clear, low-consequence request -> light handling inside the autonomy envelope
unclear cap or multi-intent request      -> MÈTIS / cap clarification
context dependency or missing context    -> CONTEXT_STACK.md
source dependency or freshness gap       -> SOURCE_NEED_AND_REGISTRY.md / ARGOS
liability or external effect             -> THEMIS + policy / approval / human gate as applicable
memory or durable-retention effect        -> MEMORY.md and applicable memory gates
candidate output                          -> Evidence and approval posture appropriate to intended use
```

Proportional activation must not become a hidden router or workflow engine. It is a method rule for deciding which existing owners are relevant.

### Request decomposition

When the request needs more than light handling, separate the candidates before composing them:

```text
Request Candidate           -> what the user asked, as received
Cap Candidate               -> the situated aim proposed from the request
Expected Context Profile    -> context expected to safely proceed
Input Admission Candidate   -> what was supplied, retrieved, recalled or is absent
Source Need Candidate       -> what source is missing and why it matters
Output Intent Candidate     -> what kind of output is expected and under what status
Situated Approach Candidate -> what method motifs are composed for this situation
Result Candidate            -> output produced by a role, runtime or adapter
Evidence Pack Candidate     -> review material supporting or contradicting assertions
Gate / Decision             -> accepted, refused, to_verify, to_arbitrate or blocked
```

These are governance objects or documentary candidates. They do not execute.

Their detailed contracts remain with their existing owners.

### Input is not output

Pantheon keeps available input separate from intended output:

```text
Input describes what is available.
Output describes what is requested.
The governed approach constrains the transformation.
```

Input availability never authorizes final output by itself. The same corpus may support an internal orientation but remain insufficient for a source-backed claim, external transmission, durable memory or another consequential effect.

### Complexity drivers

Governance depth increases when a material driver increases, including:

```text
cap ambiguity
multi-intent request
project-specific fact
context or source dependency
evidence dependency
freshness dependency
contradiction
regulatory or contractual effect
professional responsibility
external visibility or action
memory or register effect
sensitive input
```

### Owned context and source seams

This lifecycle activates, but does not redefine, the specialist owners:

- `CONTEXT_STACK.md` owns context composition, sufficiency states, Context Stack Change Candidates and the candidate HESTIA boundary;
- `SOURCE_NEED_AND_REGISTRY.md` owns Source Need Candidate structure, source families, source routes, registry semantics and freshness policy;
- Evidence, approval and memory remain with their respective owners.

```text
missing context -> consult context sufficiency -> narrow, request context or escalate
missing source  -> Source Need Candidate -> permitted retrieval handoff -> source/evidence review
```

Retrieved material remains candidate until the applicable source and Evidence owners qualify it.

### Output consequence and safe defaults

Output intent determines how much governance is needed. Typical output families include orientation, internal draft, extraction candidate, source-backed claim, document/comparison candidate, pre-transmission candidate, external-action preparation, memory candidate and register candidate.

When cap, context, source status or output consequence is unclear, prefer:

```text
allow orientation only
allow draft only
mark missing source or context
surface assumptions
request source or context
block external action
block memory promotion
send to ZEUS or human gate when required
```

## Case / Situation intake brief

When a request must cross from situated comprehension into Approach selection or Workflow Candidate forging, create a short documentary intake brief first.

`Case / Affaire` is the governed professional unit. `Situation` is the concrete question or tension. `Corpus` is a document set. A filesystem folder or colloquial dossier is not the governed Case identity.

The legacy identifier `dossier_situation_brief` and field name `dossier_situation_brief_ref` are retained as compatibility vocabulary for existing documentary examples and Workflow Candidate shapes. New explanatory text should read them as **Case / Situation brief**.

### Intake is a function, not a Role

The brief composes existing viewpoints; it creates no new canonical Role:

| Viewpoint | Intake contribution |
|---|---|
| IRIS | clarify wording, intended audience and requested effect |
| ATHENA | structure the Situation and identify an Approach / Workflow Candidate family |
| ARGOS | identify required sources, versions, provenance and evidence gaps |
| THEMIS | identify risk, liability, approval and external-effect boundaries |
| APOLLO | check completeness and delivery readiness of the brief |
| ZEUS | arbitrate status and next procedure when ambiguity or conflict remains |
| HEPHAISTOS | forge a later artifact or Workflow Candidate; not intake authority |

### Minimum documentary shape

```text
dossier_situation_brief:   # compatibility identifier; means Case / Situation brief
  request:
    raw_user_request:
    clarified_request:
    requested_output:
    requested_effect:
  project_identity:
    official_name:
    aliases:
    address:
    commune:
    parcel_refs:
    project_type:
  phase:
    user_says:
    contract_phase:
    operational_phase:
    contradiction:
  geography_and_rules:
    jurisdiction:
    PLU_zone:
    ABF_or_heritage:
    ERP_context:
    known_constraints:
  sources:
    received_now:
    required:
    available:
    missing:
    superseded_or_uncertain:
  versions:
    latest_plan_known:
    latest_notice_known:
    incoming_document_index:
    version_conflicts:
  contract_scope:
    mission_reference:
    in_scope:
    out_of_scope:
    unclear:
  relation_context:
    client_tension:
    authority_or_ABF_tension:
    contractor_tension:
    insurer_or_claim_context:
  risk_triggers:
    safety:
    cost:
    schedule:
    external_commitment:
    professional_liability:
  memory_and_register:
    runtime_memory_relevant:
    registre_entries_required:
    contradictions:
  blocking_questions:
  non_blocking_questions:
  recommended_next_status:
```

This is documentary vocabulary, not an executable schema. Any future schema belongs under `schemas/` and requires its own protected-path review.

### Intake statuses

| Status | Meaning |
|---|---|
| `ready_for_workflow_candidate` | enough information exists to forge a Workflow Candidate |
| `pending_clarification` | user wording or project target is ambiguous |
| `pending_source` | a required source, version or proof element is missing |
| `pending_contract_scope` | the mission boundary is unclear |
| `risk_review_required` | risk or tension requires Themis review before work continues |
| `zeus_arbitration_required` | conflicting candidate paths or statuses require arbitration |
| `blocked` | continuing would create false truth, unauthorized effect, wrong memory or another illegitimate consequence |

The brief remains candidate material. It does not answer the substantive question as final, send or publish, validate a professional position, mutate the Registre Probatoire, promote runtime memory or authorize a durable workflow.

Worked example: `../examples/architecture_erp_effectif_impact_workflow/` shows the richer ERP/effectif impact case without duplicating it here.

## MÈTIS — situated comprehension, keeper of the cap

MÈTIS is the role of situated, adaptive intelligence: she understands what is really being asked and holds the heading.

She is activated conditionally, not on every request:

```text
direct, clear, single-intent request   -> no MÈTIS; act
fuzzy, indirect, implicit-goal,         -> convene MÈTIS
multi-intent, contradictory,
or vague but consequential
```

A light triage (not MÈTIS herself, to avoid circularity) decides whether to convene her. MÈTIS may also be convened mid-course if answers reveal hidden ambiguity or complexity.

When convened, MÈTIS establishes the four things that matter for the métier:

```text
the real demand    (not the literal words)
the goal aimed at  (the professional outcome — the cap)
the watch-points   (what can go wrong in this domain)
the responsibility limit (where the system and the professional do not decide)
```

MÈTIS proposes; she does not arbitrate or engage.

## The cap and its re-evaluation

The cap lives in the Task Contract (`TASK_CONTRACTS.md`) as its intent.

It is held by MÈTIS and re-read against incoming answers. When the answers shift the picture:

```text
minor, within scope    -> MÈTIS adjusts, notes it, continues (reversible, logged)
material change of cap  -> MÈTIS proposes; a governed revision is required
   (the real demand, scope, responsibility or destination changes)
```

A material change of cap is a Task Contract revision (`TASK_CONTRACT_REVISIONS.md`), not a silent pivot. The system stays adaptive without drifting: it adjusts the heading when reality speaks, but never changes destination in secret.

## ZEUS arbitrates the cap and the status

ZEUS does not rubber-stamp the cap; he arbitrates its status. Three outcomes:

```text
validated          -> the College works
insufficient / fuzzy -> returned to MÈTIS to deepen
touches engagement  -> routed to the human (decision gate)
```

Bounds:

```text
The MÈTIS <-> ZEUS loop is bounded. After a few rounds without convergence, the
ambiguity is real and belongs to the human, not to more deliberation.
ZEUS validates the QUALITY of the framing, never the engagement. A well-framed but
consequential cap is declared sound, then routed to the human to engage.
ZEUS arbitrates; he does not re-comprehend in MÈTIS's place.
```

This loop is a bounded governed iteration, in the spirit of `rites/AUTOCRITIQUE_CONTRADICTOIRE.md`.

## CERBÈRE and CHARON — the threshold of memory

These are not judges. They are gates on the memory and record lifecycle (`MEMORY.md`, `SCOPE_ISOLATION.md`, `CORE_RECORDS_MODEL.md`), named for clarity. One controls entry of the past, the other exit into the archive.

```text
CERBÈRE  guards entry — filters what returns from the past
         (stale, to_reconfirm, out-of-scope memory is not admitted blindly)
CHARON   guards exit  — ferries what must no longer act into the archive
         (superseded -> archived, kept but inactive, never hard-deleted)
```

They run alongside the request, not as steps in it. They keep returning memory trustworthy and retire what should stop acting.

## Distinct natures — never confuse

```text
MÈTIS, ZEUS, and the College (Athéna, Argos, Thémis, Apollon, Héphaïstos, Iris) -> Roles (judgment)
CERBÈRE, CHARON                                                                 -> gates (memory operations)
the execution runtime                                                           -> runtime (external execution)
the human                                                                       -> decides at cliffs and engages
```

At every stage: proposing is not arbitrating is not engaging. MÈTIS proposes the cap; ZEUS arbitrates its status; the human engages.

## Canonical-registry note

This document proposes MÈTIS as a Pantheon Role and CERBÈRE / CHARON as memory-threshold gates. Promoting MÈTIS into the canonical role registry (`AGENTS.md`, `GOVERNANCE_COLLEGE.md`) and the gates into `MEMORY.md` / `CORE_RECORDS_MODEL.md` is a separate governed step. Until then this is active support doctrine describing the lifecycle, not a change to the canonical College roster.

## The consequential chokepoint

When the lifecycle reaches an effect that is consequential, that effect resolves through Pantheon's policy check before it touches the world. This is the chokepoint that makes Pantheon master in fact (`HERMES_INTEGRATION.md`, `UNIFORM_CAPABILITY_GOVERNANCE.md`).

```text
Non-consequential effect -> the runtime proceeds freely.
Consequential effect     -> the runtime asks the check, then proceeds only on an
                            allow / allow_with_gate decision, with an Evidence Pack.
```

The lifecycle decides what is consequential (the cap, the placement test); the chokepoint decides whether it may proceed. Neither runs the work.

## Boundary

`active_support_doctrine` boundary profile applies. Locally, this document does not promote MÈTIS, CERBÈRE or CHARON into canonical registries, authorize runtime execution, admit memory, or turn the intake brief into Evidence or workflow authority; those remain separate governed steps.

```text
MÈTIS understands and holds the cap, when the demand is unclear.
The lifecycle clarifies the minimum Case / Situation brief when needed.
The lifecycle activates only the owners consequence requires.
The College works the path.
CERBÈRE and CHARON guard the threshold of memory.
ZEUS arbitrates the status, on evidence.
The execution runtime executes outside.
The human decides at the cliffs and engages.
```