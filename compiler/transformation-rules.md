# Transformation Rules

**Version:** 0.1.0  
**Status:** Draft

Transformation rules define how Requirement Objects are normalized.

## TR-001 Split multiple obligations

### Trigger

A requirement has lint finding `RFP001`.

### Action

Split the original requirement into separate atomic Requirement Objects.

### Constraints

- Preserve procurement intent.
- Do not merge unrelated obligations.
- Reclassify each resulting object.
- Capability-map each resulting object independently.

### Example

Input:

> The solution shall support REST APIs, OpenAPI documentation and webhook callbacks.

Output:

> The solution shall support REST APIs.  
> OpenAPI documentation shall be provided.  
> The solution shall support webhook callbacks.

---

## TR-002 Move evidence out of requirement

### Trigger

A requirement has lint finding `RFP004`.

### Action

Move evidence request text to the `evidence` field.

### Example

Input:

> The supplier shall provide documentation showing that audit logging is supported.

Output:

Requirement:

> Security-relevant events shall be audit logged.

Evidence:

> Technical documentation.

---

## TR-003 Remove explanatory text

### Trigger

A requirement has lint finding `RFP005`.

### Action

Remove background, motivation, and examples unless they define mandatory scope.

---

## TR-004 Replace subjective wording

### Trigger

A requirement has lint finding `RFP002`.

### Action

Replace subjective wording with measurable criteria.

If objective criteria cannot be inferred, mark as `defer`.

---

## TR-005 Compress requirement

### Trigger

A requirement exceeds configured word limit.

### Action

Remove non-essential words while preserving:

- Actor
- Obligation
- Object
- Threshold
- Condition
- Time period

---

## TR-006 Normalize mandatory language

### Trigger

A mandatory obligation does not use configured mandatory keyword.

### Action

Rewrite using configured mandatory keyword, normally `shall`.

---

## TR-007 Separate baseline and maturity

### Trigger

A requirement contains both minimum compliance and maturity differentiators.

### Action

Create:

1. Binary mandatory baseline requirement.
2. Optional scoreable maturity requirement.

---

## TR-008 Reject unevaluable requirement

### Trigger

A requirement has lint finding `RFP003` and cannot be rewritten objectively without changing intent.

### Action

Set status to `rejected`.

Require human review.
