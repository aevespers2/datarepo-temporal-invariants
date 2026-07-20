# Repository-Integrity Operations

## Purpose

This playbook converts the open forensic-epoch incident requirements into a bounded operator sequence. It supplements `SECURITY_INCIDENT_2026-07-17.md`; it does not close the incident, identify an actor, or authorize destructive remediation.

## Governing rule

Preserve first, contain second, investigate third, repair fourth, validate independently, and only then request closure.

```mermaid
flowchart LR
    O[Observation] --> P[Preserve evidence]
    P --> C[Contain writers]
    C --> I[Identify writer and invocation path]
    I --> R[Repair mutable-state design]
    R --> V[Independent replay]
    V -->|all criteria pass| A[Architect closure decision]
    V -->|failure or ambiguity| P
```

## Roles

| Role | Responsibility |
|---|---|
| Architect | Defines scope, approves containment, accepts residual risk, and closes or continues the incident |
| Inspector | Captures evidence, tests competing hypotheses, and independently replays the repaired path |
| Builder | Implements only the approved state-handling repair and fixtures |
| Repository owner | Reviews account, token, deploy-key, branch, workflow, and audit evidence available through GitHub |

A single person may perform multiple roles, but the independent replay must be clearly separated from the repair evidence.

## Phase 1 — Preserve

Capture without editing the affected files. The following example handles an absent tracked marker, refuses a symlinked observed marker, redacts remote credentials, records sensitive Git configuration names without values, and writes the checksum manifest atomically after hashing every other evidence file.

```bash
umask 077
mkdir -p "$HOME/datarepo-incident-evidence"
EVIDENCE="$HOME/datarepo-incident-evidence/$(date -u +%Y%m%dT%H%M%SZ)"
mkdir -p "$EVIDENCE"

# Read-only repository and worktree observations.
git status --porcelain=v2 --branch > "$EVIDENCE/git-status.txt"
git diff --binary -- .forensics/last_run_epoch.txt > "$EVIDENCE/marker.diff"
git worktree list --porcelain > "$EVIDENCE/worktrees.txt"
git reflog --all --date=iso-strict > "$EVIDENCE/reflog.txt"

# Preserve the committed marker only when it exists at the selected commit.
if git cat-file -e HEAD:.forensics/last_run_epoch.txt 2>/dev/null; then
  git show HEAD:.forensics/last_run_epoch.txt > "$EVIDENCE/marker.committed.txt"
else
  printf 'HEAD does not contain .forensics/last_run_epoch.txt\n' \
    > "$EVIDENCE/marker.committed.absent.txt"
fi

# Preserve an observed marker only when it is a regular, non-symlink file.
if [ -f .forensics/last_run_epoch.txt ] && [ ! -L .forensics/last_run_epoch.txt ]; then
  cp -p .forensics/last_run_epoch.txt "$EVIDENCE/marker.observed.txt"
else
  printf 'Observed marker is absent or is not an approved regular file\n' \
    > "$EVIDENCE/marker.observed.absent-or-rejected.txt"
fi

# Redact URL user information, query strings, and fragments before retention.
REMOTE_TMP="$(mktemp "${TMPDIR:-/tmp}/datarepo-remotes.XXXXXX")"
git remote -v > "$REMOTE_TMP"
python - "$REMOTE_TMP" "$EVIDENCE/remotes.redacted.txt" <<'PY'
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit

source = Path(sys.argv[1])
output = Path(sys.argv[2])
redacted = []
for raw in source.read_text(encoding="utf-8", errors="replace").splitlines():
    fields = raw.split()
    if len(fields) < 2:
        continue
    name, value, *rest = fields
    if "://" in value:
        parsed = urlsplit(value)
        host = parsed.hostname or ""
        if parsed.port:
            host = f"{host}:{parsed.port}"
        value = urlunsplit((parsed.scheme, host, parsed.path, "", ""))
    elif re.match(r"^[^/@\s]+@[^:\s]+:.+", value):
        value = re.sub(r"^[^@]+@", "[REDACTED]@", value)
    redacted.append("\t".join([name, value, *rest]))
output.write_text("\n".join(redacted) + ("\n" if redacted else ""), encoding="utf-8")
source.unlink(missing_ok=True)
PY

# Retain configuration origins and key names, never credential-bearing values.
git config --show-origin --name-only --get-regexp \
  'core\.hooksPath|include|credential|url\..*\.insteadOf' \
  > "$EVIDENCE/git-config-sensitive-keys.txt" 2>&1 || true

# Build the manifest outside the evidence tree and atomically install it last.
EVIDENCE="$EVIDENCE" python - <<'PY'
from hashlib import sha256
from pathlib import Path
import os

root = Path(os.environ["EVIDENCE"]).resolve()
lines = []
for path in sorted(root.rglob("*")):
    if not path.is_file() or path.name == "SHA256SUMS":
        continue
    digest = sha256(path.read_bytes()).hexdigest()
    lines.append(f"{digest}  {path.relative_to(root).as_posix()}")
temporary = root.parent / f".{root.name}.SHA256SUMS.tmp"
temporary.write_text("\n".join(lines) + "\n", encoding="utf-8")
os.replace(temporary, root / "SHA256SUMS")
PY
```

