# Tool Card implementation

Status: executable candidate — catalogue, GET-only Hermes observation adapter, V2 spatial catalogue projection and I7 exact-governance projection implemented; live Hermes observation and canonical I2–I6 records are not connected to the Cockpit.

Pantheon Next owns Capability governance and the canonical I2–I6 contracts. This repository owns concrete catalogue records, normalized runtime/Hermes observations and the executable Cockpit projection. Hermes owns native discovery and execution. The Cockpit never becomes the owner of binding, activation, compatibility, safety or authorization state.

## Implemented here

- `mvp_vertical/cockpit/tool_catalog.json`: concrete supplementary catalogue, not authority.
- `mvp_vertical/hermes_tool_inventory.py`: GET-only normalization of reviewed Hermes discovery surfaces.
- `mvp_vertical/cockpit/data/cockpit_data_loader.js`: `loadToolCatalog()` reads the catalogue as an optional collection, so an unreachable catalogue degrades visibly instead of inventing state.
- `mvp_vertical/cockpit/projection/cockpit_projection.js`: existing Tool Card construction and catalogue-unavailable behavior.
- `mvp_vertical/cockpit/projection/tool_governance_projection.js`: bounded I7 decorator that projects exact binding/release, scoped activation and compatibility qualification fields when supplied; absent values render `not_observed` rather than being inferred.
- `mvp_vertical/cockpit/projection/child_collection_assembler.js`: resolves the Tool Card collection for spatial navigation.
- independent axes remain visible for catalogue, installation, native state, health, governance, update, activation, compatibility, safety and freshness.
- consequence-bearing permissions remain known/unknown/potential; unknown is never inferred safe.
- Haystack remains a candidate only; LlamaIndex/LangChain/LangGraph remain watch/comparison entries. No dependency is selected, installed, approved or activated by this catalogue.

## I7 exact-governance projection

The projection accepts these optional fields on a Tool catalogue/projection record:

```text
binding_id
implementation_anchor.kind
implementation_anchor.value
activation_state
activation_scope.scope_type
activation_scope.scope_id
activation_scope.scope_label
compatibility_status
safety_status
freshness_status
source_observation_ref
compatibility_observed_at
```

They mirror, without owning, the Pantheon-Next I2–I6 dimensions:

```text
Capability Slot
  -> exact Capability Binding
  -> immutable implementation/release anchor
  -> scoped governance activation
  -> exact-release compatibility observation
```

The current catalogue intentionally does not invent canonical binding IDs, release digests, activation decisions or compatibility observations for its existing framework entries. Until an authoritative server-side projection supplies those values, the I7 fields display `not_observed`.

## V2 spatial projection

The active Cockpit remains the schema-driven CardShell V2. No alternate Tool renderer is introduced. `tool_governance_projection.js` decorates the same Tool Card models immediately after graph construction and before normal rendering.

```text
Outils
  ↓
tool_catalog.json / future server projection
  ↓
Tool Card siblings
  ├─ identity / description
  ├─ Capability Slots
  ├─ exact binding identity
  ├─ immutable release anchor
  ├─ installation observation
  ├─ native state
  ├─ health observation
  ├─ governance state
  ├─ scoped activation
  ├─ compatibility observation
  ├─ safety qualification
  ├─ freshness
  ├─ update state
  ├─ permissions
  ├─ Evidence expectation
  ├─ rollback posture
  └─ next human decision
```

If the catalogue cannot be loaded, the Cockpit displays an explicit catalogue-unavailable card. It does not infer that any runtime/tool is absent or uninstalled.

## Runtime observation

Reviewed Hermes surfaces:

```text
GET /v1/skills
GET /v1/toolsets
GET /v1/capabilities
```

Normalized observations preserve runtime provenance and state but do not become I2–I6 governance records by themselves. The adapter performs no POST, install, enable, update, approval, run launch or activation.

The live observer is deliberately not called from the browser. Its future Cockpit connection must remain server-side so credentials are never exposed to the UI. A future server projection may join canonical I2–I6 records to Tool Cards; the browser must not reconstruct that authority from runtime observations.

## Non-equivalences

```text
catalogued       != discovered
discovered       != installed
installed        != approved
binding_selected != dependency_adopted
native_enabled   != scope_activated
scope_activated  != task_authorized
healthy          != compatible
compatible       != safe
compatible       != activated
update_available != update_authorized
runtime_success  != Evidence
projected        != persisted
UI status        != authorization
watchlist_item   != install_instruction
```
