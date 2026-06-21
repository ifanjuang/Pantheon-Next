# AI Log — Architecture Source Policy

Date: 2026-06-16  
Actor: ChatGPT  
Branch: `chatgpt/architecture-source-policy`  
Scope: candidate support doctrine / documented non-implemented

## Task

Continue after PR #151 and distill the first accepted architecture-domain slice: Architecture Source Policy.

The goal is to define how sources are classified, checked, bounded and attached to architecture-domain outputs before they can support claims, drafts, Evidence Pack Candidates or future Register Candidates.

## Files added

```text
docs/governance/ARCHITECTURE_SOURCE_POLICY.md
ai_logs/2026-06-16-architecture-source-policy.md
```

## Sources read

Current Pantheon Next canonical/support sources:

```text
docs/governance/STATUS.md @ 7611a9145df4ba625a760ff1454ec7a4810774ce
docs/governance/MODULAR_DOMAIN_REORIENTATION.md @ d3e1bdcb9f9e5030e40aae900a814db854597bf6
docs/governance/CAPABILITY_PLACEMENT.md @ 331a727ccc4ebe04cb74dbb1a0753e5586da4fde
docs/governance/DOMAIN_PACK_SPEC.md @ f900f42a82ba47c1444bc11561d772f8fad1fb33
docs/governance/ARCHITECTURE_OS_RECONCILIATION.md @ f7701e80e9eb6f5645a44751dc2c0bcb4aa420f8
```

Repository checks:

```text
Open issues searched for architecture source policy / freshness / architecture_fr.
Open PRs searched for architecture source policy / freshness / architecture_fr.
Repository file search run for existing architecture source policy material.
```

Result: no open competing issue/PR found and no equivalent existing document found under the searched terms.

## Changes made

Added `ARCHITECTURE_SOURCE_POLICY.md` as candidate support doctrine.

The document defines:

```text
source states
source authority classes
fetch-before-cite rule
freshness and supersession rule
project-source priority
claim type minimum support
contradiction handling
Evidence Pack Candidate expectations
output status discipline
external communication source rule
forbidden collapses
safe fallback
relationship to future ARCHITECTURE_DOMAIN_PACK_SPEC.md
```

## Boundary

No runtime created.
No OpenWebUI configuration created.
No Hermes skill created.
No schema created.
No tests created.
No operations file created.
No platform file created.
No Docker or environment file touched.
No automatic source validator created.
No doctrine promoted to canonical.

## Protected path check

Not modified:

```text
schemas/
tests/
operations/
platform/
Docker files
.env files
pyproject.toml
CLAUDE.md
```

## Repository state

Documented non-implemented.

Candidate support doctrine.

## Next safe actions

1. Open a PR for review.
2. Verify diff only touches `docs/governance/` and `ai_logs/`.
3. If accepted, use this source policy as input for the future `ARCHITECTURE_DOMAIN_PACK_SPEC.md`.
4. Later, open a separate PR for `ARCHITECTURE_OUTPUT_FORMATS.md`.
