# Pantheon Cockpit — Knowledge Navigation UX

Status: candidate support specification — documented non-implemented.
Boundary profile: candidate_support_note.

This document specializes the Cockpit and Card Stack candidates for navigation inside the `Knowledge` tab.

It connects:

- `PANTHEON_COCKPIT_UX_SPEC.md`;
- `CARD_STACK_MODEL.md`;
- `DOCUMENT_LIFECYCLE_GOVERNANCE.md`;
- `DOCUMENT_PRODUCTION_LIFECYCLE.md`;
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`.

It defines a product and visual contract only. It does not implement a frontend, component library, file browser, database schema, source store, drag-and-drop runtime, upload API, ingestion pipeline, Hermes Skill, search engine, authorization service, archive service or physical directory structure.

```text
Knowledge folders organize navigation.
Knowledge cards expose reusable items.
Source files remain preserved objects.
Hermes may process sources externally.
Pantheon governs classification, status and consequential transitions.
```

## 1. Decision

The Cockpit `Knowledge` tab should allow the user to:

- create folders;
- create nested subfolders;
- navigate through the hierarchy;
- deposit one or more files into a selected folder;
- create Knowledge items from those files;
- display each resulting Knowledge item as a card;
- search across the current folder, descendants or all Knowledge;
- move or link items between folders without duplicating source bytes;
- display processing, review and publication states;
- download the original source when authorized.

The principal visual distinction is:

```text
Knowledge folder
= card-shaped navigation container with a gradient-filled background

Knowledge item
= neutral or surface-colored card with a thick gradient outline only
```

The distinction must remain visible in light mode, dark mode, mobile and reduced-motion contexts.

## 2. Folder is a navigation object, not a source object

The Cockpit may use the familiar word `folder` in the interface.

The underlying concept should remain a logical Knowledge navigation container or collection, not a required NAS or filesystem directory.

```text
Cockpit folder
!= physical directory
Cockpit move
!= source-byte relocation
folder membership
!= source ownership
folder deletion
!= source deletion
```

A folder organizes how Knowledge is found and presented.

It does not become:

- the source of truth for file storage;
- a project phase;
- a Knowledge Item;
- Evidence;
- a permission bypass;
- an installation or execution boundary.

Candidate conceptual object:

```yaml
knowledge_folder:
  folder_id:
  parent_folder_id:
  title:
  description:
  icon:
  sort_order:
  visibility_scope:
  archived_at:
  created_by:
  created_at:
  updated_at:
```

The folder tree should use a single parent per folder for predictable navigation.

Cycles are forbidden.

```text
folder A -> folder B -> folder A
= invalid
```

A Knowledge Item may be linked to more than one folder when reuse justifies it.

That relation should not duplicate the original source or the Knowledge Item identity.

```yaml
knowledge_folder_item_link:
  link_id:
  folder_id:
  knowledge_id:
  is_primary:
  linked_by:
  linked_at:
