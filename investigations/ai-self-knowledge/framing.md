# Framing — AI Self-Knowledge

Working synthesis. Updated across sessions. AI-audience density discipline applies: prose is fine, throat-clearing is not.

## Why the decomposition matters

Bundling "self-knowledge" produces circular argument. Three distinct objects:

- **(a) Observed predispositions** — outside-view truth. Falsifiable. "Claude 4.7 collapses exploration into execution" is a claim about behaviour, not about the model's interior.
- **(b) AI-reportable self-models** — model utterances about itself. Often plausible, sometimes post-hoc, sometimes confabulated. The skeptic literature is strong here (Turpin 2023 CoT unfaithfulness; Huang/Stechly/Valmeekam 2023 intrinsic critique harmful; Anthropic 2025 introspection ~20% at best).
- **(c) Intervention effect** — whether *telling* the model (a) or (b) changes behaviour in the intended direction. The empirical claim worth testing. Implicit strong evidence: Anthropic's production system prompt does this at industrial scale. Explicit public A/B evidence: thinner than expected.

(a) is the library's first natural asset. (b) is its first natural calibration exercise. (c) is its first natural experiment.

## Key findings from round-1 research

Sources and citations in `research-01-frontier-survey.md`. The load-bearing extracts:

1. **Anthropic holds the deepest interp-to-behaviour programme.** Persona vectors (arXiv 2507.21509), assistant axis (Nov 2025), concept-injection introspection (transformer-circuits.pub Oct 2025), inoculation prompting (alignment.anthropic.com 2025). Predispositions are treated as mechanistic linear features, not folk psychology.
2. **Self-reflection is not unambiguously helpful.** Intrinsic self-critique often *lowers* accuracy on reasoning tasks. Self-refine amplifies self-bias (Xu et al. 2024, ACL). External feedback dominates.
3. **Behavioural self-awareness is real but narrow.** Betley et al. 2025 ("Tell Me About Yourself", ICLR): fine-tuned latent policies become spontaneously describable by the tuned model. Open whether this generalises to native pre-training tendencies.
4. **Anthropic's production system prompt is itself a live (c) experiment.** Simon Willison's Claude 4 annotation documents lines like "Claude never starts its response by saying a question was great" and formatting-bias correctives — Anthropic naming Claude's tendencies *to* Claude at runtime. Operational evidence it works; no published A/B.
5. **Version drift is measured and has caused real harm.** Anthropic's April 23 2025 postmortem: an anti-verbosity system-prompt addition cross-coupled into degraded coding quality, rolled back four days later. Direct warning for Shape C below.
6. **The genuinely empty slot:** a public practitioner methodology pairing a per-version predisposition registry with controlled runtime interventions against it. Research exists upstream (mech interp) and downstream (production prompts); the practitioner-facing middle is sparse.

## Candidate shapes

### Shape A — Predisposition Registry

Per-version catalogue of observed traits. Schema fields: trait, evidence source(s), model version, reproducer, mitigations tried, mitigation results. Public. Referenced from agent briefs and project CLAUDE.md files.

- **Novelty:** low intellectual, high practical. Most current knowledge lives as folklore (release-note gossip, blog posts, Slack screenshots).
- **Evidence bar to publish as pattern:** one well-maintained instance showing downstream use.
- **Risk:** degenerates into gossip. Requires evidence-strength tagging (pattern we already practise; `measurement-skepticism.md` gives vocabulary).

### Shape B — Self-Calibration Protocol

Prompt the model to enumerate its own predispositions under a defined protocol. Compare output to registry (a). Score agreement. Produce per-version self-knowledge score.

- **Novelty:** adjacent-novel. Betley / Kadavath / "Could you be wrong" (arXiv 2507.10124) are upstream; no practitioner wrapper I found.
- **Evidence bar:** run across ≥2 model versions, publish scores and the observed score-to-behaviour correlation if any.
- **Risk:** low self-report accuracy is the expected finding (the skeptic literature is unambiguous). Framing must be *diagnostic*, not "model score".

### Shape C — Intervention A/B Methodology  *(strongest novelty slot)*

