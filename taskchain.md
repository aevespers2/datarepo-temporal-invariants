# Task Chain

Architect owns task dependencies, sequencing, acceptance criteria, and boundaries. Builders preserve upstream provenance, tests, evidence, and rollback paths.

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Contain, investigate, and technically remediate the unexplained tracked mutation of `.forensics/last_run_epoch.txt` as a suspected security incident before resuming fork/overlay product work.
- **User outcome:** A developer can prove which process changed forensic state, verify that no unauthorized repository or credential activity occurred, and run the forensics automation without cross-worktree contamination or tracked-state churn.
- **MVP scope:** preserve the current and committed marker values; capture hashes, logs, worktree state, hooks, scheduler/process evidence, refs, and script identity; disable live-worktree auto-writes; move mutable state out of tracked product paths; add lock-safe atomic writes and cross-worktree isolation tests; document root cause, residual risk, and rollback.
- **Priority:** Incident containment temporarily supersedes the existing mirror/fork/overlay identity decision because provenance and repository trust are prerequisites to every later product decision. This is a documented security-driven reprioritization, not evidence that malicious activity has been proven.
- **Success criteria:** the writer and execution path are identified; competing benign and adversarial hypotheses are tested; no unexplained refs, commits, hooks, tokens, remotes, or scheduler activity remain; mutable forensic state is ignored or stored out-of-tree; concurrent, interrupted, stale-lock, unauthorized-path, and cross-worktree tests pass; evidence is retained; Architect explicitly closes the incident.
- **Non-goals:** assuming malicious intent without evidence, deleting or normalizing the drift before preservation, committing timestamp churn, rotating all credentials without a trigger, or resuming publication while provenance remains uncertain.
- **Release rationale:** No inherited package or temporal overlay can be trusted while tracked forensic evidence can change through an unclear or unsafe automation path.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Contain and investigate forensic state drift | Architect / Inspector | — | IN PROGRESS | Evidence is preserved; automation writes are disabled; writer, invocation path, worktree, refs, hooks, and credentials are examined; hypotheses are dispositioned. |
| P0.1 | Repair forensics state handling | Builder | P0 evidence capture | BLOCKED | Mutable run state is out-of-tree or ignored; writes are atomic, exclusively locked, worktree-bound, and fail closed; concurrency and isolation tests pass. |
| P0.2 | Independent incident validation | Inspector | P0.1 | BLOCKED | Inspector reproduces the prior failure mode, confirms the repair, checks evidence integrity, and finds no unexplained repository mutation. |
| P1 | Approve mirror/fork/overlay/derivative identity | Architect | P0.2 and User approval | BLOCKED | Exact upstream baseline, local divergence, package/release name, license/notices, publication target, and temporal-overlay boundary are approved. |
| P2 | Reproduce the inherited `data-repository` 0.0.2 baseline | Architect | P1 | PROPOSED | Clean build/install, complete tests, format/lint/type/docs/smoke checks, dependency/security review, commands, and provenance pass at one immutable commit. |
| P3 | Define a schema-first temporal-invariant contract | Architect | P2 | PROPOSED | Problem statement, users, inputs/outputs, canonical semantics, compatibility, migration, non-goals, fixtures, and rollback are Builder-ready without modifying upstream behavior silently. |
| P4 | Implement the approved overlay separately | Builder | P3 | PROPOSED | Versioned schemas/validators and deterministic positive/negative fixtures pass; packaging and documentation preserve upstream/local separation. |

## Documentation support

The GitHub Pages/MkDocs material documents the inherited package, current incident boundary, developer stop rules, release posture, and a non-binding temporal-overlay design envelope. It supports P0–P3 review but does not change task status, close the incident, approve repository identity, or authorize implementation/publication.

## Builder Log

Record incident evidence hashes, current and committed marker values, script and log hashes, worktree list, hooks, refs, scheduler/process evidence, lock behavior, root cause, commands/results, tests, rollback, approval decisions, upstream and local commits, package artifacts, dependency/security findings, schema/fixture hashes, migration evidence, and follow-ups.

- 2026-07-17 — Reclassified the tracked `.forensics/last_run_epoch.txt` drift as a suspected security incident until disproven. Reported evidence indicates a shift from `1769819269` to `1771791970`, an automation writer path, and a `Resource deadlock avoided` error in another worktree. The change may be benign automation churn, lock contention, unauthorized invocation, worktree confusion, or false provenance; no hypothesis is accepted without evidence.
- 2026-07-19 — Added a documentation-only project guide, architecture/trust-boundary model, incident-safe onboarding guide, repository-integrity operations playbook, proposed temporal-overlay design envelope, and expanded MkDocs navigation. No implementation, incident, release, deployment, or identity status changed.
