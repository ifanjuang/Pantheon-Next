# Hermes Integration Contract — MCP Policy Server

Status: implementation candidate — integration contract for the bounded `mcp-server/` module. Candidate until reviewed.

This contract describes how Hermes may call the Pantheon MCP Policy Server to frame work without Pantheon executing the work.

This document names a concrete surface (the bounded `mcp-server/` module) rather
than restating the generic separation, so it declares the boundary fields
directly instead of a `Boundary profile` line (`BOUNDARY_PROFILES.md`'s
"Inherited role separation" covers only the generic case):

```text
exposed_by:  Hermes Web/dashboard, or another compatible client
executed_by: Hermes Agent, outside Pantheon
governed_by: Pantheon Next, via the bounded mcp-server Policy Server
             (read-only / validation / candidate-preparation only)
approved_by: the human, at the gate
forbidden:   execute business work; send externally; write files or state;
             approve a result; promote memory or write a Registre Probatoire
             entry; install, schedule, queue or route providers
```

## Boundary

The MCP Policy Server is read-only / validation / candidate-preparation only.

It may:

- list which consultation surfaces are implemented, partial or documented non-implemented;
- explain allowlisted architecture placement and cite its governed sources;
- qualify a caller-provided capability-status candidate without probing a runtime;
- classify a request on the K/V/C axes;
- project the smallest currently relevant governance handling from caller-provided semantic observations;
- validate a capability passport;
- prepare candidate skeletons for Task Contracts and Evidence Packs;
- run read-only doctor checks;
- return policy decisions as data.

It must not:

- execute business work;
- send externally;
- write files or state;
- approve a result;
- promote memory or write a Registre Probatoire entry;
- install, schedule, queue or route providers;
- become a natural-language planner, hidden router, role runtime or workflow engine.

## Optional consultation preflight

Before task classification, Hermes may use:

```text
get_consultation_catalog
  -> discover what this MCP actually implements

explain_architecture(topic)
  -> retrieve placement, rationale, boundaries and governed source references

get_capability_status(status_yaml)
  -> qualify a status candidate already supplied by an external producer
```

`get_capability_status` does not discover live status despite its client-facing
name. The installable Hermes dashboard plugin, or another separately governed
producer, gathers operational signals; the MCP only checks the provided vocabulary, keeps status axes
separate and reports evidence/freshness/scope gaps.

The shared observation envelope keeps these axes distinct:

```text
listed | detected | installed | configured | enabled | reachable | health
governance_status | task_use_status
```

`update_status` and `rollback_status` are optional lifecycle extensions. A
dashboard `policy.governance` placement label is not a Pantheon approval
record and cannot establish `governance_status` by itself.

```text
connected != consulted
consulted != obeyed
reported status != runtime probe
qualified candidate != authorized capability
```

## Semantic intake candidate

Pantheon does not need to become the language-understanding runtime.

Hermes may describe what it observes in the request using explicit semantic
candidate fields. Typical examples are:

```yaml
intent: rewrite_email
requested_transformation: rewrite
observations:
  source_required: false
  prior_state_required: false
  professional_position: true
  financial_or_contractual_effect: false
  contradiction_detected: false
  recipient_specific_output: true
```

These observations are inputs to policy qualification only.

```text
Hermes observation != truth
semantic candidate != consequence classification
semantic candidate != Role authority
semantic candidate != authorization
```

Pantheon remains responsible for the governance consequence of the described
request. Hermes remains responsible for interaction and external execution
inside the admitted boundary.

Raw intent matching remains a conservative compatibility fallback. Ambiguous
ordinary language must not be treated as a professional commitment solely
because it contains a generic verb such as `confirm` / `confirmer`; professional
position should be represented explicitly by the semantic intake when known.

## Progressive handling projection

`classify_request` still owns K/V/C classification. Its response may additionally
contain a bounded `handling` projection produced from the request candidate and
the classification.

The handling projection answers only:

```text
What may happen next?
Which governance viewpoints materially matter now?
Is an existing reasoning topology useful?
What state must be established before moving on?
Which material changes require reconsulting Pantheon?
Is a gate required before the requested effect?
```

It does not answer how Hermes should internally execute the work.

Three dispositions are sufficient:

```text
PROCEED  -> no additional governance consultation is currently material
CONSULT  -> establish the named state with the named viewpoints before relying on the result
GATE     -> the requested consequential effect cannot occur before the applicable decision gate
```

A K4 request may still be `CONSULT` while preparing or reviewing a candidate.
The gate constrains the consequential effect, not every preceding analytical
step.

Example harmless wording request:

```yaml
disposition: PROCEED
role_viewpoints: []
constraints:
  - preserve_claim_status_and_meaning
```

Example consequential draft requiring a factual basis first:

```yaml
disposition: CONSULT
role_viewpoints:
  - ARGOS
  - THEMIS
topology:
  suggested: sequential_handoff
next_state:
  purpose: establish_factual_basis
  completion_requires:
    - applicable_source_basis_qualified
constraints:
  - do_not_strengthen_unverified_professional_claim
reconsult_if:
  - contradiction_detected
  - external_transmission
```

