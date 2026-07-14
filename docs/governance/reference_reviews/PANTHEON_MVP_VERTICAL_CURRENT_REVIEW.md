# Pantheon MVP Vertical — Current External Review

Status: validation-only external reference review — observed, not adopted.
Boundary profile: validation_only_trace.

Observation date: 2026-07-13.

## Reviewed source

```text
repository: ifanjuang/pantheon-mvp
commit: 7c6ad4893cb7300968117cdcfa5418c740c32a18
commit subject: Merge pull request #27 from ifanjuang/claude/ci-fail-not-skip
visibility: public
```

This review supersedes bundle-era operational observations for current-status purposes. It does not erase the historical bundle review.

## Review scope

Observed through the GitHub repository at the pinned commit:

- repository README and declared boundary contract;
- recent commit history visible before the pinned merge;
- declared Block 1 and Block 2 drafting-seam posture;
- declared bounded ingestion and scope-first retrieval posture;
- declared candidate, adoption, activation and production-use status;
- availability of PR-triggered CI evidence through the connected query.

Not independently reproduced in this review:

- local installation;
- Docker or pgvector startup;
- test execution;
- source-path escape tests;
- schema validation against the current Pantheon main;
- gate/register behavior;
- professional correctness;
- production safety.

## Observed external implementation

The pinned README declares:

```text
Block 1 + Block 2 drafting seam present;
bounded ingestion of declared sources;
SQL scope filtering before vector ranking;
deterministic local embedding;
Result Candidate and Evidence Pack Candidate production;
refusal / capability-gap output;
live LLM Drafter remains a Hermes-side slot;
external send, approval, memory promotion, scheduling and provider routing forbidden.
```

Recent repository history visible before the pinned commit also records work on:

- register-seam validation;
- decision and retention boundaries;
- additional C3/C4 scenarios;
- duty-of-care and legal-qualification flags;
- fail-loud pgvector CI behavior.

Commit subjects and repository documentation are implementation observations. They are not accepted Pantheon evidence by themselves.

## CI observation

The available query returned no PR-triggered workflow run for merge commit `7c6ad4893cb7300968117cdcfa5418c740c32a18`.

```text
workflow run returned: none
CI success claimed: no
CI failure claimed: no
CI evidence status: not established for this exact observation
```

The commit subject refers to CI behavior, but a commit subject is not CI evidence.

## Current classification

```text
external repository: observed
external implementation: partially verified by repository inspection
Pantheon governance evidence: not fully accepted
binding adoption: not adopted
activation: not activated
production use: forbidden
installation by Pantheon: none
```

## Historical blockers

Bundle-era claims that the repository was unpublished, contained only Block 1, or had no pushed executable content are obsolete.

The following historical P0 findings must not be marked resolved solely from commit titles or README statements:

- current Task Contract schema alignment;
- canonical source-path containment, including symlink escape behavior;
- stand-in naming and role clarity across all executable entry points;
- decision-record and retention-authorization conformance with current Pantheon schemas;
- vendored upstream freshness;
- independently observed CI and test results.

Each item requires a current file/test reference or a separate bounded reproduction before adoption.

## Remaining adoption blockers

1. compare vendored Pantheon contracts with current Pantheon main;
2. inspect the current source-path resolver and its adversarial tests;
3. inspect current decision and Register Candidate seams against canonical contracts;
4. establish CI evidence for a pinned commit;
5. verify that live provider/model wiring remains absent or separately governed;
6. perform human adoption review after evidence is accepted.

## Non-equivalence rules

```text
repository observed != binding adopted
implementation present != governance evidence accepted
README statement != reproduced behavior
commit subject != CI evidence
test exists != test passed at reviewed SHA
runtime success != evidence
candidate binding != activated dependency
healthy != safe
```

## Responsibility allocation

```text
Pantheon Next governs:
  classification, scope, evidence expectations, adoption, activation and rollback visibility.

External repository executes:
  bounded candidate runtime behavior when separately installed and invoked.

OpenWebUI exposes:
  future review and decision projections only.

Human approves:
  adoption, activation, real-dossier use, consequential reliance, external action and retention.
```

No import, installation, execution, activation, approval, memory promotion or external action is performed by this review.