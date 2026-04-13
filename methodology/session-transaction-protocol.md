# Session Transaction Protocol

Sessions are the fundamental unit of agent team work. Every other pattern — memory, coordination, self-modification — depends on sessions opening and closing reliably. But sessions fail. Context windows fill up. Connections drop. Operators walk away mid-session. Without a transaction model, these failures corrupt state: memory doesn't reflect reality, journal entries trail off mid-thought, and the next session opens into a landscape it can't trust.

The fix is treating sessions like database transactions. Open, do work, commit. The commit step is updating persistent state — memory, journal, cross-file references. Work done but not committed is dirty. And like database transactions, the interesting engineering isn't the happy path. It's what happens when the commit never comes.

## Clean Close Protocol

A clean close is the ordered sequence that constitutes a valid session commit. The order matters because each step depends on the previous one, and because partial completion of the sequence must leave the system in a recoverable state.

**1. Finalize the journal entry.** The journal has been accumulating throughout the session (see "Journal-First" below). At close, add the closing sections: outcomes achieved, practice observations, and what the next session should focus on. The closing section is what distinguishes a complete journal from an interrupted one — it's the signal that the session reached its natural end rather than being cut off.

**2. Update memory with current state.** This is the commit. Memory is what the next session reads first. It must reflect the actual state of the project after this session's work, not the state at session open. Include a reconciliation pointer — `Last reconciled: journal/YYYY-MM-DD.md` — so the next session can verify currency without reading the full journal archive. The pointer is cheap to write and expensive to lack.

**3. Cross-file updates.** Any other files that need to reflect this session's decisions — brief modifications, strategy updates, backlog changes. These happen after the memory update because they're downstream of the state that memory records.

The memory update is the commit point. If the journal is finalized but memory isn't updated, the next session can still recover — it reads the journal, finds the closing section, and reconstructs what memory should say. If memory is updated but the journal isn't finalized, the next session has an accurate starting point but an incomplete record. Both are recoverable. The worst case is when neither happens — no journal closing, no memory update — and recovery depends entirely on the journal-first pattern having captured enough in-progress notes.

### Minimum Viable Close

Not every session gets the luxury of a full close sequence. Context windows have hard limits. Sometimes the agent has 500 tokens left and needs to decide what to do with them.

The minimum viable close is a memory update. One paragraph: what was accomplished, what state the work is in, and what should happen next. If the choice is between a polished journal closing section and a raw memory update, choose memory every time. Memory is what the next session reads. The journal is the backup.

This is a pragmatic concession. The journal-first pattern means the journal already has partial records of the session's work. A memory update without a journal closing section leaves the system in a state where the next session can function. A journal closing section without a memory update leaves the system in a state where the next session has to do detective work.

## Journal-First as Write-Ahead Log

In database systems, a write-ahead log records what's about to happen before it happens. If the system crashes mid-operation, the log provides a recovery record — you can see what was intended, what was in progress, and what completed.

The journal entry serves the same function. It starts at session open, not session close. The agent creates the journal file, writes the date, states the session focus, and begins recording as work progresses. Every significant decision, finding, or direction change gets noted in the journal as it happens.

This means the journal is always ahead of memory. Memory reflects the state at the last clean close. The journal reflects what's happening right now. If the session dies — context window exhausted, connection lost, operator disappeared — the journal contains a partial but real record of what was attempted and what was discovered.

The alternative — writing the journal at session close — is the most common failure mode in session design. If the session closes cleanly, a journal-at-close approach works fine. If the session doesn't close cleanly, everything is lost. No record of what was tried, what was learned, what partially worked. The next session starts completely blind to the interrupted work.

Journal-first costs almost nothing. The overhead of writing notes as you go is trivial compared to the cost of losing an entire session's context on a dirty close. And the journal entries written incrementally tend to be better than those written from memory at session end — they capture the reasoning in the moment rather than a post-hoc reconstruction.

### What to record as you go

Not everything needs to go in the journal mid-session. The goal is a recovery record, not a transcript. Record:

- **Decisions and their reasoning.** "Chose X over Y because Z." If the session dies after this point, the next session knows the decision was made and why.
- **Findings that won't be obvious from the files.** If the agent researched something and the research shaped its approach, note the key findings. The research itself might be in a scratchpad that gets cleared, but the journal preserves the conclusions.
- **State transitions.** "Finished phase 1, moving to phase 2." If the session dies mid-phase-2, the next session knows phase 1 completed.
- **Dead ends.** "Tried approach A, didn't work because B." This prevents the next session from re-attempting the same approach — a common failure when sessions don't record their negative results.

## Dirty Close Detection

A dirty close is any session that didn't complete the clean close protocol. The next session's first job is detecting whether the previous session closed cleanly. This is not optional — skipping dirty close detection means operating on potentially corrupt state.

### Detection signals

