# Pantheon, runtime skill and organization boundary

Use this reference when creating, reviewing or changing an
organization-specific adapter for `ifja-project-context`.

## Ownership test

Ask whether a rule must remain true if Hermes, Hindsight or the current document
engine is replaced.

- If yes, Pantheon owns the invariant, authority boundary, status or gate.
- If no, but the method remains useful across organizations and bindings, the
  generic Hermes skill owns the runtime method.
- If the rule depends on current organization, source layout or available
  tools, an organization-specific adapter owns it.
- If only a name, path, endpoint, timeout or provider changes, deployment
  configuration owns it.

```text
Pantheon invariant
-> generic Hermes method
-> organization adapter
-> deployment configuration
```

Dependency must point downward only. Pantheon must not import a Hermes tool
name, bank ID or filesystem convention. The generic skill must not duplicate
the organization adapter. The adapter must not redefine Pantheon authority.

## Examples

| Concern | Owner |
|---|---|
| recalled memory is not Evidence | Pantheon |
| an alias is not silently promoted to governed identity | Pantheon |
| decide whether project context is material | role/context contract |
| retain a conversation-local working referent | generic skill |
| build a bounded candidate set from human naming | generic skill |
| search the current AFFAIRES binding before broad recall | organization adapter |
| current bank ID, path pattern or OCR engine | deployment configuration |
| admit an inspected source as Evidence | Pantheon |

An adapter may make candidate work more reliable. Its successful execution does
not approve, persist, transmit or promote the result.
