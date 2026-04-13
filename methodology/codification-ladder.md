# The Codification Ladder

Every agent team develops recurring practices. An agent that always checks the backlog before starting work. A two-step handoff sequence that emerges between agents. A memory-pruning approach that one agent figures out and others start copying. The question isn't whether these practices exist — they always do. The question is when they deserve to be written down, and in what form.

Get this wrong in either direction and the team pays. Under-codify and the same practice gets reinvented every session, with different quality each time. An agent with no accumulated context — a cold start, which is what every session is — has to rediscover what a previous session already learned. Over-codify and the team drowns in process artifacts that cost attention to maintain but don't actually change behaviour. The codification ladder is a framework for finding the right level of formality for a recurring practice.

**Evidence:** Practised (1 team, 150+ sessions). The ladder structure was extracted from one team's practice over many coaching reviews. The four tiers reflect how that team naturally organised its codified patterns. The promotion heuristics and anti-patterns are structural proposals informed by observed failures, not independently validated.

## The Problem for Agent Teams Specifically

Human teams can rely on tribal knowledge — shared understanding that lives in people's heads and gets transmitted through hallway conversations, pair programming, or institutional memory. Agent teams cannot. Every session is a cold start. The agent reads its brief, its memory, and whatever context files it's pointed at. Anything not written down doesn't exist.

This makes codification both more necessary and more dangerous than in human teams. More necessary because there's no informal channel for transmitting practices — if it's not in a file, it's lost. More dangerous because agents treat written instructions as authoritative. A human can read an outdated process document and think "nobody actually does it this way anymore." An agent follows what's written, even when what's written has drifted from what works.

The cold-start problem means the cost of not codifying is higher. The authority problem means the cost of codifying badly is also higher. The ladder helps navigate between these.

## The Two-Part Test

Not every recurring practice should be codified. A two-part test determines whether a pattern is worth writing down:

**1. Recurrence.** Has it happened three or more times? A single occurrence isn't a pattern — it might be a one-off response to unusual conditions. Two occurrences are suggestive. Three is enough to say "this keeps happening."

**2. Cold-start value.** Would an agent with no accumulated context benefit from having it written down? Some practices are obvious enough that any competent agent would arrive at them independently. Others require specific knowledge that only emerges through experience.

Both conditions must be met.

A practice that recurs but has no cold-start value doesn't need codification. Example: "read the brief before starting work." This happens every session, but it's obvious — no agent needs a process document telling it to read its own brief. Codifying the obvious adds noise without adding signal.

A practice that would help a cold-start agent but has only occurred once isn't established enough to codify. Example: an agent discovers a clever workaround for a specific tool limitation during one session. Useful, but the workaround might not generalise. Wait for recurrence before codifying, or record it as a micro-observation in the session journal where it can be promoted later if the pattern repeats.

A practice that passes both tests: checking a shared backlog file for priority changes before starting session work. It recurs every session, and an agent without this practice would start work based on stale priorities from its memory. Cold-start value is high; recurrence is established. This warrants codification.

## Four Tiers of Codification

When both conditions are met, the next question is what form the codification should take. Four tiers, from lightest to heaviest:

| Tier | Scope | Persistence | Cost to maintain |
|------|-------|-------------|-----------------|
| **Brief addition** | Single agent | Permanent (always loaded) | Low |
| **Playbook** | Single agent | On-demand (loaded when needed) | Moderate |
| **Protocol** | Team-wide | Permanent (all agents follow) | High |
| **Skill** | Any agent | Loadable (structured process) | Highest |

The principle: codify at the lightest tier that works. Each tier up adds coordination overhead, maintenance burden, and context cost. Start light and promote only when the lighter form proves insufficient.

### Tier 1: Brief Addition

A line or short paragraph added to a single agent's brief. It's the lightest form of codification — always loaded, always present, zero activation cost.

**When to use.** The practice is specific to one agent, applies every session, and can be expressed in one to three sentences. It doesn't require steps, branching logic, or significant explanation.

**What it looks like.** A direct instruction embedded in the agent's brief alongside its role definition, responsibilities, and operating principles.

