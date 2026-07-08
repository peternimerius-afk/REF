# Evaluation Rules

**Version:** 0.1.0  
**Status:** Draft

Evaluation rules decide how a requirement shall be evaluated.

## EVAL-001 Binary by default

### Rule

If a requirement defines a mandatory baseline and compliance can be objectively verified, use binary evaluation.

---

## EVAL-002 Score only measurable differentiation

### Rule

Use scoring only where suppliers can objectively exceed the baseline and the difference improves supplier selection.

---

## EVAL-003 Split before scoring

### Rule

If independent obligations exist, split them before considering scoring.

---

## EVAL-004 Score maturity, not baseline compliance

### Rule

Mandatory compliance shall not be scored.

Maturity beyond minimum baseline may be scored.

---

## EVAL-005 Enforce scoreable ratio

### Rule

If scoreable requirements exceed configured maximum ratio, flag warning and recommend conversion to binary unless scoring is justified.

---

## EVAL-006 Reject subjective scoring

### Rule

A scored requirement without objective, mutually exclusive score levels is invalid.

---

## EVAL-007 Baseline plus score

### Rule

When a capability requires a minimum and also has meaningful maturity differentiation, create:

- Mandatory baseline requirement.
- Scoreable maturity requirement.

Example:

Baseline:

> The solution shall provide documented APIs for integration.

Scoreable:

> API maturity shall be evaluated.
