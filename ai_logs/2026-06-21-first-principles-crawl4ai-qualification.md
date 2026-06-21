# AI log — First-principles skill and Crawl4AI qualification

Date: 2026-06-21

Status: documented non-implemented.

Branch:

```text
docs/first-principles-crawl4ai-qualification
```

## Trigger

User asked to convert `reshadat/first-principles-destructor` into a Hermes-compatible skill if truly useful, then analyze `unclecode/crawl4ai`.

## Source documents read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/AUTHORITY_INDEX.md`
- PR #112 summary and comments around `SKILL_LIFECYCLE.md`
- PR #162 summary around Hermes 0.17 adapter boundaries
- PR #176 draft state and Zeus comment, treated as context only because it is not merged

## External references reviewed

- `https://github.com/reshadat/first-principles-destructor`
- `https://github.com/reshadat/first-principles-destructor/blob/main/SKILL.md`
- `https://github.com/unclecode/crawl4ai`
- `https://docs.crawl4ai.com/`
- Crawl4AI Docker migration and security-hardening notes

## Decision

Accepted:

```text
first-principles-destructor is useful as a Hermes-side analytical skill candidate.
Crawl4AI is useful as a Hermes-side web/document extraction adapter candidate.
Both may produce candidates only.
```

Refused:

```text
No runnable Hermes skill is installed in Pantheon Next.
No Crawl4AI dependency is added to Pantheon Next.
No crawler runtime, Docker API, scheduler, queue, MCP host, memory engine or approval engine is added.
No source retrieval becomes proof by itself.
No external skill becomes doctrine by being copied into a template.
```

To verify:

```text
first-principles template output discipline under real Pantheon tasks;
Crawl4AI SDK behavior in a Hermes sandbox;
network egress and source authorization controls;
Markdown fidelity and metadata preservation;
Docker API hardening before any server use.
```

To arbitrate:

```text
whether first-principles review becomes a standard review angle for major Pantheon proposals;
whether Crawl4AI first admission is SDK-only or may include a local loopback Docker API later;
whether deep crawling and authenticated crawling are excluded or require explicit per-source approval.
```

## Files added

- `templates/hermes/skills/first-principles-assumption-review/SKILL.md`
- `templates/hermes/skills/first-principles-assumption-review/README.md`
- `docs/governance/reference_reviews/FIRST_PRINCIPLES_DESTRUCTOR_HERMES_SKILL.md`
- `docs/governance/reference_reviews/CRAWL4AI_HERMES_ADAPTER_REVIEW.md`

## Repo state

Documented non-implemented.

The skill template is a template only. It is not installed, active or task-authorized.

The Crawl4AI review is a placement review only. No dependency, Docker service, runtime configuration, connector or operation file was added.

No protected path was modified.