**Example.** A team lead agent that repeatedly forgot to check whether other agents had updated their memory files before starting a coaching review. After the third occurrence, a line was added to the brief: "Before any coaching review, verify that all agents have current memory files — check timestamps against the last session date." One sentence. Permanent. Solved the problem.

**The constraint.** Brief space is finite and every line competes for attention. The research on instruction density (see `writing-for-ai.md`) shows that accuracy degrades as instruction count grows. A brief that accumulates dozens of additions becomes a brief where important instructions get missed. This is the primary force that pushes practices up the ladder — not that the brief addition doesn't work, but that the brief can't hold any more.

### Tier 2: Playbook

A standalone document describing a multi-step process for a single agent, loaded on demand rather than permanently.

**When to use.** The practice is too complex for a brief line, involves multiple steps or decision points, but is still specific to one agent. It doesn't run every session — it runs when certain conditions are met.

**What makes it a playbook rather than a brief addition.** Length and conditionality. If it needs more than three sentences, or if it only applies in specific situations, it shouldn't consume permanent brief space. The brief might reference the playbook — "when conducting a deep research session, follow the research playbook" — but the playbook itself lives in a separate file loaded when needed.

**Example.** A research agent that conducts periodic competitive analyses. The analysis involves five phases: scope definition, source identification, data collection, synthesis, and output formatting. Each phase has specific quality criteria and common pitfalls. This can't fit in a brief line, and it doesn't run every session. It's a playbook: a file the agent loads when a competitive analysis is triggered.

**The constraint.** Playbooks require the agent to know they exist and when to reach for them. If the trigger conditions aren't clear in the brief (Tier 1 metadata — see `discipline-processes.md` on progressive disclosure), the playbook sits unused. A playbook that's never loaded is dead process.

### Tier 3: Protocol

A practice that all agents on the team follow, embedded in shared operating procedures or team-wide instructions.

**When to use.** The practice involves coordination between agents, or consistency across agents matters. One agent doing it isn't enough — the value comes from everyone doing it the same way.

**Example.** "All agents update their memory file before session close." This only works if every agent does it. If three of five agents update memory and two don't, the agents that read others' memory files get an inconsistent picture. The practice is only valuable as a team-wide commitment.

**The coordination overhead.** Protocols are expensive. They need to be communicated to every agent (consuming brief space or shared instruction space across the entire team), monitored for compliance, and updated everywhere when they change. A protocol change in a five-agent team means updating five briefs or one shared instruction file — either way, there's a coordination cost that brief additions and playbooks don't have.

**When it's worth paying.** When the failure mode is inconsistency rather than omission. If one agent not following the practice breaks things for other agents, it's a protocol. If one agent not following the practice only affects that agent's own output, it's a brief addition or playbook.

**The compliance problem.** Protocols are the tier most vulnerable to drift. In observed practice, agents under-complied with protocols more than with brief additions — the wiki protocol (described in `learning-from-practice.md`) was followed zero times in 75 sessions despite being documented. A protocol that isn't followed is worse than no protocol because it creates a false sense of coordination. If compliance tracking reveals persistent non-compliance, the protocol either needs enforcement mechanisms or needs to be retired.

### Tier 4: Skill

A structured, loadable process that any agent can invoke. The heaviest form of codification. Skills have their own architecture — progressive disclosure with metadata, instructions, and reference tiers (see `discipline-processes.md` for the full pattern).

**When to use.** The practice is domain-specific, complex enough to warrant structured phases with checkpoints, and valuable across agents rather than specific to one. Skills encode discipline methodologies — UX research processes, content strategy frameworks, code review procedures — that benefit from the consistency and depth that a structured process provides.

**The investment.** Building a skill requires research into the discipline's established methodology, structuring it into phases and checkpoints, writing it for AI consumption (applying `writing-for-ai.md` principles), and assigning content to progressive disclosure tiers. This is significantly more work than adding a line to a brief. The payoff is repeatable quality: the same process executed the same way every time, across any agent that loads it.

**When the investment is justified.** When improvised execution produces inconsistent quality and the practice is frequent enough that consistency matters. A team that runs design reviews occasionally might get by with a playbook. A team that runs them weekly needs a skill — the consistency gain across dozens of executions justifies the upfront investment.

