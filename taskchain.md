# Task Chain

Architect owns task dependencies, sequencing, acceptance criteria, and boundaries. Builders preserve upstream provenance, tests, evidence, and rollback paths.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Decide whether this repository is an upstream mirror, maintained fork, documentation-only temporal-invariant overlay, or renamed independent derivative while preserving the existing `data-repository` 0.0.2 provenance.
- **User outcome:** A developer can identify exactly which behavior is inherited, reproduce the supported upstream-compatible package, and evaluate any temporal-invariant extension without confusing it with upstream functionality.
- **MVP scope:** exact upstream commit/history, divergence, package identity, license/notices, supported Python/dependency matrix, clean build/install/tests/static checks, security/provenance baseline, and an approved written boundary for the temporal-invariant overlay.
- **Priority:** Fork/scope approval and inherited baseline verification precede schemas, validators, APIs, package renaming, or publication of temporal-invariant capability.
- **Success criteria:** the upstream relationship is approved; inherited and local changes are separated; build/tests/docs pass at one immutable commit; package/version naming is unambiguous; any overlay has defined semantics, non-goals, compatibility, migration, and rollback.
- **Non-goals:** silently republishing under the upstream identity, replacing the 0.0.2 history, claiming unimplemented invariant behavior, or mixing research notes into the package API without versioned contracts and fixtures.
- **Release rationale:** Provenance and product identity must be resolved before users can trust either the inherited data repository or a new temporal extension.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve mirror/fork/overlay/derivative identity | Architect | User approval | BLOCKED | Exact upstream baseline, local divergence, package/release name, license/notices, publication target, and temporal-overlay boundary are approved. |
| P1 | Reproduce the inherited `data-repository` 0.0.2 baseline | Architect | P0 | PROPOSED | Clean build/install, complete tests, format/lint/type/docs/smoke checks, dependency/security review, commands, and provenance pass at one immutable commit. |
| P2 | Define a schema-first temporal-invariant contract | Architect | P1 | PROPOSED | Problem statement, users, inputs/outputs, canonical semantics, compatibility, migration, non-goals, fixtures, and rollback are Builder-ready without modifying upstream behavior silently. |
| P3 | Implement the approved overlay separately | Builder | P2 | PROPOSED | Versioned schemas/validators and deterministic positive/negative fixtures pass; packaging and documentation preserve upstream/local separation. |

## Builder Log

Record approval decisions, upstream and local commits, commands/results, package artifacts, dependency/security findings, schema/fixture hashes, migration evidence, rollback, and follow-ups.