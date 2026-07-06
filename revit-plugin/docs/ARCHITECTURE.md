# Revit Adapter Architecture

Status: planning note — documented non-implemented.

This note describes the intended adapter shape.

## Split

```text
Pantheon -> governs status, proof, scope and approval.
Hermes -> may call an adapter.
Revit adapter -> future local execution surface.
Human -> validates consequential actions.
```

## First proof target

```text
read current document context;
read active view context;
read selection context;
produce a context pack;
produce a local trace;
create light review artifacts later.
```

## Boundary

This file does not implement the adapter.
