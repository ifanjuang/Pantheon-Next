# Agency collaboration and version intake convergence

Status: candidate support note — convergence only, documented non-implemented.
Boundary profile: candidate_support_note.

This note reconciles existing Pantheon architecture-agency doctrine for team collaboration, bounded external access and intake of revised project documents.

It does not create a new authority model, identity provider, access-control engine, document store, synchronization service, workflow runtime, portal, plugin, queue, scheduler or automatic document-classification authority.

It reuses existing owners and boundaries from:

- `AGENCY_DOMAIN_PACK.md`;
- `DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`;
- `DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- `DOCUMENT_PRODUCTION_LIFECYCLE.md`;
- `INDEX_EFFECT_MATRIX.md`;
- `SCOPE_ISOLATION.md`;
- `EXTERNAL_TOOLS_POLICY.md`;
- `PANTHEON_GRAPH_MODEL.md`;
- `COCKPIT_ARCHITECTURE.md`;
- `PANTHEON_SYSTEM_OWNERSHIP.md`;
- `schemas/project_change_variant_candidate.schema.yaml`.

```text
One logical artifact.
Many revisions.
Many surfaces.
Scoped actors.
Purpose-specific currentness.
Pantheon governs consequential effects.
The human remains responsible for professional decisions.
```

## 1. Objective

The agency needs to support, without duplicating authority:

- internal collaborative work;
- external project participants such as clients, BETs, contractors and reviewers;
- import of new indices / revisions of plans, studies, quotes, reports and other project sources;
- preservation of previous revisions;
- comparison of revisions;
- impact analysis when a source changes;
- reusable Knowledge updates derived from changed sources;
- multiple user surfaces such as Cockpit, OpenWebUI, Obsidian or future clients;
- a fast user experience where routine document handling does not expose governance internals.

The target is not application-to-application synchronization. The target is shared access to stable artifact identities, explicit revisions and bounded capabilities.

## 2. Artifact-centered collaboration

Collaboration should be organized around one logical artifact identity rather than copies owned by individual applications or users.

```text
logical artifact
  -> revision 1
  -> revision 2
  -> revision 3
       -> representations / source files
```

Examples:

- one CCTP logical document with many working and issued revisions;
- one BET study with indices A, B and C;
- one quote or offer with successive revisions;
- one drawing family with successive issue states;
- one Knowledge Item with successive editorial revisions.

A surface may display, edit or comment on an artifact. It does not become the owner of the artifact merely because the work occurred there.

```text
Obsidian file != artifact identity
OpenWebUI conversation != artifact identity
Cockpit card != artifact identity
PDF export != artifact identity
```

The collaboration invariant is:

```text
shared artifact state
+ surface-local interaction state
```

not:

```text
application A <-> application B <-> application C truth synchronization
```

## 3. Internal sequence versus external revision label

The system should preserve two separate version dimensions when relevant:

```text
version_seq
= internal monotonic sequence used by the implementation owner

revision_label
= external professional label carried by the source or issuer
```

Examples of `revision_label` include:

```text
A
B
C
A1
A2
00
01
Rev.03
Indice D
```

The implementation must not assume a universal ordering rule for external labels beyond explicit project or issuer conventions.

```text
highest-looking revision_label != current authority
latest filename != current authority
newer upload timestamp != professional approval
```

`INDEX_EFFECT_MATRIX.md` remains the owner of the professional effect classification attached to an indexed version.

## 4. Revised-source intake

When a file is received through upload, email, NAS, Drive, SFTP, project portal or another approved connector, the system may classify the intake as one of three candidate outcomes:

```text
exact duplicate
probable new revision of an existing artifact
probable new artifact
```

### 4.1 Exact duplicate

A matching content digest may prove identical bytes.

The system may reuse the existing stored object while recording a new receipt, transmission or source event when that event matters.

```text
same digest != same receipt event
same filename != same content
```

### 4.2 Probable new revision

A changed digest plus matching project, issuer, document family, subject, lot, reference or other identifiers may support a revision candidate.

Hermes or another runtime may propose:

```text
candidate_artifact_ref
candidate_revision_label
candidate_supersedes_ref
confidence
matching_reasons
uncertainties
```

The runtime must not silently bind an ambiguous source to an existing artifact when the distinction matters professionally.

### 4.3 New artifact

If no existing identity is supported strongly enough, the source remains a new document candidate until classified.

```text
new file != automatically new revision
similar title != same document family
```

## 5. Contextual upload before AI inference

The easiest and safest intake path is explicit user context.

When a user starts from an existing artifact and chooses:

```text
Déposer un nouvel indice
```

the artifact identity is already known.

The system does not need an AI model to guess the document family. The upload request carries the target artifact reference and may ask only for the source-declared revision label when it is not reliably extractable.

```text
known artifact + explicit new-revision action
-> deterministic identity binding
-> duplicate check
-> revision creation candidate
-> extraction / comparison
```

AI-assisted reconciliation is reserved for generic intake where the user drops an unclassified source into a project Inbox.

```text
contextual upload -> deterministic first
unclassified Inbox -> inference candidate
```

This reduces latency, model cost and false matches while improving usability.

## 6. Revision preservation

A new revision must not overwrite the previous source or erase its provenance.

The existing document-version posture applies:

```text
document identity
  -> version_seq
  -> revision_label
  -> supersedes_version_id
  -> source digest
  -> issuer
  -> received_at / produced_at
  -> status / effect class
