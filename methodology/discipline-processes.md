# Discipline Processes as Encoded Skills

Disciplines have processes. UX design, content strategy, SEO, analytics, engineering, testing, product management — each has established frameworks and methodologies refined over decades by practitioners. The best humans internalize these processes until they feel like intuition. AI agents haven't had decades. Without an encoded process, "do UX design" produces inconsistent, often shallow output. With one, the same task follows established discipline methodology every time.

Encoding discipline processes as structured skills is the difference between an agent that improvises and one that executes with repeatable quality. Processes raise the floor dramatically.

## Progressive Disclosure: Three-Tier Skill Structure

A library of discipline skills creates a context management problem. Twenty skills loaded in full at every session would consume most of the available context window before real work begins. The fix is progressive disclosure:

**Tier 1 — Metadata.** Trigger conditions only, loaded always. A few lines per skill describing when it applies. This is how the agent knows the skill exists and when to reach for it. Cost: negligible even at scale.

**Tier 2 — Instructions.** The actionable workflow, loaded on activation. This is the process itself — phases, decision points, outputs. Keep it under 1500-2000 words. Longer instructions hit the density problem described in `writing-for-ai.md`: agents don't get things wrong, they miss things entirely.

**Tier 3 — References.** Deep domain knowledge, loaded on demand during execution. Spacing systems, accessibility standards, competitive frameworks, scoring rubrics. An agent working through a design review loads the review rubric when it reaches that phase, not at session start.

This structure means a library of 20+ skills costs almost nothing when idle and loads depth only when active. The alternative — everything in the brief or project instructions — is how you get 500-instruction contexts where the best models drop to 63–69% accuracy (see `writing-for-ai.md` for the underlying instruction-density research).

**Evidence:** Practised (1 team, 150+ sessions). The three-tier structure prevented context bloat as a skill library grew to 22 skills across 7 domains. No controlled comparison against flat loading, but the directional evidence from instruction-density research (cited in `writing-for-ai.md`) supports the architecture.

## Anti-Patterns as First-Class Citizens

Telling an agent what to do is less effective than also telling it what not to do. Anti-patterns prevent the most common AI failure modes — the ones where output looks plausible but violates discipline fundamentals.

Examples of the form:
- "Never design from imagination — ground every decision in research findings."
- "Don't generate one approach and call it options."
- "Don't skip the problem definition phase to get to solutions faster."

Anti-patterns work because they're specific and falsifiable. An agent can check whether it's violating a negative constraint more reliably than it can evaluate whether it's achieving a vague positive goal. "Make it good" is unverifiable. "Don't present untested assumptions as findings" is a concrete gate.

Skills with explicit anti-patterns produced more consistent output than open-ended instructions in observed practice. The mechanism is straightforward: anti-patterns eliminate the highest-variance failure modes, which narrows the output distribution more than positive instructions alone.

## Human Checkpoints at Critical Junctures

Processes should include mandatory approval gates before the agent commits to a direction that's expensive to reverse. This is the authority gradient from `role-design.md` applied at the task level.

A UX process might require human approval after problem definition before spending tokens on exploration. A content strategy process might pause after topic selection before drafting. The principle: any phase transition where bad framing would waste all subsequent work is a checkpoint.

The cost of a checkpoint is one pause in execution. The cost of skipping it is an agent that spends an entire session building on a flawed premise. The economics favour checkpoints at phase boundaries where direction changes are cheap but commitment is about to get expensive.

## Quality Rubrics with Specific Criteria

Replace "review this for quality" with dimensional scoring. A design review might score 8 dimensions on a 1-5 scale: visual hierarchy, spacing consistency, accessibility, responsive behaviour, brand alignment, interaction clarity, information density, error handling. A content review might check 20+ specific points across accuracy, voice, structure, and SEO.

Rubrics reduce variance. Different agents — or the same agent across sessions — applying the same rubric converge on similar assessments. Without a rubric, "review" is underspecified and the agent fills the gap with whatever seems relevant in context, which varies.

Rubrics belong in Tier 3 (references), loaded when the process reaches a review phase. They're too detailed for always-loaded context but too valuable to improvise.

## Staged Execution Across Fresh Contexts

Complex processes benefit from splitting across multiple subagent invocations with fresh context. The reason is anchoring: early decisions in a long context constrain all subsequent work. An agent that defined the problem, explored options, and is now evaluating them has spent thousands of tokens building a narrative. It's anchored to that narrative.

Splitting phases across fresh contexts — problem definition in one invocation, exploration in another, evaluation in a third — reduces this bias. Each phase starts clean, reading only the structured output of the previous phase rather than inheriting its full reasoning chain.

This is expensive in coordination overhead. It's worth it for high-stakes processes where anchoring bias would compromise the output. It's overkill for routine tasks. The heuristic: if the process has phases where you'd want genuinely independent thinking, stage it. If it's a linear workflow, keep it in one context.

## Checklists as First-Class Objects

Some discipline knowledge is best expressed as checklists rather than prose. Spacing systems, colour contrast ratios, priority tiers, validation rules, accessibility criteria, editorial standards. These are reference artifacts that an agent applies mechanically during execution.

Checklists belong in Tier 3. They're loaded when needed and applied literally. The value is consistency — repeatable beats intuitive for any criterion that has a known-correct answer.

## The Meta-Process: A Skill for Building Skills

A skill library that grows ad-hoc accumulates inconsistency. A meta-skill — a process for creating processes — solves this. The meta-process encodes:

1. **Research phase.** What does the discipline's established methodology look like? What frameworks exist? What do practitioners actually do?
2. **Structure choice.** Which elements of the methodology translate to phases, checkpoints, anti-patterns, and rubrics?
3. **Description engineering.** Writing instructions that AI agents can follow — applying `writing-for-ai.md` principles to skill content.
4. **Progressive disclosure assignment.** What goes in Tier 1, 2, and 3?

This creates a self-reinforcing system. Better processes create better outcomes. Outcomes reveal what works and what doesn't. Those learnings feed back into improved processes through the meta-skill. The library compounds rather than just growing.

**Evidence:** Practised (1 team, 150+ sessions). A meta-skill for creating skills enabled a library to grow from a handful to 22 skills systematically. Skills created through the meta-process were structurally consistent; earlier skills created ad-hoc required later rework.

## Evidence Summary

This pattern has been observed in one production agent team running 22 discipline-encoded skills across 7 domains over 150+ sessions. The overall confidence level is **Practised (1 team, 150+ sessions)** — consistent use without catastrophic failure, but not yet replicated across independent teams or deliberately varied.

The mechanisms described here align with general process engineering principles and with the instruction-density research cited in `writing-for-ai.md`. But alignment with principles is not the same as direct evidence. The specific claims about anchoring reduction from staged execution, for example, are hypothesis-level — observed informally, not measured.

## Related Patterns

- `writing-for-ai.md` — how to write instructions AI agents can follow
- `role-design.md` — how domain ownership and authority boundaries apply to agents
- `brief-anatomy.md` — the structure of agent definitions, including why briefs set methodology rather than prescribe process
