# Application: automate a proven loop

**Default for this library: manual execution. No automation is installed.** A schedule is a trigger adapter for an existing workflow. It does not supply task authority, durable state, useful priorities, or safe disposition.

## Design before scheduling

Choose the unit of repetition: execute eligible tasks, observe a condition, or materialise an obligation occurrence. Define canonical state, attempt identity, idempotency, overlap prevention, missed-run behavior, time zone, execution budget, available tools/secrets, and the stop switch. Decide where results persist and how partial runs are reconciled.

Keep notifications actionable: completion, failure, changed evidence, or a concrete decision. Quiet unchanged observations must still leave enough health evidence to distinguish silence from a broken runner. Measure backlog age and disposition capacity before increasing execution frequency.

Test useful execution, an interruption, a duplicate trigger, and an empty/blocked queue in an appropriate pilot environment. A manual run is convenient for a new workflow, but an existing runner or staged automated trial can supply that evidence. Use the same acceptance and authority rules for scheduled and interactive execution. A schedule repeating a prompt does not approve new external actions.

## Runtime options — checked 2026-10-14

This is a dated capability map, not an installation guide. Follow the linked official documentation and inspect availability in the target environment before adopting it.

| Need | Codex | Claude Code |
|---|---|---|
| Durable repository guidance | [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | [CLAUDE.md / memory guidance](https://code.claude.com/docs/en/memory) |
| Reusable workflow instructions | [Skills](https://learn.chatgpt.com/docs/build-skills) | [Skills](https://code.claude.com/docs/en/skills) |
| Scheduled work | [Scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app) | [Cloud routines](https://code.claude.com/docs/en/routines) |
| Programmatic invocation | [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) | [Programmatic execution](https://code.claude.com/docs/en/headless) |
| Repetition in a running session | Inspect the selected runtime's exposed tools | [Scheduled prompts and /loop](https://code.claude.com/docs/en/scheduled-tasks) |

Codex's scheduled-task documentation describes scheduling work with configured execution context. Verify the selected execution environment, project access, and availability requirements there; do not assume all local and hosted surfaces behave alike. Skills package reusable instructions and supporting resources; they do not themselves create a recurring trigger.

Claude Code documents routines on managed cloud infrastructure (or configured self-hosted infrastructure), [desktop scheduled tasks](https://code.claude.com/docs/en/desktop#schedule-recurring-tasks), and scheduled prompts in an active local session. These have different persistence and environment assumptions. A committed skill can carry workflow instructions, but a configured routine also needs appropriate repository and connector access.

For a script or CI adapter, Codex documents `codex exec` and Claude Code documents `claude -p`. These run prompts programmatically; they do not supply scheduling or your work ledger. Configure permissions, output capture, failure handling, and duplicate-run protection for the actual environment. Do not infer business success from process exit alone.

Plain `execute-dev N` needs neither product's scheduler. Put the portable workflow in repository documentation; use thin vendor entry points only for convenience. Keep durable work evidence outside ephemeral session memory.

**Tradeoff:** repeated execution may increase useful throughput, review backlog, spending, or noise. Start only when continuing value exceeds those costs, and suspend on broken controls or unresolved ownership. Recheck vendor details when implementing; account access and product behavior can change.
