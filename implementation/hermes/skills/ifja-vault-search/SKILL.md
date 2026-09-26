---
name: ifja-vault-search
description: "Recherche les projets et documents dans les vaults IFJA."
license: MIT
metadata:
  version: 0.8.1
  author: IFJA
  hermes:
    tags: [ifja, hindsight, vaults, projects, documents]
    category: productivity
    depends_on: [ifja-project-context]
    related_skills: [ifja-project-context]
---

# IFJA vault search

Organization adapter for the generic `ifja-project-context` method. Apply that
skill's project-resolution, document-inspection and Pantheon boundaries first.
This adapter supplies current IFJA bindings and search tactics; it creates no
project identity, truth, Evidence, approval, governed memory or authorization.

Read [references/organization-profile.yaml](references/organization-profile.yaml)
before choosing a source or tool. Treat it as volatile deployment configuration,
not Pantheon doctrine.

## When to Use

- General or transversal question: search the relevant professional source
  without selecting a project.
- Multi-project question: keep all requested projects in scope and preserve
  their identities separately.
- Situated question with a known project: retain the conversation-local project
  and search only its bounded source scope.
- Situated question with an informal designation: build a bounded candidate set
  from a first name, client, official name, street, commune, code, description
  or distinctive subject.

Ask one targeted question only when choosing between candidates would materially
change the answer, permitted action or consequence.

## Search order

0. For every project, dossier, client, document or professional-workspace
   request, start with one fast Hindsight/Mnemosyne lookup. Emit at most one
   interim `indice mémoire — non confirmé` when it materially helps locate the
   dossier, then continue to the applicable Hindsight source. A known local
   path does not bypass this first check. Do not repeat an identical Mnemosyne
   query; a second recall is reserved for an observed freshness/synchronization
   concern and must use a distinct bounded query.
1. Use the applicable Hindsight source (AFFAIRES for situated work,
   DOCUMENTAIRES for transversal professional material) to resolve the exact
   project or document identity. For a semantic project/document question,
   issue one targeted `recall` against AFFAIRES first; use `list_documents`
   only for an explicit inventory/path request. If recall returns no usable
   candidate, use one targeted `search_knowledge_base` keyword query before the
   bounded `list_documents` fallback. For an exact name, alias, path or
   inventory question, listing/get is sufficient.
   When the configured MCP binding and function schema are already present in
   the active profile, invoke that function directly. Do not repeat Tool Search
   or Tool Describe calls for every step; use at most one schema inspection when
   the required argument shape is genuinely unknown.
2. Resolve the project page or exact source identity. A high-ranked semantic
   result does not select a project, and a failed first recall does not establish
   that the source is absent until the targeted keyword search and bounded
   AFFAIRES inventory fallback have also been attempted.
   For a document-family query, normalize the project/document terms and include
   the relevant filename tokens and professional aliases in the bounded search
   (for example, a CCTP may also be labelled CCAP, DCE or cahier des charges).
   Rank candidates by exact document-family match first, then project-name
   match, then revision/path evidence. Preserve candidates separately; a permit,
   estimate or plan is not a CCTP merely because it shares the project name.
   Never promote a lower-ranked document when an exact family match is absent;
   report the candidate set and the missing type instead.
3. Open the exact project page or requested document before returning a material
   identifier, date, status or contractual fact.

### Latest document / revision resolution

When the user asks for the latest, current, newest or applicable revision of a
document family, do not use Hindsight relevance rank, retain time, filesystem
mtime, upload time or a cartouche date/index as proof of currentness.

Resolve at most five exact-family candidates. Preserve any validated Workspace
revision projection carried by the candidate:

```text
revision_mode = supersedes | supplements
revision_of   = document_id
```

A structurally resolved explicit `supersedes` relation is a declared lineage edge,
not proof that the declaration is professionally correct. A `supplements` relation
is not replacement and must not suppress the referenced document. Never manufacture
either relation from index/date/name similarity.

Then inspect each candidate with Hindsight `get_document` so the retained
`original_text` is available. Extract from the document content itself, when
explicitly stated:

```text
source_revision
source_document_date
source_revision_history[]
source_supersedes[]
```

Treat these as source observations, not metadata truth. Do not invent a revision
or date when the source text does not state one.

Selection order for one exact document family:

```text
structurally resolved explicit Workspace supersedes relation
> explicit supersedes/replaces statement in the source
> explicit coherent revision history/table in the source
> heuristic ordering by comparable source revision/index
> source document date as heuristic tie-breaker/fallback
```

