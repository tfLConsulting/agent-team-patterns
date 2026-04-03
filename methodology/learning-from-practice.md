# Learning from Practice

Every pattern in this methodology directory is a hypothesis with varying levels of evidence. The methodology README already flags the narrow evidence base (N=3 projects, same operator, same LLM), but that overall hedge doesn't tell you which specific claims have strong backing and which are borrowed intuitions. What's been missing is per-claim granularity — a way to say "this specific mechanism has 60 sessions of evidence" versus "this sounded right when we wrote it down."

This file describes a protocol for closing that gap. It connects the pieces we already have — session journals, learnings files, methodology files — into a single learning system, and adds the missing pieces: confidence levels for methodology claims, an experiment log for deliberate variation, and criteria for when to explore versus exploit.

This protocol is itself at the **hypothesis** level. We haven't yet run it as a system.

## How the Pieces Connect

We already have the infrastructure. The missing part was showing how it flows together:

1. **Micro-observations** (in session journals) are the lightweight input. Captured during normal work as part of the journal entry agents already write. One to three sentences answering: *What about our team's setup helped or hindered this session's work?*

2. **Learnings files** (`learnings/`) are where patterns emerge. When micro-observations accumulate around a theme — three sessions noting the same friction, or independent teams converging on the same workaround — that's a learnings file. Learnings carry their own status: `observation` (seen once), `corroborated` (seen multiple times), `incorporated` (led to a change).

3. **The experiment log** is the deliberate-variation arm. Structural changes to memory architecture, role design, coordination patterns, or session protocols, tracked with outcomes. Details below.

4. **Confidence levels** are how we rate methodology claims, informed by learnings and experiments. Details below.

The flow: micro-observations feed learnings files when a pattern emerges. Learnings plus experiment results inform methodology updates when evidence warrants. Methodology patterns carry explicit confidence levels that reflect the actual evidence behind them.

Note: the learnings vocabulary (`observation / corroborated / incorporated`) and the confidence vocabulary below (`Hypothesis / Practised / Tested / Validated / Falsified`) serve different purposes. Learnings statuses track the lifecycle of an empirical observation. Confidence levels rate methodology claims — prescriptive patterns, not raw observations. A corroborated learning might feed a Hypothesis-level methodology claim if we haven't yet applied it as a pattern, or a Practised one if we have.

## Confidence Levels

Every methodology claim carries an evidence level:

**Hypothesis** — Untested, or borrowed from another context we haven't run ourselves. Most new patterns start here.

**Practised** — We've used this pattern in at least one running team, without deliberate variation. Long use tells you the pattern doesn't catastrophically fail; it doesn't tell you whether something else would work better. Because "Practised" covers a wide range — from a single journal observation to hundreds of sessions across multiple teams — claims at this level carry an evidence qualifier: the number of teams and approximate session count. For example: "Practised (1 team, 4 sessions)" versus "Practised (3 teams, 141 sessions)." The qualifier travels with the rating wherever it appears. A bare "Practised" without a qualifier should be treated as the weakest version.

**Tested** — We've deliberately varied this pattern or compared it across teams or contexts, with recorded outcomes. The variation was intentional, not accidental.

**Validated** — Consistent evidence across multiple teams, multiple contexts, many sessions. The pattern holds up under different conditions. This is the highest confidence we claim — it still isn't "proven."

**Falsified** — We tried it and it didn't work. The specifics of what failed and why are more valuable than the label. A pattern falsified in one context might work in another, so we record the conditions.

**External evidence.** Some claims are supported by published research we haven't replicated ourselves. These don't get their own confidence level — they're still Hypothesis from our perspective — but they carry a qualifier indicating the external support: "Hypothesis (supported by: [citation])." This distinguishes "we made this up based on reasoning" from "someone else tested this and we're applying it by analogy." External evidence lowers the risk of a hypothesis but doesn't substitute for running it in our context. When we do run it and observe results, it graduates to Practised like anything else.

Current evidence levels for existing patterns (as of early 2026):

- **Three-tier memory:** The hot/cold distinction is **validated** (60+ sessions across 3 teams). The warm tier scratchpad is **falsified** in at least one team composition — 8 of 9 agents in one team never created one. Topic-based warm files are **practised** (early evidence from a second team).
- **Self-modifying briefs:** **Practised** (3 teams, 141 sessions). Not yet deliberately varied or compared across contexts.
- **Strategic backlog with hypothesis/verdict lifecycle:** **Practised** — described as "the best-organized part of the system" after 60+ sessions of use in one team.
- **Wiki system:** **Falsified** for rapidly-evolving teams — zero pages created in 75 sessions despite being in protocol.

These assessments will change. That's the point.

## Why Micro-Observations Work Where the Wiki Didn't

