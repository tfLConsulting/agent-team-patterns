# Agent Team Patterns

Patterns for building AI agent teams that coordinate through files, evolve their own instructions, and run in plain-text repos.

## What's Here

This is a practitioner's patterns library — not a framework, not a product. It's a set of field-tested patterns for organising AI agents into teams that persist across sessions, maintain memory, and improve over time.

The evidence base is narrow: multiple projects, same operator, same LLM (Claude). These are practitioner field notes, not general theory. Individual patterns carry varying levels of evidence — see [learning-from-practice.md](methodology/learning-from-practice.md) for the confidence framework.

## The Patterns

**Starting a new agent team from scratch?**
Read the [practitioner's guide](methodology/agent-team-guide.md), starting with Section 4 if you're setting up a new team.

**Want the full picture?**
Read [agent-team-guide.md](methodology/agent-team-guide.md) from the beginning.

**Looking up a specific pattern:**

- [three-tier-memory.md](methodology/three-tier-memory.md) — hot/warm/cold memory architecture
- [role-design.md](methodology/role-design.md) — role design with negative rights
- [file-based-coordination.md](methodology/file-based-coordination.md) — one-way information flows through files
- [brief-anatomy.md](methodology/brief-anatomy.md) — how to write effective agent briefs
- [self-modifying-briefs.md](methodology/self-modifying-briefs.md) — how agents evolve their own instructions
- [writing-for-ai.md](methodology/writing-for-ai.md) — document quality principles for AI-consumed files
- [learning-from-practice.md](methodology/learning-from-practice.md) — evidence tracking and continuous improvement

## Exportable Skills

Ready-to-use [Claude Code skills](https://agentskills.io) that implement patterns from this library. Copy any skill directory into your project's `.claude/skills/` to use it.

- [build](skills/build/) — 6-step execution recipe for non-trivial implementation work (investigate, plan review, execute, code review, QA, close-out). Each step runs as a separate subagent with fresh context. Evidence-based — see the [research synthesis](skills/build/references/research-synthesis.md).
- [skill-building](skills/skill-building/) — how to build, review, and improve Claude Code skills. Covers the Agent Skills open standard, progressive disclosure, description writing, and common failure modes.

## How This Repo Works

This repo is managed by its own agent team, following the methodology it documents. The team curates, evolves, and presents the patterns. See [CLAUDE.md](CLAUDE.md) for how the team operates.

## License

MIT — see [LICENSE](LICENSE).
