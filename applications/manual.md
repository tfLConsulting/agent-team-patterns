# Application: manual planning and execution

**Context:** occasional work in one checkout, with no need for a continuously running queue. This library uses this application in [work/](../work/README.md).

Use one small record for the current workstream, task list, execution evidence, and disposition. Split files only when the record becomes hard to navigate. Keep completed records for provenance and an index for current state. The [templates](../templates/README.md) supply optional questions.

## One execute-dev policy to adapt

Define this in ordinary repository guidance; no custom slash command is required:

> On `execute-dev N`, validate that N is a positive integer (default 1). Reconcile unfinished attempts and preserve unrelated edits. Select one eligible task within existing authority, considering dependencies, readiness, and workstream priority. Preserve its original contract, perform the task, and record the actual result, checks, findings, and residuals. Follow the project's review policy. Repeat by selecting again, up to N distinct attempted tasks; blocked attempts count. Record attempted, submitted, accepted, and blocked counts separately. Finish required reviews or report awaiting review. Do not create a scheduler. Stop when nothing eligible remains, even if fewer than N were attempted.

Counting blocked attempts, separating reviews from N, and the listed states are local policies for this manual application; [other choices are valid](policy-choices.md). The instruction performs work. The example CLI's `next` command only selects; it does not execute this instruction, claim tasks, or enforce a batch budget.

Keep transitions explicit: ready → active → submitted → accepted, revised, blocked, deferred, or stopped. A real project may combine states; preserve their meaning in the evidence. A failed attempt stays recorded when revised. This application uses acceptance-gated dependencies. Elsewhere, specify the needed predicate: an artifact exists, a contract passes, a release is live, or a decision is authorised. Provisional use may be useful if explicitly allowed and invalidation is handled.

For review, choose self-check, a different reader, or an independent agent according to consequences and available tools. Label the choice honestly. Disposition under existing authority can be recorded by the agent; user acceptance must come from the user. A request for a new decision carries the finished artifact and concrete alternatives.

**When to change application:** multiple writers need coordination; manual state becomes inconsistent; recurring work needs occurrence identity; evidence becomes hard to retrieve. Respond to the actual failure. A scheduler does not fix inconsistent records.
