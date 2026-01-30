# Datarepo Temporal Invariants

This document defines the **non-negotiable invariants** enforced by the `datarepo-temporal-invariants` fork.

These invariants exist to prevent silent corruption of irreversible, time-sensitive data (e.g., neural telemetry). They take precedence over convenience, performance, and stylistic concerns.

---

## 1. Temporal Invariants

1. **Time is a first-class construct**

   * Time MUST NOT be treated as an untyped scalar.
   * All timestamps MUST carry provenance metadata.

2. **Timestamp provenance is mandatory**
   Each temporal reference MUST declare:

   * clock source (device, host, external sync)
   * monotonicity guarantees
   * resolution and uncertainty (jitter, drift if known)

3. **Monotonicity is explicit**

   * Monotonic ordering MUST be enforced when guaranteed.
   * Any break in monotonicity MUST be explicitly annotated and preserved.

4. **Causal order ≠ wall-clock order**

   * Systems MUST NOT assume equivalence between causal ordering and wall-clock time.
   * Reordering operations MUST declare their ordering semantics.

---

## 2. Raw Data Invariants

1. **Raw data is append-only**

   * Raw artifacts MUST NOT be mutated in-place.
   * Deletion, truncation, or overwriting of raw data is forbidden.

2. **Raw data is unprocessed**
   Raw data MUST NOT be:

   * normalized
   * filtered
   * resampled
   * unit-converted
   * precision-reduced

3. **Raw data is verifiable**

   * Raw artifacts MUST be content-hash addressable.
   * Bit-for-bit replay MUST be possible.

---

## 3. Lineage Invariants

1. **All derived data declares ancestry**

   * Every derived artifact MUST reference its parent artifact(s).

2. **Transformations are explicit**

   * No implicit or hidden derivations are permitted.
   * Transformation parameters MUST be recorded.

3. **Lineage is replayable**

   * Given parent artifacts and transformation metadata, derived artifacts MUST be reproducible.

---

## 4. Mutation Invariants

1. **In-place mutation is forbidden on raw artifacts**

   * APIs MUST prevent or fail attempts to mutate raw data.

2. **Derived data mutation requires versioning**

   * Any modification to derived data MUST produce a new versioned artifact.

3. **Schema drift is explicit**

   * Schema changes MUST be versioned.
   * Compatibility (forward/backward) MUST be declared.

---

## 5. Enforcement Philosophy

* Violations SHOULD fail fast.
* Silent degradation is unacceptable.
* Ambiguity is treated as a defect.

These invariants are the foundation of this fork and are not optional.
