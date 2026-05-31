# Quarkdown External Reference Review

Status: support review only — publication tooling candidate, not dependency approval.

This review records Quarkdown as an external reference for documentary publication, dossier rendering and presentation export.

It does not approve a dependency.

It does not approve an integration.

It does not define runtime behavior.

It does not make Quarkdown a Pantheon component.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Reference

Repository: `iamgio/quarkdown`

Observed posture on 2026-05-31:

- Markdown-based typesetting system;
- compiles one source project toward print-ready books, papers, knowledge bases, websites, presentations and PDFs;
- provides HTML, PDF and plain-text targets;
- supports slides through reveal.js;
- includes scripting, functions, variables, conditions, loops, layout builders, I/O and math through a Turing-complete Markdown extension;
- public repository under GPL-3.0 license, with additional licensing details to verify before any product or distributed use.

## Why it matters

Pantheon Next produces doctrine, domain-pack material, evidence-boundary language, checklists, templates and reviewable support documents.

Those artifacts may need publication in several formats:

```text
source doctrine -> HTML site
source doctrine -> PDF handbook
source doctrine -> slide deck
source domain pack -> professional fiche
source checklist -> printable review aid
```

Quarkdown is relevant as a candidate publication tool because it can reduce duplication between web, PDF, documentation and slides.

## Placement decision

Quarkdown belongs outside Pantheon Core.

It is a publication / rendering candidate, not a governance authority.

| Concern | Placement |
|---|---|
| source doctrine status | Pantheon |
| canonical document status | Pantheon |
| evidence status | Pantheon |
| approval status | Pantheon |
| memory status | Pantheon |
| publication rendering | external publication adapter candidate |
| PDF / HTML / slides export | external publication adapter candidate |

## Accepted

Quarkdown may be treated as a candidate external publication adapter for:

- publishing Pantheon governance documentation;
- rendering professional fiches from validated source documents;
- producing PDF handbooks, web documentation or slides from governed source material;
- supporting a future documentation CI, if explicitly approved outside Pantheon Core.

## Refused

Quarkdown must not be treated as:

- Pantheon Core;
- source of truth;
- Canonical Memory;
- Evidence Pack;
- approval record;
- runtime;
- scheduler;
- workflow engine;
- authority over document status;
- source validation engine;
- professional advice engine.

## To verify

Before any operational use, verify:

1. licensing impact for internal use, public distribution, commercial distribution and SaaS use;
2. whether AGPL-licensed modules or tooling affect the intended adapter boundary;
3. sandboxing requirements, because Quarkdown is Turing-complete;
4. whether document compilation may read local files, remote resources or environment data;
5. whether GitHub Actions use would introduce executable CI behavior requiring separate approval;
6. whether PDF generation depends on Node.js, npm, Puppeteer or browser execution;
7. whether generated outputs clearly retain source revision, status and date.

## Boundary rule

```text
The source status is governed by Pantheon.
The publication adapter renders from governed source.
The rendered artifact inherits status; it does not create status.
```

## Adapter posture

A future Quarkdown adapter, if created, must live outside Pantheon or in a separately approved adapter repository.

It may depend on Pantheon source files, templates and statuses.

Pantheon must not depend on Quarkdown.

A conformant adapter would:

```text
read governed source;
render target artifact;
stamp source revision and status;
return publication artifact metadata;
never decide truth, proof, memory or approval.
```

## Risk

Primary risk: confusing a polished rendered document with a validated document.

Secondary risk: treating scripted Markdown as passive Markdown.

Mitigation:

```text
Rendered does not mean validated.
Compiled does not mean approved.
Pretty does not mean true.
```

## Recommendation

Keep Quarkdown as `candidate / to verify` for publication tooling.

Do not integrate it into Pantheon Core.

Do not add CI, executable templates, publication pipelines or dependency files without a separate explicit approval.

## Boundary phrase

```text
Quarkdown may publish.
Pantheon governs status.
The validated remains.
```
