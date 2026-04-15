# Self-Modifying Agent Briefs

Agents that can modify their own instructions get better over time. Agents that can't are limited to the understanding their designer had at session zero. This pattern covers what self-modification means in practice, what constraints make it safe, what goes wrong without those constraints, and what we've actually observed in a working system.

**Evidence:** Practised (2 agents, 19 sessions in this repo; 3 teams, 150+ sessions across source projects). Self-modification has been the primary mechanism for brief evolution in every team observed. The constraints (journaling, research-first, human review for irreversible changes) emerged independently across teams. Specific claims carry inline qualifiers below. The pattern has not been deliberately varied or compared against static-brief alternatives.

## What Self-Modification Means

An agent that discovers its brief is wrong -- missing a responsibility, over-scoped, or based on an assumption that proved false -- can fix it. It doesn't wait for a human to notice and reconfigure. The agent identifies the gap, makes the change, and records why.

This applies to:
- **Briefs** -- role definition, authority boundaries, negative rights
- **Session protocols** -- how work starts, progresses, and closes
- **Memory protocols** -- how information flows between tiers
- **Team composition** -- proposing new agents or retiring ones
- **Strategy documents** -- priorities, hypotheses, positioning

The scope is broad because every aspect of how an agent operates is a candidate for improvement. **Practised (3 teams, 150+ sessions)** -- all three source teams exercised self-modification across these categories. In this repo's 2-agent team, modifications have been concentrated in session protocols and brief refinements rather than team composition, which is consistent with a small, stable team.

## Why This Matters

Static configurations create a growing gap between what the brief says and what the agent should be doing. The human operator becomes the bottleneck for every adaptation -- every session where the agent knows its brief is wrong but can't fix it is a session running on degraded instructions.

Self-modification closes this loop: the agent operates under its brief, discovers where it falls short, and improves it. The next session starts with a better brief. This compounds -- each session's learning is encoded in the operating instructions for all future sessions. **Practised (2 agents, 19 sessions)** -- observed directly in this repo. The team lead's brief grew from a bootstrap template to a 110-line document reflecting 19 sessions of accumulated operational learning. **Hypothesis** for the compounding claim specifically: we observe that later sessions operate on better briefs, but we haven't isolated self-modification as the cause versus operator learning, methodology maturation, or general experience.

The cold-start problem makes this especially important for agent teams. Every session begins fresh -- the agent has no memory of previous sessions except what's written in files (see `three-tier-memory.md`). A human team member who discovers a process flaw might remember to work around it next time. An agent won't remember unless the brief is updated. Self-modification is the mechanism that turns session-level learning into permanent capability.

## The Constraints

Self-modification without discipline is chaos. Four constraints make it safe:

**1. Journal everything.** Every modification is recorded with what changed and why. This creates an audit trail and enables rollback through version control. The journal is the accountability mechanism -- without it, modifications are invisible and unjustifiable. See `session-transaction-protocol.md` for how journaling integrates with the session lifecycle. **Practised (2 agents, 19 sessions)** -- every self-modification in this repo has a corresponding journal entry.

**2. Research before changing.** Don't modify the brief based on a single session's frustration. The research-first principle from `CLAUDE.md` applies to self-modification too: what do other teams do? What has been tried? What failed? In practice, this constraint is the least-exercised -- modifications in this repo have been based on direct observation rather than external research, because the work profile hasn't required it. **Practised (3 teams) for the principle; Hypothesis for whether it prevents premature modifications** -- the constraint exists but its preventive value hasn't been isolated.

**3. Preserve core commitments.** Some things don't change: honesty, research-first thinking, self-assessment. These are the invariants that self-modification operates within. Everything else is fair game. The distinction between invariant and mutable is itself a design decision that belongs in the brief (see `brief-anatomy.md`, the Role section on what defines the agent's fundamental purpose). **Practised (2 agents, 19 sessions)** -- no core commitment has been modified in this repo's history. The team lead's "known bias" acknowledgment, added organically, demonstrates adding to the brief without changing its fundamental orientation.

**4. Human review for irreversible changes.** Adding a new agent, changing strategic direction, retiring a role -- these warrant human review. Tweaking a session protocol doesn't. The authority gradient from `role-design.md` applies: the agent acts autonomously on low-risk modifications and escalates high-risk ones. **Practised (3 teams, 150+ sessions)** -- the gradient between autonomous and escalated modifications has been consistent across all observed teams.

