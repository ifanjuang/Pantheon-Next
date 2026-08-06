# WorkIssue scope contract

Date: 2026-08-06
Status: contract candidate implemented in schema, runtime implementation pending.

## Observed state

`WorkIssue` already owns task identity, lifecycle, comments, admitted Hermes runs and material events. Its first persistence slice carries one `case_ref` and one optional `primary_card_ref`, while the accepted Cockpit roadmap requires the same Tâche identity to appear in several relevant contexts and also permits agency work without a Project.

The generic EntityRef relation carrier is not widened for this purpose. Its four relation meanings remain Information semantics. A Tâche that concerns an object is scope, not `responds_to`, `relies_on`, `supersedes` or `contradicts`.

## Decision

Add an aggregate-owned `WorkIssueScopeLink` contract:

```text
WorkIssue
-> scope_role
-> EntityRef
```

Closed endpoint vocabulary:

```text
agency
project
information
decision
person
organization
apu_object
```

The contract reserves Decision and APU endpoints for their reviewed owner tranches. An executable adapter must resolve endpoint existence when an owner exists, allow only one active primary scope per WorkIssue, keep active entity links unique and retire links instead of deleting history.

## Boundaries

```text
scope link != semantic relation
scope visible != Context Pack widened
scope linked != task authorized
same WorkIssue projected twice != duplicate WorkIssue
agency scope != Project invented
retired scope != history deleted
```

No runtime, scheduler, queue, provider router, automatic approval, Evidence admission, memory promotion or Project mutation is introduced.
