# Pantheon Cockpit — Hermes-Authored Card Review UX

Status: candidate support specification — documented non-implemented.
Boundary profile: candidate_support_note.

This document defines a transverse Cockpit review mode for any content-bearing card whose primary content was authored, rewritten, synthesized, expanded or materially reorganized by Hermes.

It complements:

- `DOCUMENT_PRODUCTION_LIFECYCLE.md`;
- `DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- `CARD_STACK_MODEL.md`;
- `PANTHEON_COCKPIT_UX_SPEC.md`;
- `KNOWLEDGE_NAVIGATION_UX.md`;
- `docs/domain-packs/architecture/PROJECT_NAVIGATION_UX.md`;
- `ITERATIVE_DELIBERATION_LIFECYCLE.md`;
- `WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`;
- `HERMES_INTEGRATION.md`.

It does not implement a card component, editor, comment system, review engine, workflow engine, queue, scheduler, Hermes Skill, archive service, chunker, embedding model, vector store, database migration or external action.

```text
Hermes may author a candidate.
The Cockpit exposes the exact draft and review loop.
Pantheon governs status, version identity and finalization scope.
The human validates one exact index and draft version.
Hermes finalizes only the authorized bundle.
```

## 1. Purpose

A card created from a faithful source transformation and a card containing newly authored language do not have the same review posture.

The Cockpit must distinguish:

```text
source transformation
= extraction, OCR, transcription, conversion, Markdown normalization,
  structural preservation or sectorization without material editorial authorship

Hermes authorship
= drafting, synthesis, rewriting, interpretation, enrichment, expansion,
  insertion, reorganization, conclusion writing or other material composition
```

When Hermes materially authors the card's primary content, the card must be surfaced as a draft before it can appear as an ordinary retained card.

```text
Hermes-authored content
-> Draft Card surfaced for review
-> direct edits and revision requests
-> human validation of an exact index/version/hash
-> bounded finalization request sent to Hermes
-> archive, chunking, embedding and index publication as authorized
-> ordinary card appearance after verified finalization
```

The rule applies across card families when the card's primary payload is an authored artifact, including:

- Knowledge items;
- project documents;
- reports;
- meeting minutes;
- notices;
- letters;
- methods or guides when they are being authored as retained content;
- project notes intended to become retained documents;
- text-insertion results;
- other content-bearing cards.

It does not automatically convert every card containing a generated short summary into a full Draft Card. The trigger is material authorship of the retained primary content.

## 2. Authorship classification

### 2.1 Faithful transformation

The following operations alone do not trigger the authored-card review mode:

```text
native text extraction
OCR faithful transcription
speech-to-text faithful transcription
format conversion
PDF or Office to Markdown conversion
heading normalization
whitespace and encoding cleanup
page-reference preservation
chunking
embedding
sectorization
source metadata capture
```

These operations may still require extraction-quality review when warnings, ambiguity or low confidence exist.

```text
not editorially authored
!= automatically correct
```

### 2.2 Material Hermes authorship

The following operations trigger Draft Card review when they affect the primary retained content:

```text
drafting from notes
writing from a voice account
synthesis across several sources
rewriting or reformulation
adding explanatory passages
adding details not present verbatim in one source
expanding terse notes into prose
organizing facts into a narrative
creating a conclusion
creating recommendations
creating actions, decisions or responsibilities from interpreted context
merging several passages semantically
inserting generated text into an existing document
materially enriching or restructuring an existing draft
```

### 2.3 Mixed content

A card containing both source-preserved content and Hermes-authored content enters Draft Card mode.

```text
mixed faithful extraction + authored synthesis
= review required
```

The authored segments should remain identifiable when segment-level provenance is available.

### 2.4 Candidate classification shape

```yaml
content_origin:
  transformation_mode: faithful | mixed | authored
  operations:
    - ocr
    - markdown_conversion
    - synthesis
  primary_content_authored_by_hermes: true
  editorial_review_required: true
  classification_reason:
  classified_by_binding:
  classified_at:
