# Choices that examples must not settle for you

A reference implementation necessarily chooses. Treat those choices as hypotheses for a context. The transferable part is the question and the failure it prevents; the values and mechanisms below remain local policy.

| Choice | Why the initial example chose it | Other valid designs |
|---|---|---|
| Manual invocation | This library changes infrequently | Existing reliable scheduling, event triggers, continuous interactive work |
| Workstream on every task | Demonstrates grouping related results | Standalone fixes, service obligations, evidence grouped only at review time |
| One serial active task | Keeps manual ownership easy to inspect | Isolated concurrent attempts with shared ownership/recovery rules |
| Acceptance satisfies dependencies | Avoids consuming unreviewed output in this demo | Artifact available, tests passed, release complete, or explicit provisional use |
| One dependency relation | Keeps example code small | Separate data, sequencing, authority, and observation dependencies |
| Ready/active/submitted/etc. | Makes handoffs visible | Separate progress, readiness, review, release, and outcome axes |
| Blocked/deferred needs a wake condition | Prevents invisible parking | Terminal decision with no review, periodic reevaluation, explicit owner monitoring |
| Blocked attempts count toward N | Bounds this manual batch's effort | Time/token/spend budget, successful-task target with a separate attempt cap |
| Retry after revision | Keeps manual batches bounded and prior evidence inspectable | Bounded repair in the same run, a later batch, or escalation; prevent budget-reset loops |
| Priority then ID | Deterministic demonstration | Deadline, aging, capacity allocation, cost of delay, operator selection |
| Evidence beneath ledger directory | Self-contained portable fixture and containment check | Restricted external store, hosted checks, content-addressed artifacts |
| Snapshot and attempt record for every task | Demonstrates evidence identity | Git revision and inline result for a small change; richer records for costly retries |
| Files plus Git retain history | Easy inspection in one checkout | Transactional store, managed audit log, selective retention or deletion |
| All example decisions have named makers | Makes attribution visible | Policy reference with automated receipts and sampled review |
| Human-focused consequence categories | Helps route meaningful findings | Domain-specific severity, affected population, timing, cost and reversibility |
| Manual proof before new scheduling | Cheap diagnostic step for an unproven workflow | Sandbox dry runs, replay, staged automated pilot, established production runner |

The example's JSON schema is not a portable ontology. In a richer application, a task can be in design, blocked on access, awaiting review of a partial artifact, and not yet released at the same time. Separate these dimensions when combining them would lose a decision-relevant fact. A unified queue and separate queues are both possible; specify how capacity and dependencies work across them.

Retention also needs design. Keep evidence while decisions, recovery, or accountability rely on it; choose periods and deletion rules appropriate to sensitivity and cost. Failed attempts do not need to be retained forever merely because preserving them is useful during revision. A canonical authority per fact can span multiple systems; one physical file or database is not required.

Do not infer that low implementation risk automatically authorises applying a change, that high significance always blocks it, or that a particular risk score implies priority. The project chooses those policies explicitly. The [cases](../examples/design-cases.md) illustrate differing answers.
