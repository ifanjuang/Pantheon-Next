# Boundary Standard

Status: active support doctrine — the single reference for the standard non-implementation boundary. Consolidation support; it changes no rule.

```text
Optional compatible runtime client       -> runtime interaction
Hermes Agent                             -> external execution runtime
Runtime adapter / Hermes                 -> PEP for consequential effects
Pantheon Cockpit                         -> governed Cards, status, Evidence gaps and decisions
Pantheon policy service                  -> bounded deterministic PDP interface
Pantheon Next                            -> governance, authority and PDP semantics
Human                                    -> consequential decision when required
```

## Purpose

Almost every governance document repeats the same list of effects it does not implement. That repetition is maintenance debt: when the list evolves, dozens of files drift. This document states the standard boundary once. Other documents reference it with one line and keep only their **specific** additions.

## The standard non-implementation boundary

A Pantheon Next governance document, template, schema or example does not implement and must not become:

```text
an execution engine or agent runtime
a tool runtime or tool dispatcher with implicit authority
an LLM provider router
a scheduler or internal job runner
a message bus or mandatory agent queue
an approval engine (the gate decides; the human decides)
a memory promotion engine or auto-promoted memory
a Registre Probatoire writer (entries require evidence, gate and human decision)
a connector gateway, credential store or webhook bus
a plugin manager or automatic skill installer
a hidden workflow runtime
an external action of any kind (send, write, merge, file, sign, submit)
```

This restates the non-negotiable boundaries of `CLAUDE.md` at document level; `CLAUDE.md` remains authoritative.

## How to reference it

In a new or edited document, replace the standard list with:

```text
Boundary: the standard non-implementation boundary applies — see BOUNDARY_STANDARD.md. In addition, this document specifically does not <specific items only>.
```

Keep only the items that are **specific** to the document (for example "no PDF writer" in a form-filling doctrine). Never re-list the standard items.

## Rules

1. This document is referenced, never copied.
2. A document's specific forbidden items stay in that document.
3. Existing documents are converted progressively (consolidation waves); conversion is mechanical and must not change meaning — when in doubt, keep the original wording and flag for review.
4. Changing the standard list above is a governed doctrine change (chokepoint + review), since it alters the boundary of every referencing document at once.
