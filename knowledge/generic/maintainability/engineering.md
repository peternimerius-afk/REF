# Maintainability Engineering Guidance

**Capability ID:** `maintainability`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that the solution can be maintained, patched, upgraded, and supported over time.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> The supplier shall provide a documented maintenance process.

## Common mistakes

- Combining patching, upgrades, support lifecycle, and release notes in one requirement.
- Using future-proof or modern maintainability wording.
- Failing to separate evidence from obligation.

## Evaluation guidance

Default evaluation: **binary**

Score lifecycle maturity where automated updates, predictable releases, backwards compatibility, or maintenance transparency creates value.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
