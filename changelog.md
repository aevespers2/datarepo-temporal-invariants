# Changelog

All notable product, architecture, implementation, release, and deployment changes are recorded here.

## Unreleased

### Product
- 2026-07-16 — Made mirror/fork/overlay/derivative identity the blocking decision and preserved `data-repository` 0.0.2 as the inherited baseline.
- 2026-07-16 — Deferred executable temporal-invariant work until upstream provenance, package identity, compatibility, migration, and publication scope are approved.
- 2026-07-17 — Temporarily elevated forensic-state containment and remediation above the fork/overlay decision because repository trust and provenance are prerequisites to product identity work.

### Architecture
- The task chain separates inherited-package reproduction from a later schema-first temporal overlay.
- Mutable forensics run state must not be written into tracked live-worktree paths; approved remediation requires out-of-tree or ignored state, exclusive locking, atomic replacement, and worktree identity binding.
- 2026-07-19 — Added architecture and trust-boundary documentation that distinguishes inherited package behavior, local integrity/release controls, and the unimplemented temporal overlay.
- 2026-07-19 — Added a proposed temporal-contract design envelope covering time models, canonicalization, result states, compatibility, fixtures, security, evidence, and rollback without selecting unapproved semantics.
- 2026-07-19 — Added proposed ADR-0001 comparing mirror, maintained-fork, documentation-only, and renamed-derivative identity models; the decision remains blocked by incident closure.
- 2026-07-19 — Added proposed ADR-0002 defining an explicit, additive, read-only temporal-validation boundary separated from inherited query behavior; the proposal remains dependent on P1–P3 approval.

### Documentation
- 2026-07-19 — Added a repository project guide, architecture diagrams, incident-safe developer onboarding, repository-integrity operations playbook, proposed temporal-overlay design, and expanded MkDocs navigation.
- 2026-07-19 — Preserved inherited site and repository metadata while adding an explicit warning that publication identity remains undecided.
- 2026-07-19 — Added authority and claims governance with inherited/observed/configured/implemented/tested/verified/approved/proposed/blocked vocabulary, source-of-truth precedence, update obligations, and publication stop rules.
- 2026-07-19 — Added inherited API and extension-boundary documentation covering stability classes, candidate adapters, forbidden implicit integrations, result separation, compatibility questions, and implementation documentation obligations.
- 2026-07-19 — Added a release-evidence matrix that separates documentation-candidate verification from incident, inherited-runtime, temporal, deployment, and release-approval evidence.
- 2026-07-19 — Expanded the project guide and MkDocs navigation to include governance, API boundaries, release evidence, and architecture decision records.

### Implementation
- Existing upstream-derived code is not recorded as newly completed local work; temporal notes remain proposals until contracts and fixtures exist.
- Reported drift of `.forensics/last_run_epoch.txt` from `1769819269` to `1771791970` is preserved as incident evidence. The available report also identifies `scripts/git_forensics_autocommit.sh` as a writer path and records `Resource deadlock avoided` in another worktree.
- These observations do not prove malicious activity. Benign automation churn, lock contention, unauthorized invocation, hook or scheduler misuse, worktree confusion, and altered provenance remain hypotheses requiring evidence.
- 2026-07-19 — No runtime, schema, query, storage, packaging, hook, scheduler, network, credential, or publication behavior changed in the documentation milestone.

### Security
- The repository is now treated as under a suspected security incident until the writer, invocation path, refs, hooks, remotes, credentials, worktrees, logs, and file metadata are examined and the automation is repaired.
- Do not commit, discard, or normalize the timestamp drift before preserving hashes and metadata.
- Auto-commit or live-worktree mutation touching `.forensics/` must remain disabled until lock-safe remediation and independent replay pass.
- 2026-07-19 — Added a bounded preserve/contain/investigate/repair/independent-validation playbook; the playbook does not close the incident or assert malicious activity.
- 2026-07-19 — Added documentation rules prohibiting unsupported compromise attribution and requiring evidence-qualified incident language.

### Release
- Release remains blocked by the incident gate, fork/scope approval, upstream divergence evidence, current build/test/security results, and provenance.
- 2026-07-19 — Documentation completeness improved, but no build, test, security, provenance, publication, or deployment gate was marked passed.
- 2026-07-19 — Added artifact, digest, replay, review, invalidation, and fail-closed evidence requirements without changing the blocked release decision.

### Deployment
- No package publication under the inherited identity or new temporal product name is authorized.
- Documentation-site deployment remains blocked until repository identity, privacy review, exact-head verification, provenance, and release approval are complete.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
