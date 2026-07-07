# External Reference Reviews

Status: support doctrine index — reference review navigation only.

This directory contains detailed reviews of external systems before any Pantheon distillation, Hermes candidate use or OpenWebUI exposure pattern.

It does not approve dependencies.

It does not approve integrations.

It does not define runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review rule

Every external reference should be reviewed across three layers:

```text
Pantheon   -> governance distillation and forbidden imports
Hermes     -> execution candidate only, if useful and bounded
OpenWebUI  -> cockpit exposure only, not runtime authority
```

## Reviews

The detailed one-shot reviews formerly stored in this directory were removed on 2026-07-07 (governance cleanup, audit follow-up). Each remains available in git history; what survived their distillation lives in the doctrine documents (`EXTERNAL_TOOLS_POLICY.md` and the documents each review fed). The mapping is recorded in `ai_logs/2026-07-07-governance-cleanup-pass-a.md`.

New reviews follow the review rule above, are distilled promptly, and the one-shot review file is removed once its distillate lands — a review is a working document, not doctrine.

## Non-adoption rule

A review may recommend:

- watch;
- distill;
- reject;
- keep as Hermes candidate;
- expose as OpenWebUI template;
- archive.

A review must not be treated as:

- dependency approval;
- implementation approval;
- runtime migration;
- skill installation;
- provider choice;
- memory promotion;
- approval shortcut.

## Final rule

```text
Review first.
Distill only what survives the boundary.
Install nothing by implication.
```
