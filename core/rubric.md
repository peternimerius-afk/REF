# Requirement Quality Rubric

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define a measurable quality score for procurement requirements.

The Requirement Quality Score measures engineering quality, not business importance.

A critical requirement may have a low engineering quality score if it is ambiguous, verbose, subjective, or unevaluable.

---

## Score scale

| Score | Meaning |
|---:|---|
| 90-100 | Procurement-ready |
| 75-89 | Minor improvements recommended |
| 60-74 | Usable with revision |
| 40-59 | Major revision required |
| 0-39 | Reject or rewrite |

---

## Weighted dimensions

| Dimension | Weight |
|---|---:|
| Atomicity | 20 |
| Objectivity | 20 |
| Evaluability | 20 |
| Evidence separation | 15 |
| Conciseness | 10 |
| Correct evaluation model | 10 |
| Traceability | 5 |
| **Total** | **100** |

---

## Atomicity

**Weight:** 20

| Score | Definition |
|---:|---|
| 20 | One independent obligation |
| 10 | Mostly atomic but contains minor secondary condition |
| 0 | Multiple independent obligations |

---

## Objectivity

**Weight:** 20

| Score | Definition |
|---:|---|
| 20 | Fully objective |
| 10 | Mostly objective but contains one weak term |
| 0 | Subjective or marketing-oriented |

---

## Evaluability

**Weight:** 20

| Score | Definition |
|---:|---|
| 20 | Can be evaluated consistently by independent evaluators |
| 10 | Evaluability requires interpretation |
| 0 | Cannot be objectively evaluated |

---

## Evidence separation

**Weight:** 15

| Score | Definition |
|---:|---|
| 15 | Requirement and evidence are separate |
| 8 | Evidence partially embedded |
| 0 | Requirement is primarily evidence request |

---

## Conciseness

**Weight:** 10

| Score | Definition |
|---:|---|
| 10 | Within configured length limit |
| 5 | Slightly verbose |
| 0 | Excessively verbose |

---

## Correct evaluation model

**Weight:** 10

| Score | Definition |
|---:|---|
| 10 | Binary/scored method is justified |
| 5 | Evaluation method is acceptable but not optimal |
| 0 | Evaluation method is wrong or missing |

---

## Traceability

**Weight:** 5

| Score | Definition |
|---:|---|
| 5 | Source and capability traceable |
| 3 | Source traceable but capability unclear |
| 0 | No traceability |

---

## Example scoring

Requirement:

> The supplier shall provide a modern and flexible support model and describe escalation procedures.

Score:

```yaml
quality:
  atomicity: 0
  objectivity: 0
  evaluability: 5
  evidence_separation: 0
  conciseness: 5
  correct_evaluation_model: 5
  traceability: 5
  total: 20
```

Finding:

> Reject or rewrite.
