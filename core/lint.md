# REF Lint Rules

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define deterministic diagnostics for procurement requirement quality.

Linting is the process of identifying requirement engineering defects before requirements are published, evaluated, or contracted.

A lint finding is not a stylistic preference. It is an engineering signal that a requirement may be ambiguous, unevaluable, unfair, unnecessarily costly to evaluate, or unsuitable for procurement use.

---

## Severity levels

| Severity | Meaning |
|---|---|
| Error | Must be corrected before publication |
| Warning | Should be corrected unless justified |
| Notice | Improvement opportunity |
| Info | Informational guidance |

---

## RFP001: Multiple obligations

**Severity:** Error

### Definition

The requirement contains more than one independent obligation.

### Rationale

Independent obligations must be evaluated independently. Combined obligations reduce transparency, increase supplier ambiguity, and make compliance assessment harder.

### Detection signals

- Multiple SHALL, MUST, or REQUIRED statements.
- Conjunctions connecting obligations, especially "and", "or", "including".
- Requirement combines capability, evidence, SLA, reporting, testing, and support obligations.
- One sentence contains several compliance points.

### Required action

Split into atomic requirements.

### Bad example

> The solution shall support SAML 2.0 and OpenID Connect and provide audit logs.

### Good example

> The solution shall support SAML 2.0.  
> The solution shall support OpenID Connect.  
> Security-relevant events shall be audit logged.

### Related principles

- E001 Atomicity
- E005 Evidence Separation

---

## RFP002: Subjective wording

**Severity:** Error

### Definition

The requirement uses subjective or marketing-oriented language without objective criteria.

### Prohibited unless defined

- robust
- modern
- flexible
- intuitive
- user-friendly
- seamless
- state-of-the-art
- best practice
- adequate
- sufficient
- future-proof
- comprehensive
- efficient

### Required action

Replace subjective language with measurable criteria.

### Bad example

> The solution shall provide robust monitoring.

### Good example

> The solution shall alert on failed integrations within five minutes.

---

## RFP003: Not objectively evaluable

**Severity:** Error

### Definition

Compliance cannot be verified through objective evidence or consistent evaluator judgement.

### Required action

Rewrite with measurable acceptance criteria, or reject the requirement.

### Bad example

> The supplier shall provide a high-quality support service.

### Good example

> Priority 1 incidents shall have a response time of 30 minutes or less.

---

## RFP004: Evidence embedded in requirement

**Severity:** Warning

### Definition

The requirement text includes instructions about how the supplier shall prove compliance.

### Rationale

Evidence belongs in the evidence field, not the requirement statement.

### Detection signals

- "describe how"
- "provide documentation"
- "submit evidence"
- "explain"
- "demonstrate"
- "include in the tender response"

### Required action

Move evidence to the evidence field.

### Bad example

> The supplier shall provide documentation showing that audit logging is supported.

### Good example

Requirement:

> Security-relevant events shall be audit logged.

Evidence:

> Technical documentation.

---

## RFP005: Explanatory text embedded

**Severity:** Warning

### Definition

The requirement contains background, motivation, examples, or explanatory prose.

### Required action

Remove explanatory text unless contractually required.

### Bad example

> Because the airport operates continuously, the solution shall support 24/7 monitoring.

### Good example

> The solution shall support 24/7 monitoring.

---

## RFP006: Unnecessary implementation prescription

**Severity:** Warning

### Definition

The requirement prescribes how the supplier shall implement a capability when the implementation method is not mandatory.

### Required action

Specify the outcome instead of implementation.

### Bad example

> The supplier shall use PostgreSQL for operational data storage.

### Good example

> Operational data shall be stored in a supported relational database.

---

## RFP007: Missing measurable criterion

**Severity:** Error

### Definition

The requirement lacks a measurable threshold, condition, or compliance point.

### Required action

Add objective criteria.

### Bad example

> The system shall be highly available.

### Good example

> Monthly production availability shall be at least 99.9%.

---

## RFP008: Excessive verbosity

**Severity:** Warning

### Definition

The requirement exceeds the configured word limit without justified need.

### Default thresholds

| Requirement type | Default maximum |
|---|---:|
| Binary mandatory | 20 words |
| Scoreable | 35 words |
| Evidence | 15 words |

### Required action

Compress to the smallest wording that preserves procurement intent.

---

## RFP009: Duplicate obligation

**Severity:** Warning

### Definition

The requirement duplicates another requirement or partially overlaps with it.

### Required action

Merge, delete, or clarify scope boundaries.

---

## RFP010: Wrong evaluation method

**Severity:** Warning

### Definition

The requirement is binary but has been made scoreable without justified supplier differentiation, or scoreable where binary compliance would be sufficient.

### Required action

Apply the evaluation decision tree in `core/evaluation.md`.

---

## RFP011: Scoreable requirement lacks scoring scale

**Severity:** Error

### Definition

A scored requirement does not define objective levels.

### Required action

Define a 1-4 scale using measurable criteria.

---

## RFP012: Scoring levels overlap

**Severity:** Error

### Definition

Score levels are not mutually exclusive.

### Required action

Rewrite score levels so each supplier response maps to exactly one score.

---

## RFP013: Missing evidence

**Severity:** Warning

### Definition

No evidence has been defined for the requirement.

### Required action

Define evidence that can verify compliance.

---

## RFP014: Vendor-specific wording

**Severity:** Error

### Definition

The requirement references a named supplier, product, proprietary feature, or vendor-specific implementation without objective justification.

### Required action

Rewrite vendor-neutrally or document legal justification.

---

## RFP015: Ambiguous actor

**Severity:** Warning

### Definition

The requirement does not clearly identify whether the obligation applies to the solution, supplier, service, hosting provider, or contracting authority.

### Required action

Clarify actor.

---

## Output format

Lint findings should be reported as:

```yaml
lint:
  - code: RFP001
    severity: Error
    finding: Multiple obligations detected.
    recommendation: Split into atomic requirements.
    reference: core/engineering.md#e001-atomicity
```
