# Role Design & Authority Boundaries

The most common failure in multi-agent systems is role confusion. Agents duplicate work, contradict each other, or sit idle because nobody owns the problem. The fix isn't more coordination — it's sharper role definition.

This pattern covers what makes a role work, what makes it fail, and how to decide whether a role should exist at all.

**Evidence:** Practised (3 teams, 150+ sessions across the source teams). The negative-rights principle and authority gradient have been consistent across all three projects where agent teams were operated. The domain ownership model has been stable since early sessions. The "when NOT to create" heuristics emerged from observed over-engineering in one team's bootstrap and have been applied preventatively in two subsequent teams. Evidence qualifiers for specific claims are noted inline.

## The Principle: Domain Ownership with Negative Rights

Each agent owns a specific domain. Ownership means the agent has authority over findings and recommendations within that domain. But authority is bounded by explicit "what you don't do" statements.

Negative rights matter more than positive ones. An agent told "you own content strategy" will inevitably drift into design, analytics, or implementation. An agent told "you own content strategy; you don't write code, you don't make design decisions, you don't publish without review" stays in its lane. This finding was consistent across all three projects where teams were operated — every team that started with positive-only role definitions experienced drift within the first few sessions.

The mechanism is straightforward: LLMs are helpful by default. Given a broad mandate and adjacent work that needs doing, an agent will do it. Negative rights create explicit fences that override the helpfulness instinct. They work because they're specific and falsifiable — an agent can check "am I writing code right now?" more reliably than "am I staying within my content strategy domain?"

## Anatomy of a Good Role Definition

Six elements make a role definition complete:

1. **Domain:** What slice of the problem space does this agent own?
2. **Authority:** What decisions can this agent make autonomously?
3. **Boundaries:** What does this agent explicitly NOT do? (List the adjacent roles it could drift into)
4. **Inputs:** What files/data does this agent read from other agents?
5. **Outputs:** What does this agent produce, and who consumes it?
6. **Success:** What does good work look like? (Descriptive, not metric-based — see `brief-anatomy.md` for why)

The boundaries section carries the most weight. A role definition with a clear domain but vague boundaries will drift. A role definition with strong boundaries but a vague domain will still stay in its lane.

### Worked Examples from This Repo

This repository's own agents illustrate the pattern:

**Team Lead** (`agents/team-lead/brief.md`) — owns routing and synthesis. Its negative rights are extensive: "You don't run web searches or fetch pages. You don't write research documents or analysis. You don't draft methodology content. You don't interpret agent findings beyond synthesis." Each negative right names a specific adjacent activity the team lead would otherwise absorb. The brief also defines what the team lead does NOT own by explicitly listing that execution work goes to sub-agents — even when no specialist exists. This prevents the most common team-lead failure mode: doing work inline instead of routing it.

**Team Coach** (`agents/team-coach/brief.md`) — owns team composition and health assessment. Its key negative right: "Do NOT read other agents' memory files." This isn't just a boundary — it's a deliberate context-separation constraint. The coach evaluates from the outside (briefs + journals) to maintain genuinely different cognitive context from the agents it evaluates. Without this constraint, the coach's assessments would be anchored on each agent's self-narrative.

## The Authority Gradient

Not all decisions carry equal weight. The authority gradient maps decision types to autonomy levels:

**Full authority** — analysis and recommendations within the agent's domain. The agent acts without waiting for approval.

**Limited authority** — decisions that cross domain boundaries or affect other agents. The agent proposes and waits for the team lead to route or approve.

**No authority** — irreversible actions (publishing, deploying, sending communications, retiring agents). These require human review regardless of the agent's confidence.

This gradient means agents can work autonomously on research and analysis but naturally pause at decision points that affect other agents or the outside world. The gradient is also the mechanism behind human checkpoints in discipline processes (see `discipline-processes.md`) — any phase transition where bad framing would waste all subsequent work is a checkpoint.

## When NOT to Create an Agent

A role should exist only when all of these are true:

1. **Recurring need.** The work has recurred across 3+ sessions. One session of needing code review doesn't justify a code-reviewer agent.
2. **Persistent perspective.** It would benefit from its own persistent memory and domain context loaded each session.
3. **Briefable scope.** The role is specific enough to brief clearly (see `brief-anatomy.md` for the test: could a competent person read the brief and start working?).
4. **Context separation.** The proposed agent would have genuinely different loaded context from existing agents — different files read, different brief focus, different memory. This is the most important test.

The context-separation test prevents the most common over-engineering failure: agents that are just the team lead wearing a different hat. If a proposed agent would read mostly the same files and have mostly the same brief as an existing agent, it doesn't produce different thinking — it produces the same thinking with a different name. In one observed team, the team lead never proposed changing team composition despite having explicit authority to do so, which is consistent with context anchoring: the team lead's context includes the current team as a given, making it structurally difficult to reason about alternatives. This is why the team coach — with different loaded context — owns composition decisions.

Premature specialisation creates coordination overhead without enough value. One generalist agent that handles three types of work is better than three specialist agents that need constant routing. The two-agent start (team lead + team coach) exists because of this principle — everything else follows the 3-session rule.

## Anti-Patterns

### Over-Specification