```

The trigger should be deterministic from the requested operations and output manifest where possible, not guessed only from fluent wording.

## 3. Non-equivalence rules

```text
OCR completed != Hermes-authored draft
Markdown generated != authored document
summary displayed != primary card content necessarily authored
Hermes generation complete != human reviewed
comment sent != revision applied
revision applied != revision accepted
content validated != finalization completed
finalization requested != archived
archived != chunked
chunked != embedded
embedded != index published
index published != retrieval verified
normal card appearance != Evidence status
Indice A active != Indice B draft accepted
```

## 4. Draft Card as a transverse visual state

Draft Card is not a new permanent card family.

It is a temporary review state applied over the normal visual grammar of the underlying card family.

```text
Knowledge item normal family
+ Draft Card review state

Project document normal family
+ Draft Card review state

Other content card normal family
+ Draft Card review state
```

After successful finalization, the card returns to its ordinary family appearance while retaining its index and provenance.

### 4.1 Priority surfacing

A Draft Card requiring review should be promoted above ordinary retained cards in the relevant Cockpit scope.

Candidate placements:

```text
À relire
Drafts requiring attention
Project review stack
Knowledge review stack
Home / Requests to process
```

The system should not bury a required review inside the destination folder as if the content were already retained.

Candidate priority dimensions:

```yaml
draft_attention:
  review_required: true
  blocking_finalization: true
  requested_by:
  due_at:
  consequence_level:
  unresolved_comment_count:
  destination_scope:
```

The position indicates required attention, not truth or approval.

### 4.2 Visible draft markers

The Draft Card should expose at least:

- a persistent `BROUILLON` label;
- an edit or review icon;
- the target index;
- the internal draft revision;
- review state;
- unresolved-comment count;
- last modification time;
- authoring origin such as `Rédigé avec Hermès`;
- the intended destination;
- the blocking reason for finalization.

The draft state must remain recognizable without relying only on color.

### 4.3 Underlying family identity

The card may preserve a restrained indication of its future family:

```text
Knowledge draft
-> retains Knowledge icon or family label

Project-document draft
-> retains project color accent and project reference
```

But it must not use the fully finalized ordinary appearance before finalization is verified.

## 5. Recto — compact draft summary

The front of a Draft Card should remain concise and actionable.

Recommended fields:

```text
BROUILLON
card title
card or document type
target index
internal draft revision
Rédigé avec Hermès
current review status
last updated
unresolved comments
source count or source posture
target project / phase / Knowledge folder
finalization blocked reason
```

Example:

```text
BROUILLON
Compte rendu de chantier — Lieurey
Indice A · Brouillon v3
Rédigé avec Hermès
5 sources · 2 commentaires ouverts
Destination : 50_Chantier
Validation requise avant archivage et indexation
```

Recommended actions:

```text
Lire et modifier
Commentaires
Comparer les versions
Comparer aux sources
Valider l'indice
Rejeter / abandonner
```

`Valider l'indice` must identify the exact target index and draft revision.

## 6. Verso / full-content review surface

### 6.1 Complete document access

The reverse side or detail surface should expose the complete draft content, not only a truncated preview.

The implementation may use:

- a card back on desktop;
- a full-screen editor;
- an expanded panel;
- a side sheet;
- a `Recto / Document complet` segmented control;
- another accessible detail surface.

The semantic requirement is:

```text
front = review orientation
back/details = complete content and revision tools
```

A literal 3D flip is optional and must not be required on mobile or for reduced-motion users.

### 6.2 Direct modification

An authorized reviewer may edit the draft directly in the Cockpit.

A direct edit should produce a traceable new draft revision or patch, rather than silently mutating the reviewed content.

Candidate direct-edit flow:

```text
open Draft Version A-v3
-> edit paragraph
-> save changes
-> create Draft Version A-v4
-> preserve A-v3
-> review status returns to required for A-v4
```

Candidate patch shape:

```yaml
human_draft_patch:
  patch_id:
  source_draft_version_id:
  target_index:
  selection_or_anchor:
  previous_content_hash:
  patch_content:
  created_by:
  created_at:
  resulting_draft_version_id:
```

### 6.3 Comment-based Hermes revision

The full-content surface should expose a `Commenter` action.

