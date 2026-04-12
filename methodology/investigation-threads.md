# Investigation Threads

Some questions don't resolve — they evolve. An agent team investigating why a system behaves a certain way, or whether a structural choice is working, or what's causing a recurring friction pattern, needs an artifact that matches the shape of that inquiry. Tasks complete. Research documents capture a point in time. Memory files track current state. None of these serve the specific need of a question that persists across sessions and accumulates evidence over weeks or months.

Investigation threads are persistent, hypothesis-centric documents that track evolving inquiry. They stay open as long as the question is alive, get updated with new evidence as sessions produce it, and branch when sub-hypotheses emerge. The key dynamic is hypothesis expansion: threads don't narrow toward a single answer so much as they expand understanding by accumulating evidence and revealing new questions.

## What Goes in a Thread

Each investigation thread is a standalone file with a consistent structure:

**Core hypothesis.** One or two sentences stating what the thread is investigating. This is the anchor — it may get refined over time, but it gives every future reader (human or agent) immediate context. Example: "Hot-tier memory above 150 lines degrades agent decision quality."

**Evidence for and against.** Dated entries recording observations that support, challenge, or complicate the hypothesis. Each entry cites the session or source. Evidence is not argument — it's observation. "Session 47: agent missed two priority items when memory was at 180 lines" is evidence. "This proves memory should be shorter" is interpretation, and belongs in the hypothesis refinement section.

**Hypothesis refinements.** As evidence accumulates, the original hypothesis often turns out to be too broad, too narrow, or slightly wrong. Refinements record how thinking has shifted. "Original hypothesis was about line count; evidence suggests the issue is information density, not length per se."

**Branching sub-hypotheses.** When a thread reveals a question distinct enough to warrant its own inquiry, it spawns a branch. The parent thread links to the child; the child links back. This is how investigation threads grow into a network rather than a single document.

**Related threads.** Cross-references to other active threads that touch adjacent questions.