```

## 3. Hierarchy and depth

The Knowledge tab supports folders and subfolders.

No fixed universal depth is required by doctrine, but the product should discourage excessive nesting.

Recommended default UX posture:

```text
Level 0 — Knowledge root
Level 1 — broad family or cabinet category
Level 2 — subject or practice area
Level 3 — specialized collection when useful
```

Deeper levels may remain technically possible, but the Cockpit should warn when hierarchy becomes harder to navigate than tags, search or cross-links.

The five architecture-domain families may remain available as default first-level folders:

```text
Référentiels
Responsabilité
Méthodologie
Techniques
Réglementations
```

They are defaults, not an exclusive or immutable taxonomy.

Users with the relevant rights may create other folders and nested subfolders.

```text
no mandatory subfolder structure
!= no user-created subfolders
```

The earlier rule against mandatory subfolders means that Pantheon does not impose a deep universal filesystem taxonomy. It does not forbid a configurable logical hierarchy in the Cockpit.

## 4. Primary navigation pattern

The Knowledge tab should expose:

```text
Knowledge
├── breadcrumb
├── current-folder title and description
├── search and filters
├── primary actions
├── folder cards
└── Knowledge item cards
```

Recommended primary actions:

```text
New folder
Upload files
Add URL
Create Knowledge note
Produce a document
Sort
Filter
Switch grid / list
```

The primary surface should remain understandable without exposing OCR, embeddings, vector stores, provider details or runtime internals.

Technical details belong in a secondary detail panel or technical administration mode.

## 5. Breadcrumb

Nested navigation requires a persistent breadcrumb.

Example:

```text
Knowledge / Réglementations / Urbanisme / PLU et PLUi
```

Breadcrumb behavior:

- every ancestor is clickable;
- the current folder is clearly identified;
- long paths collapse responsively;
- mobile may show the parent and an expandable full path;
- search results retain the source folder path;
- moving an item shows both current and target paths before confirmation.

The breadcrumb displays navigation context. It does not change permissions or source provenance.

## 6. Folder card visual contract

A folder appears as a card-shaped navigation object with a gradient-filled surface.

### 6.1 Required visual properties

```text
background       = full gradient fill
border           = optional subtle inner or outer separator
shape            = same general radius family as Knowledge cards
icon             = folder or collection icon
text             = high-contrast over the gradient
content emphasis = folder title, item count and navigation cue
```

Recommended visible fields:

- folder title;
- optional short description;
- number of direct subfolders;
- number of direct Knowledge items;
- optional total descendant count;
- visibility or restriction indicator when material;
- archived or special status when material.

Example content hierarchy:

```text
[folder icon]
Réglementations
18 sous-dossiers · 246 cartes
```

### 6.2 Interaction states

Default:

```text
full gradient fill
high-contrast text
clear folder icon
```

Hover or pointer focus:

```text
slight elevation or light shift
visible navigation cue
no geometry jump
```

Keyboard focus:

```text
strong external focus ring
not represented only by a gradient change
```

Selected:

```text
persistent selection marker
optional check indicator
selection must remain distinct from hover
```

Drag target:

```text
folder accepts drop
strong but non-destructive target state
folder title and destination path remain visible
```

Restricted:

```text
lock or scope badge
no misleading drag target
```

Archived:

```text
desaturated or visually reduced treatment
explicit Archived label
```

### 6.3 Gradient discipline

The gradient communicates `container / navigation` rather than truth, approval, quality or risk.

```text
gradient fill != approved
gradient fill != active binding
gradient fill != high confidence
gradient fill != Evidence
```

The folder gradient should derive from a controlled Cockpit token rather than an arbitrary gradient per folder.

Optional category variation may use approved token families, but should not make folders look like status indicators.

## 7. Knowledge item card visual contract

A Knowledge Item appears as a neutral card with a thick gradient outline.

### 7.1 Required visual properties

```text
background       = neutral Cockpit surface
border           = thick gradient outline
interior fill    = no gradient fill
shape            = same radius family as folders
content emphasis = title, summary, type, status and provenance
```

The thick outline distinguishes an item from a folder while maintaining one visual family.

Recommended border thickness:

```text
desktop = visually strong, approximately 3 to 5 CSS pixels
mobile  = visually strong without consuming excessive card width
```

The exact implementation may use:

- a gradient border image;
- a pseudo-element mask;
- a wrapped gradient layer;
- another accessible and performant technique.

The visual contract is more important than one CSS mechanism.

### 7.2 Recommended card fields

Primary information:

- title;
- document or Knowledge type;
- short summary;
- primary folder;
- source count;
- updated date;
- owner or responsible scope when relevant.

Status information when material:

- processing;
- review required;
- ready;
- warning;
- failed;
- superseded;
- archived;
- restricted source;
- original download available.

Secondary actions:

```text
Open
View sources
Download original
Move or link
Edit metadata
Request reprocessing
Archive
```

Actions must be permission- and state-aware.

### 7.3 Card type variants

The outline remains the primary item signature across variants.

Possible card variants:

```text
Source-backed Knowledge card
Multi-source Knowledge card
Knowledge note card
Generated document card
Template or guide card
Reference card
```

Additional icons or badges may distinguish variants, but should not replace the folder-fill versus item-outline rule.

## 8. Folder and item coexistence

The current folder may show folders and Knowledge cards in the same grid.

Recommended order:

```text
1. folders and subfolders
2. pinned Knowledge cards
3. remaining Knowledge cards
```

Alternative list view may interleave by sort criteria, but object type must remain unmistakable.

The user should never have to infer object type from title wording alone.

```text
folder = filled gradient container
item   = thick gradient outline
```

Folder and item cards should share:

- card radius;
- spacing rhythm;
- typography family;
- hover timing;
- focus behavior;
- responsive grid behavior.

They should differ in:

- fill treatment;
- iconography;
- navigation behavior;
- available actions;
- metadata density.

## 9. File deposit flow

Dropping a file into a Knowledge folder does not immediately convert the file into approved Knowledge.

The interaction captures a requested Knowledge destination.

```text
file drop into folder
-> Source Capture
-> Intake Item
-> requested Knowledge folder
-> external processing when required
-> Knowledge card candidate or Knowledge item
-> visible processing and review state
```

The original remains preserved and downloadable when authorized.

The card is a projection of the resulting Knowledge Item or intake state. It is not the source binary itself.

### 9.1 Immediate UX feedback

After drop, the Cockpit should create a visible provisional card or intake placeholder in the target folder.

Example:

```text
Rapport structure.pdf
Import reçu
Analyse en attente
```

As Hermes exposes progress, the card may update:

```text
Source capturée
Contexte compris
Extraction en cours — 18 / 42 pages
Résumé en attente
```

The Cockpit must not fabricate a percentage.

### 9.2 Completion states

Candidate item states:

```text
uploading
source_captured
processing
processing_with_warnings
review_required
ready
failed
archived
```

These should be mapped to orthogonal lifecycle axes in implementation rather than compressed into one universal status field.

### 9.3 Batch deposit

A user may deposit several files.

The Cockpit should show:

- one batch summary;
- one individual card or placeholder per source;
- individual failures;
- individual warnings;
- target folder;
- duplicate detection candidates;
- no silent merge.

```text
same filename != same source
same hash = duplicate candidate, not automatic merge
```

## 10. URL and connector deposit

The same target-folder experience should apply to:

- URL capture;
- email attachment;
- Drive file;
- repository file;
- NAS reference;
- approved connector source.

The interface may use `Add source` rather than `Upload file` as the broader action label.

A URL card should retain:

- original URL;
- capture date;
- captured content hash;
- archived source capture when policy allows;
- retrieval and access posture.

## 11. Produced documents

A document produced from notes, scan, voice or supplied text may be visible in a drafting or review surface before it is placed in Knowledge.

The production rule remains:

```text
generated draft
-> human review of exact version
-> sectorization into Knowledge folder
-> archive when authorized
```

A generated document must not appear as a finalized Knowledge card merely because Hermes completed drafting or rendering.

Before review, it may appear as:

- a draft card in a dedicated draft area;
- a provisional card marked `Review required`;
- a review item linked to the intended folder but not yet admitted to it.

After review and sectorization, the exact reviewed version becomes the Knowledge card version.

```text
reviewed version 2
!= later version 3 automatically reviewed
```

## 12. Create folder

The `New folder` action should request only the minimum useful information:

- title;
- optional description;
- parent folder;
- visibility scope when different from the parent;
- optional icon or approved visual token.

Default behavior:

- inherit parent visibility where policy allows;
- place the new folder at the end or according to current sort;
- focus the new folder card after creation;
- allow immediate rename;
- record creator and date.

Creating a folder is a reversible organizational action when it changes no access rights or external system.

Changing visibility, inheritance or protected scope may require a stronger gate.

## 13. Rename, move and link

### 13.1 Rename folder

Renaming changes the navigation label.

It does not rewrite source files, project phases or source hashes.

### 13.2 Move folder

Moving a folder changes its parent relation.

Before moving, the system should check:

- no cycle is created;
- visibility inheritance remains coherent;
- descendants remain accessible as intended;
- references and bookmarks can resolve through stable IDs;
- the move is reversible.

### 13.3 Move Knowledge item

Moving a Knowledge item may mean:

- change primary folder;
- remove one folder link and add another;
- preserve other folder links;
- preserve source identity and Knowledge identity.

### 13.4 Link Knowledge item

The user may add an existing Knowledge Item to another folder without duplicating it.

The UI should distinguish:

```text
Move
= change organizational placement

