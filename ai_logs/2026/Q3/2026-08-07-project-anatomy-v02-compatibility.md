# Project Anatomy V0.2 compatibility layer

Date: 2026-08-07
Status: implementation candidate
Parent authority: `docs/domain-packs/architecture/PROJECT_ANATOMY_V02_DESIGN_REVIEW.md`

## Objective

Make the protected V0.2 core usable without structurally preserving V0.1 as a second canonical model.

## Verified red boundary

After the V0.2 core branch reached a clean schema/root-test posture, the only remaining Governance CI failures were the known V0.1 consumers:

- the worked Architecture Project Understanding dossier and its referential-integrity script;
- the bounded MCP APU validator and its V0.1 fixtures.

The core schemas were not widened to accept both V0.1 and V0.2 shapes.

## Compatibility posture

A static compatibility registry classifies each carrier as:

```text
canonical
support
compatibility_only
```

`compatibility_only` always implies:

```text
canonical_emission = false
```

The explicit MCP compatibility adapter may mechanically project old shapes where the mapping is non-ambiguous. It must not invent missing source observations, timestamps, Evidence, approval, certainty or professional validation.

In particular:

```text
legacy stable_object.matches
!= sufficient data to invent source_representation
!= sufficient data to invent identity.represents relation
```

Such matches remain readable historical input and produce an explicit warning unless a curated fixture or later migration has the additional source provenance needed to create V0.2 primitives truthfully.

## Worked dossier

The worked dossier now emits canonical V0.2 forms for:

- stable objects;
- requirements;
- attribute claims;
- derivations;
- one source representation;
- identity and project relation claims.

Selected V0.1 files remain in the dossier only as compatibility fixtures (for example `object_identity`, `object_relation`, `spatial_node`, `space_group`, `deviation`, `human_override` and the former APU Evidence shape). The referential-integrity check validates these separately and verifies their registry posture.

## Boundaries

```text
legacy readable != canonical V0.2
compatibility projection != persistence migration
compatibility validation != Evidence admission
old approval field readable != V0.2 use grant
old match readable != source identity accepted
schema valid != project truth
```

No runtime, adapter execution, persistence, provider routing, task authorization, Evidence admission, automatic canonization or approval is added by this compatibility layer.
