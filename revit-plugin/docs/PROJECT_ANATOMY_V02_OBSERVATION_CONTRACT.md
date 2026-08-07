# Revit 2027 ↔ Project Anatomy V0.2 observation contract

Status: documented, non-implemented.

Authority relationship:

- `docs/domain-packs/architecture/PROJECT_ANATOMY_MODEL.md` remains the sole conceptual authority for Project Anatomy V0.2;
- `docs/governance/REVIT_LOCAL_ADAPTER.md` remains the canonical Revit execution boundary;
- this note specializes the adapter output seam for Revit 2027 and does not create a second APU model, Evidence model, approval model or runtime;
- the production add-in and Host Agent remain external implementation artifacts.

## 1. Purpose

The Revit adapter must translate live Revit source reality into a bounded observation package that Pantheon can inspect, persist, review and later align with Project Anatomy V0.2.

The adapter does **not** decide project identity and does **not** directly create canonical project objects.

The stable flow is:

```text
Revit live state
    ↓
Revit Context Snapshot
    ↓
source-bound observations
    ↓
Observation Bundle candidate
    ↓
Hermes interpretation / matching candidate
    ↓
Pantheon review and governance
    ↓
Project Anatomy owner application
```

The following distinctions are invariants:

```text
Revit ElementId != stable_object_id
Revit UniqueId != stable_object_id
source representation stored != project truth
attribute observed != attribute accepted for every downstream purpose
relation observed != stable project-world relation
matching candidate != identity alignment admitted
runtime success != Evidence
transaction success != governance approval
```

## 2. Target implementation baseline

The first production binding targets:

```text
product: Autodesk Revit
release: 2027
target framework: .NET 10 / Windows, subject to final Revit 2027 API verification
execution: local only
Internet dependency: none
Autodesk Assistant dependency: none
Autodesk Public MCP dependency: none
APS dependency: none
```

This is an implementation target, not a current support claim.

The binding is not considered `supported` until the corresponding operation passes the live Revit 2027 conformance corpus.

## 3. Project Anatomy V0.2 primitives consumed by the seam

The adapter is designed around the frozen V0.2 project-world primitives:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

The adapter primarily contributes observations that can become:

```text
source_representation
attribute_claim candidate about a source_representation
relation_claim candidate between source_representations
```

An identity proposal between a Revit occurrence and an existing project object is represented by a candidate:

```text
relation_type = identity.represents
subject_ref = source_representation
object_ref = stable_object
```

Only the governed Project Anatomy owner may apply such an identity alignment.

The add-in must never manufacture a new `stable_object` merely because a Revit element exists.

## 4. Revit source representation

A Revit occurrence should map naturally to the governed `source_representation` contract.

Illustrative payload:

```yaml
representation_id: rep.revit.project-a.3f54...
project_ref: project-a
source_artifact_ref: source.revit.model-a
source_version_ref: snapshot.revit.model-a.00042
source_kind: revit
identifiers:
  - scheme: revit.unique_id
    value: "..."
  - scheme: revit.element_id
    value: "145772"
locators:
  - locator_type: native
    value: "revit://model-a/element/145772"
observed_at: "2026-08-07T21:00:00Z"
binding_ref: binding.revit-local.workstation-01
adapter_version: "0.1.0"
freshness_token: "sha256:..."
content_digest: "sha256:..."
context:
  document_ref: revit-document:model-a
  view_ref: revit-view:level-00
  phase_ref: revit-phase:new-construction
  design_option_ref: revit-option:main
  workset_ref: revit-workset:architecture
  level_ref: revit-level:00
  native_context:
    category: OST_Doors
    family: Porte intérieure
    type: P93
proof_status: candidate
limitations: []
evidence_refs: []
```

The exact locator and identifier schemes belong to the Revit binding/profile, not to the Project Anatomy core.

### 4.1 Native identifiers

The adapter should retain, when available:

