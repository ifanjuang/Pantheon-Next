# Cockpit JavaScript inventory

## Scope

This inventory describes the browser-side Cockpit code loaded from `mvp_vertical/cockpit`. It does not change Pantheon governance, authorization, Evidence, ChangeCandidate semantics, or server authority.

## Current active chain

`index.html` loads `cockpit_bootstrap.js`.

Live mode then loads `live_bootstrap.js`, which loads the following modules in order:

1. `live_collection_adapter.js` when Swiper is available;
2. `shell_controls.js`;
3. `structured_interface.js`;
4. `context_resolver.js`;
5. `agency_data_binding.js`;
6. `spatial_navigation.js`;
7. `v2_app_schema.js`;
8. `interactions/interaction_policy.js`;
9. `project_claim_view_adapter.js`;
10. `information_view_adapter.js`;
11. `v2_context.js`;
12. `v2_handoff.js`;
13. `v2_hermes_send.js`;
14. `actions/card_actions.js`;
15. `actions/change_candidate_actions.js`;
16. `schema_editor.js`;
17. `contacts_editor.js`;
18. `information_create.js`;
19. `interactions/card_interactions.js`.

`live_collection_adapter.js` imports `rendering/card_renderer.js` directly. The live collection therefore receives canonical card structure before mount; the adapter no longer translates class vocabularies.

Demo mode loads `v3/demo_collection_app.js` and `shell_controls.js` from `cockpit_bootstrap.js`.

## Responsibility classification

### Entrypoints and boot

- `cockpit_bootstrap.js`: canonical browser entrypoint, mode selection and visible boot failure.
- `live_bootstrap.js`: live dependency loading and ordered classic-script startup.
- `demo_bootstrap.js`: live renderer demo data bootstrap.

### Collection and navigation

- `live_collection_adapter.js`: collection integration boundary. It receives projected models, invokes the canonical card renderer and delegates lifecycle to the shared collection controller.
- `v3/collection/collection_controller.js`: collection lifecycle.
- `v3/collection/motion_adapter.js`: sole Swiper API boundary.
- `v3/collection/navigation_state.js`: navigation state.
- `v3/providers/live_provider.js`: live collection snapshots.
- `spatial_navigation.js`: historical spatial navigation consumer; migration status must be verified before renaming or removal.

### Rendering and projection

- `rendering/card_renderer.js`: canonical structural card renderer. It emits semantic card structure and stable projection axes; it emits no decorative nodes.
- `v2_app_schema.js`: active model projection and fallback renderer. Its live DOM output is no longer mounted by the collection path; its remaining fallback and state responsibilities must be separated before retirement.
- `structured_interface.js`: structured interface projection.
- `project_claim_view_adapter.js`: ProjectClaim projection adapter.
- `information_view_adapter.js`: Information projection adapter.

### Interaction and consequential actions

- `interactions/card_interactions.js`: canonical card activation, pointer/keyboard flip behavior and optional material assignment.
- `interactions/interaction_policy.js`: interaction policy and spatial-navigation locking while a verso is open.
- `actions/card_actions.js`: Information and Work decision actions. Server authority remains mandatory.
- `actions/change_candidate_actions.js`: human apply/reject actions for ChangeCandidates.
- `v2_handoff.js`: handoff behavior.
- `v2_hermes_send.js`: Hermes send surface; it remains an adapter and does not make Pantheon a runtime.

### Context, bindings and data

- `context_resolver.js`: context resolution.
- `agency_data_binding.js`: agency data binding.
- `v2_context.js`: historical context bridge; consumers must be enumerated before replacement.

### Editors

- `schema_editor.js`: schema-driven editor.
- `contacts_editor.js`: Contacts editor.
- `information_create.js`: Information creation workflow.

### Shell

- `shell_controls.js`: shell menu and Hermes dock interactions.

## Confirmed architectural debt

1. `v2_app_schema.js` still combines model projection, fallback DOM rendering, navigation state and network loading.
2. Compatibility `v2-*` classes remain temporarily emitted beside canonical classes because the fallback path still consumes them.
3. `live_bootstrap.js` still mixes dependency acquisition, mode state, ordered script loading and failure projection.
4. Classic scripts communicate through globals, so imports alone are insufficient to prove that a file is dead.
5. Swiper must remain isolated behind `v3/collection/motion_adapter.js`; no cleanup may move its API into controllers or renderers.

## Dead-code proof

For every JavaScript file, establish all of the following before deletion:

- HTML script inclusion;
- static import;
- dynamic import;
- ordered classic-script inclusion;
- global produced and global consumed;
- test or published regression surface dependency.

A file is removable only when every category is empty.

## Next stages

### Remove compatibility classes

Retire the fallback DOM renderer or make it canonical, then remove dual classes from `rendering/card_renderer.js` and the bounded `:is(.card, .v2-card)` seams.

### Functional identifiers

Rename `v2-*` DOM identifiers only after all JavaScript, CSS, tests and published routes consuming them are migrated in the same change.

### Domain consolidation

Separate model projection, data loading, navigation and fallback rendering from `v2_app_schema.js`. Consolidate only modules with proven overlapping responsibility. Do not target a file count.

## Invariants

```text
visual projection != semantic model
UI status != authorization
runtime_success != Evidence
retrieved != truth
Pantheon != runtime
```
