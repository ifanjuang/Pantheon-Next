# 2026-08-09 — Agency document exchange convergence

## Objective

Converge the architecture-agency document collaboration doctrine after clarifying that direct Pantheon use is currently internal to IFJA and that external participants may work through heterogeneous mediated surfaces, including email, project vaults, share links, limited Cockpit projections or dedicated interfaces.

Issue: #604.

## Repository state verified before change

Pantheon-Next current main at the start of the slice:

```text
9f65f6648b7b6cc89443004f6e70a3810fb224be
```

Relevant existing owners / doctrine reviewed:

- `AGENCY_COLLABORATION_AND_VERSION_INTAKE_CONVERGENCE.md` already owned agency collaboration and revision intake;
- `DOCUMENT_LIFECYCLE_GOVERNANCE.md` already described Source Capture and conceptual intake decomposition;
- `INDEX_EFFECT_MATRIX.md` already owned `visa_status_record` semantics and separated visa comment from execution authority;
- `RAW_DERIVED_GOVERNED_RECORDS.md` already separated original material from derived content and preserved provenance;
- merged Pantheon-Next A governance remained at `fc5aef13ace19e6ce97b2492e79dce2074dd2ade`;
- `pantheon-mvp` current main was `12f8da0a7360ceae4ace25c9ceb1702b92eab8bb` after H4 #280;
- no open `pantheon-mvp` PR required coordination;
- Pantheon-Next PR #600 concerns Revit freshness and does not overlap this slice.

## Observed problem

The existing collaboration note was complete but too portal-centric and over-decomposed for the clarified operating model.

It still suggested an `external portal` as the natural external surface and described technical access around external principals even though the current IFJA posture is:

```text
Pantheon direct use = internal IFJA perimeter
external actors = mediated surfaces only
```

The older lifecycle note also lists an `Intake Item` and several related conceptual objects. Those concepts remain useful for reasoning but should not force a separate canonical owner when Source, provenance, task and event records already preserve the needed semantics.

## Convergence decision

Keep the smallest stable model:

```text
Document / logical artifact
-> Revision / exact Source
-> Relations
-> Exchange inbound | outbound
-> Review / Decision when needed
-> Publication only when exposure must persist
```

This is a reasoning model, not a mandatory one-table-per-line implementation.

### Exchange

Inbound and outbound exchange are boundary events / provenance concerns. They may share technical fields such as direction, channel, actor, timestamp and payload references, but this change does not create a canonical `Exchange` schema or owner.

### Publication

Persistent Publication remains distinct from an outbound event:

```text
Exchange = event
Publication = persistent externally consumable exposure
```

Two useful publication modes are retained without creating type-specific owners:

```text
snapshot
= immutable exact-version manifest
= DCE / consultation package

controlled collection
= evolving explicit inclusion
= client meeting reports / selected project documents
```

A share link is only a replaceable access mechanism over a publication or exact published item.

### Visa / review

Visa is attached to an exact submitted revision and reuses existing professional effect / decision semantics. A new submitted revision opens a new review cycle; it does not rewrite the historical review of the previous revision.

No `VisaWorkflow` owner is introduced.

### Annotated execution plan

An IFJA redline or correction drawn on a received external plan is a derived review representation of that exact external revision. It is not the next issuer revision.

If IFJA produces a genuine autonomous drawing/detail, that output is a distinct IFJA-authored logical document with its own revision lineage and an explicit relation to the external source/baseline.

## Changed artifact

Rewrote the existing convergence note in place rather than adding a parallel model:

```text
docs/domain-packs/architecture/AGENCY_COLLABORATION_AND_VERSION_INTAKE_CONVERGENCE.md
```

The rewrite preserves the previously useful responsibilities:

- stable logical artifact identity;
- exact revisions and issuer vocabulary;
- Source provenance;
- deterministic contextual intake before inference;
- duplicate receipt handling;
- purpose-specific currentness;
- comparison and downstream review candidates;
- variants and offers;
- Knowledge source updates;
- external surfaces and technical-access separation;
- graceful degradation.

It adds / clarifies:

- direct Pantheon use is internal IFJA in the current deployment posture;
- external collaboration is mediated and channel-flexible;
- email-only participants remain first-class;
- inbound/outbound exchange are event/provenance concerns rather than a new ontology;
- Publication exists only for persistent exposure;
- DCE snapshot versus evolving client collection;
- visa chain as exact-revision review/decision composition;
- derived annotation versus autonomous IFJA-authored drawing;
- conceptual `Intake Item` decomposition is optional, not a mandatory canonical owner.

## Boundaries retained

```text
external surface != Pantheon
exchange != approval
published != approved
shared != contractual
visa comment != execution authority
annotation != issuer revision
derived_from != authorship transfer
email received != source validated
link opened != acknowledgement
runtime success != Evidence
```

## Implementation status

```text
documented = yes
schema changed = no
registry changed = no
runtime changed = no
pantheon-mvp changed = no
external access activated = no
publication/share-link implementation = no
visa approval owner implemented = no
```

## Verification target

Before merge:

- inspect the final diff for accidental authority expansion or lost document-lifecycle responsibilities;
- verify current main has not advanced incompatibly;
- run Pantheon governance / architecture checks on the exact PR head;
- merge only if the documentation change remains conflict-free and checks are green.
