# Team Lead — Memory

## Current State
- **Session:** 11
- **Date:** 2026-04-13
- **Phase:** Pattern extraction — mining live project experience into methodology
- **Last reconciled:** journal/2026-04-13-2.md

## Goals
- Curate and present the agent team methodology as a public patterns library
- Ensure all content is clean for public consumption (no internal refs)
- Evolve the patterns based on evidence and community feedback

## Team
| Agent | Status |
|-------|--------|
| team-lead | Active |
| team-coach | Active — Review 2 complete (session 9), next review session 14 |

### Candidate specialists (not yet created)
- **researcher** — strongest context-separation case, zero demand through 10 sessions. Activate when work requires external investigation.
- **curator** — tested informally, fails context-separation test at current scale.

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
- **New pattern: investigation-threads.md (session 10)** — living hypotheses, lifecycle, anti-patterns
- **New pattern: load-bearing-beliefs.md (session 10)** — strategy as testable hypotheses with kill conditions
- Public repo audit (session 11) — cleaned private project ref from journal/2026-04-03-6.md, added safety sweep to session close

## Editorial Roadmap (session 2, updated session 10)
Priority-ordered improvements from methodology review:

1. ~~Fix three-tier-memory.md~~ — **DONE (session 3)**
2. ~~Reconcile bootstrapping path~~ — **DONE (session 5)**
3. ~~Reduce guide/pattern redundancy~~ — **DONE (session 7)**
4. **Add concrete example** — reference agents/ as living worked example from methodology
5. **Add full citations to writing-for-ai.md** — strongest evidence claims lack verifiable references

### Pattern Extraction Backlog (from session 8 research, updated session 10)
Patterns identified in live project, not yet written:
- **Codification ladder** — MEDIUM, NEXT SESSION. When and how to formalize recurring patterns (brief → playbook → protocol → skill). Partially covered in coaching-framework.md; warrants standalone depth.
- **Session transaction protocol** — MEDIUM. Fault-tolerant session close with dirty-close detection and reconciliation.
- **Measurement skepticism** — MEDIUM. Systematic metric auditing. Related to load-bearing beliefs (the measurement trap).
- **Bounded mission teams** — MEDIUM. Teams with explicit sunset conditions.
- **Projects manifest** — LOW. Single-file project lifecycle tracking.

### File ratings from review (updated session 10)
- Strong: README, agent-team-guide, learning-from-practice, writing-for-ai, discipline-processes, coaching-framework, **investigation-threads** (new), **load-bearing-beliefs** (new)
- Adequate: three-tier-memory (improved session 3), role-design, file-based-coordination, brief-anatomy, self-modifying-briefs

### Exportable skills (`skills/`)
- `build` — 6-step subagent orchestration recipe, evidence-based
- `skill-building` — meta-skill for creating Claude Code skills

### Noted gaps (not yet prioritised)
Error recovery, human-agent interface, cost management, platform portability

## Next Session Focus
**Write codification-ladder pattern (when and how to formalize recurring patterns).**

The coaching-framework.md has a seed version (brief → playbook → protocol → skill with a two-part test). The standalone pattern should go deeper: lifecycle of formalization, examples of each tier, heuristics for when to promote, anti-patterns (premature formalization, formalization debt). If it writes quickly, also tackle session transaction protocol.
