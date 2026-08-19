# SourceDown / Docling / Hindsight qualification checkpoint

Date: 2026-08-19

Status: partial qualification record. Remote/upstream facts are qualified; real SourceDown execution in the IFJA Obsidian installation remains blocked on local host/vault access. This record does not install, activate, bind or authorize a runtime.

## Objective

Qualify the selected Obsidian-facing document path after merge of Pantheon-Next #678 without inventing a second parser pipeline or a Markdown-cleaner owner.

Target working composition:

```text
received source
-> Obsidian / SourceDown workspace surface
-> selected structural parser profile
-> final intended Markdown
-> existing one-way Hindsight synchronization
```

OCR-AI / `L3-N0X/obsidian-marker` remains a later candidate rather than an active parallel path.

## Repository state checked

At qualification start:

```text
Pantheon-Next main
= b5a39b510968ce35e48a899b4148bdfc88a71e03
= merge of #678 docs(documents): converge Obsidian Markdown derivation path

pantheon-mvp main
= ea54fdd120c8f9ac9653fdcf0ec14e5d30adbb9a
```

Recent `pantheon-mvp` changes observed after the earlier document-path inspection are Cockpit/mobile graph work and do not establish a newer document parser/normalization owner.

Existing responsibilities remain sufficient:

```text
DOCUMENT_OCR_DERIVATION_PIPELINE.md
#662 replaceable document structural-analysis qualification
pantheon-mvp DocumentConverter / ConvertedDocument
pantheon-mvp structured compilation
OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md
HERMES_CAPABILITY_BINDINGS.md
```

No new Capability Slot, normalization service or memory path is justified.

## SourceDown public-surface qualification

Current Obsidian marketplace observation on 2026-08-19:

```text
SourceDown version = 1.3.0
platform = desktop only
Obsidian minimum = 1.5+
Python minimum = 3.10+
default converter = MarkItDown
optional converters = Docling, Marker
local converter environment = private .venv outside vault
vault attachment conversion = supported from context menu
embedded images = asset folder beside generated note
duplicate import = numbered filename
```

The marketplace surface also documents converter selection/version checks as local operations and says local files are converted on the computer.

Primary public surface inspected:

```text
https://community.obsidian.md/plugins/sourcedown
```

Classification:

```text
SourceDown identity / basic documented UX = qualified
SourceDown selected IFJA workspace surface = documented working choice
SourceDown Pantheon binding                = no
```

The public material does not establish:

```text
complete DoclingDocument / JSON retention
exposure of all current Docling pipeline options
independent placement of structured JSON/assets from Markdown
reconversion semantics over an already edited generated note
```

Those remain `to_verify_local`.

## Docling current hierarchy correction

The earlier qualification discussion focused on `docling-project/docling#3633`, merged 2026-06-23, which introduced opt-in heading hierarchy based on numbering with style fallback.

Current released Docling has advanced beyond that picture.

Observed upstream commit:

```text
9cbef428c63cf42b0fada976e07dbcf62e0eab88
feat(pdf): infer heading levels from PDF bookmarks/ToC (#3688)
merged 2026-07-01
```

A direct repository comparison proves this commit is contained in tag `v2.117.0`:

```text
base = 9cbef428c...
head = v2.117.0
status = ahead
ahead_by = 101
behind_by = 0
```

Therefore current released heading inference uses, in precedence order:

```text
PDF bookmarks / embedded ToC
> numbering
> visual style
```

The #3688 implementation adds PDF outline extraction and fuzzy bookmark-to-heading matching. Partial/noisy outlines fall back to numbering/style. The commit records `use_bookmarks` defaulting true inside the hierarchy feature.

The exact `v2.117.0` `HeadingHierarchyOptions` source was also rechecked. Overall hierarchy inference remains disabled by default:

```text
HeadingHierarchyOptions.enabled = False
```

So the meaningful native comparison is:

```text
Docling v2.117 default
!=
Docling v2.117 with heading hierarchy enabled
```

When hierarchy is enabled, use the current released profile including bookmarks rather than recreating the historical #3633 numbering/style-only state unless a test explicitly needs that historical control.

Primary upstream resources inspected:

```text
https://github.com/docling-project/docling/commit/9cbef428c63cf42b0fada976e07dbcf62e0eab88
https://github.com/docling-project/docling/blob/v2.117.0/docling/datamodel/pipeline_options.py
https://github.com/docling-project/docling/blob/main/docling/models/stages/heading_hierarchy/heading_hierarchy_model.py
```

## Hindsight compatibility recheck

`vectorize-io/hindsight-obsidian` was rechecked. Latest observed release commit remains:

```text
daf529aacad14a5b8f7db9f34a7f49c9e3629b61
release(obsidian): v0.2.1
2026-08-10
```

No newer observed release changes the already-qualified one-way workspace posture.

The relevant composition remains:

```text
Obsidian Markdown source
-> designated one-way hindsight-obsidian synchronization
-> Hindsight derived bank
-> bounded read consumers
```

SourceDown, Docling and OCR-AI remain upstream producers of candidate Markdown. They do not become Hindsight authority or professional-currentness authority.

The local gate is specifically to ensure SourceDown reconversion does not accidentally create multiple intended-looking Markdown siblings that Hindsight would legitimately retain as distinct documents.

## What can and cannot be qualified from this session

Qualified remotely:

```text
SourceDown current marketplace identity/basic UX
Docling v2.117 current hierarchy feature shape
#3688 inclusion in v2.117
heading hierarchy overall disabled by default
bookmarks-first precedence when enabled
Hindsight 0.2.1 current observed release identity
existing repository ownership/boundaries
```

Not executable from this session:

```text
actual IFJA SourceDown installation
actual SourceDown private .venv converter versions
actual vault conversion output
actual SourceDown exposure of advanced Docling options
actual DoclingDocument/JSON retention by SourceDown
actual reconversion behavior over edited Markdown
actual Hindsight before/after state for that real note
```

Classification:

```text
remote/upstream qualification = complete
real SourceDown conversion     = blocked_on_local_execution
blocked_on_local_execution     != SourceDown failure
```

## Exact local test gate

Use one already-frozen private #662 control source with deep hierarchy; control F is the preferred first source.

Record before conversion:

```text
SourceDown plugin version
SourceDown selected converter profile
locally installed Docling version
source SHA-256
existing same-name Markdown state
Hindsight document-list state for the target scope
```

Then execute:

1. SourceDown default conversion;
2. SourceDown + Docling conversion with the current locally installed Docling;
3. inspect generated Markdown, frontmatter/properties, asset paths and any structured artifact;
4. determine whether SourceDown exposes `HeadingHierarchyOptions.enabled` or an equivalent advanced Docling option path;
5. re-import the exact same PDF and record duplicate behavior;
6. manually edit the generated Markdown, reconvert the same source and record overwrite/numbered-note/preservation behavior;
7. reconcile Hindsight and deterministically list the resulting note documents.

Required observations:

```text
markdown digest
heading hierarchy
reading order
table structure where present
asset-link stability
structured JSON present/absent
manual-edit survival
same-source reimport behavior
Hindsight document identity/count before and after
```

If SourceDown cannot expose the hierarchy option, record an integration limitation. Do not create a permanent second parser path merely to access that option.

## Decision posture after this checkpoint

```text
SourceDown real workspace path     = selected / local qualification pending
Docling structural analysis       = preferred candidate
Docling v2.117 native hierarchy   = current semantics qualified
Docling Agent                      = targeted fallback candidate only
OCR-AI / obsidian-marker           = later candidate
custom AI Markdown cleaner         = not justified
custom canonical renderer          = not justified before observed defects
Hindsight architecture change      = not justified
pantheon-mvp implementation change = not justified before local result
```

The upstream correction and local gate were also recorded in Pantheon-Next #662.

## Done / remaining

Done:

- current repositories rechecked;
- SourceDown public surface rechecked;
- current Docling hierarchy semantics corrected from the earlier #3633-only picture;
- inclusion of #3688 in v2.117 proven;
- Hindsight current release posture rechecked;
- exact real-vault test gate fixed;
- no duplicate owner introduced.

Remaining:

- execute the real SourceDown test on the IFJA workstation/vault;
- attach or summarize generated Markdown/assets/structured-artifact observations;
- decide whether native Docling output is already sufficiently clean;
- only then evaluate deterministic rendering or Docling Agent if a demonstrated defect remains;
- continue the broader #662 parser matrix separately.

This checkpoint does not close #662.