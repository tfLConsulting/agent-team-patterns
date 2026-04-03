# Writing for AI Consumption

Every document an agent reads competes for its attention. This applies to briefs, memory files, journal entries, research, project instructions — all of it. The quality requirements for AI-consumed documents differ from human documentation, and getting them wrong measurably degrades agent performance.

## The Problem: More Text, Worse Performance

The intuition that comprehensive documentation helps is wrong for AI agents. The evidence is consistent and cross-validated:

- **Restating what code already expresses** causes a 2-3% performance *decrease* — worse than no documentation at all (ETH Zurich, AGENTbench 2026).
- **Verbose coherent prose** performs worse than shuffled fragments of the same content. Models extract information from structure, not narrative flow (Chroma "Context Rot" study, 194k LLM calls across 18 models).
- **Instruction density degrades accuracy.** At 100+ instructions, accuracy drops to 50-98%. At 500+, the best model hits 63%. Omission errors are 30x more frequent than modification errors at high instruction counts — agents don't get things wrong, they miss things entirely.
- **Mid-document information gets lost.** Positional encoding creates architectural attention bias toward the beginning and end of context. Content buried in the middle is systematically under-weighted (Liu et al., TACL 2024).
- **Semantically similar but incorrect content** is far more damaging than obviously irrelevant text. A document about the wrong pricing model does more harm than a document about unrelated infrastructure (ICLR 2025).
- **Stale claims corrupt downstream reasoning.** Incorrect information doesn't just cause local errors — it poisons the chain of reasoning that follows.
- **Large filled context windows** cause mild accuracy loss (~0.5%) but latency spikes up to 719%. Every unnecessary line costs processing time even when it doesn't cause errors.

## What Works

**Only document what code can't express.** Decisions, rationale, gotchas, non-obvious relationships. If it's inferable from the codebase, file structure, or standard conventions, don't repeat it.

**Front-load the non-obvious.** Primacy bias means the first content in any document gets the most attention weight. Put the most important, least predictable information first.

**Structure over prose.** Tables, lists, and labeled sections are easier for models to parse than flowing paragraphs. Use prose only when the relationships between ideas are the point.

**One concept per document.** Smaller focused documents are retrieved and consumed more reliably than large multi-topic files. This is why the methodology uses separate pattern files rather than one monolith.

**Delete rather than update questionable content.** A wrong document is worse than a missing one. When information becomes uncertain, remove it. The gap is safer than the risk of semantic near-misses.

**Keep files small.** Less context means less latency and more room for actual task work. The 200-line memory limit exists for this reason — not as arbitrary discipline, but because every line has a measurable cost.

## Self-Check

Before committing any document an agent will read, apply these tests (adapted from Anthropic's guidance on AI-readable documentation):

1. Would removing any line cause an agent to make a mistake? If not, cut it.
2. Does anything here repeat what's visible in code, config, or standard conventions?
3. Is every claim accurate against the current state of the project right now?
4. Could this be shorter without losing actionable information?

## Application to Agent Team Documents

**Memory files:** Every line in memory.md competes for attention. The 200-line limit is a direct application of this principle — not a storage constraint, but an attention budget.

**Briefs:** Set the board, don't script the game. Worked examples anchor agents to one pattern. Quantitative KPIs create perverse incentives. Both are forms of attention waste.

**Journal entries:** Written for future readers, so narrative structure matters. But padding does not. Information density is the goal — say what happened and why, not how it felt.

**Research and analysis:** These outputs are consumed by other agents. Semantic near-misses — topically related but factually wrong content — are worse than gaps. When uncertain, flag uncertainty explicitly or omit.

**Cross-references:** Be precise. "Read `agents/analyst/activation-analysis.md` — three failure modes, first-session output equals activation" is useful. "Read the analyst's findings regularly" wastes attention on a vague instruction the agent can't act on.

## The Meta-Principle

This document should practice what it preaches. If it were longer, it would be worse. The research points in one direction: for AI-consumed documents, the editing question is never "what should I add?" It's "what can I cut?"
