# AI intervention — Project Anatomy V0.2 design review

Date: 2026-08-07
Repository: `ifanjuang/Pantheon-Next`
Branch: `docs/project-anatomy-v02-design-review`
Base observed: `a15f5c418560f292df1b915572b21a04fc9fdf23`

## Request

Re-read Project Anatomy critically after the Revit/AI/openBIM audit and after H1/H2 executable progress. The user explicitly allowed proposing substantial simplification or redesign where justified.

## Active repository state reviewed

Pantheon Next owners reviewed:

```text
docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md
docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md
docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md
docs/domain-packs/architecture/PROJECT_ANATOMY_KNOWLEDGE_STRUCTURE.md
docs/domain-packs/architecture/PROJECT_ANATOMY_IMPLEMENTATION_CONVERGENCE.md
docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md
schemas/architecture-project-understanding/* relevant identity/claim/relation/property schemas
mcp-server/pantheon_mcp/apu.py
```

Downstream executable state reviewed in `pantheon-mvp`:

```text
mvp_vertical/apu_owner.py
mvp_vertical/sql/021_project_anatomy_owner.sql
commit f1c0dcd56bafb9a8fd7a2be985ca6bc3340afd86
```

Current H2 owner behavior observed:

```text
project-scoped owner revision
stable-object persistence
optional object-identity persistence
relation persistence
freshness-bound add_match_to_existing_object
human authorization reference
idempotent replay
append-only owner event
no automatic canonization / Evidence / Decision / task authority
```

Open PR #579 was also checked for overlap. It touches OpenTakeoff/Revit adapter documentation but not the new V0.2 review file. This review deliberately remains separate.

## Main findings

### 1. Duplicate identity responsibility

`stable_object` and `object_identity` both carry stable id/kind/human identity material. The executable owner has to assert equality between them. Proposed simplification: one identity carrier, preferably `stable_object`, with nomenclature folded into it or with a subordinate value object that carries no duplicate id/kind authority.

### 2. Three value-bearing fact channels

`attribute_claim`, `property_set.claims` and `instance_override` can all hold project values/status/source material. Proposed simplification: `attribute_claim` becomes the sole canonical value-bearing fact carrier; property sets become organization/inheritance over claim refs; overrides become precedence/replacement relations between claims.

### 3. Spatial identity duplication

`stable_object.kind` and `spatial_node.node_kind` overlap for spaces and levels. Proposed simplification: one stable object identity; spatial hierarchy becomes a role/profile and/or typed relation projection.

### 4. Missing first-class source representation

The doctrine describes Revit/IFC/PDF/photo occurrences, but current schemas do not have one carrier rich enough for source version, native id, locator, coordinate frame, binding, freshness, observation time and limitations. Proposed new concept: `source_representation`, with matching separated into a governed `representation_match` statement.

### 5. Relations lack proof depth

`object_relation` carries source refs but not the same proof/derivation/certainty/validity posture as `attribute_claim`. Proposed target: `relation_claim` or an equivalent extension in place.

### 6. `object_kind` is now too narrow

The current enum was adequate for the first spatial proof but is too narrow for the confirmed first wave (architecture, economy, site/DET, RE2020, ACV). Proposed model: broad stable object families plus source/tool classifications; do not mirror Revit categories into the core enum.

### 7. `stable_object.matches` should not become the long-term source log

H2's embedded match is correct for the bounded first write but would become an overloaded heterogeneous source history if used for Revit/IFC/PDF observations. Preserve H2 event provenance while later projecting matches into first-class representation/match storage.

### 8. Documentation is stale relative to H2

The convergence note still lists authorized APU write application as unestablished, while `pantheon-mvp` now implements it. Future documentation alignment should classify the family as partial rather than either wholly implemented or wholly documentation-only.

### 9. Fixture/schema drift exists

The architecture vertical example uses `object_kind: door`, while the current shared `object_kind` enum does not admit `door`. This supports replacing a narrow discipline enum with broad families plus classifications rather than continually widening it.

## Preserved invariants

The review does not challenge:

```text
APU != Project Anatomy projection
Revit/IFC ids != stable identity
source agreement != truth
adapter success != Evidence
APU != ProjectClaim
APU != WorkIssue
APU != Decision
contradictions remain held
human consequential gate remains external to adapter/runtime
```

## Proposed V0.2 core

```text
stable_object
source_representation
representation_match
attribute_claim
relation_claim
object_group
existing program / requirement / classification contracts
governed cross-family references
```

`property_set`, `instance_override`, `spatial_node`, current `object_relation` and embedded `stable_object.matches` become compatibility/deprecation questions, not automatically retained authorities.

## Revit consequence

The future Revit 2027 plugin should return:

```text
Context Snapshot
source representation candidates
attribute observations
relation observations
warnings / limitations
```

It should not manufacture stable APU identity or directly mutate the Project Anatomy owner.

## Files changed in this intervention

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_V02_DESIGN_REVIEW.md
ai_logs/2026/Q3/2026-08-07-project-anatomy-v02-design-review.md
```

No protected path, schema, test, runtime, migration, Revit add-in, adapter implementation or MVP code was modified.

## Not decided by this intervention

- exact schema field names;
- final `object_family` enum;
- `object_identity` removal vs subordinate compatibility shape;
- `spatial_node` deprecation vs strict one-to-one profile;
- `relation_claim` new schema vs extending `object_relation`;
- physical SQL migration;
- H2 legacy match projection migration;
- RevitMCPSDK dependency decision;
- implementation sequencing or schedule.

These require a separate reviewed contract/migration tranche, with protected-schema changes only after explicit approval.
