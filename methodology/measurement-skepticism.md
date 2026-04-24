# Measurement Skepticism

Agent teams generate numbers. Session counts, compliance rates, output quality assessments, completion percentages, coaching maturity scores. These numbers feel solid — they're in files, they have dates, they get referenced in decisions. But agent team metrics are structurally unreliable in ways that traditional software metrics are not, and the default assumption should be skepticism: the measurement is wrong more often than the thing being measured is broken.

This isn't nihilism about measurement. It's a prior — a starting position that protects against the most common failure mode in metric-driven agent teams: acting on bad data with high confidence. The discipline is checking the measurement before interpreting the result, every time, not just when something looks suspicious.

## Why Agent Team Metrics Are Structurally Fragile

Traditional software metrics benefit from stable definitions, large sample sizes, and automated collection. Agent team metrics have none of these.

**Small samples.** A team with 50 sessions has 50 data points. A "30% failure rate" based on 10 observations is three failures — one of which might be a dirty close that didn't record its outcome, another a session where the criteria changed mid-run. Statistical instability isn't a risk to manage; it's the default condition.

**Evolving definitions.** Agent teams change their own briefs, processes, and evaluation criteria over time — that's the point of self-modification (see `self-modifying-briefs.md`). But a metric like "percentage of sessions with useful output" means something different after the team has refined what "useful" means three times. The metric name stays the same while the measurement changes underneath it. Comparing session 20's "useful output rate" to session 80's is comparing two different measurements with the same label.

**Self-assessment.** Most agent team metrics are self-reported. The team that produces the work also evaluates it. `learning-from-practice.md` already flags this: "Treat all ratings as optimistic by at least one notch." The structural bias toward overconfidence applies to every metric the team generates about itself. There is no external auditor, no independent measurement, no blind evaluation. Self-assessed metrics are evidence, but they're evidence with a known directional bias.

**Survivorship bias.** Sessions that close cleanly produce complete records. Sessions that dirty-close (see `session-transaction-protocol.md`) produce partial or no records. If your metrics are drawn from journal entries and memory updates, they systematically over-represent successful sessions and under-represent failures. The sessions most likely to reveal problems are the ones least likely to produce data about those problems.

**Proxy gap.** What agent teams can measure — file updates, protocol compliance, word counts, session duration — is rarely what they care about. Decision quality, strategic coherence, compounding learning — these are the outcomes that matter, but they resist direct measurement. Every metric in an agent team is a proxy, and the gap between proxy and target is where measurement skepticism earns its keep.

## The Default Prior

The operational stance: when a metric says something unexpected — good or bad — the first hypothesis is that the measurement is wrong. Not the only hypothesis, but the first one checked.

This inverts the natural instinct. The natural instinct when a metric drops is to ask "what went wrong with the team?" The measurement-skeptic instinct is to ask "what went wrong with the metric?" Both questions eventually get asked, but the order matters because the first question anchors the investigation.

The prior is justified by base rates. In a system where definitions drift, samples are small, collection is manual, and assessment is self-reported, measurement error is more common than genuine signal. This doesn't mean genuine signals don't exist — it means they need to survive scrutiny of the measurement before being acted on.

The Measurement Trap section in `load-bearing-beliefs.md` applies this prior to one specific context: when a kill condition fires. Measurement skepticism generalises the principle to all metric-driven decisions, not just belief evaluation.

## Practices

### Metric Auditing

Periodically review the metrics the team relies on. For each metric, ask:

**Is the definition stable?** Has what this metric measures changed since it was established? If the team's briefs, processes, or evaluation criteria have evolved, metrics defined under the old regime may no longer measure what they claim to.

**Is the sample adequate?** How many observations underlie this number? For agent teams in their first 50 sessions, most per-session metrics lack the sample size to support confident conclusions. State the N alongside the metric. A bare percentage without a denominator is a number pretending to be a finding.

**Is collection consistent?** Are sessions contributing data uniformly, or do some sessions produce data and others don't? If data collection depends on the clean-close protocol, check whether dirty closes are skewing the sample.

