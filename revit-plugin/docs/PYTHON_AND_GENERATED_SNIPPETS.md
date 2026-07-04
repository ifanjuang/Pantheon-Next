# Python and Generated Snippets

Status: support policy candidate — documented non-implemented.

This document defines the role of Python and generated snippets around the future Revit plugin.

It does not implement Python tooling, a Revit add-in, an execution bridge or runtime behavior.

## Core rule

```text
C# / .NET 10 is the future Revit add-in core.
Python is support tooling only.
Generated snippets are candidate references only.
```

## Allowed Python support uses

```text
validate sample context packs;
summarize JSONL logs;
mock Hermes responses;
convert logs to Markdown or HTML reports;
prepare static test data;
stage generated snippets as reference material.
```

## Disallowed role

Python must not become the primary Revit plugin core for this adapter path.

Python must not be treated as the source of Revit governance authority.

Python must not bypass the future C# Revit-controlled path.

## Generated snippets

Snippets from assistants, RevitApiDocs Code, Dynamo examples, forums or other sources may help exploration.

They remain candidate references until reviewed, tested and manually promoted.

## Promotion path

```text
candidate snippet
-> source and date recorded
-> manual review
-> test on safe material
-> rewritten or wrapped in controlled implementation if useful
-> capability status updated separately
```

## Boundary

```text
Python may support.
Python may summarize.
Python may validate static samples.
Python may not decide approval.
Python may not replace the Revit add-in core.
```
