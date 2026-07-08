# Disaster Recovery Engineering Guidance

**Capability ID:** `disaster-recovery`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that service can be restored after major incident or site/service failure.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> Guaranteed RTO for critical services shall not exceed {rto}.

## Common mistakes

- Combining RTO, RPO, DR testing, historical recovery, and incident definitions in one requirement.
- Scoring DR without objective recovery levels.
- Failing to distinguish DR from backup.

## Evaluation guidance

Default evaluation: **binary**

Score recovery maturity where shorter RTO, tested automation, or resilient architecture materially differentiates suppliers.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