Rules:

- If the validated explicit `supersedes` graph has one unambiguous head, that
  head is the current retrieval candidate. If it has multiple heads, cycles or
  unresolved targets, return the conflict instead of choosing silently.
- If one source explicitly says it supersedes/replaces another candidate, prefer
  the superseding source for this retrieval, but do not automatically write a
  cartouche revision relation from that observation.
- If a source contains an explicit revision history/table, use it to validate the
  current revision token and chronology. A coherent revision history is stronger
  evidence than an isolated date field.
- Comparable isolated revisions (for example A/B/C, 01/02/03, P1/P2/P3,
  REV01/REV02) may order candidates for retrieval convenience, but they do not by
  themselves establish professional currentness or create a revision relation.
- The source document date is a consistency check, not an automatic override.
- If the higher isolated revision carries an earlier source date than the lower
  revision, keep it first only as the index-ranked candidate and emit
  `revision_date_conflict`; keep the other candidate visible.
- If two candidates have the same revision/index, the later explicit source date
  may order them for retrieval, but emit `duplicate_revision`. If their dates
  are also equal or missing, do not silently collapse them.
- If revisions are missing or not safely comparable, an explicit source date may
  order candidates only as `date_fallback`. Do not derive chronology from
  filename ordering or filesystem timestamps.
- If no explicit lineage/source chronology resolves the candidates, return the
  ordered candidate set and state that currentness is unresolved. The first item
  is a retrieval preference, not a professional-currentness assertion.

A "latest" answer should expose the basis used:

```text
selection_basis =
  workspace_supersedes
  | source_supersession
  | source_revision_history
  | heuristic_revision_order
  | date_fallback
  | ambiguous

revision_conflict =
  none
  | duplicate_revision
  | revision_date_conflict
  | incomparable_revision
  | branching_lineage
  | invalid_lineage
```

The cartouche may help locate the family and may carry an explicit declared
revision relation, but its descriptive `index` and `document_date` cannot
silently establish currentness.


   If Hindsight returns no exact candidate but an admitted Workspace/vault path
   or filename is already known, treat this as an indexing gap: validate and
   open that exact local source (Docling for a file needing extraction) rather
   than asking for an upload or declaring the document absent. Distinguish
   `binding_unavailable`, `no_match` and `indexing_gap` in the limitation.
4. Use one targeted recall when the request is conceptual, associative or the
   exact source remains unknown.
5. For a recent project or information possibly awaiting synchronization, use
   the second and final recall against the configured conversation-memory
   binding only when a freshness/synchronization concern is explicitly observed
   and the distinct query can change the result. Never repeat Mnemosyne after an
   exact AFFAIRES document has already been opened merely to enrich the answer.
   Attribute memory-only information to recent conversation and mark it
   unconfirmed until an admitted business source supports it.

For a material professional factual answer, the applicable source lookup is
mandatory before final synthesis: `AFFAIRES` for dossier facts,
`DOCUMENTAIRES` for transversal professional facts, and both for a mixed
question. A memory lead never satisfies this requirement. If the required
binding is unavailable, return the limitation rather than substituting model
recall.

Never report that Hindsight is unavailable solely because a recall or search
returned no match. Availability is established by the active MCP catalogue and
connectivity test; an empty result is a search outcome and may indicate an
indexing gap or an overly narrow query.

Do not turn a generic remembered checklist into a regulatory conclusion. Each
technical, legal, contractual or standards requirement must be tied to an exact
document or section returned by the admitted source path, or be labelled
`à vérifier` with the missing reference stated.

```text
subject match != selected project
recall snippet != exact document
conversation memory != business source
fast memory lead != confirmed answer
document opened != Evidence admitted
```

## Source routing

- Use `AFFAIRES` for project records, clients, contracts, correspondence,
  permits, plans, schedules and administrative material.
- Use `DOCUMENTAIRES` for transversal technical, regulatory, legal, contractual
  and professional references.
- Use both when a project-specific fact must be tested against a transversal
  rule. Keep their contributions distinguishable.
- For a mixed document/compliance question, open the exact AFFAIRES document
  first, then issue one targeted DOCUMENTAIRES recall for the rule families
  needed to test the observed content. Do not list the entire DOCUMENTAIRES
  bank before the project source is identified.
- Once a technical or regulatory comparison is requested, a targeted
  DOCUMENTAIRES recall and the relevant page/document must be opened before
  presenting normative gaps. If no applicable reference is found, label the
  item `à vérifier` rather than implying that the standard was consulted.
