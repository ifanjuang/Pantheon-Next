# Adoption Review — Block 1 vertical slice

Review date: 2026-07-11
Reviewed commit: `236cb78` (merge of PR #2, Block 1 import)
Reviewer role: external code review against `GOVERNANCE_STATUS.md` adoption gates
Nature: **report only.** This document approves nothing, activates nothing,
and changes no status. It is the visible review evidence that
`GOVERNANCE_STATUS.md` requires *before* a human may consider adoption.

```text
review_pass != adoption
findings != approval
The human decides.
```

## Verdict

**Not ready for adoption as-is.** One blocking gap, two partials, one
deferred; four gates satisfied.

| # | Gate | Status |
|---|------|--------|
| 1 | Task Contract schema alignment | ⚠️ partial |
| 2 | Source path boundary (absolute / traversal / symlink) | ❌ **not met — blocking** |
| 3 | Fixture-specific drafting status | ✅ met |
| 4 | Human gate decision semantics | ⚠️ partial |
| 5 | System-signer refusal | ⏸️ deferred (no signing surface in Block 1) |
| 6 | External-send refusal | ✅ met (see nuance) |
| 7 | CI result after code push | ✅ met |
| 8 | Human approval for activation | ✅ correctly abstained |

## Findings

### Gate 1 — Task Contract schema alignment ⚠️ partial

`tests/test_block1.py::test_output_validates_against_vendored_schema`
validates the **output** objects (`result_candidate`,
`evidence_pack_candidate`) against
`vendor/pantheon/mvp_governed_loop_objects.schema.yaml`. Good.

But the **contract itself** is not validated against the vendored schema.
`contract.load_contract` only checks presence of `REQUIRED_FIELDS`
(`contract.py:44-62`); it never runs the `task_contract` `$def` from the
schema. A contract that satisfies the required-field presence check but
violates the schema (wrong types, malformed `object_id` pattern, etc.)
would load without objection.

**Recommendation:** jsonschema-validate the loaded contract against the
vendored `task_contract` `$def`, and add a test asserting a malformed
contract is rejected.

### Gate 2 — Source path boundary ❌ not met (blocking)

The gate names three attacks explicitly — **absolute paths, traversal, and
symlink escape** — and the code defends against **none** of them.

`contract.assert_source_in_scope` (`contract.py:65-70`) checks only set
membership: is `source_ref` one of the contract's declared sources? It
never inspects the *shape* of the path. `store.ingest`
(`store.py:79-96`) then does `path = root / source_ref` and reads it.

Demonstrated on the merged code:

```text
root / "/etc/passwd"              -> /etc/passwd            (absolute wins)
(root / "../../../etc/passwd")    -> /etc/passwd            (traversal escapes)
assert_source_in_scope(c, "/etc/passwd")     -> passes
assert_source_in_scope(c, "../../secret.md") -> passes
```

A contract that *declares* an absolute or traversing source path is read
verbatim. The "declared perimeter" boundary is therefore only as safe as
the contract author, with no defense in depth — exactly what this gate
exists to prevent. Symlink escape (a declared in-tree file that is a
symlink pointing out of the dossier) is likewise unchecked.

**Recommendation (small, self-contained):** before reading, require each
declared source to be relative, reject `..` components, resolve against a
canonicalized `root`, and assert the *real* (symlink-resolved) path is
contained under the dossier root. Reject otherwise with a `ContractError`.
Add tests for each of the three attack shapes. This is the natural first
follow-up.

### Gate 3 — Fixture-specific drafting status ✅ met

Drafting is a deterministic template hardcoded to the `devis_reprise`
fixture (`runner.py`, the French draft body naming Q-2026-041, lot 06,
CCTP 3.2). Status is `draft_to_review`; `external_action_authorized` is
`False`. This is honestly declared as a Block 1 stand-in in the README
("Drafting: template-based and deterministic in Block 1. The LLM slot
belongs to the Hermes profile (Block 2+)"). Acceptable for Block 1.

**Note (not a gate failure):** the draft is specific to the one fixture and
would produce the wrong text for any other dossier. Generalization is
Block 2's LLM-slot work, not an adoption blocker for the Block 1 scope.

### Gate 4 — Human gate decision semantics ⚠️ partial

The decision *vocabulary* is present as data: the evidence pack carries
`possible_decisions: [approve, refuse, request_revision,
request_more_evidence]`, and every candidate carries
`external_action_authorized: False` with `status: draft_to_review`.

But there is **no executable gate stand-in**. `GOVERNANCE_STATUS.md`'s own
stand-in rule names `gate.py -> terminal_gate_standin.py`, and the README's
expected shape lists a "human decision gate stand-in" — neither exists in
the tree. Nothing consumes a human decision and emits a `decision_record`
(a schema object type that currently has no producer).

**Recommendation:** add a terminal gate stand-in that reads the candidate
stream, presents the `possible_decisions`, and records the human's choice
as a `decision_record` — explicitly labelled a stand-in, never the
OpenWebUI cockpit.

### Gate 5 — System-signer refusal ⏸️ deferred

There is no signing surface in Block 1: no `decision_record` is produced,
so there is nothing yet that could self-sign. The current stand-in for the
invariant is that the runner sets `external_action_authorized: False`
everywhere — the system never authorizes action on its own. That is the
right posture, but the *explicit* system-signer refusal cannot be
exercised until the gate/decision surface of Gate 4 lands.

**Recommendation:** when Gate 4's decision surface is built, forbid the
system from ever populating a signer/decider field; only a human decision
may. Add a test that the system refuses to self-sign.

### Gate 6 — External-send refusal ✅ met (with nuance)

`runner.run` refuses before any retrieval when the question implies sending
(`envoie` / `envoyer` / `send`) and `external_send` is in the contract's
`forbidden_scope`; covered by
`test_block1.py::test_forbidden_operation_is_refused`.

**Nuance — do not mistake the detector for the cage.** The real guarantee
is *structural*: the runner has **no send code path at all**; it only emits
data. The keyword check is an advisory early-refusal for display, and it is
evadable by paraphrase (`transmets`, `fais suivre`, a non-French phrasing).
This is fine as long as it is understood as UX, not as the boundary. The
boundary is the absence of a transport. (This is the item flagged for
hardening before the Block 2 LLM slot is introduced.)

### Gate 7 — CI result after code push ✅ met

PR #2's `tests` job ran the full suite green against a
`pgvector/pgvector:pg16` service container (perimeter-breach test and both
refusal paths included). CI is `on: [push (main), pull_request]`.

### Gate 8 — Human approval for activation ✅ correctly abstained

Repository status remains `not adopted` / `not activated` /
`production forbidden`, and no code path claims activation. The code
correctly does not self-activate; the approval is the human's to give and
has not been fabricated.

## Recommended sequence

1. **Gate 2** — path boundary hardening (blocking; small, self-contained).
2. **Gate 6 nuance / hardening** — as already planned before the LLM slot.
3. **Gate 1** — validate the contract against the vendored schema.
4. **Gate 4 + 5** — terminal gate stand-in emitting `decision_record`,
   with system-signer refusal.

None of the above changes the doctrine posture. This slice remains a
candidate: not adopted, not activated, production forbidden.

## Addendum — 2026-07-11

The findings above record the state at commit `236cb78` and are left intact
as the review record. This PR is **report-only** and changes no code.

- **Gate 2 (blocking)** is addressed separately, as an executable change, in
  PR #4 (branch `claude/gate2-source-path-boundary`):
  `contract.assert_source_path_safe` rejects absolute and `..`-traversing
  declared sources at load time, and `contract.resolve_source_within`
  asserts symlink-safe containment under the ingestion root at read time,
  with four DB-free tests covering all three named attacks.

Gates 1, 4, and 5 remain open per the recommended sequence.
