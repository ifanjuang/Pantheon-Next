---
name: ifja-project-context
description: "Use for IFJA professional work that needs project/context retrieval or source routing across Hindsight, AFFAIRES, DOCUMENTAIRES, source-research and Pantheon policy. Routes to existing capabilities; creates no truth, Evidence, approval, governed memory or authorization."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  governed_by: docs/governance/HERMES_INTEGRATION.md
  related_skills: [pantheon-activity-projection, pantheon-request-intake, source-research]
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

Use Hindsight when associative recall materially helps with prior context, actors, chronology, earlier positions or dossier resolution.

```text
Hindsight recall != source authority
memory recalled != Evidence
bounded referent candidate set != merged identity
conversation continuity != governed persistence
```

### 2. Workspace first

Use admitted workspace bindings; do not hard-code filesystem paths, Hindsight bank IDs or provider-specific names.

- `AFFAIRES` -> dossier-specific facts, history, correspondence, contracts, CCTP, estimates, schedules, plans and project records.
- `DOCUMENTAIRES` -> transversal technical, standards/DTU, regulatory, legal, contractual, responsibility, jurisprudence and professional reference material.
- `AFFAIRES` + `DOCUMENTAIRES` -> consult both in parallel when a dossier-specific question must be tested against a transversal professional rule.

Keep the two source families distinguishable in the synthesis.

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

The current repository decision interface is the bounded HTTP policy service described by `mcp-server/docs/HTTP_API_CONTRACT.md`. Invoke `classify_request` through a binding that actually exposes that operation; do not assume that the consultation-only MCP binding exposes classification. If the selected deployed binding cannot provide the required decision operation, stop before the consequential effect and return a Capability Gap rather than inventing policy locally.

Pass the semantic request candidate plus observable scope. Do not derive K/V/C, approval levels or gate rules in this skill. Follow the policy data returned by Pantheon. Do not call Pantheon mechanically for trivial consultation unless the current doctrine, Task Contract or binding requires it.

### 5. Execute without changing authority

Hermes may search, read, compare, analyze, calculate, draft and delegate within the admitted boundary. Parallelize independent retrieval when useful, especially `AFFAIRES` + `DOCUMENTAIRES` and already-justified currentness checks.

Preserve provenance and surface missing information, contradiction, freshness limits and uncertainty.

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