- Revit `ElementId` as an execution locator valid only for the observed document state;
- Revit `UniqueId` as a more durable Revit-native identifier;
- document identity/fingerprint;
- linked-document identity when the observed element belongs to a Revit link;
- category/family/type identities as source classifications, not project identity;
- phase, design option, workset, level and view context.

No native identifier is sufficient by itself to establish Pantheon stable identity.

## 5. Revit Context Snapshot

Before an operation can emit observations, the add-in must be able to report the live execution context.

Minimum context:

```text
binding identity
plugin version
Revit version/build
document identity
read-only/modifiable state
worksharing state
active view
selection
phase context
design option context
units
coordinate context
observed_at
freshness token
```

The snapshot is source/execution context. It is not a Project Anatomy object.

A stale snapshot must be rejected for any operation whose contract requires live freshness.

## 6. Observation Bundle

Project Anatomy V0.2 identifies the Observation Bundle as the intended adapter seam. For the Revit binding, the bundle should be a bounded, immutable runtime return containing source observations and gaps, not canonical project truth.

Conceptual envelope:

```yaml
bundle_id: observation-bundle.revit....
project_ref: project-a
binding_ref: binding.revit-local.workstation-01
adapter_version: "0.1.0"
operation_id: revit.architecture.observe_scope.v1
request_id: request-...
observed_at: "..."
source_artifact_ref: source.revit.model-a
source_version_ref: snapshot.revit.model-a.00042
freshness_token: "sha256:..."
scope:
  document_ref: revit-document:model-a
  level_refs: [revit-level:00]
  categories: [OST_Rooms, OST_Doors]
representations: []
attribute_claim_candidates: []
relation_claim_candidates: []
coverage: {}
withheld: []
warnings: []
limitations: []
```

This note does not create a protected JSON Schema for that bundle. The executable schema should only be introduced after the V0.2 MVP owner seam is merged and the adapter contract is reviewed.

## 7. Attribute observations

An observed Revit value should become a candidate `attribute_claim` about its `source_representation`, not automatically about the project `stable_object`.

Example:

```yaml
attribute_claim_id: claim.revit.width....
subject_ref:
  entity_type: source_representation
  entity_id: rep.revit.project-a.3f54...
attribute_key: geometry.width
value:
  value_type: number
  value: 930
  unit: mm
assertion_mode: observed
source_authority: source_observation
proof_status: candidate
certainty: E4
source_representation_refs:
  - rep.revit.project-a.3f54...
```

The Revit profile must define which parameters map to which governed attribute keys.

Unknown or ambiguous mappings remain source-native data or are withheld; the adapter must not invent a project semantic key.

## 8. Relation observations

Relations directly observable in Revit may become candidate `relation_claim` records whose subjects and objects are source representations.

Examples include:

- hosted by;
- belongs to level;
- room/door adjacency when actually resolvable from the current model state;
- containment;
- source-native grouping;
- source-native type/instance relationships when a governed relation type exists.

If the relation requires inference beyond deterministic Revit state, it must carry the corresponding assertion mode/derivation rather than masquerading as a direct observation.

## 9. Identity alignment

Identity is outside the add-in authority.

The adapter may return enough observations for Hermes/Pantheon to propose:

```yaml
relation_type: identity.represents
subject_ref:
  entity_type: source_representation
  entity_id: rep.revit....
object_ref:
  entity_type: stable_object
  entity_id: object....
assertion_mode: proposed
source_authority: model_interpretation_candidate
proof_status: candidate
```

The add-in itself does not know whether that relation is professionally accepted.

If identity is unresolved, the `source_representation` remains valid and queryable without a stable-object link.

## 10. Delta-first observation

Revit is a high-density source. Full-model snapshots are therefore not the default continuous exchange unit.

The preferred pattern is:

```text
bounded baseline
+ explicit scope
+ source freshness
+ delta since baseline
```

A delta may describe:

