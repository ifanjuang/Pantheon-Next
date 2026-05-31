# Quarkdown External Reference Review

Status: support review only — publication tooling and Hermes Skill Candidate boundary, not dependency approval.

This review records Quarkdown as an external reference for documentary publication, dossier rendering and presentation export.

It does not approve a dependency.

It does not approve an integration.

It does not install or define a Hermes skill.

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

Its operational projection, if used, should be a Hermes Skill Candidate for document rendering, not a Pantheon component.

It is a publication / rendering candidate, not a governance authority.

| Concern | Placement |
|---|---|
| source doctrine status | Pantheon |
| canonical document status | Pantheon |
| evidence status | Pantheon |
| approval status | Pantheon |
| memory status | Pantheon |
| publication rendering | Hermes Skill Candidate or external publication adapter |
| PDF / HTML / slides export | Hermes Skill Candidate or external publication adapter |
| rendered artifact display | exposure surface |

## Operational projection

If used, Quarkdown should be exposed as a Hermes Skill Candidate for document rendering.

Suggested skill name:

```text
quarkdown_publish_candidate
```

Alternative neutral name:

```text
hermes_skill_quarkdown_render
```

The skill may compile governed source into Rendered Artifact Candidates.

It must not validate, approve, publish externally, promote memory or decide document status.

### Skill envelope

Input:

```text
Task Contract
source document path or source bundle
target format: html | pdf | slides | text
source status
expected artifact metadata
approval ceiling
```

Output:

```text
Rendered Artifact Candidate
Evidence Pack Candidate or compile evidence candidate
compile log
source revision
source status
render timestamp
warnings
license / dependency note if relevant
```

### Forbidden skill outputs

The skill must not produce:

```text
approved artifact
canonical document status
Canonical Memory
Evidence Pack final status
external publication confirmation
professional advice
source validity decision
```

## Accepted

Quarkdown may be treated as a candidate Hermes rendering skill or external publication adapter for:

- publishing Pantheon governance documentation after human-approved source status;
- rendering professional fiches from validated or explicitly candidate source documents;
- producing PDF handbooks, web documentation or slides from governed source material;
- returning Rendered Artifact Candidates with compile metadata;
- supporting a future documentation CI, if explicitly approved outside Pantheon Core.

## Refused

Quarkdown must not be treated as:

- Pantheon Core;
- source of truth;
- Canonical Memory;
- Evidence Pack final status;
- approval record;
- approval engine;
- scheduler;
- workflow engine;
- authority over document status;
- source validation engine;
- professional advice engine.

## To verify

Before any operational use, verify:

1. licensing impact for internal use, public distribution, commercial distribution and SaaS use;
2. whether AGPL-licensed modules or tooling affect the intended adapter or skill boundary;
3. sandboxing requirements, because Quarkdown is Turing-complete;
4. whether document compilation may read local files, remote resources or environment data;
5. whether GitHub Actions use would introduce executable CI behavior requiring separate approval;
6. whether PDF generation depends on Node.js, npm, Puppeteer or browser execution;
7. whether generated outputs clearly retain source revision, status and date;
8. whether the Hermes Skill Candidate can run without mutating governed source files.

## Boundary rule

```text
The source status is governed by Pantheon.
The Hermes skill renders from governed source.
The rendered artifact inherits status; it does not create status.
```

## Adapter and skill posture

A future Quarkdown adapter or skill, if created, must live outside Pantheon or in a separately approved adapter / Hermes repository.

It may depend on Pantheon source files, templates, Task Contracts and statuses.

Pantheon must not depend on Quarkdown.

A conformant Hermes Skill Candidate would:

```text
read governed source;
render target artifact;
stamp source revision and status;
return publication artifact metadata;
return compile logs and warnings;
never decide truth, proof, memory or approval.
```

## Risk

Primary risk: confusing a polished rendered document with a validated document.

Secondary risk: treating scripted Markdown as passive Markdown.

Operational risk: allowing a rendering skill to become a hidden publishing pipeline.

Mitigation:

```text
Rendered does not mean validated.
Compiled does not mean approved.
Pretty does not mean true.
Rendered Artifact Candidate does not mean deliverable.
```

## Recommendation

Keep Quarkdown as `candidate / to verify` for publication tooling and Hermes Skill Candidate projection.

Do not integrate it into Pantheon Core.

Do not add CI, executable templates, publication pipelines, dependency files or a Hermes skill implementation without a separate explicit approval.

## Boundary phrase

```text
Quarkdown may render.
Hermes may execute the rendering as a candidate skill.
Pantheon governs status.
The validated remains.
```
