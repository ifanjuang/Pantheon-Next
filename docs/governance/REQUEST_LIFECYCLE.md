# Request Lifecycle

Status: active support doctrine — the governed lifecycle of a request, from situated comprehension to human engagement — implemented as documentation.
Boundary profile: active_support_doctrine.

This document defines the moments a request passes through, who holds the goal (the cap), how the cap is re-evaluated, and who guards the threshold of memory. It connects the Governance College, the Task Contract, the rites and the autonomy doctrine into one lifecycle.

Runtime/client boundary: see `HERMES_INTEGRATION.md`. This document owns lifecycle choreography only; execution remains external and consequential memory or engagement gates remain separately governed.

## Core thesis

A request is not just executed. First its real demand is understood, a heading (the cap) is set and held, the College works the path, the status is arbitrated, and the human engages. Most of this is autonomous; control attaches only where consequence earns it (`EXECUTION_MINIMALISM.md`).

```text
Understand the cap. Hold the cap. Work the path. Arbitrate the status. The human engages.
```

The cap is the goal. The path is the method. Pantheon governs the cap; it trusts the path.

## The lifecycle

```text
request
  -> triage: direct or fuzzy?
       direct  -> act (autonomy); no MÈTIS
       fuzzy   -> convene MÈTIS
  -> MÈTIS: understand the situated demand, set the cap
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

`active_support_doctrine` boundary profile applies. Locally, this document does not promote MÈTIS, CERBÈRE or CHARON into canonical registries, authorize runtime execution, or admit memory; those remain separate governed steps.

```text
MÈTIS understands and holds the cap, when the demand is unclear.
The College works the path.
CERBÈRE and CHARON guard the threshold of memory.
ZEUS arbitrates the status, on evidence.
The execution runtime executes outside.
The human decides at the cliffs and engages.
```