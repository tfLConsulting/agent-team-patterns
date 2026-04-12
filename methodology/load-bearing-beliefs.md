# Load-Bearing Beliefs: Strategy as Testable Hypotheses

Every project rests on assumptions. Most leave them implicit — buried in strategy documents, encoded in architecture choices, or never articulated at all. Load-bearing beliefs are the assumptions that, if wrong, would invalidate significant downstream work. Making them explicit, with pre-defined conditions for abandonment, is the difference between a team that pivots when evidence demands it and one that rationalises its way past warning signs.

The pattern is simple: identify the beliefs your project depends on, state them clearly, define what would falsify each one, and track evidence over time. The discipline is harder than the structure.

## What Makes a Belief Load-Bearing

Not every assumption matters equally. A load-bearing belief is one where other decisions depend on it — downstream work, resource allocation, architectural choices. If the belief turns out to be wrong, those dependent decisions are also wrong.

Examples of load-bearing beliefs from agent team practice:

- "File-based coordination is sufficient for teams under 10 agents." If false, most of the coordination architecture needs rethinking.
- "Agents can reliably self-modify their own briefs without drift toward incoherence." If false, the self-modification pattern needs human review gates.
- "Session journals produce enough micro-observations to feed the learning system." If false, a different observation mechanism is needed.

The test: ask "what would we do differently if this were wrong?" If the answer is "a lot," the belief is load-bearing. If the answer is "not much," it's a regular assumption — still worth tracking, but not with the same urgency.

## Identifying Hidden Beliefs

The most dangerous load-bearing beliefs are the ones nobody thinks to question because they feel obvious. They hide in several places:

**Architecture choices.** Every structural decision encodes a belief. Choosing file-based coordination over a message bus encodes a belief about latency requirements. Choosing hot-tier memory under 200 lines encodes a belief about how much context agents need at session start.

**Methodology patterns.** Patterns that have been practised long enough start feeling like facts. "Three-tier memory works" is a belief, not a law. It worked in the contexts observed so far. That's different from always working.

**Unstated prerequisites.** "We'll add a QA agent when the team grows" assumes the team will grow, that QA is best handled by a dedicated agent rather than a process, and that current quality is acceptable without one. Three beliefs hiding behind one plan.

A useful exercise during strategy sessions: for each major decision, ask "what would have to be true for this to be the right call?" Each answer is a candidate load-bearing belief.

## Structure of a Belief Entry

A belief entry needs enough structure to be actionable without becoming bureaucratic overhead. Five fields:

**Belief statement.** One sentence, concrete enough to be falsifiable. "Our approach works" is too vague. "File-based coordination handles inter-agent dependencies without blocking for teams of 5-9 agents" is testable.

**Why it's load-bearing.** What depends on this belief? Which decisions, investments, or architectural choices would need revisiting if it's wrong? This field forces you to trace the dependency chain.

**Kill conditions.** Specific, observable criteria that would falsify the belief. These must be concrete enough that two reasonable people would agree on whether the condition has been met. "If it doesn't work out" is not a kill condition. "If more than 30% of cross-agent handoffs require manual intervention over a 20-session window" is.

**Current evidence status.** What do you actually know? Use the confidence vocabulary from `learning-from-practice.md` — Hypothesis, Practised, Tested, Validated, or Falsified — with evidence qualifiers. Update this as evidence accumulates.

**Last reviewed.** When was this belief last actively examined? Beliefs that haven't been reviewed in months are effectively untracked.

## Kill Conditions: The Core Discipline

Kill conditions are what distinguish load-bearing beliefs from wishful thinking. They answer: "What would I need to see to change my mind?"

Good kill conditions share three properties:

**Observable.** Based on things you can actually see or measure, not internal states or subjective assessments. "If agents seem confused" is subjective. "If agents produce output that contradicts their brief's stated boundaries in more than 2 of 10 sessions" is observable.

**Bounded.** They specify a timeframe or sample size. Without bounds, a kill condition can always be deferred — "we haven't seen enough yet" becomes a permanent excuse. "Over the next 15 sessions" or "after the third coaching review" creates a deadline for judgment.

**Pre-committed.** Written down before you need them, not invented in the moment. This is the psychological core of the pattern. In the moment when evidence is mounting against a belief, the sunk cost is real and the temptation to rationalise is strong. A kill condition written in advance, when you had no stake in the outcome, is harder to explain away.

