# Agent Team Patterns

A design library for organising agent-assisted work around **planning, execution, and disposition**. Use it to help Codex, Claude Code, or a human design a way of working that fits a particular repository.

The main contribution is the reasoning: what deserves attention, what evidence supports a decision, how controls reduce risk, and how information survives between sessions. Roles, queues, branches, pull requests, and schedules are possible applications of those principles. None is a prerequisite.

## Start here

- [Adopt in a new repository](applications/adoption.md): a prompt and discovery process starting from the project's needs.
- [The operating cycle](principles/operating-cycle.md): vocabulary, planning, bounded execution, and disposition.
- [Design considerations](principles/README.md): attention, consequences, tests, residuals, information, recovery, and cost.
- [Choose an application](applications/README.md): manual files, branch-based work, review queues, or scheduled execution.
- [Run a small example](examples/manual-ledger/README.md): dependency-aware selection and disposition packets using Python's standard library. No model calls or background jobs.
- [Challenge the defaults](applications/policy-choices.md) with [contrasting design cases](examples/design-cases.md).
- [Templates](templates/README.md): starting shapes to adapt, not a required schema.

## Principles and applications

A principle explains a problem and a tradeoff. An application chooses a mechanism in a context. Keep both, and record when the mechanism stops earning its cost. One project can use a single Markdown record; another can use a database, PRs, or a mixture. A branch isolates edits but does not by itself preserve the task, evidence, decision, or eventual outcome.

The [second-pass review](work/2026-10-design-review.md) records omissions and overgeneralisations found in the initial version. The new material is an initial practitioner synthesis and a set of design proposals, not a validated universal method. The runnable example is a deliberately limited reference implementation. Historical patterns retain their original evidence qualifications; their existence does not establish that every project needs a team or a coach.

## Earlier patterns

The [earlier methodology](methodology/README.md), [skills](skills/), [agent examples](agents/), [journals](journal/), and [investigations](investigations/) remain available. They explore persistent roles, file coordination, memory, and learning. The [reuse map](applications/earlier-patterns.md) explains where these still help and which assumptions need reconsideration. They are historical material, not the default setup for this repo.

## Working on this library

This repo uses [a small manual work record](work/README.md). It has no scheduler or live project interface. Read [AGENTS.md](AGENTS.md) for contribution and privacy rules. MIT licensed; see [LICENSE](LICENSE).
