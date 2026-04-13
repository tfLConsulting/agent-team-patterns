# File-Based Coordination

Most multi-agent frameworks coordinate through message passing, shared memory, or orchestration layers. We found that file-based coordination -- agents collaborating through completed outputs rather than shared reasoning -- is simpler, more observable, and more robust. The core mechanism is one-way information flow: Agent A writes a file, Agent B reads it when relevant. No bidirectional dependency, no waiting for responses, no shared context window.

**Evidence:** Practised (3 teams, 150+ sessions across the source teams). The one-way flow principle and directory-as-architecture model have been stable across all three projects. Explicit file contracts emerged independently in each team. The failure modes and anti-patterns draw from observed breakdowns in those teams, though the sample is small. Evidence qualifiers for specific claims are noted inline.

## The Core Pattern: One-Way Information Flow

Agents collaborate through completed outputs, not shared reasoning. Each agent knows its readers (from its brief). Each reader knows where to look (from its brief). Nobody guesses.

```
Analyst writes activation-analysis.md
  -> Designer reads it, maps failure modes to user flows
  -> Educator reads designer's spec, drafts help content
  -> Customer success reads educator's drafts, uses in outreach
  -> Analyst measures whether engagement moved
```

One-way flows eliminate circular waits. If Agent A needs Agent B's input to finish, and Agent B needs Agent A's output to start, neither can work. One-way flows mean agents can run in parallel because they read completed outputs, not in-progress thinking. **Practised (3 teams, 150+ sessions)** -- every team that adopted this pattern found it reduced coordination overhead compared to their previous approach. The causal mechanism (eliminating bidirectional dependency) is consistent with distributed systems principles, though we haven't isolated it from other factors.

## Explicit Contracts: Inputs and Outputs

Each agent's brief specifies what files it reads from other agents (with the reason) and what files it produces and who consumes them. These are explicit contracts. When an agent is created, its inputs and outputs are defined. This prevents both "nobody reads my work" and "I don't know where to find what I need." **Practised (3 teams, 150+ sessions)** -- all three teams converged on explicit brief-level contracts independently.

Example from a working system:

| Agent | Produces | Consumed By |
|-------|----------|-------------|
| SEO Analyst | keyword-opportunities.md | Content Strategist |
| Product Analyst | activation-analysis.md | Designer, Strategist |
| Designer | journey-map.md | Educator, Engineering Lead |

The brief is where contracts live. The Starting Intelligence section names exact file paths to read; the Role section names what the agent produces and for whom. See `brief-anatomy.md` for the full structure.

## Directory Structure as Architecture

Each agent owns its directory. No agent writes to another agent's directory. The directory structure reflects the information architecture -- if you can't tell what an agent does from its directory contents, the role isn't clear enough. **Practised (3 teams)** -- the directory-ownership rule was adopted in all three teams. Violations were caught in coaching reviews and corrected by tightening briefs.

```
agents/
  team-lead/        # Routing + sequencing (thin state)
  team-coach/       # Assessment outputs
  analyst/          # Research outputs
  strategist/       # Content plans + drafts
```

Directory ownership maps directly to domain ownership in role design (see `role-design.md`). One agent, one directory, one domain. The physical structure enforces the logical boundary.

## Observability

File-based coordination is inherently observable. Every piece of agent reasoning that matters is in a file. You can read any agent's current state (memory.md), trace how a decision was made by following the file chain, see what information an agent had when it acted, and audit whether agents are reading the right inputs. No logging framework needed -- the files are the log. **Practised (3 teams, 150+ sessions)** -- this observability was consistently cited as the primary advantage over message-passing alternatives. The team coach's entire assessment model depends on it: the coach reads briefs and journals (not memory) to evaluate team health from the outside.

## Worked Examples from This Repo

This repository's own agents are a working instance of file-based coordination (1 team, 18 sessions):

**Team Lead** (`agents/team-lead/brief.md`) produces journal entries in `journal/` and maintains `agents/team-lead/memory.md`. The brief specifies the team table (which agents exist), session protocol (how work flows), and journal protocol (what gets recorded). The team lead reads agent briefs and memory files to route work; agents read nothing from the team lead directly -- routing happens through dispatch, not through shared files.

**Team Coach** (`agents/team-coach/brief.md`) reads journal entries and all agent briefs, but deliberately does not read other agents' memory files. This is a file-contract constraint serving an architectural purpose: the coach evaluates from the outside to maintain genuinely different cognitive context. The coach's brief explicitly names this as a negative right, not just a boundary.

The directory structure (`agents/team-lead/`, `agents/team-coach/`, `methodology/`, `journal/`) is itself directory-as-architecture. Each directory has a clear owner and purpose. The `methodology/` directory is a shared output -- patterns written by specialist agents, curated by the team lead, read by anyone.

## Failure Modes

### Stale Reads

An agent reads a file that another agent has since updated in a different session. Memory pointers and reconciliation (see `session-transaction-protocol.md`) help but don't eliminate this. In practice, dirty closes cause memory to lag behind reality. When a downstream agent reads stale memory, it makes decisions based on outdated state. The reconciliation protocol catches this at session open, but between sessions there's no enforcement. **Practised (1 team, 18 sessions)** -- observed multiple times when sessions closed dirty and the next session's agent read stale pointers.

