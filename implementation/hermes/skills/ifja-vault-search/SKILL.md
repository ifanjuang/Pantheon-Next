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

```text
subject match != selected project
recall snippet != exact document
conversation memory != business source
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
