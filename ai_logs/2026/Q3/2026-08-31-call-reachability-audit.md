# Symbol call reachability in the module usage audit

Date: 2026-08-31

Status: validation-only trace — implemented read-only audit extension.
Boundary profile: validation_only_trace.

## Objective

The module usage audit reported 432 modules and no unreferenced module, while
the policy chokepoint was imported everywhere and called nowhere. Import
reachability is not call reachability, and the inventory had no way to say so.

## Existing owner reused

`implementation/tools/audit_module_usage.py` already owns the question "is this
referenced?". "Is this path taken?" is the same responsibility at a finer
granularity, so the layer was added there rather than in a second tool.

## Change

- Updated: `implementation/tools/audit_module_usage.py` — a symbol layer over
  module-level functions and classes, and a `--required-call-paths` registry
  check.
- Added: `implementation/qualification/required-call-paths.json`.
- Updated: `implementation/tests/test_module_usage_audit.py`.
- Updated: `.github/workflows/implementation-architecture-audit.yml` — one flag.

## What the layer sees

Against the implementation zone today, where the module layer reports zero
unreferenced modules:

```text
symbols                            1466
never_called                          8
runtime_called_unreached             52
test_called_only                     31
```

Three of those rows are the chokepoint finding, reached mechanically rather than
by hand:

```text
policy_gate:HttpPolicyClient        test_called_only
policy_gate:governed_effect         test_called_only
capability_manager:governed_execute test_called_only
```

The only real PDP client, the wrapper that applies the gate to an effect, and
the governed capability-execution path are each constructed or invoked by tests
and by nothing else.

## Resolution limits

Call edges resolve by bare symbol name, so a call to `foo()` matches every
symbol named `foo` in the zone. This over-connects the graph, which makes
`never_called` and `runtime_called_unreached` conservative and
`entry_reachable` weak. `entry_reachable` means a chain of names reaches the
symbol — not that a deployed run takes the path, and not that the call supplies
real arguments. The semantic complement remains the assembly and inventory
tests.

Two classes of false positive were found and fixed before commit: request body
models, which appear only as route annotations, and setuptools command
subclasses, which appear only as `cmdclass` values. Counting a name mentioned
without being called took `never_called` from 105 to 8.

## The registry

Eight declared paths, pinned to what the zone does today rather than to intent.
Divergence fails in both directions, and a path declared as not taken must name
what blocks it. Three entries currently declare a dead path; when the wiring
lands, this file has to be updated deliberately instead of the change passing
unremarked.

## Boundary

Protected paths touched: `implementation/tools/`, `implementation/tests/`,
`implementation/qualification/`, `.github/workflows/` — read-only audit only.
Runtime impact: none.
Authority impact: none.
Schema/test/CI impact: the architecture audit fails when a declared path
diverges.
External action: none.
Memory behavior: none.

## Local distinctions

```text
import reachability != call reachability
module referenced   != symbol called
entry_reachable     != a deployed run takes the path
gate implemented    != gate invoked
declared dead path  != accepted dead path
audit finding       != deletion or approval authorization
```

## Next decision

The 31 `test_called_only` symbols are the surface worth reading next: each is
either a path that should be wired, a capability that is not yet in service, or
code that should go. None of that is decided by this audit.
