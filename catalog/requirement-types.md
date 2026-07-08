# Requirement Types

**Version:** 0.1.0  
**Status:** Draft

REF distinguishes requirement types to select the correct engineering and evaluation strategy.

---

## Mandatory binary requirement

A mandatory obligation evaluated as Yes/No.

Use when:

- There is a minimum acceptable level.
- Compliance can be objectively verified.
- Additional maturity should not be rewarded.

Example:

> The solution shall support federated authentication.

---

## Scoreable requirement

A quality or maturity differentiator evaluated using a defined scale.

Use when:

- Suppliers can meaningfully exceed the minimum.
- Differences are objectively measurable.
- Scoring improves supplier selection.
- Evaluation effort is justified.

Example:

> API maturity shall be evaluated.

---

## Mandatory baseline plus scoreable maturity

A capability with both minimum compliance and differentiated maturity.

Example:

Mandatory:

> The solution shall provide documented REST APIs.

Scoreable:

> API maturity shall be evaluated.

---

## Evidence request

A request for proof. Not a requirement.

Example:

> Supplier shall provide API documentation.

REF should usually represent this as evidence, not as requirement text.

---

## Verification instruction

Instructions for evaluators. Not a supplier obligation.

Example:

> Evaluators shall verify the SLA against submitted documentation.

---

## Contract clause

A contractual term. Not a requirement unless it expresses an evaluable supplier obligation.

---

## Rejected requirement

A candidate requirement that cannot be objectively evaluated or normalized without changing intent.

Rejected requirements require human intervention.
