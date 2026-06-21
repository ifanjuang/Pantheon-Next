# AI Log — Crawl4AI Hermes Skill Template

Date: 2026-06-21
Status: documented non-implemented
Scope: external tool review + Hermes-compatible skill template

## Work performed

- Reviewed the active Pantheon Next doctrine boundary:
  - `STATUS.md`
  - `MODULAR_DOMAIN_REORIENTATION.md`
  - `CAPABILITY_PLACEMENT.md`
  - `DOMAIN_PACK_SPEC.md`
  - `SKILL_LIFECYCLE.md`
  - `PADDLEOCR_HERMES_SKILL_NOTE.md`
- Reviewed `unclecode/crawl4ai` public GitHub README and Crawl4AI v0.9.x documentation.
- Classified Crawl4AI as useful only as a Hermes-side execution adapter for bounded source extraction.
- Added a reference review under `docs/governance/reference_reviews/`.
- Added a non-executable Hermes-compatible skill template under `templates/hermes/skills/web/crawl4ai-web-extract/`.

## Files added

- `docs/governance/reference_reviews/CRAWL4AI_HERMES_SKILL_REVIEW.md`
- `templates/hermes/skills/web/crawl4ai-web-extract/SKILL.md`
- `templates/hermes/skills/web/crawl4ai-web-extract/references/candidate-contract.md`
- `templates/hermes/skills/web/crawl4ai-web-extract/templates/public_page_task.yaml`
- `ai_logs/2026-06-21-crawl4ai-hermes-skill-template.md`

## Placement

```text
Crawl4AI retrieves.
Hermes executes the bounded skill.
Pantheon governs the candidate.
The validated remains.
```

## Accepted

- Crawl4AI as a candidate implementation detail inside a bounded Hermes web extraction skill.
- Single URL / small URL set extraction to Markdown or JSON candidates.
- Bounded deep crawl only with explicit domain, depth and page caps.
- Output as Web Extraction Candidate and Evidence Pack Candidate.

## Refused

- Crawl4AI as Pantheon doctrine.
- Crawl4AI as Pantheon runtime.
- Docker API server as default Pantheon/Hermes service.
- Unbounded crawl or hidden ingestion.
- Automatic RAG import.
- Approved evidence, validated truth or canonical memory.
- Paywall, access-control or anti-bot bypass as default behavior.

## To verify

- Local Hermes installation path for skill deployment.
- Installed `crawl4ai` version.
- Availability of `crwl`, `crawl4ai-doctor` and Playwright browsers.
- Whether the Docker API server is ever worth a separate review; default answer remains no.

## Repo state

Documented non-implemented.

No schemas, tests, operations, platform files, Docker files, `.env` files or runtime code were modified.
