# Overlap Analysis: bootstrapping-protocol.md vs. agent-team-guide.md

## Purpose

The editorial roadmap flagged that bootstrapping steps are split between two files, creating redundancy and reader confusion. This document provides a section-by-section overlap map and a specific reconciliation proposal.

---

## 1. Section-by-Section Overlap Map

### 1.1 "When do you need agents?" / Assessment Gate

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| Not every project needs agents | "The Assessment Gate" (lines 35-38) | Section 1 "When You Don't Need One" (lines 19-37) | **Guide wins.** The guide has specific bullet-point criteria for CLAUDE.md-sufficient vs. agent-warranted projects. The bootstrapping doc has a brief two-paragraph version. |
| "Valid outcome, not a failure" line | Line 36 (almost verbatim) | Line 37 (almost verbatim) | **Identical phrasing.** Pure duplication. |

### 1.2 The Structural Contradiction / Two-Agent Start

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| "Create agents only after 3+ sessions" vs. bootstrapping before session 1 | "The Structural Contradiction" (lines 16-21) | Section 4.4 "Create Two Core Agents" paragraph "Why only two" (lines 236-238) | **Both are good; bootstrapping doc is slightly more philosophical.** The guide restates the same resolution in nearly the same words. |
| Team lead as minimal entry point | Line 18 | Line 236 | **Near-identical.** |
| Team coach exists because team lead can't evaluate its own composition | Line 18 | Lines 236-239 | **Guide is better** -- adds the empirical observation about the team lead never proposing composition changes. |
| "Deliberately underpowered at first" | Lines 20-21 | Lines 190-191 (Section 3.6) and line 236 | **Bootstrapping doc is more explicit** about why underpowered-at-first is the point. Guide says it but more briefly. |
| Team coach review schedule (session 3, every 5 after) | Line 20 | Lines 234, 385 | **Guide wins** -- covered in both Section 4.4 and Section 6, with more operational detail. |

### 1.3 What's Universal / Patterns That Work

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| Negative rights in role design | Lines 44-46 | Section 2.1 (lines 45-57) | **Guide wins decisively.** Full problem/solution treatment with domain/authority/boundaries/inputs-outputs breakdown. Bootstrapping doc has two bullet points. |
| Brief anatomy | Lines 46-47 | Section 2.2 (lines 59-79) | **Guide wins decisively.** Full pattern with what to include and what to leave out. Bootstrapping doc lists seven words. |
| Three-tier memory | Lines 48-49 | Section 2.3 (lines 81-96) | **Guide wins decisively.** Full pattern with failure mode reference. Bootstrapping doc has two sentences. |
| Team coordination / router model | Lines 50-51 | Section 2.5 (lines 109-133) | **Guide wins decisively.** Full treatment. Bootstrapping doc has a half-sentence summary. |
| File-based coordination | Lines 52-53 | Section 2.4 (lines 97-108) | **Guide wins.** |

**Pattern:** The guide's Section 2 is a thorough treatment. The bootstrapping doc's "What's Universal" section is a compressed summary of the same material. There is no scenario where a reader would prefer the bootstrapping doc's treatment over the guide's.

