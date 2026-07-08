# Requirements Engineering Framework (REF)

**Version:** 0.1.0  
**Status:** Draft  
**Scope:** Non-functional procurement requirements

REF is an engineering framework for designing, reviewing, normalizing and validating procurement requirements.

REF is not a prompt library. REF is not tied to any AI model. REF is a specification and repository of engineering rules, policies, schemas and knowledge packs that can be used by humans, AI assistants, scripts, applications or future procurement tooling.

## Purpose

REF exists to improve the quality of procurement requirements by making them:

- concise;
- atomic;
- objective;
- measurable;
- reusable;
- configurable;
- traceable;
- objectively evaluable.

The initial focus is non-functional requirements, especially for public procurement contexts where requirements must support transparent and fair evaluation.

## Core idea

Requirements define obligations.  
Evidence demonstrates compliance.  
Evaluation determines fulfilment.  

These concepts must remain separate.

## Design goals

REF aims to answer five practical questions:

1. Are the requirements well engineered?
2. Which requirements are ambiguous, verbose or hard to evaluate?
3. Which requirements should be binary SHALL requirements?
4. Which requirements should be scoreable because they create meaningful supplier differentiation?
5. Which expected capabilities are missing from the requirement set?

## Architecture

```text
Importer
  -> Parser
  -> Requirement Detection
  -> Requirement Objects
  -> Engineering Engine
  -> Evaluation Engine
  -> Capability Mapping
  -> Gap Analysis
  -> Requirement Generation
  -> Export
```

The engineering core is independent from laws, industries, technologies and organizations. Local variations are expressed through policies and knowledge packs.

## Repository structure

```text
REF/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── docs/
├── core/
├── policies/
├── catalog/
├── knowledge/
├── templates/
├── examples/
└── tests/
```

## Layers

REF separates concerns into layers:

1. **Core** — universal requirements engineering rules.
2. **Policies** — configurable procurement and organizational choices.
3. **Capability Catalog** — generic capabilities expected in requirement sets.
4. **Knowledge Packs** — reusable domain, technology and industry knowledge.
5. **Projects** — confidential project-specific configuration and documents. Projects are not committed to this repository.

## Initial use cases

### Use case 1: Improve existing NFRs

Input: Word, Excel, PDF, Markdown or text containing draft requirements.  
Output: normalized, concise, atomic and evaluable requirements.

### Use case 2: Generate NFRs from configuration

Input: project configuration such as SaaS, airport system, AODB, LIS 2-3-3, GDPR.  
Output: candidate NFR set based on loaded policies and knowledge packs.

### Use case 3: Gap analysis

Input: project configuration plus existing requirements.  
Output: missing capabilities and proposed missing requirements.

## Guiding principle

A requirement shall exist because a capability requires it, not because it appeared in a previous tender.
