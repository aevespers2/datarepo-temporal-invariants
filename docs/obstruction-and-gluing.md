# Obstruction and Gluing Analysis

## Status

**Documentation and contract analysis only.** This page does not close the repository-integrity incident, approve the fork or product identity, implement temporal validation, authorize data access, issue credentials, publish a site or package, or grant enforcement authority.

## Method

This repository is treated as a candidate local section in the A.L.I.S.T.A.I.R.E. architecture:

- the inherited `datarepo` package describes catalogs, databases, tables, source adapters, and read-only exports;
- the proposed temporal overlay would describe observations, invariant contracts, canonicalization, evaluation, and evidence;
- neighboring repositories may retrieve evidence, authorize capabilities, validate transport, or display results.

A **gluing map** is a versioned interface that lets two sections agree on identity, semantics, authority, evidence, failure behavior, and rollback. An **obstruction** is any unresolved condition that prevents those local sections from composing into one deterministic and reviewable system.

This is an engineering compatibility analysis, not a completed mathematical homology computation.

## Active obstruction ledger

| ID | Obstruction | Affected boundary | Why composition fails | Required witness or decision | Status |
|---|---|---|---|---|---|
| DT-01 | Repository and package identity is unresolved | Upstream `datarepo` ↔ local temporal work | Consumers cannot tell whether this is a mirror, maintained fork, overlay, or renamed derivative | approved upstream commit, divergence manifest, package/site name, notices, publication target, migration and rollback | BLOCKED |
| DT-02 | Repository-integrity incident remains open | local worktree ↔ provenance and release evidence | Mutable tracked forensic state and unclear invocation paths make exact-source claims unreliable | preserved evidence, writer and invocation identity, containment, repair, independent replay, explicit closure | FAIL |
| DT-03 | Supported Python contract conflicts with source syntax | package metadata ↔ runtime/tooling | metadata claims Python 3.8 while current source validation requires Python 3.10+ | approved supported-version matrix, clean fixtures, metadata migration, downstream compatibility report | BLOCKED |
| DT-04 | Temporal subject identity is undefined | catalog/table declarations ↔ observations and results | renames, partitions, paths, aliases, and derived artifacts may map to different subjects | canonical subject-ID rules and rename/migration fixtures | PROPOSED |
| DT-05 | Clock and ordering semantics are undefined | observations ↔ invariant engine | event time, observation time, commit time, partial order, and late data can produce incompatible results | one approved time model, ordering rules, ambiguity behavior, and deterministic fixtures | PROPOSED |
| DT-06 | Canonicalization is undefined | input adapters ↔ result hashes | timestamps, Unicode, decimals, floats, nulls, paths, maps, sets, and metadata may hash differently | canonical serialization specification and cross-language golden vectors | PROPOSED |
| DT-07 | Validation result vocabulary is not mapped portfolio-wide | temporal result ↔ Bridge, QSO-STUDIO, AionUi, release gates | `pass`, `fail`, `indeterminate`, and `error` may be interpreted inconsistently or `indeterminate` may be promoted to pass | versioned result schema, severity mapping, fail-closed fixtures, UI rendering fixtures | PROPOSED |
| DT-08 | Evidence transport ownership is unclear | temporal evidence ↔ Bridge and public documentation | generated evidence may be packaged, corrected, revoked, or published by multiple components without one contract owner | evidence-envelope owner, correction/revocation rules, hashes, signatures, retention and publication authority | BLOCKED |
| DT-09 | Retrieval and observation authority is unclear | QSO-SEEKER or source adapters ↔ remote datasets | a retrieval record does not itself authorize data access, sampling, or repeated observation | Repository `1` capability envelope, data classification, purpose, scope, rate/cost limits, expiry and revocation | BLOCKED |
| DT-10 | Validator versus enforcer authority is not separated contractually | temporal engine ↔ Repository `0`, Repository `1`, deployment and payment systems | a validator result could be treated as permission to mutate, publish, deploy, or pay | explicit rule that validation emits evidence only; separate policy decision and capability grant required | PROPOSED |
| DT-11 | Static catalog privacy boundary is incomplete | catalog generation ↔ GitHub Pages or another publication endpoint | schemas, samples, source URIs, operational metadata, and private endpoints may leak | field-level publication policy, redaction fixtures, privacy review, artifact inspection and withdrawal path | BLOCKED |
| DT-12 | ROAPI output can be mistaken for an authorization layer | generated YAML ↔ API deployment | generated configuration describes query access but does not supply authentication, authorization, limits, or audit | deployment-owned security profile and negative unauthorized-access fixtures | PROPOSED |
| DT-13 | Custom Python table functions cross from metadata into execution | catalog inspection ↔ build/docs/validation | documentation or schema discovery may execute arbitrary application code and external effects | static declaration path or explicitly trusted sandbox, no-network default, time/resource limits and hostile fixtures | BLOCKED |
| DT-14 | Build hooks are part of the supply-chain boundary | package build ↔ Node/static assets/network | packaging may run subprocesses or dependency resolution not represented in source-only validation | reviewed hook manifest, offline build fixture, dependency lock, SBOM and reproducible artifact hashes | BLOCKED |
| DT-15 | Portfolio emergency-stop and rollback sequence is not bound to temporal observations | incident/revocation ↔ cached observations, results and displays | revoked data or invalid evidence may remain visible or actionable downstream | invalidation event, cache purge/marking, evidence preservation, bounded restart order and replay fixture | PROPOSED |

## Contract-edge gluing matrix

