# Configuration Management Engineering Guidance

**Capability ID:** `configuration-management`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that configuration is controlled, documented, traceable, and recoverable.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> System configuration changes shall be traceable.

## Common mistakes

- Mixing configuration management with change management and release management.
- Using controlled configuration without defining traceability.
- Failing to require auditability.

## Evaluation guidance

Default evaluation: **binary**

Score operations maturity where automation, versioning, rollback, or environment promotion creates measurable value.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
