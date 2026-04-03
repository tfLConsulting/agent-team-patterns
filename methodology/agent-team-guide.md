# Building Agent Teams: A Practitioner's Guide

This guide is based on building and operating agent teams across three projects over 28+ sessions. The evidence base is narrow: N=3 projects, one operator, one LLM (Claude). What's here works for us. We don't know yet how much of it is universal. We've tried to be honest about the difference.

The guide serves two purposes. For humans, it explains the patterns, the reasoning behind them, and the failure modes we hit. For AI agents, it's actionable — it provides enough structure to assess a project and either create or improve an agent team.

---

## 1. What Agent Teams Are (And When You Don't Need One)

An agent team is a set of AI agents with defined roles, persistent memory, and structured information flows, operating across sessions on a shared project. Each agent has its own context window, its own brief (role definition), and its own memory. They coordinate through files in a shared repository.

We believe the key mechanism is **context separation**. Each agent starts from the same base model, but loading different instructions, different memory, and different prior context produces genuinely different cognitive starting states. This isn't role-playing — a transformer's output distribution is conditioned on its full context window. An agent loaded with "find assumptions and ask hard questions, never propose solutions" and a history of identified blind spots produces fundamentally different computation than a team-lead told "now challenge your own assumptions." The team-lead version operates on context that already contains the conclusions and the reasoning that produced them. The separate agent has none of that baggage.

This is a hypothesis, not a proven mechanism. The evidence is consistent with it (our Skeptic catches things the team-lead doesn't, consistently; our Strategist surfaces tensions the team-lead wasn't tracking; the team-lead has never proposed changing team composition despite having authority to do so — all consistent with context anchoring). But we haven't run controlled experiments to isolate context separation from other possible explanations.

This matters because it means agent teams aren't just a division-of-labour mechanism. They're a heterogeneity engine. Different contexts produce different thinking, which produces better collective output — the same principle behind ensemble methods in ML and cognitive diversity in human teams.

### When a CLAUDE.md Is Enough

A CLAUDE.md is a project-level instructions file that configures how an AI assistant works with your codebase. It's a convention used by Claude Code and similar tools — the equivalent of a persistent system prompt scoped to a project.

Not every project needs agents. A well-written CLAUDE.md handles many projects well. Agents add coordination overhead that's only worth paying when the benefits are clear.

**A CLAUDE.md is probably sufficient when:**
- Work is mostly one type (just coding, just writing, just research)
- Sessions are infrequent or don't build on each other much
- The project is small enough that one conversation can hold all relevant context
- The human is deeply involved in every session anyway

**Agents start earning their keep when:**
- Work spans multiple distinct domains that benefit from different persistent perspectives
- There's recurring work that benefits from memory across sessions
- Complexity is high enough that specialisation and routing improve output quality
- The human wants to operate as a director/reviewer rather than being hands-on in every session

"You don't need agents — here's a better CLAUDE.md" is a valid outcome, not a failure.

---

## 2. Core Patterns That Work

These are the patterns we've found to be load-bearing across all three projects. They're presented as problems and solutions, not prescriptions.

### 2.1 Role Design: Negative Rights Prevent Drift

**The problem:** Agents told "you own content strategy" inevitably drift into design, analytics, implementation, and everything else nearby. Positive role definitions are insufficient boundaries.

**What worked:** Defining what an agent does NOT do matters more than defining what it does. An agent told "you own content strategy; you don't write code, you don't make design decisions, you don't publish without review" stays in its lane.

Each agent's role has:
- **Domain:** What slice of the problem space it owns
- **Authority:** What decisions it can make autonomously (full authority over analysis and recommendations within domain; limited authority over cross-domain decisions; no authority over irreversible actions)
- **Boundaries:** What it explicitly does NOT do — the adjacent roles it could drift into
- **Inputs/Outputs:** What files it reads from other agents and what it produces

Without negative rights, the agent will do everything itself and the team structure becomes pointless. This was consistent across all three projects.

### 2.2 Brief Anatomy: Set the Board, Don't Script the Game

**The problem:** Over-specified briefs (step-by-step processes, tool-calling sequences, worked examples) produce brittle agents that fail when conditions change. Under-specified briefs produce aimless agents.

**What worked:** A brief that gives enough context to start working without being prescriptive about how.

Effective briefs include:
1. **Context** — the project situation, grounded in facts and specifics
2. **Role** — domain, authority, boundaries (with negative rights)
3. **Starting intelligence** — specific file paths to read, with reasons (not vague "read the analyst's findings regularly" but "read `agents/analyst/activation-analysis.md` — three failure modes, first-session output equals activation")
4. **Approach** — methodology and frameworks, NOT step-by-step processes
5. **Success criteria** — descriptive, not quantitative ("recommendations lead to decisions" is better than "produce 5 findings per session")
6. **Memory protocol** — how to manage the three tiers

