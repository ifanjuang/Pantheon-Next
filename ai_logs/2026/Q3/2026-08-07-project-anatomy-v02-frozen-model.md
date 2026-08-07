# AI log — Project Anatomy V0.2 conceptual freeze

Date: 2026-08-07
Scope: documentation only
Branch: `docs/project-anatomy-v02-frozen-model`
Base: `98be3a1dd07be6b6ee2847127d698618f6ff703a`

## Context

After the V0.2 core-schema refactor and explicit V0.1 compatibility layer merged, Project Anatomy was re-evaluated against Revit 2027, IFC/IDS, PDF/OpenTakeoff, site observations, economy, RE2020, ACV/carbon, Hermes orchestration, incomplete source sets and indexed plan revision workflows.

The discussion converged on a smaller semantic core and explicit extension mechanisms rather than adding more project-world carriers.

## Frozen decisions

The Project Anatomy core remains:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

`requirement` remains prescriptive intent outside the four project-world primitives.

Additional decisions frozen conceptually:

- no growing canonical BIM `kind` taxonomy on `stable_object`;
- domain semantics extend through versioned profiles and governed predicate/relation registries;
- structural facets are derived/indexed projection material, not new authority;
- coordinated indexed drawing/file issues are represented conceptually as Revision Sets outside APU core;
- source representations may exist before stable identity is resolved;
- coverage controls whether source absence may be interpreted;
- missing data is normal and must not be filled with synthetic `unknown` claims by default;
- claims are temporal/append-oriented; later observations do not erase historical claims;
- no universal stored `current_value`; purpose-specific lenses calculate projections;
- Hermes/adapters should emit bounded Observation Bundles/candidates rather than write APU persistence directly;
- Revit/IFC high-density adapters should be delta-first where practical;
- missing source occurrence is not automatic Project-object deletion;
- object replacement/split/merge/retirement preserves history;
- consequential Change Requests should be anchored to an exact Revision Set/baseline and rebased if the Project has advanced;
- Evidence, Proof, ProjectClaim, Decision and WorkIssue remain outside APU authority;
- future Proof qualifies sufficiency for a declared purpose rather than universal truth;
- raw adapter data is not automatically retained as Project Anatomy knowledge.

## Repo-state discipline

Implemented at contract/validation level on Pantheon-Next main:

```text
V0.2 core schemas
V0.1 explicit compatibility posture
MCP/read-only validation compatibility
```

Implemented in `pantheon-mvp` before this freeze:

```text
H1/H2/H3 executable APU slices against the pre-V0.2 carrier
```

Documented non-implemented at freeze time:

```text
H4c V0.2 executable owner migration
Revision Set contract
Profile/Predicate Registry
Observation Bundle contract
semantic lens policy
purpose-specific Proof model
production Revit add-in
```

## Boundaries preserved

```text
source != Project truth
source representation != stable object
missing != deleted
same revision != source agreement
claim != ProjectClaim
claim != Evidence
latest != universally applicable
projection != authority
accepted for one purpose != accepted for every purpose
Hermes output != APU mutation
successful Revit transaction != governance approval
```

## Change control

The conceptual model is frozen before H4c and Revit adapter implementation. New profiles, predicates, relations, lenses and adapter bindings may evolve without reopening the core. Adding a fifth project-world primitive, embedding Evidence/Proof/approval inside APU, making source-native ids authoritative identity, or introducing an ungoverned extension bag requires a separate architecture review.

No schema, test, runtime, persistence, Revit execution, provider routing, approval or external effect is changed by this documentation slice.