# Bootstrapping an Agent Team

How to go from zero to a working agent team in any project. This document explains the thinking behind the bootstrapping protocol.

## The Hard Question

Creating agents is easy. Creating a *team* — agents with the right roles, sharp boundaries, persistent memory, and coordination patterns — is hard. The hardest part isn't the infrastructure; it's figuring out which agents a project actually needs.

This is harder than it sounds because:
- A project's codebase doesn't encode its goals, pain points, or workflow
- The person who needs the protocol most is least equipped to evaluate its output
- Over-engineering is the default failure mode (more agents does not mean better team)

## The Structural Contradiction

Our methodology says: "Create agents only after 3+ sessions demonstrate a recurring need." A bootstrapping protocol creates agents before session 1. Both can't be true.

Resolution: **the protocol creates the capacity for a team, not a finished team.** It creates exactly two core agents — a team lead and a team coach — plus the infrastructure for the team to grow. The team lead is justified as the minimal entry point. The team coach exists because the team lead structurally cannot evaluate its own team composition — its context is anchored on the current team. Everything else follows the 3-session rule. Specialist agents are proposed as candidates but not created.

This means a bootstrapped team is deliberately underpowered at first. That's the point. A team that starts small and grows into what it needs is better than a team that starts full-size and has agents sitting idle or duplicating work. The team coach — reviewing composition at session 3 and every 5 sessions after — is the mechanism by which growth actually happens.

## Wiring in the Learning Loop

The bootstrapping protocol creates team structure. It should also create the mechanism for that structure to improve itself. Three things to set up at bootstrap, not bolt on later:

1. **Experiment log.** An empty file (e.g. `team-coach/experiment-log.md`) with the template from [learning-from-practice.md](learning-from-practice.md). Every structural choice made during setup — memory architecture, role design, session protocol — is the first batch of entries. Status: active. Observed impact: blank (to be filled after running).

2. **Micro-observation prompt in the session-close protocol.** Add to the team-lead's brief or command file: *"What about our team's setup helped or hindered this session's work?"* — 1-3 sentences in the journal entry. This is the cheapest form of learning and it doesn't happen unless it's in the protocol.

3. **Treat the first ~10 sessions as exploration.** The bootstrapped structure is a starting point. Agents should record what's working and what isn't from session 1. The team-coach's first review (session 3) should check the experiment log alongside composition.

See [learning-from-practice.md](learning-from-practice.md) for the full protocol — confidence levels, deliberate variation, cross-team harvesting.

## The Assessment Gate

Not every project needs agents. A well-written CLAUDE.md handles many projects well. The protocol's first job is to honestly assess whether agents are warranted. "You don't need agents, but here's a better CLAUDE.md" is a valid outcome, not a failure.

Agents add value when work spans multiple domains, benefits from persistent memory across sessions, and has enough complexity that specialisation helps. If the work is mostly one type, sessions are infrequent, or the project is small — simpler tooling wins.

## What's Universal

From 28+ sessions across three projects, these patterns emerged. Note: this is N=3, same operator, same LLM. They work for us. They haven't been validated across diverse project types or operators.

**Universal:**
- **Role design with negative rights.** What an agent DOESN'T do matters more than what it does. Without boundaries, agents drift into adjacent domains.
- **Brief anatomy.** Context, Role, Boundaries, Inputs, Approach, Success, Memory. No worked examples, no quantitative KPIs, no step-by-step processes.

**Mostly universal (principle portable, implementation varies):**
- **Three-tier memory.** Hot (always loaded, small) / Warm (pulled when relevant) / Cold (archive). The principle of forced pruning is universal. The exact limits (200 lines, 30-day triggers) are calibration choices.
- **Team coordination.** Router-not-manager team lead. Directed/undirected session modes. Self-modification with journaling.

**Context-dependent:**
- **File-based coordination.** Works in environments with a shared filesystem (Claude Code, similar tools). The underlying principle — one-way flows through completed outputs — is universal even when the mechanism differs.
- **Self-modifying briefs.** Powerful for mature teams. Risky for new teams that haven't stabilised. Enabled at bootstrap but only meaningful after several sessions.

## Failure Modes

**Over-engineering** (most likely): Protocol creates too many agents, too much structure. A solo project doesn't need 8 agents and formal self-modification protocols. The protocol's own sophistication biases it toward sophisticated outputs.

**Cargo culting**: Copying patterns without understanding why they work. Three-tier memory for a project that runs one session per month. Negative rights for roles where drift hasn't been observed.

**Wrong composition**: Assessment gets the project type or work domains wrong, producing agents that don't match actual needs.

**Early-session confirmation bias** (observed, N=2): Both teams that used this protocol exhibited confirmation bias in their first 3-5 sessions — each research round validated the previous conclusion rather than challenging it. The team-lead starts as both advocate and judge, with no structural check until the team-coach review fires (session 3). Whether this is caused by missing protocol features, compressed session timing, or a model-level trait is unclear. Awareness of the pattern may be the only portable mitigation; prescriptive fixes (e.g., mandatory adversarial review) face a bootstrap paradox.

**Premature rigidity**: The bootstrapped structure gets treated as permanent. Nobody exercises self-modification because the bootstrap felt authoritative.

**The bootstrap paradox**: The protocol is designed for people who don't yet know how agent teams work. But evaluating its output requires that knowledge. The first few sessions require more human judgment than later ones.

## Compatibility with Claude Code Native Agent Teams

Claude Code's native Agent Teams feature (shipped Feb 2026) provides concurrent execution, shared task lists, and inter-agent messaging. This is complementary to the bootstrapping approach, not competing:

- **Native Agent Teams** handles execution: running multiple agents concurrently, coordinating within a session.
- **The file-based approach** handles persistence: roles that maintain memory across sessions, briefs that evolve, journal narratives that compound.

A project can use both. The bootstrapping protocol creates the persistent layer (briefs, memory, coordination patterns). Native Agent Teams handles the execution layer if needed.

## Limitations

- **N=3, same operator.** This methodology was developed across three projects by the same operator with the same LLM. One team was bootstrapped using this protocol and produced a viable but different team — validating that the protocol doesn't prescribe outcomes. But all three share the same operator and LLM, so presenting these as universal principles without diverse validation is framework over-extraction.
- **Tacit knowledge.** An effective team lead benefits from operator judgment built over sessions — when to intervene, when a brief is wrong, when memory needs pruning. The protocol creates the structure but not the experience.
- **Platform evolution.** Claude Code's capabilities change rapidly. If native features subsume what the protocol provides, the protocol becomes unnecessary. That's fine — it means the platform caught up.
- **A well-configured CLAUDE.md may be enough.** For many projects, a single generalist agent with good project instructions outperforms a multi-agent team. The assessment gate exists because over-engineering is worse than under-engineering.
