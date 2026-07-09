# Template model and prompt templates

Date: 2026-07-08

Status: validation-only trace — documented non-implemented.

## Context

A review considered whether external prompt collections could inspire Pantheon / Hermes templates without becoming governance authority, runtime material, dependency, knowledge corpus or prompt ingestion source.

The repository boundary was checked before modification:

- `README.md`
- `docs/governance/STATUS.md`
- `docs/governance/WHAT_RUNS.md`
- `docs/governance/AUTHORITY_INDEX.md`
- `docs/governance/MODULES.md`
- `docs/governance/README.md`
- `templates/README.md`
- `templates/TEMPLATE_REGISTRY.md`

## Change

Added a non-executable template discipline file:

- `templates/TEMPLATE_MODEL.md`

Added a non-executable prompt template group:

- `templates/prompt_templates/README.md`
- `templates/prompt_templates/evidence_extraction.template.md`
- `templates/prompt_templates/dce_review.template.md`
- `templates/prompt_templates/visa_review.template.md`
- `templates/prompt_templates/client_email.template.md`
- `templates/prompt_templates/decision_record.template.md`

Updated local template visibility:

- `templates/README.md`
- `templates/TEMPLATE_REGISTRY.md`

## Rationale

Prompt templates are useful as reusable execution contracts: they define role, scope, source hierarchy, uncertainty handling, allowed outputs, forbidden outputs and human validation points.

They should remain candidate support material, not implementation.

## Boundary kept

```text
Template does not mean implementation.
Prompt template does not mean deployed system prompt.
Draft does not mean signed position.
Runtime success does not mean evidence.
Candidate does not mean approval.
```

Pantheon governs template status and consequence.
Hermes may execute from a template only under bounded Task Contract.
OpenWebUI may expose forms or prompt surfaces.
The human validates consequential output.

## External inspiration rule

External prompt collections may inspire abstract prompt architecture patterns only.

Forbidden:

- raw ingestion;
- verbatim reuse;
- vectorization as knowledge;
- skill derivation from proprietary prompts;
- dependency adoption;
- automatic update;
- treating external prompts as authority.

## Risks / limitations

The new files are not tested implementation.
They do not create schemas, runtime checks, OpenWebUI assets, Hermes skills or MCP behaviour.

Further work may add more professional templates, but each must keep the same non-executable status unless explicitly promoted through the authority and review path.
