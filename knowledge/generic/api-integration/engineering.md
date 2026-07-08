# API Integration Engineering Guidance

**Capability ID:** `api-integration`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that the solution can exchange data through documented machine-readable interfaces.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> The solution shall provide documented APIs for integration.

## Common mistakes

- Combining REST, OpenAPI, webhooks, SDKs, sandbox, and versioning in one requirement.
- Scoring individual API features instead of API maturity.
- Treating documentation as capability coverage.

## Evaluation guidance

Default evaluation: **binary**

API maturity is often a valid scoreable differentiator if objective levels are defined.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
