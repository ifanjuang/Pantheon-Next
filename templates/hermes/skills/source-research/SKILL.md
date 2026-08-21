---
name: source-research
description: "Use for bounded source research under an authorized Task Contract: discover sources, inspect source content, map claims to sources, surface contradictions and uncertainty, and return a traceable research candidate. Never treats retrieval as truth, Evidence, approval, or canonical memory."
metadata:
  owner_layer: hermes
  status: candidate_template_only
  pantheon_role: ARGOS
  governed_by: docs/governance/AGENTS.md
  upstream: "agentskills.io SKILL.md standard; exact Hermes runtime compatibility must be qualified before admission"
---

# Source research (governed candidate)

Non-executable Hermes skill candidate. Pantheon governs; Hermes executes outside the repository under Task Contract.

## Purpose

Perform source-grounded research within an explicitly bounded question.

```text
question
→ research frame
→ source discovery
→ source inspection
→ claim/source mapping
→ contradiction + uncertainty review
→ synthesis candidate
→ validation
```

## When to use

Use for:

- source discovery for a bounded question;
- deeper investigation beyond supplied context;
- source credibility or contradiction audit;
- multi-source synthesis;
- final validation of claims, citations, dates or completeness.

Do not use merely to restate already sufficient context.

## Required context

Use the available Task Contract and Context Pack to identify, when relevant:

- research question and scope;
- admitted source references;
- jurisdiction, date or freshness requirements;
- allowed retrieval capabilities;
- evidence/citation expectations;
- material limits on breadth, cost, time or data exposure.

Missing capability, scope or authorization must be reported, not bypassed.

## Modes

A task may combine these modes without creating separate skills:

- `discover` — find candidate sources; discovery results are not facts;
- `investigate` — inspect source content and extract relevant claim candidates;
- `audit` — assess provenance, credibility, freshness, methodology, bias signals, limitations and contradictions;
- `synthesize` — combine inspected sources while preserving agreement, disagreement and uncertainty;
- `validate` — re-check material claims, citations, dates, conflicts and coverage before return.

## Method

### 1. Frame

- restate the bounded question;
- split material sub-questions when useful;
- identify important assumptions and unknowns;
- do not silently widen scope.

### 2. Discover

Use only capabilities allowed by the Task Contract.

Prefer source classes appropriate to the question, generally:

1. primary or official sources;
2. peer-reviewed or methodologically transparent research;
3. authoritative institutional or industry material;
4. credible expert analysis;
5. reputable reporting;
6. community discussion for experience, dissent or leads.

Popularity does not confer authority.

### 3. Inspect

Search snippets, previews, summaries and retrieval excerpts are discovery aids.

For a material claim, inspect the supporting source content when technically available before relying on it. If full inspection is unavailable, disclose the limitation and reduce certainty.

Do not enforce a fixed source count. Use enough independent sources for the consequence and uncertainty of the claim.

### 4. Map claims to sources

For each material claim candidate, retain when available:

- source reference and identity;
- precise locator;
- publication/revision/observation date;
- posture: `supports`, `contradicts`, `qualifies`, or `uncertain`;
- material limitation.

```text
claim candidate
├─ source A: supports
├─ source B: qualifies
├─ source C: contradicts
└─ uncertainty
```

Citation count is not confidence. Dependent sources are not independent corroboration.

### 5. Evaluate proportionally

Assess only factors material to the question, such as:

- identity and provenance;
- primary vs derivative status;
- issuer/author competence;
- date, revision and applicability;
- methodology and underlying evidence;
- conflict-of-interest signals;
- independent corroboration;
- jurisdiction and scope;
- limitations or missing data.

Do not force SWOT or another generic framework.

### 6. Reconcile

- distinguish real contradiction from differences of scope, date, definition or method;
- preserve material minority/conflicting findings;
- prefer stronger applicable evidence over majority vote;
- state when available sources do not support a conclusion candidate.

### 7. Synthesize

Distinguish:

```text
observed source content
interpretation
inference
recommendation candidate
uncertainty
```

Retrieved statements do not become professional, legal, contractual or project truth.

### 8. Validate

Before return, verify that:

- material claims are source-traceable or labeled inference/uncertainty;
- citations point to the intended source/locator when available;
- relevant dates and versions fit the question;
- important contradictions and limitations are visible;
- scope has not silently widened;
- no output has been promoted into Evidence, Decision, Knowledge or canonical memory.

## Allowed outputs

As authorized:

- `research_report_candidate`;
- `source_map`;
- `claim_candidate`;
- `source_risk_note`;
- `contradiction_note`;
- `missing_source_note`;
- `uncertainty_note`;
- `research_limitation`;
- `followup_candidate`;
- `capability_gap`.

## Forbidden effects

This skill must not by itself:

- approve or professionally validate;
- create canonical Evidence or Knowledge;
- promote memory;
- mutate doctrine or registries;
- send externally;
- perform consequential external effects;
- install or activate tools/providers/runtimes;
- widen the task automatically;
- create autonomous recurring research loops.

## Escalation

- source identity/provenance/evidentiary ambiguity → ARGOS review;
- legal/policy/authorization/consequential risk → THEMIS;
- completeness/evidence sufficiency → APOLLO;
- unresolved competing candidate postures → ZEUS;
- missing capability → return `capability_gap`.

## Return expectations

A substantial return should expose, as applicable:

1. question and scope;
2. concise findings candidate;
3. material claim/source support;
4. contradictions and uncertainty;
5. source-quality/freshness limitations;
6. missing information;
7. source references and locators;
8. follow-up as candidate, never authorization.

## Non-equivalences

```text
searched != inspected
retrieved != truth
cited != verified
many sources != independent corroboration
source supports claim != professional validation
research synthesis != Evidence
runtime success != result validity
candidate conclusion != Decision
useful result != canonical memory
```
