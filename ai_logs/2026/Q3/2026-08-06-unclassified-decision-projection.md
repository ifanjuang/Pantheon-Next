# Unclassified Decision projection boundary

Date: 2026-08-06
Scope: Decision Request classification and Cockpit projection

## Observed ambiguity

The initial Decision Request contract allowed `project_ref` to be null but did
not state how the global Decisions space differs from Project projections. The
MVP branch consequently loaded all pending requests into a global collection and
also projected Project-bound requests under their Project. The WorkIssue scope
resolver additionally anticipated an `agency_decisions` owner that does not
exist.

## Decision

There is no `agency_decision` entity or authority.

```text
project_ref = null
-> request is unclassified
-> eligible for the global Decisions attention space

project_ref = <project>
-> request is classified
-> projected only under that matching Project
```

Both views retain the same Decision Request identity. Resolving a request creates
a separate canonical `decision_record`. A WorkIssue scope of type `decision`
therefore targets a `decision_record`, never an agency-level Decision object.

## Boundaries

```text
global Decisions space != agency Decision authority
unclassified != agency-owned semantic type
project classification != duplicate request
Decision Request != decision_record
Decision recorded != WorkIssue transitioned
```

No runtime, scheduler, automatic approval, Project mutation, Evidence admission
or memory promotion is introduced.
