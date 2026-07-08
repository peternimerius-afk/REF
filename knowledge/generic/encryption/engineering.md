# Encryption Engineering Guidance

**Capability ID:** `encryption`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Protect data confidentiality and integrity in storage and transmission.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> Data shall be encrypted in transit and at rest.

## Common mistakes

- Using secure data handling instead of explicit encryption obligation.
- Combining encryption with key management and access control.
- Specifying algorithms unnecessarily unless mandated.

## Evaluation guidance

Default evaluation: **binary**

Score security maturity only where key management, customer-managed keys, or advanced controls materially differentiate suppliers.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
