# Divergence Ledger

This document records **intentional and justified divergences** between `datarepo-temporal-invariants` and the upstream `datarepo` repository.

This file exists to preserve trust, auditability, and long-term maintainability.

---

## Fork Origin

* **Upstream repository:** `datarepo`
* **Fork name:** `datarepo-temporal-invariants`
* **Fork purpose:** Enforce temporal integrity and raw-data immutability for irreversible time-series data (e.g., neural telemetry).

---

## Divergence Policy

Divergences from upstream are permitted **only** when required to uphold documented invariants.

Each divergence MUST:

* be explicitly recorded in this document
* identify the violated invariant if upstream behavior were preserved
* describe the compatibility impact

---

## Initial Divergences

### D-001 — Temporal Invariants Introduced

**Description**
Introduction of explicit temporal invariants where upstream behavior treats time as implicit or untyped.

**Rationale**
Implicit time handling permits silent reordering, drift, and corruption of irreversible datasets.

**Impact**

* Additional metadata requirements
* Stricter validation at ingestion and serialization boundaries

---

### D-002 — Raw Data Immutability

**Description**
Prohibition of in-place mutation for raw data artifacts.

**Rationale**
Neural and similar datasets cannot be re-acquired; mutation destroys scientific and forensic validity.

**Impact**

* Write paths are constrained
* Some upstream convenience APIs may be restricted or wrapped

---

## Compatibility Notes

* This fork aims to remain API-compatible with upstream where invariants are not violated.
* Divergent APIs will be clearly documented and isolated.

---

## Maintenance Guidance

When syncing upstream changes:

1. Evaluate against `docs/invariants.md`
2. Preserve upstream behavior when safe
3. Record any new divergence here before merging

This ledger is append-only and MUST NOT be rewritten.
