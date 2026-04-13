# Coaching Framework: Systems-Level Team Assessment

Composition coaching — adding, removing, or reshuffling agents — addresses only one dimension of team health. Teams can have the right agents and still fail because briefs have drifted from practice, memory is stale, processes are ad-hoc, information doesn't flow between agents, or the team can't evolve its own setup. A coaching framework that evaluates the full system, not just who's on the team, catches these problems before they compound.

**Evidence:** Practised (1 team, 150+ sessions). The five-dimension framework described here was extracted from a running agent team and used across multiple coaching reviews. It has not been replicated in independent teams.

## The Problem with Composition-Only Coaching

The natural first question about an agent team is "do we have the right agents?" It's a reasonable question, but it's one of at least five that matter. A team with well-designed roles can still produce poor results if:

- **Briefs have drifted** from what agents actually do. The brief says one thing; the journals show something different.
- **Memory is stale or bloated.** Agents carry outdated context or hit size limits that force important information out.
- **Recurring work is improvised every time.** The same multi-step task gets done differently each session, with inconsistent quality.
- **Agents can't find each other's output.** Information exists but isn't where the consuming agent looks for it, or it's in a format that doesn't support downstream use.
- **Nothing changes.** The team runs the same patterns session after session with no mechanism to evaluate whether they work.

Addressing any one of these through composition changes (add a new agent, split a role) treats symptoms rather than causes. The coaching framework below evaluates all five dimensions directly.

## Five Assessment Dimensions

Each dimension is independent — a team can be strong in one and weak in another. The dimensions are:

### 1. Specification Quality

Are agent briefs clear, bounded, and current?

- **Brief clarity.** Can a cold-start agent (one with no accumulated context) read the brief and know what to do? Vague briefs produce vague work.
- **Boundary definition.** Are negative rights explicit? (See `role-design.md` for why "what you don't do" matters more than "what you do.")
- **Drift detection.** Compare what briefs prescribe against what journals show agents actually doing. Drift isn't always bad — sometimes practice has outgrown the brief — but unacknowledged drift means the brief is misleading.

### 2. State Management

Is team memory serving its purpose?

- **Freshness.** Does hot-tier memory reflect the current state of the project, or does it carry decisions and context from weeks ago that no longer apply?
- **Decision-utility.** When an agent reads its memory at session start, does it get what it needs to make good decisions? Or is memory a changelog rather than a decision-support document?
- **Protocol compliance.** Are agents actually writing and reading memory according to the team's conventions? (See `three-tier-memory.md` for the architecture.) Non-compliance is common and is itself diagnostic — it may indicate the protocol is too burdensome.
- **Size discipline.** Hot-tier memory that exceeds its intended limits (typically under 200 lines) forces agents to skip or skim. Bloated memory is worse than sparse memory because it erodes trust in the file.

### 3. Process Maturity

Are recurring patterns codified appropriately?

- **Pattern recognition.** What work recurs across sessions? Session startup, research workflows, review procedures, handoff protocols — these are candidates for codification.
- **Codification level.** Is each recurring pattern at the right level of formality? (See the codification ladder below.) Some patterns belong in a brief; others warrant a standalone skill.
- **Lifecycle management.** Are codified processes reviewed and retired when they stop serving? A process inventory that only grows eventually becomes a process graveyard.

### 4. Information Architecture

Does information flow where it needs to go?

- **Cross-agent file contracts.** When Agent A produces output that Agent B consumes, is the format, location, and update frequency clear to both? Implicit contracts break silently.
- **Output-to-action ratio.** Are agents producing artifacts that nobody reads? High-effort outputs with no downstream consumer are waste.
- **Input freshness.** When an agent reads another agent's output, is it current? Stale inputs produce decisions based on outdated information.

### 5. Evolutionary Fitness

Can the team improve itself?

- **Experiment tracking.** Does the team make deliberate structural changes and record what happens? (See `learning-from-practice.md` for the experiment log pattern.)
- **Belief updates.** When evidence contradicts a team assumption, does anything change? Teams that accumulate evidence but never act on it have a learning system in name only.
- **Stale pattern retirement.** Are patterns that aren't working identified and removed? Keeping dead patterns in briefs or protocols adds noise and erodes the signal of the patterns that do work.

## Maturity Ladder

Each dimension can be assessed on a five-level maturity scale:

| Level | Label | Description |
|-------|-------|-------------|
| 0 | Ad hoc | Different every time. No recognisable pattern. |
| 1 | Documented | A pattern exists somewhere in writing. |
| 2 | Consistent | The pattern is followed reliably across sessions. |
| 3 | Measured | There is evidence about whether it works. |
| 4 | Refined | The pattern evolves based on that evidence. |

The ladder is descriptive, not prescriptive. Not every dimension needs to reach Level 4. A two-agent team in its first month might reasonably be at Level 0-1 across most dimensions, and that's fine — the ladder shows where you are, not where you must be.

**The over-codification warning.** Pushing every dimension to higher maturity levels is a trap. Process theatre — elaborate procedures that exist to demonstrate rigour rather than to improve outcomes — is worse than no process. The coaching question is not "how do we get to Level 4?" but "given this team's size, age, and work, what level is appropriate here?" A small team with simple coordination needs might be well-served by Level 1 specification quality and Level 2 state management. Forcing maturity where it isn't needed creates overhead without value.

## Backward Validation of Recommendations

A coaching framework that produces recommendations without tracking their outcomes optimises for plausibility rather than impact. It's easy to give advice that sounds good. It's harder to give advice that actually helps.

Every coaching recommendation should be tracked through a lifecycle:

1. **Proposed.** The recommendation, with an expected outcome stated at proposal time. The expected outcome must be observable — "should improve coordination" is not testable; "agents should reference each other's output files at least once per session" is.
2. **Implemented.** The team has made the change.
3. **Validated** or **Retired.** At the next review after implementation, assess: did the expected outcome materialise? If yes, validated. If no, retired — with a note about what was learned.

Two rules prevent recommendation drift:

- **Stalled proposals.** If a recommendation stays at "Proposed" for three or more reviews with no implementation, flag it. Either the recommendation isn't important enough to act on (in which case, retire it) or there's a blocker worth surfacing.
- **Missing outcomes.** If an implemented recommendation has no outcome assessment at the next review, the coaching process has a gap. Recommendations without follow-through are coaching theatre.

This backward-validation mechanism is what distinguishes coaching that compounds from coaching that sounds good once. Over time, the record of validated and retired recommendations becomes the most valuable coaching artifact — it shows what actually works for this specific team.

## Framework Self-Reflection

The coaching framework itself is a hypothesis, not a settled methodology. At each review, the coach evaluates the framework in a few lines:

- Are the five dimensions the right ones? Are any redundant? Is anything missing?
- Did this review surface useful findings, or was it going through the motions?
- Have any dimensions consistently failed to produce actionable insights? (That's a signal to revise or drop them.)

The framework should be versioned (v1, v2, etc.) and treated as a mutable experiment with its own review trigger — for example, after every three coaching reviews, assess whether the framework itself needs updating. A coaching framework that can't evolve is inconsistent with the evolutionary fitness it's supposed to evaluate.

## The Codification Ladder

*This section summarises the codification ladder. For the full treatment — promotion heuristics, anti-patterns, lifecycle management — see `codification-ladder.md`.*

Coaching reviews surface recurring patterns. Not all of them should be formalised. A two-part test determines whether a pattern is worth codifying:

1. **Recurrence.** Has it happened three or more times?
2. **Cold-start value.** Would an agent with no accumulated context benefit from having it written down?

Both conditions must be met. A pattern that recurs but is obvious to any agent doesn't need codification. A pattern that would help a cold-start agent but has only happened once isn't established enough to codify — it might be a one-off.

When both conditions are met, the next question is what form the codification should take. Four levels, from lightest to heaviest:

| Level | Scope | Persistence | Example |
|-------|-------|-------------|---------|
| **Brief addition** | Single agent | Permanent | "At session start, always check the backlog file" |
| **Playbook** | Single agent | On-demand | A multi-step research procedure invoked when needed |
| **Protocol** | Team-wide | Permanent | "All agents update memory before session close" |
| **Skill** | Any agent | Loadable | A stateless, structured process any agent can invoke (see `discipline-processes.md`) |

The principle: codify at the lightest level that works. A brief addition is cheaper than a protocol. A protocol is cheaper than a skill. Start light and promote to heavier forms only when the lighter form proves insufficient. Over-engineering codification creates maintenance burden and the process theatre described above.

## Adapting to Team Size

The framework scales down. A two-agent team doesn't need formal information architecture assessment — there's only one information flow to evaluate. A team in its first ten sessions won't have enough history for meaningful evolutionary fitness assessment. The dimensions still apply conceptually, but the depth and formality of assessment should match the team's complexity.

Rules of thumb:

- **Small teams (2-3 agents).** Focus on specification quality and state management. These matter at any scale. Process maturity and information architecture can be assessed informally.
- **Young teams (under 20 sessions).** Evolutionary fitness assessment is premature — there hasn't been enough time to run experiments. Focus on getting the basics right: clear briefs, working memory, emerging patterns.
- **Larger teams (5+ agents).** Information architecture becomes critical. As agent count grows, the number of potential information flows grows combinatorially. Implicit file contracts that worked with three agents break with seven.

## What's Not Yet Known

This framework was extracted from a single team's practice. Several questions remain open:

- **Dimension completeness.** Are five dimensions the right number? There may be dimensions this team didn't need that other teams would — for example, coordination overhead in teams with more complex handoff patterns, or quality assurance in teams producing customer-facing output.
- **Assessment frequency.** The source team ran coaching reviews periodically, but the optimal cadence is unknown. Too frequent and reviews become rote; too infrequent and problems compound.
- **Maturity targets.** The warning against over-codification is based on observation, but there's no systematic evidence about which maturity levels are appropriate for which team configurations.
- **Cross-team coaching.** The framework assesses one team at a time. In multi-team environments, inter-team dynamics (shared infrastructure, competing priorities, divergent conventions) may warrant additional dimensions.

## Evidence Summary

The five-dimension framework and backward-validation mechanism are **Practised (1 team, 150+ sessions)** — used consistently in a running team across multiple coaching reviews. The maturity ladder and codification ladder are structural proposals extracted from that practice, not independently validated. The adaptation guidelines for different team sizes are **Hypothesis** — reasoned from the framework but not yet tested across teams of varying scale.

The framework aligns with general systems-thinking principles (evaluating a system on multiple dimensions rather than optimising one variable), but alignment with principles is not evidence. The specific claims — that these five dimensions are sufficient, that backward validation prevents coaching theatre, that the codification two-part test avoids empty processes — are hypotheses supported by limited practice.

## Related Patterns

- `role-design.md` — domain ownership and authority boundaries (dimension 1: specification quality)
- `three-tier-memory.md` — memory architecture (dimension 2: state management)
- `discipline-processes.md` — encoding processes as skills (dimension 3: process maturity)
- `codification-ladder.md` — when to formalise recurring patterns and at what level (dimension 3: process maturity)
- `file-based-coordination.md` — information flow through files (dimension 4: information architecture)
- `learning-from-practice.md` — experiment tracking and confidence levels (dimension 5: evolutionary fitness, and the evidence framework used here)
- `brief-anatomy.md` — how to write effective briefs (relevant to specification quality assessment)
