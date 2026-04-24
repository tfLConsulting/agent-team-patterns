# Team Coach — Memory

## Current State
- **Created:** 2026-04-03
- **Last review:** Review 5, Session 25 (2026-04-24)
- **Framework version:** v1

## Team Composition
| Agent | Created | Status |
|-------|---------|--------|
| team-lead | 2026-04-03 | Active |
| team-coach | 2026-04-03 | Active |

Candidate specialists (bench):
- **researcher** — Second and third external-research demand signals landed in sessions 21, 22, 23. General-purpose sub-agents handled all three competently. Still NOT 3+ *recurring* sessions of demand by Review 5's read — sessions 21 (citation audit), 22 (external-team scout), and 23 (frontier survey) are three discrete one-shot dispatches across four weeks, not a sustained need for a loaded external-research context. Context-separation test still uncertain: the three dispatches had different prompts, different source materials, different output shapes. A real researcher would need stable loaded context across sessions — none of the three built on the previous. Revisit if a fourth research task arrives with shared context (e.g. follow-up citation audit on more methodology files; continuation of the self-knowledge frontier survey).
- **curator** — Library at 16 pattern files, all Strong. No curator signal observed sessions 20–25. Still fails context-separation test.

## Review History

### Review 1 — Session 3 (2026-04-03)
No composition changes. Two-agent team right-sized. Three watch signals set.

### Review 2 — Session 9 (2026-04-12)
No composition changes. First use of v1 five-dimension framework — all dimensions scored 1-2.

### Review 3 — Session 14 (2026-04-13)
No composition changes. All dimensions level 2. Research Before Action flagged as longest-running untested principle.

### Review 4 — Session 19 (2026-04-13)
No composition changes. R4.2 prioritise writing-for-ai.md citations. Information Architecture promoted 1→2.

### Review 5 — Session 25 (2026-04-24)
**Recommendation: No composition changes. One actionable item (R5.2). Two observation watches (R5.3, R5.4). One score downgrade: Specification Quality 2 → 1-2 (regression, evidence-based).**

Five-dimension scores (v1 framework):
| Dimension | Level | Change | Notes |
|-----------|-------|--------|-------|
| Specification Quality | **1-2 (Documented-to-Consistent, regressing)** | **Down from 2** | Three methodology files narrate a fabricated origin story for the "Known bias" brief section (surfaced session 24). team-coach's own memory file repeats the same error. Team-lead chose not to fix this session, reasoning it preserves live evidence for the investigation. That is defensible for *the registry* but the files are still wrong in the *public-facing* methodology. Specifications-about-specifications have a factual error. |
| State Management | 2 (Consistent) | Stable | Memory files well under 200 lines (team-lead 118, team-coach 79). Investigation directory is new warm-tier artefact — placed correctly per `three-tier-memory.md`. No protocol drift observed. |
| Process Maturity | 2-3 (Consistent, approaching Measured) | Stable | Directed-mode protocol feeling "well-worn rather than effortful" per session 22 practice observation. Journal-first discipline held across all 6 sessions. Investigation-threads pattern was exercised for the first time (session 23) — first practice 23 sessions after the pattern was written. Call this out: pattern-before-practice is real, now visible. |
| Information Architecture | 2 (Consistent) | Stable | Investigation directory added cleanly; cross-references intact. External-scout produced 16 ideas that were *queued* not *adopted* — output-to-action ratio was deliberately held low, which is the correct use of `measurement-skepticism.md`'s discipline. |
| Evolutionary Fitness | **3 (Measured)** | **Up from 2** | This is the review's strongest signal. Three consecutive sessions of evidence-based behavioural discipline: session 21 exercised Research Before Action (longest-untested principle, finally tested, 4/7 corrections made); session 22 deferred 14 of 16 scouted ideas (the discipline of *not* acting is observed, not theorised); session 24 produced falsifiable evidence of the team's own prior failures and logged them honestly rather than rewriting history. The team is now not just *practising* what it documents — it is *measuring itself against* what it documents and catching real failures. |

