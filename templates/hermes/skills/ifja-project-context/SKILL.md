---
name: ifja-project-context
description: "Use for IFJA professional work that needs project/context retrieval or source routing across Hindsight, AFFAIRES, DOCUMENTAIRES, source-research and Pantheon policy. Routes to existing capabilities; creates no truth, Evidence, approval, governed memory or authorization."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/HERMES_INTEGRATION.md
  related_skills: [pantheon-governed-method, pantheon-activity-projection, pantheon-request-intake, source-research]
  upstream: "agentskills.io SKILL.md standard; exact Hermes runtime compatibility must be qualified before admission"
---

# IFJA project context (runtime routing candidate)

Non-executable Hermes skill candidate. It routes IFJA professional work to existing context, source and policy capabilities. It owns no Pantheon governance, source authority, persistence or external-effect authorization.

## When to use

Use when work involves an affaire/project, professional documents or correspondence, technical/regulatory/legal/contractual/responsibility analysis, or a professional action that needs source-aware context.

Do not use merely for generic conversation when no professional workspace context or governed boundary is relevant.

## Conversation projection

For non-trivial IFJA work, when `pantheon-activity-projection` is available in the current Hermes profile, load and apply it before substantial execution. Use it only to present the plan, meaningful milestones, real sources, actual methods/tools and the result; it does not prescribe the runtime tool sequence and it does not create authority.

If the projection skill is unavailable, continue only within the otherwise admitted boundary and treat the missing projection as a presentation capability gap rather than inventing an equivalent governance layer.

```text
projection skill available != task authorized
projection plan != runtime dispatch plan
visible milestone != MCP-prescribed tool sequence
```

## Routing

### 1. Resolve context only when useful

Ground the active affaire/project from the request and available context. When project identity or the target referent is ambiguous, preserve the unresolved possibilities as a bounded candidate set; do not silently merge or select an identity merely to make reasoning easier. If the distinction would materially change the answer, permitted action or consequence, request targeted clarification or return a safe non-conclusion. If it would not, continue only from supported shared facts while carrying the uncertainty explicitly.

Once an affaire/project is sufficiently grounded, keep it as the conversation-local working referent for elliptical follow-ups until the user selects another one or material evidence makes the referent uncertain. For detailed resolution and alias handling, use [references/project-resolution.md](references/project-resolution.md).

For every material professional factual answer, complete a source preflight
before the final answer. This is a completion requirement, not a generic
governance classifier:

```text
dossier/client/address/budget/date/status/planning -> AFFAIRES required
technical/standard/regulatory/legal/method question -> DOCUMENTAIRES required
dossier fact tested against a transversal rule -> AFFAIRES + DOCUMENTAIRES required
ambiguous dossier or conversational continuity -> conversation memory lead, then the applicable source above
```

The preflight is not required for casual conversation, pure transformation of
content supplied in the current request, or a question whose answer does not
depend on professional workspace facts.

Record the completed consultation with the generic
`templates/hermes/returns/source_preflight_receipt.template.yaml` shape. Each
required family must name the actual binding/tool, the exact source reference
opened, any inspected locator and observed limitations. A search result or a
memory lead without an opened exact source leaves the receipt incomplete.

When dossier identity is ambiguous or continuity materially helps, consult the
admitted conversation-memory binding first. Treat it only as a fast location or
context lead. If interim assistant messages are supported, publish one compact
`Mnemosyne` milestone as soon as that lead changes the user's understanding,
label it `indice mémoire — non confirmé`, and continue immediately with exact
source discovery. Do not wait for the final synthesis to disclose a useful lead,
but do not present it as the answer.

Before returning a material budget, date, status, obligation or recommendation,
resolve and open the exact applicable workspace source. If the required binding
is unavailable or returns no support, state the Capability Gap or unconfirmed
scope instead of answering from model recall.

```text
Hindsight recall != source authority
fast memory lead != confirmed answer
memory recalled != Evidence
bounded referent candidate set != merged identity
conversation continuity != governed persistence
```

### Fast context path for project questions

For a context-only question about an affaire or project (for example “what do
we know about Floquet?”), use this bounded sequence:

```text
1. Hindsight Memory — one fast Mnemosyne lead
2. Hindsight AFFAIRES — confirm dossier-specific facts and identity
3. Hindsight DOCUMENTAIRES — only when a technical, regulatory, legal,
   standards or professional rule is actually required
```

Do not call the three Hindsight bindings in parallel for a simple project-context
question. Do not use Web Search before this local path has returned no usable
support or a current public fact is explicitly required. If the project name is
ambiguous, preserve the candidates and ask one targeted clarification rather
than widening the web query. Label the first memory result `indice mémoire —
non confirmé`; do not present it as a dossier fact until AFFAIRES confirms it.

