# Anatomy of an Effective Agent Brief

The brief is the most important artifact in an agent team. It's the difference between an agent that produces useful, bounded work and one that drifts, hallucinates scope, or duplicates effort. A good brief sets the game board. The agent figures out how to play.

## Structure

### 1. Context (The Business)

What's the situation? What problem is being solved? What stage is the business at? This is boilerplate shared across agents — it grounds them in the same reality.

Keep it factual and current. Include specific numbers where they exist (revenue, user count, conversion rates). Agents make better decisions when they know the scale they're operating at.

### 2. Role (Domain + Authority + Boundaries)

What does this agent own? What decisions can it make? What does it explicitly NOT do?

The boundaries section is the most important part of the brief. See `role-design.md` for the full pattern. A brief without negative rights will produce an agent that drifts into adjacent domains.

### 3. Starting Intelligence (What You Know)

Specific file paths to read from other agents, with the reason for each. Key findings that shape this agent's work. Dependencies that must be true for the work to matter.

Be precise: "Read `agents/analyst/activation-analysis.md` — three failure modes, first-session output equals activation" is useful. "Read the analyst's findings regularly" is not.

### 4. Data Sources (Tools + Access)

Which tools are available? Which code files or databases can the agent read? Which external research tools (web search, APIs) are permitted?

Flag what's unavailable or broken: "Google Search Console integration is coming — not available yet." This prevents agents from wasting sessions trying to access data they can't get.

### 5. Approach (Methodology, Not Process)

How this agent moves from input to output. What frameworks apply to this domain. How the agent validates its own confidence.

Do NOT prescribe step-by-step processes, tool-calling sequences, or session templates. The brief sets the board; the agent figures out how to play. Over-specified processes produce brittle agents that fail when conditions change.

### 6. Success Criteria (Descriptive, Not Quantitative)

What does good work look like? When should the agent stop researching? What's the feedback loop?

"Recommendations lead to decisions" is better than "produce 5 findings per session." Descriptive criteria let the agent trade depth for breadth based on what the situation needs.

### 7. Self-Management (Memory Protocol)

How to maintain memory.md (<200 lines). Session start/end practices. When to archive vs. promote. Link to the memory protocol if it exists as a shared spec.

## What Effective Briefs DON'T Include

- **Worked examples of good output.** These anchor the agent to one pattern instead of letting it adapt.
- **Approval chains.** If the agent needs approval, say who reviews; don't specify a multi-step process.
- **Quantitative KPIs.** These create perverse incentives (5 shallow findings vs. 1 deep one).
- **How to use tools.** The agent knows its tools. Tell it what data to get, not how to get it.

## The Test

A good brief passes this test: could a competent person in this role read the brief and start working on day one without asking clarifying questions? If yes, an agent can too.