### Broken Contracts

An agent changes its output format without updating consumers. The brief says what the contract is, but there's no enforcement mechanism beyond coaching review. In one team, an agent's output structure drifted over several sessions; consumers adapted informally rather than flagging the mismatch. The coaching framework (see `coaching-framework.md`) is the detection mechanism, but it runs periodically, not continuously. **Practised (1 team)** -- observed once; the structural risk is clear but the sample is small.

### Race Conditions

Multiple agents writing to shared files or overlapping directories. The "one agent owns one directory" rule prevents this in theory, but cross-cutting concerns (shared reference material, methodology files edited by multiple specialists) create real risks. In practice, the team lead's routing prevents parallel writes by sequencing agent dispatch, but this is a coordination constraint, not an architectural guarantee. **Hypothesis** -- the risk is structural and well-understood from distributed systems, but we haven't observed a destructive race condition in our teams.

### Silent Divergence

The file an agent produces drifts from what its brief says it produces, and consumers adapt informally rather than flagging the mismatch. This is the file-coordination equivalent of role drift. The coaching review cycle catches it by comparing what briefs prescribe against what journals show, but between reviews the divergence is invisible. **Practised (1 team)** -- the team coach identified this pattern in a review.

## Anti-Patterns

### The Shared Scratchpad

Multiple agents writing to the same file. This destroys the one-way flow principle -- the file becomes a shared mutable state with no clear ownership. Conflicts aren't just possible; they're inevitable when sessions overlap or agents have different expectations about the file's contents. The fix: every file has exactly one writer. If two agents need to collaborate on a document, one writes and the other reads. **Practised (2 teams)** -- observed and corrected early in two team bootstraps.

### Implicit Contracts

Agents discover each other's outputs by exploration rather than explicit brief references. This works until an agent changes its output format, at which point every implicit consumer breaks silently. Explicit contracts in briefs (see `brief-anatomy.md`, Starting Intelligence section) are the fix -- they make dependencies visible and auditable. **Practised (3 teams)** -- every team that started without explicit contracts added them after experiencing breakage.

### Broadcast Files

A file written "for anyone who needs it" rather than for specific named consumers. These files tend to grow unbounded, satisfy nobody's specific needs, and eventually stop being read. Every output file should name its consumers in the producing agent's brief. If no consumer is named, the file probably shouldn't exist. **Hypothesis** -- reasoned from the explicit-contract principle and observed in shared/ directories, but not systematically tracked.

### Cross-Directory Writes

An agent writing to another agent's directory, violating ownership. This creates ambiguity about who maintains the file, who's responsible for its accuracy, and who should update it when circumstances change. The directory-ownership rule exists precisely to prevent this. When cross-directory writes are detected in coaching reviews, the fix is either moving the file to the writing agent's directory or reassigning responsibility. **Practised (1 team)** -- caught and corrected in one coaching review.

## Evidence Summary

The **one-way information flow** principle is Practised (3 teams, 150+ sessions). All three teams adopted it and found it reduced coordination overhead. The mechanism is consistent with distributed systems principles, but the causal claim hasn't been isolated from other factors that differ between teams.

**Explicit file contracts** are Practised (3 teams, 150+ sessions). Every team converged on brief-level contracts independently, which is suggestive but not controlled evidence. The claim that explicit contracts prevent breakage is based on observing what happened when contracts were implicit versus explicit -- not a deliberate experiment.

**Directory-as-architecture** is Practised (3 teams). The directory-ownership rule was adopted in all three teams. Violations occurred and were corrected, suggesting the rule needs active enforcement rather than being self-sustaining.

The **failure modes** (stale reads, broken contracts, silent divergence) are Practised (1 team, 18 sessions) -- observed in this repository's own team. Race conditions are Hypothesis -- the risk is structural but hasn't manifested destructively in our teams.

The **anti-patterns** draw from observed failures but the sample is small. The Shared Scratchpad and Implicit Contracts are the strongest (Practised, 2-3 teams). Broadcast Files is Hypothesis. Cross-Directory Writes is Practised (1 team). The claim that these are the most important anti-patterns is Hypothesis.

## Related Patterns

- `brief-anatomy.md` -- briefs are where file contracts are defined; the Starting Intelligence section names exact file paths to read and the Role section names what the agent produces and for whom
- `role-design.md` -- domain ownership maps to directory ownership; the inputs/outputs in role definitions are the file contracts that make coordination explicit
- `three-tier-memory.md` -- memory files are the most important coordination files; the three-tier model structures how they're written, pruned, and consumed across sessions
- `session-transaction-protocol.md` -- sessions are when files get written; the transaction model ensures files reach a consistent state even when sessions close dirty
- `self-modifying-briefs.md` -- when file contracts need to change, briefs must update too; self-modification is the mechanism that keeps contracts current as teams evolve
- `discipline-processes.md` -- human checkpoints in discipline processes are file-contract review points; phase transitions are where bad file state would waste all subsequent work
- `coaching-framework.md` -- the team coach's Information Architecture dimension directly evaluates file-contract health, output-to-action ratios, and cross-agent information flow
- `agent-team-guide.md` -- the practitioner's guide covers file-based coordination in context, including practical setup guidance
