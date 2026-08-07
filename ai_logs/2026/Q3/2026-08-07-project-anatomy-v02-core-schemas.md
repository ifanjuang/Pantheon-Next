# AI intervention — Project Anatomy V0.2 core schemas

Date: 2026-08-07
Repository: `ifanjuang/Pantheon-Next`
Branch: `refactor/project-anatomy-v02-core-schemas`
Stack base: `docs/project-anatomy-v02-design-review` / PR #580 target model.

## Request

After the Project Anatomy V0.2 design review, the user explicitly authorized remodeling the protected schema structure now, before Revit 2027, IFC/IDS, OpenTakeoff, economy, DET, RE2020 and ACV make later structural changes more expensive.

## Scope

This tranche changes the canonical protected **contract primitives only**. It deliberately does not yet migrate the legacy MCP validator, worked dossier, downstream `pantheon-mvp` persistence or production adapters.

## V0.2 primitives implemented in schema

```text
stable_object
source_representation
attribute_claim
relation_claim
```

Supporting contracts updated:

```text
shared.schema.yaml
derivation.schema.yaml
requirement.schema.yaml
```

## Main structural decisions encoded

### `stable_object`

Now owns durable project identity and nomenclature only.

Removed from the canonical shape:

```text
kind
proof_status
matches
source-native ids
spatial span data
supersession fields
notes
```

These responsibilities move to claims, source representations, relation claims or persistence/governance layers.

### `source_representation`

New first-class source-bound occurrence supporting:

```text
source artifact/version
source kind
namespaced native identifiers
locators
observation timestamp
binding + adapter version
freshness token
content digest
coordinate frame/calibration
bounded source context
limitations
proof status
```

It does not require a stable-object match.

### `attribute_claim`

Now carries the sole canonical project value assertion and may target a `stable_object` or `source_representation` through a typed entity ref.

Approval/use grants were removed from the claim shape. Human correction is represented by superseding claims rather than source mutation.

### `relation_claim`

New canonical relationship assertion with the same provenance/proof posture as attributes.

`identity.represents` is constrained to:

```text
source_representation -> stable_object
```

so a separate `representation_match` carrier is not needed.

### `derivation`

Generalized to produce attribute or relation claim refs and record method/version, inputs, binding/adapter provenance and deterministic posture without executing anything.

### `requirement`

Generalized beyond `from_program` to typed sources including programme, document, IDS, decision, contract, regulation, technical brief and agency standard.

Requirements remain prescriptive and separate from observed claims.

## Shared V0.2 vocabulary added

```text
object_family
apu_entity_ref
apu_claim_ref
assertion_mode
claim_value
source_kind
source_identifier
relation_type
```

Legacy V0.1 `$defs` remain temporarily in `shared.schema.yaml` because old compatibility schemas still reference them. Their presence does not make them V0.2 canonical.

## Examples

Canonical examples now demonstrate:

```text
stable project object
Revit source representation
attribute observed on the representation
human-reviewed identity.represents relation
derivation provenance
generic programme requirement
```

## Tests

Added `tests/test_apu_v02_core_schemas.py` to lock the new contract independently of legacy dossier validation.

It verifies in particular:

```text
stable_object rejects legacy fact/source fields
source_representation can exist unmatched
attribute_claim rejects embedded approval/use grants
identity.represents enforces typed endpoints
requirement accepts IDS as a source class
derivation may produce relation claims
```

## Deliberately deferred to stacked compatibility tranche

```text
mcp-server/pantheon_mcp/apu.py
docs/examples/architecture_project_understanding_dossier/
.github/scripts/check_apu_referential_integrity.py
legacy carrier deprecation/removal
schemas/README.md full family description
existing generic schema-test registry
```

This keeps the protected contract PR reviewable and prevents mixing the target schema with migration adapters.

## Downstream work intentionally not performed here

```text
pantheon-mvp SQL/persistence owner
H2 source_match event projection
Revit adapter DTOs
IFC/IDS adapters
OpenTakeoff adapter
Cockpit projections
```

## Preserved boundaries

```text
schema != runtime
source observation != truth
runtime success != Evidence
claim != approval
Revit/IFC id != stable project identity
Pantheon governs
Hermes orchestrates
Revit executes locally
```
