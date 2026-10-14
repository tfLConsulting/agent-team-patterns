# Choose mechanisms to fit the project

Applications are examples of choices, not maturity levels. A busier repo may still prefer manual execution. Combine mechanisms only when their responsibilities and canonical records are clear.

| Application | Good fit | Cost or limitation |
|---|---|---|
| [Manual files](manual.md) | Occasional work, one operator, inspectable evidence | Manual transitions; little concurrency support |
| [Branches and durable records](storage-and-review.md) | Isolated code changes without hosted PRs | Must supply durable identity, review, evidence, and decisions |
| [PRs or a shared database](storage-and-review.md) | Many artifacts, reviewers, or concurrent writers | Hosting, schema, permissions, and reconciliation overhead |
| [Optional scheduling](automation.md) | Stable repeatable work with continuing value | Environment availability, duplicate runs, stale assumptions |

Start with [adoption](adoption.md), check the [local policy choices](policy-choices.md), and compare the [contrasting cases](../examples/design-cases.md). Reuse [earlier patterns](earlier-patterns.md) selectively. The [manual ledger example](../examples/manual-ledger/README.md) makes selection and missing evidence visible without choosing an execution runtime.