```text
representation added
representation observed as changed
representation no longer found in the current source state
attribute observation changed
relation observation changed
```

But:

```text
representation no longer found != stable_object deleted
```

Deletion/retirement of project objects remains governed outside the adapter.

## 11. Coverage and absence

An empty observation is not automatically a negative project fact.

Every bounded extraction capable of supporting absence reasoning should report coverage, for example:

```yaml
coverage:
  scope_complete: true
  categories_observed:
    - OST_Rooms
    - OST_Doors
  filters:
    phase_ref: revit-phase:new-construction
    design_option_ref: revit-option:main
  linked_models_included: false
  excluded_reasons: []
```

Without sufficient coverage, Hermes/Pantheon must not infer that an object or property is absent merely because the bundle did not contain it.

## 12. Withheld, blocked, refused and failed

The Revit adapter should not collapse all non-success outcomes into an exception.

Recommended operational statuses:

```text
success
withheld
blocked
refused
failed
cancelled
rolled_back
```

Interpretation:

- `withheld`: observation/action could not be asserted safely from the available state; task may continue around it;
- `blocked`: dependency or user action is required;
- `refused`: contract, freshness, scope, safety or authorization conditions are not satisfied;
- `failed`: attempted technical execution failed unexpectedly;
- `rolled_back`: a transaction started but its effects were reverted.

Examples:

```text
family required but absent -> blocked
ambiguous room adjacency -> withheld
wrong active document -> refused_document_mismatch
stale context token -> refused_stale_context
worksharing ownership conflict -> blocked_worksharing
unexpected Revit API exception -> failed
```

A withheld action must not force unrelated task actions to stop.

## 13. Operation Registry integration

Every add-in operation must be declared in one closed Revit Operation Registry.

The registry is the implementation source for generating or checking:

```text
Capability Manifest
Host Agent tool bindings
advanced local exposure UI
documentation
conformance fixtures
```

Each entry should eventually carry at least:

```yaml
operation_id: revit.architecture.observe_rooms.v1
capability_id: building_model.observe.spaces
effect_class: read_only
warning_level: W0
revit_versions: [2027]
requires:
  active_document: true
  live_context: true
  transaction: false
outputs:
  observation_bundle: true
  source_representations: true
  attribute_claim_candidates: true
  relation_claim_candidates: true
local_exposure:
  configurable: true
preflight:
  required: false
tests:
  contract: required
  live_revit: required
```

The registry must not be generated by reflecting the Revit API.

An operation absent from the registry is not executable through Hermes even when technically possible in C#.

## 14. Shared human/agent operation layer

Manual plugin commands and Hermes-triggered commands must use the same deterministic operation implementation.

```text
Ribbon / local UI ─┐
                   ├─> Revit Operation -> Revit API
Host Agent/Hermes ─┘
```

There must not be a separate implementation of the same business operation for the agent path.

This parity is a testable requirement.

## 15. Revit 2027 units boundary

Revit internal units must not leak into the Pantheon/Hermes contract.

The external adapter contract should use explicit units suitable for professional architectural work, for example:

```text
length: mm or m as declared by the attribute profile
area: m²
volume: m³
angle: degrees when exposed to the agent
```

Conversions from/to Revit internal units remain inside the binding and must be covered by live tests.

No bare numeric value is sufficient when the governed attribute requires a unit.

## 16. Architecture-first capability scope

Initial observation scope should prioritize the first-wave architect responsibilities:

### Architecture

- document/view/selection context;
- levels/phases/design options/worksets;
- rooms and spatial boundaries;
- walls/floors/roofs/ceilings;
- doors/windows/openings;
- architectural families/types;
- materials and compound structures;
- views/sheets/schedules;
- warnings and model quality observations.

### Economy

- deterministic geometric quantities;
- occurrence/type counts;
- material quantities;
- deltas between bounded snapshots;
- schedule data.

### Construction / DET

