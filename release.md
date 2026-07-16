# Release Plan

## Current Decision

Status: `BLOCKED — FORK/SCOPE APPROVAL REQUIRED`

This repository contains the existing `data-repository` Python package at version `0.0.2` with upstream metadata pointing to `neuralinkcorp/datarepo`, plus newer temporal-invariant coordination material. No release is eligible because P0 is blocked on approval of mirror/fork/overlay/derivative identity, `punchlist.md` is absent, inherited and local work are not separated, and candidate head `6113bae9b29e17de68ed5eefdb7e0c4b14a1054a` lacks current build, test, security, documentation, schema/fixture, provenance, artifact, and rollback evidence.

## Versioning

- Preserve the inherited `0.0.2` package lineage.
- Approve one identity before tagging: upstream mirror, maintained fork, documentation-only temporal overlay, or renamed derivative.
- Any fork package must record its exact upstream commit and use differentiated naming/versioning.
- Temporal-invariant capability may not be versioned until its contracts, fixtures, migration, and security evidence pass.

## Release Scope

### Inherited baseline
- Upstream commit/history, divergence, license/notices, package identity, supported Python matrix, build/install/tests/static checks, security, documentation, and provenance.

### Optional temporal overlay
- Approved problem statement, users, inputs/outputs, canonical semantics, non-goals, compatibility, migration, versioned schemas, deterministic fixtures, and rollback.

## Selected Completed Work

None. Existing upstream implementation and temporal notes are candidate inputs, not newly verified aevespers2 release work.

## Planned Changelog Entries

- `Fork`: upstream baseline, divergence, attribution, and ownership model.
- `Documentation`: approved temporal-overlay charter, semantics, compatibility, non-goals, and migration policy.
- `Added`: schemas, validators, and fixtures only after implementation gates pass.
- `Security`: dependency, secret, data-source, serialization, filesystem, network, and workflow findings.
- `Release`: package/source artifacts, SBOM, checksums, provenance, and approval.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Fork/scope decision | BLOCKED | Approve repository identity, package/release name, publication target, and overlay boundary. |
| Task completion | FAIL | P0 is `DONE`; `punchlist.md` exists and included work has evidence. |
| Upstream provenance | FAIL | Exact baseline, divergence, imported history, license/notices, and prior release relationship are recorded. |
| Build/tests/static | NO CURRENT EVIDENCE | Clean build/install, full tests, format, lint, type, docs, and smoke checks pass. |
| Temporal determinism | NOT YET INCLUDED | If executable, canonical outputs, hashes, fixtures, compatibility, and migrations pass. |
| Security | NO CURRENT EVIDENCE | Dependencies, secrets, parsers/serialization, filesystem/network, CI, and supply chain pass review. |
| Documentation | PARTIAL | Package metadata and notes exist; approved identity, setup, semantics, limitations, and rollback remain incomplete. |
| Provenance | NO RELEASE EVIDENCE | Candidate/upstream commits, runtimes, commands, reports, artifacts, hashes, SBOM, and attestations are retained. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements

- Upstream/fork provenance and divergence report.
- Reproducible source archive, sdist, and wheel for any package candidate.
- Complete build, test, static, documentation, smoke, security, and dependency reports.
- For any overlay: versioned schemas, fixtures, compatibility matrix, migration evidence, and canonical hashes.
- SBOM, SHA-256 checksums, provenance manifest, and rollback instructions.

## Rollback Criteria

Withdraw or roll back if attribution or identity is unclear, imported and local work cannot be separated, packaging misrepresents the `0.0.2` baseline, tests are non-reproducible, temporal semantics accept invalid state or break compatibility silently, severe security findings remain, or hashes differ. Restore the approved upstream/fork baseline and preserve rejected overlay evidence.

## Unresolved Blockers

- Approval is required for mirror/fork/overlay/derivative identity, package naming, publication target, and ownership.
- `punchlist.md` and accepted Builder evidence are absent.
- No current install/build/test/static/security/documentation/provenance bundle exists.
- No implemented temporal schema, validator, deterministic fixture set, compatibility matrix, or migration evidence exists.
- Publishing under the inherited package identity remains prohibited until authority and provenance are approved.

## Release Log

- 2026-07-16: Aligned the candidate with the explicit fork/overlay decision gate; no release-ready work selected.