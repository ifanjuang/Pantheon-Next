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
- `PANTHEON_SYSTEM_OWNERSHIP.md`.

```text
One logical artifact.
Many revisions.
Many surfaces.
Scoped actors.
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
- multiple user surfaces such as Cockpit, OpenWebUI, Obsidian or future clients.

The target is not application-to-application synchronization. The target is shared access to stable artifact identities and explicit revisions.

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

### Exact duplicate

A matching content digest may prove identical bytes.

The system may reuse the existing stored object while recording a new receipt, transmission or source event when that event matters.

```text
same digest != same receipt event
same filename != same content
```

### Probable new revision

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

### New artifact

If no existing identity is supported strongly enough, the source remains a new document candidate until classified.

```text
new file != automatically new revision
similar title != same document family
```

## 5. Revision preservation

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

## 6. Revision comparison

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

## 7. Dependency and impact analysis

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

## 8. Quotes, offers and variants

A revised commercial document is not always a new revision of the same offer.

The system should distinguish, as candidates:

```text
same offer / new revision
separate variant
replacement offer
new offer
```

Hermes may compare quote lines, totals, quantities, exclusions and CCTP / DPGF alignment.

Acceptance, rejection, negotiation, attribution or contractual effect remains a human / governed decision.

## 9. Knowledge-source updates

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

## 10. Team collaboration

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

## 11. External project participants

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

The existing professional role model and technical access policy must remain distinct.

```text
professional role != technical permission
technical permission != professional authority
button availability != approval authority
```

A BET may, for example, be allowed to:

```text
view selected project documents
upload a new revision of its own study
comment on selected artifacts
respond to a review request
```

without being allowed to inspect unrelated commercial, legal, memory or other-project material.

`SCOPE_ISOLATION.md` remains the owner of project, dossier, user and organization scope boundaries.

## 12. Access-grant gap to verify

The repository already models or discusses:

- users;
- organizations;
- contacts;
- professional party roles;
- project / dossier / user / organization scopes;
- confidentiality;
- `access_scope` document metadata;
- candidate storage access policies.

This review did not establish a stable, dedicated object that expresses the full generic relationship:

```text
subject X
may perform capability Y
on resource scope Z
until optional time T
```

Do not create a new canonical concept solely from this note.

Before implementation, verify again whether an existing authorization, resource, scope or policy object already covers the responsibility.

If no existing owner covers it, a future minimal access-grant contract may be justified because technical resource access is a distinct responsibility from professional role and Pantheon approval.

Any such contract should remain narrow and must not become:

- a professional role ontology;
- an approval engine;
- a provider permission router inside Pantheon;
- a replacement for runtime / identity-provider authorization;
- a source of project truth.

## 13. External portal posture

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

## 14. Inbox and assisted reconciliation

A project inbox may expose ambiguous intake candidates without forcing the user to manually classify every file.

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
high-confidence low-risk reconciliation -> may be streamlined
ambiguous identity / consequential effect -> review
```

## 15. Non-goals

This note does not introduce:

- a new document database;
- a second knowledge graph;
- a new memory store;
- application-to-application synchronization as authority;
- automatic replacement of prior revisions;
- automatic impact propagation;
- automatic Knowledge promotion;
- automatic approval;
- automatic external publication;
- mandatory Obsidian, OpenWebUI, Hindsight or Hermes dependency.

## 16. Future implementation acceptance criteria

A bounded implementation should eventually prove:

1. one logical document can retain multiple imported revisions;
2. exact duplicate bytes do not create false content versions;
3. a separate receipt event can still be recorded for duplicate bytes;
4. `version_seq` and `revision_label` remain distinct;
5. prior revisions remain retrievable after supersession;
6. a probable revision can be proposed without silent binding;
7. revision comparison preserves source references and uncertainty;
8. downstream impact candidates identify their exact baseline revision;
9. impacted artifacts are not automatically rewritten;
10. internal users can reach the same artifact from multiple surfaces;
11. stale concurrent writes cannot silently overwrite a newer revision;
12. an external participant sees only explicit project / resource scope;
13. professional role does not automatically confer technical access or approval authority;
14. removing an external surface leaves artifact identity and Pantheon state unchanged;
15. Knowledge update candidates preserve the newer and prior source provenance.

## 17. Convergence decision

The repository already contains the principal concepts required for agency collaboration and revised-source intake.

The preferred path is therefore:

```text
reuse document identity and versioning
reuse scope isolation
reuse party / professional roles
reuse index effect classification
reuse existing storage and provenance boundaries
reuse Project Anatomy relations for impact where they already exist
```

Do not add a collaboration platform ontology or a parallel version model.

The only candidate gap identified by this review is the generic technical access-grant responsibility. It remains a gap to verify, not a new approved concept.

```text
one artifact
many revisions
many actors
many surfaces
one scoped authority path
```
