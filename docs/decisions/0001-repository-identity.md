# ADR-0001: Repository Identity and Publication Authority

- **Status:** Proposed — decision blocked by P0 incident closure
- **Date:** 2026-07-19
- **Decision owner:** Architect
- **Related records:** `taskchain.md` P1, `release.md`, `deploy.md`, repository-integrity incident record

## Context

`datarepo-temporal-invariants` contains an inherited `data-repository` 0.0.2 codebase, upstream-oriented documentation and metadata, local governance and incident records, and design material for a possible temporal-invariant overlay. The repository does not yet have an approved identity as an upstream mirror, maintained fork, documentation-only overlay, or renamed derivative.

The identity decision determines:

- what the repository is authoritative for;
- how upstream history and attribution are represented;
- whether package names and imports remain inherited or become differentiated;
- who owns maintenance, security response, releases, and support;
- whether GitHub Pages may use inherited site metadata;
- where a future temporal overlay belongs;
- how users distinguish inherited behavior from local work.

The decision must not be finalized while repository provenance is under an open integrity incident.

## Decision drivers

- Preserve exact upstream provenance and license obligations.
- Avoid implying endorsement, maintenance, or publication authority that has not been granted.
- Prevent package-name or documentation-site confusion.
- Isolate local temporal design from inherited behavior.
- Support reproducible comparison with the upstream baseline.
- Permit rollback to an immutable inherited state.
- Provide a clear security, maintenance, and release owner.
- Keep migration costs proportional to the approved product objective.

## Options

### Option A — Read-only upstream mirror

The repository preserves upstream history and artifacts with minimal local additions.

**Advantages**

- simplest provenance story;
- minimal behavioral divergence;
- useful for reproducible baseline review.

**Costs and risks**

- local governance and temporal design do not naturally belong in the mirror;
- publication can be confused with upstream authority;
- local fixes may create ambiguity unless separated.

**Required controls**

- exact upstream sync policy;
- no local package publication;
- local evidence and planning stored in a separate repository or branch model;
- prominent mirror status and upstream links.

### Option B — Maintained fork

The repository owns a differentiated fork of the inherited package.

**Advantages**

- allows reviewed fixes and ongoing maintenance;
- keeps inherited architecture available for extension;
- can establish local release and security processes.

**Costs and risks**

- highest maintenance and compatibility burden;
- requires differentiated package/release identity;
- may create user confusion if upstream branding remains;
- temporal work could silently alter inherited behavior without strong boundaries.

**Required controls**

- exact fork point and divergence ledger;
- approved new package/release/site identity;
- license/notices and attribution review;
- supported Python/dependency matrix;
- compatibility, migration, support, security, and release ownership.

### Option C — Documentation-only temporal overlay

The repository retains contracts, schemas, examples, and evidence design without executable package changes.

**Advantages**

- lowest runtime and supply-chain risk;
- separates semantic review from implementation;
- useful for cross-repository contract alignment.

**Costs and risks**

- does not provide executable validation;
- inherited code may be unnecessary or misleading;
- requires a clear reason to retain the upstream tree.

**Required controls**

- remove or isolate inherited code if not needed for reference;
- differentiated Pages identity;
- explicit non-executable status;
- contract ownership and versioning policy.

### Option D — Renamed derivative with separate temporal package

The repository becomes a differentiated derivative and places the temporal overlay in a separate package or namespace.

**Advantages**

- clearest local ownership and product boundary;
- overlay can be independently versioned and removed;
- reduces silent compatibility claims.

**Costs and risks**

- migration and packaging work;
- duplicate maintenance if inherited code is retained;
- requires complete identity, compatibility, and support decisions.

**Required controls**

- approved derivative name and namespace;
- exact upstream attribution and divergence;
- explicit dependency or adapter boundary;
- independent release artifacts and documentation;
- rollback to the inherited baseline.

## Proposed decision

No option is accepted yet. After P0.2 independent incident validation, the Architect should select one option using a recorded comparison of:

- intended users and first bounded use case;
- need for executable inherited-package maintenance;
- need for executable temporal validation;
- ownership and long-term support capacity;
- package/site naming and publication targets;
- license and notice requirements;
- security response and release authority;
- migration and rollback cost.

Until then, treat the repository as an **unreleased evaluation workspace containing an inherited baseline, local evidence/governance records, and proposed temporal design**.

## Interim rules

- Do not tag or publish a package.
- Do not deploy GitHub Pages under inherited site identity.
- Preserve upstream attribution and links as inherited metadata.
- Do not claim maintained-fork status.
- Do not describe temporal capability as implemented.
- Keep incident and local governance records distinguishable from upstream material.
- Record any upstream sync or local code change with exact provenance.
- Keep release and deployment blocked.

## Acceptance criteria

ADR-0001 may become `Accepted` only when:

- the integrity incident is explicitly closed;
- exact upstream baseline and local divergence are established;
- license and notice obligations are reviewed;
- intended users, product objective, and first bounded workflow are approved;
- package, repository, and Pages identities are approved;
- maintenance, security, review, support, and release owners are named;
- temporal-overlay placement is decided;
- compatibility, migration, provenance, publication, and rollback requirements are documented;
- `taskchain.md`, `release.md`, `deploy.md`, `changelog.md`, MkDocs metadata, and project overview are updated consistently.

## Consequences after acceptance

The accepted identity will determine which inherited files remain, which metadata changes, where executable work occurs, what can be published, and how compatibility is described. Any incompatible future identity change requires a superseding ADR and migration plan.

## Rejection and rollback

If identity cannot be established without confusing users or misrepresenting upstream authority, the safe default is to archive the evaluation workspace or retain it privately as evidence/reference only. Rejected publication artifacts must remain unpublished, and preserved incident/provenance records must not be deleted during cleanup.
