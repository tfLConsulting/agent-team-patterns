# Team Lead — Memory

## Current State
- **Session:** 18
- **Date:** 2026-04-13
- **Phase:** Elevation — strengthening Adequate-rated patterns to Strong
- **Last reconciled:** journal/2026-04-13-9.md

## Goals
- Curate and present the agent team methodology as a public patterns library
- Ensure all content is clean for public consumption (no internal refs)
- Evolve the patterns based on evidence and community feedback

## Team
| Agent | Status |
|-------|--------|
| team-lead | Active |
| team-coach | Active — Review 3 complete (session 14), next review session 19 |

### Candidate specialists (not yet created)
- **researcher** — strongest context-separation case. Zero demand through 16 sessions (all source material operator-supplied). Activate when work requires external investigation.
- **curator** — tested informally via general-purpose sub-agents. Fails context-separation test at current scale (12 pattern files). Cross-reference maintenance not yet burdensome. Watch for signal as library grows.

## Key Decisions
- Bootstrap with team-lead + team-coach only (following our own methodology)
- Journal-first protocol adopted (session 1)
- Methodology review complete (session 2) — all 10 files assessed
- Team review #1 (session 3) — no changes, team right-sized for editorial phase
- Retired team-coordination.md (session 4) — 4/5 sections redundant with guide
- Retired bootstrapping-protocol.md (session 5) — ~60/85 lines redundant with guide
- Added exportable skills (session 6) — build recipe + skill-building
- Resolved guide/pattern redundancy (session 7) — hybrid approach
- New pattern: discipline-processes.md (session 8) — 7 mechanisms from live project
- New pattern: coaching-framework.md (session 9) — five-dimension assessment, maturity ladder
- Team review #2 (session 9) — no composition changes, all dimensions level 1-2
- New pattern: investigation-threads.md (session 10) — living hypotheses, lifecycle, anti-patterns
- New pattern: load-bearing-beliefs.md (session 10) — strategy as testable hypotheses with kill conditions
- Public repo audit (session 11) — cleaned private project ref, added safety sweep to session close
- New pattern: codification-ladder.md (session 12) — four tiers, two-part test, promotion heuristics
- New pattern: session-transaction-protocol.md (session 13) — transaction metaphor, clean/dirty close
- Team review #3 (session 14) — no composition changes, Process Maturity up to solid Level 2
- New pattern: measurement-skepticism.md (session 15) — default prior, agent-team-specific fragility
- **Extraction backlog complete (session 16)** — 3/5 items written (Strong), 2 retired (insufficient evidence). Bounded-mission-teams retired (1 instance, contradicts own 3+ rule). Projects-manifest retired (implementation detail, not pattern).
- **Phase transition: Extraction → Elevation (session 16)** — strengthening Adequate patterns to Strong
- **Elevated: role-design.md (session 16)** — from 45 lines prescription to 121 lines field notes. Added evidence summaries, 5 anti-patterns, worked examples, cross-references, evolution observations.
- **Elevated: brief-anatomy.md (session 17)** — from 57 lines prescription to 127 lines field notes. Added evidence summaries (per-claim inline + summary section), 5 anti-patterns, worked examples from both agents, 7 cross-references. Honest about thin evidence (tool instructions = Hypothesis).
- **Elevated: file-based-coordination.md (session 18)** — from 66 lines prescription to 121 lines field notes. Added 4 failure modes (stale reads, broken contracts, race conditions, silent divergence), 4 anti-patterns, worked examples from both agents, 8 cross-references. Race conditions and broadcast files honestly marked Hypothesis.

## Elevation Roadmap (session 16)
Adequate patterns to elevate, priority-ordered by reference frequency and load-bearing importance:

1. ~~**role-design.md**~~ — **DONE (session 16)** — elevated to Strong
2. ~~**brief-anatomy.md**~~ — **DONE (session 17)** — elevated to Strong
3. ~~**file-based-coordination.md**~~ — **DONE (session 18)** — elevated to Strong
4. **self-modifying-briefs.md** — has decent examples but needs evidence summary, anti-patterns, cross-references
5. **three-tier-memory.md** — strongest Adequate (has Known Risks). Needs: evidence summary, reference to warm-tier falsification from learning-from-practice.md

## Editorial Roadmap (session 2, updated session 16)
Priority-ordered improvements from methodology review:

1. ~~Fix three-tier-memory.md~~ — **DONE (session 3)**
2. ~~Reconcile bootstrapping path~~ — **DONE (session 5)**
3. ~~Reduce guide/pattern redundancy~~ — **DONE (session 7)**
4. **Add concrete example** — reference agents/ as living worked example from methodology
5. **Add full citations to writing-for-ai.md** — strongest evidence claims lack verifiable references. Also exercises Research Before Action (untested 16 sessions, team-coach watch item).

### Extraction Backlog — COMPLETE (session 16)
Final scorecard:
- Codification ladder — WRITTEN (session 12), Strong
- Session transaction protocol — WRITTEN (session 13), Strong
- Measurement skepticism — WRITTEN (session 15), Strong
- Bounded mission teams — RETIRED (session 16), 1 instance evidence
- Projects manifest — RETIRED (session 16), implementation detail

### File ratings from review (updated session 16)
- Strong: README, agent-team-guide, learning-from-practice, writing-for-ai, discipline-processes, coaching-framework, investigation-threads, load-bearing-beliefs, codification-ladder, session-transaction-protocol, measurement-skepticism, **role-design** (elevated session 16), **brief-anatomy** (elevated session 17), **file-based-coordination** (elevated session 18)
- Adequate: three-tier-memory (improved session 3), self-modifying-briefs

### Exportable skills (`skills/`)
- `build` — 6-step subagent orchestration recipe, evidence-based
- `skill-building` — meta-skill for creating Claude Code skills

### Noted gaps (not yet prioritised)
Error recovery, human-agent interface, cost management, platform portability

## Next Session Focus
**Elevate self-modifying-briefs.md.** Fourth on the elevation roadmap. Has decent examples from a working system but needs evidence summary, anti-patterns, cross-references, and honest assessment of tested vs. hypothesised claims. After self-modifying-briefs, one Adequate pattern remains (three-tier-memory) before the elevation roadmap is complete.

Team-coach review #4 due at session 19. Watches: cross-reference maintenance burden (R3.3), extraction backlog exhaustion (R3.4 — now resolved), Research Before Action (untested 18 sessions).
