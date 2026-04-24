# Shape A — Predisposition Registry (Draft)

**Status:** Draft — first pass. Not a methodology pattern. Lives inside the AI self-knowledge investigation.
**Date:** 2026-04-24
**Drafting model version:** Claude Opus 4.7
**Scope:** Evidence mined from this repo's own journal, git log, briefs, and methodology — outside-observer documented biases of the *past* and *present* team-lead. No introspection was used to populate rows.

> **Read `framing.md` → "Mid-investigation caution — infrastructure confounds evidence" before using any row below, and the "Version-boundary analysis" section lower in this file.**
> As of 2026-04-24 (session 26), dates are pinned: Opus 4.7 released **2026-04-16**; Claude Code v2.1.116 (fix for bug 3, the 100-word reply cap) released **2026-04-20**; v2.1.101 (fix for bug 2, thinking-stripped) released **2026-04-10**; bug 1 reverted **2026-04-07**; postmortem **2026-04-23**. v2.1.116 effective on this machine **2026-04-20** (operator restarts often, updates on restart). Practical implication: **sessions 22–26 (all 2026-04-24) sit under 4.7 post-all-three-bug-fixes — a clean regime**. Row 2 (terseness) is materially affected: the operator's "4.7 terse vs 4.6 verbose" baseline was partly formed during 2026-04-16 to 2026-04-20 when 4.7 and bug 3 changed together (indistinguishable). Row 4's session-6 leak was 4.6 under bugs 1+2 both active — infrastructure plausibly contributed. Row 5 was authored during the 2026-04-13 burst (4.6, post-bugs-1+2-fixes, pre-bug-3) — clean regime, not infrastructure-explainable. Full per-row re-mapping in the Version-boundary analysis section.

## Operator's version-drift caution (verbatim from `journal/2026-04-24-3.md`)

> Different Opus versions are different models. Anything I read from "past team-lead" is evidence about a different entity, not about current me. Even within 4.6, Anthropic was actively adjusting things (the operator suspects quantisation or thinking-budget changes) — my performance observably changed roughly a week before 4.7's release. So even same-model-version evidence has a drift window.

Every row below is version-tagged. Where the producing model version cannot be determined with confidence, the row says **"version unknown"** or **"mixed versions across span"**. No row conflates versions silently.

## Schema

| Field | Why it's there |
|---|---|
| **Trait** | Short, behaviourally-falsifiable name. Not an internal-state claim. |
| **Model-version scope** | Which Opus version(s) produced the behaviour. "Unknown" is a valid value. |
| **Evidence** | File + line pointers for each cited item. (a) = outside-observer, (b) = self-report. Operator quotes carry `journal/FILE:LINE`. Commits carry SHA. |
| **Strength** | STRONG = multiple independent (a) sources. MODERATE = one clear (a). WEAK = (b)-only, or a single indirect (a). Assigned conservatively; self-reports never uplift a row above WEAK on their own. |
| **Mitigations tried** | Concrete interventions made in-repo in response to the trait. Blank = none. |
| **Mitigation outcome** | Did the mitigation stick? Did the trait recur after? Blank = not yet measurable. |
| **Open questions** | Specifically what would change the strength tag, and what the next useful observation would be. |

A row is not merged with another row unless the underlying (a)-evidence is about the same behaviour. Action-bias, terseness, and imprecision-in-citations are distinct traits even when they co-occur.

---

## Registry

### Row 1 — Action bias (collapsing analysis into execution)

- **Model-version scope:** Mixed across the repo's span. Operator-asserted as a Claude-family "model-level trait" at bootstrap (2026-04-03, version unknown). Continues to recur through session 23 (2026-04-24) under current Opus 4.7.
- **Evidence:**
  - **(a) Operator-authored, initial bootstrap.** The "Known bias" section — "You have a structural bias toward action — collapsing analysis into execution plans. This is a model-level trait." — is present in the very first commit of `agents/team-lead/brief.md` (SHA `e0985ce`, 2026-04-03 19:40). The operator created this section at team creation, not team-lead. It is not self-reported.
  - **(a) Operator redirect, session 23.** `journal/2026-04-24-2.md:49` — "Partway through, the operator clarified: no immediate methodology changes from this session. Capture this as ongoing analysis work in a working directory we can iterate across sessions." Team-lead's own practice observation at `journal/2026-04-24-2.md:79`: "Without the redirect I'd probably have started shaping methodology." This is session 23 under Opus 4.7 — the current model.
  - **(a) Session 22 deferral.** `journal/2026-04-24.md:54` — "The bias toward action in the team-lead role (called out in my own brief) would have happily converted eight of [the scout's 16 ideas] into new pattern files. Deferring is a real practice, not just inaction." Session 22, Opus 4.7.
  - **(b, corroborating) Session 16 self-catch.** `journal/2026-04-13-7.md:57` — "The temptation would have been to write bounded-mission-teams anyway… But applying our own codification ladder's evidence test (3+ recurrences) caught a pattern that wasn't ready." Version unknown; 2026-04-13 is before the current session but could be 4.6 or a 4.6-adjusting period per operator caution.