A role definition that prescribes how the agent works, not just what it owns. Step-by-step processes, tool-calling sequences, worked examples of good output — these belong in skills or playbooks (see `codification-ladder.md`), not in role definitions. An over-specified role produces a brittle agent that fails when conditions change. The brief should set the board; the agent figures out how to play.

Over-specification is especially common at bootstrap, when the team designer has a clear picture of how work should flow. That picture is almost always wrong — it's based on assumptions that the first few sessions will challenge. A role definition that's tightly coupled to a specific workflow becomes an obstacle to the self-modification that should improve it.

### Under-Specification

A role definition that gives the agent a domain but no boundaries. "You own research" is under-specified — research about what? Using which sources? Producing what format of output? For whom? Under-specified roles don't cause drift in the same way that missing negative rights do. They cause aimlessness — the agent produces work that's competent but unfocused because it lacks the constraints that would channel its effort.

The fix isn't more words. It's sharper boundaries. The six elements above (domain, authority, boundaries, inputs, outputs, success) are a checklist — if any element is genuinely blank, the role definition is incomplete.

### Missing Negative Rights

The most common anti-pattern, already covered above but worth naming explicitly. A role definition that says what the agent does but not what it doesn't do. Without negative rights, every agent gradually converges toward doing everything. In observed practice, agents without explicit "you don't do X" constraints would absorb adjacent work within 2-3 sessions, particularly when the adjacent role wasn't active in that session.

### Role Overlap Without Shared Protocol

Two agents with overlapping domains but no explicit protocol for who handles what. The result is either duplication (both agents do the work) or gaps (each assumes the other will handle it). Overlap itself isn't always bad — some redundancy provides resilience. But unacknowledged overlap is always bad. If two roles intentionally share a boundary, the boundary protocol should be documented in both briefs.

### Identity Without Function

Creating an agent because the role sounds useful rather than because recurring work demands it. "Every team needs a QA agent" or "we should have a strategist" — these are identities, not functions. The 3-session rule exists to prevent this: the need must be demonstrated through actual recurring work before the role is created.

## How Roles Evolve

Role definitions aren't permanent. They change as the team learns what works. Self-modifying briefs (see `self-modifying-briefs.md`) are the mechanism — agents can update their own role definitions when they discover the brief is wrong, as long as they journal the change and its reasoning.

Common evolution paths observed in practice:

- **Boundary tightening.** An agent drifts into adjacent work; the negative rights list gets expanded. This is the most common modification — it's easier to discover missing boundaries by hitting them than to predict them at design time.
- **Scope narrowing.** An agent's domain turns out to be too broad for a single brief to capture. The response is either narrowing the scope or splitting into two roles (if the 3-session rule supports both).
- **Input/output refinement.** The agent discovers it needs data from a source not listed in its brief, or produces output that a different consumer needs. These are low-risk modifications that compound into better information flow.
- **Authority adjustment.** The authority gradient shifts — usually expanding as the team builds trust in the agent's judgment within its domain.

The team coach review cycle (see `coaching-framework.md`) is the structural mechanism for catching role drift and proposing boundary adjustments. The coach reads briefs and journals — not memory — and can detect when what an agent actually does has diverged from what its brief says it should do.

## Evidence Summary

The negative-rights principle is **Practised (3 teams, 150+ sessions)**, the strongest evidence in this pattern. Every team that used positive-only role definitions experienced drift; every team that added explicit negative rights saw drift contained. The mechanism (LLM helpfulness overriding vague boundaries) is consistent with how language models behave, but the causal claim hasn't been isolated from other factors.

The six-element role anatomy is **Practised (1 team, 150+ sessions)** — extracted from one team's evolved brief structure, not a tested framework. Other teams used similar elements without following this exact structure.

The authority gradient is **Practised (3 teams, 150+ sessions)**. All three teams converged on a similar gradient independently, which is suggestive but not controlled evidence.

The "when NOT to create" heuristics (including the 3-session rule and context-separation test) are **Practised (2 teams)** — applied in two team bootstraps. The context-separation test was proposed based on the observation that team leads don't self-evaluate composition, and has been used by team coaches in multiple reviews. Its effectiveness at preventing bad agent creation hasn't been directly measured — we know it's been applied, not that it's optimal.

The anti-patterns are drawn from observed failures across multiple teams but the sample is small. They represent things that went wrong, not a comprehensive taxonomy. **Practised (1-3 teams, varying)** for the specific failures described; **Hypothesis** for the claim that these are the most important anti-patterns.

## Related Patterns

- `brief-anatomy.md` — the structure of agent briefs, which is where role definitions live in practice; the seven-section anatomy operationalises the role definition elements described here
- `self-modifying-briefs.md` — how agents evolve their own role definitions over time; the constraints on self-modification (journal everything, research first) apply to role changes too
- `coaching-framework.md` — the team coach assesses specification quality (dimension 1), including role clarity, boundary definition, and drift detection; the review cycle is the structural mechanism for catching role problems
- `codification-ladder.md` — when role-level practices outgrow the brief, the codification ladder determines whether they become playbooks, protocols, or skills
- `agent-team-guide.md` — the practitioner's guide, which covers role design in context (Section 2.1) and the team coach mechanism for role evolution (Section 6)
- `discipline-processes.md` — the authority gradient from role design applies at the task level through human checkpoints in discipline processes
