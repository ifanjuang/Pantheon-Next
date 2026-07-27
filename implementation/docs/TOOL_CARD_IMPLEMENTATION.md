# Tool Card implementation

Status: executable candidate primitives — catalogue + Hermes observation adapter implemented; V2 spatial projection integration pending.

Pantheon Next owns the governance contract (`TOOL_CARD_MODEL.md`). This repository owns concrete catalogue records, normalized runtime/Hermes observations and the future executable Cockpit projection. Hermes owns native discovery and execution.

## Implemented here

- `mvp_vertical/cockpit/tool_catalog.json`: concrete supplementary catalogue, not authority.
- `mvp_vertical/hermes_tool_inventory.py`: GET-only normalization of reviewed Hermes discovery surfaces.
- independent axes for catalogue, installation, native state, health, governance, update and activation.
- consequence-bearing permissions remain known/unknown/potential; unknown is never inferred safe.
- Haystack is a candidate only; LlamaIndex/LangChain/LangGraph are watch/comparison entries. No dependency is selected, installed, approved or activated by this catalogue.

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

## V2 projection rule

The active Cockpit is the schema-driven CardShell V2. The old #86 `index.html/tools.js` scene is intentionally not replayed. Tool Cards must be integrated into the existing V2 spatial graph rather than creating a second renderer/navigation stack.

Until that integration is made, these primitives are implemented but the concrete V2 Tool Card collection remains partial.
