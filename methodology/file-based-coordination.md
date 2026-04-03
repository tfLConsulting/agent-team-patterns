# File-Based Coordination

Most multi-agent frameworks coordinate through message passing, shared memory, or orchestration layers. These add complexity, introduce race conditions, and make the system harder to debug. File-based coordination is simpler and more robust.

## The Core Pattern: One-Way Information Flow

Agents collaborate through completed outputs, not shared reasoning. Agent A writes a file. Agent B reads it when relevant. There's no bidirectional dependency, no waiting for responses, no shared context window.

```
Analyst writes activation-analysis.md
  → Designer reads it, maps failure modes to user flows
  → Educator reads designer's spec, drafts help content
  → Customer success reads educator's drafts, uses in outreach
  → Analyst measures whether engagement moved
```

Each agent knows its readers (from its brief). Each reader knows where to look (from its brief). Nobody guesses.

## Why One-Way Flows

Bidirectional dependencies create circular waits. If Agent A needs Agent B's input to finish, and Agent B needs Agent A's output to start, neither can work. One-way flows eliminate this. Agents can run in parallel because they read completed outputs, not in-progress thinking.

This also makes the system observable. You can trace any decision back through the file chain: who wrote what, when, and what they were reading when they wrote it.

## The Contract: Explicit Inputs and Outputs

Each agent's brief specifies:
- **What files it reads** from other agents (with the reason)
- **What files it produces** and who consumes them

Example from a working system:

| Agent | Produces | Consumed By |
|-------|----------|-------------|
| SEO Analyst | keyword-opportunities.md | Content Strategist |
| SEO Analyst | technical-health.md | Engineering Lead |
| Product Analyst | activation-analysis.md | Designer, Strategist |
| Designer | journey-map.md | Educator, Engineering Lead |

These are explicit contracts. When an agent is created, its inputs and outputs are defined. This prevents both "nobody reads my work" and "I don't know where to find what I need."

## Directory Structure as Architecture

Each agent owns its directory. No agent writes to another agent's directory. Shared knowledge lives in a `shared/` directory or a wiki.

```
agents/
├── shared/           # Cross-cutting reference material
├── team-lead/        # Routing + sequencing (thin state)
├── analyst/          # Research outputs
├── strategist/       # Content plans + drafts
└── designer/         # Specs + wireframes
```

The directory structure reflects the information architecture. If you can't tell what an agent does from its directory contents, the role isn't clear enough.

## Debugging and Observability

File-based coordination is inherently observable. Every piece of agent reasoning that matters is in a file. You can:
- Read any agent's current state (memory.md)
- Trace how a decision was made (follow the file chain)
- See what information an agent had when it acted
- Audit whether agents are reading the right inputs

No logging framework needed. The files ARE the log.