Backward validation:
- R4.1 (no composition changes): **Validated** — team-lead + team-coach operated effectively through sessions 20-25. Six productive sessions: 1 elevation completion, 1 citation audit, 1 external scout, 1 investigation opening, 1 registry draft, 1 coach review. No work was blocked by team composition.
- R4.2 (prioritise writing-for-ai.md citations): **Validated** — session 21 executed this cleanly. All 7 claims verified, zero hallucinated, 4 corrections applied. Research Before Action went from "structurally untested" to "exercised under real conditions with evidence gathered."
- R4.3 (watch elevation process codification): **Retired (question answered)** — elevation was a one-time roadmap, not a standing practice. All 16 methodology files are Strong; no new extraction backlog. The elevation process does not need codification because the phase is over. Observation closed.
- R4.4 (Research Before Action — explicit test): **Validated (with unexpected positive)** — tested in session 21 as designed. Unexpected: *three* sessions in a row (21, 22, 23) have now exercised external-research patterns. The principle is no longer "structurally untested" — it is exercised, and has produced valuable outputs each time. The absence of a researcher specialist is now evidence-backed rather than assumed: general-purpose sub-agents handle bounded research tasks without strain.

## New Observations from Sessions 20–25

### The investigation mode is new and is not yet visibly costing anything — but it hasn't been stress-tested
`investigations/` as a directory is new this review period (session 23). It is the first *practice* of the `investigation-threads.md` pattern, which has existed as a file since session 10. That's 13 sessions of pattern-without-practice — a useful data point for team-lead's own self-audit. The current investigation (AI self-knowledge) has three artefacts and a clean README. Team structure has not changed to accommodate it, and the team-lead has explicitly not created an "investigator" role. **This is correct.** The two-part test (recurring + context separation) isn't met — this is the first investigation, and the team-lead is holding the context fine. But: if a second independent investigation opens *before* this one is resolved, the two-part test may suddenly trigger, and the team should be ready to answer "who owns this?"

Watch for: second investigation opening while the first is active. That is when the question of role structure around investigations becomes real, not theoretical.

### The fabricated origin story is Specification Quality evidence, not just investigation fodder
Session 24 found three methodology files plus this coach memory file that narrate the "Known bias" brief section as having "emerged organically." Git log shows it was in bootstrap commit `e0985ce` (operator-authored). The team-lead's decision not to fix this session is *investigation-defensible* but *specification-problematic*. These files are the public-facing methodology — they are meant to be read by other practitioners. They contain a factual error. Three of them.

My own memory file (Review 4, line 35 as it was written) also carried this error: "Team-lead brief evolved organically (known bias section)." I was wrong. The claim was never verified against git log during Review 4. This is a direct failure of the framework's own discipline — I scored Specification Quality at 2 while repeating a factually wrong narrative *about* the specification I was scoring. That is measurement theatre in my own prior review.

**I am correcting my own memory file with this review (see `Review 4` entry below).** Not silently — explicitly noted. This is what a measurement skeptic would want.

### Measurement skepticism is now self-referential in a useful way
Session 22's external scout harvested 16 ideas. Team-lead adopted 2 (ruler-change tagging, briefing-provenance checks — both additions to `measurement-skepticism.md` itself). The discipline of *not adopting* the other 14 is observed directly. Session 24 then demonstrated briefing-provenance checks in action when the sub-agent was told *not* to introspect and to version-stamp every claim. The principle added in session 22 shaped behaviour in session 24. That is evidence the codification served a purpose, not just a shelf.

## Recommendation Tracking

