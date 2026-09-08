---
name: ifja-project-context
description: "Use for IFJA professional work that needs project/context retrieval or source routing across Hindsight, AFFAIRES, DOCUMENTAIRES, source-research and Pantheon policy. Routes to existing capabilities; creates no truth, Evidence, approval, governed memory or authorization."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/HERMES_INTEGRATION.md
  upstream: "agentskills.io SKILL.md standard; exact Hermes runtime compatibility must be qualified before admission"
---

# IFJA project context (runtime routing candidate)

Non-executable Hermes skill candidate. It selects and combines existing runtime/source paths for IFJA professional work. It owns no Pantheon governance, source authority, persistence, memory promotion or external-effect authorization.

## When to use

Use when IFJA work involves an affaire, project, client, contractor, professional document, prior correspondence, technical or regulatory reference, legal/contractual/responsibility question, or a professional action that requires source-aware context.

Do not use merely for generic conversation when no professional workspace context or governed boundary is relevant.

## Route context and sources

### 1. Resolve the working context

Identify the active affaire/project when relevant from the user request and available context. Use Hindsight only when associative recall materially helps identify prior context, actors, chronology, earlier positions or the likely dossier.

```text
Hindsight recall != source authority
memory recalled != Evidence
```

### 2. Prefer the professional workspace before external research

Use the currently admitted workspace bindings. Do not hard-code filesystem paths, Hindsight bank IDs or provider-specific names in this skill.

Use `AFFAIRES` for dossier-specific material, such as:

- project history and chronology;
- client, contractor and consultant correspondence;
- meeting reports and site records;
- contracts, markets, CCTP, estimates and schedules;
- project drawings, documents and prior positions;
- facts specific to one affaire.

Use `DOCUMENTAIRES` for transversal professional references, such as:

- construction techniques and methods;
- standards, DTU and technical guidance;
- regulation;
- legal, contractual and professional-responsibility references;
- jurisprudence, doctrine and professional guidance;
- relevant reference or product documentation.

When a dossier-specific question must be tested against a transversal professional rule, consult `AFFAIRES` and `DOCUMENTAIRES` in parallel when useful, then preserve their provenance separately in the synthesis.

```text
AFFAIRES = dossier-specific source material
DOCUMENTAIRES = transversal professional reference material
AFFAIRES + DOCUMENTAIRES = applied professional analysis when both are needed
```

### 3. Escalate to external research only for a material gap

After workspace retrieval, assess whether the material is sufficient, current and non-contradictory for the question.

Use external research when it materially improves the answer, for example when:

- required information is missing from the workspace;
- an internal reference may be stale or its currentness is uncertain;
- current law, regulation, standards status or official technical information matters;
- an authoritative external verification is needed;
- important sources conflict or a challenge search is warranted;
- the requested fact is inherently current and not maintained internally.

When external research is admitted, reuse the existing `source-research` skill/capability and its current contract. Do not create a second web/research workflow here.

Before external retrieval, minimize unnecessary private or dossier-specific detail. Prefer an abstracted query when it can answer the same question. Workspace access does not authorize external disclosure.

```text
vault first != vault always sufficient
external research available != external research necessary
private local context != permission to disclose it externally
```

### 4. Consult Pantheon at governed boundaries

If the request may cross a governed boundary, consult the current Pantheon policy service through the admitted MCP binding, using `classify_request` when that remains the exposed contract.

Relevant boundaries include, as applicable:

- professional, contractual or financial consequence;
- Evidence, validation or approval;
- governed status or protected mutation;
- external transmission or consequential action;
- memory/Register promotion or other governed persistence;
- a decision or authorization boundary owned by Pantheon.

Send observable request facts and scope to Pantheon. Do not derive K/V/C, approval levels or gate rules in this skill. Follow the policy data returned by Pantheon, including Task Contract, Evidence, gate, blocking and allowed-output requirements when present.

Do not call Pantheon mechanically for trivial consultation unless the current doctrine, Task Contract or binding requires it.

### 5. Execute with provenance preserved

Hermes may read, search, compare, calculate, analyze documents/images/plans/data, draft candidates and delegate independent work within the admitted boundary.

Parallelize independent retrieval when useful, especially `AFFAIRES` + `DOCUMENTAIRES`, multiple independent documents, or an already-justified external currentness check.

Keep material source families distinguishable in the result. Surface missing information, contradiction, freshness limits and uncertainty instead of flattening them into confidence.

## Final invariants

```text
retrieved != truth
Hindsight != Evidence
workspace source != governed truth
external source != automatic authority
model agreement != Evidence
runtime success != authorization
candidate != Decision
projection != persistence
```

This skill routes work. Existing source capabilities retrieve and research. Pantheon governs consequential status and authorization.