```

Supersession changes current-use posture. It does not erase history.

```text
superseded != deleted
obsolete != never existed
```

## 7. Purpose-specific currentness

There must not be one universal persisted `current_version` that collapses professional uses.

The same logical artifact may legitimately have different revisions that are current for different purposes.

Example:

```text
study C = latest received
study B = latest reviewed
study B = current coordination baseline
study A = signed contractual baseline
```

Currentness should therefore be exposed as deterministic projections over version metadata, effect class, decisions and evidence rather than inferred from filename order.

Candidate projections include:

```text
latest_received
latest_reviewed
current_working
current_for_coordination
current_for_consultation
current_contractual
current_for_execution
current_for_site
latest_as_built_candidate
```

These are projection concerns, not new authority objects.

A projection must disclose the exact revision and the basis used to select it.

```text
current_for_execution -> revision C
basis -> issued_for_execution + applicable approval / visa reference
```

If the inputs are insufficient or conflicting, the projection is unresolved rather than guessed.

```text
latest_received != current_for_execution
latest_reviewed != current_contractual
highest revision label != current authority
```

## 8. Revision comparison

A runtime may compare two revisions to produce a bounded comparison candidate.

Useful outputs include:

- changed pages, sheets, clauses or articles;
- added / removed sections;
- changed quantities, amounts, dimensions or performance values;
- changed normative references;
- changed exclusions or variants;
- changed issue metadata;
- uncertainty where extraction is insufficient.

The comparison remains a technical or professional review candidate.

```text
difference detected != significance established
difference detected != project state changed
```

Comparison should reuse cached structured extraction when source digest and processing configuration are unchanged.

A new revision should process only the new source and the comparison required against selected baselines; it should not force full reprocessing of unrelated project documents.

## 9. Dependency and impact analysis

When a new revision is received, the system may identify artifacts that explicitly reference the superseded revision.

Example:

```text
BET thermal study B
  -> used by CCTP C
  -> used by notice
  -> used by cost review

BET thermal study C received
  -> impact candidates: CCTP, notice, cost review
```

The system may create review candidates or tasks.

It must not silently rewrite dependent artifacts.

```text
new source revision != dependent artifact automatically updated
impact candidate != required professional change
```

Project Anatomy relations may support impact navigation where a governed relation already exists. A new parallel dependency graph must not be created merely for version intake.

Impact candidates must preserve the exact baseline that created the dependency.

```text
analysis ACT
-> based_on CCTP revision C

CCTP revision D received
-> analysis ACT remains historically based_on C
-> impact candidate may request re-analysis against D
```

## 10. Variants are not generic branches

The repository already owns a bounded Project-change variant contract in `project_change_variant_candidate.schema.yaml`.

That contract explicitly states:

```text
variant produced != ChangeCandidate persisted
variant persisted != variant selected
variant selected != Project mutation applied
```

and explicitly forbids creation of a generic branch object.

Therefore this collaboration model must not introduce:

```text
artifact -> branch -> revision
```

as a universal architecture.

For Project attribute alternatives, reuse:

```text
project_change_variant candidate
-> existing ChangeCandidate owner
-> comparison projection
-> human selection or refusal
-> separately governed application
```

For document and commercial alternatives, treat a genuinely separate variant as a separate logical artifact associated with the same consultation, lot, issuer, source request or parent business context unless an existing owner explicitly models it otherwise.

```text
new revision
= continuation of the same artifact identity

variant
= sibling artifact / alternative proposition
```

A variant may itself have revisions.

```text
base offer
  -> revision A
  -> revision B

