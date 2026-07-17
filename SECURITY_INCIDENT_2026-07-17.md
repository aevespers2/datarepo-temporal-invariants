# Suspected Security Incident — Forensic Epoch Drift

**Status:** OPEN — containment and investigation required  
**Classification:** Suspected repository-integrity incident; malicious activity is not established  
**Affected surface:** `.forensics/last_run_epoch.txt` and the automation path reported to write it

## Preserved observations

- Previous tracked value: `1769819269`.
- Observed local value: `1771791970`.
- Difference: `1,972,701` seconds.
- Reported original commit: `f76a3ad`, message `forensics(auto): baseline 2026-01-31T00:27:49Z host=Vespers’s MacBook Pro`.
- Reported writer: `scripts/git_forensics_autocommit.sh`.
- Reported error: `Resource deadlock avoided` while writing a `.forensics/last_run_epoch.txt` path in another worktree.
- Reported additional local noise: `.DS_Store` and `.codex/`.

These facts are based on the supplied forensic report and must be independently reproduced before closure.

## Narrative possibilities

1. **Expected automation churn:** a scheduled or manually invoked job updated a tracked run marker.
2. **Lock-contention corruption:** concurrent writers or recursive worktree activity produced stale, partial, or misdirected state.
3. **Cross-worktree contamination:** the automation resolved the wrong repository root or wrote through a shared path.
4. **Unauthorized local invocation:** an unexpected user, process, hook, task runner, launch agent, or IDE invoked the script.
5. **Repository hook misuse:** local or global Git hooks altered evidence or triggered an auto-commit path.
6. **Credential or remote misuse:** an actor changed refs, branches, or automation configuration and left only local drift visible.
7. **False provenance:** the marker, logs, baseline commit description, or timestamps were altered after execution.
8. **Tool defect:** recursion, non-atomic writes, absent locking, or ambiguous path handling caused a misleading security signal.

No narrative is accepted until tested against preserved evidence.

## Immediate containment

- Stop `git_forensics_autocommit.sh` and any scheduler, hook, launch agent, IDE task, or cron entry that can invoke it.
- Do not commit, reset, checkout, clean, or overwrite the changed marker before evidence capture.
- Prevent further writes to tracked `.forensics/` paths.
- Avoid credential rotation unless account, token, hook, or remote misuse is detected; preserve authentication logs first where possible.

## Evidence capture

Retain command output and hashes for:

- `git status --porcelain=v2 --branch`
- `git diff --binary -- .forensics/last_run_epoch.txt`
- `git show HEAD:.forensics/last_run_epoch.txt`
- `git worktree list --porcelain`
- `git reflog --all --date=iso-strict`
- `git remote -v`
- `git config --show-origin --get-regexp 'core\.hooksPath|include|credential|url\..*\.insteadOf'`
- repository and global hook directories
- process, cron, launch-agent, and task-runner configuration
- file metadata and SHA-256 for the marker, script, logs, hooks, and relevant configuration
- recent commits, signatures, branch protection state, deploy keys, tokens, and account audit events where available

## Required technical repair

- Move mutable run epochs and locks outside the repository, or into an explicitly ignored local state directory.
- Never auto-commit mutable session state.
- Resolve repository and worktree identity explicitly before every write.
- Use an exclusive lock scoped to repository identity and worktree path.
- Write to a temporary file, `fsync`, and atomically rename.
- Reject symlinks, path traversal, unexpected owners, and paths outside the intended worktree.
- Emit append-only evidence containing start/end timestamps, process identity, worktree identity, script hash, prior/new state hashes, outcome, and error status.
- Fail closed on lock contention; do not retry recursively or mutate another worktree.

## Verification fixtures

- two concurrent writers
- stale lock recovery
- interrupted write
- recursive invocation
- wrong worktree root
- shared `.git` directory with multiple worktrees
- symlinked state path
- unauthorized owner or permissions
- missing state directory
- read-only worktree
- changed script hash
- changed hook configuration

## Closure criteria

The Architect may close this incident only after:

1. the exact writer and invocation path are identified;
2. refs, commits, hooks, remotes, credentials, and schedulers contain no unexplained activity, or findings are remediated;
3. the state writer is moved out of tracked product paths and made atomic, lock-safe, and worktree-bound;
4. all verification fixtures pass;
5. an independent Inspector replay confirms no unexplained mutation;
6. evidence hashes and rollback instructions are retained.
