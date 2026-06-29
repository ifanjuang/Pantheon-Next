# AI Log — Architecture Method Run Tests

Date: 2026-06-29

Actor: ChatGPT

## Context

After the Method Card and cockpit reconciliation work moved to PR #237, a follow-up discussion focused on practical use and optimization.

The conclusion was that the next useful artifact should not be another abstract model. It should be a run-test document that checks whether Method Cards, Hermes handoff discipline and cockpit visibility reduce professional confusion in real architecture-agency cases.

## Change made

Created:

- `docs/governance/ARCHITECTURE_METHOD_RUN_TESTS.md`

The document defines three architecture-domain run tests:

- chantier report production;
- complementary quotation review;
- CERFA / administrative filing preparation.

Each test includes:

- user intent;
- professional risk;
- expected candidate;
- forbidden final effects;
- thresholds;
- initial task chain;
- failure signal;
- Method Proposal Candidate;
- executable Hermes handoff;
- returned candidate;
- cockpit display;
- bad path / corrected path;
- success and failure criteria.

## Design decision

The document treats run examples as operational tests, not illustrative stories.

It tests whether Pantheon can answer:

```text
Is it true?
Is it sourced?
Is it inside our mission scope?
Can it leave the cockpit?
```

It also adds a failure taxonomy so Pantheon first classifies why a task failed before asking Hermes to rerun.

## Boundary preserved

Documentation only.

No schema, test file, runtime, UI, platform, operations file, Docker file, environment file, Hermes skill, connector, approval engine, memory engine or external action was added.

The future data shape included in the document is explicitly non-schema.

## Repo state

Documented non-implemented.

The branch is separate from PR #237 to avoid conflict while that PR is being handled.

## Decision status

Accepted:

- run tests are the next useful layer after Method Cards;
- examples should function as an operational bench, not passive documentation;
- Hermes is execution runtime only, never the professional responsible role;
- gates must remain visible before consequential effects.

To verify:

- whether this document should wait until #237 merges before being opened as ready-for-review;
- whether the run tests should later be shortened or split into examples and checklists;
- whether `AUTHORITY_INDEX.md` should index this file as candidate support examples after merge.

The validated remains.
