# Backup Engineering Guidance

**Capability ID:** `backup`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that data can be recovered from backup after loss, corruption, or operational failure.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> Backup shall be performed at least daily.

## Common mistakes

- Mixing backup frequency, retention, restore testing, and RPO in one requirement.
- Requesting description of backup process as the requirement.
- Failing to require restore verification.

## Evaluation guidance

Default evaluation: **binary**

Score backup only for maturity aspects such as automation, retention flexibility, immutable backups, or tested restore performance.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
