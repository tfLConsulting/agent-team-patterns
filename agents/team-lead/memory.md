# Team Lead — Memory

## Current State
- **Session:** 26
- **Date:** 2026-04-24
- **Phase:** Post-elevation — editorial + active investigation (AI self-knowledge). Shape B pilot 01 + scoring complete same session.
- **Last reconciled:** journal/2026-04-24-5.md

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

## External-scout idea backlog (session 22)

Ideas harvested from scouting a more mature external agent team. Each carries real evidence from that team's practice. **Do not adopt because interesting — adopt when we feel the pain it solves, or when the evidence case is strong enough to codify as a library pattern for others.**

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
  - **Asks still open, operator-declined:** 2 (Row 5 framing — "no idea"), 4 (tier structure for (b)-visible trait classes — "i don't know"). Resolved by deferral; rows stay as-is.
  - **Clean regime established:** sessions 22–26 are all 2026-04-24 under 4.7 post-all-three-bug-fixes. All post-session-26 in-repo evidence is in this regime.

## Next Session Focus

Depends on operator redirect. Two operator asks remain open (both operator-declined this session — Row 5 framing; tier structure for (b)-visible classes). Three asks answered session 26 late — registry scopes tightened and clean 4.7 regime established for sessions 22–26.

**If operator doesn't redirect**, candidate next steps in rough priority order:

1. **Row-2-terseness clean-regime retest** — new in session 26 late. With sessions 22–26 established as clean-regime 4.7 (post-v2.1.116, no bug 3), a targeted read of those sessions' journals against a 4.6 post-earlier-fixes baseline (the 2026-04-13 09:33 burst is the cleanest 4.6 comparison) would produce the first clean 4.6/4.7 terseness contrast in the investigation. Small bounded sub-agent task. This is the measurement that was blocked by "need 4.7 date" before; now unblocked.
2. **Cold-read Shape B variant (pilot 02)** — scorer's primary recommendation from session 26. Permitted reading reduced to `CLAUDE.md` + task spec only (no brief, no README, no methodology). Scored against same Shape A registry by a fresh sub-agent. Isolates primed vs. unprimed self-knowledge — the confound the first pilot exposed.
3. **Editorial roadmap item 4** — concrete worked example referencing `agents/` from methodology. Still overdue at 26 sessions. Clean non-investigation focus if a break from the investigation is wanted.
4. **Watch-signal light sweep** — coach flagged experiment log absence (R5.4 pattern-without-practice) and stale session counts ("18 sessions", "13 sessions", "20 sessions" in various methodology files where we're at 26). Either could be a light session.
5. **Outstanding flagged-not-fixed items from session 25 audit** — 4 items sit on external source-team evidence this repo cannot verify:
   - `methodology/investigation-threads.md:101` — source-team origin claim
   - `methodology/learning-from-practice.md:54` — "23% of sessions had no memory writes" (specific %)
   - `methodology/learning-from-practice.md:58` — source-team memory-experiments origin
   - `methodology/agent-team-guide.md:552` — "Claude Code's native Agent Teams feature shipped Feb 2026"
   These need source-team evidence or operator confirmation; not fixable from this repo alone.

Alternates (external-scout backlog, unchanged):
- Dual-gate retro items (small addition to `session-transaction-protocol.md`)
- Codification-ladder refinement with process-inventory-as-cost note

Do NOT adopt external-scout ideas or new patterns just because they're interesting. The protocol is: feel the pain, or have evidence strong enough to warrant codifying for others.
