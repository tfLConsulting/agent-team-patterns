# Anatomy of an Effective Agent Brief

The brief is the most important artifact in an agent team. It's the difference between an agent that produces useful, bounded work and one that drifts, hallucinates scope, or duplicates effort. A good brief sets the game board. The agent figures out how to play.

This pattern covers the structure we've converged on, what we've learned about what works and what doesn't, and how to tell whether a brief is complete.

**Evidence:** Practised (3 teams, 150+ sessions across the source teams). The seven-section structure evolved across all three projects. Early briefs were prescriptive checklists; later briefs converged on the structure below through self-modification and coaching review. The convergence was independent — teams arrived at similar structures without copying each other — which is suggestive but not controlled evidence. Evidence qualifiers for specific claims are noted inline.

## The Seven Sections

### 1. Context (The Business)

What's the situation? What problem is being solved? What stage is the project at? This section is boilerplate shared across agents on a team — it grounds them in the same reality.

We found that including specific numbers where they exist (scale, constraints, key metrics) measurably improved agent decision-making. An agent told "this is a small project" makes different tradeoffs from one told "this is a public patterns library with 12 methodology files and 2 agents." The specifics anchor judgment. **Practised (2 teams)** — two teams independently added quantitative context after observing agents make scale-inappropriate decisions.

### 2. Role (Domain + Authority + Boundaries)

What does this agent own? What decisions can it make? What does it explicitly NOT do?

The boundaries section — the negative rights — is the most important part of the brief. See `role-design.md` for the full pattern. A brief without negative rights produces an agent that drifts into adjacent domains. This was the single most consistent finding across all three projects: every team that started with positive-only role definitions experienced drift within the first few sessions. **Practised (3 teams, 150+ sessions).**

### 3. Starting Intelligence (What You Know)

Specific file paths to read from other agents, with the reason for each. Key findings that shape this agent's work. Dependencies that must be true for the work to matter.

Precision matters here. "Read `agents/team-lead/memory.md` — current priorities and session count" is useful. "Read the team lead's state regularly" is not. Vague cross-references waste attention on instructions the agent can't act on (see `writing-for-ai.md` on instruction density). **Practised (1 team, 150+ sessions)** — extracted from observing agents ignore vague references while consistently acting on precise ones.

### 4. Data Sources (Tools + Access)

Which tools are available? Which files or databases can the agent read? Which external research tools are permitted?

We found that flagging what's unavailable or broken prevented wasted sessions. "Google Search Console integration is coming — not available yet" stops agents from spending a session trying to access data they can't get. The cost of a missing negative flag is an entire wasted session; the cost of including one is a single line. **Practised (2 teams)** — both teams added unavailability flags after observing wasted sessions.

### 5. Approach (Methodology, Not Process)

How this agent moves from input to output. What frameworks apply to this domain. How the agent validates its own confidence.

This section is where the "set the board, don't script the game" principle is most load-bearing. The brief describes the methodology — research-first, depth over breadth, specific quality criteria — not the step-by-step procedure. Over-specified processes produce brittle agents that fail when conditions change. Under-specified approaches produce aimless agents that lack the constraints that would channel effort. The sweet spot is methodology without procedure. **Practised (3 teams)** — teams that started with step-by-step processes self-modified toward methodology descriptions within the first 5-10 sessions.

### 6. Success Criteria (Descriptive, Not Quantitative)

What does good work look like? When should the agent stop researching? What's the feedback loop?

"Recommendations lead to decisions" is better than "produce 5 findings per session." Descriptive criteria let the agent trade depth for breadth based on what the situation demands. Quantitative KPIs create perverse incentives — an agent optimising for count produces shallow work. **Practised (2 teams)** — one team observed the shallow-output problem directly after setting numeric targets; the other adopted descriptive criteria from the start and didn't hit the problem.

### 7. Self-Management (Memory Protocol)

How to maintain memory.md (under 200 lines). Session start/end practices. When to archive versus promote. Link to the memory protocol if it exists as a shared spec.

