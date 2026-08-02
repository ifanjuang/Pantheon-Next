# Cockpit JavaScript inventory

## Scope

This inventory describes the browser-side Cockpit code loaded from `mvp_vertical/cockpit`. It does not change Pantheon governance, authorization, Evidence, ChangeCandidate semantics, or server authority.

## Current active chain

`index.html` loads `cockpit_bootstrap.js`.

Live mode then loads `live_bootstrap.js`, which:

1. loads the tag icon registries through `rendering/tag_icons.js`;
2. loads and validates `projection/navigation_registry_loader.js` before navigation and projection startup;
3. imports `navigation/swiper_loader.js` to acquire Swiper without exposing its CDN logic to the boot orchestrator;
4. loads `live_collection_adapter.js` when Swiper is available;
5. loads `shell_controls.js`;
6. loads `structured_interface.js`;
7. loads `context_resolver.js`;
8. loads `agency_data_binding.js`;
9. loads `spatial_navigation.js`;
10. loads `projection/navigation_registry_adapter.js`;
11. loads `data/cockpit_data_loader.js`;
12. loads `projection/cockpit_projection.js`;
13. loads `interactions/interaction_policy.js`;
14. loads `project_claim_view_adapter.js`;
15. loads `information_view_adapter.js`;
16. loads `context/context_selection.js`;
17. loads `handoff/handoff_lifecycle.js`;
18. loads `handoff/handoff_send.js`;
19. loads `actions/card_actions.js`;
20. loads `actions/change_candidate_actions.js`;
21. loads `schema_editor.js`;
22. loads `contacts_editor.js`;
23. loads `information_create.js`;
24. loads `interactions/card_interactions.js`.

`live_collection_adapter.js` imports `rendering/card_renderer.js` directly. The live collection therefore receives canonical card structure before mount; the adapter no longer translates class vocabularies.

Demo mode loads `v3/demo_collection_app.js` and `shell_controls.js` from `cockpit_bootstrap.js`.

## Responsibility classification

### Entrypoints and boot

- `cockpit_bootstrap.js`: canonical browser entrypoint, mode selection and visible boot failure.
- `live_bootstrap.js`: mode state, ordered application startup and visible failure projection.
- `navigation/swiper_loader.js`: optional Swiper acquisition, version pinning and readiness metadata. It owns CDN fallback only; it does not construct a Swiper instance.
- `demo_bootstrap.js`: live renderer demo data bootstrap.

### Collection and navigation

- `live_collection_adapter.js`: collection integration boundary. It receives projected models, invokes the canonical card renderer and delegates lifecycle to the shared collection controller.
- `v3/collection/collection_controller.js`: collection lifecycle.
- `v3/collection/motion_adapter.js`: sole Swiper instance/API boundary.
- `v3/collection/navigation_state.js`: navigation state.
- `v3/providers/live_provider.js`: live collection snapshots.
- `spatial_navigation.js`: historical spatial navigation consumer; migration status must be verified before renaming or removal.
- `projection/navigation_registry_loader.js`: loads and strictly validates the versioned root-navigation registry before the classic projection chain starts. It exposes declarative identities and abstract sources only.
- `projection/navigation_registry_adapter.js`: applies the registered root collection and ordering at the spatial-navigation boundary. It does not select endpoints, authorize tasks or promote Evidence.

Swiper must remain isolated behind `v3/collection/motion_adapter.js` for instance construction and navigation APIs. `navigation/swiper_loader.js` may only acquire the optional library and expose readiness metadata.

### Rendering and projection

- `rendering/card_renderer.js`: canonical structural card renderer. It emits semantic card structure and stable projection axes; it emits no decorative nodes.
- `rendering/tag_icons.js`: presentation-only resolver for type and subject tag icons. It binds registered tags to vendored Radix assets or Google Material Symbols and gives unregistered tags a visible, accessible fallback.
- `projection/cockpit_projection.js`: active model projection and fallback renderer. Its live DOM output is no longer mounted by the collection path; its remaining fallback, child-assembly and state responsibilities must be separated before retirement.
- `structured_interface.js`: structured interface projection.
- `project_claim_view_adapter.js`: ProjectClaim projection adapter.
- `information_view_adapter.js`: Information projection adapter.

### Interaction and consequential actions

- `interactions/card_interactions.js`: canonical card activation, pointer/keyboard flip behavior and optional material assignment.
- `interactions/interaction_policy.js`: interaction policy and spatial-navigation locking while a verso is open.
- `actions/card_actions.js`: Information and Work decision actions. Server authority remains mandatory.
- `actions/change_candidate_actions.js`: human apply/reject actions for ChangeCandidates.
- `handoff/handoff_lifecycle.js`: handoff preview, submission, bounded admission and revocation lifecycle. It never dispatches Hermes.
- `handoff/handoff_send.js`: convenience adapter that prepares then submits a handoff; it does not admit or dispatch execution.

### Context, bindings and data

- `context_resolver.js`: context resolution.
- `agency_data_binding.js`: agency data binding.
- `data/cockpit_data_loader.js`: bounded browser transport for Cockpit registries, tool catalogue and read-only Agency Data projections. It does not render cards, navigate or infer authorization.
- `context/context_selection.js`: read-only context search and explicit user selection. Selection remains distinct from Evidence.

### Editors

- `schema_editor.js`: schema-driven editor.
- `contacts_editor.js`: Contacts editor.
- `information_create.js`: Information creation workflow.

### Shell

- `shell_controls.js`: shell menu and Hermes dock interactions.

## Confirmed architectural debt

1. `projection/cockpit_projection.js` still combines model projection, fallback DOM rendering, child collection assembly and navigation state; network transport is isolated in `data/cockpit_data_loader.js`, while root identities, order and abstract source declarations are isolated in the navigation registry.
2. Compatibility `v2-*` classes remain temporarily emitted beside canonical classes because the fallback path still consumes them.
3. `live_bootstrap.js` still combines mode state, ordered script loading and failure projection, but no longer owns external Swiper acquisition.
4. Classic scripts communicate through globals, so imports alone are insufficient to prove that a file is dead.
5. Swiper instance construction and navigation APIs must remain isolated behind `v3/collection/motion_adapter.js`; `navigation/swiper_loader.js` may only acquire the library.

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

### Registry source bindings and child assembly

Use the abstract sources declared by `registries/navigation_registry.json` to replace hard-coded source selection. Move child collection assembly out of `projection/cockpit_projection.js` into a bounded projection/assembly module. Keep endpoint transport in `data/cockpit_data_loader.js`, server authority unchanged and the registry free of executable routing, authorization or Evidence semantics.

### Remove compatibility classes

Retire the fallback DOM renderer or make it canonical, then remove dual classes from `rendering/card_renderer.js` and the bounded `:is(.card, .v2-card)` seams.

### Functional identifiers

Rename `v2-*` DOM identifiers only after all JavaScript, CSS, tests and published routes consuming them are migrated in the same change.

### Domain consolidation

Separate model projection, navigation and fallback rendering from `projection/cockpit_projection.js`. Data loading now has a bounded owner in `data/cockpit_data_loader.js`; root navigation declarations have a bounded owner in `registries/navigation_registry.json`. Consolidate only modules with proven overlapping responsibility. Do not target a file count.

## Invariants

```text
visual projection != semantic model
UI status != authorization
runtime_success != Evidence
retrieved != truth
binding_selected != dependency_adopted
Pantheon != runtime
```
