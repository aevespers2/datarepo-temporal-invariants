# Punch List

This punch list implements the sequencing and evidence requirements in `taskchain.md` and `release.md`. A checked documentation item means the file exists in this candidate; it does not close the integrity incident, approve repository identity, prove runtime behavior, certify accessibility, or authorize publication.

## P0 — Repository-integrity incident

- [ ] Preserve committed and observed `.forensics/last_run_epoch.txt` values, binary-safe copies, metadata and SHA-256 hashes.
- [ ] Identify every writer, invocation path, hook, scheduler, task runner, process, worktree and repository identity involved.
- [ ] Capture refs, reflogs, remotes, relevant Git configuration names without secret values, ownership and filesystem evidence.
- [ ] Disable tracked-state auto-commit and live-worktree mutation affecting `.forensics/`.
- [ ] Approve or revise ADR-0003's separation of local operational state, immutable run evidence and reviewed repository evidence.
- [ ] Move mutable run state out of tracked product paths or into an explicitly ignored and ownership-checked location.
- [ ] Implement exclusive locking, atomic write/`fsync`/rename, path validation and worktree binding under a separately approved implementation task.
- [ ] Pass concurrent, interrupted, stale-lock, recursive, wrong-worktree, shared-`.git`, symlink, unauthorized-owner, read-only, changed-script and changed-hook fixtures.
- [ ] Complete independent replay and record residual risk.
- [ ] Obtain explicit Architect incident-closure approval.

## P0D — Documentation candidate

- [x] Add a safety-first Pages/MkDocs homepage that separates inherited, observed, proposed and blocked claims.
- [x] Document inherited package architecture, local control architecture and the proposed temporal overlay separately.
- [x] Add trust-boundary, authority/claims, API/extension, developer, integrity-operations and release-evidence guidance.
- [x] Add proposed ADRs for repository identity and temporal-overlay isolation.
- [x] Add obstruction and gluing analysis with pairwise edges, triple overlaps, fail-closed conditions and repair order.
- [x] Add ADR-0003 separating mutable operational state, immutable run evidence and reviewed repository evidence.
- [x] Add an accessibility and review-evidence guide separating source, rendered, generated, inherited-export, temporal-report and governance surfaces.
- [x] Define exact-artifact binding, review states, diagram/prose integrity, keyboard/focus, zoom/reflow, contrast/motion, screen-reader, privacy, correction and fail-closed evidence requirements.
- [x] Add this punch list and align it with `taskchain.md`, `release.md` and `changelog.md`.
- [x] Replace credential-bearing publication with least-privilege validation-only workflow behavior in the candidate.
- [ ] Obtain an exact-head GitHub Actions run for the final candidate.
- [ ] Pass strict MkDocs build, internal-link review, Mermaid rendering and generated-site boundary inspection.
- [ ] Complete rendered keyboard, visible-focus, 200%/400% zoom and reflow, contrast, reduced-motion, screen-reader and plain-language reviews against one retained exact artifact.
- [ ] Complete privacy and sensitive-data review for rendered pages, generated API content, inherited static exports, asset failures and incident records.
- [ ] Retain an immutable documentation and accessibility evidence record plus digest tied to the final head.
- [ ] Record omitted checks and limitations; do not infer certification from automated validation.

## P1 — Repository and product identity

- [ ] Record the exact upstream commit and imported history relationship.
- [ ] Complete the divergence manifest and identify inherited versus local files and commits.
- [ ] Approve one identity: mirror, maintained fork, documentation-only overlay or renamed derivative.
- [ ] Approve repository, package, distribution and Pages-site names.
- [ ] Preserve upstream license, notices, attribution and support boundaries.
- [ ] Define publication target, security contact, support owner, migration path and rollback.
- [ ] Prevent competing publication under inherited and local identities.

## P2 — Inherited `data-repository` 0.0.2 baseline

