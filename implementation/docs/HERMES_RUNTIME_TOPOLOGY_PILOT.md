# Hermes Runtime Topology Pilot

Status: implementation candidate — projection, read-only Cockpit topology view
and contradictory-review binding contract implemented; live `pantheon-governed`
Runs delegation not yet qualified.

## Objective

Use the public Hermes Agent 0.21.2 subagent lifecycle already available on the
Runs SSE surface without creating a Pantheon multi-agent runtime.

```text
Pantheon Role != Hermes subagent
Role viewpoint != worker identity
runtime parent_id != inferred causal edge
runtime completion != Evidence
runtime success != authorization
projection != persistence
```

## Runtime topology projection

`mvp_vertical.hermes_runtime_topology_projection.HermesRuntimeTopologyProjector`
accepts only public `subagent.start` and `subagent.complete` events. It retains
Hermes-reported `subagent_id`, `parent_id`, `delegation_id`, child session,
depth, status and bounded execution metrics. It deliberately omits
`output_tail`, subagent tool chatter and private reasoning.

The existing `HermesRoleTraceRelay` remains the sole upstream Runs SSE consumer
for a run. It now multiplexes two presentation event kinds from that one stream:

```text
role.stage       -> governed semantic Role presentation
runtime.subagent -> explicit Hermes worker topology
```

The SSE event name preserves that distinction. No relation is synthesized from
time, ordering, Role labels or handoff prose. A runtime worker is explicitly
marked `governed_identity: false`.

## Cockpit presentation

The composed Cockpit keeps the existing Role Trace Graph as DOM/CSS semantic
lanes and renders Runtime Hermes separately. The runtime view uses a lazily
loaded, integrity-pinned D3 tree layout only after a `runtime.subagent` event is
observed.

```text
Role Trace Graph
-> semantic responsibility lanes
-> no worker identity

Runtime Hermes
-> D3 hierarchy/tree presentation
-> explicit parent_id -> subagent_id relations only
-> synthetic run root is display containment only
```

D3 is not a state store, scheduler, causal model or authority source. A missing
parent event creates no inferred parent edge. Cycles are cut for display and
reported rather than repaired. If D3 cannot load, the Cockpit falls back to a
plain bounded list of observed worker identifiers and parent identifiers.

The main Cockpit continues to use the existing Swiper-owned collection motion.
On mobile, compact card collections expose an explicit fraction position while
preserving horizontal sibling swipe, vertical parent/child swipe and the
existing previous/next fallback when Swiper is unavailable. The Workspace
Cockpit remains a filtered dossier inventory and is not reinterpreted as the
same governed card carousel.

## `AUTOCRITIQUE_CONTRADICTOIRE` pilot

`mvp_vertical.hermes_contradictory_review_runtime` prepares the Hermes
`delegate_task` shape reviewed in Hermes Agent 0.21.2:

```text
tasks[]
  goal
  context
  output_schema
```

Only findings are model-authored:

```text
observations
analogous_occurrences
limits
```

Task Contract identity, candidate digest, binding identity, runtime execution
identity and Rite closure semantics remain caller-owned. A schema-valid child
result is passed through the existing deterministic
`contradictory_review.report_from_payload` compiler. The child cannot repair the
reviewed candidate, widen scope, create Evidence, approve output or close the
Rite.

## Qualification boundary

Repository implementation does not prove that the currently deployed
`pantheon-governed` profile exposes `delegate_task` through the exact Runs API
route used by the external Pantheon binding. The parallel runtime-profile work in
PR #1057 observed that the profile-prefixed Runs API reported its API-server
toolsets disabled even while the interactive profile had working MCP bindings.

Therefore this pilot is not activated merely because the projection and binding
contracts exist. Live acceptance must prove, on the exact selected Hermes
artifact and route:

1. `delegate_task` is present in the reviewed active Runs tool envelope;
2. the one-child `output_schema` contract validates and returns a bounded result;
3. `subagent.start` and `subagent.complete` expose the expected explicit runtime
   identifiers on the same admitted `run_id`;
4. no Role identity is assigned to the worker;
5. the existing contradictory-review candidate path remains non-authoritative;
6. no second Runs SSE consumer, scheduler, queue or retry loop is introduced.

Until those checks pass, the live capability remains unqualified rather than
silently falling back to inferred topology or simulated Role agents.