A comment may target:

- the full document;
- one section;
- one paragraph;
- one sentence;
- a table;
- a selected range;
- a missing section position.

The comment should be converted into a structured revision request sent through the Pantheon backend to Hermes.

```text
Cockpit comment
-> bounded Revision Request
-> Pantheon scope and policy check
-> Hermes revision
-> new Draft Version
-> Cockpit diff and review
```

The browser must not call Hermes directly with a privileged secret.

## 7. Revision request types

The comment action may offer common intents while preserving free-form instruction.

Candidate intents:

```text
Corriger
Améliorer la rédaction
Clarifier
Raccourcir
Développer
Ajouter des détails
Enrichir une section
Ajouter des exemples
Réorganiser
Ajouter des sources ou citations
Vérifier la cohérence
Rendre plus professionnel
Rendre plus diplomatique
Rendre plus ferme
Ajouter une réserve
Corriger une responsabilité ou une attribution
Insérer du texte
Supprimer un passage
Autre instruction
```

Candidate request shape:

```yaml
revision_request:
  revision_request_id:
  card_id:
  draft_document_id:
  source_draft_version_id:
  target_index:
  requested_by:
  requested_at:
  request_type:
  user_comment:
  selection_anchor:
  selected_text_hash:
  surrounding_context_ref:
  source_scope_refs: []
  preserve_requirements: []
  forbidden_changes: []
  expected_output: revised_draft | patch_candidate | clarification_only
```

A revision request is not approval for unrelated scope expansion.

### 7.1 Adding details

When asked to add details, Hermes should distinguish:

```text
detail supported by existing sources
vs
detail inferred from context
vs
detail requiring a new user fact or source
```

Missing information must not be invented.

### 7.2 Enrichment

An enrichment request may authorize broader use of selected project or Knowledge context.

The request should state the allowed context scope.

```yaml
enrichment_scope:
  project_refs: []
  knowledge_refs: []
  source_refs: []
  external_research_allowed: false
```

Hermes must expose newly introduced sources or assumptions.

## 8. Comment and revision lifecycle

Candidate comment statuses:

```text
open
sent_to_hermes
revision_running
revision_proposed
resolved_by_revision
resolved_without_change
rejected
superseded
```

Candidate model:

```yaml
review_comment:
  comment_id:
  card_id:
  draft_version_id:
  target_index:
  anchor:
  body:
  created_by:
  created_at:
  status:
  hermes_run_ref:
  resulting_draft_version_id:
  resolution_note:
```

A comment remains linked to the exact version and selection that motivated it.

A new revision should not silently mark every open comment resolved. Each resolution should be explicit or mechanically linked to the applied change.

## 9. Hermes revision result

Hermes should return a structured revision result.

```yaml
revision_result:
  revision_request_id:
  source_draft_version_id:
  resulting_draft_version_id:
  target_index:
  draft_revision:
  content_ref:
  content_hash:
  diff_ref:
  change_summary:
  source_additions: []
  assumption_additions: []
  unresolved_items: []
  warnings: []
  runtime_status:
```

The Cockpit should expose:

- what changed;
- what did not change;
- newly used sources;
- newly introduced assumptions;
- unresolved requests;
- the full resulting content;
- a diff against the previous draft.

```text
Hermes revised != reviewer accepted
```

## 10. Index and draft revision model

### 10.1 Two axes

The UX should distinguish the public document index from the working draft revision.

```text
Document index
= retained edition identity visible after finalization

Draft revision
= working iterations before that index is finalized
```

Example:

```text
Indice A · Brouillon v1
Indice A · Brouillon v2
Indice A · Brouillon v3
Indice A · Validé
Indice A · Finalisé
```

Later modification:

```text
Indice A · Actif
Indice B · Brouillon v1
Indice B · Brouillon v2
Indice B · Validé, finalisation en cours
Indice B · Actif
Indice A · Superseded but retained
```

### 10.2 Candidate shape

```yaml
card_revision_identity:
  card_id:
  document_id:
  active_index:
  target_index:
  index_scheme: alphabetic | numeric | semantic | project_defined
  draft_revision_number:
  draft_version_id:
  content_hash:
  supersedes_index:
  review_status:
  finalization_status:
```