**Example.** A content audit skill with five phases (inventory, evaluation, gap analysis, recommendation, prioritisation), each with quality rubrics and anti-patterns. Any agent can load and execute it. The skill ensures the audit follows established content strategy methodology rather than whatever approach the agent improvises.

## Promotion Heuristics

Patterns move up the ladder when the current tier proves insufficient. The key principle: **promotion should be reactive, not proactive.** Don't promote a brief addition to a playbook because it might outgrow the brief. Wait for evidence that it has.

### Signals that the current level isn't working

**Brief addition to playbook.** The brief line keeps getting violated or partially followed because the practice is more nuanced than one sentence can capture. Agents follow the letter of the instruction but miss the intent because the reasoning and edge cases aren't there. Or the brief is reaching its density limit and lower-value additions need to move out to make room.

**Playbook to protocol.** Multiple agents have independently developed their own versions of the same playbook, with inconsistencies that cause coordination problems. Or one agent follows the playbook and another doesn't, and the inconsistency creates downstream issues for other agents.

**Protocol to skill.** The protocol is complex enough that agents execute it inconsistently even when they intend to follow it. The steps involve enough domain knowledge and decision points that unstructured instructions produce variable quality. Or the protocol would benefit from quality rubrics, anti-patterns, and staged execution that only the skill architecture supports.

**Playbook to skill.** The playbook works for the agent it was written for, but other agents need it too and the process is complex enough that a simple file share isn't sufficient — it needs the progressive disclosure and structured phases of a full skill.

### The reactive principle in practice

A team notices that their "check for priority changes" brief addition has grown to a five-line paragraph with caveats and exceptions. It still works, but it's consuming valuable brief space and the caveats are getting ignored. Evidence: two sessions where the agent checked the backlog but missed a priority change because the caveat about checking both the backlog and the memory file was buried. Reactive promotion to a playbook that covers the full priority-checking procedure with its edge cases.

Compare with proactive promotion: "this brief addition is getting long, it might cause problems someday, let's make it a playbook now." The problem with proactive promotion is that you pay the maintenance cost of the heavier form before you know it's needed. Sometimes a five-line brief addition works fine. You can't tell until it doesn't.

## Anti-Patterns

### Premature Formalization

Codifying after one occurrence, or codifying at too heavy a tier. An agent encounters a situation, handles it well, and someone immediately writes a protocol for it. The protocol sits in the shared instructions, consuming attention, for a situation that may never recur.

The maintenance tax is real. Every codified practice needs to be kept current, reviewed for relevance, and updated when the context changes. A library of 30 protocols, half of which address situations that happen once a quarter, is a library where agents skim rather than read — and the important protocols get missed along with the irrelevant ones.

The two-part test exists to prevent this. Wait for recurrence. Wait for cold-start value. Don't codify the first time something works.

### Formalization Debt

The opposite failure: a pattern that clearly needs codification but remains as tribal knowledge — or rather, as knowledge that only exists in journal entries and agent memory, neither of which a cold-start agent reliably consults.

The symptom is session-to-session inconsistency. The same task gets done three different ways across three sessions, with varying quality, because no agent has access to the approach that worked best. The knowledge exists somewhere in the journal archive, but no agent reads the full journal archive at session start.

Formalization debt compounds. Each session that reinvents the practice is a session that might discover a worse approach. And unlike financial debt, formalization debt is invisible — there's no line item showing what knowledge is being lost. The coaching framework (see `coaching-framework.md`, dimension 3: process maturity) is one mechanism for surfacing it.

### Promotion Without Retirement

When a practice is promoted from one tier to a higher tier, the old form should be replaced or removed. A brief addition that gets expanded into a playbook should become a brief reference to the playbook, not remain as a brief addition alongside the playbook.

When both forms persist, agents face contradictions. The brief says "check the backlog file at session start." The playbook says "check the backlog file and the priority override channel at session start." Which one does the agent follow? Usually whichever it reads last, which depends on context loading order — not a reliable coordination mechanism.

The discipline: when promoting, remove or replace the old form in the same change. Don't leave it for a future cleanup pass. Future cleanup passes are where process hygiene goes to die.

### Process Theatre

Codification that exists to demonstrate rigour rather than to improve outcomes. The test is simple: would removing this process change anyone's behaviour? If the answer is no — if agents would do the same thing with or without the documented process — the process is theatre.

