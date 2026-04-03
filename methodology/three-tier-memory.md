# Three-Tier Memory

The default for AI agents is amnesia. Frameworks treat memory as a checkbox — "add a vector database." This doesn't work. The problem isn't storage, it's attention management. An agent drowning in retrieved context performs worse than one with no memory at all.

Three-tier memory solves this by matching information to urgency.

## The Tiers

**Hot (memory.md, <200 lines):** Loaded every session. Contains only what the agent can't function without — current priorities, recent decisions, next actions, key numbers. Ruthlessly pruned. Every line competes for the agent's attention, so unnecessary content directly degrades performance.

**Warm (topic files, scratchpad):** Not loaded by default, but the agent knows where to find it. Structured research, analysis, reference data. Pulled when relevant. The scratchpad is a special warm-tier file that's cleared each session — it's the workspace for in-progress thinking that hasn't been consolidated yet.

**Cold (archive/):** Historical records compressed into monthly files. Exists for search, not for regular consumption. An agent touches cold memory only when investigating something specific.

## Why Not Embeddings

Vector search introduces a retrieval problem on top of the memory problem. The agent doesn't control what gets surfaced. Wrong context at the wrong time causes failures — like the sales agent that gave a 50% discount because its retrieval pulled the wrong pricing information.

Plain files with intentional structure give the agent predictable, controllable access to its own knowledge. The agent knows what it knows and where to find it. No retrieval surprises.

## The Consolidation Ritual

At session end, everything in the scratchpad is triaged:
- **Promote to hot:** Will the next session need this? → Update memory.md
- **Promote to warm:** Is this enduring reference material? → Create/update a topic file
- **Archive to cold:** Is this historical record? → Compress into archive/YYYY-MM.md
- **Discard:** The default. Most session work doesn't need to persist.

After promotion, prune memory.md back under 200 lines. Test each line: "Will the next session need this?" If no, it goes.

## Maintenance Triggers

- memory.md exceeds 200 lines → prune immediately
- Topic file untouched 30+ days → consolidate or delete
- 3+ sessions since last archive write → compress recent work
- Enduring insight discovered → promote immediately, don't batch

## Why This Works

It mimics how effective humans manage information: keep the critical stuff top of mind, know where to find the rest, archive what's historical. The key insight is that the 200-line limit on hot memory forces discipline. Without it, memory files grow unbounded until the agent is effectively context-stuffing itself into confusion.

## Known Risks

The most documented failure mode is **pruning away load-bearing decisions.** During consolidation, a decision that shaped the project's architecture looks like historical context — it happened in the past, the next session probably won't re-make it. So it gets pruned. Then a later session encounters the same design question, has no record of the prior decision or its rationale, makes a different choice, and introduces a bug. Buttondown's AI agent hit exactly this: a key architectural decision was pruned during memory consolidation, re-litigated in a later session, and the different choice broke things.

The mitigation is to ask a harder question during pruning. Instead of just "will the next session need this?" also ask: **"If this were missing, could a future session make a decision that contradicts it?"** Decisions about what *not* to do, architectural constraints, and choices made after evaluating alternatives are almost always load-bearing. They don't look urgent, but removing them reopens resolved questions.

There's no perfect heuristic for this. Some decisions genuinely become irrelevant as projects evolve. The practical rule: when in doubt about whether a decision is historical context or a live constraint, keep it. The cost of a few extra lines in memory.md is lower than the cost of re-litigating a settled decision and getting it wrong.

## Related Patterns

**[Writing for AI Consumption](writing-for-ai.md)** — How you write memory content determines whether it survives pruning correctly. A concise, front-loaded decision record is easy to evaluate during consolidation; a buried aside in a narrative paragraph gets pruned because nobody recognises it as load-bearing. The writing patterns directly affect whether three-tier memory works or silently loses critical information.

**[Learning from Practice](learning-from-practice.md)** — The experiment log pattern provides a complementary approach to preserving decisions. Where hot memory captures what the agent needs *now*, the experiment log captures *why structural choices were made* — rationale, observed impact, and kill conditions. Decisions that get pruned from memory.md may survive in the experiment log, giving future sessions a warm-tier path back to the reasoning.
