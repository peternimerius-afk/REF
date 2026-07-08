# Authentication Engineering Guidance

**Capability ID:** `authentication`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that users and systems are securely identified before access is granted.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> The solution shall support federated authentication.

## Common mistakes

- Combining authentication and authorization.
- Requiring a specific identity provider without justification.
- Using secure login without defining the mechanism.

## Evaluation guidance

Default evaluation: **binary**

Score identity maturity only where additional federation, MFA, conditional access, or lifecycle integration improves supplier differentiation.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
