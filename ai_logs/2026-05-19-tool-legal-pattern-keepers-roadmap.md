# Tool and Legal Pattern Keepers Roadmap Update

Date: 2026-05-19

## Summary

Updated `docs/governance/ROADMAP.md` to record additional external pattern keepers from two repository families:

- verified tool-factory patterns;
- professional verticalization and legal workflow patterns.

The update keeps the patterns as roadmap-level distillation candidates only.

It does not adopt these repositories.

It does not add dependencies.

It does not implement runtime behavior.

## Changed

Added a roadmap subsection titled `External tool and professional verticalization keepers` under Phase 1.

## Patterns kept

From verified tool-factory patterns:

- verified external tool candidates before exposure;
- proof artifacts for generated or discovered capabilities;
- dry-run defaults before write-capable tool use;
- lockfile, hash and semantic drift detection for external specifications;
- deterministic snapshot and replay for tool behavior tests;
- tool scorecards that separate technical readiness from governance approval;
- explicit non-goals for anti-bot bypass, CAPTCHA solving and terms-of-service violations;
- distinction between generated tool, verification proof, installation state, allowed use and governed approval.

From professional verticalization patterns:

- domain-specific playbooks and practice profiles;
- cold-start interview to capture professional context, house style, escalation rules and seed documents;
- draft-only output posture for regulated or liability-sensitive domains;
- explicit professional review gate before reliance, filing, publication, transmission or external effect;
- source attribution and citation verification posture;
- visible jurisdiction, scope and assumption declarations;
- conservative handling of privilege, confidentiality and subjective professional judgment;
- connector trust layer with restrictive default allowlist;
- skill QA before use or recommendation;
- install or capability log for auditability;
- freshness gate for bundled references, procedures, regulations and playbooks.

## Patterns rejected

Rejected from tool-factory patterns:

- internal Pantheon tool factory;
- MCP server or MCP router inside Pantheon;
- automatic tool generation, installation or exposure;
- automatic skill installation;
- catalog or registry treated as marketplace;
- tool availability treated as authorization;
- technical proof treated as business, professional or governance approval.

Rejected from professional verticalization patterns:

- legal or professional agents as autonomous authorities;
- scheduled agents inside Pantheon;
- managed-agent orchestration inside Pantheon;
- connector access without Task Contract scope;
- community skill marketplace;
- skill installer, recommender or auto-updater;
- professional outputs treated as advice without review;
- playbook drift promoted into doctrine or memory without governed review.

## Why

The external repositories contain useful patterns, but their architectures include runtime, plugin, connector, managed-agent and marketplace assumptions that must not be imported into Pantheon Next.

Pantheon Next must preserve the boundary:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Risks and limitations

- The roadmap entry is not an implementation plan.
- The roadmap entry is not an approval to build a Pantheon tool factory, MCP runtime, skill marketplace, legal agent suite or managed-agent orchestration.
- Future use still requires governed distillation into pattern cards, example constraints, skill QA checklists or Hermes candidate constraints.

## Files touched

- `docs/governance/ROADMAP.md`
- `ai_logs/2026-05-19-tool-legal-pattern-keepers-roadmap.md`