| Edge | Minimum shared contract | Fail-closed condition | Evidence witness |
|---|---|---|---|
| inherited catalog → observation adapter | catalog/table identity, schema version, source type, selected fields, observation time and data classification | unknown identity/version, unauthorized source, executable inspection required without approval | catalog declaration hash, adapter version, capability reference and bounded observation manifest |
| QSO-SEEKER → observation adapter | canonical record ID, provenance, retrieval time, source locator, content hash, sanitization status and policy version | missing provenance, unsupported record version, unresolved hostile content or no data capability | Seeker record fixture plus independently recomputed hash |
| observation adapter → temporal canonicalizer | subject ID, clock, ordering, schema, null/missing rules and canonicalization version | unsupported major version, ambiguous clock/order or non-canonical value | golden canonical bytes and hash vectors |
| invariant contract → temporal engine | contract ID/version, predicate family, window, severity, resource bounds and compatibility rules | unknown required field, unsupported semantic version or unbounded expression | positive, negative, adversarial and migration fixture set |
| temporal engine → Bridge | result schema, evidence manifest, input/result hashes, engine version, environment, correction/revocation state | `indeterminate` or `error` promoted to pass, hash mismatch or incomplete evidence | replayed result and Bridge envelope fixture |
| Bridge → QSO-STUDIO/AionUi | immutable evidence reference, display vocabulary, redaction policy, verification state and stale/revoked marker | raw secret/private data, unsupported status, missing verification or stale evidence shown as current | deterministic UI snapshot and accessibility/error-state review |
| Repository `0` → Repository `1` → remote adapter | proposed observation task, exact target, purpose, data class, resource limits, expiry, credential reference and human approval class | proposer self-issues authority, missing scope/expiry/revoker or target mismatch | signed/recorded capability envelope and denial fixtures |
| temporal result → release/deployment decision | exact result/evidence ID, policy rule, required independent checks and approval record | validator directly causes release/deploy, evidence superseded, result not bound to candidate head | policy-decision receipt separate from validation result |
| revocation/incident → all downstream consumers | invalidation ID, affected subjects/results/artifacts, reason, effective time, retention and recovery instructions | cached or published evidence remains actionable without revoked/stale state | end-to-end invalidation and bounded-restart replay |

## Required triple-overlap witnesses

Pairwise compatibility is insufficient when three components assign different meaning to the same object. The following overlaps require one deterministic fixture suite per accepted contract version.

### Seeker → datarepo observation → temporal validator

The same source evidence must retain one canonical identity and provenance chain across retrieval, catalog/adapter representation, and temporal evaluation. The fixture must prove that sanitization or catalog metadata cannot silently alter source identity, observation time, content hash, or data classification.

### Repository `0` → Repository `1` → data-source adapter

A proposed autonomous task must not become authorized merely because an adapter can execute it. The fixture must prove that the adapter rejects absent, expired, revoked, target-mismatched, over-budget, or self-issued capabilities and emits evidence without exposing credential material.

### Temporal validator → Bridge → Studio/AionUi

One result must render with the same status and limitations across the validator, evidence envelope, and human interface. Fixtures must preserve the distinction among `pass`, `fail`, `indeterminate`, and `error`, display stale/revoked evidence, and prevent unsupported claims from being inferred from a green visual state.

### Temporal validator → policy decision → release/deployment

A valid result is evidence, not authority. The fixture must prove that release or deployment remains blocked without a separate accepted policy decision tied to the exact candidate head, complete evidence set, named approver, and rollback plan.

### Incident authority → evidence store → downstream cache

A freeze or revocation must propagate while preserving forensic evidence. The fixture must prove that affected results are marked invalid or stale, cannot trigger consequential actions, remain available for investigation under retention policy, and can be replayed after an explicitly approved recovery.

## Gluing invariants

1. **Identity is explicit and versioned.** Repository, package, catalog, subject, contract, observation, result, evidence and artifact identities may not be inferred from display names.
2. **Unknown is not valid.** Unsupported versions, missing evidence, ambiguous time/order and `indeterminate` results fail closed for consequential decisions.
3. **Validation is not authorization.** The temporal engine emits evidence only; Repository `1` or an approved successor owns capability and canonical-state decisions.
4. **No hidden execution.** Catalog discovery, documentation generation and canonicalization must not execute unreviewed custom Python or access remote data implicitly.
5. **Provenance survives every edge.** Hashes, versions, environment, policy and capability references remain traceable without recording secrets.
6. **Corrections and revocations propagate.** Superseded or invalid evidence remains visibly non-current in transport, interfaces, caches and release records.
7. **Rollback restores a reviewed boundary.** The temporal overlay remains separable from inherited query behavior and can be removed without rewriting source data.
8. **Security state is external to the component being stopped.** Emergency stop, capability revocation and recovery do not depend solely on the affected adapter or validator.

## Recommended repair sequence

1. close the repository-integrity incident with preserved evidence and independent replay;
2. approve repository/package/site identity and exact upstream provenance;
3. resolve the Python support matrix and reproducible inherited baseline;
4. assign owners for subject identity, canonicalization, result schema and evidence envelope;
5. approve Repository `1` or another independent capability authority for remote observations;
6. create cross-repository golden fixtures for the required overlaps;
7. approve privacy, publication, correction, revocation and emergency-stop contracts;
8. only then mark the temporal contract task `READY` for implementation.

## Architectural clarification required

The portfolio must designate:

- whether this repository is a mirror, maintained fork, documentation-only overlay or renamed derivative;
- the canonical owner of temporal subject identity and contract/result schemas;
- the evidence-envelope boundary between this repository and Bridge;
- the source-observation contract with QSO-SEEKER;
- Repository `1` or another approved issuer for remote-data capabilities;
- the policy owner that maps results to release/deployment consequences;
- privacy, publication, incident, revocation, emergency-stop and recovery owners.
