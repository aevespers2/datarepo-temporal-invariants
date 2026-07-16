# Release Plan

## Current Decision
Status: `BLOCKED — FORK/SCOPE APPROVAL REQUIRED`

This repository is not a blank temporal-invariant implementation. It contains the existing `data-repository` Python package at version `0.0.2`, declares Apache-2.0 licensing, and retains upstream project metadata pointing to `neuralinkcorp/datarepo`. The recently added temporal-invariant documents and coordination files do not establish whether this repository is intended to be a mirror, maintained fork, research overlay, or independently published derivative. No release is eligible until that relationship, naming, ownership, and compatibility boundary are approved and current build/test/security/provenance evidence is produced for reviewed head `dec114917dab8c886a6ce074fd473c0858b303fe`.

## Versioning
- Preserve and account for the existing package version `0.0.2`; do not silently replace it with an unrelated `0.1.0-alpha.1` line.
- Approve one release identity before tagging: upstream mirror, maintained fork, documentation-only temporal overlay, or renamed independent derivative.
- A fork release must record its upstream commit and use a clearly differentiated version/name consistent with Python packaging rules.
- Temporal-invariant schemas or APIs may not be versioned as package capabilities until implemented, tested, and integrated without obscuring upstream provenance.

## Candidate Scope
### Fork baseline
- Record upstream repository/commit, imported history, license/notices, package identity, supported Python versions, dependency ranges, build system, tests, workflows, and published-artifact history.
- Reproduce installation, build, complete tests, formatting, lint, type checks, documentation, and smoke usage.
- Review dependency, credential, data-source, serialization, filesystem, network, and supply-chain boundaries.

### Temporal-invariant overlay
- Approve the invariant problem statement, relation to the existing datarepo package, schema/API boundaries, non-goals, migration policy, and whether the overlay is documentation-only or executable.
- If executable, add versioned schemas, deterministic fixtures, validation, compatibility tests, and independent provenance.

## Existing Candidate Assets
- `pyproject.toml` defines `data-repository` version `0.0.2`, Python `>=3.8`, Hatchling builds, package contents, dependency ranges, and Apache-2.0 licensing.
- The repository has substantial upstream implementation and release history predating the temporal-invariant coordination files.
- Temporal-invariant notes and release/task coordination files are present.

These assets are not selected as newly completed aevespers2 release work until upstream provenance and local verification are separated and approved.

## Selected Completed Work
None. Existing upstream-derived implementation has not been re-verified as an aevespers2 candidate, and the temporal-invariant overlay has no completed schema, fixture, validator, compatibility, security, or provenance evidence.

## Planned Changelog Entries
- `Fork`: upstream baseline, divergence, license/notice preservation, and local ownership model.
- `Documentation`: approved temporal-invariant charter, relation to datarepo, semantics, examples, non-goals, and migration policy.
- `Added`: versioned invariant schemas, validators, and fixtures only after implementation gates pass.
- `Security`: dependency, secret, data-source, parser/serialization, filesystem/network, workflow-permission, and supply-chain findings.
- `Release`: build/test reports, SBOM, checksums, provenance, and approval decision.

## Acceptance Gates
| Gate | Status | Requirement |
|---|---|---|
| Fork/scope decision | BLOCKED | Approve mirror vs fork vs overlay vs renamed derivative, upstream attribution, package/release identity, and publication target. |
| Task completion | FAIL | P0 is revised to the approved scope and reaches `DONE`; `punchlist.md` exists with completed evidence. |
| Upstream provenance | FAIL | Exact upstream baseline, divergence, imported history, license/notices, and prior release relationship recorded. |
| Build/install | NO CURRENT EVIDENCE | Clean Hatchling build and installation pass on the supported Python matrix. |
| Tests/static validation | NO CURRENT EVIDENCE | Complete tests, formatting, lint, mypy, docs, and smoke usage pass at the candidate commit. |
| Temporal determinism | NO IMPLEMENTATION EVIDENCE | Any included invariant schemas/validators reproduce canonical outputs and hashes with positive, negative, boundary, ordering, and migration fixtures. |
| Security | NO CURRENT EVIDENCE | Dependency, secret, data-source, parser/serialization, filesystem/network, CI, and supply-chain checks pass. |
| Documentation | PARTIAL | Package metadata and temporal notes exist; approved scope, verified setup, invariant semantics, compatibility, limitations, and rollback are incomplete. |
| Provenance | NO RELEASE EVIDENCE | Candidate/upstream commits, tool/runtime versions, commands, test reports, artifact hashes, SBOM, and attestations recorded. |
| Approval | PENDING | Explicit release approval after all blocking gates pass. |

## Artifact Requirements
- Upstream/fork provenance and divergence report.
- Source archive and reproducible Python sdist/wheel for any package candidate.
- Complete build, test, static-analysis, documentation, and smoke reports.
- Versioned schemas/fixtures/compatibility matrix for any temporal-invariant implementation.
- Security/dependency report, SBOM, SHA-256 checksums, and provenance manifest.

## Rollback Criteria
Withdraw or roll back if upstream attribution or release identity is unclear, local changes cannot be separated from imported history, packaging changes overwrite or misrepresent the existing `0.0.2` baseline, tests are not reproducible, an invariant accepts invalid state or breaks compatible data without declaration, severe security findings remain, or artifact hashes differ. Restore the recorded upstream/fork baseline and preserve rejected overlay evidence.

## Unresolved Blockers
- Approval is required for the repository's intended relationship to `neuralinkcorp/datarepo`, local ownership, package naming, and publication target.
- The current task chain describes a new temporal-invariant product but does not reconcile the existing `data-repository` package and upstream history.
- `punchlist.md` is absent and P0 remains `READY`.
- No current install/build/test/static/security/documentation/provenance evidence is tied to the candidate commit.
- No temporal-invariant schema, validator, deterministic fixture set, compatibility matrix, or migration evidence exists.
- Publishing under the existing upstream package identity is prohibited until provenance, authority, and versioning are approved.

## Release Log
- 2026-07-16: Corrected the release model to preserve the existing `data-repository` `0.0.2` and upstream provenance; candidate remains `BLOCKED — FORK/SCOPE APPROVAL REQUIRED`.