**Status.** Active, dormant (no new evidence recently, but the question isn't resolved), or retired (the hypothesis has been sufficiently resolved, superseded, or rendered moot by changes). Retired threads are never deleted — they're historical records of how understanding evolved.

## Lifecycle

Investigation threads have a lifecycle distinct from tasks or issues.

**Opening.** A thread opens when an agent (or human) identifies a question that won't be answered in a single session and would benefit from structured evidence accumulation. The threshold is judgment-based: not every question warrants a thread. If the question can be answered by checking a few files or running one experiment, it doesn't need a thread. Threads are for sustained inquiry.

**Active accumulation.** During normal work, agents encounter evidence relevant to open threads. The discipline is noting it — adding a dated entry to the relevant thread rather than letting the observation live only in a session journal. This is the critical habit. Without it, threads become stale documents rather than living artifacts.

**Branching.** When evidence reveals a sub-question substantial enough to warrant its own evidence trail, a new thread is created and linked from the parent. The parent thread doesn't try to track everything — it delegates. A thread investigating "why do agents under-use warm-tier files" might branch into "do agents read warm files they didn't create" and "does warm-file naming convention affect discoverability."

**Dormancy.** A thread goes dormant when no new evidence has been added for an extended period but the question remains unresolved. Dormancy is a natural state, not a failure. Some questions require conditions that haven't arisen yet. Dormant threads should be periodically reviewed — not to force activity, but to decide whether the question is still worth tracking.

**Retirement.** A thread retires when the hypothesis has been sufficiently explored — validated, falsified, superseded by a better framing, or rendered irrelevant by structural changes. Retirement means the thread stops receiving new evidence. It stays in the file system as a record. The retirement entry should summarize what was learned.

Note the absence of "closed" or "completed." Investigation threads don't complete in the way tasks do. Even retired threads might be reopened if new evidence surfaces. The lifecycle is circular, not linear.

## Where Threads Live

Investigation threads are warm-tier artifacts in the three-tier memory model (see `three-tier-memory.md`). They are not loaded every session — that would bloat context. Instead, hot-tier memory references which threads are currently active, and agents pull the relevant thread file when they encounter related evidence or need to review the state of an inquiry.

A practical file structure:

```
investigations/
  memory-density-threshold.md
  warm-file-adoption.md
  session-length-impact.md
  ...
```

Each file is self-contained. An agent reading a thread for the first time should understand the hypothesis, the current state of evidence, and what sub-threads exist without needing to read anything else.

## How Threads Interact with Journals

Session journals and investigation threads serve complementary purposes. Journals capture the narrative of a single session — what happened, what was decided, what was observed. Threads capture longitudinal inquiry — how understanding evolves across many sessions.

The interaction is straightforward: journals are where evidence is first noticed; threads are where it accumulates. A journal entry might note "agent B ignored the handoff file again — third time this week." That observation belongs in the journal. It also belongs as a dated evidence entry in whatever investigation thread is tracking handoff reliability. The journal provides narrative context; the thread provides structured accumulation.

Without threads, longitudinal observations stay buried in individual journal entries. An agent trying to understand a pattern has to read weeks of journals and mentally reconstruct the evidence trail. Threads do that reconstruction in advance, incrementally.

## Anti-Patterns

**The stale document.** A thread is created with a hypothesis, initial evidence is recorded, and then nobody updates it. It sits in the file system looking like an active investigation but contributing nothing. The fix is the dormancy mechanism: if a thread hasn't received evidence in a defined period, explicitly mark it dormant and decide whether to keep watching or retire.

**The task list in disguise.** A thread that's really tracking work items rather than evolving a hypothesis. "Investigate performance" with entries like "fixed the slow query" and "added caching" is a task list, not an investigation thread. The test: does the thread have a hypothesis that evidence supports or challenges? If it's just tracking actions, it belongs in a backlog.

**The thread that never branches.** A thread that grows to cover too many sub-questions in a single document. This usually means the original hypothesis was too broad. When a thread exceeds a manageable size (the same principle as hot-tier memory — every line competes for attention), it's a signal to branch.

**Premature retirement.** Closing a thread because it's inconvenient or because early evidence seems conclusive. Investigation threads exist precisely for questions that need sustained attention. Retiring a thread after three evidence entries because "it seems like the answer is X" defeats the purpose.

**Thread proliferation.** Creating a thread for every question that arises. Not every question warrants the overhead of a persistent document. Reserve threads for questions that are genuinely longitudinal — spanning multiple sessions, requiring evidence accumulation, and important enough to justify the maintenance cost.

## When to Use Threads vs. Simpler Artifacts

Investigation threads add coordination overhead. They need to be maintained, reviewed, and eventually retired. Use them when:

- The question will persist across multiple sessions
- Evidence will arrive incrementally, not all at once
- The hypothesis is likely to evolve as evidence accumulates
- Multiple agents might encounter relevant evidence independently

Use simpler artifacts when:

- The question can be answered in one session (use the scratchpad)
- The answer is a fact to look up, not a hypothesis to test (use a reference file)
- The "investigation" is really a task with steps to complete (use a backlog item)
- Only one agent cares about the question (consider a note in that agent's warm-tier files)

## Hypothesis Expansion

The most important property of investigation threads is that they expand rather than narrow. A well-maintained thread typically ends with a richer understanding of the problem space than the original hypothesis anticipated. The initial hypothesis about memory line count might expand into understanding about information density, decision-critical versus reference information, pruning discipline, and the relationship between memory size and agent confidence.

This expansion is the thread's primary value. It's why threads persist rather than close — each answered question reveals new questions. The investigation into warm-file adoption might resolve the original hypothesis but uncover a pattern about file naming conventions that becomes its own thread.

Teams that resist this expansion — that try to keep threads narrowly focused on the original question — miss the mechanism that makes threads valuable. The original hypothesis is a starting point, not a boundary.

## Evidence Summary

The investigation thread pattern is **Practised (1 team, 150+ sessions)** for the core mechanism — persistent, hypothesis-centric documents that accumulate evidence across sessions. The pattern emerged organically from a running agent team and was subsequently recognized and structured.

The specific structural recommendations (file layout, status lifecycle, branching conventions) are **Hypothesis** — reasoned from the practice but not yet codified and tested as a formal system. The anti-patterns are drawn from observed failures, but the sample is small.

The claim about hypothesis expansion as the key dynamic is an observation from practice, not a tested mechanism. It's the most interesting claim in this pattern and the one most in need of deliberate investigation across different team contexts.

## Related Patterns

- `three-tier-memory.md` — where investigation threads sit in the memory hierarchy (warm tier)
- `learning-from-practice.md` — the experiment log is a related artifact; investigation threads track hypotheses, experiment logs track deliberate structural changes
- `coaching-framework.md` — coaching reviews may surface questions that warrant investigation threads (dimension 5: evolutionary fitness)
- `file-based-coordination.md` — threads are a file-based coordination artifact following one-way information flow principles