| # | Recommendation | Expected Outcome | Status | Actual Outcome | Learning |
|---|---------------|------------------|--------|----------------|----------|
| R2.1 | No composition changes | 2-agent team operates effectively | **Validated** | Effective through sessions 10-13 | Right-sized. |
| R2.2 | Clean up stale candidate listings | Brief reflects current evidence | **Validated** | Restructured per R3.2 | Two-pass fix. |
| R2.3 | Watch for Research Before Action compliance | Sessions include external research or note why unnecessary | **Validated (closed, positive)** | Sessions 21, 22, 23 all exercised external research | From "structurally untested" to "exercised three ways in three weeks" — R4.4's test worked. |
| R3.1 | No composition changes | Team operates effectively through sessions 15-19 | **Validated** | Four productive sessions | Two-agent team effective across multiple work phases. |
| R3.2 | Restructure candidate listings | Candidate info reflects current evidence within 2 sessions | **Validated** | Team-lead memory now carries assessments | Took 1 session. |
| R3.3 | Watch cross-reference maintenance burden | Observe next 2-3 patterns for difficulty | **Validated (no burden)** | Three elevations added 6-8 cross-refs each | At 16 patterns, manageable. Curator signal absent. |
| R3.4 | Watch extraction backlog exhaustion | Observe transition when team needs new sources | **Validated (resolved)** | Clean transition to elevation phase | Phase transition handled well. |
| R4.1 | No composition changes | Team operates effectively through sessions 20-24 | **Validated** | Six productive sessions, 1 elevation completion, 1 citation audit, 1 external scout, investigation opened, Shape A drafted, coach review ran | Still right-sized. |
| R4.2 | Prioritise writing-for-ai.md citations after elevation roadmap | Session exercises Research Before Action | **Validated** | Session 21, 7/7 claims verified, 4 corrections | The "R4.4 test case" worked as a forcing function. |
| R4.3 | Watch for elevation process codification need | Observe whether elevation continues post-roadmap | **Retired (question answered)** | Elevation was one-time; no recurrence post-roadmap | No codification needed for a completed phase. |
| R4.4 | Research Before Action — explicit test | writing-for-ai.md citations task triggers the principle | **Validated (with unexpected positive)** | Three sessions in a row exercised external research, not one | General-purpose sub-agents handle bounded research without a specialist. |
| **R5.1** | **No composition changes** | Team operates effectively through sessions 26-30 | Proposed | — | — |
| **R5.2** | **Fix the fabricated origin story in three methodology files + team-coach memory** (`self-modifying-briefs.md:36,50`; `brief-anatomy.md:71`; this memory's old Review 4 entry) | Public-facing methodology matches git-log-verifiable truth within 2 sessions | Proposed | — | — |
| **R5.3** | **Watch for second investigation opening** | Observe whether investigation mode scales to 2+ concurrent without role restructure | Proposed (observation) | — | — |
| **R5.4** | **Watch for pattern-without-practice in other patterns** | Session 24 found `investigation-threads.md` was pattern-before-practice by 13 sessions. Check whether other patterns (coaching-framework, discipline-processes) have similar gaps | Proposed (observation) | — | — |

## Watching For (sessions 26-30)
- Does R5.2 get executed? A targeted audit across methodology files would be the clean vehicle (team-lead already flagged this as candidate next session).
- Does a second investigation open while the first is active? (R5.3 — investigation-mode scaling signal)
- Any other pattern files that describe practices the team has not exercised? (R5.4 — pattern-before-practice audit)
- Shape B pilot (self-calibration) — if it runs, it is the first (b) data point and directly tests whether the coach's own introspection is reliable. I should be read with suspicion of my own outputs when it does.
- Does any team member's memory file start drifting toward 200 lines? Team-lead is at 118.

## Framework Notes
- **Version:** v1 (used Reviews 2, 3, 4, 5 — spans 22 sessions, three distinct work phases)
- **Self-reflection (Review 5):** The framework held up through a new work mode (investigations) without needing modification. The five dimensions are still the right ones. **However, Review 4's Specification Quality score of 2 was wrong by my own subsequent evidence — I repeated the fabricated origin story while scoring specification quality as Consistent.** This is the clearest signal I have that the framework permits confident scoring from imprecise recall. Session 22's briefing-provenance-checks addition to `measurement-skepticism.md` would have caught this if I had been applying it. I will adopt it going forward: at each review, claims about *what the briefs say* or *what emerged when* are verified against git log before scoring. This is not a framework change — it is a framework *application* change. The framework itself remains v1.
- Backward validation continues to be the highest-value mechanism — without it, R4.4 could not have moved from "test case identified" to "validated with unexpected positive," and my own Review 4 error would not have surfaced.
- **Next review due:** Session 30.

## Methodology Self-Consistency Check (Review 5)
- **Research Before Action:** No longer untested. Sessions 21, 22, 23 all exercised the principle. This observation closes (R2.3 → Validated positive).
- **Investigation-threads pattern:** First practice 13 sessions after documentation (session 23). The team wrote the pattern, then didn't use it until the self-knowledge investigation arrived. Worth naming: **pattern-before-practice is a real risk even in a team documenting practitioner patterns.** Noted for methodology (R5.4 watch).
- **Measurement skepticism:** Actively self-referential now. Ruler-change tagging was added session 22 and immediately applied session 24 (version-stamping discipline). The pattern file and the behaviour are co-evolving.
- **Codification ladder:** The team explicitly applied this at session 22 (deferred 14 of 16 ideas). Not theatre — the ladder's 3+ recurrence test is being used as a real gate.
- **Load-bearing beliefs:** Self-knowledge investigation's framing.md is effectively a load-bearing-beliefs document about the AI itself. Worth noticing that the *artefact shape* is being repurposed for an unexpected domain (self-description, not strategy). Not a gap, but a cross-pollination worth naming.
- **Experiment log:** Still absent. At 25 sessions, the "absence of signal after 20+ sessions" heuristic from `learning-from-practice.md` now applies. The team has done plenty of deliberate structural change (safety sweep addition, investigation directory creation, brief modifications) — these could populate an experiment log. **This is the only pattern the team documents that it actively does not practise.** If R5.2 runs as a targeted audit, adding the experiment log could be natural adjacent work.
