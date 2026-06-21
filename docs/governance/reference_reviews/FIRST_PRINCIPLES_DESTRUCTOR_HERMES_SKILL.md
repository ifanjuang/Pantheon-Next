# First Principles Destructor — Hermes Skill Placement Review

Status: external reference / support review — candidate only.

Date: 2026-06-21

External source reviewed:

```text
https://github.com/reshadat/first-principles-destructor
```

Related template:

```text
templates/hermes/skills/first-principles-assumption-review/SKILL.md
```

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## What it is

`first-principles-destructor` is an external AI-agent skill / prompt pattern. It strips a statement, process, business model or belief into hidden assumptions, searches for a reality floor, estimates convention tax, tests assumption removal, rebuilds from surviving constraints and asks why the rebuilt version does not already exist.

It is not an execution tool. It does not call systems, crawl sources, write files, operate a connector or produce deterministic proof.

## Initial qualification

Accepted:

```text
as a Hermes-side analytical skill candidate;
as a critique lens for hidden assumptions, tool drift and governance scope creep;
as a producer of Assumption Review Candidates;
as a producer of Evidence Pack Candidates when sources are supplied or retrieved under a separate authorized handoff.
```

Refused:

```text
as Pantheon doctrine;
as Zeus arbitration;
as proof;
as approval;
as professional validation;
as canonical memory;
as repository mutation authority;
as a domain-pack method source.
```

To verify:

```text
whether the adapted template gives enough structure for repeatable reviews;
whether outputs remain disciplined under pressure to be contrarian;
whether the skill reliably separates regulatory, contractual, professional and organizational assumptions;
whether it can emit useful capability_gap_signal objects instead of over-answering.
```

To arbitrate:

```text
whether this should become a standard review angle for major Pantheon proposals;
whether architecture-domain use should require an architecture-specific review appendix before client-facing use.
```

## Placement

```yaml
module_manifest_candidate:
  id: first-principles-assumption-review
  owner_layer: execution_runtime
  type: skill
  status: candidate
  activation:
    state: candidate
    scope: task
  task_authorization:
    state: unauthorized_by_default
  interface:
    allowed_inputs:
      - statement
      - belief
      - process
      - workflow
      - product_idea
      - doctrine_candidate
      - method_candidate
    allowed_outputs:
      - assumption_review_candidate
      - evidence_pack_candidate
      - capability_gap_signal
    forbidden_outputs:
      - truth_final
      - approval_final
      - memory_promotion
      - doctrine_change
      - external_action
      - professional_validation
      - direct_repo_mutation
  governance:
    consequential: true
    risk_level: medium
    approval_behavior: candidate_only
    memory_behavior: never_canonical
    scope_behavior: task_scope_only
```

## Why it is useful

The skill is useful because Pantheon work repeatedly faces the same failure mode: a candidate capability starts as a tool feature, then quietly becomes a governance rule, memory authority, proof mechanism or approval surface.

A first-principles assumption review can expose those hidden moves early.

Examples:

```text
“Pantheon needs a data platform.”
“Crawl4AI output can feed RAG directly.”
“Graph connectivity can show proof.”
“A Hermes skill is safe because it is installed.”
“A Revit plugin preview list is effectively an approval queue.”
```

The useful output is not the rebuilt idea itself. The useful output is the separation between:

```text
what is necessary;
what is only convention;
what needs evidence;
what needs approval;
what must stay outside Pantheon.
```

## Specific correction made during adaptation

The external `SKILL.md` front matter currently exposes a YAML error because `Trigger phrases:` is written as an unquoted/non-normalized key in the metadata block. The Pantheon template rewrites the metadata as valid YAML and places trigger phrases under:

```yaml
activation:
  trigger_phrases:
```

## Boundary note

The template in `templates/hermes/skills/first-principles-assumption-review/` is intentionally non-executable inside this repository.

Actual runnable Hermes skills must live outside Pantheon Next or in a separately governed runtime repository. If copied into Hermes, the copy must declare the target Pantheon contract / manifest version and remain subject to skill admission, preflight and per-task authorization.
