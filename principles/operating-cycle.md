# Planning, execution, and disposition

**Principle:** distinguish choosing worthwhile work, doing it, and deciding what its results mean. These responsibilities can recur and overlap within one interaction; they do not require three serial stages, separate people, or separate systems.

## Vocabulary

| Concept | Purpose | Fictional example |
|---|---|---|
| Workstream | Holds a desired outcome across multiple tasks | Make an export usable without assistance |
| Plan | Current argument for what to do and in what order | Inspect failures, compare two formats, implement one |
| Task | A bounded unit with an acceptance contract | Preserve quoted line breaks in exported records |
| Attempt | A particular execution against a particular contract | Second run after a failed compatibility check |
| Evidence | Inspectable support, tied to an artifact/version | A fixture, command result, and output hash |
| Disposition | A recorded decision about work or findings | Accept implementation; observe support demand next month |
| Obligation | Work expected to recur | Check export compatibility after a dependency update |
| Residual | Named uncertainty or exposure left after controls | Spreadsheet behavior was checked in only one application |

This vocabulary is a useful working language, not a required object model. A standalone repair need not acquire a workstream, and an ongoing service need not become a sequence of finite projects. A workstream can contain research, decisions, implementation, and observation. A task is not a workstream shortened to fit a queue. An obligation needs occurrences so last month's success cannot silently discharge this month's check. A residual is not automatically a new task: it can be accepted, bounded, investigated, or stopped.

## Plan at the level where choices matter

State the outcome, beneficiary, constraints, evidence available, important unknowns, alternatives, and a stopping condition. Identify who can decide direction and what execution is already authorised. Make tasks only as detailed as the next useful steps require. Commit to an outcome and learning budget before filling a long queue with guesses.

Review how demand enters the plan, what new work displaces, and what invalidates existing commitments; see [planning and replanning](planning-and-replanning.md). Use a short sketch for a known fix; add a comparison or position paper when implementation would prematurely commit to a disputed direction. An investigation can finish with a decision to stop. Not every workstream needs the same gates.

## Execute in bounded batches

`execute-dev N` can be an ordinary instruction: attempt up to N eligible tasks, respecting dependencies and existing authority. Define N locally. The manual application counts distinct attempted tasks, including blocked attempts; a time budget or a completion target with a separate attempt cap can also work. Report attempted, submitted, and accepted honestly under the chosen policy. Reviews do not silently disappear when the limit is reached. See the [manual application](../applications/manual.md).

Read the current contract, preserve its version, do the work, record actual checks and limitations, then submit the result for the applicable review/disposition. Re-select after important results; do not blindly execute a stale initial list. A task being attempted does not authorise every external action that might complete it.

## Dispose explicitly

Disposition can accept, revise, defer, reject, stop, or request observation. Name the artifact/version, evidence, rationale, decision maker, authority, remaining uncertainty, and any next trigger. Distinguish the decision from carrying it out and from observing its effects. A recommendation is not a decision; a decision to deploy is not a successful deployment.

Use standing policy for routine decisions where justified, with receipts and exceptions. Group related results into a workstream packet when the decision concerns direction or cumulative benefit. Preserve task-level evidence underneath it.

**Failure modes:** execution creates its own priorities; submitted work counts as accepted; changed briefs erase the original contract; deferral has no wake condition; accepted tasks imply an achieved outcome. Separate records only where they prevent these failures. For one small change a single document can hold the whole cycle.