This section connects the brief to the team's memory architecture. Without it, agents improvise their own memory approach, which produces inconsistency across the team and memory files that drift from the intended structure. See `three-tier-memory.md` for the architecture. **Practised (1 team, 150+ sessions)** — the memory section was added to briefs after observing inconsistent memory practices in the first team.

## What Effective Briefs Don't Include

These exclusions emerged from observed failures, not theory. Each was tried and caused problems.

- **Worked examples of good output.** These anchor the agent to one pattern instead of letting it adapt. An agent given an example of a "good journal entry" produces entries that look like the example rather than entries appropriate to the session. **Practised (2 teams)** — both removed worked examples after observing output anchoring.

- **Approval chains.** Multi-step approval processes create coordination overhead without improving quality. If the agent needs review, name the reviewer. Don't specify a workflow. **Practised (1 team)** — one team simplified approval processes after observing agents getting stuck in multi-step chains.

- **Quantitative KPIs.** "5 findings per session" produces 5 shallow findings instead of 1 deep one. The incentive is count, not quality. **Practised (2 teams)** — described under Success Criteria above.

- **Tool usage instructions.** The agent knows its tools. Telling it how to use them consumes brief space without adding value. Tell it what data to get, not how to get it. **Hypothesis** — reasoned from the writing-for-ai principle that restating what's already known degrades performance, but not directly tested as a removal experiment.

## Worked Examples from This Repo

This repository's own agents illustrate the structure in practice:

**Team Lead** (`agents/team-lead/brief.md`) — a 110-line brief that demonstrates the full seven-section structure. The context section names the repo, its public status, and what the team does. The role section defines routing and synthesis as the domain, with five explicit negative rights ("you don't run web searches, you don't write research documents, you don't draft methodology content..."). Starting intelligence is implicit in the team table and session protocol. Data sources list the agents and their command files. Approach defines two session modes (directed and undirected) rather than a single procedure. Success criteria are embedded in the principles ("depth over breadth," "short output"). Self-management references the three-tier model with specific line limits.

The brief also includes a "known bias" section — acknowledging the team lead's structural tendency toward action over analysis. This isn't part of the seven-section template; it was operator-authored in the bootstrap commit (`e0985ce`, 2026-04-03) as a deliberate addition on top of the standard structure. The design intent is that naming a known bias helps the agent self-correct. **Practised (1 team)** — present in this project's team lead brief since session zero; whether the naming actually moves behaviour is under investigation (`investigations/ai-self-knowledge/`), not yet evidenced.

**Team Coach** (`agents/team-coach/brief.md`) — a brief that demonstrates sharp boundary definition. The "What You DON'T Do" section is extensive and specific. The most important negative right — "Do NOT read other agents' memory files" — is a deliberate context-separation constraint, not just a boundary. The coach evaluates from the outside to maintain a genuinely different cognitive perspective. This illustrates how negative rights can serve architectural purposes beyond preventing drift.

## The Briefable Scope Test

A good brief passes this test: could a competent person in this role read the brief and start working on day one without asking clarifying questions? If yes, an agent can too.

This test also serves as a role design heuristic. If a proposed role can't be briefed clearly — if the brief would need to say "it depends" in too many places — the role may be too broad or too vague to produce focused work. The coaching framework uses this as one criterion for specification quality assessment (see `coaching-framework.md`, dimension 1). **Practised (2 teams)** — applied during coaching reviews to evaluate both brief quality and role viability. Effective as a clarity check; less effective as a completeness check, because a brief can be clear and still miss a section.

## Anti-Patterns

### The Prescriptive Brief

A brief that scripts how the agent works rather than what it owns and why. Step-by-step session protocols, tool-calling sequences, "first do X, then do Y" instructions. The result is an agent that executes the script reliably but fails when conditions don't match the script's assumptions. Every team that started with prescriptive briefs self-modified toward methodology descriptions within the first 5-10 sessions. The brief should set the board; the agent figures out how to play.

