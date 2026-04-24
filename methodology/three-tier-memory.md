# Three-Tier Memory

The default for AI agents is amnesia. Frameworks treat memory as a checkbox -- "add a vector database." This doesn't work. The problem isn't storage, it's attention management. An agent drowning in retrieved context performs worse than one with no memory at all. Three-tier memory solves this by matching information to urgency: what must be loaded every session, what can be found when needed, and what exists only for search.

**Evidence:** Validated for hot/cold distinction (3 teams, 60+ sessions); Practised for topic-based warm files (1 team, early evidence); Falsified for scratchpad-as-warm-tier (1 team, 8/9 agents never created one). This repo's own 2-agent team has maintained hot-tier memory for 20 sessions. Specific claims carry inline qualifiers below.

## The Tiers

**Hot (memory.md, <200 lines).** Loaded every session. Contains only what the agent can't function without -- current priorities, recent decisions, next actions, key numbers. Ruthlessly pruned. Every line competes for the agent's attention, so unnecessary content directly degrades performance (see `writing-for-ai.md`, "The Problem" section on instruction density). **Validated (3 teams, 60+ sessions)** -- every team that ran long enough converged on a small, always-loaded memory file. The 200-line limit is a specific operationalisation of this principle.

**Warm (topic files, journal entries).** Not loaded by default, but the agent knows where to find it. Structured research, analysis, reference data. Pulled when relevant. The original pattern prescribed a scratchpad as the primary warm-tier file -- a per-session workspace cleared at session open. This has been **Falsified (1 team, 150+ sessions)** -- 8 of 9 agents in one team never created a scratchpad despite it being in protocol. Topic-based warm files (organised by subject rather than session) are **Practised (1 team, early evidence)** and show more promise. In this repo, journal files serve the warm-tier function -- not loaded by default, but referenced when the agent needs session history. The team-lead scratchpad exists but has seen minimal use; the journal-first protocol (see `session-transaction-protocol.md`, "Journal-First as Write-Ahead Log") absorbed the workspace function.

**Cold (archive/).** Historical records compressed into monthly or topic-based files. Exists for search, not for regular consumption. An agent touches cold memory only when investigating something specific. **Hypothesis for this repo** -- no archive directory has been created after 20 sessions. The two-agent team hasn't needed cold storage, which may indicate that cold tier becomes necessary only at scale or over longer timeframes. The pattern is **Practised (1 team, 150+ sessions)** from source teams that did create and use archives.

## Why Not Embeddings

Vector search introduces a retrieval problem on top of the memory problem. The agent doesn't control what gets surfaced. Wrong context at the wrong time causes failures -- like the sales agent that gave a 50% discount because its retrieval pulled the wrong pricing information. Semantically similar but incorrect content is far more damaging than obviously irrelevant text (see `writing-for-ai.md`, "The Problem" section on semantic near-misses). **Practised (3 teams, 150+ sessions)** -- all source teams used plain files rather than embedding-based retrieval, and none reported retrieval-related failures. This is not a controlled comparison against embeddings; it's an observation that the plain-file approach was sufficient.

## The Consolidation Ritual

At session end, information accumulated during the session is triaged:
- **Promote to hot:** Will the next session need this? Update memory.md
- **Keep warm:** Is this enduring reference material? It lives in a topic file or journal entry
- **Archive to cold:** Is this historical record that's consuming hot-tier space? Compress into archive/
- **Discard:** The default. Most session work doesn't need to persist

After promotion, prune memory.md back under 200 lines. The pruning question is not just "will the next session need this?" but also: **"if this were missing, could a future session make a decision that contradicts it?"** (See "Known Risks" below.) The consolidation ritual is part of the session close protocol described in `session-transaction-protocol.md` (Clean Close Protocol, step 2). **Practised (2 agents, 20 sessions)** -- both agents in this repo update memory at session close. The team-lead memory includes a reconciliation pointer (`Last reconciled: journal/YYYY-MM-DD.md`) that lets the next session verify currency without reading the full journal archive.

## Worked Examples from This Repo

**Team-lead memory (20 sessions).** The team-lead's `memory.md` has been maintained across 20 sessions. It currently sits at ~90 lines -- well under the 200-line limit. It carries current state, goals, team composition, key decisions (with session numbers), the elevation roadmap, and a reconciliation pointer. Key decisions have been pruned over time: early editorial fixes are compressed into single lines, while recent phase transitions retain more detail. The file is read at every session open and updated at every session close.

**Team-coach memory (~80 lines).** The coach's memory carries review history, recommendation tracking with backward validation, and a watch list. It demonstrates a different hot-tier structure -- oriented around periodic reviews rather than continuous work. Both memory files serve the same architectural function (session-start context loading) with different internal organisation suited to different roles.

**Journal as warm tier.** The journal directory contains 20 entries across the project's history. These are not loaded at session start, but the team-lead references them when needed -- for example, to verify what happened in a specific session or to trace the history of a decision. The reconciliation pointer in hot memory creates a bridge: the pointer names the last-synced journal, and the presence of newer journal files signals a dirty close (see `session-transaction-protocol.md`, "Dirty Close Detection").

**No cold tier yet.** After 20 sessions, no `archive/` directory exists. Neither agent has needed to compress historical records. This is either evidence that cold storage is unnecessary for small teams over short timeframes, or evidence that the team hasn't yet accumulated enough history to need it. **Hypothesis** -- we cannot distinguish between these explanations at this scale.

## Known Risks

