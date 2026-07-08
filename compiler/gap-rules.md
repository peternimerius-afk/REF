# Gap Rules

**Version:** 0.1.0  
**Status:** Draft

Gap rules determine expected, covered, partial, and missing capabilities.

## GAP-001 Expected capability resolution

Expected capabilities are the union of:

- Generic baseline
- Procurement profile
- Security profile
- Industry pack
- Solution pack
- Technology pack
- Project configuration

---

## GAP-002 Covered capability

A capability is covered when at least one valid requirement creates an obligation for it.

---

## GAP-003 Evidence-only gap

If only evidence exists for a capability, classify as `evidence_only`.

---

## GAP-004 Partial coverage

If only part of a capability is covered, classify as `partial`.

---

## GAP-005 Missing capability

If an expected capability has no valid requirement, classify as `missing`.

---

## GAP-006 Not applicable

A capability may be excluded by project configuration.

The exclusion shall be traceable.
