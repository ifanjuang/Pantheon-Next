# AI Log — Priority Communication Pattern Metadata

Date: 2026-06-23  
Actor: ChatGPT  
Scope: metadata templates / documented non-implemented

## Task

The user approved creating metadata files for the first priority architecture communication patterns.

## Files added

```text
templates/architecture_probative_instruction/communication_patterns/01_client_moa/PAT-COMM-0001_project_owner_role_boundary_reminder.md
templates/architecture_probative_instruction/communication_patterns/06_role_drift_risk/PAT-COMM-0003_role_chain_reminder.md
templates/architecture_probative_instruction/communication_patterns/03_bet_control/PAT-COMM-0005_pro_dce_non_exe_footer_candidate.md
```

## Rationale

These three patterns are the most structurally important:

```text
PAT-COMM-0001:
  role boundary reminder for the project owner.

PAT-COMM-0003:
  role-chain reminder across project owner / MOE / contractor.

PAT-COMM-0005:
  PRO / DCE non-EXE footer candidate for technical document status.
```

## Design choice

The metadata files do not contain ready-to-send full emails. They define:

```text
- purpose;
- metadata;
- required sources;
- required output structure;
- forbidden uses;
- human gates.
```

## Accepted

```text
- Add one metadata file per registered pattern.
- Keep patterns candidate-only.
- Preserve source review and human review gates.
- Avoid reusable wording that could be sent without context.
```

## Refused

```text
- No external mail.
- No legal advice.
- No insurer advice.
- No project record.
- No memory promotion.
- No runtime, schema, tests, operations, platform, Docker, .env or pyproject change.
```

## Repo state

Documented non-implemented.

Priority pattern metadata only.