### 10.3 Index allocation

The project or Knowledge policy determines the index scheme.

Candidate examples:

```text
A, B, C
01, 02, 03
P01, P02
Rev.0, Rev.1
project-defined code
```

An index should not be silently reused for materially different finalized content.

A failed or abandoned draft may keep its draft lineage without becoming an active published index.

### 10.4 Index display after finalization

Once the card returns to ordinary appearance, it must continue to display its active index.

Recommended compact display:

```text
Indice A
Mis à jour le 23 juillet 2026
```

The index remains visible in:

- card front or metadata line;
- full document view;
- download filename or metadata where applicable;
- archive record;
- chunk and embedding manifests;
- retrieval citation metadata;
- later revision comparison.

## 11. Human validation

### 11.1 Exact validation target

The reviewer validates:

```text
one card
one target index
one exact draft version
one content hash
one declared finalization bundle
```

Candidate decision:

```yaml
card_validation_decision:
  validation_id:
  card_id:
  document_id:
  target_index:
  draft_version_id:
  content_hash:
  reviewer:
  validated_at:
  decision: accepted | corrections_required | rejected
  unresolved_comments_acknowledged: []
  finalization_bundle_ref:
```

Validation of `Indice A · Brouillon v3` does not validate `Indice A · Brouillon v4`.

### 11.2 Validation action label

The UI should make the exact consequence visible.

Candidate button labels:

```text
Valider l'indice A
Valider et demander la finalisation
Demander des corrections
Rejeter ce brouillon
```

### 11.3 Unresolved comments

By default, unresolved blocking comments prevent validation.

A reviewer may explicitly accept a known unresolved point only when policy allows it and the acceptance is recorded.

## 12. Finalization request

### 12.1 User experience

After validation, the Cockpit should immediately show a clear confirmation:

```text
Indice A validé.
Demande de finalisation envoyée à Hermès.
```

The card enters:

```text
validé — finalisation en attente
```

or:

```text
finalisation en cours
```

It does not yet take the ordinary retained appearance.

### 12.2 Finalization bundle

The validation surface should show which operations will be requested.

Candidate bundle:

```yaml
finalization_bundle:
  freeze_validated_content: true
  render_formats:
    - markdown
    - pdf
    - docx
  sectorize: true
  archive: true
  generate_chunks: true
  generate_embeddings: true
  publish_index: true
  retrieval_verification: true
  distribute: false
```

The exact bundle may vary by card type and policy.

```text
content validation
!= authorization for every possible external effect
```

A single validation action may authorize the declared standard finalization bundle when the bundle is visible and previously governed. Distribution remains separately governed unless explicitly included under an applicable gate.

### 12.3 Structured request

```yaml
finalization_request:
  finalization_request_id:
  card_id:
  document_id:
  target_index:
  validated_draft_version_id:
  content_hash:
  validation_decision_ref:
  finalization_bundle_ref:
  destination_refs: []
  archive_policy_ref:
  chunking_profile_ref:
  embedding_profile_ref:
  index_scope_ref:
  requested_by:
  requested_at:
```

Pantheon checks the request and delegates the executable operations to Hermes or other approved bindings.

## 13. Finalization progress

The Cockpit should display only progress actually exposed by Hermes or the selected bindings.

Candidate steps:

```text
Validation recorded             completed
Final Markdown frozen           completed
PDF / DOCX rendering            running
Sectorization                   pending
Archiving                       pending
Chunking                        pending
Embeddings                      pending
Index publication               pending
Retrieval verification          pending
```

Quantified progress may be displayed only when measured:

```text
Chunks: 42 / 78
Embeddings: 42 / 78
```

The card should expose last-observed time and stale/unreachable status as defined by `DOCUMENT_LIFECYCLE_GOVERNANCE.md`.

## 14. Finalization result

Hermes should return a structured result rather than only `done`.

