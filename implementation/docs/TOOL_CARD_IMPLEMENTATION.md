# Tool Card implementation

Status: executable candidate — catalogue, GET-only Hermes observation adapter and V2 spatial catalogue projection implemented; live Hermes observation not connected to the Cockpit.

Pantheon Next owns the governance contract (`TOOL_CARD_MODEL.md`). This repository owns concrete catalogue records, normalized runtime/Hermes observations and the executable Cockpit projection. Hermes owns native discovery and execution.

## Implemented here

- `mvp_vertical/cockpit/tool_catalog.json`: concrete supplementary catalogue, not authority.
- `mvp_vertical/hermes_tool_inventory.py`: GET-only normalization of reviewed Hermes discovery surfaces.
- `mvp_vertical/cockpit/v2_app_schema.js`: each catalogue record is one real Tool Card sibling in the existing `Outils` spatial collection.
- independent axes for catalogue, installation, native state, health, governance, update and activation.
- consequence-bearing permissions remain known/unknown/potential; unknown is never inferred safe.
- Haystack is a candidate only; LlamaIndex/LangChain/LangGraph are watch/comparison entries. No dependency is selected, installed, approved or activated by this catalogue.

## V2 spatial projection

The active Cockpit remains the schema-driven CardShell V2. The obsolete #86 `index.html/tools.js` scene was intentionally not replayed.

```text
Outils
  ↓
tool_catalog.json
  ↓
Tool Card siblings
  ├─ identity / description
  ├─ Capability Slots
  ├─ provenance
  ├─ installation observation
  ├─ native state
  ├─ health observation
  ├─ governance state
  ├─ activation state
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

Normalized observations preserve:

```text
provenance_mode
native_identifier
version
installation_state
native_state
health_state
governance_state
update_state
activation_state
observed_at
capabilities
permissions
```

The adapter performs no POST, install, enable, update, approval, run launch or activation.

The live observer is deliberately not called from the browser. Its future Cockpit connection must remain server-side so `HERMES_API_SERVER_KEY` is never exposed to the UI. Until connected, catalogue Tool Cards retain their declared unknown/listed states rather than inventing a live runtime state.

## Non-equivalences

```text
catalogued       != discovered
discovered       != installed
installed        != approved
native_enabled   != scope_activated
healthy          != safe
update_available != update_authorized
runtime_success  != Evidence
binding_selected != dependency_adopted
watchlist_item   != install_instruction
```