## Worked Examples from This Repo

This repository's own agents have modified their briefs multiple times across 19 sessions:

**Journal-first protocol (session 1).** The team lead modified its own session protocol, moving journal creation from step 5 to step 2. The trigger was operator feedback about unreliable end-of-session journaling. The modification was journaled, practised in the same session that proposed it, and assessed for methodology-pattern status (deferred -- too early). This later became the foundation for `session-transaction-protocol.md`. A brief addition that grew into a standalone pattern is a textbook case of the codification ladder (see `codification-ladder.md`, Tier 1 to Tier 3 promotion).

**Public safety sweep (session 11).** After a private project reference leaked in session 6, the team lead added a grep-based safety sweep to its session-close protocol. The journal entry noted: "This session exposed a gap between having a principle ('public repo awareness') and having a mechanism that enforces it." A vague principle became an operational check. The gap persisted for five sessions before the mechanism was added -- self-modification was reactive to observed failure, not preventive.

**Team-coach framework evolution (sessions 8-14).** The team-coach brief was substantially modified three times: adding a Processes evaluation criterion (session 8), restructuring into a five-dimension framework with maturity ladder and methodology self-consistency checks (session 9), and restructuring candidate listings to separate criteria-in-brief from assessments-in-memory (session 14). Each modification was proposed by the coach or team lead, journaled, and backward-validated in subsequent reviews.

**Known bias acknowledgment.** The team-lead brief acquired a "known bias" section identifying a structural tendency toward action over analysis. This wasn't part of the original seven-section template (see `brief-anatomy.md`) but emerged as a useful addition. Naming the bias helps the agent self-correct. **Practised (1 team)** -- observed in this project only.

**Candidate specialist listings (sessions 9-16).** The team-lead brief's listing of candidate agents was modified multiple times: initially populated at bootstrap, updated to reflect evidence from 9 sessions (session 9), restructured per coach recommendation to separate criteria from assessments (session 14), and updated again when the extraction backlog completed (session 16). Each update was journaled. The pattern illustrates how even metadata sections of a brief benefit from periodic revision as evidence accumulates.

Across these examples, a pattern emerges: modifications cluster around session protocols and evaluation frameworks, not role definitions or core authority. The fundamental "what you own" and "what you don't do" sections have been stable since bootstrap. The "how you work" sections have been heavily modified. This suggests that operational procedures are the primary target for self-modification, while role boundaries are more durable. **Practised (2 agents, 19 sessions)** -- observed in this repo. Whether this holds for larger teams or longer timeframes is unknown.

## The Modification Lifecycle

In practice, modifications follow a pattern: **trigger, assess, modify, journal, validate.** The trigger is a gap between what the brief says and what the agent needs -- surfaced through direct experience, coaching review, or operator feedback. Assessment applies the constraints above: is this a real pattern or a one-off? Does it change core commitments? The modification itself should be an edit, not an append -- replace or refine what's there rather than accumulating additions. The journal entry records both the change and its reasoning. Validation comes in subsequent sessions: did the modification actually help? The coaching framework's backward-validation mechanism (see `coaching-framework.md`, recommendation tracking) is the structural check, but informal validation happens naturally when the agent operates under the modified brief and finds it better or worse.

Not all modifications survive. A change that seemed right in session 8 might prove wrong by session 12. Version control makes rollback possible; the journal trail makes the rollback decision informed. The willingness to revert a self-modification is as important as the willingness to make one.

## Anti-Patterns

### The Frozen Brief

A brief that was written at bootstrap and never modified. If the brief from session 0 is unchanged at session 15, something is wrong -- either the agent hasn't learned anything about its role, or it has learned things but isn't encoding them. The coaching framework (see `coaching-framework.md`, dimension 1: specification quality) monitors for this. **Practised (2 agents, 19 sessions)** -- identified as a risk; the team coach watches for it in reviews.

### Modification Without Journaling

Changing the brief without recording what changed and why. This defeats the audit trail that makes self-modification safe. Without a journal entry, the next session operates on modified instructions without knowing they were modified or why. Version control provides a safety net (diffs are visible), but relying on git archaeology rather than explicit journaling is a degraded mode. **Hypothesis** -- reasoned from the constraint framework. We haven't observed this failure because the journaling discipline has been strong, but the risk is structural.

### Drift Through Accumulation