```yaml
finalization_result:
  finalization_request_id:
  card_id:
  document_id:
  finalized_index:
  validated_content_hash:
  output_artifacts: []
  archive_record_ref:
  sectorization_refs: []
  chunk_manifest_ref:
  embedding_manifest_ref:
  index_publication_ref:
  retrieval_verification_ref:
  warnings: []
  errors: []
  runtime_status:
  completed_at:
```

Pantheon records observed runtime success separately from governance and professional status.

## 15. Card appearance transition

### 15.1 Before validation

```text
Draft Card
BROUILLON label
priority surfaced
full review tools available
normal retained appearance withheld
```

### 15.2 After validation, before finalization

```text
Validated Draft Card
Indice A validé
finalization pending or running
content read-only by default
normal retained appearance still withheld
```

A new edit after validation invalidates the validated hash and creates a new Draft Version requiring re-validation.

### 15.3 After successful finalization

The card returns to the ordinary visual grammar of its family.

Examples:

```text
Knowledge item
-> neutral card with thick gradient outline

Project document
-> ordinary project-document card with project accent

Other retained card
-> its owner-defined normal family appearance
```

The ordinary card still shows:

- active index;
- current status;
- last updated date;
- source/provenance access;
- archived or indexed posture where useful;
- warning badge when finalization completed with warnings.

### 15.4 Partial or failed finalization

If one step fails, the card must not falsely take the fully finalized appearance.

Candidate states:

```text
finalized_with_warnings
archive_completed_index_pending
archive_failed
embedding_failed
index_verification_failed
finalization_unreachable
```

The UI should state what succeeded and what remains blocked.

## 16. Later modification of a finalized card

A later modification creates a new target index or revision according to policy.

Recommended default:

```text
active Indice A remains available
-> user requests modification
-> create Indice B · Brouillon v1 from A
-> review and Hermes revision loop
-> validate exact B version
-> finalize B
-> activate B
-> retain A as superseded history
```

The active finalized card must not be silently replaced while the new draft is under review.

### 16.1 Modification request

```yaml
new_index_request:
  request_id:
  card_id:
  source_active_index:
  proposed_target_index:
  requested_changes:
  requested_by:
  requested_at:
  preserve_refs: []
```

### 16.2 Concurrent display

While a new index is being drafted, the Cockpit may show:

```text
Indice A — actif
Indice B — brouillon, relecture requise
```

The ordinary card may expose a badge:

```text
Nouvel indice en préparation
```

### 16.3 Rollback and supersession

Finalizing a new index does not delete the prior one.

```text
Indice B active
Indice A superseded
```

Rollback selects a retained prior index according to the applicable decision and index-publication policy.

## 17. Card-type specializations

### 17.1 Knowledge Card

A Hermes-authored Knowledge item:

- appears first as Draft Card;
- exposes complete authored content and source lineage;
- cannot take the thick-gradient normal appearance until finalization;
- shows active index after finalization;
- may remain derived and non-Evidence after publication.

### 17.2 Project Document Card

A Hermes-authored project document:

- appears in the project review stack before ordinary phase retention;
- shows proposed project phase and filename;
- requires exact-index validation;
- is sectorized and archived only during the authorized finalization bundle;
- shows active index and project phase after finalization.

### 17.3 Text insertion card or existing-document revision

A generated insertion or rewrite:

- targets one existing active index;
- creates a new draft/index candidate;
- exposes exact diff;
- does not mutate the active retained index;
- follows the same validation and finalization transition.

### 17.4 Project identity and directory cards

A Project Card, Contacts Card or Entreprises Card may contain Hermes-proposed fields without becoming one monolithic authored-document Draft Card.

Field-level candidate and review status remains appropriate when Hermes proposes structured project data.

The full Draft Card mode applies when the card's primary payload is a produced textual artifact rather than a structured directory projection.

```text
Hermes proposes one contact field
!= entire Contacts Card becomes a document draft
```

This preserves the user's rule for all authored content cards without forcing document-style review onto every structured card containing one candidate field.

## 18. Permissions

Candidate permissions should separate:

```text
view draft
view sources
edit directly
comment
send revision request to Hermes
compare versions
validate content
request finalization
view archive
view chunk / index status
request new index
```

