# Availability Engineering Guidance

**Capability ID:** `availability`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that the service is available at the minimum level required for business operation.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> Monthly production availability shall be at least {target}.

## Common mistakes

- Combining availability target, maintenance windows, evidence, and service credits in one requirement.
- Using subjective wording such as high availability without a numeric target.
- Embedding historical availability evidence in the requirement text.

## Evaluation guidance

Default evaluation: **binary**

Score availability only where higher availability materially improves procurement outcome and can be objectively weighted against price.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
