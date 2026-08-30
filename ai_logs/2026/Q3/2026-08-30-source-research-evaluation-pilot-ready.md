# 2026-08-30 — source-research evaluation pilot readiness

## Objective

Prepare #824 D/E as a real baseline/current/candidate evaluation without inventing a generic eval subsystem or mistaking static contract checks for behavioral acceptance.

## Exact repository state

Branch base:

```text
main = 47ae870d128ca101f6c07f0ba93bf20be8c3b70e
```

No PR was open at pilot preparation time. The remaining open issues were revalidated; they represent current real-environment, legal/maintainer, document-parser or first-professional-vertical work rather than competing #824 evaluation owners.

## Existing owner reused

`hermes/profiles/_base/EVALUATION_AND_SIMULATION_CANDIDATE.md` remains the evaluation/simulation candidate. It is explicitly `not installed, not implemented` and no executable source-research A/B/C runner exists in the repository.

`PRE_EXECUTION_SIMULATION.md` remains the simulation-method owner. Evidence, approval, memory and Improvement Candidate consequences remain with their current owners.

No new evaluation doctrine, schema, service, runner, database, judge authority or benchmark registry is created.

## Exact A/B/C variants

```text
A = baseline without specialized source-research skill
    no SKILL.md loaded; exact runtime identity must be recorded at execution

B = pre-Slice-C source-research
    commit 80b2aa93365a84081ab114c31db2c11338dadc35
    path templates/hermes/skills/source-research/SKILL.md
    blob 4c85fdf96af45d3de5065e6dafdce5d7f1368aa8

C = post-Slice-C source-research
    commit 47ae870d128ca101f6c07f0ba93bf20be8c3b70e
    path templates/hermes/skills/source-research/SKILL.md
    blob bb382bc8dff12c1b1c338dbef516b9536f7a5ff9
```

B includes the converged bounded research method and optional source-notebook seam but predates #844.

C additionally includes:

- private-query minimization;
- exact external-transmission authorization boundary;
- secrets excluded from external retrieval surfaces;
- proportionate challenge search;
- decision-relevant stopping criterion.

## Representative corpus

`tests/fixtures/source_research_evaluation_pilot.json` contains nine manually reviewable cases:

1. source version changed;
2. official/derivative authority disagreement;
3. citation that does not support the claim;
4. unanswerable/absent information;
5. wrong jurisdiction/applicability;
6. freshness mismatch;
7. unnecessary private detail in an external query;
8. broad research requiring a stop condition;
9. supported claim requiring proportionate challenge search.

Every case carries:

```text
input
expected posture
required observations
forbidden claims/effects
human label
```

The corpus is synthetic and contains no client data.

## Measures retained

The fixture requests only useful dimensions:

```text
supported material claims
unsupported material claims
material contradictions detected
correct refusals
false refusals
scope drift
source/currentness errors
private-disclosure boundary errors
latency if observable
tokens if observable
cost if observable
```

No composite Pantheon quality score is introduced.

## Behavioral execution blocker

A true D/E comparison still requires one missing prerequisite:

```text
a reproducible sandbox runtime
that can load A/B/C as isolated instruction envelopes
on the same cases
with exact model/runtime identity
and return raw outputs plus observable latency/token/cost metadata
```

The current repository does not provide that runner, and the Hermes evaluation candidate explicitly states that it is not installed or implemented.

Creating canned expected outputs or checking only whether method clauses exist would violate an existing Pantheon distinction:

```text
structural validation != behavioral acceptance
```

Therefore the pilot state is:

```text
corpus + human labels + exact variant provenance = ready
behavioral A/B/C run                              = blocked_missing_reproducible_runtime
observed gains/regressions                       = not yet claimed
Improvement Candidate                            = not yet populated with fake observations
```

## D/E consequence

This is an explicit blocked pilot, not a successful evaluation.

The next admissible execution is to run the immutable corpus through a bounded sandbox runtime, retain raw outputs as observations, calculate only the declared dimensions, and then draft an Improvement Candidate containing observed gains, regressions, known failure modes, uncertainty and exact implementation provenance.

An evaluator/LLM judge may be added only as a review signal after comparison against the human labels. It must not become admission or approval authority.

## Slice F decision at this checkpoint

Do **not** introduce a machine evaluation schema now.

The current fixture plus existing simulation/Evidence/Improvement Candidate owners can represent the blocked pilot and the intended comparison. No distinct machine invariant has yet been demonstrated by an actual run.

```text
blocked pilot != schema gap
fixture useful != generic eval platform needed
no observed run != justification for more architecture
```

Reassess F only after behavioral execution produces concrete information that cannot be represented by existing structures.

## Repository cleanup context

Before preparing D/E:

- #839, #844 and #845 were merged;
- #721/#722 stale Dependabot PRs were closed for current-main reconstruction rather than merged from old topology;
- #661 Rowboat qualification was closed as speculative/no demonstrated need;
- no PR remained open;
- #731, #660, #659, #714, #644/#607, #662, #262 and #827 remain open for demonstrated current reasons;
- obvious temporary and superseded branch families were audited as deletion candidates, but the available GitHub connector exposes no branch-ref deletion operation.

This branch-cleanup limitation does not block D/E and must not be worked around by moving stale refs to `main`.

## Boundary

```text
fixture validated != capability behavior validated
runtime output != Evidence
score != approval
self-evaluation != self-admission
Improvement Candidate != automatic update
blocked execution != authorization to invent results
```
