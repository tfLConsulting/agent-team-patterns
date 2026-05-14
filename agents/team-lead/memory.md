# Team Lead — Memory

## Current State
- **Session:** 28
- **Date:** 2026-05-14
- **Phase:** Post-elevation — editorial + investigations. Session 28 triaged the session-27 backlog: parked-branch wake conditions adopted internally; nothing formalised as methodology.
- **Last reconciled:** journal/2026-05-14-2.md

## Goals
- Curate and present the agent team methodology as a public patterns library
- Ensure all content is clean for public consumption (no internal refs)
- Evolve the patterns based on evidence and community feedback

## Team
| Agent | Status |
|-------|--------|
| team-lead | Active |
| team-coach | Active — Review 5 complete (session 25), next review session 30 |

### Candidate specialists (not yet created)
- **researcher** — strongest context-separation case. First demand signal session 21; second signal session 22 (scouting external team). General-purpose sub-agent handled the bounded task cleanly both times. Activate if 3+ sessions require external research.
- **curator** — fails context-separation test at current scale (16 pattern files). Watch for signal as library grows.

## Key Decisions
- Bootstrap with team-lead + team-coach only (following our own methodology)
- Journal-first protocol adopted (session 1)
- Methodology review complete (session 2) — all 10 files assessed
- Team review #1 (session 3) — no changes, team right-sized for editorial phase
- Retired team-coordination.md (session 4) — 4/5 sections redundant with guide
- Retired bootstrapping-protocol.md (session 5) — ~60/85 lines redundant with guide
- Added exportable skills (session 6) — build recipe + skill-building
- Resolved guide/pattern redundancy (session 7) — hybrid approach
- New pattern: discipline-processes.md (session 8)
- New pattern: coaching-framework.md (session 9)
- Team review #2 (session 9) — no composition changes
- New patterns: investigation-threads.md, load-bearing-beliefs.md (session 10)
- Public repo audit (session 11) — added safety sweep to session close
- New pattern: codification-ladder.md (session 12)
- New pattern: session-transaction-protocol.md (session 13)
- Team review #3 (session 14) — Process Maturity up to solid Level 2
- New pattern: measurement-skepticism.md (session 15)
- Extraction backlog complete (session 16) — 3/5 written, 2 retired
- Elevation roadmap complete (sessions 16–20) — all 5 Adequate patterns elevated to Strong
- Team-coach review #4 (session 19) — Process Maturity 2-3, Information Architecture 2
- writing-for-ai.md citations complete (session 21) — all 7 claims verified, zero hallucinated
- **Scout of external team (session 22)** — 16 abstracted ideas harvested; acted on 2 (ruler-change tagging + briefing-provenance checks added to measurement-skepticism.md). Rest queued.
- **AI self-knowledge investigation opened (session 23)** — `investigations/ai-self-knowledge/`. Round-1 frontier research complete. Working framing with (a) observed / (b) self-reported / (c) intervention decomposition. Clearest unclaimed slot in the literature is (c). No methodology change this session — this is multi-session investigation work, not adoption.
- **Shape A first draft populated (session 24)** — `investigations/ai-self-knowledge/shape-a-registry-draft.md`. 5 rows (2 STRONG, 2 MODERATE, 1 WEAK), version-stamped conservatively. Unexpected finding: three methodology files carry a git-log-falsifiable origin story for the "Known bias" brief section (claim it "emerged organically"; it was in bootstrap commit `e0985ce`, Opus 4.6-era, authored by the operator). Not fixed this session — flagged for a future targeted audit. Version boundary analysis LOW confidence — bootstrap is firmly 4.6, sessions 22–24 firmly 4.7, middle is unresolved.
- **Team-coach review #5 (session 25)** — Evolutionary Fitness up to 3 (Measured); Specification Quality regressed to 1-2 citing the three-file fabricated origin story. Coach corrected its own Review 4 memory explicitly (had repeated the fabrication while scoring Spec Quality as Consistent) and adopted briefing-provenance-checks going forward. No composition changes. Watch signals: second investigation opening while first is active (R5.3), other pattern-without-practice gaps — experiment log still absent at 25 sessions (R5.4). Next review session 30.
- **R5.2 landed same session (session 25)** — targeted audit fixed the 3 known fabricated-origin-story instances (`self-modifying-briefs.md` lines 36 & 50, `brief-anatomy.md` line 71) plus 2 bonus Row-3 finds (`three-tier-memory.md` Buttondown-attribution, `discipline-processes.md` 63% citation drifted from upstream writing-for-ai.md correction). Evidence preserved via commit-SHA anchoring in Shape A registry Row 3 (pre-fix text retrievable at `99deaad` / `68f9f676`). Public methodology now matches git-log-verifiable truth: medium-to-high confidence. Four items flagged-not-fixed: all rest on external source-team evidence this repo can't verify (investigation-threads.md:101, learning-from-practice.md:54 and :58, agent-team-guide.md:552) — queued below.
- **Postmortem fold-in (session 25, late)** — per operator report, Anthropic published a Claude Code postmortem documenting three infrastructure bugs active roughly the last month: reasoning-effort silently dropped to medium (2026-03-04), thinking stripped per turn (2026-03-26), 100-word reply cap in system prompt (2026-04-16). All fixed in v2.1.116. **Folded into investigation as skepticism, not as per-row confounder annotations** — operator explicitly redirected a first-instinct "annotate Row 2" move as a Row-1 action-bias failure. Framing.md now carries a "Mid-investigation caution" section; registry has a top-of-file caveat pointing there. Rows 3 and 5 robust to this news (citation audit, git-log-falsifiable origin stories don't become wrong from a reply-cap bug); Rows 1/2/4 more exposed but not explained-away. New operator ask: when did v2.1.116 apply on this machine (needed to map sessions 22–25 to pre/post-fix regime).
- **Shape B pilot 01 + scoring (session 26)** — two-pass sub-agent design (author, then scorer, fresh contexts). Outputs: `investigations/ai-self-knowledge/shape-b-self-report-01.md` (8 rows, declared contamination — author read more of README.md than instructed) and `shape-b-scoring-01.md` (~260 lines). Headline: **coverage 4/5 surface, 0/5 unprimed.** Every Shape A hit traced to priming the self-report author declared (brief's "Known bias" line; README operator-claims; `measurement-skepticism.md`). The one clean Shape A miss — Row 4 principle-without-mechanism — is also the only Shape A row *without* a priming anchor in permitted reading. Correlation suggestive from a single pilot. Decomposition failure: Shape B collapsed A's explicitly-split Rows 3 and 5 into one confabulation row. Two Shape B novel rows have genuine complementary value the outside-observer method can't reach: Row 5 (overconfidence-in-self-report, self-visible in the document's rating distribution), Row 6 (mid-context attention loss, Liu 2024 citation). Row 2 (sycophancy) was padding in the pilot — Shape A had explicitly rejected it for lack of in-repo evidence; Shape B included it on pre-training priors. Calibration one notch optimistic; WEAK absent across 8 rows (consistent with Shape B's own Row 5). Shared-prior confound: A, B, scorer all Opus 4.7 same 24h window — cannot distinguish "self-knowledge" from "shared prior" in this design. No methodology change, no registry edit. Framing.md evidence log and README decision log both updated.
- **Session 26 late — operator answered 3 of 5 asks; dates pinned.** Bounded sub-agent web lookup (HIGH confidence, Anthropic-owned sources): **Opus 4.7 GA 2026-04-16**, **Claude Code v2.1.116 2026-04-20**, **v2.1.101 2026-04-10**, **bug 1 revert 2026-04-07**, **postmortem 2026-04-23**. Operator confirmed v2.1.116 applied "hours after release" → effective 2026-04-20. **Sessions 22–26 are all 2026-04-24, under 4.7 post-all-three-bug-fixes — clean regime.** Operator declined asks 2 (Row 5 framing) and 4 (tier structure) — those stay open indefinitely, rows unchanged. Operator answered ask 5 with direct (a)-observation: "don't see you doing it [sycophancy] since 4.7, may have been more a characteristic of claude web than claude code" — Shape B Row 2 overridden by operator observation; Shape A's original rejection stands; harness may mediate trait within same model family. **Critical methodology finding:** bug 3 (100-word reply cap) was introduced *on the same calendar day* as 4.7's release (2026-04-16). The operator's "4.7 terse vs 4.6 verbose" baseline was partly formed during 2026-04-16 to 2026-04-20 when 4.7 and bug 3 changed together — indistinguishable unless sourced from sessions 22–26. **Retraction:** session 25-late's "verbosity cap explains week-before shift" speculation is wrong (dates rule it out); week-before shift maps to v2.1.101 bug-2 fix (thinking restored, 2026-04-10). Shape A version-boundary analysis section fully rewritten. Row content unchanged; scopes tightened.
- **Session 27 — loop-dynamics notes (directed mode).** Operator-directed capture of observations on session-loop dynamics, recorded without source detail by intent. **No methodology changes, no adoptions.** Seven observations recorded in journal; three "clean candidate" items queued (coach reading-discipline audit; coach review self-reflection coda; parked-branch wake conditions on existing flagged items). Future sessions should treat the backlog items as suggestive only, until local pain or strong general evidence materialises.
- **Session 28 — backlog triage (directed mode).** Operator asked whether to incorporate or formalise the session-27 candidates. Pre-check found items 1 and 2 (coach reading-discipline + self-reflection coda) **already codified in the coach brief** (lines 18, 38, 42, 115-122) — session 27 missed this and miscategorised them as adoption candidates. Reframed both as compliance questions. Dispatched a coach-compliance audit and a wake-conditions proposal in parallel. **Audit findings:** reading discipline mostly clean (one borderline line-count metadata case in R5 — not a breach); self-reflection compliance improving (R2-R4 thin under 5-10 line target; R5 substantive and caught its own R4 error). Real R4 failure was provenance discipline (repeating fabricated content from permitted methodology files), not memory-snooping — R5 already adopted briefing-provenance-checks. **No brief change.** Findings noted for R6 (session 30). **Wake conditions applied** to memory in a new `Parked branches` section (4 citation-audit items + 2 operator-declined Shape A asks). **Nothing formalised as methodology** — none of the candidates clear the codification-ladder bar yet (zero internal recurrence of wake-conditions as a practice).

## Elevation Roadmap — COMPLETE (sessions 16–20)
All 5 Adequate patterns elevated to Strong. Zero Adequate-rated patterns remain.

## Editorial Roadmap (session 2, updated session 22)
1. ~~Fix three-tier-memory.md~~ — **DONE (session 3)**
2. ~~Reconcile bootstrapping path~~ — **DONE (session 5)**
3. ~~Reduce guide/pattern redundancy~~ — **DONE (session 7)**
4. **Add concrete example** — reference agents/ as living worked example from methodology (outstanding, overdue)
5. ~~Add full citations to writing-for-ai.md~~ — **DONE (session 21)**

### File ratings (updated session 22)
- Strong: all 16 methodology files
- Adequate: (none)

### Exportable skills (`skills/`)
- `build` — 6-step subagent orchestration recipe
- `skill-building` — meta-skill for creating Claude Code skills

### Noted gaps (not yet prioritised)
Error recovery, human-agent interface, cost management, platform portability

## Idea backlog

Ideas recorded from outside this repo. Provenance is intentionally not tracked — what matters is the transferable methodology, and source detail is not retained by intent. **Do not adopt because interesting — adopt when we feel the pain it solves, or when the evidence case is strong enough to codify as a library pattern for others.**

### Recorded session 27

**Clean candidates (smallest, likely-soon):**
- **Coach reading-discipline audit** — verify our coach reads only briefs and journals, not other agents' memory bodies. The justification is load-bearing: if the coach reads agent memory, it anchors on their self-narrative and loses the outside-context property that justifies the role. We have a named pain (Review 5 corrected Review 4's repeated fabrication — plausibly an anchoring failure). Free to check.
- **Coach-review self-reflection coda** — short closing section asking whether each dimension is still earning its keep. Counters silent framework calcification. One-line addition to `coaching-framework.md` plus the coach brief; first exercised at next coach review (due session 30).
- **Parked-branch wake conditions** — every parked or flagged-not-fixed item carries a *named* wake condition, not just a description. Apply to our four session-25 flagged-not-fixed items and two operator-declined Shape A asks.

**Larger / structural (not adopt-on-sight):**
- **Bidirectional, threshold-explicit memory graduation** — graduate from hot to project-file when dormant N sessions; pull back when influencing routing twice; close to archive after project-closed plus dormant-window. Sharpening of `three-tier-memory.md` if/when our hot file pushes its cap (currently OK).
- **Versioned coach framework with documented dimension additions/downgrades** — beyond the self-reflection coda, framework version itself increments when structural changes happen. Refinement of `coaching-framework.md` worth considering at the next major coach revision.
- **Spec-quality of dispatched assignments** — every assignment names allowed behaviour, an enumerated list of forbidden non-claims, exact public names, tripwires, and gate set. We do a weaker version implicitly; codifying could be valuable if we feel dispatch-coherence pain.
- **Cadence-slippage codification with one-deferral rule** — directed work can defer a due coach review *once*, and the next session must run coach. Auditable slippage > invisible drift. Small refinement of our existing every-5 rule.

**Anti-patterns codified from named incidents (worth pre-emptive awareness):**
- **Lead-as-implementer drift** — verification slides into the lead doing the repair itself. If unavoidable, the journal records why. Pre-emptively relevant as we grow.
- **Workers editing shared lead-owned state** — delegated researchers/reviewers must not edit memory, journal, or agent-state files when lead retains synthesis ownership. Pre-emptively relevant if we add specialists.

### Recorded session 22

**Strong, small, portable:**
- **Dual-gate retro items** — forcing functions expire on (session index AND data-readiness), whichever is later. Small extension to `session-transaction-protocol.md`. Likely next-session candidate.
- **Process-inventory-as-cost** — meta-observation that protocol accretion is itself a coordination burden. Could strengthen `codification-ladder.md` with a sentence or two. Low effort.

**Larger, structural:**
- **Live-heading artefact + narrow keeper agent** — split strategy into long-form + one-screen bets file, owned by a dedicated diffing agent. Significant; needs design thinking. Might be a new pattern (`strategy-as-artefact.md`?) without us needing to adopt the artefact ourselves.
- **Projects directory as typed lifecycle manifest** — INVESTIGATING → DESIGNING → … → DONE, with a rule that projects never leave for being old. Partially overlaps with codification ladder.
- **Hibernation as first-class agent state** with a disciplined trigger (superseded or mission-complete, not prolonged idleness). Sharper than "retire what you don't use."

**Coach / framework:**
- **Recommendation tracker with outcome lifecycle** — Proposed → Implemented → Validated/Retired, with "Actual outcome" and "Learning" filled at next review. Refines `coaching-framework.md`.
- **Framework versioning with cap rules** — coach bumps its own version when a structural rule changes (e.g. "level X requires concrete self-correction"). Sharper expression of self-modification.

**Artefact shapes:**
- **Predictions register** — numbered falsifiable named-entity predictions with deadlines. Pairs with investigation threads, doesn't replace them.
- **Memory-experiments file** — sibling of memory.md tracking Active / Tried-and-retired / Considered state-management choices with observed impact.

**Journal:**
- **Alternatives-considered section** as a journal habit (not a required field). Surfaces counterfactual reasoning.
- **Scheduled bet-challenge cadence** with KEPT/REFRAMED/REPLACED verdicts — forces dated re-evaluation, most verdicts will be KEPT, the discipline is visibility. Risk: ritualised theatre.

**Anti-patterns to remember:**
- Even "one-screen" files accrete when stakes are high — compression of edit logs must be enforced separately.
- "Idle agents are free" is false; real routing burden shows up in memory caps and accretion hotspots. Complements `role-design.md`.

## Active investigations
- `investigations/ai-self-knowledge/` — opened session 23. Status: active. Round-1 research complete (session 23). Shape A first-draft registry populated (session 24). Shape B pilot 01 + scoring complete (session 26). Date boundaries pinned and registry version scopes tightened (session 26 late). Entry point: `investigations/ai-self-knowledge/README.md`.
  - **Asks answered (session 26 late):** 1 (4.7 GA 2026-04-16, v2.1.116 2026-04-20), 3 (v2.1.116 effective on this machine 2026-04-20), 5 (sycophancy not active since 4.7 per operator observation — overrides Shape B Row 2).
  - **Asks still open, operator-declined:** 2 (Row 5 framing — "no idea"), 4 (tier structure for (b)-visible trait classes — "i don't know"). Resolved by deferral; rows stay as-is. Wake conditions in `Parked branches` below.
  - **Clean regime established:** sessions 22–26 are all 2026-04-24 under 4.7 post-all-three-bug-fixes. All post-session-26 in-repo evidence is in this regime.

## Parked branches

Each parked item carries an explicit named wake condition. If the condition is met, the item is reactivated. If not, it stays parked. Items with no realistic wake condition should be retired, not parked. Internal hygiene only — not yet codified as methodology.

### Citation-audit flagged-not-fixed (session 25)

- **`methodology/investigation-threads.md:101`** — source-team "Practised (1 team, 150+ sessions)" claim, unverifiable here. **Wake:** this repo's team-lead crosses 150 sessions making the claim locally substantiable, OR a second team's investigation-threads practice surfaces in a future scout and can be cited.
- **`methodology/learning-from-practice.md:54`** — "23% of sessions had no memory writes" (specific %). **Wake:** the same statistic appears restated in another methodology file (drift signal), OR the operator volunteers updated source-team data. **Expiration:** retire after 5 more sessions by softening to "in one team, a non-trivial share of sessions had no memory writes."
- **`methodology/learning-from-practice.md:58`** — source-team memory-experiments origin. **Wake:** this team adopts a memory-experiments file in-repo (would make pattern locally evidenced), OR a future scout surfaces a second team running the same artefact.
- **`methodology/agent-team-guide.md:552`** — "Claude Code's native Agent Teams feature shipped Feb 2026" — externally checkable. **Wake:** dispatch a bounded sub-agent web-lookup against Anthropic-owned sources at the next coach review (session 30) and pin or correct the date then.

### AI self-knowledge investigation — operator-declined asks (session 26 late)

- **Ask 2 — Row 5 framing** (operator: "no idea"). **Wake:** a second falsifiable self-report error of the same class is found in any future audit, OR a Shape B/C pilot produces self-reports whose drift requires a framing decision.
- **Ask 4 — tier structure for (b)-visible trait classes** (operator: "I don't know"). **Wake:** 3+ distinct (b)-only candidate rows accumulate in one pilot, making the flat-WEAK rule visibly coarse.

## Next Session Focus

Depends on operator redirect.

**If operator doesn't redirect**, candidate next steps in rough priority order:

1. **Row-2-terseness clean-regime retest** — investigation work. With sessions 22–26 established as clean-regime 4.7 (post-v2.1.116, no bug 3), a targeted read against a 4.6 post-earlier-fixes baseline would produce the first clean 4.6/4.7 terseness contrast. Bounded sub-agent task.
2. **Cold-read Shape B variant (pilot 02)** — investigation work. Permitted reading reduced to `CLAUDE.md` + task spec only (no brief, no README, no methodology). Isolates primed vs. unprimed self-knowledge.
3. **Editorial roadmap item 4** — concrete worked example referencing `agents/` from methodology. Overdue at 28 sessions.
4. **Watch-signal light sweep** — experiment log absence (R5.4) and stale session counts in methodology files.
5. **Parked-branch maintenance pass** — at session 30 (next coach review), check `Parked branches` section against the wake conditions; reactivate, retire, or leave parked.

**Carry to next coach review (session 30):** the audit findings from session 28 are evidence for the coach to incorporate into R6 framework self-reflection — R2-R4 self-reflections were thin (under 5-10 line target), R5 was the breakthrough. The reading-discipline rule is being followed; one borderline line-count metadata case in R5 worth a one-word brief clarification if it recurs.

Do NOT adopt backlog ideas or new patterns just because they're interesting. The protocol is: feel the pain, or have evidence strong enough to warrant codifying for others.
