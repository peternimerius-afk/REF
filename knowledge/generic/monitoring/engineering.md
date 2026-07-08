# Monitoring Engineering Guidance

**Capability ID:** `monitoring`  
**Version:** 0.1.0  
**Status:** Draft

## Purpose

Ensure that service health, integration failures, and operational events are detected and acted upon.

## Engineering strategy

Use binary mandatory requirements for the baseline.

Split the capability into separate requirements when the text contains independent obligations.

Do not embed evidence requests in the requirement statement.

## Baseline requirement pattern

> The solution shall monitor service availability and critical integrations.

## Common mistakes

- Using robust monitoring without defining monitored events.
- Combining monitoring, alerting, reporting, and incident response.
- Treating dashboards as sufficient monitoring.

## Evaluation guidance

Default evaluation: **binary**

Score observability maturity where proactive alerting, business event monitoring, synthetic checks, or operational dashboards improve value.

## Related REF rules

- `RFP001` Multiple obligations
- `RFP004` Evidence embedded in requirement
- `RFP008` Excessive verbosity
- `RFP010` Wrong evaluation method
