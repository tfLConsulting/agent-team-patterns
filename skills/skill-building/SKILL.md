---
name: skill-building
description: Build, review, or improve Claude Code skills. Use when creating a new skill from scratch, auditing an existing skill for quality, or converting research into a reusable skill. Covers the Agent Skills open standard, progressive disclosure, description writing, reference file organisation, and common failure modes. Also use when the user says "build a skill", "create a skill", "make a slash command", or asks how skills work.
---

> Historical application (April–May 2026). For current guidance, start with [the design library](../../README.md) and [current instructions](../../AGENTS.md). This document retains its original assumptions and evidence limits.

# Skill Building

See `references/official-docs-and-spec.md` for the complete frontmatter reference, string substitutions, invocation control matrix, and Agent Skills specification.
See `references/community-patterns-and-examples.md` for real-world skill examples, archetypes, and anti-patterns from Anthropic, Trail of Bits, obra/superpowers, and others.

## The Process

### Step 1: Research

Before writing any skill files, gather domain knowledge. This is the most important step — a skill is only as good as its source material.

1. Fetch official docs (Anthropic, MDN, framework docs, specs)
2. Search for community examples and prior art
3. Find real-world failure modes and gotchas
4. Store raw research in `references/` with source attribution

### Step 2: Structure

Choose the right archetype based on the skill's purpose:

| Archetype | When to use | Structure |
|-----------|------------|-----------|
| **Pure instructions** | Standards, guidelines, preferences | SKILL.md only, no supporting files |
| **Instructions + references** | Complex domains, heavy documentation | SKILL.md as router, `references/` for depth |
| **Instructions + scripts** | Deterministic tasks, capability uplift | SKILL.md describes workflow, `scripts/` has executables |
| **Discipline-enforcing** | Behavioural rules Claude tends to violate | Iron laws, rationalization tables, gate functions |
| **Subagent orchestration** | Multi-step workflows needing fresh context | Prompt templates in separate files, dispatch subagents |

Create the directory:
```
.claude/skills/<skill-name>/
  SKILL.md              # Required. Under 500 lines.
  references/           # Detailed reference material, one level deep
  scripts/              # Executable tools (optional)
  examples/             # Example outputs (optional)
  assets/               # Templates, images — not loaded into context (optional)
```

### Step 3: Write the Description

The description is the most load-bearing line in the skill. Claude uses it to decide when to auto-load. Get it wrong and the skill either fires constantly or never fires.

**Rules:**
- Third person ("This skill processes..." not "I can help you...")
- Include specific trigger phrases — list every scenario where the skill should activate
- Be slightly "pushy" — err on the side of over-triggering
- ONLY triggering conditions, never a workflow summary (Claude shortcuts descriptions instead of reading the full skill)
- Under 1024 chars (hard limit), but stay well under to share the context budget with other skills

**Good:**
```
Use this skill whenever the user wants to do anything with PDF files. This includes
reading or extracting text/tables from PDFs, combining or merging multiple PDFs into
one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs,
filling PDF forms, encrypting/decrypting PDFs, and OCR on scanned PDFs. If the user
mentions a .pdf file or asks to produce one, use this skill.
```

**Bad:**
```
Helps with PDF documents and related tasks.
```

**Explicit exclusions pattern (for skills that could over-trigger):**
```
TRIGGER when: code imports `anthropic` or user asks to use Claude API.
DO NOT TRIGGER when: code imports `openai` or general programming tasks.
```

### Step 4: Write SKILL.md

**Target:** 1,500-2,000 words. Under 500 lines. This is the instruction tier — not the reference tier.

**Writing style:**
- Imperative/infinitive form: "To accomplish X, do Y" — not "You should do X"
- Explain the why behind rules, not just the what. "Today's LLMs are smart. If you find yourself writing ALWAYS or NEVER in all caps, reframe and explain the reasoning." (Anthropic's own guidance)
- Lead with the most actionable content — checklists, decision trees, quick reference tables
- Put detailed explanations in `references/`

**Structure a SKILL.md like this:**
1. Pointer to reference files (one line each)
2. The core workflow or checklist (the thing Claude needs every time)
3. Decision trees or tables for choosing approaches
4. Anti-patterns / common mistakes
5. `$ARGUMENTS` placeholder at the end (if user-invocable)

**Progressive disclosure is the most important concept.** Three tiers:
1. **Metadata (~100 tokens):** Name + description. Loaded at startup for ALL skills.
2. **Instructions (<5,000 tokens):** Full SKILL.md body. Loaded when triggered.
3. **Resources (as needed):** references/, scripts/. Loaded only during execution.

### Step 5: Write Reference Files

- One file per major subtopic (not one giant file)
- Include a table of contents at the top of files >100 lines
- Keep one level deep from SKILL.md — never chain references to deeper references
- Include source URLs and dates — research goes stale
- Files >10k words: add grep-friendly section headings so Claude can search without loading the whole file

### Step 6: Validate

1. Read the description in isolation — would Claude know exactly when to fire?
2. Read SKILL.md without references — does it give enough to act on the common case?
3. Check line count: SKILL.md under 500 lines? Each reference file has a purpose?
4. Check for unreferenced files — every file in the skill directory should be mentioned in SKILL.md
5. Test: invoke the skill on a real task and observe whether Claude follows it or takes shortcuts

## Frontmatter Quick Reference

```yaml
---
name: my-skill                    # lowercase, hyphens, max 64 chars
description: Third-person trigger-rich description under 1024 chars.
argument-hint: "[optional-hint]"  # shown in autocomplete
disable-model-invocation: true    # for side-effect workflows only
allowed-tools: Bash Read Grep     # pre-approved tools (space-delimited)
model: sonnet                     # override model
context: fork                     # run in subagent context
agent: Explore                    # subagent type (with context: fork)
---
```

Only `name` and `description` matter for most skills. Add other fields only when needed.

## Common Failure Modes

| Failure | Symptom | Fix |
|---------|---------|-----|
| Vague description | Skill never auto-fires | Add explicit trigger phrases and scenarios |
| Workflow in description | Claude skips SKILL.md body | Description = triggers only, workflow in body |
| Everything in SKILL.md | Slow loading, wasted context | Move detail to `references/`, keep SKILL.md as router |
| No examples | Inconsistent output quality | Add one excellent example (beats many mediocre ones) |
| Magic constants | Claude can't adapt to edge cases | Document why values were chosen |
| Deeply nested refs | Claude partially reads or skips files | Keep references one level deep from SKILL.md |
| Unreferenced files | Claude doesn't know they exist | Mention every file in SKILL.md |
| Second person style | Slightly less reliable following | Use imperative: "To X, do Y" |

## Reviewing an Existing Skill

Checklist for auditing a skill:

- [ ] Description is third-person, trigger-rich, under 1024 chars
- [ ] Description contains no workflow summary
- [ ] SKILL.md is under 500 lines
- [ ] Every file in the directory is referenced in SKILL.md
- [ ] References are one level deep (no chained references)
- [ ] Large reference files (>100 lines) have a table of contents
- [ ] Writing uses imperative form, not second person
- [ ] Rules explain the "why"
- [ ] No magic constants without explanation
- [ ] At least one concrete example of good/bad output for non-trivial skills

$ARGUMENTS
