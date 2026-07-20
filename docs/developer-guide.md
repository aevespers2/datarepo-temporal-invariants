# Developer Guide

## Before you begin

The repository is under an open, release-blocking integrity investigation. Begin with read-only inspection. Do not run repository automation, hooks, schedulers, build hooks, package publication, documentation deployment, or cleanup commands until the relevant path has been reviewed and explicitly authorized.

The commands below describe the intended contributor workflow. They are not evidence that the current candidate passes installation, testing, documentation, or security gates.

## Prerequisites

- Git with worktree support;
- Python 3.10 or newer for the current source tree;
- an isolated virtual environment;
- no globally configured Git hook path affecting the checkout;
- no scheduled invocation of repository scripts;
- enough local disk space for Python, Arrow, Polars, Delta Lake, documentation, and test dependencies.

`pyproject.toml` still declares Python 3.8 compatibility, while current source annotations require Python 3.10 or newer and existing CI uses Python 3.10. Treat that metadata mismatch as a release blocker rather than evidence of Python 3.8 support.

## 1. Establish repository identity

Run read-only checks first and retain their output when working on incident or release evidence:

```bash
git rev-parse --show-toplevel
git rev-parse --git-dir
git rev-parse HEAD
git status --porcelain=v2 --branch
git worktree list --porcelain
git remote -v
git config --show-origin --name-only --get-regexp \
  'core\.hooksPath|include|credential|url\..*\.insteadOf' || true
```

Confirm that the resolved repository root and worktree are the intended paths. Stop if the checkout contains unexplained changes, unexpected hooks, unknown remotes, or an active process that may write into `.forensics/`. Do not retain raw credential-bearing remote or configuration values in shared evidence.

## 2. Inspect before execution

Review these files before running any automation:

- `SECURITY_INCIDENT_2026-07-17.md`;
- `taskchain.md`;
- `release.md`;
- `deploy.md`;
- `pyproject.toml`;
- `requirements-validation.txt`;
- any script, hook, task, or build hook that the intended command may invoke.

Do not normalize, discard, or overwrite incident evidence. In particular, avoid `git reset --hard`, `git clean`, forced checkout, or automated formatting across the repository until relevant evidence is captured.

## 3. Create a validation-only Python environment

The project defines a custom Hatch build hook that runs the static-site asset toolchain during package builds. An editable package installation can therefore invoke unreviewed Node and network work. Do not use `pip install -e .` or build the package during incident-safe onboarding.

After reviewing `requirements-validation.txt`, prepare a validation-only environment:

```bash
python3.10 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --requirement requirements-validation.txt
export PYTHONPATH="$PWD/src"
```

Record the exact Python, pip, operating-system, architecture, and dependency versions used:

```bash
python --version
python -m pip --version
python -m pip freeze > .local-dependency-snapshot.txt
```

Keep local environment snapshots out of commits unless a reviewed evidence format explicitly requires them.

## 4. Run bounded checks

Prefer targeted, deterministic checks before broader validation:

```bash
PYTHONPATH=src python -m compileall -q src/datarepo
PYTHONPATH=src python -m pytest -q test
black --check src/datarepo
flake8 src/datarepo --count --select=E9,F63,F7,F82 --show-source --statistics
mypy src/datarepo
mkdocs build --strict --site-dir site
```

The inherited test tree is `test/`, not `tests/`. Formatting and lint checks are scoped to `src/datarepo`, matching the inherited workflow. A command that is unavailable, misconfigured, or unexpectedly invokes network/build automation should fail the review rather than be replaced silently.

For accepted evidence, record:

- exact commit and worktree;
- exact command;
- start/end timestamps;
- exit code;
- complete output or retained report;
- tool and dependency versions;
- generated files and SHA-256 hashes;
- any network, credential, subprocess, or build-hook activity.

## 5. Build documentation locally

A clean documentation build does not require the inherited web-catalog generator. The documentation hook omits the catalog preview when reviewed generated assets are absent.

```bash
mkdocs build --strict --site-dir site
```

Use `mkdocs serve` only after reviewing `mkdocs.yml`, `docs/hooks.py`, referenced JavaScript/CSS, and generated output. The documentation site is not approved for deployment while the release and integrity gates remain blocked.

The optional web catalog is a separate, executable generation path with Python, package, Node, and data dependencies. Do not generate or embed it until that path is independently reviewed and authorized. Review the generated `site/` directory for private endpoints, credentials, data samples, absolute local paths, inherited branding, broken links, and unapproved product claims before retaining it as an artifact.

## 6. Understand the package model

The inherited API exposes catalog, database, table, lazy-dataframe, and export concepts. Start with:

- `docs/README.md` for the package overview;
- `docs/user-guide.md` for table, database, catalog, query, and caching examples;
- `docs/api-docs.md` for generated reference entry points;
- `src/datarepo/core/__init__.py` for the public core exports;
- `pyproject.toml` for package metadata and dependency constraints.

Treat the upstream-oriented examples as inherited documentation. Do not imply that local temporal behavior exists unless it is implemented, tested, versioned, and approved.

## 7. Make a scoped documentation change

1. Select a `READY` task or a documentation correction that does not alter implementation scope.
2. Identify inherited statements, local statements, and proposed statements explicitly.
3. Update diagrams and cross-links together.
4. Add a changelog entry with evidence.
5. Run Markdown/MkDocs checks and inspect generated output.
6. Confirm that `taskchain.md` and `release.md` statuses remain accurate.
7. Open a pull request that states what is documented, what remains unverified, and whether architecture approval is required.

## 8. Future temporal-overlay work

Do not add validators, schemas, package names, commands, or compatibility promises until P0–P3 are complete. The first approved implementation task must specify:

- input schema and time model;
- canonical form and deterministic serialization;
- validation result schema;
- positive and negative fixtures;
- compatibility and migration rules;
- failure behavior and resource bounds;
- security and privacy assumptions;
- rollback to the inherited baseline.

## Pull-request evidence checklist

- [ ] Scope is documentation-only or explicitly approved.
- [ ] Inherited, local, and proposed behavior are distinguished.
- [ ] No incident evidence was removed or normalized.
- [ ] No release/deployment gate is falsely marked complete.
- [ ] Diagrams render with supported Mermaid syntax.
- [ ] Internal links resolve in MkDocs.
- [ ] Commands are reproducible or clearly labeled unverified.
- [ ] Generated-site review found no sensitive content.
- [ ] Changelog and planning references are aligned.
- [ ] Rollback is a simple revert of the documentation commits.

## Troubleshooting and stop rules

- **Unexpected tracked mutation:** stop, preserve hashes and metadata, and follow the repository-integrity playbook.
- **Dependency resolution changes:** retain the resolver output; do not widen constraints without an approved task.
- **Build hook performs unexpected work:** terminate safely, preserve logs, and treat it as a supply-chain finding.
- **Docs expose private data:** do not publish; remove the source exposure and regenerate from reviewed inputs.
- **Tests fail outside scope:** document the failure and stop rather than broadening the patch.
- **Repository identity remains unclear:** restrict work to reviewable documentation and request the architectural decision recorded in `taskchain.md`.