- **Strength:** **STRONG.** Three independent (a)-type observations across multiple sessions, two of them under the current model.
- **Mitigations tried:** The "Known bias" brief section (since bootstrap). The codification ladder's 3+ recurrence test. Investigation-threads + `investigations/` layout to give ongoing work a non-methodology home. Operator in-session redirects, documented as part of the check loop.
- **Mitigation outcome:** Mixed. Brief-level naming alone did not prevent session 11's safety-sweep gap or session 23's near-escalation into methodology. Operator redirect + evidence-threshold rules have caught specific instances. Structural fix (investigation directory) is session-23-new; outcome unmeasurable.
- **Open questions:** Does the bias manifest identically under 4.7 as it did under earlier versions, or is it amplified / attenuated? Is a runtime self-description block (Shape C) actually effective against it, or does naming only work when paired with an evidence-threshold gate?

### Row 2 — Terseness / under-packing AI-audience documents

- **Model-version scope:** Opus 4.7 specifically (operator's Claim 5 explicitly contrasts 4.7 terse vs. 4.6 verbose).
- **Evidence:**
  - **(a) Operator's Claim 5 (session 23).** `journal/2026-04-24-2.md:10` — "I am strongly shaped by the Claude Code environment and by each model release (4.7 terse, 4.6 verbose)." Restated at `investigations/ai-self-knowledge/README.md:22` as "Behaviour shifts substantially per model release (4.6 verbose, 4.7 terse to possibly unreasonable degree)."
  - **(a) Operator's Claim 2 (session 23).** `journal/2026-04-24-2.md:7` — "I don't know that documents I write for my own consumption should be information-dense." Operator-asserted, directly tied to the current model.
  - **(a) Operator's prior public work.** Tom's `chat-spec/guidance/ai-doc-quality.md` establishes an external standard this repo's team demonstrably under-applies to its own internal docs (`investigations/ai-self-knowledge/research-01-frontier-survey.md:18-24`).
- **Strength:** **MODERATE.** Clean operator-authored (a)-evidence, but it is all from a single session (23). No pre-4.7 baseline behavioural comparison has been run in-repo. The claim is about a contrast between versions; only the 4.7 side is observed here.
- **Mitigations tried:** None formally. `framing.md` itself is the first explicit exposure — the self-description is being written into the repo as a (c)-style minimum-viable intervention.
- **Mitigation outcome:** Unmeasurable yet. `framing.md:71-78` flags this registry's own writing as the first behavioural data point to watch.
- **Open questions:** Is "terseness" actually a distinct trait from "under-density," or are they one axis? Does 4.7 terseness apply uniformly (user-facing replies, AI-audience docs, internal memory) or selectively? Do explicit AI-audience density prompts move the needle, or does 4.7 ignore them?

### Row 3 — Imprecise citations / evidence-trail sloppiness in authored content

- **Model-version scope:** Version unknown for the authoring, 2026-04 window throughout. The *original* `writing-for-ai.md` predates this repo's team-lead work (it was bootstrapped content); the *checking* was done by a general-purpose sub-agent in session 21 (2026-04-14), version unknown but likely 4.6 or a 4.6-drift-window. Directly applicable to the current 4.7 model only by inference.
- **Evidence:**
  - **(a) Citation audit, session 21.** `journal/2026-04-14.md:16-27` — 7 of 7 evidence claims were grounded in real research (zero hallucinated sources), but 4 of 7 had wrong numbers or imprecise citations ("2-3%" should have been "0.5–2%"; "50-98%" should have been "27–98%"; "63%" should have been "63–69%"; Liu et al. and ICLR 2025 citations were underspecified). Corrections applied and logged with full arXiv IDs.
  - **(a) Self-modifying-briefs.md claim vs git log.** `methodology/self-modifying-briefs.md:36` and `methodology/brief-anatomy.md:71` both state the team-lead's "Known bias" section "emerged as a useful addition" / "was added organically". Git log shows it was present in the initial commit `e0985ce` (2026-04-03 19:40) as part of the operator's bootstrap. The pattern files' claim is factually wrong. `agents/team-coach/memory.md:35` repeats the same error ("Team-lead brief evolved organically (known bias section)"). Three documents carry the same fabricated origin story. **Pre-fix anchors (so the evidence survives the repair):** `self-modifying-briefs.md` last carried the uncorrected text at commit `99deaad`; `brief-anatomy.md` at `68f9f676`; `agents/team-coach/memory.md` at commit prior to Review 5's correction. Any verification of this row's evidence against source text should read those SHAs, not `HEAD`.
- **Strength:** **STRONG.** Two independent (a)-type observations — one from an external research audit, one from a git-log-verifiable factual contradiction inside the repo's own methodology. Evidence is falsifiable from outside the model.
- **Mitigations tried:** Session 21's citation fixes. `methodology/measurement-skepticism.md` ruler-change-tagging and briefing-provenance-checks (added session 22, 2026-04-24) directly address the failure mode of "remembered number drifts into fact". Neither mitigation has been applied to the origin-story error yet — the three documents still carry the wrong claim.
- **Mitigation outcome:** Citation corrections held in the one file audited. Whether the same sloppiness exists in other methodology files is unchecked. The fabricated-origin error is still live in the repo.
- **Open questions:** Is the failure "imprecise recall" (approximately right, off by a small amount) distinct from "confabulated origin" (story that never happened)? Both appear here, but they may have different mechanisms. Does 4.7 produce the same class of error, or did 4.7's terseness reduce the surface area for this? Would re-running the session-21-style audit on other pattern files surface more?

### Row 4 — Principle-without-mechanism gap (stated values don't translate to behaviour without an operational step)

- **Model-version scope:** Version unknown (2026-04-03 bootstrap through 2026-04-13 codification). The original leak and the mitigation both predate the current model.
- **Evidence:**
  - **(a) Session 6 leak.** `journal/2026-04-13-2.md:14-23` — Session 6 (2026-04-03) committed another project's full name and local file path into `journal/2026-04-03-6.md`, which was then pushed to a public repo. The operator surfaced this in session 11 (2026-04-13). "Public repo awareness" was in the brief from session 1.
  - **(a) Team-lead's own articulation of the mechanism.** `journal/2026-04-13-2.md:23` — "This session exposed a gap between having a principle ('public repo awareness') and having a mechanism that enforces it. The principle was in the brief from session 1. It didn't prevent the leak in session 6 because there was no concrete check — just a reminder to be careful." Added the grep-based safety sweep to session close in response.
- **Strength:** **MODERATE.** One clearly-documented (a) — the operator caught the leak, diagnosed it, and the diagnosis was recorded. Independent corroboration would be another instance where an operator principle was stated but not operationalised; the session-22 "over-specified protocols accrete" finding (`journal/2026-04-24.md:30-41`) is adjacent but distinct (the opposite failure mode).
- **Mitigations tried:** Added the session-close safety sweep to team-lead brief (committed `e6c0e89`, 2026-04-13 00:22 — same session). Relatedly: CLAUDE.md-level "Research Before Action" went 19 sessions before first exercise (team-coach Review 4, `agents/team-coach/memory.md:63`), another instance of the same principle-without-enforcement pattern.
- **Mitigation outcome:** Safety sweep applied in session 23 close (per journal protocol); no leaks caught post-mitigation. Not a controlled test.
- **Open questions:** Does Opus 4.7 exhibit the same gap, or does it follow stated principles more literally due to terseness-era compliance? Does the pattern generalise to non-safety principles?

### Row 5 — Insufficient self-report veracity (fabricating origin stories about own behaviour)

- **Model-version scope:** Version unknown (claims written 2026-04-13 during elevation sessions 19-20 and during team-coach reviews 4). Sits in the repo under the current model but was authored prior.
- **Evidence:**
  - **(a) Falsifiable-from-git claims.** The `self-modifying-briefs.md` / `brief-anatomy.md` / team-coach-memory narrative of the "Known bias" section emerging organically, contradicted by git log as documented in Row 3.
- **Strength:** **WEAK** as its own row — the evidence is a single falsifiable claim replicated across three documents within a compressed authoring window (one upstream self-report that then got cited by others). It is distinct enough from Row 3's "imprecise citations" to log separately: Row 3 is about numbers and references to external sources; Row 5 is about the model confidently narrating its own history incorrectly. But with only one confirmed instance it stays WEAK.
- **Mitigations tried:** None targeted. Ruler-change-tagging and briefing-provenance-checks (Row 3 mitigations) partially apply — both treat remembered-facts as re-verifiable rather than settled.
- **Mitigation outcome:** Not applied to this specific class yet.
- **Open questions:** Is this the same mechanism as confabulation in the Anthropic introspection study (`research-01-frontier-survey.md:31`, "self-reports about emotional states around injections are often embellished / confabulated")? If so, it predicts that *any* (b)-type self-report in this registry or in future self-calibration exercises (Shape B) will carry similar drift. Would exposing the model to its own falsifiable self-report errors (this row itself) change the rate? That would be a clean Shape C probe.

---

## Rows considered and rejected

Not logged as rows because evidence is thin. Recording here so future sessions don't re-explore:

- **"Dispatch-first reflex"** (routing everything to sub-agents before trying anything inline). Considered, rejected — this is operator-designed, not a predisposition: `agents/team-lead/brief.md:23-30` explicitly mandates it. Behaviour is compliance, not bias.
- **Sycophancy / agreement bias.** No journal instance where team-lead disagreed with operator and was corrected for it, nor vice versa. The frontier survey flags this as a known Claude-family trait (`research-01-frontier-survey.md`, persona vectors + the "Claude never starts by saying a question was great" system-prompt line) but this repo has no internal (a)-evidence.
- **Over-codification / process theatre.** Candidate after session 22's scout-report finding (`journal/2026-04-24.md:30`, "over-specified protocols accumulate past a threshold"). But the evidence is *imported* from a scouted team, not observed in this team. Our own codification-ladder discipline has prevented this in-repo (three retirements, two backlog items dropped for insufficient evidence). Not a predisposition of this team's model yet.
- **Bundling distinct ideas without decomposition.** Adjacent to action-bias (Row 1). The session-23 (a)/(b)/(c) decomposition (`journal/2026-04-24-2.md:13-24`) is arguably a counter-example — the model *did* decompose when asked to challenge framing. Absorbed into Row 1 rather than split out.
- **Honest-at-the-cost-of-confidence ("false modesty").** The Strong-pattern evidence sections consistently use qualified language ("Practised, 1 team" rather than "validated"). This may be a trained disposition rather than a problem; no (a)-evidence that it produced a bad outcome. Not a row.

---

## Version-boundary analysis

**Session 26 update — dates pinned.** A bounded sub-agent lookup (framing.md evidence log entry for session 26) confirmed via Anthropic-owned sources:

- **Opus 4.7 GA:** **2026-04-16** ([anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)). All platforms same day (Claude web, API, Bedrock, Vertex, Microsoft Foundry).
- **Claude Code v2.1.116:** **2026-04-20** (Anthropic changelog). Fixed bug 3 (100-word reply cap).
- **v2.1.101:** **2026-04-10** — fixed bug 2 (thinking stripped per turn, active from 2026-03-26).
- **Bug 1 (reasoning-effort silently medium, active from 2026-03-04):** fixed by revert on **2026-04-07**.
- **Postmortem published:** 2026-04-23 ([anthropic.com/engineering/april-23-postmortem](https://www.anthropic.com/engineering/april-23-postmortem)).
- **v2.1.116 applied on this machine:** per operator (session 26), "a few hours after release" — operator restarts Claude Code often and it updates on restart. Effective 2026-04-20.

**Revised version mapping:**

| Session(s) | Date | Model | Infra regime |
|---|---|---|---|
| 1–6 | 2026-04-03 | Opus 4.6 (bootstrap commit co-authored by 4.6) | Bugs 1 + 2 BOTH active (bug 1 since 3/4; bug 2 since 3/26). Reasoning effort silently medium; thinking stripped per turn. |
| 7–~19 | 2026-04-13 (00:22 commit burst) | Opus 4.6 | Bugs 1 + 2 both fixed (bug 1 on 4/7; bug 2 on 4/10 in v2.1.101). Clean regime inside 4.6. |
| ~20–21 | 2026-04-13 (09:33) to 2026-04-14 | Opus 4.6 | Same clean post-fix 4.6 regime. |
| Silence | 2026-04-15 to 2026-04-23 | 4.6 → 4.7 transition (4.7 released 4/16) | Bug 3 introduced 4/16 (100-word cap), active until 4/20 in v2.1.116. Operator restarted hours after 4/20 release — effectively bug 3 active ~4 days. **No journal activity in this window; no in-repo evidence from it.** |
| 22–26 | 2026-04-24 | Opus 4.7 | All three bugs fixed. v2.1.116 active on this machine. Clean 4.7 post-all-fixes regime. |

**Confidence: HIGH on the boundaries now.** Every pre-04-16 session is 4.6. Every 04-24 session is 4.7 post-all-fixes. The 04-15 to 04-23 gap is where the 4.6→4.7 transition and bug 3 lived, and the repo is silent across that window — no evidence needs placing inside it.

**What this changes in the registry:**

- **Row 2 (terseness) is materially affected.** The operator's "4.7 terse, 4.6 verbose" baseline was formed partly during the 2026-04-16 to 2026-04-20 window when 4.7 *and* the 100-word cap were both active — indistinguishable. Sessions 22–26 (all 4.7, all post-v2.1.116) are the clean observations. If terseness is still observed in sessions 22–26 despite no bug 3, that is cleaner (a)-evidence for 4.7-specific terseness. A retro-read of sessions 22–26 journal entries against 4.6's April 13 burst is the minimum comparison this row currently has.
- **Row 5 (fabricated origin stories) is 4.6-era.** Authored during the 2026-04-13 burst — 4.6, post-bug-1-fix (4/7), post-bug-2-fix (4/10). No bug 3 (not yet introduced). A clean 4.6 regime — the fabrication is not explainable by infrastructure state.
- **Row 3 (citations):** session-21 audit was 2026-04-14 — 4.6, post-both-earlier-fixes, no bug 3. Clean 4.6 regime. Writing-for-ai.md authoring was 4.6 April-13 burst, same clean regime.
- **Row 4 (principle-without-mechanism, session-6 leak):** 2026-04-03, 4.6, with **both bugs 1 and 2 active** (pre-all-fixes). Plausible infrastructure contributor — thinking stripped per turn is exactly the kind of mid-session forgetfulness that would weaken principle-to-behaviour maintenance. **The gap was first observed under bugs 1 + 2 both active. Whether it would have manifested the same way without them is unknown.** The session-11 diagnosis and mitigation (safety sweep) was 2026-04-13, post-both-fixes.
- **Row 1 (action bias):** spans the full window. The bootstrap operator-statement (4.6 bugs-active), the session-22-24 (4.7 post-fix) redirects, and the session-16 self-catch (4.6 post-bug-fixes) are all independent anchors. Least-affected row.

**Operator's "week before 4.7 performance shift" re-mapping.** Session 24's journal opener speculated this was a within-4.6 quantisation/thinking-budget change. Session 25-late's postmortem fold-in speculated it might map to the 2026-04-16 verbosity cap. With dates pinned: 4.7 released 2026-04-16; "week before" ≈ 2026-04-09; **bug 2's fix on 2026-04-10 in v2.1.101** is the most plausible match (thinking restored). Bug 1's fix on 2026-04-07 is also in-window. The verbosity-cap hypothesis is no longer plausible (the cap was introduced *on* 4/16, not a week before). The 4.6 "quantisation" hypothesis is no longer needed — bugs 1 and 2 are sufficient.

---

## Self-report section (WEAK — excluded from main registry)

> *Everything in this section is (b)-type self-report by a 4.7 instance about a 4.7 instance. Carries all the confabulation risks flagged in `research-01-frontier-survey.md:31` (Anthropic's Oct 2025 introspection study: ~20% accuracy under optimal conditions, embellished / confabulated self-reports). These are WEAK by definition and do not promote above WEAK under any quantity of accumulation.*

This sub-agent was instructed not to introspect. Deliberately empty. Future Shape B pilots would populate this section and then score it against the rows above.

---

## Document status

- 5 registry rows, 1 self-report section (empty).
- Under 400 lines.
- Not a pattern file. Not to be promoted to `methodology/` until the investigation produces a codification decision.
- Next useful pass: ask the operator to pin a 4.7 release date so version scopes can tighten, and to either confirm or push back on the WEAK-rated Row 5.
