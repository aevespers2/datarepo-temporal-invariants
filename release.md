# Release Plan

## Current Decision

Status: `BLOCKED — OPEN REPOSITORY-INTEGRITY INCIDENT`

No release is eligible. The repository records a suspected forensic-state integrity incident involving tracked `.forensics/last_run_epoch.txt`, a reported writer path at `scripts/git_forensics_autocommit.sh`, cross-worktree `Resource deadlock avoided` behavior, and an unexplained epoch change from `1769819269` to `1771791970`. These observations do not establish malicious activity, but repository trust, provenance, and release evidence are not acceptable until the writer and invocation path are identified, evidence is preserved, automation is contained and repaired, and independent replay closes the incident.

The inherited `data-repository` Python package remains at version `0.0.2` with upstream metadata pointing to `neuralinkcorp/datarepo`. The mirror/fork/overlay/derivative identity decision remains required after incident closure. A substantial documentation candidate and `punchlist.md` now exist, but no accepted exact-head workflow result, repository-health approval, inherited-baseline reproduction, temporal contract, cross-repository compatibility witness, or release approval exists.

## Versioning

- Preserve the inherited `0.0.2` package lineage and upstream attribution.
- Do not tag, publish, or increment a package version while the integrity incident is open.
- After incident closure, approve one identity before release: upstream mirror, maintained fork, documentation-only temporal overlay, or renamed derivative.
- Any maintained fork must record the exact upstream commit and use differentiated package and release naming.
- Temporal-invariant capability may not be versioned until contracts, deterministic fixtures, compatibility, migration, security, provenance, cross-repository gluing, and rollback evidence pass.
- Incident-remediation commits are security maintenance evidence only; they do not constitute a product release by themselves.

## Release Scope

### Incident containment and remediation prerequisite

- Preserve the committed and observed forensic marker values, hashes, metadata, logs, worktree state, hooks, schedulers, process evidence, refs, remotes, credentials, and script identity.
- Disable tracked-state auto-commit and live-worktree mutation affecting `.forensics/` until repair is accepted.
- Move mutable run state out of tracked product paths or into an explicitly ignored local state location.
- Require repository/worktree identity binding, exclusive locking, atomic temporary-write/`fsync`/rename behavior, path and ownership validation, and fail-closed lock contention.
- Reproduce and pass concurrent-writer, stale-lock, interrupted-write, recursive-invocation, wrong-worktree, shared-`.git`, symlink, unauthorized-owner, read-only, changed-script, and changed-hook fixtures.
- Retain an independently reviewed incident report, residual-risk statement, evidence hashes, and rollback procedure.

### Inherited baseline after incident closure

- Exact upstream commit/history and local divergence.
- License, notices, package identity, supported Python/dependency matrix, reproducible build and installation.
- Complete tests, formatting, linting, typing, documentation, smoke checks, security review, and provenance.

### Optional temporal overlay after identity approval

- Approved problem statement, users, inputs/outputs, canonical semantics, non-goals, compatibility, migration, versioned schemas, deterministic fixtures, security model, and rollback.
- Approved pairwise contracts and triple-overlap witnesses with QSO-SEEKER, Repository `0`, Repository `1` or another capability authority, Bridge, QSO-STUDIO/AionUi, release policy, and incident/revocation handling.
- Explicit separation between validation evidence and capability, enforcement, merge, release, deployment, payment, or canonical-state authority.

## Selected Completed Work

- Incident observations and competing explanations have been preserved without asserting an unverified cause.
- Immediate containment, evidence-capture requirements, technical repair requirements, validation fixtures, and incident-closure criteria are documented.
- Product work has been reprioritized behind repository-integrity restoration.
- A deployment evidence record fail-closes publication and packaging while the incident remains open.
- A Pages-ready documentation candidate now separates inherited package behavior, local integrity/release controls, and the unimplemented temporal overlay.
- Architecture, authority/claims, API/extension, onboarding, integrity operations, release evidence, identity, overlay-isolation, obstruction/gluing, and temporal-design documents exist.
- `punchlist.md` now decomposes incident, documentation, identity, inherited baseline, temporal contract, cross-repository gluing, privacy, security, release, and recovery work.
- The candidate workflow is validation-only and does not retain checkout credentials or publish a package or Pages site.