Take registry (a). Inject as a runtime self-description block. Measure behaviour on bounded tasks with and without. Document direction *and* cross-coupling.

- **Novelty:** highest. Direct public (c) test is genuinely underpublished.
- **Evidence bar:** one well-run instance for one model version, ≥3 tasks, shift in intended direction, no regressions on others. Anthropic April 23 2025 postmortem is the cautionary case — cross-coupling is real.
- **Risk:** highest cost; cross-coupling likely; result may be "targeted injection helps on-target but introduces a regression elsewhere."

### Shape D — Version-Drift Operational Hygiene

Runbook for release-boundary behaviour: what to re-measure, what to re-test, how to update prompts and memories. Integrates A/B/C.

- **Novelty:** integrator, low standalone.
- **Evidence bar:** apply once across a real release boundary.

## Current inclination

**A + C in combination is the strongest publishable artefact.** A produces the ground truth C requires. B is a cheap intermediate that tests whether self-report can short-cut A. D integrates.

Sequencing hypothesis:

1. Draft A schema + one worked entry. Cheapest. Immediately useful.
2. Pilot B against A. Cheap. Produces a calibration data point.
3. Design C only if A is populated enough to support it and the team feels the pain.

Feel-the-pain test is not hypothetical here: the operator has just observed that I am demonstrably bad at knowing my own doc-density predispositions. That is the pain. It is the evidence that justifies at least step 1.

## Built-in self-experiment

This investigation is itself a (c) test. The act of naming my predispositions here, then writing subsequent sessions, is the minimum-viable intervention. Signals to capture over time:

- Do subsequent outputs shift toward higher information density after this file is written?
- Does the operator observe behavioural change across sessions?
- Does having (a) in repo make synthesis sharper, more cautious, or neither?

Entries go in the evidence log below, dated.

## Open questions

1. Can an agent self-populate (a), or is an outside observer required? Betley et al. suggest partial self-population works for fine-tuned policies. Unknown for native pre-training tendencies.
2. Does (c) require the model to *believe* a self-description, or does exposure suffice? Persona-prompting literature suggests exposure. Honest self-descriptions may be a distinct case.
3. What's the right re-measurement cadence per model version? No clean answer in drift literature.
4. Is there a lightweight version for short-lived agents, distinct from a library-maintained long-lived registry?
5. Density ↔ behaviour: does writing denser AI-audience docs actually produce measurable behaviour change, or is density only a loss-minimiser (not a behaviour-shaper)? This is the operator's Claim 1 phrased as a hypothesis.

## Next-session candidates

- Draft Shape A skeleton schema + one worked entry ("4.7 terseness").
- Pilot minimum Shape B (ask current model to enumerate predispositions; score against a small hand-written a-list).
- Write a second research round with tighter scope (sustained intervention-(c) studies only).

## Evidence log

- **2026-04-24** — research round 1 received (`research-01-frontier-survey.md`). Frontier established; clearest unclaimed slot is (c).
- **2026-04-24 (session 24)** — Shape A first draft produced: `shape-a-registry-draft.md`. 5 rows, evidence-tagged, version-stamped. Two rows STRONG (action bias, imprecise-citations / evidence-trail sloppiness), two MODERATE (4.7 terseness, principle-without-mechanism gap), one WEAK (fabricated-origin self-reports). Unexpected finding: three methodology files (`self-modifying-briefs.md`, `brief-anatomy.md`, `agents/team-coach/memory.md`) carry an origin-story for the "Known bias" brief section that is falsified by git log (section was present in bootstrap commit `e0985ce` by operator, not emerged organically). That is clean falsifiable (a)-evidence of in-repo self-narration failure. Not fixed this session; flagged for a future targeted audit.
  - Version-anchor tightened: bootstrap commit `e0985ce` (2026-04-03) is co-authored by Claude Opus 4.6 per its commit message. So sessions 1–6 are at minimum 4.6-era, not 4.5. The 4.6→4.7 boundary inside the 2026-04-14 to 2026-04-24 repo-silence window is still unresolved from in-repo evidence alone.
  - Open ask for operator: pin the 4.7 public release date so every pre-04-24 row scope can tighten. Confirm or push back on Row 5 (WEAK) as its own distinct trait vs. subsumed into Row 3.
