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
