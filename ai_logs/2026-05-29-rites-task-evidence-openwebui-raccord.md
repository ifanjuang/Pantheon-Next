# 2026-05-29 - Rites raccord to Task Contracts, Evidence Packs and OpenWebUI

## Summary

Connected the Rites governance layer to the three surrounding governance surfaces:

- `docs/governance/TASK_CONTRACTS.md`
- `docs/governance/EVIDENCE_PACK.md`
- `docs/governance/OPENWEBUI_INTEGRATION.md`

## Changes

`TASK_CONTRACTS.md` now states that a Task Contract may recommend or require a rite as bounded governance context.

The Task Contract still cannot execute, schedule, trigger or automate the rite.

`EVIDENCE_PACK.md` now states that an Evidence Pack may record rite-related governance evidence, such as trigger reason, roles called, tensions, ZEUS status, User Decision Gate impact and memory impact.

The Evidence Pack must not store hidden chain-of-thought, raw role debate, runtime state or automatic approval state.

`OPENWEBUI_INTEGRATION.md` now states that OpenWebUI may display rite proposals, rite status and rite review notes as cockpit surfaces.

OpenWebUI must not execute rites, trigger rites automatically, treat rite completion as approval or convert rite output into Canonical Memory.

## Boundary

This pass is documentation-only.

It does not implement:

- rite runtime;
- automatic rite trigger engine;
- hidden rite debate loop;
- scheduler;
- queue;
- OpenWebUI function, tool, pipe, filter, action or pipeline;
- Hermes skill installation;
- automatic approval;
- automatic memory promotion.

## Changelog note

A `CHANGELOG.md` update was attempted but the file changed concurrently with a new `0.1.15` RAG reconciliation entry.

The changelog was not force-rewritten in order to avoid overwriting parallel work.

A future micro-pass should add a dedicated changelog entry for this rites raccord if no concurrent changelog update is in progress.

## Final rule

A Task Contract may recommend a rite.

An Evidence Pack may summarize a rite.

OpenWebUI may display a rite.

None of these executes the rite.