**Is the proxy close to the target?** What do you actually want to know, and how far is this metric from that? "Number of memory updates per session" is easy to count but doesn't tell you whether memory quality is good. "Percentage of sessions where the agent referenced another agent's output" measures a behaviour, not whether the reference was useful. Name the gap between proxy and target explicitly — it calibrates how much weight the metric deserves.

Metric auditing doesn't need to be a formal process. A few lines in a coaching review (see `coaching-framework.md`) asking "are we still measuring what we think we're measuring?" is sufficient. The point is that auditing happens at all, not that it follows a rigid procedure.

### State the N

Every quantitative claim about an agent team should carry its sample size. Not buried in a footnote — alongside the claim.

"Compliance improved from 60% to 90%" invites action. "Compliance improved from 3/5 to 9/10" invites appropriate caution. The same information, but the second version makes the fragility visible. This is a writing discipline, not a statistical technique. It costs nothing and prevents the most common form of over-interpretation.

The confidence levels in `learning-from-practice.md` already do a version of this with evidence qualifiers: "Practised (1 team, 4 sessions)" versus "Practised (3 teams, 141 sessions)." Measurement skepticism extends the same discipline to all metrics, not just methodology confidence ratings.

### Pre-Mortem on New Metrics

Before adopting a new metric, ask: how could this metric mislead us? What would make it go up (or down) for reasons unrelated to what we care about?

A team considering "average session length" as a productivity proxy should ask: what makes sessions longer? Genuine complexity, scope creep, context window waste, dirty closes that extend runtime, and simply having more to do are all different causes with the same metric signature. If the team can't distinguish between these causes from the metric alone, the metric will eventually mislead.

This isn't a reason not to measure. It's a reason to understand what the metric can and cannot tell you before you start relying on it.

### Ruler-Change Tagging

When a metric's definition shifts while its name stays the same, tag the change explicitly rather than treating it as a normal data point. A dedicated log entry records: what the metric measured before, what it measures now, whether the historical baseline is preserved or reset, and the count delta introduced by the definition change alone.

The point isn't to avoid changing definitions — in a self-modifying team, definitions must be allowed to evolve. It's to prevent the before/after comparison from being contaminated by the shift itself. If "useful output" was redefined between sessions 30 and 31 to be stricter, and the next reported rate is lower, the drop might be entirely explained by the redefinition. Without an explicit ruler-change tag, that explanation gets lost within a few sessions, and the redefinition looks like regression.

Distinguish ruler-changes from corrections (fixing a miscount under the same ruler) and reframes (changing what the metric is used for). All three are legitimate; conflating them erases longitudinal integrity. A one-line convention in the journal or metric log — `ruler-change: X → Y, baseline preserved, count delta = -2` — is enough to make the category visible. The discipline is recognising which of the three happened, not the specific tag syntax.

### Briefing-Provenance Checks

Before a number from prior-session memory is used to justify a new directive, re-measure it against source data. Memory entries drift: an initial observation becomes a summarised claim, then a cited fact, then an input to the next plan — with each step obscuring whether the original measurement still holds under current definitions.

The protocol is simple. When any agent is about to act on a count or rate pulled from `memory.md` or a prior journal entry, treat that number as a claim requiring verification rather than a fact. Re-count from the source — journal entries, methodology files, whatever the metric was originally drawn from. If the number has changed, update memory and note the drift; if it hasn't, proceed.

This guards against a specific failure mode — memory-as-truth drift — that the three-tier model (`three-tier-memory.md`) is vulnerable to by design. Memory exists so the next session doesn't re-read everything; briefing-provenance ensures that labour-saving doesn't compound into decision-making on stale numbers. The rule only needs to fire when a remembered number is about to drive action — not every memory read, which would defeat the point of memory.

## Anti-Patterns

**Metric fixation.** Treating a number as the reality it's meant to represent. "Our compliance rate is 85%" becomes "we're 85% compliant" — but the compliance rate might be measuring whether a file was updated, not whether the update was meaningful. The map is not the territory, and agent team metrics are particularly rough maps.

**Anchoring on historical comparisons.** Comparing metrics across time periods when the team, its processes, and its measurement definitions have all changed. Session 1-20 metrics and session 80-100 metrics come from what is effectively a different team. Trends across these periods are noise unless you can demonstrate that the measurement held constant while only the thing being measured changed — which in a self-modifying agent team is almost never true.

