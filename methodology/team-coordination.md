# Team Coordination

## The Router, Not Manager

The team lead is a router: it reads all agent states, decides who runs next, and provides direction. It does NOT interpret findings, tell agents how to work, or duplicate analysis. Its own memory is thin — just enough state to sequence work.

What the team lead tracks:

| Field | Purpose |
|-------|---------|
| Last run date per agent | Know what's stale |
| Key state per agent | One-line summary of where each agent is |
| Strategic priorities | What matters most right now |
| Backlog | Queue of open questions |

This is routing information, not management overhead. The team lead's context window stays clear for decision-making.

## Session Modes

**Directed:** The human asks for something specific. Skip the assessment. Run the relevant agent. Do the work.

**Undirected:** The human says "continue" or gives no direction. The team lead assesses: sync data, compare key numbers, pick the highest-priority question from the backlog, run the right agent, report back.

Undirected sessions are where the team lead earns its keep. The ability to autonomously identify and execute the most important work is the difference between an agent team and a set of chatbots.

## The Backlog as Governance

The team maintains a queue of strategic questions. Each question gets investigated across one or more sessions. Answered questions stay in the log (marked answered) so the team doesn't re-investigate.

This creates a visible record of what the team has learned and what it's currently investigating. It also prevents the team lead from chasing whatever seems interesting in the moment — there's a prioritised queue.

## Scaling Limits

Each new agent adds one more memory file to read and one more routing decision. At 4-6 agents this is manageable. At 10-12 it strains. Beyond that, you likely need sub-teams with their own team leads.

The scaling limit isn't compute — it's the team lead's ability to hold enough context about each agent's state to make good routing decisions. This is why thin state tracking matters: if the team lead needs to read 200 lines of memory per agent to decide who runs next, 8 agents means 1,600 lines of routing context before any work begins.

## Self-Modification

The team is not static. Strategy, team composition, and even agent briefs can evolve.

Rules for self-modification:
1. Any change to strategy or team composition is documented with reasoning
2. New agents must pass the justification test (recurring need across 3+ sessions)
3. Changes are journaled — the narrative of why things changed is as valuable as the change itself
4. Nothing is sacred except research-first thinking and honest self-assessment

Self-modification is what makes this a system that learns, not just a system that executes. But undisciplined self-modification creates chaos. The journal requirement forces the team to be deliberate about evolution.
