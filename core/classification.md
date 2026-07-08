# Content Classification

**Version:** 0.1.0  
**Status:** Draft  
**Purpose:** Define how imported document content is classified before requirement engineering.

REF shall not assume that all imported text is a requirement. Documents commonly mix requirements, evidence requests, explanatory text, evaluation instructions, comments, and contractual material.

Classification must happen before engineering.

## Classification types

| Type | Description | Processed as requirement? |
|---|---|---:|
| `requirement` | Candidate supplier obligation | Yes |
| `evidence` | Proof requested from supplier | No, attach as evidence |
| `evaluation` | Scoring or pass/fail method | No, attach as evaluation |
| `verification` | Evaluator action | No, attach as verification |
| `background` | Context or explanation | No |
| `scope` | Applicability or boundary | Sometimes |
| `assumption` | Unverified premise | No |
| `question` | RFI/RFP question | Maybe |
| `contract` | Contractual term | Maybe |
| `comment` | Editorial or internal note | No |
| `ignore` | Not relevant | No |

## Classification confidence

| Confidence | Interpretation | Recommended action |
|---:|---|---|
| 0.90-1.00 | High confidence | Process automatically |
| 0.70-0.89 | Medium confidence | Process, but flag for review |
| 0.40-0.69 | Low confidence | Ask for human confirmation |
| 0.00-0.39 | Very low confidence | Do not process automatically |

## Requirement indicators

High-confidence requirement signals include:

- shall
- must
- is required to
- shall not
- must not
- supports
- provides
- retains
- encrypts
- logs
- authenticates
- authorizes
- integrates
- shall be able to

Structural signals include:

- Column named `Requirement`
- Column named `RFP Requirement`
- Numbered list under requirement section
- Table row with requirement identifier
- Word style indicating requirement paragraph

## Evidence indicators

Evidence signals include:

- provide documentation
- describe how
- submit evidence
- demonstrate
- explain
- include in the tender response
- attach
- supplier shall provide
- documentation shall include

Evidence shall normally be moved to the evidence field.

## Background indicators

Background signals include:

- because
- in order to
- for example
- this is needed to
- the purpose of
- currently
- today
- historically

Background shall not become requirement text unless it defines scope or mandatory constraints.

## Question indicators

Question signals include:

- What
- How
- Describe
- Can the supplier
- Does the solution
- Please provide

Questions from RFI material may contain useful procurement intent but are not automatically RFP requirements.

## Contract indicators

Contract signals include:

- service credits
- liquidated damages
- liability
- termination
- penalty
- contractual commitment
- indemnity
- warranty

Contractual material shall be separated unless it expresses an objectively evaluable supplier obligation.

## Classification output

```yaml
content_unit:
  id: CU-001
  text: The solution shall support SAML 2.0 authentication.
  classification:
    primary: requirement
    confidence: 0.98
    alternatives:
      - type: scope
        confidence: 0.12
  source:
    document: requirements.docx
    section: 5.4
    paragraph: 3
```

## Human review

A user interface should present low-confidence classifications for confirmation.

```text
Detected as: Evidence
Confidence: 0.62

"The supplier shall describe its disaster recovery process."

Confirm classification:
[ Requirement ] [ Evidence ] [ Background ] [ Ignore ]
```