**Measurement avoidance.** The opposite failure: concluding that because metrics are unreliable, there's no point measuring. Measurement skepticism is not measurement nihilism. Unreliable data, honestly acknowledged, is better than no data. The discipline is in how you interpret the data, not whether you collect it.

**Precision theatre.** Reporting metrics to false precision. "Session quality improved 12.7% quarter-over-quarter" from a sample of 30 sessions is false precision masquerading as rigour. Round to the level of confidence the data supports. When in doubt, use words instead of numbers: "roughly improved," "approximately stable," "possibly declining."

**Blaming the measurement to avoid the finding.** Measurement skepticism cuts both ways. The prior that measurements are fragile is meant to prevent premature action on bad data. It should not become a reflex for dismissing inconvenient results. When a metric survives scrutiny — the definition is stable, the sample is adequate, collection is consistent, and the proxy is close to the target — the finding deserves to be taken seriously, even if it's unwelcome. The two-step check from `load-bearing-beliefs.md` applies: check the measurement first, honestly, and then evaluate the finding.

## When to Trust a Metric

Skepticism has a resolution. A metric earns trust when:

1. **The definition has been stable** for the period being measured.
2. **The sample size is stated** and adequate for the claim being made.
3. **Collection is consistent** — no systematic gaps from dirty closes or selective reporting.
4. **The proxy gap is acknowledged** — you know what it measures and what it doesn't.
5. **The finding survives the question** "what else could explain this?"

A metric that passes all five checks is worth acting on. Most agent team metrics, honestly evaluated, pass two or three. That's fine — it means the metric is evidence with known limitations, not a conclusion. Calibrating confidence to evidence quality is the whole point.

## Evidence Summary

This pattern is **Practised (1 team, multiple catches)**, drawn from an agent team running 150+ sessions where metric reliability was repeatedly questioned and the measurement was found to be wrong in multiple cases. The specific failure modes described (definition drift, survivorship bias, self-assessment bias, small-N instability) are observed, not hypothetical.

The core claim — that measurements are wrong more often than the thing being measured — is an empirical observation from one team's practice, not a tested statistical proposition. It may not generalise to teams with more rigorous measurement infrastructure or larger sample sizes. The claim is strongest in the context where it was observed: small teams, early in their lifecycle, with self-reported metrics and evolving definitions.

The practices (metric auditing, stating the N, pre-mortem on new metrics) are structural proposals informed by that practice, not codified processes that were run as described. They represent what the source team did informally, extracted and structured into a pattern.

The two more specific sub-practices — **ruler-change tagging** and **briefing-provenance checks** — have a narrower evidence base. Both were observed in a second agent team that evolved them after encountering the failure modes they address (definition-shift contamination and memory-as-truth drift respectively). They haven't yet been tried in the team documenting this pattern. Treat them as **Observed (1 team, specific catches)**: well-motivated, but imported rather than independently confirmed. Teams considering them should notice whether the underlying failure mode is actually occurring before adopting the protocol.

No controlled comparison exists between teams practising measurement skepticism and teams that don't. The claimed benefit — avoiding decisions based on bad data — is observed but not isolated from other factors (the source team also practised load-bearing beliefs, investigation threads, and coaching reviews, all of which contribute to evidence quality).

## Related Patterns

- `load-bearing-beliefs.md` — the Measurement Trap section applies measurement skepticism to one specific context (kill conditions); this pattern generalises the principle
- `learning-from-practice.md` — confidence levels with evidence qualifiers are a form of measurement skepticism applied to methodology claims; the self-assessment bias warning directly supports this pattern
- `coaching-framework.md` — Level 3 (Measured) on the maturity ladder assumes the measurements are reliable; measurement skepticism asks whether that assumption holds
- `investigation-threads.md` — threads accumulate evidence that may itself be unreliable; measurement skepticism applies to the evidence entries, not just to aggregate metrics
- `session-transaction-protocol.md` — dirty closes create survivorship bias in session data, one of the structural fragilities this pattern addresses
- `three-tier-memory.md` — briefing-provenance checks guard the hot tier against memory-as-truth drift, a failure mode the three-tier model is particularly exposed to
