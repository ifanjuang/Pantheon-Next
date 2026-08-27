# Converge Evidence Topology authority

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: Evidence Topology doctrine and examples
Change level: semantic

## Objective

Replace the concatenated historical Evidence Topology document with one current authority that matches the repository's implemented schema contract and current Hermes/Cockpit responsibility split.

## Checks before change

The complete `docs/governance/EVIDENCE_TOPOLOGY.md` was read through EOF before modification. It contained active doctrine plus bridges, checklist, roadmap addendum, reconciliation note, a schema-candidate note and a historical changelog addendum. Those layers repeated the same rules, retained OpenWebUI ownership and contradicted one another about whether topology fields were merely candidates or already implemented.

Current `schemas/task_contract.schema.yaml` and `schemas/evidence_pack.schema.yaml` were then read from `main`. They confirm that `reasoning_topology`, `evidence_items`, `handoff_artifacts` and `reasoning_topology_record` already exist as optional governance metadata, with `topology_dispatch: false`. The active example README was also checked and found to retain historical OpenWebUI/non-schema wording. No open parallel PR covered Evidence Topology.

## Change

- retain one current Evidence Topology doctrine focused on proof-chain preservation and topology selection;
- retain all seven topology enum values already owned by the schemas;
- preserve Evidence Item, Handoff Artifact and topology-record semantics;
- make the Task Contract/schema boundary explicit and current rather than future/candidate;
- preserve Hermes execution, scope/tool, memory, Governance College and User Decision Gate boundaries;
- replace OpenWebUI exposure ownership with replaceable Hermes runtime interaction plus Pantheon Cockpit governed projection;
- update the active fictional example README to acknowledge current schema validation without confusing conformance with Evidence sufficiency;
- remove obsolete concatenated roadmap/bridge/reconciliation/schema-candidate/changelog layers from the active owner; Git history retains them;
- acknowledge the deliberate large reduction in the truncation registry;
- add targeted regression tests.

Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
retrieved != truth
worker output != conclusion
runtime topology != governance authority
handoff != approval
runtime state != Pantheon memory
memory != Evidence
projection != persistence
schema conformance != Evidence sufficiency
```

## Exit criteria

- current doctrine contains no OpenWebUI dependency or stale schema-candidate layer;
- machine fields remain owned by current schemas and topology dispatch remains false;
- examples describe the current contract honestly;
- no runtime, dispatcher, scheduler, swarm controller or authority path is added;
- CI/review are green on the exact PR head before merge.
