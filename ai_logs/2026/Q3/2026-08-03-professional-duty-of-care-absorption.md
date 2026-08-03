# Professional duty-of-care absorption

Date: 2026-08-03

Change level: semantic clarification of an existing candidate owner.

## Observed need

`pantheon-mvp` contained `docs/governance/PROFESSIONAL_DUTY_OF_CARE.md`, even though professional mission, responsibility and external-reply boundaries belong to Pantheon-Next governance.

The note also used the historical term `cage` and declared several legal references uncertain.

## Existing owner checked

`docs/domain-packs/architecture/MISSION_RESPONSIBILITY_BOUNDARY_REFLEX.md` already owns:

```text
mission scope classification
responsibility risk
safe reply posture
forbidden professional assertions
competent-party referral
human decision before consequential output
```

A second permanent doctrine document would duplicate this owner.

## Decision

Absorb the useful professional-duty anchors into the existing reflex rather than create a parallel `PROFESSIONAL_DUTY_OF_CARE.md` in Pantheon-Next.

Verified official anchors added:

```text
Code de déontologie des architectes, article 3
Code de déontologie des architectes, article 12
Code de déontologie des architectes, article 23
Décret n° 2026-568 du 26 juin 2026
entry into force: 1 July 2026
```

MAF material remains prevention guidance, not Pantheon authority or legal advice.

## External implementation reconciliation

The external MVP file is replaced by a short implementation pointer to the Pantheon-Next owner. The MVP may implement flags or projections, but it must not maintain a second copy of the professional doctrine.

## Boundaries

```text
professional reference != automated legal advice
warning flag != legal qualification
source present != conclusion validated
professional opinion candidate != human professional judgment
runtime_success != Evidence
```

No runtime, schema, approval engine, sender, legal-review engine or external action is introduced.