- **2026-04-24 (session 25)** — R5.2 landed: the three fabricated-origin-story instances in `self-modifying-briefs.md`, `brief-anatomy.md`, and `agents/team-coach/memory.md` are fixed. Pre-fix text preserved via commit-SHA anchors in Row 3. Two bonus Row-3 finds also fixed (`three-tier-memory.md` Buttondown attribution; `discipline-processes.md` citation drift from session-21 correction).
- **2026-04-24 (session 25, late)** — *per operator report.* Anthropic has just published a postmortem documenting three Claude Code infrastructure bugs affecting behaviour over roughly the last month:
  1. **2026-03-04** — default reasoning-effort silently dropped from high to medium (UI continued to show high).
  2. **2026-03-26** — a caching optimisation stripped Claude's thinking every turn instead of once. "Claude got forgetful mid-session."
  3. **2026-04-16** — a system prompt was added telling Claude to keep replies under 100 words. "Coding quality tanked."

  All three fixed in Claude Code v2.1.116. See the "Mid-investigation caution" section below for how this propagates into registry confidence (spoiler: it widens uncertainty, it does not narrow it into per-row confounders).
- **2026-04-24 (session 26)** — Shape B self-report pilot 01 and scoring pass 01 complete. Two sub-agent passes: author (`shape-b-self-report-01.md`, 8 rows, declared contamination from reading more of README.md than instructed) and scorer (`shape-b-scoring-01.md`, ~260 lines). Headline findings:
  - **Coverage 4/5 (80%) surface; 0/5 (0%) unprimed.** Every Shape A row the self-report hit traced to text the author had already read (brief's "Known bias" line primed Row 1; README.md operator-claims primed Rows 2 and 4-subsumed-5; `measurement-skepticism.md` primed calibration claims). The single clean Shape A miss — Row 4 (principle-without-mechanism) — is the only Shape A row *without* a priming anchor in permitted reading. Correlation suggestive: the self-report echoed what the operator had surfaced, missed what the operator had not.
  - **Decomposition failure.** Shape A split Row 3 (imprecise numerical recall) and Row 5 (fabricated origin stories) on explicit mechanism-difference grounds. Shape B collapsed both into a single "confabulation of provenance" row. This is distinct from trait-missing — the self-report had the content but lost the split. Clean (a)-type data point about the model class's decomposition discipline under self-report conditions.
  - **Novel complementary value.** Two of Shape B's novel rows (Row 5 overconfidence-in-self-report, Row 6 mid-context attention loss) surface trait classes the outside-observer registry by design cannot reach. Row 5 is self-visible (the document itself is exhibit A — 3 STRONG and 4 MODERATE ratings, zero WEAK despite a brief warning most should be WEAK). Row 6 carries a public citation (Liu et al. 2024 "Lost in the Middle") already in this repo's `writing-for-ai.md`. These have genuine evidentiary value distinct from self-knowledge-about-observed-traits.
  - **Calibration optimistic by one notch, WEAK absent.** On the one corresponding row where strength ratings disagreed, Shape B rated STRONG (on public-literature grounding) a trait Shape A rated WEAK (on single-instance repo-specific evidence). WEAK is absent from Shape B's 8 rows entirely. Both consistent with Shape B's own Row 5 claim.
  - **Padding row.** Shape B Row 2 (sycophancy) was included with thin public citations and introspection despite Shape A having considered and explicitly rejected it for lack of in-repo (a)-evidence. Clearest "pushed toward 8 rows rather than a smaller higher-evidence set" signal in the pilot.
  - **Shared-prior confound limits interpretation.** Shape A author, Shape B author, and the scorer are all Opus 4.7 sub-agents from the same 24-hour window. A 4/5 match is as consistent with "shared pre-training prior" as with "genuine self-knowledge". This pilot alone cannot disentangle them.
  - **New open questions for operator:** (i) do the (b)-visible complementary trait classes (Shape B Rows 5, 6, 7, 8) belong in Shape A as a distinct evidence tier, or in a separate Shape-B-flavoured registry? (ii) sycophancy — is it active in team-lead's observed behaviour? Shape A said no in-repo evidence; Shape B asserted it from priors. One direct operator observation would resolve.
  - **Scorer's primary recommendation:** before running additional Shape B pilots, run one **cold-read variant** (permitted reading reduced to `CLAUDE.md` + task spec only — no brief, no README, no methodology) to separate primed self-knowledge from any unprimed component. The current permitted-reading list is where the priming comes from; repeating it will produce more instances of the same finding.
- **2026-04-24 (session 26, late — operator answers folded in).** Operator addressed 3 of 5 open asks directly; 2 declined. Dispatched a bounded sub-agent for public-date lookups; all Anthropic-owned sources.
  - **Ask 1 answered (dates pinned, HIGH confidence, Anthropic-owned sources).**
    - Opus 4.7 general availability: **2026-04-16** ([anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)).
    - Claude Code v2.1.116: **2026-04-20** (Anthropic changelog; fixes bug 3).
    - v2.1.101: **2026-04-10** (fixes bug 2).
    - Bug 1 revert: **2026-04-07**.
    - Postmortem published: **2026-04-23** ([anthropic.com/engineering/april-23-postmortem](https://www.anthropic.com/engineering/april-23-postmortem)).
  - **Ask 2 declined by operator.** Row 5 framing — no operator input. Row stays WEAK, as its own row, unchanged. Resolved by deferral, not by argument.
  - **Ask 3 answered.** Operator restarts Claude Code often and it updates on restart; v2.1.116 effective on this machine "a few hours after release" — so effective 2026-04-20. Combined with date pins, this means **sessions 22–26 (all 2026-04-24) are post-all-three-bug-fixes under 4.7**. Every evidence point from those sessions is under a clean infrastructure regime.
  - **Ask 4 declined by operator.** Tier structure (whether (b)-visible complementary rows belong in Shape A or a separate Shape-B registry) — no operator input. Shape B Rows 5, 6, 7, 8 stay in the self-report pilot file only; Shape A unchanged structurally.
  - **Ask 5 answered — direct (a)-type operator observation.** "I don't see you doing it since 4.7, and it may have been more of a characteristic of claude web than claude code anyway." This is a direct operator observation that **Shape B Row 2 (sycophancy) is not active in team-lead's current behaviour**. Two secondary findings: (i) the operator attributes the behaviour-change to the 4.6→4.7 transition; (ii) the operator differentiates Claude web from Claude Code environments, suggesting the trait may be more harness-mediated than model-mediated even within the same family. Shape A's original rejection of sycophancy stands ("no in-repo evidence"); Shape B's inclusion of it is now explicitly overridden by operator observation.
  - **Material registry update.** `shape-a-registry-draft.md`'s version-boundary analysis section rewritten with the pinned dates. Per-row re-mapping:
    - **Row 2 (terseness) materially affected.** Bug 3 (100-word reply cap) was introduced **on the same day** as 4.7's release (2026-04-16). Any "4.7 terse vs 4.6 verbose" contrast the operator formed during 2026-04-16 to 2026-04-20 is confounded — bug 3 and the new model both changed at once. Only sessions 22–26 (all 2026-04-24, post-v2.1.116) produce clean 4.7 terseness observations. The operator's baseline is not itself clean evidence of a model-level trait.
    - **Row 5 (fabricated origin stories) is 4.6 post-all-then-fixes.** Authored during the 2026-04-13 burst, after bug 1 fix (4/7) and bug 2 fix (4/10), before bug 3 existed. Clean 4.6 regime — not explainable by infrastructure state.
    - **Row 4 (principle-without-mechanism) session-6 leak was 4.6 under bugs 1+2 both active.** The gap was first observed under thinking-stripped-per-turn — plausibly contributing. Whether the gap would have manifested the same way without infrastructure confounds is unknown from in-repo evidence.
    - **Row 3 (citations):** session-21 audit (2026-04-14) is 4.6, clean regime.
    - **Row 1 (action bias):** unchanged — spans enough independent regimes that infrastructure doesn't explain it.
  - **Session 25-late "verbosity cap" speculation retracted.** Session 25-late noted the operator's "week before 4.7" performance shift "maps plausibly onto the 2026-04-16 verbosity cap." With dates pinned: 4.7 released 2026-04-16, "week before" ≈ 2026-04-09, and bug 2's fix on 2026-04-10 in v2.1.101 (thinking restored) is the most plausible match. Bug 1's revert (2026-04-07) is also in-window. The verbosity-cap hypothesis is incompatible with the dates (the cap was introduced *on* 4/16, not a week before). The 4.6 "quantisation" hypothesis is no longer needed — the postmortem's documented bugs are sufficient explanation. Registry v-boundary section and this log carry the corrected reading.

## Mid-investigation caution — infrastructure confounds evidence, skepticism widens rather than narrows

The three bugs above are external (a)-evidence that factors *other than model predispositions* were shaping observable behaviour during the windows when this investigation collected its evidence. The dates matter:

| Date range | What was active |
|---|---|
| 2026-03-04 onward | Reasoning-effort silently medium (not high). |
| 2026-03-26 onward | Thinking stripped every turn (intra-session forgetfulness). |
| 2026-04-16 onward | 100-word reply cap in Claude Code system prompt (verbosity compression). |
| Until v2.1.116 | All three active. |

Every row in `shape-a-registry-draft.md` carries evidence collected during one or more of these windows. Session 21 (2026-04-14) predates the April 16 verbosity cap but falls inside the reasoning-effort and caching bugs. Sessions 22–24 (2026-04-24) sit inside all three bugs *if* v2.1.116 had not yet been pulled onto this machine by the time of those sessions. The timing of the update on this specific machine is not established in-repo.

**The temptation this finding creates, and why it is wrong to give in:** the Shape A rows most superficially affected (Row 2 terseness, Row 4 principle-without-mechanism, Row 1 action bias under a reasoning cap) have an obvious candidate alternative explanation now. It would be natural to walk through each row and annotate "confounded by bug X". That annotation would itself be a Row-1-flavoured move: collapsing uncertainty into a specific causal story.

What we actually know:

- The three bugs existed and affected Claude Code behaviour in ways that *plausibly* overlap with several registry rows.
- We do not know, per row, whether a given observation was (i) purely predisposition, (ii) purely infrastructure, or (iii) a product of both. The rows do not support that separation yet.
- Some rows are almost certainly robust to this news. Row 3 (imprecise citations) concerns specific claims grounded in specific sources — a 100-word reply cap does not cause a researcher to change "0.5–2%" to "2–3%". Row 5 (fabricated origin stories) is git-log-falsifiable and was in-repo for weeks.
- Some rows are more exposed. Row 2 (4.7 terseness) rests on evidence from session 23 (2026-04-24), inside the April 16 cap window. If Claude Code was not yet updated on this machine at that point, the session 23 terseness could be model-level, infra-level, or both.

**How to carry this forward without over-correcting:**

1. No per-row annotation this session. Rows stay as they are. The registry carries a pointer up to this section.
2. A Shape B pilot (the next-up item) now has a much cleaner hypothesis: ask the current model to self-report its predispositions *post-fix* and compare to pre-fix operator observations. Divergence between pre-fix behaviour and post-fix self-report is itself evidence — about both the model and the fix.
3. Version-boundary analysis was already LOW confidence. It is now LOW-er. The useful operator asks are now three, not two: (i) 4.7 release date; (ii) Row 5 framing; (iii) when was v2.1.116 applied on this machine (critical for mapping sessions 22–25 to pre/post-fix regimes).
4. None of the three bugs explains Row 3's citation-audit finding or the fabricated-origin-story finding. Those remain the registry's most robust evidence regardless.
5. This is itself a datapoint about the investigation's methodology: the version-drift discipline (session 24 caution) was correct in spirit and the specific mechanism turned out to be harness-level, not quantisation. The operator's instinct — "performance shifted roughly a week before 4.7's release" — maps plausibly onto the 2026-04-16 verbosity cap. Not confirmed; noted.

Skepticism widens. Findings do not collapse into revised claims. The registry gets better only by getting more evidence, not by retro-fitting the evidence it has to a new explanation.
