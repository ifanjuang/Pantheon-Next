# 2026-08-08 — Project Anatomy H4 Cockpit projection

## Objective

Close the H4 read-surface gap after the Project Anatomy V0.2 executable owner landed in #267.

The slice must expose the existing server-owned V0.2 Anatomy in Cockpit without creating a second owner, persistence model, authorization path or semantic relation vocabulary.

## Repository state verified before change

- `pantheon-mvp` `main` was `e04374579ac5eb9d6bcce5eea86726db90e9f7e3` (merge of #267 H4c).
- H1 (#260), H2 (#265), H3 (#266) and H4c (#267) were merged.
- no open H4 Cockpit PR or branch existed.
- parallel document-revision work did not touch the H4 implementation files.
- Pantheon-Next had already merged the V0.2 core, compatibility layer, adapter chokepoint, Revit observation contract and Drawing Takeoff specialization.

## Observed gap

`cockpit_composed.py` initialized the H1 migration (`021`) but did not replay the already-merged V0.2 owner migration (`024`) on a fresh composed startup.

The executable V0.2 owner already exposed stable objects, source representations, attribute claims and relation claims, but Cockpit had no Project Anatomy read route or visible Project child.

The current executable owner does not persist Observation Bundle coverage and has no admitted hierarchy-relation registry. H4 therefore must not infer absence or manufacture a parent/child hierarchy from generic relation strings.

## Implemented

- added a server-calculated `project_anatomy_projection` read model over the existing V0.2 owner;
- exposed `GET /agency/projects/{project_id}/project-anatomy` behind the existing Cockpit read key;
- mounted the route in the composed Cockpit and applied `V02_MIGRATION` after the H1 owner migration;
- exposed both the exact V0.2 contract authority ref and the separate conceptual doctrine ref;
- projected stable objects, source representations, relation/attribute claims, phase references and explicit uncertainty;
- exposed source representations with no active `identity.represents` relation as unmapped material;
- made `coverage.status = not_persisted` and `absence_inference_allowed = false` explicit;
- made hierarchy `not_derived` until an admitted relation-semantic registry exists;
- added a presentation-only browser module that creates a secondary `Anatomie du projet` card, stable-object cards and unmapped-source cards under the selected Project;
- kept every Anatomy browser card read-only with no actions;
- treated only `404` (no owner) and `409` (owner not migrated to V0.2) as optional Anatomy unavailability; other transport/server failures remain visible;
- updated the Cockpit JavaScript inventory.

## Authority boundaries retained

```text
Project Anatomy projection != Project Anatomy owner
UI card != Information entity
UI status != authorization
unmapped source != absent object
missing coverage != absence proof
relation visible != hierarchy inferred
certainty visible != professional approval
source representation != stable identity
runtime success != Evidence
```

No schema, canonical predicate, Evidence, Decision, WorkIssue, ProjectClaim or runtime authority was added or changed by this slice.

## Tests added

- server projection behavior and refusal to infer absence/hierarchy;
- rejected identity relation remains unmapped;
- protected read route and V0.2 conflict semantics;
- composed migration order and read-only API contract;
- Cockpit loader/assembly wiring;
- JavaScript syntax checks for the changed/new frontend modules.

## Remaining after this slice

H4 should be considered complete only after exact-head CI and review checks pass and the PR is merged.

H5 remains separate: validate identity continuity, provenance, contradiction/correction behavior and index changes progressively on representative structured document, image/photo, IFC and Revit sources. Observation Bundle coverage persistence remains a separate contract/owner question and is not silently solved by H4.

## Review hardening after `main` advanced

The H4 head was brought onto `pantheon-mvp` `main` at `3b1f3b6ba5fccff4e4826161b07708e73d600208`, preserving the operational B4 collaboration migration and route assertions alongside the H1 → V0.2 order.

The unresolved review findings were reproduced before correction. The bounded read projection now:

- renders each structured attribute value and optional unit in Cockpit;
- preserves source-scoped attribute claims on their source representation and in the complete projected claim collection;
- preserves native source identifiers and renders them on unmapped-source cards;
- treats only `accepted_as_support` identity claims as mapped, while unresolved claims remain visible on the source and do not hide unmapped material;
- exposes complete projected attribute/relation claim collections without changing the canonical owner.

Behavior tests cover `candidate` and `requires_more_evidence` identity states, source-scoped claims, native identifiers and Cockpit rendering. The full suite available in this environment passed with 1,178 successes and 337 service/platform skips; PostgreSQL-backed cases remain delegated to exact-head CI.