Also preserve file metadata, relevant scripts, hook directories, scheduler definitions, process listings, IDE/task-runner configuration, logs, refs, recent commits, signatures, and account audit information where available.

Do not place secrets into the repository evidence bundle. Record the existence, scope, identifier, and review result of credentials without copying secret values.

## Phase 2 — Contain

- stop scheduled, hooked, IDE-triggered, launch-agent, cron, or manual execution of the reported writer;
- prevent further tracked writes under `.forensics/`;
- do not delete the script, marker, logs, or lock artifacts before preservation;
- do not rotate credentials unless evidence establishes a credential-related trigger or containment need;
- avoid working in multiple linked worktrees until identity and lock behavior are understood;
- do not publish, tag, deploy, or activate workflows.

Record every containment action, operator, time, affected path/process, and rollback method.

## Phase 3 — Hypothesis testing

| Hypothesis | Minimum evidence |
|---|---|
| Expected automation churn | authorized scheduler/task definition, execution logs, matching process identity, expected worktree, expected timestamp transition |
| Lock contention or recursion | reproducible concurrent/recursive invocation and matching deadlock/error behavior |
| Cross-worktree contamination | path-resolution trace demonstrating a write to a different worktree or shared state path |
| Unauthorized local invocation | process, shell, IDE, scheduler, account, or filesystem evidence tying execution to an unapproved source |
| Hook misuse | repository/global hook contents, hashes, configuration origin, and invocation evidence |
| Credential or remote misuse | unexplained refs, commits, deploy keys, tokens, sessions, workflow runs, or audit events |
| False provenance | inconsistent hashes, metadata, timestamps, logs, commit claims, or evidence-chain gaps |
| Tool defect | code review and deterministic fixture reproducing non-atomic, unlocked, path-ambiguous, or recursive behavior |

Classify each hypothesis as supported, contradicted, inconclusive, or not testable, with evidence references. Do not collapse “inconclusive” into “benign” or “malicious.”

## Phase 4 — Required repair design

Mutable state should live outside tracked product paths and be bound to explicit repository identity.

```mermaid
flowchart TB
    INV[Invocation] --> ID[Resolve repository and worktree identity]
    ID --> AUTH[Validate path, owner, permissions, script and hook hashes]
    AUTH --> LOCK[Acquire exclusive identity-scoped lock]
    LOCK --> READ[Read prior state]
    READ --> TMP[Write temporary file]
    TMP --> SYNC[Flush and fsync]
    SYNC --> REN[Atomic rename]
    REN --> LOG[Append evidence record]
    LOG --> UNLOCK[Release lock]

    ID -->|ambiguous| FAIL[Fail closed]
    AUTH -->|invalid| FAIL
    LOCK -->|contended| FAIL
    TMP -->|error| FAIL
```

The repair must:

- store run epochs and locks outside the repository or in an explicitly ignored local state directory;
- never auto-commit session state;
- bind locks and state to both repository identity and worktree path;
- reject symlinks, traversal, unexpected ownership, and unauthorized paths;
- use exclusive locking, temporary writes, flush/`fsync`, and atomic rename;
- fail closed without recursive retry or cross-worktree fallback;
- append start/end timestamps, process identity, worktree identity, script hash, prior/new hashes, outcome, and errors.

## Phase 5 — Verification matrix

| Fixture | Expected result |
|---|---|
| Two concurrent writers | one succeeds; the other fails closed without mutation |
| Stale lock | deterministic, authorized recovery with evidence |
| Interrupted write | prior valid state remains intact |
| Recursive invocation | inner invocation is rejected |
| Wrong worktree root | no write occurs |
| Shared `.git` with multiple worktrees | state and locks remain isolated |
| Symlinked state path | rejected before write |
| Unauthorized owner/permissions | rejected and logged |
| Missing state directory | created only at the approved out-of-tree location, or fails closed |
| Read-only worktree | no product-path mutation |
| Changed script hash | rejected or explicitly re-approved |
| Changed hook configuration | detected and surfaced |

Retain command lines, environments, exit codes, logs, output files, and hashes for each fixture.

## Independent validation

The Inspector should start from the preserved failure description, reproduce the unsafe behavior where possible in an isolated fixture repository, then verify the repair without relying on the Builder's conclusions. Validation must include repository and worktree identity, evidence-hash verification, negative tests, interruption tests, and a check for unexplained mutation.

## Closure packet

The Architect requires:

- preserved original and observed marker evidence;
- writer and invocation-path determination;
- hypothesis disposition table;
- containment record;
- repair design and reviewed patch;
- complete fixture results;
- independent replay report;
- repository/account integrity review;
- residual-risk statement;
- tested rollback instructions;
- explicit closure decision and date.

Until that packet is accepted, `taskchain.md`, `release.md`, and `deploy.md` remain blocked.

## Rollback

If the repair introduces new writes, loses evidence, permits ambiguous identity, fails concurrency or interruption tests, or changes inherited product behavior, stop the writer, preserve the new evidence, revert only the repair commits, and restore the last independently verified state. Do not rewrite incident history or delete failed evidence.
