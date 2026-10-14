# Contrasting design cases

These fictional cases are design walkthroughs, not execution receipts or claims of measured success. Unlike the runnable ledger's intentionally narrow schema, they show decisions that do not fit one task pipeline.

## A small local repair

An operator asks for a broken delimiter in a local exporter to be fixed. The failure is reproducible. There is no unresolved product direction, and existing authority covers a local reversible edit.

The plan can be a few lines beside the request: reproduce, repair, check the failing case and relevant boundaries. The operator can use self-check plus the regression test. A standalone task and a Git revision may preserve enough evidence; no standing workstream, separate reviewer occurrence, position paper, or disposition sitting is necessary.

The decision is acceptance under the local contribution policy. Distribution to another user, if needed, is a separate question. The remaining untested consumer behavior is recorded only to the extent that someone relies on compatibility. The acceptance criterion can be satisfied without claiming a measured reduction in support demand.

**Design test:** would added records or agents change the confidence or authority of the decision enough to justify their cost?

## An investigation changes the plan

A team is considering a different exchange format. It has not established which external consumers must remain compatible. Two research tasks recommend a format, but the available sources do not resolve an important consumer requirement.

The team distinguishes work not yet done from a question its current access cannot answer. It records the attempted methods and the decision exposed by the gap. The decision maker may authorise a reversible prototype with explicit limits, obtain the missing access, or stop the proposal. Completing more research tasks is not automatically progress.

During the prototype, a new fixture contradicts an assumption in the accepted recommendation. The new evidence can be correct while the implementation is safe to integrate locally. Acceptance of the evidence does not keep the original direction valid. The affected design is reopened, dependent rollout work is reconsidered, and the earlier recommendation is linked to its correction. Important findings reach their reader without waiting for the final workstream report.

**Design test:** can the system withdraw an accepted premise and stop dependent work, rather than merely append another green task?

## A recurring service check with an external action

A small operations repo periodically checks a dataset's freshness. It uses an existing scheduler and a shared service for state. It needs neither a fresh manual bootstrap nor branches for observations. The task can remain in the same service workflow while readiness, review, and occurrence identity are tracked separately.

A read-only observation can report no change and close under policy. A stale dataset may justify a proposed repair; publication requires a different existing permission. Review of the repair checks the actual dataset and source, not merely whether the report looks complete. An accepted proposal does not count as a published update.

If an observation is missed, the project chooses whether to catch up or inspect only the newest state. It also distinguishes a quiet successful check from a runner that never executed. Time-bounded observation after a repair can finish; the continuing service obligation can persist.

**Design test:** do occurrence semantics, authority, and health evidence work without forcing every observation through a finite development workstream?

## What these cases do not prove

They demonstrate why design choices differ; they do not establish empirical benefits. The [manual ledger](manual-ledger/README.md) tests mechanical helpers only. A useful adoption pilot should cover the target project's awkward case—changed direction, partial evidence, or a mixed-authority action—as well as its happy path.
