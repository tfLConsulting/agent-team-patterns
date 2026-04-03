# Build Recipe — Research Synthesis

Evidence base for the 6-step build recipe. Compiled 2026-03-25.

## Why structure matters: the 82% finding

Ken Judy (InfoQ, 2026) compared structured vs unstructured AI coding on the same feature:

| Metric | Unstructured | PDCA structured |
|--------|-------------|-----------------|
| Total tokens | 1,485,984 | 1,331,638 |
| Troubleshooting tokens | 1,221,217 (82%) | negligible |
| Production code lines | 534 | 350 |
| Test code lines | 759 | 984 |

The unstructured approach spent 82% of tokens AFTER the agent declared the task complete — all on debugging, resolving incomplete implementation, and correcting assumptions about existing code. The structured approach produced 34% less production code but 30% more test code.

Source: [A Plan-Do-Check-Act Framework for AI Code Generation](https://www.infoq.com/articles/PDCA-AI-code-generation/)

## Why fresh context for review

Anthropic's own best practices recommend the Writer/Reviewer pattern with separate sessions: "A fresh context improves code review since Claude won't be biased toward code it just wrote."

Greptile's analysis confirms: even when the same LLM generates and reviews code, context separation matters more than the underlying model being different. The context separation removes "anchoring on a shared framing before forming an independent opinion."

Sources: [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices), [Greptile](https://www.greptile.com/blog/ai-code-reviews-conflict)

## Why read existing code first

Factory.ai (raised $50M, ships production AI coding agents) found: "baseline codebase quality is the only reliable predictor of whether AI accelerates or decelerates an organization." Their agents build graph-based codebase representations during indexing so agents enter tasks with pre-built understanding.

Context blindness — AI not reading existing code — causes code drift, pattern divergence, and duplicate implementations. The CodeScene study found agents replicate patterns already in the repo, even suboptimal ones, causing invisible architectural degradation.

Sources: [Stack Overflow / Factory.ai](https://stackoverflow.blog/2026/02/04/code-smells-for-ai-agents-q-and-a-with-eno-reyes-of-factory/), [CodeScene](https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality)

## Why test-first

Judy's TDD rules:
- DO NOT test interfaces — test concrete implementations
- DO NOT use compilation errors as RED phase
- DO create stub implementations that compile but fail behaviorally
- DO use real components over mocks when possible

The Agentic Coding Handbook (Tweag) found: "A test becomes a natural language spec that guides the AI toward exactly the behavior you expect." Tests are both specification and verification.

Sources: [PDCA framework](https://www.infoq.com/articles/PDCA-AI-code-generation/), [Agentic Coding Handbook](https://tweag.github.io/agentic-coding-handbook/WORKFLOW_TDD/)

## Why small commits

Judy's GitHub Actions quality metrics (targets for AI-generated code):

| Metric | Target |
|--------|--------|
| Large commits (>100 lines) | <20% of commits |
| Sprawling commits (>5 files) | <10% of commits |
| Average files per commit | <5 |
| Average lines per commit | <100 |
| Test-first discipline | >50% of commits |

Osmani: commits are "save points in a game" — they let you undo AI missteps cheaply.

Sources: [PDCA framework](https://www.infoq.com/articles/PDCA-AI-code-generation/), [Addy Osmani](https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e)

## AI code bug rates

Study of 470 GitHub repos found AI-generated code has:
- 1.7x more bugs overall
- 75% more logic and correctness errors
- 1.5-2x more security issues
- ~8x higher excessive I/O operations
- ~2x more error handling issues
- 2.74x higher XSS vulnerability rate

PR volume increases ~18% with AI, but incidents per PR up ~24% and change failure rates up ~30%.

Google DORA 2025: 90% AI adoption increase correlates with 9% climb in bug rates, 91% increase in code review time, 154% increase in PR size.

Sources: [Stack Overflow](https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/), [CodeRabbit](https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality)

## Subagent invocation quality

ClaudeFast: "Sub-agent failures aren't execution failures — they're invocation failures." The #1 cause of subagent failure is vague instructions without specific file paths and clear deliverables.

Anthropic docs: "Include tests, screenshots, or expected outputs so Claude can check itself. This is the single highest-leverage thing you can do."

Martin Fowler: "Even with large token budgets, excessive context degrades agent effectiveness — more information doesn't automatically mean better reasoning."

Sources: [ClaudeFast](https://claudefa.st/blog/guide/agents/sub-agent-best-practices), [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices), [Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)

## Spec-driven development evidence

- McKinsey 2025: 20-45% productivity gains from AI tools that reduce rework
- AWS/Kiro: Two-week feature cut to two days
- LLMs generate vulnerable code at 9.8-42.1% across benchmarks; specs reduce this by making requirements explicit
- Spec overhead: 20-40% of manual implementation time, pays back 2-3x
- ThoughtWorks caution: verbose specs are tedious to review, agents sometimes ignore or over-comply with them, forced specs for small tasks create overhead

Sources: [Red Hat](https://developers.redhat.com/articles/2025/10/22/how-spec-driven-development-improves-ai-coding-quality), [ThoughtWorks](https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices), [Augment Code](https://www.augmentcode.com/guides/what-is-spec-driven-development)
