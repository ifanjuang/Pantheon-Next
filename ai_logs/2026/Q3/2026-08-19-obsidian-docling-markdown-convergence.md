# Obsidian / Docling Markdown convergence — qualification record

Date: 2026-08-19

Status: documentation and qualification handoff. No runtime, plugin, parser, model, binding, activation or production use is installed or authorized by this record.

## Objective

Converge the current Obsidian document-conversion discussion into existing repository owners without creating a second document pipeline, a Markdown-cleaner service, a new memory path or a new Capability Slot.

## Repository state checked

Before modification:

```text
Pantheon-Next main = beedb86eaa8af30f405a5e3ff5b8b97df87fe752
pantheon-mvp main  = ea54fdd120c8f9ac9653fdcf0ec14e5d30adbb9a
```

Relevant existing owners were checked before adding doctrine:

- `docs/governance/DOCUMENT_OCR_DERIVATION_PIPELINE.md` already owns OCR/structural-derivation placement and the MVP reconciliation gate;
- `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` already owns the one-way Obsidian Markdown -> Hindsight source path and workspace/memory boundaries;
- `docs/governance/HERMES_CAPABILITY_BINDINGS.md` already keeps Docling as the preferred `document_structural_analysis` candidate;
- Pantheon-Next #662 already owns same-corpus parser qualification;
- `pantheon-mvp/mvp_vertical/documents.py` already exposes the provider-neutral `DocumentConverter` / `ConvertedDocument` seam;
- `pantheon-mvp/mvp_vertical/structured_extraction.py` already owns deterministic structural compilation, Markdown fallback and explicit table repair/quality flags.

No new governance document was therefore justified.

A stale historical branch `agent/document-purpose-currentness` was also checked. It is diverged from current `main` and its document-currentness work has already been consolidated through later mainline work; it is not a current owner to extend.

## Current working decision

For the human Obsidian workspace path:

```text
SourceDown = selected current conversion surface for real daily use
OCR-AI / L3-N0X/obsidian-marker = later candidate to test
```

This does not make SourceDown a Pantheon binding or a source/document authority.

The public SourceDown listing observed on 2026-08-19 documents MarkItDown as default, optional Docling/Marker engines, conversion of imported or already-vaulted files, generated Markdown/source metadata/assets, numbered duplicate handling and desktop-only operation. The currently available public material did not establish complete Docling JSON retention or exposure of all current Docling pipeline options; those remain local qualification items.

OCR-AI's public repository was checked as a later comparison candidate. It documents batch conversion, mobile-compatible plugin use when the conversion endpoint is reachable, optional PDF movement, asset subfolders and smart same-folder integration. It is not activated as a second production path.

## Docling hierarchy finding

Upstream `docling-project/docling#3633` was rechecked. It was merged on 2026-06-23 and adds opt-in PDF heading-level inference. The implementation rewrites heading levels only, without adding/removing/reordering document items. Numbering is the primary signal; style is a fallback; the feature is off by default and style inference requires parsed-page data.

Consequence:

```text
native Docling hierarchy inference
must be tested before
custom downstream hierarchy repair
```

If SourceDown does not expose the relevant Docling option, that is an integration limitation to record, not justification for silently creating a permanent bypass pipeline.

## Docling Agent finding

The official `docling-project/docling-agent` repository was rechecked on 2026-08-19:

```text
package version = 0.6.0
classifier = Development Status :: 3 - Alpha
README posture = immature / work-in-progress
```

The editing agent accepts a `DoclingDocument` and can apply targeted edits. Its official `task-configs/editor.yaml` contains the structural task:

```text
Review the indentation levels of the sections and correct if necessary
```

Therefore Docling Agent is retained as a targeted fallback candidate for ambiguous structural repair, not a default pass over every document.

The use gate is:

```text
structured Docling artifact available
+ native/deterministic repair insufficient
+ traced derivative output
```

If SourceDown exposes only final Markdown and not the structured Docling artifact, do not introduce a hidden second permanent parser path solely to insert Docling Agent before that integration gap is qualified.

## Markdown-cleanup convergence

No generic AI Markdown cleaner is added.

Preferred order:

```text
SourceDown workspace surface
-> selected structural parser
-> parser-native repair
-> existing deterministic compilation/rendering seam
-> targeted Docling Agent repair only when necessary
-> final Markdown
-> existing one-way Hindsight sync
```

If a canonical human-facing renderer is demonstrated as necessary, extend the existing `pantheon-mvp` structured-compilation responsibility rather than add a separate cleaning service.

Safe deterministic cleanup is limited to presentation/structure that does not change meaning: whitespace, blank lines, stable Markdown/list/table rendering, asset/link normalization and deterministic export-noise removal with provenance preserved.

```text
format normalization != semantic correction
clean Markdown != source truth
Hindsight recall != professional currentness
```

## Hindsight result

No Hindsight doctrine change was required. `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md` already states the intended durable path:

```text
Obsidian Markdown source
-> designated synchronization/ingestion path
-> Hindsight derived bank
-> bounded read consumers
```

Hindsight remains downstream of the final Markdown and does not need to know whether SourceDown, Docling or a later OCR-AI candidate produced it.

## Modified owner

Only the existing derivation owner is extended:

```text
docs/governance/DOCUMENT_OCR_DERIVATION_PIPELINE.md
```

The workspace/Hindsight document was deliberately not modified because it already covers the needed boundary and adding SourceDown there would duplicate responsibility.

## Remaining qualification

Before implementation, use one frozen private control source from #662 and compare:

```text
A. SourceDown current/default profile
B. SourceDown with current Docling profile where selectable
C. Docling native heading hierarchy enabled where exposed
D. deterministic presentation normalization only if defects remain
E. Docling Agent targeted hierarchy repair only if ambiguity remains
F. OCR-AI later as a separate candidate
```

Record exact plugin/parser/model identities, source/config/output digests, structured JSON availability, hierarchy/reading-order/table/assets behavior, reconversion behavior around user edits and Hindsight document identity/duplicate behavior.

No runtime or binding change is justified until those observations exist.