variant offer 01
  -> revision A
  -> revision B
```

No generic branch runtime is required.

## 11. Quotes and offers

A revised commercial document is not always a new revision of the same offer.

The system should distinguish, as candidates:

```text
same offer / new revision
separate variant
replacement offer
new offer
```

Hermes may compare quote lines, totals, quantities, exclusions and CCTP / DPGF alignment.

A quote or offer analysis must pin its baseline package and document revisions.

```text
offer analysis
-> offer revision B
-> CCTP revision C
-> DPGF revision B
-> consultation package P3
```

When one baseline changes, the previous analysis remains valid as a historical analysis of its exact inputs but may become stale for current use.

Acceptance, rejection, negotiation, attribution or contractual effect remains a human / governed decision.

## 12. Knowledge-source updates

A newer source may affect reusable Knowledge without automatically replacing it.

```text
new source edition
  -> compare with prior source
  -> identify Knowledge Items that cite prior source
  -> propose Knowledge update candidates
  -> preserve source provenance
```

A Knowledge Item remains distinct from its source.

```text
source updated != Knowledge silently rewritten
Knowledge updated != Evidence admitted
```

A newer source may coexist with the older source when historical applicability matters.

The Knowledge update should identify which source edition and passages support the proposed editorial change.

## 13. Team collaboration

Internal agency users may reach the same artifact through different surfaces.

```text
Cockpit
OpenWebUI
Obsidian
future editor
```

The surfaces should share artifact identity and revision context rather than synchronize private application state with each other.

Preferred pattern:

```text
shared artifact identity
+ shared revision identity
+ shared project scope
+ surface-local UX
```

Avoid:

```text
OpenWebUI <-> Obsidian <-> Cockpit bidirectional truth synchronization
```

For the first implementation, optimistic concurrency is sufficient unless real simultaneous co-editing is demonstrated as a requirement.

A write candidate should identify its exact base revision or content digest. A stale base produces a conflict or rebase path, not silent overwrite.

Real-time CRDT collaboration remains an optional future runtime / editor capability.

## 14. Identity, professional role, technical access and authority

Four dimensions must remain independent:

```text
identity
= who is this actor?

professional role
= what does the actor represent in the operation?

technical access
= which resources and operations may the actor currently reach?

professional authority
= which consequential decisions may the actor legitimately make?
```

Therefore:

```text
professional role != technical permission
technical permission != professional authority
button availability != approval authority
identity authenticated != action approved
```

A BET may be technically allowed to upload its study without being authorized to validate the architect's CCTP.

A client may be technically allowed to submit a decision through a decision surface, but the resulting record still needs the applicable identity, scope and decision semantics.

## 15. External project participants

External access should be resource- and scope-bounded.

Examples include:

- project owner / client;
- BET structure;
- BET thermal;
- bureau de contrôle;
- SPS;
- contractor;
- subcontractor;
- external reviewer.

A BET may, for example, be allowed to:

```text
view selected project documents
upload a new revision of its own study
comment on selected artifacts
respond to a review request
```

without being allowed to inspect unrelated commercial, legal, memory or other-project material.

`SCOPE_ISOLATION.md` remains the owner of project, dossier, user and organization scope boundaries.

## 16. Technical access placement decision

The repository already models or discusses:

- users;
- organizations;
- contacts;
- professional party roles;
- project / dossier / user / organization scopes;
- confidentiality;
- `access_scope` document metadata;
- candidate storage access policies;
- permission scopes on governed resource relations.

The review did not find an implemented general user-to-resource authorization owner in `pantheon-mvp`.

That does not justify creating a new Pantheon kernel concept.

The preferred placement is:

```text
Pantheon Next
-> defines scope, confidentiality, authority and consequential-boundary doctrine

identity / access implementation
-> authenticates principals and enforces technical resource permissions

pantheon-mvp
-> records / projects the professional resource state and can consume bounded principal / access context

Cockpit / external portal
-> exposes only the capabilities permitted by the effective access context
```

Pantheon must not become an IAM, RBAC engine, identity provider or general permission router.

If a future implementation requires a durable access record, its smallest implementation-owned shape may need to answer:

```text
principal
resource scope
actions
validity window
issuer / grant provenance
revocation state
```

but this note does not canonize that shape or name a new governance object.

Professional authority remains governed separately.

## 17. External portal posture

External participants should not be required to adopt the agency's internal editor.

A future web surface may expose only the capabilities needed by the participant, for example:

```text
view
open / download
upload new revision
comment
respond to request
review candidate
```

The portal remains a projection and interaction surface.

The server remains authoritative for artifact identity, version relations and scoped access decisions.

External users should normally receive the simplest project-specific view, not the full internal Cockpit.

Example:

```text
PROJECT

