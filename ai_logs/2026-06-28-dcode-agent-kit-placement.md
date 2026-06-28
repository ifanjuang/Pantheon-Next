# AI log — dcode-agent-kit placement review

Date: 2026-06-28

Status: documented non-implemented.

Branch:

```text
docs/dcode-agent-kit-placement
```

## Trigger

User shared:

```text
https://github.com/EliaAlberti/dcode-agent-kit
```

and approved the proposed classification as a candidate external reference for skill / capability scaffolding rather than Pantheon doctrine.

## Source documents read

Canonical / active repository posture:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
```

Specialized documents consulted:

```text
docs/governance/COMPETENCE_MODEL.md
docs/governance/CARD_STACK_MODEL.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/README.md
```

External repository reviewed:

```text
https://github.com/EliaAlberti/dcode-agent-kit
skills/new-dcode-agent/SKILL.md
reference/deepagents-guide.md
```

Coordination reviewed:

```text
open issues around capability / skill / card placement, including #118 and #135;
open PR #190 for the New Capability Effect Review candidate rite;
open PR #232 for card-stack reconciliation questions;
open PR #233 for method-card model candidate.
```

## Decision

Accepted:

```text
dcode-agent-kit is useful as an external reference for bounded agent / skill scaffolding.
The valuable pattern is interview -> spec -> confirmation -> scaffold -> smoke-test.
The approval-gate lesson is useful for runtime posture checks.
The card-stack implication should be captured as Capability Candidate / Skill Candidate vocabulary.
```

Refused:

```text
No dcode-agent-kit dependency is added.
No Claude Code plugin is installed.
No Deep Agents runtime is added.
No dcode CLI agent is created.
No Hermes skill generator is implemented.
No Pantheon runtime, skill installer, approval engine, memory engine, scheduler, queue, provider router or external action is added.
No AGENTS.md or generated agent identity is treated as Pantheon Role authority or Registre Probatoire.
```

To verify:

```text
whether existing SKILL_LIFECYCLE and CAPABILITY_PLACEMENT already cover the full admission path;
whether the card-stack model should gain a Capability Candidate / Skill Candidate sub-card section;
whether smoke-test observations should become a standard Evidence Pack Candidate component for capability admission;
whether a Hermes-side scaffold template is useful enough to draft later outside the kernel.
```

To arbitrate:

```text
whether future card-stack changes should wait for PR #232 and PR #233 reconciliation;
whether New Capability Effect Review from PR #190 should become the default rite for high-risk skill admission;
whether generated runtime skills should enter through CAPABILITY_REGISTRY, SKILL_LIFECYCLE, or a narrower candidate-card review.
```

## Files added

```text
docs/governance/reference_reviews/DCODE_AGENT_KIT_HERMES_SKILL_SCAFFOLDING_REVIEW.md
ai_logs/2026-06-28-dcode-agent-kit-placement.md
```

## Files deliberately not changed

```text
docs/governance/CARD_STACK_MODEL.md
```

Reason: the file already exists as candidate support doctrine and open PRs are actively discussing card-stack / method-card reconciliation. The review records the proposed card vocabulary without silently applying it to the cockpit model.

## Repo state

Documented non-implemented.

The new reference review is covered by the grouped `docs/governance/reference_reviews/` row in `AUTHORITY_INDEX.md`. No individual authority-index row was added to avoid duplicate indexing.

No protected path was modified. No schema, test, operation, platform file, Docker file, `.env`, `pyproject.toml` or `CLAUDE.md` was touched.

The validated remains.