No package implementation, temporal overlay, publication artifact, credential, remote integration, enforcement path, or production authority is selected as releasable completed work.

## Planned Changelog Entries

- `Security`: preserve forensic epoch drift observations and classify them as a suspected integrity incident pending investigation.
- `Security`: remove mutable forensics state from tracked live-worktree paths and add lock-safe, atomic, worktree-bound state handling.
- `Fixed`: prevent recursive, concurrent, cross-worktree, symlink, path-escape, and unauthorized-owner mutations.
- `Tests`: add deterministic incident-reproduction and containment fixtures.
- `Provenance`: retain evidence hashes, script identity, refs, hooks, scheduler/process findings, and independent replay results.
- `Fork`: record approved upstream baseline, divergence, attribution, ownership, and publication identity after incident closure.
- `Documentation`: record the approved temporal-overlay charter, semantics, compatibility, limitations, migration, gluing contracts, and rollback policy.
- `Release`: publish only after artifacts, SBOM, checksums, provenance, approvals, and all acceptance gates pass.

## Acceptance Gates

| Gate | Status | Requirement |
|---|---|---|
| Incident containment | FAIL | Preserve evidence; disable the unsafe writer, scheduler, hook, or task path; prevent further tracked `.forensics/` mutation. |
| Root-cause determination | FAIL | Identify the exact writer and invocation path; disposition benign and adversarial hypotheses using retained evidence. |
| Repository integrity | FAIL | Refs, commits, hooks, remotes, credentials, worktrees, schedulers, logs, ownership, and file metadata contain no unexplained activity, or findings are remediated. |
| State-writer repair | FAIL | Mutable state is out-of-tree or ignored; writes are atomic, exclusively locked, worktree-bound, path-safe, ownership-checked, and fail closed. |
| Incident fixtures | FAIL | All concurrency, interruption, recursion, cross-worktree, symlink, ownership, read-only, script-hash, and hook-change fixtures pass. |
| Independent validation | FAIL | Inspector reproduces the prior failure mode, confirms containment and repair, verifies evidence hashes, and reports no unexplained mutation. |
| Incident closure approval | PENDING | Architect explicitly closes the incident after evidence and residual risk are reviewed. |
| Fork/scope decision | BLOCKED | After incident closure, approve repository identity, package/release name, publication target, and overlay boundary. |
| Task completion | FAIL | Complete and evidence the blocking items in `punchlist.md`; mark corresponding task-chain work `DONE`. |
| Repository health | FAIL | Accepted repository-health evidence covers branch state, workflows, dependencies, maintainability, licensing, documentation, security, and release controls. |
| Upstream provenance | FAIL | Exact baseline, divergence, imported history, license/notices, and prior-release relationship are recorded. |
| Build/tests/static | NO CURRENT EVIDENCE | Clean build/install, complete tests, format, lint, type, docs, and smoke checks pass at one immutable candidate commit. |
| Temporal determinism | NOT INCLUDED | If executable overlay work is proposed, canonical outputs, hashes, fixtures, compatibility, and migrations pass. |
| Cross-repository gluing | PROPOSED | Pairwise contracts and triple-overlap fixtures preserve subject identity, capability, status, evidence, revocation, privacy, policy and rollback semantics. |
| Security | FAIL | Incident is closed and dependencies, secrets, parsers/serialization, filesystem/network, CI, permissions, custom functions, build hooks, data capabilities, privacy and supply chain pass review. |
| Documentation | PARTIAL | Project, architecture, design, operations, authority, evidence, obstruction and punch-list material exists; final exact-head build, link/diagram/accessibility/privacy review, artifact and approval remain pending. |
| Provenance | FAIL | Candidate/upstream commits, commands, runtimes, reports, artifacts, hashes, SBOM, attestations, contract versions, capability references and reviewer identities are retained. |
| Exact-head CI | PENDING | The final documentation pull-request head passes source assertion, validation-only checks, strict documentation build and retained evidence; no accepted run is currently recorded for the updated head. |
| Deployment | BLOCKED | `deploy.md` records fail-closed deployment posture; no package, tag, publication, workflow activation, remote integration, downstream pin, or Pages deployment is authorized. |
| Release approval | PENDING | Explicit approval only after every blocking gate passes. |

## Artifact Requirements

### Incident evidence bundle