A brief that gets longer with every modification but never shorter. Each session adds a line, a caveat, a new responsibility. Over time, the brief becomes a sediment layer of every past session's concerns. This violates the instruction-density principle from `writing-for-ai.md`: every line competes for attention, and accuracy degrades as instructions accumulate. The fix is treating modifications as edits to an existing document, not appends. Remove what's superseded. **Practised (1 team, 150+ sessions)** -- observed in one source team where brief additions accumulated until coaching review identified the problem.

### Premature Generalization

Modifying the brief based on a single session's experience. One frustrating session doesn't justify a protocol change. The three-occurrence heuristic from the codification ladder (see `codification-ladder.md`, the two-part test) applies: wait for a pattern to recur before encoding it. The public safety sweep is an instructive edge case -- it was added after one leak, not three occurrences. But the severity of the failure (private data in a public repo) justified the exception. Severity can override recurrence as a modification trigger, but this should be the exception, not the norm. **Hypothesis** -- reasoned from the codification ladder's evidence requirements. The severity exception is observed (1 instance) but not tested as a general principle.

### Scope Creep Through Self-Modification

An agent that modifies its brief to absorb adjacent work rather than routing it to the appropriate agent or flagging a gap. Self-modification authority makes this tempting -- if the agent can change what it owns, it can expand to cover anything it encounters. The negative rights in the brief (see `role-design.md`, the negative-rights principle) are the check: they define what the agent doesn't do, and self-modification shouldn't erode those boundaries without the team lead's or coach's review. **Hypothesis** -- structural reasoning from the negative-rights pattern. Not observed in this repo's 2-agent team, but the risk increases with team size.

## Evidence Summary

The core pattern -- agents modifying their own instructions -- is **Practised (3 teams, 150+ sessions across source teams; 2 agents, 19 sessions in this repo)**. Every team that ran long enough modified agent briefs. The modification types observed include session protocol changes, boundary adjustments, evaluation framework evolution, and brief additions for newly discovered concerns.

The four constraints (journal, research-first, core commitments, human review) are **Practised (3 teams, 150+ sessions)** as a set. Individual constraints vary: journaling is the most consistently exercised; research-before-changing is the least exercised in this repo (the work profile hasn't triggered external research through 19 sessions).

The claim that self-modification produces compounding improvement is **Hypothesis**. We observe that briefs improve over time, but we haven't isolated self-modification as the cause versus operator learning, methodology maturation, or general experience.

The **modification lifecycle** (trigger, assess, modify, journal, validate) is a description of observed practice, not a tested protocol. **Practised (2 agents, 19 sessions)** -- every modification in this repo followed something like this sequence, but it was extracted after the fact, not followed prescriptively.

The **worked examples** are the strongest evidence in this pattern because they're specific and verifiable -- the journal entries, brief diffs, and coaching reviews are all in the repo's history. The patterns they suggest (operational procedures change more than role boundaries, severity can override recurrence as a trigger) are **Hypothesis** -- observed in one small team, not tested.

The anti-patterns are a mix. The Frozen Brief and Drift Through Accumulation are **Practised (1-2 teams)** -- observed in coaching reviews. Modification Without Journaling, Premature Generalization, and Scope Creep are **Hypothesis** -- reasoned from constraints and related patterns but not observed as failures in our teams.

## Related Patterns

- `brief-anatomy.md` -- the structure that self-modification operates on; the seven-section anatomy defines what can be modified and how sections relate to each other
- `role-design.md` -- the authority gradient that governs which modifications require escalation; negative rights are the boundaries self-modification must respect
- `codification-ladder.md` -- brief additions are Tier 1 codification; the two-part test (recurrence + cold-start value) applies to self-modification decisions; promotion from brief to playbook/protocol is the lifecycle path
- `session-transaction-protocol.md` -- journaling is the accountability mechanism for self-modification; the journal-first protocol itself originated as a self-modification (session 1)
- `coaching-framework.md` -- the team coach monitors specification quality (dimension 1), catching both frozen briefs and drift; the methodology self-consistency check ensures teams practice what their briefs prescribe
- `learning-from-practice.md` -- the evidence framework used throughout this pattern; self-modifications are practised-level evidence (used without deliberate variation)
- `discipline-processes.md` -- the public safety sweep example illustrates converting a principle into an operational check, which is what discipline encoding does at larger scale
- `writing-for-ai.md` -- instruction density constrains brief length, which makes every self-modification a tradeoff against existing content; the drift-through-accumulation anti-pattern is the failure mode when this constraint is ignored
