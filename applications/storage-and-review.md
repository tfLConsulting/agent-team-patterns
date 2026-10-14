# Application: choose the work record and review mechanism

**Principle applied:** intent, evidence, and decisions need durable identity. Isolation, review, and storage are different functions even when one product supplies them together.

| Mechanism | Provides | You must still design |
|---|---|---|
| Markdown + Git | Readable contracts and version history | State discipline, dependency rules, evidence retention |
| Branch/worktree | Isolated edits and revisions | Task identity, reviewer, decision record, eventual integration |
| Pull request | Hosted diff, comments, checks, review, lifecycle | Acceptance contract, authority, workstream synthesis, outcome observation |
| SQLite or service database | Structured queries and transactions | Schema, backups, migration, artifact references, access control |
| Issue/task service | Assignment, workflow, discovery | Evidence binding, code identity, exports, cross-system reconciliation |

## Without PRs

Assign a stable task ID and attempt ID. Preserve the original brief and base revision. Store the result, exact artifact revision or content hash, checks, review, findings, and disposition in a durable record. Use a branch for isolation if needed. Preserve evidence after branch deletion or rebasing, for example in an integrated records directory or a durable artifact store.

A reviewer compares the actual artifact against the original contract and checks the evidence. Record identity, what they inspected, findings, and verdict. An agent editing the author's report is not necessarily an independent review. Integration can still require conflict resolution and renewed checks; acceptance of an old revision does not accept arbitrary later changes.

## With PRs

Use PRs as an adapter: stable IDs, versioned diff, check evidence, and discussion. Keep project decisions and outcome observations accessible beyond one PR. Record whether accepted, merged, released, and observed are different milestones locally. Do not force a research result into an empty code diff just to give it a record.

## With a database

Use transactions for claims and transitions; define uniqueness and recovery. A durable occurrence snapshot prevents a changed task definition from rewriting the acceptance contract of an old run. Retain attempts and receipt identities according to recovery, review, privacy, and accountability needs. Back up records and test export/reconstruction alongside the artifacts they reference.

**Failure modes:** branch disappearance erases evidence; two canonical status stores disagree; a review applies to a different version; a database migration drops history; a merge is mistaken for delivered benefit. The simplest application is the one that preserves necessary distinctions at tolerable cost.
