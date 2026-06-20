# Human correction sheet — Architecture Vertical MVP

Status: template — human review capture, non-executable.

This sheet records the correction layer after the external adapter returns a rooms/doors Result Candidate and an Evidence Pack Candidate.

It must not mutate the PDF source. It must not promote the extraction to truth. It records what the human reviewer accepts, corrects, refuses or sends back to acquisition.

## Run metadata

```text
slice_id:
project_ref:
source_pdf:
program_ref:
adapter_or_runtime_ref:
reviewer_role:
review_date:
```

## 1. Correct readings

```text
What did the adapter read correctly?

- Object / attribute:
  Evidence locator:
  Accepted as:
  Remaining caveat:
```

## 2. Missed elements

```text
What did the adapter miss?

- Missing object / attribute:
  Where visible:
  Blocking consequence:
  Follow-up needed:
```

## 3. Over-read or invented elements

```text
What did the adapter invent, infer too strongly or mislabel?

- Candidate object / attribute:
  Problem:
  Corrective status: refused | to_verify | replacement_candidate
  Human correction:
```

## 4. Program delta review

Use only these categories:

```text
matched
missing_in_plan
extra_in_plan
ambiguous_match
dimension_or_area_to_verify
relation_to_verify
source_insufficient
```

```text
Program line:
Adapter category:
Human category:
Reason:
Evidence locator or absence reason:
```

## 5. Ontology feedback

Classify failures without adding new ontology during the run.

```text
Schema debt:
Adapter weakness:
Source insufficiency:
Human-method issue:
```

## 6. Zeus decision

```text
Decision: accepted | refused | to_verify | to_arbitrate
Reason:
Next action:
Schema change required: yes | no | to_arbitrate
Adapter change required: yes | no | to_arbitrate
```

## 7. Non-negotiable status discipline

```text
Extraction success is not proof.
Program matching is not compliance.
Human correction is not source mutation.
Candidate output is not canonical memory.
A reviewed slice may revise the ontology; it does not silently extend it.
```
