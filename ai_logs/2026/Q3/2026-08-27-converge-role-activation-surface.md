# Converge role/domain/skill activation surface

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: role/domain/skill activation doctrine
Change level: semantic

## Objective

Remove the historical OpenWebUI-specific activation/display path and reduce duplicated activation doctrine without removing the useful role, domain and skill eligibility controls.

## Observed state

After #772 aligned canonical `AGENTS.md`, `ROLE_ACTIVATION.md` still declared `OpenWebUI exposes`, contained `openwebui_template_pack`, projected a separate OpenWebUI display status vocabulary, stored `openwebui_templates` in the domain example and owned dedicated OpenWebUI exposure/template sections. The document also repeated extensive profession/skill examples already owned by domain, capability, Task Contract, Evidence and Register documents.

## Change

- align the operating boundary to Hermes clients, Hermes Agent, Pantheon Cockpit and Pantheon governance;
- retain role participation statuses, domain states, skill eligibility states and mandatory role triggers;
- retain the distinction between eligibility, task authorization, approval and retention authorization;
- remove the client-specific template activation class and display-state owner;
- route runtime-facing presentation to existing client owners and governed projection to Cockpit/Card owners;
- reduce duplicated domain/skill examples to bounded contract shapes and references to existing owners;
- preserve MNEMOSYNE retrieval/retention boundary and Hermes external-execution admission requirements;
- add targeted regression tests.

The large reduction is deliberate and is acknowledged in `.github/scripts/truncation_ack.txt`. Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
role active != agent started
domain enabled != professional authority
skill eligible != task authorized
task authorized != approved
activation != retention authorization
projection != persistence
client selected != governance authority
memory != Evidence
```

## Exit criteria

- no active OpenWebUI owner remains in `ROLE_ACTIVATION.md`;
- role/domain/skill eligibility capabilities remain represented;
- no new runtime, UI, registry or activation owner is introduced;
- Governance CI, Architecture Audit and Obsolete Authority checks are green on the exact PR head.
