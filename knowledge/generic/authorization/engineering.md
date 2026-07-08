# Authorization Engineering Guidance

**Capability ID:** `authorization`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that authenticated users and systems have access only to authorized functions and data.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> The solution shall support role-based access control.

## Common mistakes

- Combining authorization with authentication.
- Using flexible access control without objective criteria.
- Failing to distinguish roles, permissions, and segregation of duties.

## Evaluation guidance

Default evaluation: **binary**

Score access control maturity where fine-grained permissions, delegated administration, or segregation controls create value.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
