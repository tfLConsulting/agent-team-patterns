# Bounded execution and honest recovery

**Principle:** a run should leave a result that another session can reconcile. More execution should not automatically create more work than anyone can evaluate.

Choose eligible work using dependencies, priorities, readiness, and authority. A task blocked on evidence should carry the evidence needed and an observable wake condition; a date alone does not resolve it. Recurring obligations need an occurrence policy for missed periods: catch up, coalesce, or skip explicitly. Keep deadlines distinct from earliest useful start dates.

Set work-in-progress limits at the scarce resource: review capacity, release capacity, or human decisions may constrain delivery more than worker availability. Allocate capacity between workstreams deliberately. Queue size alone is not health; read age, blocked time, cohort completion, starvation, useful outcomes, and cost. Task generation is justified only if the new work serves an outcome.

Preserve enough of the instruction and artifact version to reconstruct consequential work. A snapshot and attempt ID are one application; a Git revision and inline result may suffice for a small repair. After interruption, inspect artifacts and active ownership before retrying. Distinguish no result, partial result, submitted result, reviewed result, decision recorded, and decision applied. Do not silently steal an active claim or overwrite evidence still needed for recovery or review. Apply the project's retention policy after those needs end. Retrying an external action needs an idempotency or reconciliation strategy.

One writer in one checkout is a reasonable simple application. Concurrent workers need isolation of edits and shared-state writes, ownership, lock/lease semantics, and recovery rules. A local lock does not coordinate separate clones. Git branches isolate some work; they do not prevent two agents calling the same external API.

Choose model capability, context size, review independence, and tool access against task ambiguity and consequence. Use fresh review context when it prevents anchoring; give the reviewer original evidence before the author's conclusions. Same-model agreement is not independent empirical confirmation. Report when a review is self-review.

Observe total cost: execution, retries, review, operator attention, and maintaining the machinery. Use richer workflows only when the failure they prevent justifies those costs. Before expanding unattended execution, establish useful behavior, recovery, and disposition. A manual run is one way to do that; an existing runner, replay, sandbox, or staged automated pilot may be the better starting point. Manual operation is not a universal prerequisite.

End with a small learning record: expected result, observed result, why they differed, and one possible adjustment. Define a disconfirming observation before experimenting. Retire rules that are no longer useful; historical success is not a reason to keep a mechanism indefinitely.
