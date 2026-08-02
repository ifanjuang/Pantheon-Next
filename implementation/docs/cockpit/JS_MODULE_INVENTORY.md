# Cockpit JavaScript inventory

## Scope

This inventory describes the browser-side Cockpit code loaded from `mvp_vertical/cockpit`. It does not change Pantheon governance, authorization, Evidence, ChangeCandidate semantics, or server authority.

## Current active chain

`index.html` loads `cockpit_bootstrap.js`.

Live mode then loads `live_bootstrap.js`, which:

1. loads the tag icon registries through `rendering/tag_icons.js`;
2. loads and validates `projection/navigation_registry_loader.js`;
3. imports `navigation/swiper_loader.js`;
4. loads `live_collection_adapter.js` when Swiper is available;
5. loads `shell_controls.js`;
6. loads `structured_interface.js`;
7. loads `context_resolver.js`;
8. loads `agency_data_binding.js`;
9. loads `spatial_navigation.js`;
10. loads `projection/navigation_registry_adapter.js`;
11. loads `projection/child_collection_assembler.js`;
12. loads `data/cockpit_data_loader.js`;
13. loads `projection/cockpit_projection.js`;
14. loads `interactions/interaction_policy.js`;
15. loads `project_claim_view_adapter.js`;
16. loads `information_view_adapter.js`;
17. loads `context/context_selection.js`;
18. loads `handoff/handoff_lifecycle.js`;
19. loads `handoff/handoff_send.js`;
20. loads `actions/card_actions.js`;
21. loads `actions/change_candidate_actions.js`;
22. loads `schema_editor.js`;
23. loads `contacts_editor.js`;
24. loads `information_create.js`;
25. loads `interactions/card_interactions.js`.

`live_collection_adapter.js` imports `rendering/card_renderer.js` directly. The live collection receives canonical card structure before mount.

Demo mode loads `demo/collection_app.js` and `shell_controls.js` from `cockpit_bootstrap.js`.

## Responsibility classification

### Entrypoints and boot

- `cockpit_bootstrap.js`: canonical browser entrypoint, mode selection and visible boot failure.
- `live_bootstrap.js`: mode state, ordered application startup and visible failure projection.
- `navigation/swiper_loader.js`: optional Swiper acquisition, version pinning and readiness metadata.
- `demo_bootstrap.js`: live renderer demo data bootstrap.

### Collection and navigation

- `live_collection_adapter.js`: collection integration boundary and canonical renderer consumer.
- `collection/collection_controller.js`: collection lifecycle.
- `collection/motion_adapter.js`: sole Swiper instance/API boundary.
- `collection/navigation_state.js`: navigation state.
- `providers/live_provider.js`: live collection snapshots.
- `spatial_navigation.js`: spatial sibling, descend, ascend and root navigation state.
- `projection/navigation_registry_loader.js`: strict loader for the versioned root-navigation registry.
- `projection/navigation_registry_adapter.js`: applies registered root identity and order at the navigation boundary.
- `projection/child_collection_assembler.js`: resolves abstract registry sources and assembles root and selected-project child collections. It owns no transport, authorization or Evidence semantics.

Registry source names are projection inputs only: they are neither endpoint declarations nor authority grants.

Swiper must remain isolated behind `collection/motion_adapter.js` for instance construction and navigation APIs.

### Rendering and projection

- `rendering/card_renderer.js`: canonical structural card renderer.
- `rendering/tag_icons.js`: presentation-only type and subject icon resolver.
- `projection/cockpit_projection.js`: card-model normalization, Cockpit state, navigation orchestration and bounded non-Swiper fallback. It delegates all parent-child assembly to `child_collection_assembler.js`.
- `structured_interface.js`: structured interface projection.
- `project_claim_view_adapter.js`: ProjectClaim projection adapter.
- `information_view_adapter.js`: Information projection adapter.

### Interaction and consequential actions

- `interactions/card_interactions.js`: canonical card activation and flip behavior.
- `interactions/interaction_policy.js`: interaction policy and navigation locking while a verso is open.
- `actions/card_actions.js`: Information and Work decision actions; server authority remains mandatory.
- `actions/change_candidate_actions.js`: human apply/reject actions for ChangeCandidates.
- `handoff/handoff_lifecycle.js`: handoff preview, submission, bounded admission and revocation lifecycle.
- `handoff/handoff_send.js`: convenience adapter that prepares then submits a handoff; it does not admit or dispatch execution.

### Context, bindings and data

- `context_resolver.js`: context resolution.
- `agency_data_binding.js`: agency data binding.
- `data/cockpit_data_loader.js`: bounded browser transport for registries, tool catalogue and read-only Agency Data projections.
- `context/context_selection.js`: read-only context search and explicit user selection.

### Editors

- `schema_editor.js`: schema-driven editor.
- `contacts_editor.js`: Contacts editor.
- `information_create.js`: Information creation workflow.

### Shell

- `shell_controls.js`: shell menu and Hermes dock interactions.

## Confirmed architectural debt

1. `projection/cockpit_projection.js` still combines model normalization, navigation orchestration and a bounded fallback renderer; child assembly and network transport now have separate owners.
2. Compatibility `v2-*` classes and identifiers remain because active HTML, CSS, interaction adapters and published regression surfaces still consume them.
3. `live_bootstrap.js` still combines mode state, ordered script loading and failure projection.
4. Classic scripts communicate through globals, so imports alone are insufficient to prove a file dead.
5. Swiper instance construction and navigation APIs remain isolated behind `collection/motion_adapter.js`.

## Dead-code proof

Before deleting a JavaScript file or compatibility token, establish all of the following reference classes:

- HTML script inclusion;
- static import;
- dynamic import;
- ordered classic-script inclusion;
- global produced and global consumed;
- CSS selector consumption;
- test or published regression surface dependency.

Removal is allowed only when every dependency category is empty.

## Next stages

### Compatibility retirement

Identify `v2-*` classes and identifiers whose dependency graph is empty, remove them in bounded changes and retain those still consumed by active HTML, CSS, interaction adapters or published routes.

### Graphical evolution

Only after the functional compatibility cleanup is stable, apply the ConnorGriffin-inspired method to a new graphical evolution. The graphical layer must consume the existing schema-driven projection contracts and must not introduce backend authority or runtime behavior.

## Invariants

```text
visual projection != semantic model
UI status != authorization
runtime_success != Evidence
retrieved != truth
binding_selected != dependency_adopted
Pantheon != runtime
```
