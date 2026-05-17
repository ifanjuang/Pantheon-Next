# Example — Architecture / MOE — Recovery Quote and Client Communication

Status: fictional professional example — educational support only.

This example illustrates how Pantheon Next may frame an AI-assisted review of a sensitive architecture / maîtrise d’œuvre dossier.

It is not legal advice.

It is not technical validation.

It is not insurance advice.

It does not replace the architect’s judgment, site knowledge, contractual analysis or professional liability review.

## Scenario

A project has a failing or defaulting contractor.

A new company proposes a recovery quote.

The client asks the architect / MOE to prepare an email validating or responding to the quote.

The dossier is sensitive because:

- previous works may not have been received;
- the quote may include works outside the initial CCTP;
- site conditions may be uncertain;
- the contractor’s failure may affect responsibility and sequencing;
- a poorly worded email could be interpreted as professional validation;
- the architect’s DET mission may have limits.

## User request

```text
Prepare an email to the client responding to the recovery quote.
```

## Pantheon interpretation

The request must not be treated as a simple drafting task.

It contains professional-risk tension:

```text
reply to client
vs.
avoid validating works, scope, price, responsibility or reception status too early
```

## Mission sheet — Task Contract excerpt

```text
Mission        : Review recovery quote and prepare client-facing response
Scope          : Project [PROJECT-MASKED], recovery quote [QUOTE-ID-MASKED]
Allowed        : recovery quote
                 initial CCTP
                 contract / mission limits
                 site reports and meeting minutes
                 previous payment and progress records
                 photographs or constat if available
Forbidden      : other client dossiers
                 assumptions about hidden defects not documented
                 definitive legal or insurance conclusions
Expected       : internal risk note + candidate client email
Approval       : architect review required before transmission
Memory         : no durable memory unless validated and scoped to project
```

## Source and evidence review

| Item | Status | Comment |
|---|---|---|
| Initial CCTP | Required | Needed to compare initial scope and recovery quote. |
| Recovery quote | Required | Must be separated into in-scope, out-of-scope and unclear items. |
| Site reports / meeting minutes | Required | Needed to understand execution history and reservations. |
| Reception status | Critical uncertainty | If no reception occurred, avoid wording that implies acceptance. |
| Contractor default context | Required | Must be described factually, not over-interpreted. |
| Client request | Required | Clarifies whether the client asks for technical opinion, validation or negotiation wording. |
| Insurance / legal position | Not assumed | Must be referred to competent adviser if needed. |

## Useful tensions

| Tension | Pantheon handling |
|---|---|
| The client wants a quick answer. | Produce a candidate email, but mark it as requiring architect review. |
| The quote may be partly valid. | Split into categories instead of approving globally. |
| Prior works may not be received. | Avoid language implying reception, acceptance or validation. |
| Some items may be corrective works. | Ask whether they are included, additional, remedial or uncertain. |
| The architect has DET limits. | Make mission boundary explicit before advising beyond scope. |

## Evidence Pack excerpt

```text
Evidence Pack — Recovery quote review

Sources used:
- recovery quote [QUOTE-ID-MASKED]
- CCTP [VERSION-MASKED]
- site report [CR-XX]
- contractor default note [DATE-MASKED]

Assumptions:
- no formal reception identified in supplied documents
- some quote items appear outside the initial CCTP, to verify
- site condition requires contradictory verification before firm position

Contradictions / gaps:
- quote item 2.3 described as reprise, but no matching reservation found
- quote item 4.1 may be improvement rather than recovery
- payment history does not establish reception or validation

Risk note:
- do not state that the quote is accepted or technically validated
- do not state that previous works are received
- recommend neutral wording and request missing checks
```

## Candidate deliverable — internal note

```text
The recovery quote should not be approved globally at this stage.

Suggested classification:

1. Items apparently within initial scope
   - to compare against CCTP and remaining balance.

2. Items possibly outside initial scope
   - to request clarification and separate pricing.

3. Items requiring site verification
   - to be checked contradicto­rily before recommendation.

4. Items with responsibility or insurance implications
   - to avoid validating in client email without further advice.
```

## Candidate deliverable — client email

```text
Subject: Recovery quote — points to clarify before position

Hello [CLIENT],

I have reviewed the recovery quote as a working document.

At this stage, I would avoid treating it as globally validated. Several items need to be separated before a position can be taken:

1. items that appear to correspond to the initial scope;
2. items that may be additional or outside the initial CCTP;
3. items that require site verification before confirmation;
4. items whose wording may affect the handling of previous works.

I suggest we ask the company for a clarified breakdown before any approval, separating recovery works, additional works and items requiring verification.

This review does not constitute reception of previous works or validation of hidden conditions.

Best regards,
[ARCHITECT]
```

## User Decision Gate

Pantheon should require a decision if the user asks to send the email directly.

```text
Decision required:
Send neutral clarification email now
or
wait for additional verification / contradictory site review
or
prepare internal note only
```

Decision effects:

| Option | Effect |
|---|---|
| Send neutral clarification email | Low external effect, if wording remains non-committal. |
| Wait for verification | Safer for technical and responsibility posture. |
| Internal note only | No external effect, but client remains unanswered. |

## Memory rule

Possible Memory Candidate:

```text
Project [PROJECT-MASKED] has unresolved recovery quote classification issues as of [DATE].
```

This must not become Canonical Memory unless:

- project scope is confirmed;
- source documents are linked;
- architect approves retention;
- memory is scoped to the project only.

## Why this example matters

This is a strong Pantheon case because the risk is not only hallucination.

The risk is premature professional commitment.

Pantheon helps separate:

```text
draft
technical opinion
client-facing wording
approval
reception
memory
```

The professional remains responsible for the final position.