**Pruning away load-bearing decisions.** The most documented failure mode. During consolidation, a decision that shaped the project's architecture looks like historical context -- it happened in the past, the next session probably won't re-make it. So it gets pruned. Then a later session encounters the same design question, has no record of the prior decision or its rationale, makes a different choice, and introduces a bug. One source team hit exactly this while integrating Buttondown as a newsletter platform: the platform choice and the working integration had been pruned from hot memory, and a later session re-litigated the decision and rebuilt the backend from scratch before the mismatch was caught (see `agent-team-guide.md` for the fuller account). This risk connects directly to the load-bearing beliefs pattern (see `load-bearing-beliefs.md`, "Kill Conditions") -- decisions that encode architectural constraints are load-bearing beliefs that must survive pruning. **Practised (3 teams)** as an observed risk; the Buttondown-integration case is the most specific in-team example.

The mitigation: during pruning, ask **"if this were missing, could a future session make a decision that contradicts it?"** Decisions about what *not* to do, architectural constraints, and choices made after evaluating alternatives are almost always load-bearing. When in doubt, keep it. The cost of a few extra lines is lower than the cost of re-litigating a settled decision.

## Anti-Patterns

### Unbounded Hot Memory

A memory.md that grows without pruning. Each session adds findings, decisions, and context. The file passes 200 lines, then 500. The agent loads it all at session start, and performance degrades as instruction density overwhelms attention (see `writing-for-ai.md`, "The Problem" section). The 200-line limit is a discipline process (see `discipline-processes.md`, "Quality Rubrics") -- a hard constraint that forces the consolidation ritual to actually run. **Practised (3 teams, 60+ sessions)** -- observed as a failure mode before the limit was introduced; the limit emerged as a response to it.

### Premature Archiving

Moving information to cold storage before it's genuinely historical. The temptation is to keep hot memory lean by aggressively archiving. But if the archived information gets referenced within the next few sessions, it should have been warm, not cold. The practical test: has anyone retrieved this from cold storage? If cold storage is being searched regularly, the tier boundaries are wrong. **Hypothesis** -- reasoned from the tier structure but not observed as a failure in our teams.

### Retrieval-First Thinking

Designing the memory system around retrieval technology (embeddings, search indices) rather than around what the agent needs at session start. This inverts the problem: instead of deciding what's important and organising it by urgency, the system stores everything and relies on search to surface the right information at the right time. The plain-file approach forces intentional curation. **Practised (3 teams)** as a design choice; the negative case (retrieval-first systems causing problems) is external evidence, not directly observed in our teams.

### Cold Storage Avoidance

Never archiving anything, letting warm-tier files accumulate indefinitely. This is the mirror of premature archiving. Without periodic compression, the warm tier becomes an unstructured dump that's hard to navigate. **Hypothesis** -- reasoned from the tier model. This repo's own team has not created cold storage in 20 sessions, but it's unclear whether this is appropriate restraint or this anti-pattern in nascent form.

## Evidence Summary

The **hot/cold distinction** -- keeping a small, always-loaded memory file separate from archival storage -- is **Validated (3 teams, 60+ sessions)**. Every team that ran long enough converged on this structure independently.

The **200-line limit** on hot memory is **Practised (3 teams, 60+ sessions)**. It emerged as a response to observed unbounded-growth failures and has been maintained without difficulty across teams.

The **warm tier** is the least settled. Scratchpad-as-warm-tier is **Falsified (1 team, 8/9 agents never created one)**. Topic-based warm files are **Practised (1 team, early evidence)**. Journal-as-warm-tier is **Practised (1 team, 20 sessions)** in this repo but hasn't been deliberately tested.

The **consolidation ritual** is **Practised (2 agents, 20 sessions)** in this repo. Both agents update memory at session close. The pruning discipline has held -- neither memory file has exceeded the 200-line limit.

The **"Why Not Embeddings" position** is **Practised (3 teams)** as a design choice. No controlled comparison against embedding-based systems exists.

The **cold tier** is **Practised (1 team, 150+ sessions)** from source teams. This repo's team hasn't needed it, which is either appropriate or an untested gap.

## Related Patterns

- `writing-for-ai.md` -- instruction density and semantic near-misses explain *why* unbounded memory degrades performance; the 200-line limit is a direct application of the attention-budget principle (see "Application to Agent Team Documents")
- `session-transaction-protocol.md` -- the consolidation ritual is part of the clean close protocol (step 2: "Update memory with current state"); the reconciliation pointer enables dirty close detection (see "Detection signals")
- `discipline-processes.md` -- the 200-line limit is a discipline process; a hard constraint that makes the consolidation ritual non-optional (see "Quality Rubrics with Specific Criteria")
- `load-bearing-beliefs.md` -- the "pruning away load-bearing decisions" risk is the memory-tier version of losing beliefs that downstream decisions depend on (see "Kill Conditions: The Core Discipline")
- `learning-from-practice.md` -- contains the evidence ratings for three-tier memory claims (see "Current evidence levels"); the experiment log is itself a warm-tier file
- `self-modifying-briefs.md` -- brief modifications encode session-level learning into permanent instructions, complementing what memory captures; the cold-start problem described there is what hot-tier memory solves
- `brief-anatomy.md` -- the memory protocol section of agent briefs references three-tier memory directly (see "Session Protocols" section); brief structure determines what hot memory must carry
- `coaching-framework.md` -- the State Management dimension (dimension 2) evaluates whether memory practices are healthy; coaching reviews have confirmed this repo's memory is well under limits and serving its function