Process theatre is particularly insidious in agent teams because agents don't push back on pointless processes the way humans do. A human team member who's told to fill out a form that nobody reads will eventually stop filling it out, or complain, or find a workaround. An agent follows instructions. It will fill out the form forever, consuming context and tokens, producing output that nobody consumes.

The output-to-action ratio from the coaching framework (see `coaching-framework.md`, dimension 4) is the diagnostic: if a codified process produces artifacts that have no downstream consumer, it's a candidate for process theatre. Retire it and see if anything breaks. If nothing breaks, it was theatre.

## Lifecycle

Codified patterns aren't permanent. They move through a lifecycle:

**Promotion.** The current tier proves insufficient and the pattern moves to a heavier form. Described above.

**Demotion.** A pattern was over-formalised and the maintenance cost exceeds the value. A protocol that was written for a five-agent team might be demoted to a playbook when the team shrinks to two agents and the coordination overhead is no longer justified. A skill that's only used by one agent and doesn't need structured phases might be demoted to a playbook.

Demotion is psychologically harder than promotion — it feels like admitting a mistake. But over-formalisation is a real cost, and demotion is the fix. The signal: a codified practice that's being maintained but isn't producing value proportional to its maintenance cost. If a protocol takes effort to keep current and only one agent actually benefits from it, demote it to a brief addition for that agent.

**Retirement.** The practice no longer recurs, or the context has changed enough that it's no longer valuable. Retired patterns are removed from active instructions but can be preserved in version control history. The signal: a practice that hasn't been triggered in a defined number of sessions and wouldn't be missed. The coaching framework's process lifecycle review is the natural place to identify retirement candidates.

**Merging.** Two separately codified patterns that turn out to be aspects of the same underlying practice. Common when patterns are codified at different times by different agents who didn't know the other pattern existed. The signal: two patterns that are always triggered together, or that have overlapping instructions with minor variations. Merge into one pattern at the appropriate tier.

Each of these lifecycle transitions should be journalled — what changed, why, and what evidence prompted it. This creates the audit trail that makes future lifecycle decisions easier.

## Evidence Summary

The four-tier structure (brief addition, playbook, protocol, skill) is **Practised (1 team, 150+ sessions)**. These tiers emerged from how one team naturally organised its codified patterns, not from a theoretical framework. The team used all four tiers, promoted patterns between tiers, and retired patterns that stopped serving.

The two-part test (recurrence + cold-start value) is **Practised (1 team, 150+ sessions)**. It was applied in coaching reviews to evaluate which recurring practices warranted codification.

The promotion heuristics (reactive over proactive, specific tier-to-tier signals) are **Hypothesis**. They are structural proposals extracted from observed promotions, not a tested decision framework. The reactive principle is a belief that could be falsified — a team that proactively promotes patterns might achieve better outcomes with lower total cost.

The anti-patterns are drawn from observed failures but the sample is small — they represent things that went wrong in one team's practice, not a comprehensive taxonomy of codification failures. **Practised (1 team)** for the specific instances described; **Hypothesis** for the claim that these are the most important anti-patterns.

The lifecycle framework (promotion, demotion, retirement, merging) is **Hypothesis** at the system level. Individual transitions have been observed (patterns were promoted and retired), but the lifecycle as a described system has not been deliberately run.

## Related Patterns

- `coaching-framework.md` — the codification ladder originated as part of the coaching framework's process maturity dimension (dimension 3); coaching reviews are a natural trigger for evaluating codification levels
- `discipline-processes.md` — the skill tier in depth, including progressive disclosure, anti-patterns as first-class citizens, and the meta-process for building skills
- `self-modifying-briefs.md` — brief additions are a form of self-modification; the constraints on self-modification (journal everything, research first) apply to codification decisions too
- `learning-from-practice.md` — the confidence levels and evidence framework used throughout this pattern, and the experiment log as a mechanism for tracking codification changes
- `writing-for-ai.md` — instruction density research that constrains how much can fit in a brief, which drives promotion from brief additions to heavier forms
- `brief-anatomy.md` — the structure of briefs, relevant to understanding the constraints on Tier 1 additions