A user allowed to comment is not necessarily allowed to validate or finalize.

## 19. Audit and trace

The trace should preserve:

- original authoring request;
- source set;
- Production Brief;
- every Draft Version and hash;
- direct human patches;
- comments and anchors;
- Hermes revision requests and results;
- validation decision;
- finalization request and declared bundle;
- output artifacts;
- archive, chunk, embedding and index manifests;
- active-index changes;
- supersession and rollback decisions.

The trace need not expose hidden chain-of-thought. It records observable requests, outputs, decisions and changes.

## 20. Status model

Candidate orthogonal dimensions:

```yaml
card_authorship:
  mode: faithful_transformation | mixed | hermes_authored

card_review:
  status: not_required | required | revision_requested | under_review | accepted | rejected

card_finalization:
  status: blocked | pending | running | completed | completed_with_warnings | failed

card_publication:
  status: unsectorized | sectorization_pending | retained | superseded | archived

card_indexing:
  status: not_requested | pending | chunked | embedded | indexed | verification_failed | revoked
```

The card's visual state is derived from these dimensions but must not compress them into one ambiguous label.

## 21. Gates

### Gate A — Authorship classification

Checks:

- requested operations;
- primary-content origin;
- faithful transformation versus material authorship;
- mixed-content posture;
- editorial review requirement.

### Gate B — Draft reviewable

Checks:

- exact index and draft revision;
- full content available;
- sources and warnings visible;
- unresolved extraction or authorship failures exposed;
- comment and edit actions scoped.

### Gate C — Revision request bounded

Checks:

- exact source draft version;
- target selection or full-document scope;
- allowed context;
- forbidden changes;
- requester permission;
- no silent scope expansion.

### Gate D — Human validation

Checks:

- exact target index;
- exact Draft Version;
- exact content hash;
- unresolved blocking comments handled;
- finalization bundle displayed;
- reviewer authority.

### Gate E — Finalization authorized

Checks:

- valid human decision;
- sectorization destination;
- archive policy;
- rendering formats;
- chunking and embedding profiles;
- index scope;
- approved bindings;
- privacy and data posture;
- no unauthorized distribution.

### Gate F — Normal appearance authorized

Checks:

- validated hash matches finalized content;
- required finalization steps completed;
- archive/index warnings exposed;
- active index recorded;
- card family destination known.

## 22. Responsibility split

### Pantheon governs

Pantheon governs:

- authorship classification;
- Draft Card status;
- review requirement;
- index and version lineage;
- permissions;
- comment and revision-request scope;
- exact validation target;
- declared finalization bundle;
- sectorization, archive and index-publication gates;
- normal-appearance eligibility;
- supersession and rollback visibility.

Pantheon does not:

- write the draft;
- edit the content;
- execute comments;
- render the document;
- chunk;
- embed;
- archive bytes;
- publish the vector index;
- operate a job queue.

### Hermes executes

Hermes may:

- draft;
- revise;
- improve;
- add source-supported detail;
- enrich within allowed context;
- return diffs and warnings;
- render approved formats;
- execute authorized finalization operations through bindings;
- report progress and output manifests.

Hermes must not:

- validate its own draft;
- resolve comments without a visible result;
- alter the active finalized index silently;
- reuse an index for materially different finalized content without policy;
- invent missing detail;
- archive or index outside the declared bundle;
- mark finalization successful when required steps failed.

### Cockpit exposes

The Cockpit:

- promotes Draft Cards for review;
- shows recto summary and complete document;
- enables direct edits;
- captures comments and structured revision requests;
- displays diffs and version history;
- captures exact validation;
- confirms that finalization was sent to Hermes;
- displays real finalization progress;
- changes the card to ordinary appearance only after verified completion;
- keeps active index visible.

### Human decides

The human:

- edits or comments;
- requests improvement, details or enrichment;
- accepts or rejects revised content;
- validates one exact index/version/hash;
- authorizes the displayed finalization bundle;
- requests later modification and a new index;
- decides rollback where consequential.

## 23. Candidate API projections

Exact routes remain an external MVP decision.

Candidate reads:

```http
GET /v1/draft-cards
GET /v1/cards/{card_id}/draft
GET /v1/cards/{card_id}/draft/versions
GET /v1/cards/{card_id}/draft/comments
GET /v1/cards/{card_id}/finalization
```

Candidate bounded actions:

```http
POST /v1/cards/{card_id}/draft/comments
POST /v1/cards/{card_id}/draft/revision-requests
POST /v1/cards/{card_id}/draft/direct-patches
POST /v1/cards/{card_id}/draft/validate
POST /v1/cards/{card_id}/finalization-requests
POST /v1/cards/{card_id}/new-index-requests
```

A route does not create authority by itself.

## 24. Candidate Cockpit messages

After sending a revision request:

```text
Commentaire envoyé à Hermès.
La carte restera en brouillon jusqu'à la relecture de la nouvelle version.
```

After validation:

```text
Indice A validé.
Demande de finalisation envoyée à Hermès.
```

During finalization:

```text
Finalisation de l'indice A en cours : archivage, chunking et vectorisation.
```

After completion:

```text
Indice A finalisé et archivé.
La carte est maintenant disponible dans son apparence normale.
```

If finalization is partial:

```text
Indice A archivé, mais indexation incomplète.
La carte reste signalée jusqu'à résolution.
```

## 25. Implementation sequence

### Phase 1 — Draft overlay and full-content view

- authorship classification;
- `BROUILLON` label;
- priority surfacing;
- front summary;
- complete-content view;
- visible target index and draft revision.

### Phase 2 — Direct editing and comments

- exact anchors;
- direct human patch;
- comment creation;
- structured revision request;
- Hermes revision result;
- diff and comment resolution.

### Phase 3 — Exact validation

- content hash;
- unresolved-comment checks;
- validation decision;
- declared finalization bundle;
- `validé — finalisation en attente` state.

### Phase 4 — Finalization orchestration surface

- bounded request to Hermes;
- progress display;
- archive, chunk, embedding and index manifests;
- partial-failure handling;
- normal-appearance gate.

### Phase 5 — Later index revision

- create new target index from active index;
- concurrent active and draft display;
- supersession;
- rollback visibility;
- index-aware retrieval and download metadata.

## 26. Acceptance criteria

The candidate UX is coherent when:

1. faithful OCR/conversion alone does not trigger editorial Draft Card mode;
2. material Hermes authorship always triggers Draft Card mode for primary retained content;
3. mixed source and authored content triggers review;
4. Draft Cards are promoted above ordinary cards requiring no action;
5. the recto identifies draft state, target index and working revision;
6. the complete document is readable from the reverse or detail surface;
7. an authorized user may directly edit the draft;
8. a direct edit creates a new traceable Draft Version;
9. comments may target exact text or the full document;
10. comments can request correction, improvement, detail or enrichment from Hermes;
11. Hermes returns a new version and diff rather than overwriting silently;
12. validation targets one exact index, draft version and content hash;
13. validation displays the finalization bundle;
14. the Cockpit confirms that finalization was sent to Hermes;
15. archiving, chunking, embeddings and index publication remain observable distinct steps;
16. the card retains draft/finalizing appearance until required finalization completes;
17. the card returns to its ordinary family appearance after verified finalization;
18. the active index remains visible after finalization;
19. later modification creates a new draft index without replacing the active index;
20. previous finalized indices remain retained and traceable;
21. structured directory cards use field-level candidate review when appropriate rather than unnecessary full-document draft mode;
22. no editor, comment engine, archive service, vector runtime or Hermes Skill is implemented in Pantheon Next.

## 27. Final rule

```text
Any card whose primary retained content was materially authored by Hermes is a
Draft Card first.

Its recto identifies the draft, target index and review state.
Its reverse or details surface exposes the complete document and revision tools.
Human edits and comments produce traceable new draft versions.
Validation applies to one exact index, version and hash.
The Cockpit then sends a bounded finalization request to Hermes.
Only after the required archive, chunking, embedding and index steps are observed
as complete may the card take its ordinary retained appearance.
The active index remains visible, and later modifications create a new index
without erasing the previous one.
```