The mechanism: LLMs are instruction-followers by default. A prescriptive brief activates that compliance mode at the expense of judgment. A methodology-oriented brief activates reasoning about how to apply principles to the current situation. **Practised (3 teams).**

### The Vague Brief

A brief that gives the agent a domain but no boundaries, no starting intelligence, and no success criteria. "You own research" — research about what? Using which sources? Producing what format? For whom? The result is an agent that produces competent but unfocused work because it lacks the constraints that channel effort.

The fix isn't more words. It's sharper structure. The seven sections above are a checklist — if any section is genuinely blank (not just short), the brief is incomplete. **Practised (2 teams)** — vague briefs were identified and tightened in coaching reviews.

### The Anchored Brief

A brief that includes worked examples, sample outputs, or "here's what good looks like" sections. The agent anchors on the example rather than adapting to the situation. This is especially damaging in creative or analytical roles where the right output varies by context. Removing worked examples from briefs consistently improved output variety without reducing quality. **Practised (2 teams).**

### Missing Negative Rights

The most common brief failure. A brief that says what the agent does but not what it doesn't do. Without negative rights, every agent gradually converges toward doing everything. See `role-design.md` for the full treatment. **Practised (3 teams, 150+ sessions).**

### The Frozen Brief

A brief that was written at bootstrap and never modified. If the brief from session 0 is unchanged at session 15, something is wrong — either the agent hasn't learned anything about its role, or it has learned things but isn't encoding them. Self-modification is the mechanism for briefs to improve (see `self-modifying-briefs.md`). The frozen brief anti-pattern is premature rigidity applied to the most important artifact in the system. **Practised (1 team)** — observed as a risk; the team coach monitors for this in specification quality reviews.

## Evidence Summary

The **seven-section structure** is Practised (3 teams, 150+ sessions). The structure evolved independently across teams, converging from different starting points. The specific section names stabilised after the first ~30 sessions. The structure has been stable since then, suggesting it captures something real about what agents need, though it hasn't been tested against alternative structures in a controlled way.

The **exclusion list** (what briefs don't include) is mixed. Worked examples and quantitative KPIs are Practised (2 teams) — both were tried and removed after observing problems. Approval chains are Practised (1 team). Tool usage instructions are Hypothesis — reasoned from writing-for-ai principles but not directly tested as a removal experiment.

The **briefable scope test** is Practised (2 teams) — used in coaching reviews. Effective as a clarity heuristic but has a known gap: it checks for clarity without checking for completeness.

The **anti-patterns** are drawn from observed failures across multiple teams but the sample is small. The Prescriptive Brief, Missing Negative Rights, and The Anchored Brief are the strongest (Practised, 2-3 teams each). The Vague Brief and Frozen Brief are Practised (1-2 teams). The claim that these are the most important anti-patterns is Hypothesis.

The **quantitative context claim** — that specific numbers in the context section improve agent decisions — is Practised (2 teams) but the mechanism hasn't been isolated. It could be the numbers, or it could be that teams who add numbers also write sharper briefs overall.

## Related Patterns

- `role-design.md` — the authority boundaries and negative rights that the Role section of a brief must define; the six-element role anatomy maps directly to the brief's seven sections
- `self-modifying-briefs.md` — how agents evolve their own briefs over time; the constraints on self-modification (journal everything, research first) keep brief evolution disciplined
- `coaching-framework.md` — the team coach evaluates specification quality (dimension 1), including brief clarity, boundary definition, and drift between what briefs say and what agents do
- `codification-ladder.md` — when practices outgrow a brief addition, the codification ladder determines what form they take next; brief space is finite and the ladder is the overflow mechanism
- `writing-for-ai.md` — instruction density research that constrains brief length; every line in a brief competes for attention, and the editing question is always "what can I cut?"
- `three-tier-memory.md` — the memory architecture that the Self-Management section of a brief references; briefs and memory are the two always-loaded files, so they share the same attention budget
- `agent-team-guide.md` — the practitioner's guide covers brief anatomy in Section 2.2 and brief assessment in Section 5.2