- After the exact document is open, search DOCUMENTAIRES for only the
  standards, regulations, contractual clauses or professional references that
  correspond to observed gaps. Open the relevant knowledge pages and cite them
  separately from the project document; do not present a generic catalogue as a
  finding.
- Use the live source only when the user requests current state or indicates a
  change may not yet be indexed. Do not silently merge live and indexed state.

## Documents and plans

Apply the generic document-inspection reference. A Markdown derivative or recall
mention does not prove that a PDF exists or that its relevant visual content was
inspected. Use the configured document-analysis binding only for the exact
sources and pages needed. Preserve source identity and locator.

### Docling tool routing

When the requested answer depends on the content of a PDF, DOCX, PPTX, XLSX or
image, use the configured Docling MCP binding through this bounded sequence:

```text
exact source path or URL
-> is_document_in_local_cache(document_key) when a document_key is already known
-> convert_document_into_docling_document(source) when conversion is needed
-> get_overview_of_document_anchors(document_key)
-> search_for_text_in_document_anchors(...) when a term or section is targeted
-> get_text_of_document_item_at_anchor(...) for the smallest relevant extract
```

For Hermes MCP calls, the conversion argument is exactly `source`:

```json
{"source": "/srv/pantheon/obsidian-documentaires/<document>.pdf"}
```

Do not call `get_prompt`, `list_prompts`, `read_resource` or `list_resources` as
a substitute for document conversion or content inspection. Those are MCP
introspection/resource operations and do not open an arbitrary local PDF. Do
not invent `filepath` or `file_path` for the Hermes conversion wrapper; if the
selected binding exposes a different schema, inspect that schema before calling
it rather than guessing.

The same rule applies to Hindsight resource/introspection calls: use
`get_document` for an identified document and `get_knowledge_page` for an
identified knowledge page. A `read_resource` result is not a document
consultation and must not be cited as one.

The `source` path is resolved by the Docling service, not by the model. Use a
path shared with that service, such as the reviewed `/srv/pantheon/obsidian`,
`/srv/pantheon/obsidian-affaires` or `/srv/pantheon/obsidian-documentaires`
mounts. A WebUI upload path under `/home/hermeswebui/.hermes/webui/attachments`
is not assumed to be visible there. If no shared path or URL exists, report a
Capability Gap and request a supported source location; do not retry the same
conversion with guessed paths.

Opening `http://127.0.0.1:8020/mcp` in a browser is not a document test. It is a
machine-to-machine MCP endpoint and requires an MCP request body. Validate the
binding with Hermes MCP diagnostics, then invoke the document tool with its
required arguments.

### Workspace files

An attached file shown by Hermes WebUI is a candidate input, not automatically
a Docling-visible path. Before conversion, resolve the attachment to one of
 these forms:

```text
shared Workspace/vault path visible to Docling
or
supported URL reachable by Docling
```

The current local deployment shares the `/srv/pantheon/obsidian*` roots with
Docling. A virtual UI label such as `/workspace`, or an attachment path under
`/home/hermeswebui/.hermes/webui/attachments`, must not be guessed or passed to
Docling unless the deployment explicitly mounts it there. If the attachment is
not shared, report `source_not_visible_to_docling` and ask for a Workspace/vault
path or an explicit upload-to-shared-workspace step. Do not silently copy a
private attachment into a professional vault, and do not retry with another
invented path.

## Limits and return

- At most two recall calls across all bindings for one question.
- For a single professional lookup, use at most one Mnemosyne recall, one
  AFFAIRES semantic recall, one targeted `search_knowledge_base` query and one
  bounded listing fallback. Repeating an identical query is not a search
  strategy.
- Open at most five candidate documents unless the user requests an exhaustive
  inventory.
- Stop widening retrieval when remaining unknowns cannot change the permitted
  conclusion.
- Cite the exact path or document ID for each material project fact.
- Expose contradictions, freshness limits and missing source confirmation.
- For every proposed omission or compliance gap, cite the exact project-document
  locator and the exact DOCUMENTAIRES reference when available. Otherwise label
  it `à vérifier` and state which reference is missing.
- End a material review with two to four optional, bounded follow-up paths when
  useful (for example: inspect a specific lot, verify a named standard, compare
  a revision or prepare a checklist). Label these as proposals; do not execute
  them or imply that they are required unless the user chooses one.
- Do not return unrelated personal contact data.
- Consult Pantheon only at the consequential boundaries defined by the generic
  skill; do not call it mechanically for ordinary lookup.
