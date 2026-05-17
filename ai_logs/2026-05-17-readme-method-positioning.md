# AI Log — README method positioning

Date: 2026-05-17

## Scope

Updated the public README positioning to make Pantheon Next easier to understand for non-technical professional readers and liberal professions.

## Files changed

- `README.md`
- `README.fr.md`
- `ai_logs/2026-05-17-readme-method-positioning.md`

## Main positioning change

Pantheon Next is now described publicly as a professional method register for AI work.

French public wording:

```text
un registre de déontologie et de méthode de travail pour l’IA
```

The README explains that before an AI receives a request and produces an answer, Pantheon frames:

- which information may be used;
- what must be checked;
- what needs evidence;
- what requires approval;
- what may be kept.

## Public vocabulary change

The public README now favors simple wording:

```text
method
frame
control
traceability
reviewability
professional validation
```

French public wording now favors:

```text
méthode
cadre
contrôle
trace
relecture
validation professionnelle
```

The internal doctrine remains unchanged:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

French:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

## Model deployment section

The README now explains two possible model strategies:

1. external AI services such as ChatGPT, Claude or Gemini with private information reduced or replaced before sharing;
2. local models running on a workstation with GPU, local machine, NAS or server under a controlled environment such as Docker.

In both cases, model output remains candidate until professional validation.

## Simplification

The “What Pantheon is not” section was shortened for public readability:

```text
not a chatbot;
not an autonomous AI worker;
not an automatic memory;
not a substitute for professional responsibility.
```

## Boundary check

This intervention is README copy and positioning only.

It does not implement runtime behavior, OpenWebUI integration, Hermes integration, Evidence Pack generation, memory promotion, provider routing, plugin management or execution tooling.

## Status

Public README positioning updated.

No runtime implementation.
