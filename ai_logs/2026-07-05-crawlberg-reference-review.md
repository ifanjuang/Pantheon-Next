# 2026-07-05 — Crawlberg reference review

## What changed

Added:

```text
docs/governance/reference_reviews/CRAWLBERG_REFERENCE_REVIEW.md
```

The new document records `xberg-io/crawlberg` as an external reference and distills it into a candidate Web Evidence Intake adapter pattern.

## Why

The user provided `https://github.com/xberg-io/crawlberg` and asked to continue after the initial assessment.

The repository already has doctrine for:

- capability placement;
- modular domain reorientation;
- domain-pack boundaries;
- RAG ingestion and evidence boundaries;
- external repository inspirations;
- card-stack projection.

The proper placement is therefore a reference review, not a new core runtime document.

## Documents checked

Read before writing:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/README.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MODULES.md`
- `docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`
- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`
- `ai_logs/README.md`

Related issue search performed with no direct open match found for crawl/web ingestion/evidence adapter language.

Recent PR list reviewed for active context; no specific open Crawlberg-related PR was found.

## Decision classification

Accepted:

- Crawlberg as inspiration for a Hermes-side web evidence intake adapter.
- The pattern `Task Contract -> execution runtime -> Result Candidate + Evidence Pack Candidate`.
- Crawl/HTML-to-Markdown/metadata/trace outputs as candidate material.

Refused:

- Crawlberg as Pantheon dependency.
- Pantheon as crawler, MCP host, browser runner, WAF bypass operator, scheduler or connector gateway.
- Crawl success as proof or source validation.
- Automatic knowledge-base mutation or memory promotion.

To verify:

- whether a Hermes skill should wrap Crawlberg or another crawler;
- security policy for SSRF, credentials, private networks and browser rendering;
- whether MCP exposure is acceptable or too broad;
- how trace references should appear in the cockpit.

To arbitrate:

- whether architecture-domain source policy should allowlist public municipal/urbanism web sources;
- whether authenticated portals can ever be crawled under approved user session scope;
- whether web intake may seed Knowledge Candidates or only Evidence Candidates in V0.

## Repo state

Documented non-implemented.

No dependency added.
No runtime added.
No Hermes skill added.
No OpenWebUI plugin added.
No MCP server added.
No schema added.
No tests added.
No protected path modified.

## Risks and limits

The main risks are:

- retrieval mistaken for proof;
- browser rendering mistaken for reliability;
- WAF/antibot handling drifting into bypass normalization;
- public web pages promoted into canonical knowledge without review;
- trace data treated as Evidence Pack content.

The review explicitly keeps these surfaces candidate-only and subject to gates.
