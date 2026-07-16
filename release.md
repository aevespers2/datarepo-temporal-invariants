# Release Plan

## Current Decision
Status: `BLOCKED`

No work is currently releasable. P0 repository-health work is `READY` rather than `DONE`, `punchlist.md` is absent, the Builder log has no evidence, and reviewed commit `a4302f8a2f9b9df62db6f9b040436245ed8f29e1` has no reported commit-status checks.

## Versioning
- Scheme: Semantic Versioning.
- First eligible candidate: `0.1.0-alpha.1`.
- Any schema, invariant, serialization, or compatibility change must be explicitly classified as backward-compatible or breaking before version selection.

## Candidate Scope
- Approved repository purpose and temporal-invariant model.
- Versioned schemas, fixtures, validation rules, and compatibility policy.
- Deterministic tests for valid, invalid, boundary, ordering, and migration cases.
- Reproducible build, documentation, security review, and provenance evidence.

## Selected Completed Work
None. Administrative coordination files are present, but no validated invariant implementation or data contract is recorded as complete.

## Planned Changelog Entries
- `Added`: versioned temporal-invariant schema, fixtures, and validator.
- `Changed`: compatibility and migration policy.
- `Fixed`: determinism, ordering, boundary, or serialization defects found during baseline testing.
- `Security`: parser, deserialization, input-size, dependency, and supply-chain findings.
- `Documentation`: invariant semantics, examples, failure modes, and migration guidance.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Task completion | FAIL | P0 and the bounded implementation task are `DONE` with commit evidence. |
| Determinism | NO EVIDENCE | Repeated runs produce identical canonical outputs and hashes. |
| Tests | NO EVIDENCE | Unit, fixture, negative, boundary, compatibility, and migration tests pass. |
| Security | NO EVIDENCE | Untrusted-data, parser, deserialization, dependency, secret, and CI checks pass. |
| Documentation | FAIL | Purpose, invariant semantics, compatibility, and migration behavior are undefined. |
| Provenance | NO EVIDENCE | Commit, schemas, fixture hashes, tool versions, commands, and artifact hashes recorded. |
| Approval | PENDING | Release approval after all blocking gates pass. |

## Artifact Requirements
- Versioned schemas and canonical fixtures.
- Validator/library source or package, where applicable.
- Test and security reports.
- Compatibility matrix and migration notes.
- Checksums, SBOM where packaged, and provenance manifest.

## Rollback Criteria
Rollback if a released invariant accepts invalid state, rejects previously valid compatible state without a declared breaking change, produces nondeterministic canonical data, or cannot reproduce its fixtures and hashes. Before the first verified tag, rollback means withdrawing the candidate and returning to the reviewed pre-release commit.

## Unresolved Blockers
- Repository charter and invariant semantics are not yet evidence-backed.
- `punchlist.md` and all implementation/test records are missing.
- No deterministic fixture, compatibility, security, documentation, or provenance evidence exists.
- No CI status is attached to the reviewed commit.

## Release Log
- 2026-07-16: Initial candidate evaluated and held `BLOCKED`; no completed work selected.