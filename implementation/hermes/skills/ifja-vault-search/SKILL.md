---
name: ifja-vault-search
description: "Recherche les projets et documents dans les vaults IFJA."
license: MIT
metadata:
  version: 0.8.0
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
   If Hindsight returns no exact candidate but an admitted Workspace/vault path
   or filename is already known, treat this as an indexing gap: validate and
   open that exact local source (Docling for a file needing extraction) rather
   than asking for an upload or declaring the document absent. Distinguish
   `binding_unavailable`, `no_match` and `indexing_gap` in the limitation.
4. Use one targeted recall when the request is conceptual, associative or the
   exact source remains unknown.
5. For a recent project or information possibly awaiting synchronization, use
   the second and final recall against the configured conversation-memory
   binding only after the applicable AFFAIRES lookup (and its bounded fallback)
   has been attempted. Attribute memory-only information to recent conversation
   and mark it unconfirmed until an admitted business source supports it.

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
