# Audit Logging Engineering Guidance

**Capability ID:** `audit-logging`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that security-relevant and operationally relevant events can be traced.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> Security-relevant events shall be audit logged.

## Common mistakes

- Mixing audit logging with monitoring.
- Not specifying retention or event types where required.
- Embedding evidence requests in the requirement.

## Evaluation guidance

Default evaluation: **binary**

Score logging maturity only where richer event coverage, tamper resistance, exportability, or correlation capability creates value.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