- [ ] Resolve Python metadata versus source-syntax support and approve the supported-version matrix.
- [ ] Produce a clean, offline-capable installation and build procedure.
- [ ] Run the complete inherited tests, formatting, linting, typing, documentation and smoke checks at one immutable commit.
- [ ] Review the custom Hatch/Node build hook, subprocesses, generated assets and network behavior.
- [ ] Produce dependency inventory, vulnerability review, SBOM, source archive, sdist, wheel and SHA-256 manifest.
- [ ] Verify static catalog and ROAPI exports without treating generated configuration as authorization.
- [ ] Review the inherited static catalog and ROAPI-facing human documentation for keyboard, table, state, error, privacy and remote-asset accessibility.
- [ ] Record reproducibility limits and rollback to the inherited baseline.

## P3 — Temporal-invariant contract

- [ ] Approve first users, use cases and subject granularity.
- [ ] Assign canonical owners for subject identity, contract schema, result schema, canonicalization and semantic versioning.
- [ ] Approve clock, ordering, window, late/missing data and uncertainty semantics.
- [ ] Specify canonical bytes for Unicode, timestamps, decimals, floats, nulls, schemas, paths, maps, sets and binary references.
- [ ] Define `pass`, `fail`, `indeterminate` and `error` semantics and portfolio-wide severity mapping.
- [ ] Define text-equivalent result, uncertainty, correction, revocation, stale and authority-state communication that never collapses non-pass states into pass.
- [ ] Define compatibility, migration, correction, revocation, retention and replay policies.
- [ ] Define bounded resource, no-network, hostile-input and privacy requirements.
- [ ] Create positive, negative, adversarial, migration and replay fixtures.
- [ ] Keep validator evidence separate from enforcement, release, deployment, payment or canonical-state authority.
- [ ] Obtain explicit `READY` status before implementation.

## P3G — Cross-repository gluing

- [ ] Approve the QSO-SEEKER canonical-record to observation-adapter contract.
- [ ] Approve the temporal-result to Bridge evidence-envelope contract.
- [ ] Approve Bridge to QSO-STUDIO/AionUi display, verification, stale and revoked-state contract.
- [ ] Approve Repository `0` task proposal to Repository `1` capability to remote-adapter contract.
- [ ] Name the issuer, revoker, credential owner, data-governance owner and incident owner for remote observations.
- [ ] Prove Seeker → observation → validator identity/provenance overlap with deterministic fixtures.
- [ ] Prove Repository `0` → Repository `1` → adapter denial and expiry behavior.
- [ ] Prove validator → Bridge → UI status, limitation and accessible text-equivalence preservation.
- [ ] Prove validator → policy → release/deployment separation of evidence and authority.
- [ ] Prove incident/revocation propagation through evidence stores, interfaces and caches with bounded restart.

## Security, privacy and operations

- [ ] Classify catalog schemas, samples, source URIs, endpoints, credentials and result payloads.
- [ ] Define field-level static-site publication and redaction policy.
- [ ] Ensure custom Python table functions are never executed implicitly during documentation or schema inspection.
- [ ] Define least-privilege remote-data credentials, rotation, expiry and revocation outside repository history and browser storage.
- [ ] Define result/evidence correction, invalidation, withdrawal and retention procedures.
- [ ] Verify that missing local assets, blocked remote assets, absent generated API content and optional inherited catalog files fail legibly without leaking private paths or data.
- [ ] Run a portfolio emergency-stop and recovery tabletop covering this repository, Repository `1`, Bridge and interfaces.
- [ ] Record monitoring, alert, incident, rollback and post-recovery evidence owners.

## Release and deployment

- [ ] Keep package, site, release and remote integration deployment blocked while P0 is open.
- [ ] Tie every candidate artifact to an immutable source head and complete evidence manifest.
- [ ] Require independent review of provenance, security, privacy, compatibility, accessibility and rollback.
- [ ] Obtain explicit release approval after all blocking gates pass.
- [ ] Retain rejected-candidate and incident evidence without exposing secrets or private data.