Documents to review       4
Documents expected        2
Questions                  3

Thermal study
current submitted index: B
[Upload new index]

Architect drawings
current consultation index: D
[Open]

Question 14
Glazing performance
[Respond]
```

The visible simplicity does not flatten the internal model.

## 18. Project Inbox and assisted reconciliation

A project Inbox may expose ambiguous intake candidates without forcing the user to manually classify every file.

Example:

```text
Study_structure_C.pdf
-> probable new revision of Study structure B

Quote_Martin_2.pdf
-> probable revised offer for lot 07

Thermal_report.pdf
-> probable new document

Technical guide 2026.pdf
-> possible reusable Knowledge source
```

Hermes may perform matching, extraction and comparison.

The human should only need to resolve ambiguity or consequence.

```text
explicit contextual intake -> deterministic path
high-confidence low-risk reconciliation -> may be streamlined
ambiguous identity / consequential effect -> review
```

The Inbox is a UX projection over intake state. It is not a new authority or storage model.

## 19. Scenario A — BET study revision

### Initial state

```text
artifact: thermal-study
revision B
issuer: BET thermal
status: reviewed
current_for_coordination: B
```

### External action

The BET opens the project portal from the `thermal-study` artifact and selects:

```text
Upload new index
```

The identity is explicit before upload.

### Intake

```text
source capture C
-> digest check
-> source metadata extraction
-> declared / detected revision_label C
-> revision candidate superseding B
```

If the bytes already exist, the system records a receipt event rather than a false new content revision.

### Processing

Hermes may:

- compare B and C;
- extract changed performance values;
- identify changed assumptions;
- locate dependent artifacts that cite B;
- produce impact candidates.

### Result

```text
latest_received: C
current_for_coordination: B until the applicable review changes it
```

Potential impacts are shown without rewriting CCTP, notice, estimate or Project Anatomy claims.

## 20. Scenario B — revised quote or commercial variant

### Initial state

```text
consultation: lot 07
contractor: Company M
base offer artifact
revision A
analysis baseline: CCTP C + DPGF B
```

### New intake

If Company M submits a corrected price schedule for the same offer:

```text
base offer revision B
```

If Company M submits an intentionally different technical solution:

```text
variant offer 01 artifact
revision A
```

The variant is not forced into the revision chain of the base offer.

### Processing

Hermes may compare:

- line items;
- total price;
- quantities;
- exclusions;
- CCTP coverage;
- DPGF alignment;
- variant scope.

### Authority

```text
newer offer != selected offer
analysis != attribution
commercial variant != Project branch
```

Any prior offer analysis remains pinned to its exact source revisions.

## 21. Scenario C — agency-authored CCTP

### Working state

One CCTP logical artifact may be edited through an internal workspace while retaining stable revision identity.

```text
CCTP logical artifact
-> working revision 24
-> structured content
-> Markdown / editor projection
```

Obsidian may be one editing surface. OpenWebUI may request Hermes changes. Cockpit may expose status and review.

### Editing

Low-risk editing may create ordinary working revisions without an approval ceremony for every paragraph.

The write path still uses exact-base optimistic concurrency.

```text
base revision 24
-> user or Hermes edit
-> revision 25
```

A stale edit cannot silently overwrite revision 25.

### Issue

When the agency issues a DCE:

```text
working revision
-> review
-> issued_for_consultation effect
-> exact package / export references
```

The PDF or DOCX is a representation / issued source of the logical CCTP, not a new parallel CCTP authority.

### Subsequent work

A later working revision does not retroactively change the consultation baseline.

```text
latest_working: 27
current_for_consultation: 25
```

## 22. Scenario D — Knowledge source edition update

### Initial state

```text
source: technical guide 2025
Knowledge Item: waterproofing practice
```

### New source

The 2026 edition is imported.

It becomes a new source capture / source edition, not an overwrite of 2025.

### Processing

Hermes may:

- compare source editions;
- identify changed sections;
- find Knowledge Items citing 2025;
- prepare an editorial update candidate with source anchors.

### Result

```text
source edition 2026 received
!= Knowledge Item automatically rewritten
```

Historical projects may still legitimately reference the 2025 edition when that was the applicable source at the time.

## 23. Performance and graceful degradation

The collaboration and intake path should remain efficient by default.

### Prefer deterministic work before model work

```text
explicit artifact context
content digest
stable metadata
known issuer / project / lot
exact prior revision
```

should be used before semantic inference.

### Reuse derived representations

If a source digest and processing configuration are unchanged, reuse existing extraction rather than rerun OCR, structure recovery or embeddings.

### Keep binaries outside the register by default

Large project originals remain in the approved storage layer. The register retains identity, hashes, provenance, status, links and derived searchable structure.

### Scope retrieval before broad retrieval

Project users and external actors should query only their permitted project / resource corpus rather than filter a global result after retrieval.

### Optional components must degrade gracefully

```text
Obsidian unavailable
-> another editor can work on the artifact

