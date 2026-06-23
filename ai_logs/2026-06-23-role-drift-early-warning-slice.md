# AI Log — Role Drift Early Warning Slice

Date: 2026-06-23  
Actor: ChatGPT  
Scope: template / examples / documented non-implemented

## Task

The user asked to build an example to prevent situations similar to prior `_maf` and `_affaires` project discussions: early identification of role drift, reminders of the architect's role, reminders to contractors, and reminders to project owners.

The user also requested legal prudence angles, MAF recommendations, and anonymized examples with dates and sources to verify before use.

## Active doctrine read

Read before creating files:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
```

Relevant boundaries:

```text
Pantheon Next is governance-first and not a runtime.
Retrieval is not proof.
Task success does not mean truth, proof, memory or professional validation.
Domain packs define vocabulary, source policy, evidence expectations, risk triggers, output statuses and delivery gates.
Templates instantiate doctrine; they do not govern or execute by themselves.
```

## Files added

```text
templates/architecture_probative_instruction/role_drift_early_warning_slice/README.md
templates/architecture_probative_instruction/role_drift_early_warning_slice/early_warning_matrix.md
templates/architecture_probative_instruction/role_drift_early_warning_slice/source_completion_pack.md
templates/architecture_probative_instruction/role_drift_early_warning_slice/output_structures.md
templates/architecture_probative_instruction/role_drift_early_warning_slice/professional_risk_review_layer.md
templates/architecture_probative_instruction/role_drift_early_warning_slice/examples/anonymized_role_drift_evidence_tree_candidate.md
```

## Note on blocked file

A ready-to-send wording file was attempted but blocked by the connector safety controls. It was replaced by `output_structures.md`, which defines candidate output shapes without ready-to-send text.

## Public references used

```text
MAF — devoir de conseil
MAF — défaut d'exécution sur chantier
MAF — défaillance d'entreprise
MAF — coût des travaux
MAF — synthèse chantier
MAF — périmètre d'intervention
MAF — déclaration de sinistre
Conseil d'Etat — 22 December 2023 — no. 472699
Conseil d'Etat — 10 December 2020 — no. 432783
Cour de cassation — 3 February 1999 — no. 97-13.427
```

These sources are treated as review references and caution signals, not automatic rules or legal advice.

## Accepted

```text
- Create a new candidate-only role-drift slice.
- Keep examples anonymized.
- Use `_maf` and `_affaires` patterns as context candidates only.
- Add a professional-risk review layer based on public MAF / case-law references.
- Keep all outputs gated and non-transmissible without human review.
```

## Refused

```text
- No legal advice.
- No insurer advice.
- No claim declaration.
- No admission.
- No external email sent.
- No canonical project record created.
- No proof-register entry created.
- No runtime, schema, tests, operations, platform, Docker, .env or pyproject change.
```

## To verify

```text
- exact project source files for any real use;
- exact dates;
- mission contract and amendments;
- contractor markets / quotes;
- site reports;
- reception / reserve status;
- payment history;
- whether senior legal / insurer review is required.
```

## Repo state

Documented non-implemented.

Candidate templates and examples only.
