# AI log — Capability Registry review feedback fix

Date: 2026-06-08

## Context

After #88 merged, automated review comments and the earlier Claude coordination review surfaced two concrete inconsistencies:

- `docs/governance/CAPABILITY_REGISTRY.md` declared itself `active support doctrine` while `AUTHORITY_INDEX.md` indexed it as `candidate / to verify`.
- The new registry used the accented `HÉPHAÏSTOS` spelling, while `GLOSSARY.md` owns `HEPHAISTOS` as the canonical token.

Claude's earlier coordination review also warned that the governed-composition keystone should not turn `RETAIN` into an automatic canonical recipe library, and that proof vocabulary must remain aligned with the Registre Probatoire rather than implying final truth.

## Change made

Updated `docs/governance/CAPABILITY_REGISTRY.md` only:

- header aligned to `candidate / to verify`;
- added explicit candidate posture section;
- replaced `HÉPHAÏSTOS` with canonical `HEPHAISTOS`;
- softened `proof` language into `evidence support`, `probative support`, and Evidence Pack Candidate expectations;
- clarified that review may promote declarations, but enrichment never auto-promotes;
- kept the SkillsGate-informed skill admission guard intact.

## Decision posture

Accepted:

```text
Align file header with AUTHORITY_INDEX.md.
Use canonical HEPHAISTOS token.
Keep the registry candidate-first.
Keep SkillsGate skill admission as generic MCP / skill-manager boundary.
```

Refused:

```text
Do not promote the registry to active support doctrine yet.
Do not add runtime, schema, tests, operations, platform, Docker or environment changes.
Do not make retained recipes canonical by success alone.
```

To verify:

```text
Whether remaining references in CHANGELOG.md / ai_logs should be normalized in a separate cleanup, or left as historical trace text.
Whether WORKFLOW_SCHEMA.md should receive a follow-up wording pass for HEPHAISTOS token and proof vocabulary.
```

## Boundary

Documentation-only correction. No runtime, MCP server, skill manager, schema, test or protected-path change.
