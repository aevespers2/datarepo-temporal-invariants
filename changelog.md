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

### Implementation
- Existing upstream-derived code is not recorded as newly completed local work; temporal notes remain proposals until contracts and fixtures exist.
- Reported drift of `.forensics/last_run_epoch.txt` from `1769819269` to `1771791970` is preserved as incident evidence. The available report also identifies `scripts/git_forensics_autocommit.sh` as a writer path and records `Resource deadlock avoided` in another worktree.
- These observations do not prove malicious activity. Benign automation churn, lock contention, unauthorized invocation, hook or scheduler misuse, worktree confusion, and altered provenance remain hypotheses requiring evidence.

### Security
- The repository is now treated as under a suspected security incident until the writer, invocation path, refs, hooks, remotes, credentials, worktrees, logs, and file metadata are examined and the automation is repaired.
- Do not commit, discard, or normalize the timestamp drift before preserving hashes and metadata.
- Auto-commit or live-worktree mutation touching `.forensics/` must remain disabled until lock-safe remediation and independent replay pass.
- 2026-07-24 — Changed validation concurrency from mutable pull-request/ref identity to the immutable submitted head, disabled cancellation between exact heads, moved retained evidence outside the checkout, and added a tracked-source mutation assertion. The repair changes validation and provenance only; repository-integrity, release, publication, deployment, credential, and runtime authority remain blocked.

### Release
- Release remains blocked by the incident gate, fork/scope approval, upstream divergence evidence, current build/test/security results, and provenance.
- 2026-07-24 — Exact-head validation remains required before the trusted workflow candidate can merge. A workflow file and successful local construction cannot substitute for a completed GitHub Actions run and retained artifact.

### Deployment
- No package publication under the inherited identity or new temporal product name is authorized.

## Entry Format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
