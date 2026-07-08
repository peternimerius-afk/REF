# Generation Rules

**Version:** 0.1.0  
**Status:** Draft

Generation rules create requirements from missing capabilities.

## GEN-001 Generate from capability baseline

When a required capability is missing, generate the baseline requirement from the capability package.

---

## GEN-002 Generate evidence

Generated requirements shall include evidence from the capability package.

---

## GEN-003 Apply project configuration

Generated requirements shall apply project-specific parameters such as:

- Availability target
- RTO
- RPO
- Security classification
- Deployment model
- Language

---

## GEN-004 Do not invent project-specific thresholds

If a required parameter is missing, generate a placeholder and flag human review.

Example:

> Monthly production availability shall be at least `{availability_target}`.

---

## GEN-005 Trace generated requirements

Every generated requirement shall reference:

- Capability
- Knowledge pack
- Policy
- Generation rule
