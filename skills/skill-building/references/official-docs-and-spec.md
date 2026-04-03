# Official Documentation & Specification

Sources: code.claude.com/docs/en/skills, platform.claude.com skill authoring best practices, agentskills.io specification, anthropics/claude-code plugin-dev skill-development guide, anthropics/skills repo skill-creator.

---

## Agent Skills Open Standard (agentskills.io)

Claude Code skills follow the Agent Skills open standard, supported across 20+ tools: Claude Code, Claude.ai, Cursor, VS Code Copilot, GitHub Copilot, Gemini CLI, JetBrains Junie, OpenHands, Goose, OpenCode, Roo Code, Kiro, Amp, Letta, OpenAI Codex, Databricks, Spring AI, Snowflake, and more.

## Skill Directory Structure

```
my-skill/
  SKILL.md           # Main instructions (required)
  template.md        # Template for Claude to fill in
  examples/
    sample.md        # Example output showing expected format
  scripts/
    validate.sh      # Script Claude can execute
  references/
    deep-dive.md     # Detailed reference material
  assets/
    logo.png         # Files used in output, not loaded into context
```

**Resource types:**
- `scripts/` — Executable code for deterministic/repeated tasks. Tell Claude to run with `--help` first, not read source.
- `references/` — Documentation loaded into context as needed. Keep >10k word files with grep patterns. One level deep from SKILL.md — never chain SKILL.md -> advanced.md -> details.md.
- `assets/` — Files used in output (templates, images, fonts), not loaded into context.
- `examples/` — Example outputs showing expected format.

## Where Skills Live (Priority Order)

| Location | Path | Applies to |
|----------|------|------------|
| Enterprise | Managed settings | All users in org |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin is enabled |

Higher-priority locations win on name conflicts. Plugin skills use `plugin-name:skill-name` namespace. Nested `.claude/skills/` in subdirectories are auto-discovered (monorepo support).

## Complete YAML Frontmatter Reference

| Field | Required | Description |
|---|---|---|
| `name` | No | Display name. Lowercase letters, numbers, hyphens only. Max 64 chars. Must not start/end with hyphen, no consecutive hyphens, must match parent directory name. |
| `description` | Recommended | What the skill does and when to use it. Max 1024 chars. Claude uses this to decide when to auto-load. Third person. |
| `argument-hint` | No | Hint shown during autocomplete: `[issue-number]` |
| `disable-model-invocation` | No | `true` prevents Claude from auto-loading. Default: `false`. Use for side-effect workflows. |
| `user-invocable` | No | `false` hides from `/` menu. Default: `true` |
| `allowed-tools` | No | Tools Claude can use without asking permission when skill is active. Space-delimited or YAML list. |
| `model` | No | Override model when skill is active |
| `effort` | No | Effort level: `low`, `medium`, `high`, `max` (Opus 4.6 only) |
| `context` | No | Set to `fork` to run in a forked subagent context |
| `agent` | No | Subagent type when `context: fork` is set (`Explore`, `Plan`, etc.) |
| `hooks` | No | Hooks scoped to this skill's lifecycle |

### Invocation Control Matrix

| Frontmatter | User can invoke | Claude can invoke | When loaded |
|---|---|---|---|
| (default) | Yes | Yes | Description always in context, full skill loads when invoked |
| `disable-model-invocation: true` | Yes | No | Description NOT in context, full skill loads when user invokes |
| `user-invocable: false` | No | Yes | Description always in context, full skill loads when Claude invokes |

## String Substitutions

| Variable | Description |
|---|---|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` / `$N` | Specific argument by 0-based index |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the SKILL.md |

## Dynamic Context Injection

The `` !`<command>` `` syntax runs shell commands before content is sent to Claude. Output replaces the placeholder:

```yaml
---
name: pr-summary
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---
## Pull request context
- PR diff: !`gh pr diff`
- Changed files: !`gh pr diff --name-only`
```

## Progressive Disclosure (Three Tiers)

The most important architectural concept for skills:

1. **Metadata (~100 tokens):** Name + description. Loaded at startup for ALL skills. This is what Claude uses to decide relevance.
2. **Instructions (<5,000 tokens recommended):** Full SKILL.md body. Loaded when skill is triggered. Keep under 500 lines / 1,500-2,000 words.
3. **Resources (as needed):** scripts/, references/, assets/. Loaded only when Claude needs them during execution.

### Three Reference Patterns

**Pattern 1: High-level guide with references**
```
SKILL.md -> FORMS.md, REFERENCE.md, EXAMPLES.md
```

**Pattern 2: Domain-specific organization**
```
SKILL.md -> reference/finance.md, reference/sales.md, reference/product.md
```

**Pattern 3: Conditional details**
```
SKILL.md -> REDLINING.md (only for tracked changes), OOXML.md (only for XML)
```

## Context Budget

Skill descriptions share a budget that scales at 2% of context window, with a fallback of 16,000 characters. Override with `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var. Keep descriptions lean — every character counts against the budget for all skills.

## Writing Style Rules (from Anthropic's own guides)

- **Description:** Third person ("This skill processes..." not "I can help you process..."). Include specific trigger phrases. Be slightly "pushy" — list all scenarios where the skill should fire.
- **Body:** Imperative/infinitive form ("To accomplish X, do Y" not "You should do X"). Explain the why, not just the what.
- **Concision:** The context window is a public good. Default assumption: Claude is already very smart. Only add context Claude doesn't already have.

## Subagent Integration

Skills can be injected into subagent definitions via the `skills` field:

```yaml
---
name: api-developer
description: Implement API endpoints following team conventions
skills:
  - api-conventions
  - error-handling-patterns
---
```

This loads full skill content into the subagent's context at startup.

## Bundled Skills (Ship with Claude Code)

| Skill | Purpose |
|---|---|
| `/batch <instruction>` | Large-scale parallel changes across codebase |
| `/claude-api` | Load Claude API reference material |
| `/debug [description]` | Troubleshoot session by reading debug log |
| `/loop [interval] <prompt>` | Run prompt repeatedly on interval |
| `/simplify [focus]` | Review changed files for quality issues |

## SKILL.md vs CLAUDE.md

CLAUDE.md loads every session — only include broadly applicable things. Skills load on demand, keeping conversations lean. Use skills for domain knowledge or workflows only relevant sometimes.
