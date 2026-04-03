# Role Design & Authority Boundaries

The most common failure in multi-agent systems is role confusion. Agents duplicate work, contradict each other, or sit idle because nobody owns the problem. The fix isn't more coordination — it's sharper role definition.

## The Principle: Domain Ownership with Negative Rights

Each agent owns a specific domain. Ownership means the agent has authority over findings and recommendations within that domain. But authority is bounded by explicit "what you don't do" statements.

Negative rights matter more than positive ones. An agent told "you own content strategy" will inevitably drift into design, analytics, or implementation. An agent told "you own content strategy; you don't write code, you don't make design decisions, you don't publish without review" stays in its lane.

## Anatomy of a Good Role Definition

1. **Domain:** What slice of the problem space does this agent own?
2. **Authority:** What decisions can this agent make autonomously?
3. **Boundaries:** What does this agent explicitly NOT do? (List the adjacent roles it could drift into)
4. **Inputs:** What files/data does this agent read from other agents?
5. **Outputs:** What does this agent produce, and who consumes it?
6. **Success:** What does good work look like? (Descriptive, not metric-based)

## Examples of Effective Boundaries

**Product Analyst** — owns customer research and usage data. Has authority to surface findings and propose investigations. Does NOT make strategic decisions (that's the team lead). Does NOT decide what content to write (that's the content strategist).

**Content Strategist** — owns what to write and why, grounded in analyst findings. Drafts content for human review. Does NOT publish. Does NOT make design decisions.

**Engineering Lead** — owns implementation plans and code standards. Writes tooling and specs, not features. Does NOT deploy to production without human review.

## The Authority Gradient

Agents have full authority over analysis and recommendations within their domain. They have limited authority over decisions that cross domain boundaries. They have no authority over irreversible actions (publishing, deploying, sending communications).

This gradient means agents can work autonomously on research and analysis but naturally pause at decision points that affect other agents or the outside world.

## When NOT to Create an Agent

A role should exist only when all of these are true:
1. The work has recurred across 3+ sessions
2. It would benefit from its own persistent memory and perspective
3. The role is specific enough to brief clearly
4. You'd want to review its output regularly

Premature specialisation creates coordination overhead without enough value. One generalist agent that handles three types of work is better than three specialist agents that need constant routing.