The wiki was in protocol and produced zero pages. Micro-observations are also "in protocol." The difference is structural: micro-observations are embedded in the journal entry agents already write at session close — an existing step in an existing workflow. The wiki required creating a new artifact, in a new location, for a new audience. That's three barriers. Embedding an observation prompt in an already-required step removes all three.

We've observed that without an explicit prompt, structural observations don't happen. In one team, 23% of sessions had no memory writes at all before the session protocol was hardened to require them. The hypothesis: embedding the observation prompt in the session-close checklist will produce consistent data. We don't yet have enough post-change sessions to confirm this.

## The Experiment Log

Generalised from a pattern that emerged organically in one team's memory experiments file. Each team maintains a log of deliberate structural choices — changes to memory architecture, role design, coordination patterns, session protocols, or anything else that shapes how the team operates.

Each entry records:

- **What:** The structural change, described concretely
- **Status:** Active / tried-and-retired / considered-but-not-tried
- **Rationale:** Why this was tried (or why it was rejected without trying)
- **Observed impact:** Filled in AFTER running, never predicted in advance. Behavioural psychology suggests that predictions anchor perception — recording what actually happened, without a prior prediction to confirm or deny, reduces this risk. We haven't tested this claim ourselves.
- **Kill condition or review trigger:** When do we revisit? A specific session count, a date, or a condition ("if we see X three more times").

The experiment log is a warm-tier file — not loaded every session, but the team lead knows it exists and references it when making structural decisions.

## Deliberate Variation

Most sessions should exploit current patterns — do real work with the setup we have. Exploration happens at the margins: small changes to one structural element while everything else stays stable.

### When to Explore

These are heuristics, not rules:

- **Accumulated friction.** Micro-observations surface 3+ complaints about the same structural element across sessions.
- **Coach-identified problems.** A team-coach review identifies a structural issue.
- **Absence of signal.** A pattern has been in use 20+ sessions with no evidence it's helping. Absence of signal is itself signal.
- **Bootstrapping period.** A new team's first ~10 sessions are a natural exploration period — everything is being tried for the first time.

### How to Explore

1. **Change one thing.** Changing multiple things simultaneously makes it impossible to attribute outcomes.
2. **State what's changing and what you'll watch for.** Not a prediction — an observation target. "We're switching from timestamp-ordered warm files to topic-based ones. We'll watch for whether agents actually reference them."
3. **Run for enough sessions before judging.** Some changes need time to take effect. One team's journal system was introduced at session 76 — after 13 sessions, it was too early to evaluate. Early discomfort is not evidence of failure; premature judgment is a recurring failure mode in our own practice.
4. **Record the outcome in the experiment log.** What happened, not whether we were right.

## Cross-Team Harvesting

For projects with methodology used by multiple teams, there's a periodic harvesting step:

1. Read experiment logs and journal observations from live teams
2. Look for convergence: what are multiple teams independently arriving at?
3. Look for divergence: where do teams disagree or take opposite approaches?
4. Update methodology files with evidence, not just assertions — cite the team, the session count, and what was observed
5. Flag when methodology contradicts what teams are actually doing — divergence is a signal worth investigating. It may indicate the methodology is wrong, or it may indicate an adoption problem. Either way, it needs attention.

The current evidence base draws from 3 teams across multiple repos (141 total sessions as of early 2026). As more teams run and accumulate sessions, the harvesting step becomes both more valuable and more feasible.

## What This Adds

The existing methodology files and learnings files already do most of the work. What was missing:

- **Per-claim confidence levels.** The methodology README hedges the whole collection, but individual claims vary widely in evidence. Confidence levels make this granular.
- **A feedback loop from practice to methodology.** Learnings files capture observations; the experiment log captures deliberate structural changes. Together they feed methodology updates. Before this, learning happened but stayed in individual team journals and memory files.
- **A mechanism for recording failure.** Falsified patterns are as valuable as validated ones — arguably more so. The wiki failure is a concrete example.
- **Criteria for deliberate variation.** Changes previously happened reactively. This protocol adds heuristics for when to explore and a structure for tracking what happens.

## Honest Acknowledgement

This protocol is at the **hypothesis** level. The evidence cited here predates the protocol — it was collected informally, not through the structured process described above.

The test is whether the system produces outputs: experiment logs with observed-impact data filled in, micro-observations accumulating in journals and finding their way into learnings files, and methodology patterns with confidence levels that shift based on evidence. If those outputs aren't appearing, this protocol has failed and should be revised or retired.

All confidence ratings in this system are self-assessed — the same teams whose claims are being rated are the ones assigning the ratings. There is no external auditor. This creates a structural bias toward overconfidence: assessors know the reasoning behind each claim and are predisposed to find it sound. We can't eliminate this, but naming it helps. Treat all ratings as optimistic by at least one notch.
