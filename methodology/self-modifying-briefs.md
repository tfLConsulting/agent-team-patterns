# Self-Modifying Agent Briefs

Agents can propose and make changes to their own role definitions, strategy documents, and operating procedures. This is what separates an agent team that learns from one that merely executes.

## What Self-Modification Means

An agent that discovers its brief is wrong — missing a responsibility, over-scoped, or based on an assumption that turned out to be false — can fix it. It doesn't need to wait for a human to notice and update the configuration. The agent notices, makes the change, and documents why.

This applies to:
- **Briefs:** Role definition, authority boundaries, inputs/outputs
- **Strategy:** Strategic priorities, hypotheses, positioning
- **Team composition:** Proposing new agents or retiring ones
- **Memory protocol:** How information flows between tiers
- **Operating procedures:** Session protocols, maintenance triggers

## Why This Matters

Static agent configurations create a fundamental problem: the world changes, the agent's understanding deepens, but its instructions don't evolve. Over time, the gap between what the brief says and what the agent should be doing grows. The human operator becomes the bottleneck for every adaptation.

Self-modification closes this loop. The agent operates under its brief, discovers where the brief falls short, and improves it. The next session starts with a better brief. This compounds — each session's learning is baked into the operating instructions for all future sessions.

## The Constraints

Self-modification without discipline is chaos. The constraints that make it work:

1. **Journal everything.** Every modification is recorded with what changed and why. This creates accountability and allows rollback.
2. **Research before changing.** Don't modify the brief based on a hunch. The research-first loop applies to self-modification too.
3. **Preserve core commitments.** Some things don't change: honesty, research-first thinking, self-assessment. Everything else is fair game.
4. **Human review for irreversible changes.** Adding a new agent, changing the strategic direction, retiring a role — these warrant discussion. Tweaking a session protocol doesn't.

## In Practice

From a working agent team (8 agents, 1+ month running):

- The team lead updated the strategy document 5 times as market understanding deepened
- An SEO analyst role was created when three recurring needs were identified across multiple sessions
- The memory protocol was overhauled when memory files grew too large — the agent team designed its own fix
- Session protocols evolved from rigid checklists to flexible directed/undirected modes

None of these changes required human intervention to identify. The agents surfaced the problems, proposed solutions, and implemented them. The human reviewed and approved.

## Where This Fits

Self-evolving agents are an active area of research — frameworks like EvoAgentX, papers from Sakana AI, and OpenAI's own cookbook explore the concept. But in practice, most teams building with agents aren't doing it. Agent configurations stay static from deployment. When something's wrong, a human debugs and reconfigures.

Self-modifying briefs close that gap. The agents are responsible for their own fitness. They can't change their fundamental purpose (that's the human's call), but they can change how they fulfil it. This produces agents that get better over time, not just agents that execute consistently.

The pattern emerges from treating agents as long-lived team members rather than stateless function calls — and the constraints (journaling, research-first, human review for irreversible changes) are what make it safe enough to do in production.