## The Measurement Trap

Sometimes a kill condition fires but the problem is the measurement, not the belief. An agent team tracking "percentage of sessions with useful output" might see a drop — but the drop could reflect a change in what counts as "useful" rather than a decline in actual quality.

The discipline is checking both: when a kill condition triggers, ask two questions in sequence. First: is the measurement reliable? If the data is noisy, the criteria ambiguous, or the sample too small, the kill condition may have fired prematurely. Second: if the measurement is sound, what does it mean for the belief?

This two-step check prevents both failure modes — abandoning a sound belief based on bad data, and clinging to a broken belief by blaming the measurement. The order matters: check the measurement first, honestly, and only then evaluate the belief.

## Belief Lifecycle

Beliefs move through stages:

**Surfaced.** Someone has identified and articulated the belief with its kill conditions. This is the starting state.

**Active.** The belief is being tracked, with evidence accumulating. Most beliefs spend most of their life here.

**Under challenge.** Evidence is accumulating against the belief, or a kill condition is close to firing. This is the stage where an investigation thread (see `investigation-threads.md`) might be warranted — a focused inquiry into whether the belief should be revised or abandoned.

**Validated.** Enough evidence has accumulated in favour of the belief, across enough contexts, that confidence is high. Validated beliefs still carry kill conditions — they're just less likely to fire.

**Killed.** A kill condition has fired and the measurement has been verified. The belief is recorded as falsified, with the evidence and context, and dependent decisions are reviewed.

**Revised.** The original belief was partially right but needed refinement. Often more useful than a binary kill — "file-based coordination works for teams under 10 agents" might become "file-based coordination works for teams under 10 agents when handoff frequency is below X per session."

Killed and revised beliefs are among the most valuable entries in the log. They represent actual learning, not just tracking.

## Anti-Patterns

**Beliefs without kill conditions.** If you can't state what would change your mind, you don't have a testable belief — you have a conviction. Convictions have their place, but they shouldn't masquerade as strategy.

**Unfalsifiable kill conditions.** "If it completely fails" is a kill condition that never fires because there's always a way to argue partial success. Kill conditions must be specific enough to actually trigger.

**Kill condition theatre.** Defining kill conditions to demonstrate rigour, then ignoring them when they fire. This is worse than having no kill conditions because it creates the illusion of discipline while practising none.

**Static belief lists.** A list of beliefs written once and never revisited is a historical document, not a strategic tool. Beliefs need active tracking — evidence updates, periodic review, and honest reassessment.

**Premature killing.** Abandoning a belief at the first negative signal without checking the measurement or allowing enough time for the approach to mature. Some patterns need time to take effect. The experiment log pattern in `learning-from-practice.md` notes this failure mode explicitly.

## Connecting Beliefs to Investigation Threads

When a belief enters the "under challenge" state, the natural response is an investigation thread — a bounded inquiry to gather evidence and reach a verdict. The belief provides the question; the investigation thread provides the structure for answering it.

This connection runs both ways. Investigation threads sometimes surface new load-bearing beliefs that weren't previously articulated. An investigation into "why are cross-agent handoffs failing?" might reveal a hidden belief about file naming conventions that nobody had thought to question.

## Evidence Summary

This pattern is **Practised (1 team, multiple validations)**. Load-bearing beliefs have been explicitly surfaced and tracked in a running agent team. Kill conditions have been defined and have fired in at least some cases, leading to actual belief revision. The structure described here was extracted from that practice.

The psychological claim — that pre-committed kill conditions reduce rationalisation bias — is supported by general decision science research on pre-commitment but has not been measured directly in agent team contexts. The measurement trap (checking both the measurement and the belief) emerged from observed practice where premature judgment was a recurring failure mode.

No controlled comparison exists between teams using explicit load-bearing beliefs and teams leaving assumptions implicit. The claimed benefits — strategic clarity, honest reassessment, faster pivots — are observed but not isolated from other factors.

## Related Patterns

- `investigation-threads.md` — the structure for bounded inquiry when a belief is under challenge
- `learning-from-practice.md` — confidence levels, experiment tracking, and the evidence framework that load-bearing beliefs feed into
- `coaching-framework.md` — the evolutionary fitness dimension directly evaluates whether teams update beliefs based on evidence
- `self-modifying-briefs.md` — brief modifications are often downstream of belief updates; a killed belief can trigger brief revision
