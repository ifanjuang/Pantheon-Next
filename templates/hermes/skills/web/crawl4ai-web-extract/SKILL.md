---
name: crawl4ai-web-extract
description: Bounded public-web extraction to Markdown or JSON candidates using Crawl4AI. Produces Web Extraction Candidates and Evidence Pack Candidates; never validates truth, evidence, memory or approval.
category: web
version: 0.1.0
status: candidate-template
---

# Crawl4AI Web Extract

Use this skill when the user needs Hermes to retrieve a public web page, or a tightly bounded public URL set, and turn it into reviewable Markdown or JSON for a Pantheon-governed task.

This skill is compatible with the Hermes skill package pattern: place this directory under `~/.hermes/skills/web/crawl4ai-web-extract/` or expose it through `skills.external_dirs`.

This skill assumes `crawl4ai` and its browser runtime are already installed in the Hermes environment. It does not install dependencies by itself.

## Authority boundary

```text
Crawl4AI retrieves.
Hermes executes the bounded skill.
Pantheon governs the candidate.
The validated remains.
```

The output of this skill is always candidate material.

It must not produce:

- validated truth;
- approved evidence;
- canonical memory;
- an approval event;
- a professional deliverable;
- an external transmission;
- an automatic RAG import;
- an unbounded corpus.

## Use this skill for

- extracting a single public page into Markdown;
- extracting a small, explicitly listed set of public URLs;
- extracting a capped public documentation section;
- producing a source quality report before a professional claim is made;
- preparing a Web Extraction Candidate and Evidence Pack Candidate for review.

## Do not use this skill for

- private, authenticated or client portal content;
- paywall bypass;
- anti-bot bypass or stealth escalation;
- credential harvesting;
- scraping personal data without a clear lawful/professional basis;
- unbounded crawling;
- hidden ingestion into memory or RAG;
- publishing, sending or filing extracted content externally;
- treating extracted content as proof without review.

## Required preflight

Before running Crawl4AI, check and state:

```text
1. Task Contract exists or user request can be safely represented as a read-only extraction task.
2. Target URL(s) are explicit.
3. URL(s) are public or explicitly authorized by the user.
4. Scope is task-bound or dossier-bound.
5. Requested effect is read_only or candidate_only.
6. No external delivery is requested.
7. No canonical memory or approved evidence will be produced.
8. For multi-page extraction: allowed domain, page cap and depth cap are explicit.
9. For professional use: review_required flag is set.
```

If any point fails, do not crawl. Return a Capability Gap.

## Default safe parameters

Use the safest useful posture unless the Task Contract explicitly allows more:

```text
single_url_default: true
same_domain_only: true
max_depth_default: 0
max_pages_default: 1
headless: true
cache_mode: bypass for freshness-sensitive sources
proxy: none
stealth_or_antibot_escalation: refused by default
llm_extraction: off by default
memory_write: never
rag_import: never
```

## Execution procedure

### 1. Dependency check

Run one or more of:

```bash
python -c "import crawl4ai; print('crawl4ai ok')"
crwl --help
crawl4ai-doctor
```

If unavailable, return a Capability Gap with the missing dependency.

### 2. Single public page to Markdown

Preferred first pass:

```bash
crwl "https://example.com/page" -o markdown --bypass-cache
```

When CLI output is insufficient or structured metadata is needed, use Python:

```python
import asyncio
import json
from datetime import datetime, timezone
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    url = "https://example.com/page"
    browser_config = BrowserConfig(headless=True)
    run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=run_config)

    candidate = {
        "candidate_type": "web_extraction_candidate",
        "adapter_id": "crawl4ai",
        "adapter_version": "unknown_or_reported",
        "source": {
            "url": url,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "access_mode": "public_web",
            "crawl_depth": 0,
            "page_count": 1
        },
        "success": bool(result.success),
        "extraction": {
            "markdown": getattr(result, "markdown", None),
            "metadata": getattr(result, "metadata", {})
        },
        "quality_flags": ["review_required"],
        "limitations": [
            "web_content_may_change",
            "not_source_of_truth_without_review"
        ],
        "evidence_status": "source_candidate",
        "memory_status": "not_memory"
    }

    print(json.dumps(candidate, ensure_ascii=False, indent=2, default=str))

asyncio.run(main())
```

### 3. Bounded deep crawl

Only use this when the Task Contract states domain, max depth and max pages.

Minimum caps:

```text
include_external: false
max_depth: explicit
max_pages: explicit
```

Example pattern:

```python
import asyncio
import json
from datetime import datetime, timezone
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.content_scraping_strategy import LXMLWebScrapingStrategy

async def main():
    start_url = "https://example.com/docs/"
    max_depth = 1
    max_pages = 10

    config = CrawlerRunConfig(
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=max_depth,
            include_external=False,
            max_pages=max_pages
        ),
        scraping_strategy=LXMLWebScrapingStrategy(),
        verbose=True
    )

    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun(start_url, config=config)

    candidate = {
        "candidate_type": "web_extraction_candidate",
        "adapter_id": "crawl4ai",
        "source": {
            "url": start_url,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "access_mode": "public_web",
            "crawl_depth": max_depth,
            "page_cap": max_pages,
            "page_count": len(results)
        },
        "pages": [
            {
                "url": r.url,
                "success": bool(r.success),
                "depth": getattr(r, "metadata", {}).get("depth", None),
                "markdown": getattr(r, "markdown", None)
            }
            for r in results
        ],
        "quality_flags": ["review_required", "bounded_deep_crawl"],
        "limitations": ["web_content_may_change", "not_source_of_truth_without_review"],
        "evidence_status": "source_candidate",
        "memory_status": "not_memory"
    }

    print(json.dumps(candidate, ensure_ascii=False, indent=2, default=str))

asyncio.run(main())
```

## Output requirements

Always return a short human-readable summary plus a candidate object.

The summary must separate:

```text
retrieved: what was fetched
not_retrieved: what was skipped or blocked
candidate_use: what the output can support
forbidden_use: what it cannot support
review_required: yes/no and why
```

The candidate object should follow the reference contract:

```text
skill_view("crawl4ai-web-extract", "references/candidate-contract.md")
```

## Evidence Pack Candidate expectations

At minimum, include:

- original URL;
- retrieval timestamp;
- crawl depth;
- page count;
- extraction mode;
- adapter id and version when available;
- Markdown or JSON candidate;
- quality flags;
- limitations;
- review recommendation.

## Capability Gap shape

Return this when blocked:

```json
{
  "candidate_type": "capability_gap",
  "missing": "task_contract_or_dependency_or_scope_or_permission",
  "needed_for": "bounded_web_extraction",
  "blocked_effect": "crawl_not_run",
  "consequence_if_ignored": "unbounded_or_unauthorized_source_use",
  "safe_fallback": "ask_for_scope_or_install_dependency_or_review_source_manually",
  "status": "blocked"
}
```

## Final reminder

A successful Crawl4AI run is not proof. It is source preparation.

A clean Markdown result is not evidence approval. It is a reviewable candidate.