### 1.4 Failure Modes

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| Over-engineering | Lines 58-59 | Section 3.6 (lines 187-191) | **Roughly equal.** Nearly identical wording. Guide adds the mitigation (two-agent start, 3-session rule). |
| Cargo culting | Lines 60-61 | Not present | **Unique to bootstrapping doc.** |
| Wrong composition | Lines 62-63 | Not directly present | **Unique to bootstrapping doc** (though the guide's team coach section addresses this indirectly). |
| Early-session confirmation bias | Lines 64 (long paragraph) | Section 3.2 (lines 159-163) | **Guide is slightly better** -- it's the same content but edited down to essentials. Bootstrapping doc is longer but not more informative. |
| Premature rigidity | Lines 66-67 | Section 9 "Premature Rigidity" (lines 503-507) | **Guide wins.** More operational ("if the brief from session 0 is still unchanged at session 15, something is wrong"). |
| Bootstrap paradox | Lines 68-69 | Not present as a standalone concept | **Unique to bootstrapping doc** as a named concept, though the guide addresses the underlying issue in Section 4.4 and Section 12. |
| Narrative outrunning reality | Not present | Section 3.3 (lines 165-172) | **Unique to guide.** |
| Inline execution | Not present | Section 3.4 (lines 173-178) | **Unique to guide.** |
| Teams can't escalate | Not present | Section 3.5 (lines 179-185) | **Unique to guide.** |
| Memory pruning losing decisions | Not present | Section 3.1 (lines 149-157) | **Unique to guide.** |

### 1.5 Wiring in the Learning Loop

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| Experiment log at bootstrap | Lines 26-27 | Not present | **Unique to bootstrapping doc.** |
| Micro-observation prompt in session close | Lines 28-29 | Not present (journal protocol is in guide but not this specific prompt) | **Unique to bootstrapping doc.** |
| First ~10 sessions as exploration | Lines 30-31 | Partially in Section 9 "Premature Rigidity" (lines 503-507) | **Bootstrapping doc is more specific** (names the ~10-session window and ties it to the experiment log). |

### 1.6 Compatibility with Claude Code Native Agent Teams

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| Native Agent Teams = execution layer, file-based = persistence layer | Lines 70-78 | Lines 579-587 | **Near-identical.** Same structure, same bullet points, same conclusion. Pure duplication. |

### 1.7 Limitations / What This Guide Doesn't Do

| Concept | bootstrapping-protocol.md | agent-team-guide.md | Stronger Treatment |
|---------|--------------------------|---------------------|--------------------|
| N=3 same operator caveat | Lines 80-81 | Lines 572-573 (Section 12) | **Both good.** Very similar wording. |
| Tacit knowledge / operator judgment | Lines 82-83 | Lines 565-566 (Section 12) | **Similar.** |
| Platform evolution | Lines 83-84 | Not present | **Unique to bootstrapping doc** but minor. |
| CLAUDE.md may be enough | Lines 84-85 | Lines 569 (Section 12) | **Both present.** |

---

## 2. Content Unique to bootstrapping-protocol.md

After mapping all overlaps, the following content is ONLY in the bootstrapping doc:

1. **"The Hard Question" framing** (lines 6-13) -- Why creating a team is harder than creating agents. Three specific reasons (codebase doesn't encode goals, least-equipped evaluator problem, over-engineering default). This is good philosophical framing not in the guide.

2. **"Wiring in the Learning Loop"** (lines 23-32) -- The experiment log template, micro-observation prompt in session-close, and treating first ~10 sessions as exploration. This is actionable and unique. The guide has journal protocol and premature rigidity warnings but not this specific three-part learning infrastructure.

3. **"Cargo culting" failure mode** (lines 60-61) -- Named concept with examples (three-tier memory for monthly projects, negative rights where drift hasn't been observed). Good practitioner warning.

4. **"Bootstrap paradox" as named concept** (lines 68-69) -- The specific tension that the protocol is designed for people who don't know agent teams, but evaluating its output requires that knowledge.

5. **"Platform evolution" limitation** (line 83) -- Minor; just notes that Claude Code may subsume the protocol.

6. **"Wrong composition" failure mode** (lines 62-63) -- Brief but useful.

Items 1-4 are the genuinely valuable unique content. Items 5-6 are minor.

---

## 3. Content Unique to agent-team-guide.md

For completeness, major content unique to the guide (not in bootstrapping doc):

- Section 2 detailed pattern treatments (role design, brief anatomy, memory, coordination, router model, journal)
- Section 3 failure modes: memory pruning (3.1), narrative outrunning reality (3.3), inline execution (3.4), teams can't escalate (3.5)
- Section 4 complete step-by-step bootstrapping procedure (4.1-4.7)
- Section 5 improving existing teams
- Section 6 team coach mechanism in detail
- Section 7 skills meta-pattern
- Section 8 multi-team considerations
- Section 9 self-modification
- Section 10 actionable checklists
- Section 11 using methodology in another project
- Section 12 what the guide doesn't do

The guide is dramatically more comprehensive. The bootstrapping doc is a subset plus a few unique items.

---

## 4. Reconciliation Options

### Option A: Bootstrapping doc becomes the "why," guide stays the "how"

**Pro:** Preserves both files, gives them clear roles.
**Con:** The bootstrapping doc's "why" content is thin once you remove the overlapping material. You'd be left with "The Hard Question," "Structural Contradiction," "Wiring in the Learning Loop," and three unique failure modes. That's maybe 40 lines of real content. A standalone document of 40 lines feels like a stub, not a pattern file. Readers would still need to go to the guide for everything actionable. The "why" framing works better as context within the guide itself.

### Option B: Merge unique content into guide, retire bootstrapping-protocol.md

**Pro:** Single source of truth. Eliminates all redundancy. Reader only needs one document. Follows the precedent set when team-coordination.md was retired in session 4.
**Con:** The guide is already long (587 lines). Adding more increases length. However, the unique content is small (maybe 30-40 lines net), and some of it naturally fits into existing sections.

### Option C: Keep bootstrapping-protocol.md as a focused "design rationale" document

**Pro:** Some readers want the philosophy without the how-to. Pattern libraries sometimes have separate "rationale" documents.
**Con:** Creates a maintenance burden. Every time the guide's Section 4 changes, someone needs to check whether the rationale doc is still consistent. This is the exact problem that created the current redundancy.

---

## 5. Recommendation: Option B (Merge and Retire)

**Rationale:**

1. The overlap is extensive. Of the bootstrapping doc's ~85 lines of content, roughly 55-60 lines are covered (often better) in the guide. The unique content is approximately 25-30 lines.

2. The unique content has natural homes in the guide:
   - "The Hard Question" framing fits into Section 4 as an introductory paragraph or into Section 1.
   - "Wiring in the Learning Loop" fits into Section 4 as a new subsection 4.6.5 or similar, or into Section 9 (Self-Modification).
   - "Cargo culting" and "wrong composition" failure modes fit into Section 3.
   - "Bootstrap paradox" fits into Section 12 or Section 4.

3. The precedent from session 4 (retiring team-coordination.md) worked well. Same pattern: content spread across two files, one file is a proper treatment, the other is a partial overlap. Merge and retire.

4. A single authoritative document is better for a public patterns library. Practitioners shouldn't have to wonder which file to read.

---

## 6. Specific Content Moves

### Move 1: "The Hard Question" framing -> Guide Section 4 intro

**Source:** bootstrapping-protocol.md lines 6-13
**Target:** Insert at the start of Section 4 (after "This section is actionable"), before Section 4.1

New paragraph to add:
> Creating agents is easy. Creating a *team* -- agents with the right roles, sharp boundaries, persistent memory, and coordination patterns -- is hard. The hardest part isn't infrastructure; it's figuring out which agents a project actually needs. This is harder than it sounds: a project's codebase doesn't encode its goals or pain points, the person who most needs the protocol is least equipped to evaluate its output, and over-engineering is the default failure mode.

This sets up the Section 4 sequence with motivation. Currently Section 4 jumps straight to "Read the Project First" without explaining why the bootstrapping sequence matters.

### Move 2: "Cargo culting" failure mode -> Guide Section 3

**Source:** bootstrapping-protocol.md lines 60-61
**Target:** New subsection in Section 3, after 3.6 (Over-Engineering at Bootstrap). Call it "3.7 Cargo Culting Patterns."

Content:
> **What it looks like:** Copying patterns without understanding why they work. Three-tier memory for a project that runs one session per month. Negative rights for roles where drift hasn't been observed. The patterns in this guide solve specific problems -- applying them where those problems don't exist adds complexity without benefit.

### Move 3: "Wrong composition" failure mode -> Guide Section 3

**Source:** bootstrapping-protocol.md lines 62-63
**Target:** Merge into existing Section 3.6 as an additional paragraph, or new subsection 3.8.

Content (brief, add to 3.6):
> A related failure: the initial assessment gets the project type or work domains wrong, producing agents that don't match actual needs. The mitigation is the same -- start with two agents and let the team coach evaluate against real usage at session 3.

### Move 4: "Wiring in the Learning Loop" -> Guide Section 4, new subsection

**Source:** bootstrapping-protocol.md lines 23-32
**Target:** New subsection 4.6.5 or renumber as 4.7, shifting current 4.7 to 4.8. Title: "Wire in the Learning Loop."

This is the most substantial unique content. It should go into the guide's bootstrapping sequence because it describes things to set up AT bootstrap time:

Content:
> ### 4.X Wire in the Learning Loop
>
> The bootstrapping protocol creates team structure. It should also create the mechanism for that structure to improve. Three things to set up at bootstrap, not bolt on later:
>
> 1. **Experiment log.** An empty file (e.g., `team-coach/experiment-log.md`) with a template for tracking structural choices. Every choice made during setup -- memory architecture, role design, session protocol -- is the first batch of entries. Status: active. Observed impact: blank (to be filled after running). See [learning-from-practice.md](learning-from-practice.md) for the template.
>
> 2. **Micro-observation prompt in the session-close protocol.** Add to the team-lead's brief: "What about our team's setup helped or hindered this session's work?" -- 1-3 sentences in the journal entry. This is the cheapest form of learning, and it doesn't happen unless it's in the protocol.
>
> 3. **Treat the first ~10 sessions as exploration.** The bootstrapped structure is a starting point. Agents should record what's working and what isn't from session 1. The team coach's first review (session 3) should check the experiment log alongside composition.

### Move 5: "Bootstrap paradox" -> Guide Section 12

**Source:** bootstrapping-protocol.md lines 68-69
**Target:** Add to Section 12 "What This Guide Doesn't Do."

Content:
> **Eliminate the bootstrap paradox.** The bootstrapping protocol is designed for people who don't yet know how agent teams work. But evaluating its output requires that knowledge. The first few sessions require more human judgment than later ones -- this is inherent, not fixable by better protocols.

Note: Section 12 already has "Replace operator judgment" which covers similar ground (lines 565-566). Consider merging: expand the existing "Replace operator judgment" paragraph to include the bootstrap paradox framing explicitly.

### Move 6: "Platform evolution" limitation -> Guide Section 12

**Source:** bootstrapping-protocol.md line 83
**Target:** Add brief note to Section 12.

Content (one sentence, append to the LLM transfer bullet):
> Additionally, Claude Code's capabilities change rapidly. If native features subsume what this guide provides, the guide becomes unnecessary -- and that's fine.

### Move 7: Remove duplicate "Compatibility with Claude Code Native Agent Teams"

Both files have nearly identical sections. The guide's version (lines 579-587) stays. The bootstrapping doc's version (lines 70-78) is retired with the file.

### Move 8: Remove all overlapping content

The following bootstrapping-protocol.md content is already covered better in the guide and does NOT need to be moved:

- "The Structural Contradiction" (lines 16-21) -- covered in guide Section 4.4
- "What's Universal" patterns (lines 42-55) -- covered in guide Section 2
- "Over-engineering" failure mode (lines 58-59) -- covered in guide Section 3.6
- "Early-session confirmation bias" (lines 64) -- covered in guide Section 3.2
- "Premature rigidity" (lines 66-67) -- covered in guide Section 9
- "Compatibility" section (lines 70-78) -- covered in guide lines 579-587
- "Limitations" N=3 caveat, tacit knowledge, CLAUDE.md sufficiency (lines 80-85) -- covered in guide Section 12
- Assessment gate (lines 35-38) -- covered in guide Section 1 and 4.3

### Final Step: Retire bootstrapping-protocol.md

After all moves are complete:
1. Delete `methodology/bootstrapping-protocol.md`
2. Check for any cross-references to it from other methodology files and update them to point to the relevant guide section
3. Update any references in agent briefs or memory files

---

## 7. Cross-References That Need Updating

Grep confirms the following files reference `bootstrapping-protocol.md` and will need updates after retirement:

1. **`README.md` line 14:** `Read [bootstrapping-protocol.md](methodology/bootstrapping-protocol.md).`
   - Change to point to `agent-team-guide.md` Section 4, e.g., "Read the [practitioner's guide](methodology/agent-team-guide.md), starting with Section 4 if you're setting up a new team."

2. **`methodology/README.md` line 8:** `Read [bootstrapping-protocol.md](bootstrapping-protocol.md). It walks through assessment...`
   - Rewrite to point to `agent-team-guide.md` Section 4. The sentence about wiring in the learning loop from learning-from-practice.md can stay but should reference the new guide subsection.

3. **`agents/team-lead/memory.md` lines 36, 43:** References in the editorial roadmap and file quality list.
   - Line 36: Mark this editorial item as completed once the merge is done.
   - Line 43: Remove bootstrapping-protocol from the "Adequate" list (file no longer exists).

4. **Journal entries** (`journal/2026-04-03-2.md`, `3.md`, `4.md`, `5.md`): Historical references. These do NOT need updating -- journals are historical records. But the session that executes the merge should note in its own journal entry that this was completed.

---

## 8. Net Impact Assessment

- **Lines added to guide:** ~40-50 (Moves 1-6)
- **Lines removed from guide:** 0
- **Files removed:** 1 (bootstrapping-protocol.md, 85 lines)
- **Redundant content eliminated:** ~55-60 lines of duplication
- **Unique content preserved:** All of it, in better locations
- **Reader experience:** Single document to read, no confusion about which file covers bootstrapping
- **Maintenance burden:** Reduced (one file to maintain instead of two)
