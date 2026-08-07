# AI intervention — Project Anatomy V0.2 target core

Date: 2026-08-07
Repository: `ifanjuang/Pantheon-Next`
Branch: `docs/project-anatomy-v02-design-review`

## Request

Critically re-read the already documented/partially implemented Project Anatomy model before Revit 2027 hardens the contracts. The user explicitly authorized substantial redesign now, including protected-schema migration in subsequent reviewed PRs, because later changes would be more expensive.

## Repository state reviewed

Pantheon Next authorities and consumers reviewed included:

```text
docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md
docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
docs/domain-packs/architecture/PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
schemas/architecture-project-understanding/*
mcp-server/pantheon_mcp/apu.py
docs/governance/APPROVALS.md
schemas/architecture-proof-register/shared.schema.yaml
```

Downstream executable state reviewed in `pantheon-mvp`:

```text
mvp_vertical/apu_owner.py
```

Observed H1/H2 persistence remains intentionally narrow:

```text
project owner revision
stable_object payload
optional object_identity payload
object_relation payloads
append-only owner events
bounded add_match_to_existing_object
freshness + idempotency + authorization refs
```

The owner already has to enforce equality between duplicate identity fields, confirming that `stable_object` and `object_identity` overlap in executable code.

## Final V0.2 target

The design review now fixes four APU primitives:

```text
stable_object
source_representation
attribute_claim
relation_claim
```

Prescriptive intent remains separate:

```text
program
requirement
classification_scheme
```

Supporting provenance/governance stays outside the project-world primitives:

```text
derivation/calculation record
Proof Register Evidence
contradiction/conflict record
Approval/use grant
Decision Request/Decision
WorkIssue
ProjectClaim
Information
```

## Key decisions

### One identity carrier

`stable_object` becomes the sole durable project identity carrier. `object_identity` is targeted for deprecation, with nomenclature folded into `stable_object`.

### First-class source occurrence

Introduce `source_representation` for Revit/IFC/PDF/OpenTakeoff/photo/manual occurrences, including source version, native identifiers, locator, binding/adapter version, freshness, timestamp, coordinate frame and limitations.

### Claims may exist before identity resolution

`attribute_claim` and `relation_claim` may target source representations as well as stable objects. This lets adapters report source reality without manufacturing project identity.

### No separate representation-match carrier

The initial V0.2 idea of `representation_match` was simplified further. Source-to-project alignment is a relation claim:

```text
source_representation
-- identity.represents -->
stable_object
```

### One value channel

`attribute_claim` becomes the only canonical value-bearing claim. Property-set inline values, instance overrides, phase state, classification values and human overrides are migrated into claims/supersession semantics.

### One relation channel

`relation_claim` replaces `object_relation` and also carries source-level relations, project-level relations, grouping, spatial containment, instance/type links and source-to-project identity alignment.

### Requirements are not facts

`requirement` remains a separate prescriptive carrier and must be generalized beyond `from_program` so IDS, CCTP, contracts, client decisions and other admitted requirement sources can participate without being misrepresented as observed claims.

### Groups/spatial nodes collapse into stable objects + relations

`spatial_node`, `space_group` and `object_group` are targeted for deprecation as independent identity carriers.

### Information stays Information

`object_note` is targeted for deprecation. Notes/site observations/coordination notes remain Information linked to project entities; machine-actionable facts extracted from them become reviewed claims.

### Human correction preserves history

`human_override` becomes a human-authored superseding claim/relation. Original source claims are never mutated.

### Evidence authority remains unique

The duplicate APU evidence carrier is targeted for deprecation in favor of Architecture Proof Register Evidence references.

### Canonization moves out of the project-world core

The useful per-use approval semantics are retained, but as governance approval/use grants rather than as another project-object carrier.

### Derived deviations are not primitives

`deviation` becomes ResultCandidate + WorkIssue/Decision Request where consequential. `program_change` becomes requirement versioning + Decision rather than a second decision lifecycle.

## Target carrier disposition

Retain/generalize:

```text
stable_object
attribute_claim
derivation
calibration
program
requirement
classification_scheme
contradiction (epistemic support, not world core)
```

Introduce:

```text
source_representation
relation_claim
typed APU entity reference
```

Deprecate or migrate out of the V0.2 core:

```text
object_identity
stable_object.matches
spatial_node
space_group
object_group
object_relation
property_set.claims as value carrier
instance_override
phase_state
classification as a separate claim carrier
analysis_context_candidate
object_note
human_override as a separate carrier
APU-local evidence authority
doubt as an operational backlog
program_change lifecycle
deviation as a core object
canonization as an APU-world carrier
```

## Revit consequence

Future Revit 2027 output should be source-oriented:

```text
Revit Context Snapshot
source_representation observations
attribute claims about those representations
relation claims between representations
warnings / limitations
```

The add-in does not create canonical stable objects and does not directly own Project Anatomy writes.

## Compatibility requirements

Existing H2 event history must remain auditable. Migration must preserve stable object ids, owner/object revisions, command digests, authorization refs, idempotency keys, review refs and source candidate/artifact/execution references.

No migration may invent missing Evidence, certainty or approval state.

## Intervention scope

This branch still changes documentation only. Protected schema/runtime work is intentionally moved to stacked reviewed PRs so each authority change remains reviewable.

Recommended dependency order, not a delivery schedule:

```text
#580 target model
-> protected core schemas
-> compatibility/MCP validator/examples
-> pantheon-mvp persistence owner
-> Revit/IFC/IDS/OpenTakeoff DTOs
-> Cockpit projections
```

## Final rationale

The refactor deliberately makes the model smaller while preserving or strengthening provenance.

```text
fewer carriers != less proof
simpler project model != weaker governance
one claim channel != one source of truth
```

This is the preferred moment to absorb the migration cost before production adapters make the V0.1 overlaps expensive to remove.