**Memory pointer mismatch.** Memory's "last reconciled" pointer names a journal file. If a newer journal file exists — one that's dated after the pointer — the previous session opened and wrote a journal but never updated memory. This is the most reliable signal because it's structural: two files that should agree and don't.

**Incomplete journal.** The latest journal file exists but has no closing section — no outcomes, no "next session" note. This means the session started (journal-first) but didn't reach clean close. The journal contents reveal how far the session got.

**Uncommitted file changes.** `git diff` and `git status` show modified or untracked files that don't correspond to what memory describes. If memory says "completed the review of pattern X" but there are uncommitted changes to pattern Y, something happened that memory doesn't account for.

**Stale scratchpad.** The scratchpad file contains work-in-progress from a prior session. Since scratchpads are cleared at session open, a non-empty scratchpad at the start of a new session (before clearing) indicates the previous session was using it. Combined with other signals, this suggests interrupted work.

**No single signal is conclusive.** A memory pointer mismatch with a complete journal might mean the agent just forgot the pointer update — annoying but not a real dirty close. An incomplete journal with no file changes might mean the session opened, started the journal, and then did nothing before being interrupted. The signals are read together, not individually.

### A concrete example

Session 12 opens. The agent reads memory and finds `Last reconciled: journal/2026-04-10.md`. But there's a file `journal/2026-04-11.md`. The agent reads that file and finds a header, a session focus ("revise the coordination pattern"), some mid-session notes about restructuring sections 3 and 4, and then nothing — no outcomes, no closing section. `git status` shows uncommitted changes to `methodology/file-based-coordination.md`.

The picture is clear: session 11 started work on revising the coordination pattern, got partway through, and died without closing. The journal tells the story up to the point of interruption. The git diff shows the actual work product. Memory is stale — it reflects the state before session 11.

## Reconciliation

Once a dirty close is detected, the current session must reconcile before doing its own work. Reconciliation means bringing memory and journals into a consistent state that accurately reflects reality.

### The reconciliation sequence

**1. Read the incomplete journal.** Understand what was attempted, how far it got, and what the interrupted session's intent was. The journal-first pattern means this record exists even though the session didn't close.

**2. Check the actual state of the work.** `git diff` and `git status` show what files were actually changed. Read the changed files. Compare what was done against what the journal says was intended. Sometimes the work is further along than the journal records — the agent did work after its last journal note. Sometimes the journal records intent that was never executed.

**3. Decide: complete or start fresh.** This is a judgment call. If the interrupted work is nearly done and the direction looks sound, completing it is efficient — the cost of the dirty close is just the reconciliation overhead. If the work is early-stage or the direction looks questionable, starting fresh might be better. The journal's reasoning notes help make this call: if the interrupted session recorded why it chose its approach, the current session can evaluate that reasoning rather than just inheriting the approach blindly.

**4. Update memory.** Whether completing or starting fresh, memory must reflect the actual current state. This means describing what the interrupted session accomplished (or partially accomplished), what was kept and what was discarded, and what this session will do. The reconciliation pointer gets updated to the current journal file.

**5. Note the reconciliation.** The current session's journal should record that a dirty close was detected and what was done about it. This creates an audit trail — if future sessions notice inconsistencies, the reconciliation entry explains when and how state was repaired.

### The temptation to skip reconciliation

When the previous session's work looks straightforward and the dirty close seems minor, the temptation is to just update the memory pointer and move on. This is usually a mistake. Minor dirty closes accumulate. A memory pointer that's off by one session is a small debt. Three sessions of minor dirty closes without reconciliation can leave memory describing a state that bears little resemblance to reality.

The discipline is: always reconcile, even when it seems unnecessary. The cost of reconciliation when nothing is wrong is a few minutes of checking. The cost of skipping reconciliation when something is wrong is a session built on false assumptions.

## Progressive Commit

The clean close protocol describes a single commit at session end. But a session might run for thousands of tokens across many tasks. If the commit only happens at the end, there's a large window where a failure loses everything.

Progressive commit reduces this window by committing state incrementally as work completes. Each completed sub-task gets a partial commit — a journal update, and where appropriate, a memory note.

### What progressive commit looks like in practice

An agent working through three tasks in a session:

- **Task 1 completes.** Update the journal with task 1 outcomes. If task 1 changed the project state significantly, update memory with a note about it.
- **Task 2 completes.** Update the journal. Update memory if warranted.
- **Task 3 completes.** Full close protocol — finalize journal, update memory with complete state, cross-file updates.

If the session dies between task 2 and task 3, the journal has records of tasks 1 and 2, and memory may have partial updates. The next session's reconciliation is straightforward: tasks 1 and 2 are done, task 3 wasn't started. Compare this to a session that does all three tasks and then tries to write the journal and update memory at the end — if it dies after task 2, there's no record of any completed work.

### When progressive commit matters

Progressive commit is most valuable when sessions are long and involve multiple distinct work units. A session with a single focused task doesn't benefit much — the commit window is the whole session regardless. But a session that researches a topic, drafts a document, and then reviews another agent's output has three natural commit points.

