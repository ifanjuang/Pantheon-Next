# AI learning repositories distillation

Date: 2026-05-29

## Summary

Added documentation-level distillation for five external AI learning repositories:

- `f/prompts.chat`;
- `dair-ai/Prompt-Engineering-Guide`;
- `anthropics/courses`;
- `microsoft/generative-ai-for-beginners`;
- `mlabonne/llm-course`.

The intervention classifies their learning value, overlap, Pantheon relevance, Hermes relevance, OpenWebUI relevance and doctrinal boundary.

## Changed files

- Added `docs/governance/AI_LEARNING_REPOS_DISTILLATION.md`.
- Added this AI log.

`docs/governance/README.md`, `docs/governance/STATUS.md` and `CHANGELOG.md` were intentionally left unchanged in the final branch because the repository had moved ahead and a first attempt revealed collision/truncation risk.

The distillation document is therefore marked as a draft support note pending governance index reconciliation.

## Rationale

The reviewed repositories are useful as external learning sources, but they must not be treated as dependencies, runtime choices, approval authorities or memory authorities.

The distillation preserves Pantheon Next's central separation:

```text
source -> retrieved knowledge -> evidence -> approval -> memory
```

It also records rejected patterns such as:

- star count as adoption signal;
- prompt persona as Pantheon Role;
- eval pass as approval;
- RAG demo as proof;
- course notebook as runtime;
- MCP example as internal connector policy.

## Boundary

This intervention is documentation-only.

It does not implement:

- runtime behavior;
- provider routing;
- scheduler or queue;
- MCP layer;
- OpenWebUI plugin, Function, Tool, Pipe, Filter, Action or Pipeline;
- Hermes skill installation;
- evaluation engine;
- RAG runtime;
- training, fine-tuning or quantization runtime;
- automatic approval;
- automatic memory promotion;
- schema changes;
- tests;
- operations tooling.

## Risks and limitations

- Repository popularity is volatile and must not be used as an approval signal.
- The document summarizes learning value and governance implications; it does not verify every lesson, notebook or commit in the source repositories.
- Provider-specific materials remain provider-specific references and do not authorize provider routing.
- Any future extraction into Pantheon doctrine, Hermes skills or OpenWebUI surfaces requires separate review and approval.
- Changelog and governance index integration should be handled in a later small reconciliation pass before activation.

## Status

Draft support note.

No external repository adopted.

No dependency added.

No runtime implemented.