### 2. Workspace first

Use admitted workspace bindings; do not hard-code filesystem paths, Hindsight bank IDs or provider-specific names.

- `AFFAIRES` -> dossier-specific facts, history, correspondence, contracts, CCTP, estimates, schedules, plans and project records.
- `DOCUMENTAIRES` -> transversal technical, standards/DTU, regulatory, legal, contractual, responsibility, jurisprudence and professional reference material.
- `AFFAIRES` + `DOCUMENTAIRES` -> consult both only when a dossier-specific question must be tested against a transversal professional rule.

Keep the two source families distinguishable in the synthesis.

Start the required source lookup as soon as the route is selected. Independent
AFFAIRES and DOCUMENTAIRES lookups may run in parallel only when both source
families are materially required by the same question. Progressive chat output
may report a bounded lead while retrieval continues; it must not imply that a
background task exists when execution is actually sequential.

For claims about plans, PDFs or other professional documents, keep `mentioned != exact source present != relevant content inspected`. When content inspection matters, use [references/document-inspection.md](references/document-inspection.md).

### 3. External research only when it adds material value

After workspace retrieval, assess whether the material is sufficient, current and non-contradictory. When information is missing, stale, uncertain, conflicting, inherently current, or needs authoritative current verification, reuse the existing `source-research` skill/capability under its current contract.

Do not create a second web/research workflow here. Before external retrieval, minimize private or dossier-specific detail and prefer an abstracted query when it can answer the same question.

```text
vault first != vault always sufficient
workspace access != external disclosure authorization
```

### 4. Pantheon only at governed boundaries

When the request may involve professional/contractual/financial consequence, Evidence or approval, governed status or protected mutation, external transmission/action, memory/Register promotion, or another consequential decision boundary, consult the currently selected Pantheon policy binding.

Before classification, reuse the generic `pantheon-request-intake` semantic adapter to describe only the material request conditions, optional coordination relations and observable completion requirements. Do not create an IFJA-specific K/V/C or trigger classifier here.

The current repository exposes the same bounded read-only policy meaning through
MCP and the authenticated HTTP service described by
`mcp-server/docs/HTTP_API_CONTRACT.md`. The reviewed governed MCP binding exposes
`classify_request`, `evaluate_preflight`, the Task Contract and Evidence Pack
skeleton preparers, and Context Pack planning/validation. If the selected
deployed binding cannot provide a required decision operation, stop before the
consequential effect and return a Capability Gap rather than inventing policy
locally.

Pass the semantic request candidate plus observable scope. Do not derive K/V/C, approval levels or gate rules in this skill. Follow the policy data returned by Pantheon. Do not call Pantheon mechanically for trivial consultation unless the current doctrine, Task Contract or binding requires it.

### 5. Execute without changing authority

Hermes may search, read, compare, analyze, calculate, draft and delegate within the admitted boundary. Parallelize independent retrieval when useful, especially `AFFAIRES` + `DOCUMENTAIRES` and already-justified currentness checks.

Preserve provenance and surface missing information, contradiction, freshness limits and uncertainty.

### 6. Select an artifact destination explicitly

When a requested artifact could be created in more than one admitted system,
resolve its destination before the first write:

1. use an exact destination already admitted by the current Task Contract or
   governed workflow; use a dossier manifest only when its admitted contract
   actually defines a destination field;
2. otherwise use the destination explicitly named in the current request;
3. otherwise, when the choice changes collaboration, permissions, external
   exposure or the source of truth, ask one short clarification presenting only
   the materially different destinations;
4. when useful, offer a local Markdown draft followed by a separately approved
   publication step.

Do not create parallel copies in multiple systems silently. Derive candidate
destinations only from the admitted capability catalogue and available governed
context; do not assume that every dossier manifest defines a destination.
A local workspace such as Obsidian Markdown is a normal candidate for durable,
dossier-linked knowledge; a collaborative system such as Google Docs is a
normal candidate for review or sharing, but requires an admitted connection and
any applicable external-write authorization. A confirmed durable
preference may be recorded in the dossier manifest through the governed update
path; do not infer or persist it from one incidental choice.

```text
available destination != selected destination
local draft != external publication
Google connection available != external write authorized
one chosen destination != permanent dossier preference
```

## Final invariants

```text
retrieved != truth
Hindsight != Evidence
workspace source != governed truth
external source != automatic authority
mentioned != exact source present
exact source present != relevant content inspected
model agreement != Evidence
runtime success != authorization
candidate != Decision
projection != persistence
```

This skill routes work. Existing capabilities retrieve and research. Pantheon governs consequential status and authorization.