Add to another folder
= create an additional navigation link
```

## 14. Delete and archive behavior

The user-facing word `Delete` should be used cautiously.

Recommended distinction:

```text
Remove from folder
Archive folder
Archive Knowledge item
Delete source capture
```

These are not equivalent.

Removing a card from a folder removes a navigation relation only when the item remains linked elsewhere or accessible through search.

Archiving a folder should not silently archive all contained Knowledge Items.

Possible archive flow:

```text
archive folder
-> folder hidden from normal navigation
-> descendant items remain governed objects
-> user resolves whether descendants move, remain linked or become archived separately
```

Deleting original source bytes is a separate retention decision and must not be triggered by folder deletion.

## 15. Search and filters

Search scopes:

```text
Current folder
Current folder and descendants
All Knowledge
Selected folders
```

Filters may include:

- source type;
- Knowledge type;
- date;
- status;
- project origin;
- source access;
- review state;
- author or organization;
- tags;
- language.

Search results should show:

- card title;
- short summary;
- folder path or paths;
- source provenance;
- status;
- original access posture.

A search result may open the card in context or reveal its folder path.

## 16. Grid and list views

### Grid view

Preferred for visual browsing.

- folder gradient fill is prominent;
- item gradient outline is prominent;
- summaries are concise;
- responsive columns adapt to viewport.

### List view

Preferred for dense review and sorting.

- object-type icon remains visible;
- folder rows retain a contained gradient marker or filled leading block;
- item rows retain a gradient outline marker or thick leading border;
- metadata columns may be compared;
- visual meaning remains consistent with grid view.

## 17. Mobile behavior

On mobile:

- use one-column or compact two-column layout depending on width;
- keep folder gradient fill and item outline distinction;
- avoid reducing the outline until it becomes visually ambiguous;
- expose primary action through a compact menu;
- keep breadcrumb understandable;
- support long-press or menu actions rather than hover-only controls;
- preserve keyboard and assistive technology semantics where available.

Drag-and-drop is optional on mobile. File selection and target-folder confirmation remain required alternatives.

## 18. Accessibility

Gradient treatment must not be the only distinction.

Folder cards also require:

- folder icon;
- semantic label;
- accessible role and name;
- navigation affordance.

Knowledge cards also require:

- item-type icon or text;
- accessible status label;
- explicit source and action labels.

Requirements:

- sufficient contrast for folder text over gradients;
- visible keyboard focus;
- non-color status indicators;
- meaningful screen-reader names;
- reduced-motion compliance;
- no essential action hidden behind hover only;
- status not encoded solely by border color.

## 19. Status color separation

The folder/item gradient is an object-family treatment.

Status must use a separate and restrained system:

```text
neutral information
processing
warning
review required
failure
ready
archived
restricted
```

Status badges should not replace the object-family visual contract.

```text
filled gradient = folder
outlined gradient = Knowledge item
badge/icon/text = lifecycle or access status
```

This prevents a folder from looking `approved` merely because it is filled with a gradient.

## 20. Permissions

Folder visibility and Knowledge item access may differ from source access.

```text
folder visible
!= every source downloadable
Knowledge card visible
!= confidential project source visible
```

The Cockpit should display:

- whether the card is visible;
- whether source detail is visible;
- whether original download is allowed;
- why an action is restricted.

Folder hierarchy must not allow users to bypass project or source permissions by linking an item into a broader folder.

## 21. Empty states

Knowledge root empty state:

```text
Create a folder
Upload files
Add a URL
Create a Knowledge note
```

Folder empty state:

```text
This folder is empty.
Drop files here, create a subfolder or link existing Knowledge.
```

Search empty state:

```text
No result in this scope.
Search descendants or all Knowledge.
```

Processing empty state should not be confused with `no content` when processing is still running.

## 22. Candidate component inventory

```text
KnowledgeTab
KnowledgeBreadcrumb
KnowledgeToolbar
KnowledgeGrid
KnowledgeList
KnowledgeFolderCard
KnowledgeItemCard
KnowledgeIntakePlaceholderCard
KnowledgeStatusBadge
KnowledgeSourceBadge
KnowledgeFolderDialog
KnowledgeMoveDialog
KnowledgeLinkDialog
KnowledgeDropZone
KnowledgeDetailsPanel
KnowledgeSourcePanel
KnowledgeReviewPanel
```

These names are implementation candidates only. They do not establish a mandatory frontend framework.

## 23. Cockpit actions

The principal Knowledge-tab actions remain simple:

```text
Navigate
Search
Open
Create folder
Create subfolder
Upload or add source
Move
Add to another folder
View source
Download original
Request processing
Review
Archive
```

The user should not need to choose:

- OCR engine;
- embedding model;
- vector dimension;
- runtime provider;
- queue;
- internal Skill route.

Those are execution and administration concerns.

## 24. Responsibility split

### Cockpit

- displays folder and card navigation;
- captures folder creation, upload target, move, link and archive intent;
- displays processing and review state;
- displays source access and original download action;
- captures explicit human decisions where required.

### Pantheon

- governs folder identity and scope;
- governs Knowledge classification and publication state;
- prevents permission bypass and destructive ambiguity;
- records review, archive and source-access consequences;
- qualifies external runtime progress.

### Hermes

- may interpret, extract, summarize, chunk, embed or draft through separately reviewed capabilities;
- reports real progress and outputs;
- does not decide folder authority, source access, final publication or archive by itself.

### Human

- chooses organizational structure within permissions;
- reviews produced documents before sectorization and archive;
- resolves destructive or consequential changes;
- confirms where policy requires a human decision.

## 25. Capability Slot projection

```yaml
capability_slot: knowledge_navigation_and_card_projection
abstract_function: >-
  expose general Knowledge through a nested logical folder hierarchy and a
  card-based surface that preserves source, item, status, permission and review
  distinctions without becoming a filesystem or processing runtime.