Example effect request:

```yaml
disposition: GATE
effect_gate:
  required_approval_ceiling: C4
  required_before_effect: true
  effect_requested_now: true
```

## Existing Role and topology vocabulary

The handling projection reuses existing owners rather than creating a second
workflow model.

Role participation follows `ROLE_ACTIVATION.md`. A viewpoint is governance
attention, not an autonomous worker.

Task topology reuses the existing Task Contract vocabulary. The V1 handling
projection uses topology only when it changes the legitimate coordination path:

```text
single relevant viewpoint
  -> no topology needs to be emitted

source/evidence basis must precede professional judgement
  -> sequential_handoff

source qualification and prior-state/currentness can proceed independently
  -> fanout_extract_then_single_synthesis

several independent viewpoints, with no proven dependency
  -> parallel_independent_workers
```

A topology recommendation is governance metadata only.

```text
topology selected != workers dispatched
parallel viewpoints != consultation
consultation != approval
phase complete != authorized effect
```

A punctual consultation between role qualities remains distinct from runtime
parallelism. A material contradiction may propose the existing
`concordance_des_sources` rite; proposing the rite does not run it.

## Next state, not full plan

Pantheon should not precompute the whole execution tree. The handling projection
names only the next governed state that must be established when such a state is
material.

Examples:

```text
establish_factual_basis
establish_current_state
assess_professional_consequence
```

Completion requirements are observable governance conditions, not hidden chain
of thought and not a new milestone ontology.

The projection deliberately reuses the meanings already owned by Task Contracts,
Workflow governed phases, expected outputs and completion criteria. It does not
add a `milestone`, `objective graph` or second workflow schema.

## Reconsultation on material change

Hermes does not need to reconsult Pantheon after every internal step.

Reconsult when a material governance condition becomes newly true, for example:

```text
contradiction_detected
source_required
evidence_gap
professional_position
financial_or_contractual_effect
liability_risk
external_effect
external_transmission
memory_promotion_requested
writes_state
```

The request is then classified again with the newly observed candidate facts.
No separate hidden workflow state machine is required.

```text
current state
  -> smallest legitimate next state
  -> Hermes works externally
  -> material condition changes?
       no  -> continue
       yes -> reconsult classify_request
```

A material change of cap, scope, responsibility or destination still follows the
Task Contract revision rules owned by `REQUEST_LIFECYCLE.md` and
`TASK_CONTRACT_REVISIONS.md`.

## Target sequence

```text
1. The user sends a request through an admitted Hermes client.
2. Hermes receives the request and may prepare bounded semantic observations.
3. Hermes calls mcp.classify_request.
4. Pantheon returns K/V/C plus the smallest current handling projection.
5. If PROCEED, Hermes continues inside the admitted boundary.
6. If CONSULT, Hermes establishes only the named next state using the relevant viewpoints/topology.
7. If a material reconsult condition appears, Hermes calls mcp.classify_request again with the new observation candidate.
8. If a Task Contract is required, Hermes prepares/reviews it through the existing candidate path.
9. Hermes executes, outside Pantheon, only the admitted work.
10. Evidence Pack Candidate preparation and result review follow existing owners when required.
11. If GATE applies to the requested effect, the human accepts, refuses, revises or escalates.
```

Execution remains outside Pantheon. The MCP Policy Server does not perform it.

## Expected Hermes output envelope

```text
RESULT_CANDIDATE
EVIDENCE_PACK_CANDIDATE
STATUS                 # candidate | to_verify | blocked
SCOPE_USED
APPROVAL_NEEDED        # C0..C5
REGISTER_CANDIDATE     # proposed only, never promoted here
LIMITS_AND_UNCERTAINTIES
```

Allowed status language:

```text
candidate
requires approval
scope unclear
blocked pending evidence
human decision required
```

Forbidden status language:

```text
approved
validated truth
authorized action
safe to execute
```

## Compliance fixtures and tests

`mcp-server/fixtures/sequence_conformance.yaml` keeps the existing candidate and
refusal sequence coverage.

`mcp-server/tests/test_progressive_request_handling.py` adds focused regression
coverage for progressive handling, including:

```text
appointment confirmation != professional confirmation
professional claim -> consult before effect gate
source + prior state -> fanout then synthesis
material contradiction -> Concordance des Sources rite candidate
external transmission -> gate
semantic observations remain candidates, not truth
```

These tests validate policy projection only. They do not run roles, workflows,
rites or external effects.

## Final rule

```text
Hermes describes what it observes and performs admitted work outside Pantheon.
Pantheon classifies consequence and names only the next legitimate governance state.
Roles provide bounded viewpoints; topology expresses coordination only when needed.
Material changes trigger reconsultation.
The gate constrains consequential effects.
The human decides.
```
