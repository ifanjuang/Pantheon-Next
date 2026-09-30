# Bounded source and coverage review

Read this reference when workspace sources support factual claims, when several
candidates must be compared, or when completeness or conformance is at issue.

## Source-first discipline

Inventory what is available, absent, stale, partial, unreadable or contradictory.
Memory and retrieval provide leads; consequential claims require an exact source
and useful locator opened through an admitted route.

## Bounded Docling reading

For long PDFs, tables or specifications, use Docling progressively:

```text
convert when needed
-> overview of anchors
-> targeted text search
-> smallest relevant anchor reads
```

Do not export an entire Docling document to Markdown for source review. Large
exports can spill to a runtime file that the governed profile cannot and should
not reopen through `terminal` or generic file access. If a result is reported as
persisted or spilled over, stay on the Docling route and repeat the request with
targeted searches and bounded anchor reads. Process one consequential document
at a time and keep only the extracts needed for the coverage matrix.

## OCR retention boundary

A Docling conversion or OCR result is temporary analysis material by default;
it is not a replacement for the source PDF and is not durable merely because
Hindsight can recall extracted content.

Before proposing any persistent OCR output, list every selected source with its
exact relative path, file type, page count when observed, OCR need or result,
and any existing target-name collision. Do not write while building this list.
Then ask once for the retention policy, with these five choices:

1. keep the OCR result only in the current session and write no project file —
   default when durable reuse was not requested;
2. update the searchable content of each corresponding existing Hindsight
   document through the single designated producer, without creating a project
   file — recommended for internal search;
3. create one adjacent Markdown sidecar for every listed source;
4. create one additional searchable `.ocr.pdf` beside every listed PDF while
   preserving each original — recommended when page appearance matters;
5. decide file by file, where in-place PDF replacement may be selected
   explicitly for an individual file.

Show the proposed output name for every file before execution. An in-place
replacement is never the default and never a batch action. It requires an
explicit per-file choice and a bounded writer that creates a recoverable backup,
preserves relevant metadata, verifies page count and rendered readability, and
reports both backup and final paths. A collision with an existing sidecar or OCR
PDF requires a fresh choice; do not overwrite it silently.

Use the reserved sibling names `<stem>.ocr.md` and `<stem>.ocr.pdf`. Treat the
original and these derivatives as one logical document family in inventories,
search and coverage counts. Show one result with its available representations;
never count a derivative as another quote, letter, contract or revision.
Hindsight must retain only one searchable representation for the family. A
Hindsight-only OCR update reuses the existing `<document_id>:source`; the single
producer replaces its searchable content while preserving the original PDF path
and identity in metadata. When project-file derivatives exist, use this
preference order: OCR Markdown, searchable OCR PDF, original. A normal
`<stem>.md` without the `.ocr` marker remains an independent authored document
and is not merged automatically.

The producer owns durable OCR state and re-emits it on every reconciliation so
ordinary source reconciliation cannot erase it. Use low-cardinality tags:

```text
ocr:status:needed | completed | stale | failed
ocr:representation:hindsight-text | markdown | searchable-pdf | in-place-pdf
```

Keep detailed provenance in document metadata, not high-cardinality tags:
`ocr_source_sha256`, `ocr_engine`, `ocr_pipeline_version`, `ocr_completed_at`
and, when relevant, `ocr_output_path`. Hermes skips OCR only when status is
`completed`, the recorded `ocr_source_sha256` equals the current PDF checksum,
and the selected searchable representation is still available. A changed PDF
becomes `stale`; an absent or failed representation becomes `needed`. Re-run an
otherwise current OCR only after an explicit user request recorded as
`force_ocr=true` for that operation.

The current governed source tools are read-only and cannot persist a file or an
OCR update. The future bounded retention route must address one already resolved
document through the designated producer; Hermes must not receive arbitrary
bank-write access. Once an authorized writer creates a project file, Hindsight
may index it only after reconciliation is observed.

```text
OCR result != source PDF replaced
Hindsight memory != document storage
file written != Hindsight reconciliation observed
batch retention choice != in-place replacement authority
three representations != three documents
same Hindsight document id != duplicate document
ocr:status:completed alone != current OCR proven
```

## Bounded delegated source review

Use `delegate_task` only for an independent, bounded source question that would
otherwise flood parent context. Begin with one child at a time. The parent owns
clarification, synthesis and verification.

Give the child only the needed toolsets:

```text
mcp-ifja-vault-read
mcp-hindsight-kroqi-project
mcp-docling — only after the parent supplies an exact bounded document list
```

Do not give browser, terminal, generic file access, writing, messaging, memory,
Kanban, clarification, unrelated MCPs or further delegation. Provide the
referent, question, admitted scope, language and stop condition. Require structured:

```text
observed_facts
exact_sources_and_locators
contradictions
missing_or_unreadable_material
limits
```

The parent reopens material supporting passages. It may make one corrective
request with the same scope; then it surfaces the gap.

```text
subagent result != source verification
scope gap != permission to broaden sources
```

## Reference-first coverage matrix

Before comparing candidates, normalize perimeter, inclusions, exclusions,
variants, tax basis, date and completeness. Build the coverage matrix from the
reference first, never from candidates found. Give every material reference
line or package exactly one state:

```text
matched_comparable
matched_scope_difference
combined_with_other_scope
alternative_or_variant
missing_candidate
unreadable_or_unverified
not_applicable_with_reason
```

Do not omit an unmatched reference item. A filename, directory or candidate
label does not prove scope coverage; verify material description and amount.
Report matched, missing and unresolved coverage separately.

Never compare a partial aggregate with a broader reference total. Overall
conformance requires complete material coverage or an explicit user-approved
exclusion. Otherwise state only item-level findings and `ready_with_limits`.