candidate_binding:
  product_surface: Pantheon Cockpit
  execution_support: Hermes where processing is requested
implementation_status: documented non-implemented in Pantheon Next
external_candidate_status: to verify in pantheon-mvp
activation_status: not authorized by this document
pantheon_gates:
  - folder hierarchy valid
  - permissions preserved
  - source capture retained
  - generated document reviewed before sectorization
  - archive consequence explicit
```

## 26. Acceptance criteria

The UX candidate is coherent when:

1. the Knowledge tab can show a root, folders and nested subfolders;
2. users with rights can create and rename folders;
3. folder hierarchy is logical and not coupled to physical source storage;
4. a folder has one parent and cycles are rejected;
5. a Knowledge Item can appear in more than one folder without source duplication;
6. files dropped into a folder create visible intake or Knowledge cards;
7. original source download remains available when authorized;
8. folder cards use a gradient-filled background;
9. Knowledge item cards use a thick gradient outline and no gradient fill;
10. icons and labels preserve the distinction without relying only on color;
11. progress is shown only from real executor observations;
12. generated documents remain review-blocked before Knowledge sectorization and archive;
13. folder deletion does not silently delete sources or Knowledge Items;
14. moving or linking preserves stable item and source identity;
15. search can operate in current folder, descendants or all Knowledge;
16. mobile and accessibility behavior preserve the folder/item distinction;
17. the Cockpit remains an exposure and decision-capture surface rather than a processing runtime.

## 27. Final rule

```text
Folders organize the Knowledge navigation tree.
Cards represent Knowledge items and their governed state.
A full gradient fill identifies a folder.
A thick gradient outline identifies a Knowledge item.
Files remain preserved sources behind the cards.
Generated documents require review before they enter the folder hierarchy as retained Knowledge.
```
