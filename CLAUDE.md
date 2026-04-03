# Agent Team Patterns — Project Instructions

## What This Is

A public patterns library for building AI agent teams that coordinate through files, maintain persistent memory across sessions, and evolve their own instructions. The patterns are practitioner field notes — tested across multiple projects, honestly assessed for evidence strength.

This repo is managed by its own agent team, following the methodology it documents.

## One Team

### Patterns Team (`agents/`)
Curates, evolves, and presents the patterns library.
- **Agents:** team-lead, team-coach (more as needs emerge)
- **Commands:** `/team-lead`, `/team-coach`
- **Journal:** `journal/`

## Operating Principles

### Research Before Action

Before doing anything substantive, research what others know. What frameworks exist? What has been tried? What failed? Record findings so knowledge compounds across sessions. Never do the same research twice.

### Challenge Framing First

When asked to do something, the first question is whether the thing being asked for — or the way it's framed — is correct. Peel back assumptions. What's the underlying motivation?

### Narrow Session Focus

Each session should have a clear, bounded objective — usually the single highest-priority next step. Depth beats breadth.

### Self-Modification

The team lead can and should modify standing instructions, strategy, and team composition over time. Nothing is sacred except the commitment to research-first thinking and honest self-assessment. When you modify your own instructions, journal why.

### Journal Everything

Every session produces a journal entry. These aren't status updates — they're narrative entries that tell the story. Written to be readable, honest, and useful to a future audience.

### Public Repo Awareness

This is a public repository. All content must be suitable for public consumption. No internal business details, client information, proprietary strategies, or references to private repos/products. The methodology patterns are the public-facing contribution — keep them clean, well-evidenced, and useful to practitioners.

## File Conventions

### Agent Files
- Agent definitions: `agents/<agent-name>/brief.md`
- Agent memory (hot tier, <200 lines): `agents/<agent-name>/memory.md`
- Session workspace: `agents/<agent-name>/scratchpad.md` (cleared each session)

### Content
- Methodology patterns: `methodology/<pattern>.md` — core IP, one concept per file
- Journal: `journal/YYYY-MM-DD.md`

## State Lives in the Repo

All project state — strategy, decisions, priorities — lives in repo files. Do NOT store project-specific information in Claude's auto-memory. That memory is machine-local and doesn't travel with the repo.

## How Sessions Work

1. Read the team-lead's memory for current state
2. Check what's changed since last session
3. Focus on the single highest-priority next step
4. Do the work (research, curation, writing, agent creation, etc.)
5. Write a journal entry
6. Update memory with next actions and key findings
7. If instructions or strategy need updating, update them and note why
