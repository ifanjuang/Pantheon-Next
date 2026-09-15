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

0. For an ambiguous or continuity-dependent request, make one fast recall
   against the configured conversation-memory binding. Emit at most one interim
   `indice mémoire — non confirmé` when it materially helps locate the dossier,
   then continue to the applicable professional source.
1. For an exact name, alias, path or inventory question, use the configured
   document-listing capability before semantic recall.
2. Resolve the project page or exact source identity. A high-ranked semantic
   result does not select a project.
3. Open the exact project page or requested document before returning a material
   identifier, date, status or contractual fact.
4. Use one targeted recall when the request is conceptual, associative or the
   exact source remains unknown.
5. For a recent project or information possibly awaiting synchronization, use
   the second and final recall against the configured conversation-memory
   binding. Attribute memory-only information to recent conversation and mark it
   unconfirmed until an admitted business source supports it.

For a material professional factual answer, the applicable source lookup is
mandatory before final synthesis: `AFFAIRES` for dossier facts,
`DOCUMENTAIRES` for transversal professional facts, and both for a mixed
question. A memory lead never satisfies this requirement. If the required
binding is unavailable, return the limitation rather than substituting model
recall.

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
- Open at most five candidate documents unless the user requests an exhaustive
  inventory.
- Stop widening retrieval when remaining unknowns cannot change the permitted
  conclusion.
- Cite the exact path or document ID for each material project fact.
- Expose contradictions, freshness limits and missing source confirmation.
- Do not return unrelated personal contact data.
- Consult Pantheon only at the consequential boundaries defined by the generic
  skill; do not call it mechanically for ordinary lookup.