- navigation to exact elements;
- source snapshots and visual captures;
- revision/delta observation;
- element presence/state required to verify a reviewed issue.

### RE2020 / thermal preparation

- envelope geometry and orientation;
- spaces/volumes;
- openings;
- material/composition observations;
- source parameters required by an external deterministic calculation adapter.

### ACV / carbon preparation

- material/component quantities;
- product/type identifiers when present;
- source classifications and provenance needed for later environmental mapping.

The Revit add-in does not become the regulatory engine, cost owner or carbon database.

## 17. Explicit exclusions

The first implementation must not expose:

```text
send_code_to_revit
execute_csharp
execute_python
eval
arbitrary reflection dispatch
arbitrary Revit API invocation
silent save
silent synchronize-with-central
automatic purge
generic unrestricted delete
provider/LLM calls from inside the add-in
project memory inside the add-in
workflow scheduler inside the add-in
```

Generated code remains `W5` and is not executable in V0.

## 18. Mutation seam remains separate

Observation compatibility with Project Anatomy does not authorize writes to Revit.

A future mutation still follows:

```text
ChangeCandidate
→ fresh Revit Context Snapshot
→ technical preflight
→ human/Pantheon authorization
→ exact bounded Operation Request
→ named Revit transaction
→ Action Report
→ result review
```

A Project Anatomy write and a Revit model write are distinct effects and must have distinct authorization paths.

## 19. Conformance expectations

Before a capability is marked supported on Revit 2027, its tests should cover at least:

- schema/input validation;
- invalid input -> structured refusal/error;
- wrong document;
- stale context;
- project units and Revit internal-unit conversion;
- phases;
- design options where relevant;
- worksharing where relevant;
- linked-model context where relevant;
- repeated invocation/no stale previous result;
- output binding to exact `request_id`/operation;
- live Revit result verification;
- no unexpected model mutation for read operations.

For write operations additionally:

- preflight;
- exact target set;
- named transaction;
- warnings/failures captured;
- rollback behavior;
- idempotency/retry posture;
- before/after effect report;
- no effects beyond the authorized scope.

## 20. Dependency posture

External projects reviewed during the Revit 2027 research are implementation references, not authorities.

Current candidates:

```text
Nice3point/RevitTemplates
→ candidate project scaffold / multi-version packaging patterns

Nice3point/RevitApi
→ candidate build-time Revit API references; redistribution rights still to verify

DTDucas/RevitMCPSDK
→ candidate source for command registry / JSON-RPC / ExternalEvent patterns;
  dependency adoption not yet decided

mcp-servers-for-revit and derivatives
→ command catalog + live-test references, not runtime dependencies
```

No external MCP repository is approved as Pantheon runtime by this contract.

## 21. First admissible executable proof

The first production-repo proof should remain intentionally small:

```text
1. load in Revit 2027;
2. identify binding/plugin build;
3. observe active document;
4. observe active view;
5. observe exact selection;
6. expose a closed capability manifest;
7. execute one bounded read operation through ExternalEvent;
8. emit one immutable observation bundle containing source representations;
9. demonstrate stale/wrong-document refusal;
10. demonstrate zero model mutation;
11. execute the same operation from local UI and Host Agent and obtain equivalent domain results;
12. succeed with Internet unavailable.
```

The proof does not require stable-object creation, Project Anatomy canonization, model write, save, sync, provider call or OpenWebUI integration.

## 22. Status

Documented:

- Revit 2027 target;
- V0.2 adapter-to-Anatomy mapping;
- source-representation-first posture;
- Observation Bundle shape;
- delta/coverage/refusal semantics;
- registry/parity/conformance expectations.

Not implemented by this repository:

- compiling Revit 2027 add-in;
- Host Agent;
- executable Observation Bundle schema;
- Operation Registry code;
- live Revit 2027 tests;
- Project Anatomy ingestion of adapter bundles;
- model mutations.

Nothing in this note upgrades those items from documented to implemented.
