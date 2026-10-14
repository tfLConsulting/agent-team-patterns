# Adopt by designing locally

Give a new repo access to this library and ask it to reason from the principles. Do not import the library's own work records as your backlog or install all of its historical skills.

## Prompt to use in another repository

> Read the Agent Team Patterns library's README, operating cycle, and design considerations. Treat it as a design reference. Inspect this repository's existing instructions, state, tests, release process, and unfinished work. Preserve its current authority and privacy boundaries. Propose the smallest useful planning, execution, and disposition approach for this project, explaining the choices and rejected alternatives. Identify canonical records, workstreams, task acceptance, evidence, residuals, and decision rights. Preserve useful existing execution arrangements. Choose manual, scheduled, or event-driven execution and PR or other records according to the project's needs; explain those choices. Implement the authorised, reversible local parts and demonstrate one bounded cycle with inspectable evidence. Do not invent successful outcomes or independent review. Keep this project's confidential material here; write nothing back to the reference library.

Supply an actual checkout path or accessible URL for the library. A reference alone does not give an agent access to a private repo or to tools it lacks.

## Discover before installing

1. What outcome matters, for whom, and how could we tell it improved?
2. What work and commitments already exist? Where is current state authoritative?
3. Who can decide direction, accept results, and authorise external actions?
4. Which failures matter, what controls exist, and what can remain untested?
5. What can the runtime read, write, review, and execute? What persists when it exits?
6. How often does useful work arise, and what limits review and attention?

Choose an initial scope that exposes the important design choices: a standalone task, a workstream, or a service occurrence may fit. Use [templates](../templates/README.md) as prompts. Avoid inventing mandatory fields that nobody reads. Explain why each constraint exists, how to detect violations, and when to retire it.

## Pilot one cycle

Capture a bounded task; preserve the contract; run in the chosen environment; produce evidence; assess residuals; record a disposition and whether it was applied. Stop and restart once to test whether another session can reconstruct the state. Check that changed findings reach the right reader and that accepted work is distinguishable from observed benefit.

Adapt after the pilot. Add a validator for recurring mechanical mistakes, independent review for consequential assumptions, or a shared store for actual concurrency. Add or retain automation when usefulness, recovery, and decision capacity are supported by the pilot evidence. Remove any structure whose cost exceeds the problem it solves. Use the [policy choices](policy-choices.md) and [contrasting cases](../examples/design-cases.md) to challenge defaults. Include a changed-premise or partial-evidence case in the pilot, not just successful closure.

**Adoption evidence:** a cold session can find the next eligible action, verify a result, explain a pending decision, and resume without guessing. A folder tree or a green setup script does not establish adoption.
