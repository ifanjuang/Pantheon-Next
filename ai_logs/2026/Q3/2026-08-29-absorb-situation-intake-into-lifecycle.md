# Governance cleanup — absorb Situation Intake into Request Lifecycle — 2026-08-29

## Objective

Continue #787 from exact `main` `1d5815c5a850fed110a3d94d69d26749107dc8c7` by removing `DOSSIER_SITUATION_INTAKE.md` as an independent active-support owner after proving that its remaining responsibility is a bounded request-lifecycle specialization.

The useful intake contract is preserved in the indexed mother owner `REQUEST_LIFECYCLE.md`; the standalone example and repeated boundary material are not duplicated.

## Repository checks

Before completing the absorption:

- `main` was still `1d5815c5a850fed110a3d94d69d26749107dc8c7` (merge of #805);
- no open PR overlapped the scope;
- #787 remained open;
- the partial branch was exactly five-file bounded after completion;
- the authority-index rewrite was inspected by patch and changed only the `REQUEST_LIFECYCLE.md` / `DOSSIER_SITUATION_INTAKE.md` rows plus an EOF normalization;
- exact-file search on `main` found active direct references only in `docs/governance/README.md` and `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`; the other exact-file hit was historical ai_log provenance;
- `WORKFLOW_FORGING_PROTOCOL.md` consumes the compatibility identifier `dossier_situation_brief_ref` but did not depend on a separate executable intake owner.

## Decision test

Question from #787:

> If all rules already owned elsewhere are removed from this file, does enough distinct normative responsibility remain to justify an independent owner?

For `DOSSIER_SITUATION_INTAKE.md`, the answer is no.

Its distinct material was limited to:

```text
Case / Situation terminology at intake
intake as a function rather than a Role
minimum documentary Case / Situation brief
intake status vocabulary
handoff condition before Approach / Workflow Candidate forging
```

These responsibilities are part of the request lifecycle boundary and do not require a separate authority lifecycle, schema, runtime, persistence or decision owner.

## Mother owner

`REQUEST_LIFECYCLE.md` already owns:

```text
request triage
cap clarification and re-evaluation
proportional activation
request decomposition
status arbitration
consequential chokepoints
```

It now also owns the documentary Case / Situation intake brief used when situated comprehension must cross into Approach selection or Workflow Candidate forging.

## Preserved compatibility vocabulary

The absorption deliberately retains:

```text
dossier_situation_brief
dossier_situation_brief_ref
```

These are documentary compatibility identifiers only. New explanatory text reads them as `Case / Situation brief`.

This preserves existing Workflow Candidate examples without treating a filesystem folder/dossier as governed identity.

## Content preserved

The mother owner retains:

- `Case / Affaire` = governed professional unit;
- `Situation` = concrete question or tension;
- `Corpus` = document set;
- folder/dossier storage != governed Case identity;
- intake composes IRIS, ATHENA, ARGOS, THEMIS, APOLLO, ZEUS and HEPHAISTOS viewpoints without creating a new Role;
- the minimum documentary brief shape;
- `ready_for_workflow_candidate`, `pending_clarification`, `pending_source`, `pending_contract_scope`, `risk_review_required`, `zeus_arbitration_required` and `blocked` intake statuses;
- the rule that the brief remains candidate material and does not itself authorize execution, Evidence admission, Registre mutation, memory promotion or professional validation.

## Content intentionally not duplicated

The standalone ERP/effectif example in the satellite is not copied into the mother owner because the repository already contains the richer example:

`docs/examples/architecture_erp_effectif_impact_workflow/`

Git history preserves the removed file verbatim.

## Reference migration

Active references are converged as follows:

```text
docs/governance/README.md
  DOSSIER_SITUATION_INTAKE.md
  -> REQUEST_LIFECYCLE.md

docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md
  independent intake row removed
  -> REQUEST_LIFECYCLE.md row expanded with Case / Situation intake ownership

WORKFLOW_FORGING_PROTOCOL.md
  Case / Situation Intake
  -> Case / Situation intake brief (`REQUEST_LIFECYCLE.md`)
  Dossier Situation Brief
  -> Case / Situation brief with compatibility identifier `dossier_situation_brief`
```

Historical ai_logs are intentionally unchanged.

## Authority impact

One indexed active-support owner is removed because its responsibility is absorbed into an existing indexed active-support owner.

No authority class is promoted. `REQUEST_LIFECYCLE.md` remains active support doctrine. No Role, Gate, runtime, approval, Evidence, persistence or Registre authority changes.

## Runtime impact

None.

No executable schema, runtime, scheduler, queue, router, client, Hermes Skill, connector, PDP/PEP path, Cockpit behavior, memory engine or external action is introduced.

## Quantitative convergence

Before this ai_log, compare against exact base showed:

```text
DOSSIER_SITUATION_INTAKE.md              removed: -236
REQUEST_LIFECYCLE.md                     +110 / -5
README.md                                 +2 / -2
WORKFLOW_FORGING_PROTOCOL.md              +2 / -2
GOVERNANCE_AUTHORITY_INDEX.md             +2 / -3
```

Net current governance-document reduction: approximately 132 lines plus one standalone file and one independent authority-index row removed.

This is not verbatim relocation; the existing richer ERP example and generic boundaries are not duplicated.

## Preserved invariants

```text
folder/dossier != governed identity
intake brief != Evidence
intake status != authorization
runtime success != authorization
memory != Evidence
runtime memory != Registre Probatoire
projection != persistence
PDP decision != PEP execution
method doctrine != runtime workflow
owner absorption != authority promotion
```

## Verification rule

The final PR must pass Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on its exact final HEAD. The patch, active-reference integrity, reviews, threads and comments must be read before merge. Any later HEAD change invalidates earlier check evidence.
