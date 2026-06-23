# AI Log — Architecture Communication Pattern Taxonomy

Date: 2026-06-23  
Actor: ChatGPT  
Scope: template taxonomy / documented non-implemented

## Task

The user clarified that the Role Drift examples are starting examples only. Future examples will be created by the Pantheon collective on the fly. The user asked whether mail and letter candidates should be classified into folders and subsections.

## Change made

Added a communication-pattern taxonomy under:

```text
templates/architecture_probative_instruction/communication_patterns/
```

## Files added

```text
templates/architecture_probative_instruction/communication_patterns/README.md
templates/architecture_probative_instruction/communication_patterns/00_index/README.md
templates/architecture_probative_instruction/communication_patterns/01_client_moa/README.md
templates/architecture_probative_instruction/communication_patterns/02_contractors/README.md
templates/architecture_probative_instruction/communication_patterns/03_bet_control/README.md
templates/architecture_probative_instruction/communication_patterns/04_admin_third_parties/README.md
templates/architecture_probative_instruction/communication_patterns/05_reception_reserves_gpa/README.md
templates/architecture_probative_instruction/communication_patterns/06_role_drift_risk/README.md
templates/architecture_probative_instruction/communication_patterns/07_internal_review/README.md
templates/architecture_probative_instruction/communication_patterns/08_rejected_or_obsolete/README.md
templates/architecture_probative_instruction/communication_patterns/role_collective_routing.md
```

## Design choice

The taxonomy stores communication patterns by:

```text
recipient_class;
professional_act;
project_phase;
risk_level;
source_basis;
output_status;
external_gate.
```

The main rule is:

```text
recipient first, risk second.
```

## Accepted

```text
- Treat current examples as starting examples, not exhaustive canon.
- Allow future on-the-fly candidate generation.
- Require mandatory classification before reuse.
- Preserve anonymization and source-status gates.
- Keep rejected / obsolete wording patterns to prevent unsafe reuse.
```

## Refused

```text
- No automatic mail generation.
- No automatic external transmission.
- No legal advice.
- No final project record.
- No memory promotion.
- No runtime, schema, tests, operations, platform, Docker, .env or pyproject change.
```

## Repo state

Documented non-implemented.

Candidate template taxonomy only.
