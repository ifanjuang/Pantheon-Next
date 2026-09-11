# Hermes Integration Contract — MCP Policy Server

Status: implementation candidate — integration contract for the bounded `mcp-server/` module. Candidate until reviewed.

This contract describes how Hermes may call the Pantheon MCP Policy Server to frame work without Pantheon executing the work.

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

- list implemented consultation surfaces;
- explain allowlisted architecture placement from governed sources;
- qualify caller-provided capability-status candidates;
- classify requests on the K/V/C axes;
- project the smallest currently relevant governance handling;
- validate capability passports and governed references;
- prepare Task Contract and Evidence Pack candidates;
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

`get_capability_status` does not discover live status. An external producer gathers operational signals; the MCP only qualifies the supplied candidate.

```text
connected != consulted
consulted != obeyed
reported status != runtime probe
qualified candidate != authorized capability
```

## Request intake: conditions, not a domain-specific ontology

Pantheon does not need to become the language-understanding runtime.

Hermes may describe the request using a small set of **governed conditions**. The preferred vocabulary is the existing trigger vocabulary owned by `ROLE_ACTIVATION.md`.

Example:

```yaml
intent: prepare a bounded response
requested_transformation: rewrite
conditions:
  - source_required
  - legal_or_professional_risk
```

Another domain may use a different subset:

```yaml
conditions:
  - project_history_reuse
  - evidence_gap
  - external_transmission
```

The handling core does not need to know whether the underlying subject is architecture, legal work, software, finance, administration or another domain. Domain packs may add context and source expectations outside this generic mechanism.

Legacy fields such as `professional_position`, `financial_or_contractual_effect` or `prior_state_required` may be accepted as compatibility aliases while callers migrate, but they are not the core ontology.

```text
condition supplied != truth
condition supplied != consequence classification
condition supplied != Role authority
condition supplied != authorization
```

Raw intent matching remains a conservative compatibility fallback. Generic wording such as `confirm` / `confirmer` must not by itself create a high-consequence professional position.

## Progressive handling projection

`classify_request` remains authoritative for K/V/C classification. Its response may additionally contain a bounded `handling` projection.

The handling projection answers only:

```text
May work continue now?
Which existing governance viewpoints materially matter?
Does coordination need an existing topology?
What observable conditions must be satisfied before relying on the result?
Which material changes require reconsultation?
Is a decision gate required before the requested effect?
```

It does not prescribe Hermes internal execution mechanics.

Three dispositions are sufficient:

```text
PROCEED  -> no additional governance consultation is currently material
CONSULT  -> satisfy the current governance requirements before relying on the result
GATE     -> the requested consequential effect cannot occur before the applicable decision gate
```

A high-consequence candidate may still be `CONSULT` while being prepared or reviewed. The gate constrains the effect, not every prior analytical step.

### Minimal output

For a harmless formatting or draft operation:

```yaml
disposition: PROCEED
role_viewpoints: []
completion_requirements: []
constraints:
  - preserve_claim_status_and_meaning
```

For a request that needs several governance concerns:

```yaml
disposition: CONSULT
conditions:
  - source_required
  - legal_or_professional_risk
role_viewpoints:
  - ARGOS
  - THEMIS
topology:
  suggested: sequential_handoff
completion_requirements:
  - supporting_basis_qualified
  - consequence_boundary_reviewed
```

For an effect request:

```yaml
disposition: GATE
effect_gate:
  required_approval_ceiling: C4
  required_before_effect: true
  effect_requested_now: true
```

## Reuse existing Role and topology mechanisms

Role participation follows `ROLE_ACTIVATION.md`. A viewpoint is governance attention, not an autonomous worker.

The progressive handler consumes only an implemented subset of that document's existing trigger vocabulary. Tests bind the code mapping back to the doctrine so the MCP cannot silently create a second Role-trigger authority.

Task topology reuses the existing Task Contract vocabulary. Emit topology only when it changes the legitimate coordination path:

```text
one relevant viewpoint
  -> no topology emitted

supporting basis must precede consequential judgement
  -> sequential_handoff

source state and continuity/currentness can be established independently
  -> fanout_extract_then_single_synthesis

several viewpoints are relevant with no proven dependency
  -> parallel_independent_workers
```

```text
topology selected != workers dispatched
parallel viewpoints != punctual consultation
consultation != approval
completion requirement satisfied != authorized effect
```

A punctual consultation between Role qualities remains distinct from runtime parallelism.

## Generic completion requirements

Pantheon should not precompute a full task tree. It should expose only the smallest observable requirements needed for the next legitimate transition.

The V1 projection deliberately uses broad, reusable requirements:

```text
scope_and_method_bounded
supporting_basis_qualified
current_state_qualified
consequence_boundary_reviewed
delivery_boundary_qualified
```

These are projection terms, not a new persistent milestone ontology. They summarize meanings already owned by Task Contracts, governed workflow phases, expected outputs and completion criteria.

Domain-specific work may refine what counts as satisfying a requirement, but should not replace the generic mechanism.

## Conflict and rites

Conflict is treated as a generic observed condition, not as a new workflow type.

When a material conflict is reported and an Evidence/source concern is active, Pantheon may propose the existing `concordance_des_sources` rite.

```text
conflict detected != contradiction resolved
rite proposed != rite executed
rite completed != truth approved
```

## Reconsultation on material change

Hermes does not need to reconsult Pantheon after every internal step.

Reconsult only when a materially relevant governed condition becomes newly true, for example:

```text
source_required
evidence_gap
source_freshness_risk
project_history_reuse
duplicate_or_supersession_risk
legal_or_professional_risk
liability_risk
external_effect
external_transmission
memory_promotion
approval_required
policy_conflict
```

The request is then classified again with the newly observed candidate conditions.

```text
current governed state
  -> smallest required transition conditions
  -> Hermes works externally
  -> material condition changes?
       no  -> continue
       yes -> reconsult classify_request
```

A material change of cap, scope, responsibility or destination still follows the Task Contract revision rules owned by `REQUEST_LIFECYCLE.md` and `TASK_CONTRACT_REVISIONS.md`.

## K0 fast exit

The canonical Glossary defines K0 as including orientation, formatting, local display and harmless drafts.

A declared harmless transformation such as `rewrite`, `wording`, `polish`, `formatting` or `summary` may therefore remain K0 when no stronger consequence signal is present.

```text
K0 harmless transformation
  -> no Task Contract solely because text exists
  -> no scope gate solely because text exists
  -> PROCEED unless another material condition appears
```

This is what makes "Pantheon always consulted" compatible with a light everyday experience.

## Target sequence

```text
1. The user sends a request through an admitted Hermes client.
2. Hermes receives it and may describe applicable governed conditions.
3. Hermes calls mcp.classify_request.
4. Pantheon returns K/V/C plus the smallest current handling projection.
5. PROCEED -> Hermes continues inside the admitted boundary.
6. CONSULT -> Hermes satisfies only the listed completion requirements using the relevant viewpoints/topology.
7. A material condition changes -> Hermes reconsults classify_request.
8. Task Contract / Evidence Pack candidates are prepared only when their existing rules require them.
9. Hermes executes outside Pantheon.
10. GATE -> the consequential effect waits for the applicable human decision.
```

Execution remains outside Pantheon.

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

## Compliance tests

`mcp-server/tests/test_progressive_request_handling.py` verifies at least:

```text
harmless rewrite -> K0 / PROCEED / no Task Contract
source basis before consequential judgement -> sequential handoff
source + continuity -> fanout then synthesis
material conflict -> existing rite candidate
external transmission -> gate
conditions remain candidate inputs
Role-trigger code mapping remains a subset of ROLE_ACTIVATION.md
```

The tests validate policy projection only. They do not run Roles, workflows, rites or external effects.

## Final rule

```text
Hermes describes material conditions and performs admitted work outside Pantheon.
Pantheon classifies consequence and exposes only the smallest current governance requirements.
Roles provide bounded viewpoints; topology expresses coordination only when needed.
Material condition changes trigger reconsultation.
The gate constrains consequential effects.
The human decides.
```
