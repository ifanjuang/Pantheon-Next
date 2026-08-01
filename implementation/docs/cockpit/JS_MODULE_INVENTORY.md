# Cockpit JavaScript inventory

## Scope

This inventory describes the browser-side Cockpit code loaded from `mvp_vertical/cockpit`. It does not change Pantheon governance, authorization, Evidence, ChangeCandidate semantics, or server authority.

## Current active chain

`index.html` loads `v3_bootstrap.js`.

Live mode then loads `v2_bootstrap.js`, which loads the following modules in order:

1. `v3_swiper.js` when Swiper is available;
2. `v2_shell_controls.js`;
3. `structured_interface.js`;
4. `context_resolver.js`;
5. `agency_data_binding.js`;
6. `spatial_navigation.js`;
7. `v2_app_schema.js`;
8. `v2_interaction_policy.js`;
9. `project_claim_view_adapter.js`;
10. `information_view_adapter.js`;
11. `v2_context.js`;
12. `v2_handoff.js`;
13. `v2_hermes_send.js`;
14. `v2_actions.js`;
15. `v2_candidate_actions.js`;
16. `schema_editor.js`;
17. `contacts_editor.js`;
18. `information_create.js`;
19. `v3/cockpit_v3.js`.

Demo mode loads `v3/demo_collection_app.js` and `v2_shell_controls.js` from `v3_bootstrap.js`.

## Responsibility classification

### Entrypoints and boot

- `v3_bootstrap.js`: canonical browser entrypoint, mode selection and visible boot failure.
- `v2_bootstrap.js`: live dependency loading and ordered legacy-script startup.
- `demo_bootstrap.js`: live renderer demo data bootstrap.

### Collection and navigation

- `v3_swiper.js`: compatibility boundary between the legacy renderer and the shared collection controller. It still owns `CLASS_MAP` and must not become permanent.
- `v3/collection/collection_controller.js`: collection lifecycle.
- `v3/collection/motion_adapter.js`: sole Swiper API boundary.
- `v3/collection/navigation_state.js`: navigation state.
- `v3/providers/live_provider.js`: live collection snapshots.
- `spatial_navigation.js`: historical spatial navigation consumer; migration status must be verified before renaming or removal.
- `v3/cockpit_v3.js`: active V3 integration module; exact ownership must be reduced to one responsibility before renaming.

### Rendering and projection

- `v2_app_schema.js`: active live renderer and main source of legacy `v2-*` card classes.
- `structured_interface.js`: structured interface projection.
- `project_claim_view_adapter.js`: ProjectClaim projection adapter.
- `information_view_adapter.js`: Information projection adapter.

### Context, bindings and data

- `context_resolver.js`: context resolution.
- `agency_data_binding.js`: agency data binding.
- `v2_context.js`: historical context bridge; consumers must be enumerated before replacement.

### Interaction and consequential actions

- `v2_interaction_policy.js`: interaction policy.
- `v2_actions.js`: general card actions.
- `v2_candidate_actions.js`: ChangeCandidate actions.
- `v2_handoff.js`: handoff behavior.
- `v2_hermes_send.js`: Hermes send surface; it remains an adapter and does not make Pantheon a runtime.

### Editors

- `schema_editor.js`: schema-driven editor.
- `contacts_editor.js`: Contacts editor.
- `information_create.js`: Information creation workflow.

### Shell

- `v2_shell_controls.js`: shell menu and Hermes dock interactions.

## Confirmed architectural debt

1. Generation-prefixed entrypoints (`v2_*`, `v3_*`) expose implementation history instead of responsibility.
2. `v3_swiper.js` normalizes the renderer through `CLASS_MAP`; the renderer and design system therefore have two DOM vocabularies.
3. `v2_bootstrap.js` mixes dependency acquisition, mode state, ordered script loading and failure projection.
4. Classic scripts communicate through globals, so imports alone are insufficient to prove that a file is dead.
5. Swiper must remain isolated behind `v3/collection/motion_adapter.js`; no cleanup may move its API into controllers or renderers.

## Migration sequence

### Stage 1 — inventory and dead-code proof

For every JavaScript file, establish all of the following before deletion:

- HTML script inclusion;
- static import;
- dynamic import;
- ordered classic-script inclusion;
- global produced and global consumed;
- test or published regression surface dependency.

A file is removable only when every category is empty.

### Stage 2 — neutral entrypoints

Rename by responsibility without changing functional DOM contracts:

- `v3_bootstrap.js` → `cockpit_bootstrap.js`;
- `v2_bootstrap.js` → `live_bootstrap.js`;
- `v3_swiper.js` → `live_collection_adapter.js`;
- `v2_shell_controls.js` → `shell_controls.js`.

### Stage 3 — canonical renderer

Make the live renderer emit canonical structural classes directly. The renderer may emit semantic structure and stable projection axes, but no decorative nodes or graphical instructions.

### Stage 4 — remove compatibility

Delete `CLASS_MAP`, legacy class normalization and the adapter code whose only purpose was vocabulary conversion.

### Stage 5 — functional identifiers

Rename `v2-*` DOM identifiers only after all JavaScript, CSS, tests and published routes consuming them are migrated in the same change.

### Stage 6 — domain consolidation

Consolidate only modules with proven overlapping responsibility. Do not target a file count. Keep distinct editors, bindings and consequential-action modules when they carry distinct contracts.

## Invariants

```text
visual projection != semantic model
UI status != authorization
runtime_success != Evidence
retrieved != truth
Pantheon != runtime
```