Hindsight unavailable
-> project sources / Knowledge / Task context still work

Hermes unavailable
-> stored artifacts and revisions remain accessible

real-time co-editing unavailable
-> optimistic concurrency remains functional
```

No optional client or memory provider becomes a dependency of document identity or project authority.

## 24. User-facing simplicity rules

The internal model may be rich, but routine flows should normally expose only the next useful action.

Examples:

```text
Upload a new index
Compare with previous
See impacts
Open current consultation version
Open contractual version
Ask Hermes
Publish / transmit
```

Do not force users to select internal status vocabulary when it can be derived safely from the action and context.

Do not hide professional distinctions when they affect consequence.

```text
simple interaction != collapsed semantics
```

## 25. Non-goals

This note does not introduce:

- a new document database;
- a second knowledge graph;
- a generic branch runtime;
- a new memory store;
- application-to-application synchronization as authority;
- a Pantheon IAM / RBAC engine;
- automatic replacement of prior revisions;
- automatic impact propagation;
- automatic Knowledge promotion;
- automatic approval;
- automatic external publication;
- mandatory Obsidian, OpenWebUI, Hindsight or Hermes dependency.

## 26. Future implementation acceptance criteria

A bounded implementation should eventually prove:

1. one logical document can retain multiple imported revisions;
2. exact duplicate bytes do not create false content versions;
3. a separate receipt event can still be recorded for duplicate bytes;
4. `version_seq` and `revision_label` remain distinct;
5. prior revisions remain retrievable after supersession;
6. a contextual `Upload new index` path can bind an explicit artifact without AI identity inference;
7. a probable revision can be proposed from a generic Inbox without silent binding;
8. revision comparison preserves source references and uncertainty;
9. downstream impact candidates identify their exact baseline revision;
10. impacted artifacts are not automatically rewritten;
11. purpose-specific current projections may point to different revisions;
12. unresolved currentness remains visible rather than guessed;
13. internal users can reach the same artifact from multiple surfaces;
14. stale concurrent writes cannot silently overwrite a newer revision;
15. an external participant sees only explicit project / resource scope;
16. professional role does not automatically confer technical access or approval authority;
17. technical access enforcement can be replaced without changing Pantheon professional semantics;
18. removing an external surface leaves artifact identity and Pantheon state unchanged;
19. a Project variant uses the existing Project variant / ChangeCandidate path rather than a generic branch object;
20. a commercial variant can remain a sibling offer artifact with its own revision history;
21. quote analyses remain pinned to exact offer / CCTP / DPGF baselines;
22. Knowledge update candidates preserve the newer and prior source provenance;
23. disabling Hermes does not remove stored versions or change current authority;
24. unchanged source digests reuse existing derived processing where configuration is unchanged.

## 27. Convergence decision

The repository already contains the principal concepts required for agency collaboration and revised-source intake.

The preferred path is therefore:

```text
reuse document identity and versioning
reuse scope isolation
reuse party / professional roles
reuse index effect classification
reuse existing Project variant / ChangeCandidate path
reuse existing storage and provenance boundaries
reuse Project Anatomy relations for impact where they already exist
compute purpose-specific currentness as projections
keep technical access enforcement outside the Pantheon kernel
```

Do not add a collaboration platform ontology, a generic branch model, a parallel version model or a Pantheon permission engine.

The remaining implementation questions are deliberately narrower:

- exact identity / access binding selected for agency and external users;
- deterministic resolver rules for each purpose-specific current projection;
- exact pantheon-mvp persistence and API slice for project-document revisions if not already owned by an executable slice;
- UX composition for internal Inbox and external portal;
- measured threshold at which real-time CRDT collaboration becomes justified.

```text
one artifact
many revisions
many actors
many surfaces
purpose-specific currentness
one scoped authority path
```