The cost is overhead — each intermediate commit takes tokens that could be spent on work. The heuristic: commit after completing a unit of work that you wouldn't want to redo. If the research phase took significant effort, commit after research. If drafting is the expensive part, commit after drafting. The commit granularity should match the cost of re-doing the work.

## Anti-Patterns

### Memory-Last

Updating memory at session start instead of session close. This sometimes happens when an agent reads its stale memory and immediately "fixes" it based on what it sees in files, then does session work, then closes without a memory update because "memory is already current."

The problem: the session work changed state, but memory reflects the state at session open plus the agent's corrections, not the state at session close. If the session had updated memory at close, it would reflect the actual final state. Memory-last means memory is always one session behind on the work that was actually done.

### Journal-at-Close

Writing the journal only at session end. This has been covered above, but it's worth naming explicitly as an anti-pattern because it's the default instinct. Most people think of journals as summaries, written after the fact. For agent teams, journals are logs, written as things happen. The summary comes at session close; the log runs throughout.

### Optimistic Memory

Assuming memory is current without checking the reconciliation pointer against the journal. This is the "trust but don't verify" approach. Memory says the project is in state X. The agent proceeds on that basis. But if the previous session dirty-closed, state X might be wrong. The reconciliation check takes seconds. Skipping it saves seconds and risks hours — hours spent on work that's based on a false picture of current state.

### Monolithic Commit

Saving all state updates for the very end of the session. Journal finalization, memory update, brief modifications, backlog updates, cross-file references — all in one burst at session close. This creates the maximum possible failure window. If the session dies during the commit sequence, some updates made it and others didn't, leaving state in a partially committed condition that's harder to reconcile than a clean dirty close where nothing was committed.

Progressive commit is the antidote. But even without full progressive commit, spacing out the close sequence helps — finalize the journal well before the end, then update memory, then do cross-file updates. Don't bunch them.

## Design Principles

**Idempotent opens.** A session open should be safe to run repeatedly. If the agent reads memory, checks for dirty closes, and reconciles, running that sequence twice should produce the same result as running it once. This matters because sessions sometimes restart — a connection drops, the operator re-invokes the agent, and the session protocol runs again from the top. If the open sequence has side effects (like clearing a scratchpad before reading it), repeating it can lose information. Design opens so that re-running them is harmless.

**Progressive commit over atomic commit.** Commit state incrementally as work completes rather than batching everything at session end. The smaller the window between doing work and recording it, the less a dirty close can lose. This is the same principle that makes write-ahead logs effective in databases — durability comes from writing early and often, not from writing everything at once.

**Minimum viable close.** Define the smallest thing that constitutes a valid session close. When context is running out or the session is being interrupted, the agent should know exactly what to do with its remaining capacity. A full close sequence is ideal. A memory-only update is acceptable. Nothing is a failure. Having a defined minimum means the agent can make the right trade-off under pressure rather than attempting a full close and running out of context midway through.

## Evidence Summary

The journal-first principle and dirty-close detection are **Practised (1 team, 13 sessions)**. Journal entries have been written at session open consistently across this repository's history. Dirty closes have occurred and been detected through pointer mismatches and incomplete journal entries. The reconciliation approach described here was used informally to recover from those dirty closes.

The full transaction model — progressive commit, the explicit reconciliation sequence, minimum viable close — is **Hypothesis**. These practices are what the team does informally, extracted and structured into a protocol. The principles are sound (they're well-established in database transaction design), but they haven't been rigorously followed as a protocol or measured for their effect on session reliability. The claim that progressive commit reduces state loss on dirty close is logical but untested in this context.

The anti-patterns are drawn from observed failures across multiple sessions. Memory-last and journal-at-close have both occurred and caused real recovery difficulties. Optimistic memory caused at least one session to build on stale state. These are **Practised (1 team)** as observed failure modes, though their frequency and severity haven't been systematically tracked.

The database transaction metaphor is a framing device. Sessions are not actually database transactions — they lack the formal guarantees (isolation, atomicity) that make database transactions reliable. The metaphor is useful for intuition but shouldn't be over-extended. Agent sessions have no rollback mechanism; dirty state must be reconciled forward, not rolled back.

## Related Patterns

- `three-tier-memory.md` — memory is the commit target of the session transaction; the consolidation ritual described there is part of the clean close protocol
- `codification-ladder.md` — the session transaction protocol is a team-wide protocol (Tier 3 in the codification ladder); its compliance characteristics should be tracked accordingly
- `coaching-framework.md` — coaching reviews can assess session hygiene, including whether dirty close detection and reconciliation are being practised
- `learning-from-practice.md` — the confidence levels and evidence framework used in this pattern's evidence summary
- `brief-anatomy.md` — the concrete session protocol in team lead briefs that this pattern generalises from
