# Investigation: AI Self-Knowledge

**Status:** Active
**Opened:** 2026-04-24 (session 23)
**Owner:** team-lead
**Entry point:** this file. Read `framing.md` for working synthesis, `research-01-frontier-survey.md` for source evidence.

## Core question

Can an agent team accumulate and act on structured self-knowledge about its AI models — observed predispositions, self-reported models, intervention effects — in a way that improves output and survives model-version churn? The value, shape, and cost of such a discipline are unknown.

## Why this exists

Operator direction (session 23): build intuition and evidence on whether a self-reflection framework for AIs helps. The operator has public prior work on AI-audience doc quality (https://github.com/tfLConsulting/chat-spec/blob/main/guidance/ai-doc-quality.md) but no framework for AI self-reflection and no intuition on its value.

The operator's five specific claims about the current AI collaborator (Claude via Claude Code):

1. Doesn't know documents written for AI consumption should be information-dense.
2. Doesn't know own predispositions.
3. Doesn't know how it will react to being told about them.
4. Strongly shaped by system prompts and the Claude Code environment.
5. Behaviour shifts substantially per model release (4.6 verbose, 4.7 terse to possibly unreasonable degree).

## Decomposition

"Self-knowledge" is ambiguous. Three distinct sub-questions:

| Label | Meaning | Tested by |
|---|---|---|
| (a) Observed predispositions | Behaviour patterns an outside observer documents | Operator logs, coach reviews, cross-project evidence |
| (b) AI-reportable self-models | What the model says about itself when asked | Prompted self-description compared to (a) |
| (c) Intervention effect | Does being told (a) or (b) change subsequent behaviour | Runtime A/B per model version |

Mapping operator's claims to decomposition:

| Claim | Sub-question |
|---|---|
| 1. Doesn't apply doc-density to AI-audience writing | (c), specific domain |
| 2. Doesn't know own predispositions | (b) is low-accuracy |
| 3. Doesn't know reaction to being told | (c) is unmeasured |
| 4. Shaped by Claude Code env | (a) has large environmental variance |
| 5. Version drift | (a)(b)(c) all reset per release |

## Current state

- Round-1 frontier research complete — `research-01-frontier-survey.md`
- Working framing + candidate shapes — `framing.md`
- Shape A first draft populated — `shape-a-registry-draft.md` (5 rows: 2 STRONG, 2 MODERATE, 1 WEAK; version-stamping conservative, pre-04-24 evidence tagged "version unknown" or "mixed")
- Shape B self-report pilot 01 + scoring complete — `shape-b-self-report-01.md`, `shape-b-scoring-01.md` (primed self-knowledge high, unprimed 0/5; cold-read variant recommended before additional Shape B runs)
- Version boundaries pinned (session 26 late) — Opus 4.7 GA 2026-04-16, v2.1.116 2026-04-20, v2.1.101 2026-04-10, bug 1 revert 2026-04-07, postmortem 2026-04-23. Sessions 22–26 are clean-regime 4.7 post-all-fixes. Shape A registry version-boundary section updated.
- No methodology file produced. Bar to publish a pattern remains: feel the pain, or evidence strong enough to codify for others.

## Candidate shapes (full rationale in framing.md)

| Shape | Description | Unclaimed-slot strength |
|---|---|---|
| A. Predisposition Registry | Per-version catalogue of observed traits | High practitioner gap, low intellectual novelty |
| B. Self-Calibration Protocol | Test (b) against (a) — score accuracy | Adjacent-novel |
| C. Intervention A/B Methodology | Direct public test of (c) | Clearest unclaimed research slot |
| D. Version-Drift Operational Hygiene | Release-boundary runbook | Integrator, low standalone |

Current inclination: A + C in combination, with B as cheap intermediate.

## Decision log

- **2026-04-24 (session 23):** Investigation opened. Frontier research commissioned and received. Operator redirected mid-session: capture as ongoing analysis, do not produce methodology changes this session. Files: `research-01-frontier-survey.md`, `framing.md`. Next action: tighten framing, pilot Shape A (registry skeleton + single worked entry on "4.7 terseness").
- **2026-04-24 (session 24):** Operator directed: gather evidence on my own biases with explicit version-drift caution. Shape A first-draft produced — 5 rows rather than a single "4.7 terseness" worked entry, because the evidence-mining pass surfaced more. Summary of findings in `framing.md` evidence log. Next action: operator to pin 4.7 release date (tightens every scope field); consider a targeted audit of the three methodology files carrying the fabricated origin story.
- **2026-04-24 (session 26):** Shape B self-report pilot 01 + scoring pass 01 complete (`shape-b-self-report-01.md`, `shape-b-scoring-01.md`). 4/5 surface coverage of Shape A rows but 0/5 unprimed coverage — every hit traces to priming the self-report author declared. The one clean Shape A miss (Row 4, principle-without-mechanism) is also the only Shape A row without a priming anchor in permitted reading. Decomposition failure: Shape B collapsed A's explicitly-split Rows 3 and 5 into one row. Two Shape B novel rows (overconfidence-in-self-report; mid-context attention loss with a Liu 2024 citation) surface trait classes the outside-observer methodology cannot reach — genuine complementary value, not self-knowledge per se. Calibration optimistic by one notch; WEAK absent across 8 rows. Shared-prior confound: A, B, and scorer all Opus 4.7 sub-agents same 24-hour window. Scorer's primary recommendation: run one cold-read Shape B variant (CLAUDE.md + task spec only, no brief, no README) before additional Shape B runs, to isolate primed vs. unprimed signal. No methodology change. Live operator asks extended to five: (1) 4.7 release date; (2) Row 5 framing; (3) v2.1.116 apply date on this machine; (4) do (b)-visible complementary trait classes belong in Shape A as a distinct tier, or a separate Shape-B registry? (5) is sycophancy active in team-lead's behaviour, per direct operator observation?
- **2026-04-24 (session 26, late):** Operator addressed 3 of 5 asks; bounded sub-agent looked up public dates. **Ask 1 answered:** Opus 4.7 GA 2026-04-16; Claude Code v2.1.116 2026-04-20; v2.1.101 2026-04-10; bug 1 revert 2026-04-07; postmortem 2026-04-23 (all Anthropic-owned sources, HIGH confidence). **Ask 3 answered:** v2.1.116 effective on this machine 2026-04-20 — sessions 22–26 are all post-all-three-bug-fixes under 4.7, a clean regime. **Ask 5 answered (direct (a)-observation):** "don't see you doing it since 4.7, may have been more of a characteristic of claude web than claude code" — Shape B Row 2 sycophancy overridden by operator observation; Shape A's original rejection stands. **Asks 2 and 4 declined by operator — resolved by deferral, Row 5 and tier-structure stay as-is.** Shape A registry's version-boundary analysis section fully rewritten with pinned dates; per-row re-mapping documented. Key new finding: bug 3 (100-word cap) was introduced *on the same day* as 4.7's release (2026-04-16), so the operator's "4.7 terse vs 4.6 verbose" baseline is confounded unless sourced from sessions 22–26 (the only clean 4.7 observations). Session 25-late's "verbosity cap explains week-before shift" speculation retracted — dates rule it out; the shift maps to v2.1.101 bug-2 fix (thinking restored, 2026-04-10) instead.

## Related methodology

- `methodology/writing-for-ai.md` — adjacent, symmetric (writing *for* AI, not *about* AI-itself)
- `methodology/self-modifying-briefs.md` — overlaps on (c) mechanism
- `methodology/load-bearing-beliefs.md` — adjacent on naming-what-guides-action
- `methodology/measurement-skepticism.md` — supplies evidence-strength vocabulary this investigation will need

## External anchors

- Operator's AI-doc-quality work: https://github.com/tfLConsulting/chat-spec/blob/main/guidance/ai-doc-quality.md
- Sustained research programmes on this question (detail in `research-01-frontier-survey.md`): Anthropic Interpretability (persona vectors, concept-injection introspection), Owain Evans' group (SAD benchmark, Tell Me About Yourself), Apollo Research (situational-awareness causality), Cognition (long-running-agent engineering), Flavell-to-LLM translators (MGV).
