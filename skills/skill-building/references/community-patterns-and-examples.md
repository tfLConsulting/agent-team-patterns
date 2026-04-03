# Community Patterns & Real-World Examples

Sources: anthropics/skills repo, trailofbits/skills, obra/superpowers, OthmanAdi/planning-with-files, EveryInc/compound-engineering-plugin, awesome-claude-code curated list.

---

## Skill Archetypes

Five distinct patterns emerge from studying 200+ real-world skills:

### Pattern A: Pure Instructions (No Scripts)
Best for: brand guidelines, coding standards, review checklists, design preferences.
Just markdown in SKILL.md. No supporting files needed.
Example: `frontend-design` — pure design philosophy and anti-patterns. Tells Claude "NEVER use generic AI-generated aesthetics."

### Pattern B: Instructions + Reference Files
Best for: complex domains with heavy documentation.
SKILL.md is a router/overview (under 500 lines), separate files hold depth.
Example: `claude-api` — massive skill with language-specific subdirectories. SKILL.md detects project language and points to the right reference. Each reference has its own table of contents.

### Pattern C: Instructions + Scripts
Best for: capability uplift where Claude needs to execute deterministic tasks.
SKILL.md describes workflow, `scripts/` has black-box executables.
Example: `webapp-testing` — decision tree for choosing approach, scripts in `scripts/` with explicit instruction: "run with `--help` first, DO NOT read the source."

### Pattern D: Discipline-Enforcing
Best for: behavioral rules where Claude tends to cut corners.
Iron laws, rationalization tables, red flags, gate functions.
Example: `test-driven-development` (obra/superpowers) — "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST." Includes a table of 11 common rationalizations with rebuttals.

### Pattern E: Subagent Orchestration
Best for: multi-step workflows where each step needs fresh context.
Dispatch subagents with crafted prompts, review loops. References prompt template `.md` files.
Example: `subagent-driven-development` — fresh subagent per task, two-stage review (spec compliance + code quality), prompt templates in separate files.

## Notable Skill Examples (Annotated)

### Anthropic's pdf skill
```yaml
---
name: pdf
description: Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.
---
```
**What works:** Exhaustive trigger list in description — leaves no ambiguity about when to fire. Supporting files: `forms.md`, `reference.md`, `scripts/`. Quick reference table at end of SKILL.md.

### Anthropic's claude-api skill
```yaml
---
name: claude-api
description: "Build apps with the Claude API or Anthropic SDK. TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`/`claude_agent_sdk`... DO NOT TRIGGER when: code imports `openai`/other AI SDK..."
---
```
**What works:** Explicit TRIGGER/DO NOT TRIGGER conditions. Language-specific subdirectories. SKILL.md acts as a routing document. "Reading Guide" section for progressive disclosure.

### Trail of Bits variant-analysis skill
```yaml
---
name: variant-analysis
description: Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgrep queries, analyzing security vulnerabilities, or performing systematic code audits after finding an initial issue.
---
```
**What works:** Five-step process. "When to Use" AND "When NOT to Use" sections. Tool selection table. Critical pitfalls. Resources directory with templates per language.

### Obra's verification-before-completion skill
```yaml
---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
---
```
**What works:** Gate function pseudocode. Common failures table mapping claims to requirements. "Why This Matters" section citing specific past failures. Pure discipline enforcement.

### Obra's writing-skills skill (Meta-skill)
**Critical discovery:** Description field should ONLY contain triggering conditions, never a workflow summary. Testing showed Claude follows description shortcuts instead of reading the full skill content.
- TDD applied to skill creation (write evals before writing the skill)
- Token efficiency targets
- Anti-patterns section
- Deployment checklist

### Planning-with-files (17k stars)
Three-file system for complex tasks: `task_plan.md` (phases/goals), `findings.md` (research/discoveries), `progress.md` (session logs). Uses hooks to re-read plans before decisions.

### Compound Engineering
Philosophy: "80% planning and review, 20% execution." Commands: ideate, brainstorm, plan, work, review, compound. Uses worktrees for isolated execution.

## What Makes Skills Fail (Anti-Patterns)

### Description Anti-Patterns
- **Vague triggers:** "Helps with documents" — Claude can't decide when to fire
- **Workflow summaries in description:** Claude shortcuts the full SKILL.md and follows the description instead
- **First person:** "I can help you..." — descriptions are injected into system prompt, third person required
- **Too long:** Eats into the shared 2% context budget for all skills

### SKILL.md Anti-Patterns
- **Everything in one file:** >3,000 words without references means slow loading, wasted context
- **Second person:** "You should..." — imperative form works better ("To accomplish X, do Y")
- **Magic constants:** Numbers without explanation ("set timeout to 4500ms" — why 4500?)
- **No examples:** Instructions without a concrete example of good/bad output
- **Time-sensitive info without dates:** "The new API..." — new when? Will be stale.

### Structure Anti-Patterns
- **Deeply nested references:** SKILL.md -> advanced.md -> details.md. Claude may partially read. Keep one level deep.
- **Unreferenced supporting files:** Files in the skill directory that SKILL.md never mentions — Claude won't know they exist
- **Windows-style paths:** Use forward slashes everywhere
- **Too many options without defaults:** Provide one recommended approach with an escape hatch

## High-Signal Patterns to Copy

1. **Exhaustive trigger lists in description** (pdf pattern) — list every scenario
2. **TRIGGER/DO NOT TRIGGER** (claude-api pattern) — explicit positive and negative matching
3. **When to Use / When NOT to Use sections** (variant-analysis) — scope boundaries
4. **Rationalization tables** (TDD pattern) — preempt every excuse Claude might use to skip steps
5. **Gate functions** (verification pattern) — "BEFORE claiming X, verify Y"
6. **Quick reference tables at end** (pdf pattern) — scannable summary after detailed content
7. **Black-box scripts** (webapp-testing) — "run --help, don't read source"
8. **Cross-skill references** — "see superpowers:skill-name" not file paths
9. **`allowed-tools` scoping** — minimize what the skill can do
10. **Evaluation-driven development** — write tests before writing the skill

## Community Scale

- awesome-claude-code: 31.5k stars, curated list
- anthropics/skills: official repo with 20+ skills, installable as plugin
- trailofbits/skills: 35 security-focused skills
- obra/superpowers: discipline + workflow skills
- antigravity-awesome-skills: 1,304+ skills with installer CLI
- alirezarezvani/claude-skills: 192 skills across engineering/marketing/compliance