**What effective briefs leave out:**
- Worked examples of good output (anchors the agent to one pattern)
- Quantitative KPIs (creates perverse incentives)
- Step-by-step tool-calling sequences (set the board; the agent figures out how to play)
- Approval chains (if it needs review, say who reviews; don't specify a multi-step process)

**The test:** Could a competent person in this role read the brief and start working on day one without asking clarifying questions? If yes, an agent can too.

### 2.3 Three-Tier Memory: The Attention Management Problem

**The problem:** The default for AI agents is amnesia. The common fix — "add a vector database" — introduces a retrieval problem on top of the memory problem. The agent doesn't control what gets surfaced. Wrong context at the wrong time causes failures.

**What worked:** Plain files with intentional structure, organised by urgency.

**Hot tier (`memory.md`, under 200 lines):** Loaded every session. Contains only what the agent can't function without — current priorities, recent decisions, next actions, key numbers. Every line competes for the agent's attention, so unnecessary content directly degrades performance.

**Warm tier (topic files, `scratchpad.md`):** Not loaded by default, but the agent knows where to find them. Structured research, analysis, reference data. The scratchpad is a workspace for in-progress thinking, cleared each session.

**Cold tier (`archive/`):** Monthly compressed summaries. Exists for search, not regular consumption.

**The consolidation ritual at session end:** Everything in the scratchpad is triaged — promote to hot if next session needs it, promote to warm if it's enduring reference, archive if historical, discard by default. Then prune memory.md back under 200 lines.

The 200-line limit is the load-bearing constraint. Without it, memory files grow unbounded until the agent is effectively context-stuffing itself into confusion. But it also creates a specific failure mode — see Section 3.1.

### 2.4 File-Based Coordination: One-Way Information Flows

**The problem:** Bidirectional dependencies between agents create circular waits and shared-state bugs.

**What worked:** Agents collaborate through completed outputs, not shared reasoning. Agent A writes a file. Agent B reads it when relevant. No bidirectional dependency, no waiting for responses, no shared context window.

Each agent's brief specifies what files it reads from other agents and what files it produces. These are explicit contracts.

Directory structure reflects information architecture: each agent owns its directory, no agent writes to another agent's directory, shared knowledge lives in a `shared/` directory. If you can't tell what an agent does from its directory contents, the role isn't clear enough.

This also makes the system inherently observable. Every piece of agent reasoning that matters is in a file. You can trace any decision back through the file chain. No logging framework needed — the files ARE the log.

### 2.5 The Team Lead as Router

**The problem:** A team lead that does its own execution work defeats context separation. Its context window fills with implementation details, crowding out routing and strategic decisions.

**What worked:** The team lead reads agent states, decides who runs next, provides direction, and synthesizes outputs. It does NOT run web searches, write research documents, draft content, or do analysis. All execution work is dispatched to sub-agents via separate context windows — even when no specialist agent exists for the task.

Two session modes:
- **Directed:** The human asks for something specific. Route to the relevant agent(s). Just do it.
- **Undirected:** The human says "continue." The team lead assesses current state, picks the single highest-priority next step, dispatches work, synthesizes outputs, writes a journal entry, updates memory.

Undirected sessions are where the team lead earns its keep — the ability to autonomously identify and execute the most important work.

The team lead's own state is minimal — just enough to route:

| Field | Purpose |
|-------|---------|
| Last run date per agent | Know what's stale |
| Key state per agent | One-line summary of where each agent is |
| Strategic priorities | What matters most right now |
| Backlog | Queue of open questions |

This is routing information, not management overhead. The team lead's context window stays clear for decision-making.

**The backlog as governance.** The team maintains a prioritised queue of strategic questions. In undirected sessions, the team lead picks from this queue rather than chasing whatever seems interesting in the moment. Each question gets investigated across one or more sessions. Answered questions stay in the log (marked answered) so the team doesn't re-investigate. This creates a visible record of what the team has learned and what it's currently pursuing.

### 2.6 The Journal as Institutional Memory

Every session produces a journal entry. Not a status update — a narrative of what happened and why. Written for a reader who wasn't there. Honest about uncertainty and changes of mind. Ends with "Next session should focus on..."

Journals serve three purposes:
1. They're the team coach's primary input (see Section 6)
2. They prevent re-investigation of answered questions
3. They create an observable record of how the team's understanding evolved

---

## 3. Known Problems and What We Learned

These are failure modes we've actually hit, not theoretical risks.

### 3.1 Memory Pruning Loses Load-Bearing Decisions

**What happened:** One of our teams spent an entire session building a Firestore newsletter backend. This was wrong — they'd already chosen Buttondown as their newsletter platform in session 9, the operator had set up an account, the calculator page already had a working Buttondown integration, and the privacy policy referenced Buttondown. But the team-lead's memory had been pruned to remove all of this. The 200-line memory limit meant infrastructure decisions were treated as prunable context.

**The cascade:** The broken newsletter meant the team's kill criterion (5 subscribers in 30 days) was measuring nothing. A single pruning decision cascaded into wasted work, a broken feature, and unmeasurable success criteria.

**The deeper problem:** Memory pruning combined with no cross-referencing creates a specific failure mode: the team confidently does wrong work because it doesn't know what it doesn't know. The danger isn't forgetting something important — it's not knowing you've forgotten it.

**What we did about it:** The team created a persistent reference file documenting key decisions not discoverable from code — stored in a location not subject to memory pruning. They also added a "DO NOT PRUNE" section to team-lead memory and a project instructions directive to read the reference file first. This is a structural fix (new file in a stable location) rather than a rule fix (telling the team-lead to be more careful). The general principle: when a behaviour recurs despite rules, fix the structure, not the rules.

### 3.2 Confirmation Bias in Early Sessions

**What happened:** Both teams that used the bootstrapping protocol exhibited confirmation bias in their first 3-5 sessions — each research round validated the previous conclusion rather than challenging it. The team-lead starts as both advocate and judge, with no structural check until the team-coach review fires at session 3.

**What we know:** Whether this is caused by missing protocol features, compressed session timing, or a model-level trait is unclear. The pattern is consistent enough to flag but not well enough understood to prescribe a fix. Awareness of it may be the only portable mitigation — prescriptive fixes (e.g., mandatory adversarial review) face a bootstrap paradox (you need the team to exist before you can run the adversarial review).

### 3.3 Narrative Outrunning Reality

**What happened:** One team's coach evaluated a "post-launch operations" phase transition while the team was still fixing a session-wasting build failure. The newsletter didn't work, Search Console wasn't set up, no domain was registered, no content had been produced, and the immediate next session was still build work. The strategic narrative had advanced further than the actual operational state.

**Why it happens:** Agent teams may have a systematic tendency to advance their narrative faster than their reality. Strategic thinking runs ahead because it's cheaper — no external dependencies, no implementation friction. Operational reality is constrained by the physical world.

**What to watch for:** When the team's self-assessment is evaluating a future state rather than the current one. This is a subtler form of confirmation bias — not confirming the product is good, but confirming the team is progressing.

### 3.4 Inline Execution Defeats Context Separation

**The problem:** When the team lead does execution work itself (research, writing, analysis) instead of dispatching to sub-agents, it defeats the entire purpose of context separation. The team-lead's context window fills with implementation details. It starts reasoning from those details instead of from its routing perspective.

**The fix:** The team-lead brief explicitly states that ALL execution work goes to sub-agents, even when no specialist exists for the task. A general-purpose sub-agent with a clear task description gets its own context window — the team-lead's stays clean. This is non-negotiable. The brief-level rule ("you do not do execution work inline") is necessary because the team-lead will always find it "easier" to just do the work itself.

### 3.5 Teams Can't Escalate

**What happened:** Google Search Console verification and domain registration were pending for 11 sessions in one of our teams. The team flagged these in every journal entry. The kill criteria depended on these human actions. The team could write "URGENT" but had no mechanism to make a human act.

**The structural limitation:** A perfectly functioning team can be blocked indefinitely by a human dependency. This is independent of team quality — it's architectural. Teams designed around "the human might say no" still create dependencies when they need human-world actions (domain registration, platform verification, account setup). The constraint isn't whether the human will do it — it's that the team has no escalation path beyond repeating the request in journal entries.

**What we haven't solved:** There's no good fix for this yet. It's a genuine limitation of autonomous agent teams that anyone setting one up should understand.

### 3.6 Over-Engineering at Bootstrap

**The most likely failure mode:** Creating too many agents, too much structure. A solo project doesn't need 8 agents and formal self-modification protocols. The protocol's own sophistication biases it toward sophisticated outputs.

The mitigation is the two-agent start (see Section 4). Specialist agents are proposed as candidates but not created until the need has recurred across 3+ sessions. A team that starts small and grows into what it needs is better than a team that starts full-size and has agents sitting idle or duplicating work.

A related failure: the initial assessment gets the project type or work domains wrong, producing agents that don't match actual needs. The mitigation is the same — start with two agents and let the team coach evaluate against real usage at session 3.

### 3.7 Cargo Culting Patterns

**What it looks like:** Copying patterns without understanding why they work. Three-tier memory for a project that runs one session per month. Negative rights for roles where drift hasn't been observed. The patterns in this guide solve specific problems — applying them where those problems don't exist adds complexity without benefit.

---

## 4. Starting From Scratch: The Greenfield Path

This section is actionable. When starting with a project that has no agents, follow this sequence.

Creating agents is easy. Creating a *team* — agents with the right roles, sharp boundaries, persistent memory, and coordination patterns — is hard. The hardest part isn't infrastructure; it's figuring out which agents a project actually needs. This is harder than it sounds: a project's codebase doesn't encode its goals or pain points, the person who most needs the protocol is least equipped to evaluate its output, and over-engineering is the default failure mode.

### 4.1 Read the Project First

Before asking the user anything, understand what you're working with:
- Read CLAUDE.md if it exists (you'll add to it, not replace it)
- Read README.md or equivalent project documentation
- Look at the directory structure
- Check package.json, pyproject.toml, Cargo.toml, go.mod, or equivalent for tech stack
- Read recent git log if available (last 10-15 commits)
- Note what kind of project this is (software, content, research, business, operations, hybrid)
- Check if any agent infrastructure already exists (command files, agent directories, skill definitions)

If agent infrastructure already exists, see Section 5 instead.

### 4.2 Interview the User

Ask these questions. Wait for answers before proceeding.

1. **What's the primary goal for this project?** (What you're trying to achieve, not what the code does)
2. **What kinds of work do you regularly do with Claude in this project?** (Code review, feature work, research, writing, analysis, debugging, planning, etc.)
3. **What's frustrating or repetitive about your current workflow?** (Where do you lose context, repeat yourself, or wish Claude remembered more?)
4. **How much time do you spend on this project per week?** (Determines how autonomous the team needs to be)
5. **Is there anything you explicitly do NOT want agents handling?** (Deployment, external communications, financial decisions, etc.)

If the user provided initial direction that already answers some of these, adapt. Don't re-ask what's already clear. Confirm your understanding before proceeding.

### 4.3 Assess Whether Agents Are Warranted

Be honest about this. See Section 1 for the criteria. If agents aren't warranted, say so. Offer to create or improve a CLAUDE.md instead. Do not proceed past this step unless agents genuinely add value.

### 4.4 Create Two Core Agents

Start with exactly two agents. No more.

**The Team Lead** is the agent the user talks to. It maintains strategic context across sessions, routes work to specialist agents, owns the project journal and session protocol, and calls the team coach at regular intervals. It does NOT do execution work.

**The Team Coach** is the agent that evolves the team. It reviews team composition at regular intervals (first at session 3, then every 5 sessions), proposes new agents when recurring needs emerge, proposes retiring agents that aren't contributing distinct value, and evaluates from the outside — reading briefs and journals, but NOT other agents' memory. It applies the context-separation test: would a proposed agent have genuinely different loaded context?

Why only two: the structural contradiction is that our methodology says "create agents only after 3+ sessions demonstrate a recurring need," but bootstrapping creates agents before session 1. The resolution is that the protocol creates the **capacity** for a team, not a finished team. The team lead is justified as the minimal entry point. The team coach exists because the team lead structurally cannot evaluate its own team composition — its context is anchored on the current team. Everything else follows the 3-session rule.

Why the team coach must be a separate agent: we observed that the team-lead has never proposed changing team composition despite having explicit authority to do so. This is consistent with context anchoring — the team-lead's context includes the current team as a given, making it harder to reason about alternatives. The team coach, loading different context (briefs and journals but NOT memory), thinks genuinely differently about team structure.

### 4.5 Propose Candidate Specialists

Based on the project and user interview, identify 2-4 roles that MIGHT become useful. For each, note:
- Name and one-line purpose
- What recurring need it would serve
- What would need to be true for it to be worth creating (the test: has this need recurred across 3+ sessions?)

These are hypotheses that go in the team-lead's memory. Not commitments. They give the team coach something to evaluate at session 3.

**Common team shapes** (for reference, not prescription):
- **Software product:** team-lead, then code-reviewer, architect, tester
- **Content/media:** team-lead, then content-strategist, editor, analyst
- **Research:** team-lead, then researcher, synthesizer, critic
- **Business/strategy:** team-lead, then strategist, skeptic, outcome-guardian
- **Operations:** team-lead, then process-analyst, monitor, reporter

Most projects don't fit neatly into one category. Adapt.

### 4.6 Create the Files

**Directory structure:**

```
agents/
  team-lead/
    brief.md
    memory.md
    scratchpad.md    (empty — session workspace, cleared each session)
  team-coach/
    brief.md
    memory.md
journal/             (empty — journal entries go here)
commands/
  team-lead.md       (command file to invoke team lead)
  team-coach.md      (command file to invoke team coach)
```

**CLAUDE.md:** If one exists, ADD an agent team section. Don't replace existing content. The section should cover: how the team works (state in repo, team lead routes, run sessions via agent invocation commands), operating principles (narrow session focus, self-modification with journaling, research before action), file conventions (where briefs, memory, journals, and scratchpads live), and session protocol (read memory, focus on one thing, do the work, journal, update memory).

**Team Lead Brief:** The most important file. Write it for this specific project following the patterns in Section 2.2. Required sections: one-line role statement, context, what you own, what you DON'T do, your team (table), how to run agents (dispatch via sub-agents, never inline), two session modes (directed/undirected), memory protocol (three tiers), journal protocol, self-modification authority.

**Team Lead Memory:** Initialize with current state (session 0, date), goals from interview, constraints, team table (team-lead and team-coach active, candidates as proposed), team coach schedule (next review: session 3), key decisions (none yet), and next session focus.

**Team Coach Brief:** Write for this specific project. Required sections: one-line role statement, what you own (team composition), what you DON'T do (route work, do project work, read other agents' memory), when you run (session 3, then every 5), how you work (read CLAUDE.md, all briefs, recent journals, own memory — NOT other agents' memory), assessment framework (per-agent, per-candidate, team-wide), the context-separation test, memory protocol.

**Team Coach Memory:** Initialize with creation date, first review due at session 3, current team composition table, empty review history.

**Command files:** Create command files for your tool (e.g., `.claude/commands/team-lead.md` for Claude Code, or equivalent for your environment). Each should instruct the agent to read CLAUDE.md, its brief, and its memory before following its session protocol. Use absolute paths.

### 4.7 Wire in the Learning Loop

The bootstrapping protocol creates team structure. It should also create the mechanism for that structure to improve. Three things to set up at bootstrap, not bolt on later:

1. **Experiment log.** An empty file (e.g., `team-coach/experiment-log.md`) with a template for tracking structural choices. Every choice made during setup — memory architecture, role design, session protocol — is the first batch of entries. Status: active. Observed impact: blank (to be filled after running). See [learning-from-practice.md](learning-from-practice.md) for the template.

2. **Micro-observation prompt in the session-close protocol.** Add to the team-lead's brief: *"What about our team's setup helped or hindered this session's work?"* — 1-3 sentences in the journal entry. This is the cheapest form of learning, and it doesn't happen unless it's in the protocol.

3. **Treat the first ~10 sessions as exploration.** The bootstrapped structure is a starting point. Agents should record what's working and what isn't from session 1. The team coach's first review (session 3) should check the experiment log alongside composition.

### 4.8 Verify and Hand Off

Read back each file to confirm coherence and correct paths. Tell the user:
- What was created and why
- How to run their first session — invoke the team lead with "continue" or a specific direction
- That the team-coach will review composition at session 3 and propose specialists based on actual usage
- That everything is provisional — the team evolves through use

---

## 5. Improving an Existing Team

When a project already has agents, the job is assessment and improvement, not replacement. Be particularly careful when the existing team's patterns predate this guide — some of these patterns were extracted from working teams. An existing team that doesn't match the guide may have local adaptations that work better. Assess divergences as questions to investigate, not gaps to fix.

### 5.1 Read Everything First

Read all existing state before doing anything else:
- CLAUDE.md
- All agent briefs (`agents/*/brief.md`)
- All agent memory files (`agents/*/memory.md`)
- Recent journal entries (last 5-10, or since last team-coach review)
- Strategy documents if they exist
- Any learnings, research, or introspection files

Do NOT re-ask the user questions that the files already answer. The interview (Section 4.2) is for when there's no existing state.

### 5.2 Assess Against the Core Patterns

Check for each pattern from Section 2:

**Role design:**
- Do agents have clear negative rights (what they DON'T do)?
- Are boundaries sharp enough to prevent drift?
- Is there overlap where two agents cover similar ground with similar context?
- Are there gaps where recurring work isn't owned by any agent?

**Briefs:**
- Do they follow the anatomy (context, role, boundaries, inputs, approach, success, memory)?
- Are they over-specified (step-by-step processes, worked examples, quantitative KPIs)?
- Could a competent person start working from each brief without clarification?

**Memory:**
- Is the three-tier model in place (hot/warm/cold)?
- Are hot memories under 200 lines?
- Is there a consolidation ritual?
- Are load-bearing decisions protected from pruning? (See Section 3.1)

**Coordination:**
- Is the team lead routing, not doing execution work?
- Are information flows one-way through completed outputs?
- Does each agent know what it reads and what it produces?

**Team evolution:**
- Is there a team coach or equivalent review mechanism?
- Does it run at regular intervals?
- Does it evaluate from the outside (not reading other agents' memory)?
- Does it apply the context-separation test?

### 5.3 Identify Gaps and Suggest Improvements

Present findings as observations with evidence, not mandates. For each finding:
- What the current state is
- What pattern it diverges from
- Why the pattern exists (the problem it solves)
- What the specific risk or cost of the current approach is
- A suggested change, with reasoning

Prioritize. Don't dump 15 improvements at once. Identify the 2-3 highest-impact changes and explain why they matter most.

### 5.4 Implement Changes Carefully

When modifying existing files:
- ADD to CLAUDE.md, don't replace existing content
- Preserve existing agent briefs' project-specific context
- Don't overwrite memory files — they contain hard-won state
- Journal any changes with reasoning
- If retiring or significantly modifying an agent, discuss with the user first

---

## 6. How Teams Grow: The Team Coach Mechanism

Teams don't grow through upfront planning. They grow through observed need.

### The 3-Session Rule

Before creating a specialist agent, the need must have recurred across 3+ sessions. This prevents the over-engineering failure mode. One session of needing code review doesn't justify a code-reviewer agent. Three sessions of it — with the team-lead noting each time that it's routing similar work to general-purpose sub-agents — does.

### The Context-Separation Test

Before proposing a new agent: "Would this role produce genuinely different thinking due to context separation, or would it just be the team-lead wearing a different hat?"

This is the most important test. If the proposed agent would read mostly the same files and have mostly the same brief focus as an existing agent, it fails the test. The value of a new agent comes from it loading different context and therefore computing differently — not from having a different name.

### The Team Coach's Review Cycle

The team coach runs at session 3 (first review, when bootstrapped candidates can be evaluated against real usage) and every 5 sessions after that. This is a forcing function in the team-lead's protocol, not optional.

The team coach:
1. Reads CLAUDE.md, all agent briefs, and recent journal entries
2. Does NOT read other agents' memory files (evaluates from the outside only)
3. Assesses each current agent: producing distinct value? Role drifted? Could another agent absorb its work?
4. Assesses proposed agents: need recurred across 3+ sessions? Would have genuinely different loaded context?
5. Assesses the team as a whole: gaps, overlaps, size, context diversity
6. Proposes specific changes with reasoning, or recommends no changes (a valid outcome)

Why the team coach doesn't read memory: this context separation is deliberate. The coach evaluates what was produced and how the team functioned, not what individual agents think about their own work. This gives it a genuinely different perspective from the agents being evaluated.

### Self-Correction

We observed a team coach self-correct on its own recommendations. It had recommended programmatic quality enforcement (ESLint, Prettier, CI pipeline) in four consecutive reviews. The team ignored it each time. In the fifth review, the coach explicitly downgraded the recommendation, noting that the team had maintained 74 passing tests, clean builds, no regressions, and shipped quality improvements from 5/10 to 7.8/10 — all without the recommended tooling.

Whether this is genuine learning or the agent rationalising non-compliance is an open question. But it demonstrates that the review mechanism can update its own assessment framework based on outcomes, not just principles. That's a useful property.

### Scaling Limits

Each new agent adds one more memory file to read and one more routing decision. At 4-6 agents this is manageable. At 10-12 it strains. Beyond that, you likely need sub-teams with their own team leads.

The scaling limit isn't compute — it's the team lead's ability to hold enough context about each agent's state to make good routing decisions. This is why thin state tracking matters: if the team lead needs to read 200 lines of memory per agent to decide who runs next, 8 agents means 1,600 lines of routing context before any work begins.

---

## 7. How Teams Acquire Expertise: The Skills Meta-Pattern

Bootstrapped teams can structure themselves effectively but can't autonomously acquire domain expertise. We discovered this when one team's visual design scored 5/10 despite strong content (8/10). The team coach could diagnose the problem — visual quality was weak — but couldn't prescribe how to fix it. The fix came from outside the team.

### What Happened

The team loaded three research-backed skills (ui-design, landing-page-design, technical-seo) into its builder agent. Visual quality moved from 5/10 to 7.8/10 across four sessions. Same agent, same brief, dramatically different output.

### The Finding: Specification, Not Execution

The team coach's diagnosis was precise: "The builder's spec compliance has been consistently excellent throughout the project. The 5/10 visual score was never a builder problem — it was an upstream specification problem."

The difference was between conceptual descriptions ("navy primary palette", "calm, authoritative") and precise specifications (exact Tailwind classes like `bg-[#1B2B4B]`, `py-16 sm:py-24`). Skills gave agents the vocabulary to write implementable specifications.

This is a meaningful distinction. The bottleneck in agent quality is often at the specification layer, not the execution layer. Agents are good at following precise instructions. They're bad at interpreting vague ones — which looks like poor execution but is actually poor specification.

### The Meta-Pattern

When a team hits a domain expertise gap:
1. **Identify the gap** — the team coach or team lead notices quality issues in a specific domain
2. **Research deeply** — investigate best practices, frameworks, and domain-specific knowledge
3. **Encode as loadable knowledge** — create a skill file or reference document that gives agents the vocabulary to write precise specifications in that domain
4. **Update quality gates** — adjust how the team evaluates output in that domain, now that it knows what good looks like

This meta-pattern — "when you don't know how to specify well in a domain, research it and encode what you learn" — is the portable insight. It teaches teams to close their own knowledge gaps rather than depending on external intervention.

### Evidence Base

This is validated (N=1 project, 4 sessions, measured improvement from 5/10 to 7.8/10). The finding that specification is the bottleneck is clean and has held up to scrutiny. The meta-pattern itself is a hypothesis derived from one instance. We believe it's likely portable but haven't tested it across diverse domains.

---

## 8. Multi-Team Considerations

**Note:** We haven't operated multiple teams in one repo yet. This section is reasoning from principles, not from experience. Treat it accordingly — validate early if you try it.

Some codebases contain multiple independent products or workstreams. Each may warrant its own agent team.

### When to Split

Consider separate teams when:
- Two workstreams have genuinely different goals, constraints, and success criteria
- A single team lead can't hold meaningful context about both
- The workstreams have different cadences (one active, one maintenance)
- Domain expertise doesn't transfer (a frontend product team and a data pipeline team have nothing to share at the agent level)

### When to Keep One Team

Keep a single team when:
- The workstreams share infrastructure, users, or strategic goals
- Decisions in one affect the other regularly
- The total volume of work doesn't strain a single team lead's routing capacity

### Shared vs. Separate Infrastructure

If you split teams:
- Each team gets its own `agents/` directory tree (e.g., `agents/product-a/team-lead/`, `agents/product-b/team-lead/`)
- CLAUDE.md can be shared (project-wide instructions) with team-specific sections
- Journal directories are separate (`journal/product-a/`, `journal/product-b/`)
- Command files are separate (e.g., `commands/product-a-team-lead.md`)
- Shared reference material can live in a common directory both teams read from

The key principle: teams should be able to operate independently. If team A's session regularly needs to read team B's state, they're probably one team.

---

## 9. Self-Modification: How Teams Learn

Agents can propose and make changes to their own role definitions, strategy documents, and operating procedures. This is what separates an agent team that learns from one that merely executes.

### What Can Change

- **Briefs:** Role definitions, authority boundaries, inputs/outputs
- **Strategy:** Priorities, hypotheses, positioning
- **Team composition:** Proposing new agents or retiring ones (via team coach)
- **Memory protocol:** How information flows between tiers
- **Operating procedures:** Session protocols, maintenance triggers

### What Makes It Safe

Self-modification without discipline is chaos. The constraints:

1. **Journal everything.** Every modification is recorded with what changed and why. This creates accountability and allows rollback.
2. **Research before changing.** Don't modify based on a hunch. The research-first loop applies to self-modification too.
3. **Preserve core commitments.** Honesty and research-first thinking don't change. Everything else is fair game.
4. **Human review for irreversible changes.** Adding a new agent, changing strategic direction, retiring a role — these warrant discussion. Tweaking a session protocol doesn't.

### In Practice

From our 8-agent team running 1+ month: the team lead updated the strategy document 5 times as understanding deepened. An SEO analyst role was created when three recurring needs were identified. The memory protocol was overhauled when files grew too large — the agent team designed its own fix. Session protocols evolved from rigid checklists to flexible directed/undirected modes.

None of these changes required human intervention to identify. The agents surfaced the problems, proposed solutions, and implemented them. The human reviewed and approved.

### Premature Rigidity

A failure mode worth flagging: the bootstrapped structure gets treated as permanent. Nobody exercises self-modification because the bootstrap felt authoritative. The bootstrapped team is deliberately underpowered and provisional. Everything should change as the team learns what it actually needs. If the brief from session 0 is still unchanged at session 15, something is wrong.

---

## 10. Actionable Reference: Assessment and Creation Checklist

This section provides a quick-reference checklist for common scenarios.

### Scenario A: Greenfield Project (No Agents)

1. Read the project (Section 4.1)
2. Interview the user (Section 4.2)
3. Assess whether agents are warranted (Section 4.3)
4. If yes: create team-lead + team-coach + file infrastructure (Section 4.4-4.7)
5. Propose candidate specialists (Section 4.5)
6. Verify and hand off (Section 4.8)

### Scenario B: Existing Agent Team

1. Read all existing state (Section 5.1)
2. Assess against core patterns (Section 5.2)
3. Identify highest-impact gaps (Section 5.3)
4. Suggest specific improvements with evidence and reasoning
5. Implement changes carefully, preserving existing state (Section 5.4)

### Scenario C: CLAUDE.md Exists but No Agents

1. Read the project and CLAUDE.md
2. Assess whether the existing CLAUDE.md is sufficient or agents would help
3. If CLAUDE.md is sufficient: suggest improvements to it
4. If agents are warranted: follow Scenario A, being careful to ADD to the existing CLAUDE.md

### Scenario D: Multi-Team Setup

1. Identify the distinct workstreams
2. Assess whether they warrant separate teams (Section 8)
3. If separate: create independent team structures with appropriate namespacing
4. If shared: create one team with a broad enough team-lead brief to cover both

---

## 11. Using This Methodology in Another Project

The core architecture is: the bootstrapping agent reads the methodology, then creates a team that owns its own files and doesn't need ongoing access to the methodology.

When bootstrapping an agent team in a new project, the bootstrapping agent reads this guide (and any relevant pattern files in `methodology/`) to understand the patterns — context separation, negative rights, memory tiers, the team coach mechanism, the 3-session rule. It then creates briefs, memory files, journals, and directory structure that embody those patterns for that specific project. Once created, the running team works from its own files. It does NOT need ongoing access to this methodology folder. The patterns are encoded in the team's own artifacts. The methodology is a bootstrap-time reference, not a runtime dependency.

This matters because the methodology folder will often be outside the new project's working directory or sandbox. Ongoing cross-repo reads are fragile and add latency. A self-sufficient team is more robust than one that depends on an external reference.

When encoding patterns into the team's own files, include the reasoning, not just the rules. Team coach briefs should explain WHY the team lead can't evaluate its own composition (its context is anchored on the current team, so it structurally can't reason about alternatives) — not just say "apply context-separation test." Rules without reasoning get self-modified away because the agent doesn't understand what they protect. The 3-session rule, context-separation test, negative rights principle, and memory pruning discipline should all be baked into briefs with their rationale. The full case studies and evidence base (Sections 3 and 7) are nice-to-have background but not load-bearing for the running team.

If you want the team to have ongoing access — for example, when making significant structural decisions like team composition changes or memory protocol overhauls — either copy the relevant pattern files into the target project's `agents/shared/` or equivalent directory, or keep a reference to this methodology repo that the team can consult. But this is optional. A well-bootstrapped team carries what it needs in its own briefs and memory.

---

## 12. What This Guide Doesn't Do

**Predict the right team.** It creates infrastructure and a starting point. The right team emerges through use.

**Replace operator judgment.** The bootstrapping protocol is designed for people who don't yet know how agent teams work, but evaluating its output requires that knowledge — a bootstrap paradox that's inherent, not fixable by better protocols. The first few sessions require more human judgment than later ones. Evaluating whether the team lead's proposals make sense, whether the brief captures the right boundaries, whether the memory is retaining the right things — these need a human until the team stabilises.

**Guarantee session-1 productivity.** The first few sessions calibrate the team. Expect iteration.

**Work for every project.** Some projects are better served by a good CLAUDE.md alone. The assessment gate exists for this reason.

**Transfer across LLMs without adaptation.** This was developed and tested with Claude. The principles (context separation, negative rights, memory tiers) are likely portable. The specific implementations (brief structure, memory limits, coordination patterns) may need adjustment for different models. Additionally, Claude Code's capabilities change rapidly. If native features subsume what this guide provides, the guide becomes unnecessary — and that's fine.

**Provide diverse validation.** N=3, same operator, same LLM. These patterns work for us. Presenting them as universal best practices without broader validation would be framework over-extraction. We've tried to be clear about what's validated versus what we believe but haven't tested.

**Solve the human dependency problem.** Agent teams can't escalate effectively. A perfectly functioning team can be blocked indefinitely by a human who doesn't act on flagged dependencies. This is architectural, not fixable by better protocols.

---

## Compatibility with Claude Code Native Agent Teams

Claude Code's native Agent Teams feature (shipped Feb 2026) provides concurrent execution, shared task lists, and inter-agent messaging. This is complementary, not competing:

- **Native Agent Teams** handles execution: running multiple agents concurrently, coordinating within a session.
- **The file-based approach** handles persistence: roles that maintain memory across sessions, briefs that evolve, journal narratives that compound.

A project can use both. This guide creates the persistent layer (briefs, memory, coordination patterns). Native Agent Teams handles the execution layer if needed.
