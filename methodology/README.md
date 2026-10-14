> Historical application (April–May 2026). For current guidance, start with [the design library](../README.md) and [current instructions](../AGENTS.md). This document retains its original assumptions and evidence limits.

# Methodology

Patterns for building AI agent teams that coordinate through files, evolve their own instructions, and run in plain-text repos.

## What do you need?

**Starting a new agent team from scratch?**
Read [agent-team-guide.md](agent-team-guide.md), starting with Section 4. It walks through assessment (do you even need agents?), creates the minimal viable team (team-lead + team-coach), and sets up the infrastructure for growth — including wiring in the learning loop from [learning-from-practice.md](learning-from-practice.md) at setup, not bolting it on later.

**Running a team and want to improve how it works?**
Read [learning-from-practice.md](learning-from-practice.md). It describes how to embed lightweight observation in normal sessions, run deliberate experiments with structural choices, and accumulate evidence about what's working. Start with micro-observations at session close and an experiment log.

**Want the full picture of how agent teams work?**
Read [agent-team-guide.md](agent-team-guide.md). Comprehensive guide covering when agents are warranted, core patterns, known failure modes, team growth, multi-team coordination, self-modification, and checklists.

**Looking up a specific pattern?**
Each pattern has its own file:

- [three-tier-memory.md](three-tier-memory.md) — hot/warm/cold memory
- [role-design.md](role-design.md) — role design with negative rights
- [file-based-coordination.md](file-based-coordination.md) — one-way information flows through files
- [brief-anatomy.md](brief-anatomy.md) — how to write effective agent briefs
- [self-modifying-briefs.md](self-modifying-briefs.md) — how agents evolve their own instructions
- [writing-for-ai.md](writing-for-ai.md) — document quality principles for AI-consumed files
- [discipline-processes.md](discipline-processes.md) — encoding discipline methodologies as structured skills
- [coaching-framework.md](coaching-framework.md) — systems-level team assessment across five dimensions
- [investigation-threads.md](investigation-threads.md) — living hypothesis documents that evolve across sessions
- [load-bearing-beliefs.md](load-bearing-beliefs.md) — framing strategy as testable hypotheses with kill conditions
- [codification-ladder.md](codification-ladder.md) — when recurring practices deserve to be written down, and in what form
- [session-transaction-protocol.md](session-transaction-protocol.md) — fault-tolerant session boundaries with dirty-close detection and reconciliation
- [measurement-skepticism.md](measurement-skepticism.md) — why agent team metrics are structurally fragile, and the discipline of checking the measurement before interpreting the result

## Evidence base

N=3 projects, same operator, same LLM (Claude). These are practitioner field notes, not general theory. Individual patterns carry varying levels of evidence — see [learning-from-practice.md](learning-from-practice.md) for the confidence framework and current assessments.
