# AI Log — Source need, registry and adaptive request method

Date: 2026-06-26

## Request

Formalize the adaptive request method and the source need / source registry logic discussed with the user.

Key intent:

```text
A request starts from the user's request, not directly from the input.
MÈTIS qualifies the cap.
HESTIA defines expected context and sufficiency.
Missing information creates a Source Need Candidate, not a guess.
Registered source routes do not automatically become evidence.
Sources may be project-specific, official, method-oriented, competence-oriented, stable, volatile, memory/recalled or absent.
```

## Required governance documents read

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
```

Additional context used from previous discussion:

```text
docs/governance/REQUEST_LIFECYCLE.md
docs/governance/CONTEXT_STACK.md
docs/governance/TERMINOLOGY_BOUNDARIES.md
```

## Search before creation

Searched repository files, open issues and PRs for:

```text
SOURCE_NEED
SOURCE_REGISTRY
source registry
source need
freshness policy
official web route
MAF
geodata
```

Result:

```text
No concrete duplicate was found.
```

## Files created

```text
docs/governance/ADAPTIVE_REQUEST_METHOD.md
docs/governance/SOURCE_NEED_AND_REGISTRY.md
templates/source_need_candidate.yaml
templates/source_registry_entry.yaml
templates/source_addition_candidate.yaml
```

## Decision classification

Accepted:

```text
Adaptive request method as active support doctrine.
Source Need Candidate before search when information is missing.
Source Registry as governed source-route registry, not evidence.
Source Addition Candidate for user/Pantheon proposed sources.
Freshness policy vocabulary.
Separation between project source, official source, professional method source, agency method source, technical competence source, stable knowledge, volatile source, memory/recall and absent source.
```

Refused:

```text
No web search engine.
No crawler.
No source database implementation.
No source validator.
No evidence engine.
No approval engine.
No memory engine.
No OpenWebUI action.
No Hermes skill.
No schema.
No tests.
No protected path changes.
No external action.
```

To verify:

```text
Whether ADAPTIVE_REQUEST_METHOD.md and SOURCE_NEED_AND_REGISTRY.md should be indexed in AUTHORITY_INDEX.md and MODULES.md.
Whether source-family vocabulary should be aligned later with ARCHITECTURE_SOURCE_POLICY.md.
Whether examples should be added under docs/examples/.
Whether a future schema should be considered under explicit approval.
```

To arbitrate:

```text
Whether official web routes should become a Notion/database-backed registry.
Whether the user can add source routes directly or only propose Source Addition Candidates.
Whether freshness policies should be blocking or advisory by source family.
Whether HESTIA should be promoted from candidate context-watch role to canonical role registry.
```

## Repository state

```text
Documented non-implemented.
Doctrine + templates only.
No schemas/ change.
No tests/ change.
No mcp-server change.
No operations/ change.
No platform/ change.
No Docker or .env change.
```

## Indexing note

`AUTHORITY_INDEX.md` is large and the connector returned truncated content during this intervention. To avoid a destructive partial overwrite, index updates were not applied in this pass. They should be handled as a focused follow-up with full-file access or a safer patch mechanism.
