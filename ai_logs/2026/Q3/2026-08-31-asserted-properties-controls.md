# Every asserted property names a control

Date: 2026-08-31

Status: validation-only trace — implemented read-only governance check.
Boundary profile: validation_only_trace.

## Objective

CLAUDE.md states properties as facts about the repository. Asserting a property
is not holding it. This binds each asserted property to the control that fails
when it stops being true, and grades that control honestly.

## Change

- Added: `.github/scripts/check_asserted_properties.py`.
- Added: `.github/asserted-properties.json`.
- Added: `tests/test_asserted_properties.py`.
- Updated: `.github/workflows/governance-ci.yml` — one step.

CLAUDE.md is not modified. The check reads it; it does not ask it to change.

## What the doctrine asserts, mechanically

Two blocks are enumerable: the `!=` invariants under *Core non-equivalences*
(9 claims) and the components the governance core must not recreate under
*Non-negotiable boundaries* (12 claims).

## What the controls turn out to be

```text
behavioural    1
schema         7
documentary   11
uncontrolled   2
```

Split by claim class, the picture is not uniform:

- the 9 non-equivalences are well held — 8 of 9 by a schema contract or by
  executable code; only `repository co-location != authority transfer` rests on
  wording;
- the 12 prohibitions are held almost entirely by wording — 10 by a forbidden-
  phrase guard over `docs/governance/`, and 2 by nothing at all. Not one is held
  structurally. No check scans `implementation/` for a scheduler, a broker
  dependency, or a workflow able to merge its own change.

This corrects a coarser earlier reading of this repository's test corpus. The
invariants are better controlled than that reading suggested; it is the
prohibitions that are not.

## Why the grade is verified rather than declared

An entry declares its binding, and the check reads the control's own source to
see whether the declaration is supportable: `behavioural` needs the control to
import implementation code or parse source, `schema` needs it to validate
instances. `documentary` is the floor and is always accepted, because a
documentary control genuinely does fail — when the wording changes, not when
the property stops being true, and saying so is the point.

The grade therefore cannot be inflated. Understating it is harmless.

## What fails

```text
a property asserted in CLAUDE.md with no entry
an entry whose property CLAUDE.md no longer asserts
a control that does not exist, or does not define the test it names
a binding stronger than its control's source supports
an uncontrolled property that does not say why
more uncontrolled properties than the declared ceiling
```

The ceiling is set to the debt that exists (2), not above it.

## Boundary

Protected paths touched: `.github/scripts/`, `.github/workflows/` — read-only
validation only.
Runtime impact: none.
Authority impact: none. The registry grades controls; it promotes nothing.
Schema/test/CI impact: one CI step that fails on an unbound property.
External action: none.
Memory behavior: none.

## Local distinctions

```text
asserted        != held
documented      != controlled
wording guard   != structural detector
declared grade  != observed grade
CI green        != the property is true
```

## Next decision

Two prohibitions have no control and ten have only a wording guard. Whether that
is acceptable is a review question, not an audit finding. The two obvious
structural candidates, if it is not, are a dependency scan for a broker and a
check that no workflow can merge its own change.