- Binary-safe diff, committed copy, observed copy, metadata, and SHA-256 values for `.forensics/last_run_epoch.txt`.
- Script, hook, scheduler, task-runner, lockfile, configuration, and log snapshots with hashes.
- `git status --porcelain=v2 --branch`, worktree inventory, reflogs, refs, remotes, relevant Git configuration, and account/audit evidence where available.
- Root-cause report, hypothesis disposition table, containment record, residual-risk statement, and explicit closure approval.
- Repair patch, deterministic reproduction fixtures, complete test results, independent replay report, and rollback instructions.

### Documentation and contract evidence

- Strictly rendered site tied to the exact pull-request head with link, navigation, diagram, accessibility, privacy and generated-output review.
- Repository identity and upstream/local provenance decision records.
- Temporal contract/result schema proposals, canonicalization vectors, compatibility/migration plan and fixture manifest.
- Cross-repository edge schemas and deterministic witnesses for Seeker → observation → validator; Repository `0` → Repository `1` → adapter; validator → Bridge → UI; validator → policy → release/deployment; and incident/revocation → evidence store → downstream cache.
- Evidence correction, revocation, retention, publication and rollback procedures.

### Release bundle after incident closure

- Upstream/fork provenance and divergence report.
- Reproducible source archive, sdist, and wheel for any package candidate.
- Complete build, test, static, documentation, smoke, security, dependency and repository-health reports.
- For any overlay: versioned schemas, fixtures, compatibility matrix, migration evidence, canonical hashes, threat model, capability model and gluing witnesses.
- SBOM, SHA-256 checksums, provenance manifest, attestations, immutable candidate commit and approval record.

## Rollback Criteria

Immediately withdraw or block any candidate if forensic state changes without an identified authorized writer; evidence hashes differ; lock contention, recursion, cross-worktree writes, symlink/path escape, unauthorized ownership, or non-atomic writes recur; refs, hooks, remotes, credentials, or scheduler activity remain unexplained; independent replay fails; or incident closure evidence is incomplete.

After release eligibility is restored, also withdraw or roll back if attribution or identity is unclear, imported and local work cannot be separated, packaging misrepresents the inherited `0.0.2` baseline, tests are non-reproducible, temporal semantics accept invalid state or break compatibility silently, `indeterminate` is promoted to pass, gluing witnesses fail, validation is treated as authorization, sensitive data leaks, revocation does not propagate, severe security findings remain, documentation is materially inaccurate, provenance is incomplete, or published hashes differ. Restore the last independently verified immutable baseline and preserve rejected candidate and incident evidence.

## Unresolved Blockers

- Open suspected repository-integrity incident involving tracked forensic epoch drift and reported cross-worktree deadlock behavior.
- Exact writer, invocation path, scheduler/hook/task source, root cause, and authorization have not been established.
- Evidence capture, containment confirmation, technical repair, deterministic fixtures, independent replay, and explicit incident closure are incomplete.
- Most blocking `punchlist.md` items remain incomplete.
- The updated documentation candidate has no accepted exact-head workflow evidence.
- No current install/build/test/static/security/documentation/provenance release bundle exists.
- Approval remains required for mirror/fork/overlay/derivative identity, package naming, publication target, ownership, and temporal-overlay boundary after incident closure.
- Python support metadata conflicts with source syntax and has no approved migration decision.
- No implemented temporal schema, validator, deterministic fixture set, compatibility matrix, migration evidence, capability contract, or gluing witness exists.
- Owners remain unresolved for subject identity, contract/result schemas, evidence transport, remote-data capability, privacy/publication, release policy, incident, emergency stop and recovery.
- Publication under the inherited package identity or a new temporal identity remains prohibited.

## Release Log

- 2026-07-16: Aligned the candidate with the explicit fork/overlay decision gate; no release-ready work selected.
- 2026-07-17: Elevated unexplained tracked forensic-state drift to a release-blocking suspected integrity incident; added containment, evidence, repair, independent-validation, artifact, and rollback gates. No release-ready work selected.
- 2026-07-17: Added `deploy.md` with environment, permissions, artifact, configuration, health, observability, rollback, and post-deployment evidence; no deployment was attempted.
- 2026-07-20: Added a substantial Pages-ready documentation, punch-list, and obstruction/gluing milestone. Release and deployment remain blocked; no implementation or authority gate changed to pass.
