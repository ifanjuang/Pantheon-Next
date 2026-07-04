# Revit Knowledge Source Policy

Status: support policy candidate — documented non-implemented.

This document defines how a future Hermes Revit reference skill may use documentation and external references.

It does not implement RAG, vector search, web browsing, a Hermes skill, a database, an indexer or runtime behavior.

## Core rule

Hermes may use reference material to propose a method candidate.

Reference material does not authorize a Revit model change.

```text
reference retrieval
-> method candidate
-> preflight / preview / validation
-> Revit-controlled execution path if approved
```

## Source authority levels

```text
A0 real Revit state observed by plugin
A1 Autodesk official documentation
A2 Revit API reference / RevitApiDocs
A3 IFJ / Pantheon validated internal notes
A4 tested internal recipes
A5 forums / blogs / GitHub discussions
A6 generated or untested snippets
```

A0 describes the current model state.

A1 and A2 are strong technical references.

A5 and A6 are candidate-only.

## Hermes Revit Reference skill

A future skill may use a local vectorized corpus.

Recommended first topics:

```text
transactions
ExternalEvent
selection
FilteredElementCollector
ElementId
Parameter
FamilySymbol / FamilyInstance
TextNote
DetailLine / CurveElement
View / ViewPlan
Worksharing
Pinned elements
Groups
Linked models
Failure handling
```

The vector index should live outside Pantheon unless explicitly promoted as a repository artifact.

Pantheon should define source policy and metadata expectations only.

## Web and forum search

Hermes may use web or forum results as exploration when local references are insufficient.

Those results remain candidate-only unless reviewed and promoted.

## Reference Pack Candidate

A reference query should produce a reviewable pack, not an action.

```json
{
  "question": "How to create a text note in Revit?",
  "revit_version": "2027",
  "sources": [
    {
      "authority_level": "A1",
      "title": "Autodesk Revit API documentation",
      "url_or_local_ref": "redacted-or-local-reference",
      "relevance": "high"
    }
  ],
  "method_candidate": {
    "summary": "Use a Revit-controlled path and a named transaction.",
    "api_classes": ["Transaction", "TextNote"],
    "warning_hint": "W2",
    "requires_preflight": true,
    "requires_validation": true
  },
  "execution_allowed": false
}
```

## Metadata expectations

Each indexed chunk should preserve:

```text
source id;
authority level;
source type;
Revit version;
retrieval date;
content hash;
API namespace/class/member when known;
operation kind;
warning hint;
source URL or local reference.
```

## Boundary

```text
The plugin observes current Revit state.
Hermes retrieves and proposes.
The Revit plugin preflights and executes only through its controlled path.
Pantheon governs status, proof, approval, scope and memory.
```
