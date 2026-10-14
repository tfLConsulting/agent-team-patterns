# Design information for the next decision

**Principle:** preserve enough reliable information to act and learn without making every session read the entire history.

Start with the questions each reader must answer. A worker needs the current contract and dependencies. A reviewer needs the original contract, actual artifact, and underlying evidence. A decision maker needs choices and consequences. A future session needs current state and unresolved triggers. Build retrieval paths for these questions before choosing folders or a database.

| Information | Authority and lifecycle |
|---|---|
| Intent and acceptance contract | Version it before execution; changed scope is explicit |
| Attempts and evidence | Preserve provenance, artifact version, date, limits; retain attempts while recovery, learning, or accountability needs them |
| Decisions and authority | Record who decided what, under which policy, and whether applied |
| Current status | Identify the authority for each fact and reconcile views; it need not be one physical store |
| Sources and claims | Distinguish source, observation, inference, recommendation, and decision |
| Memory and summaries | Routing aids; link to evidence and supersede stale summaries |

Give durable work and attempts stable identifiers. PRs supply IDs, history, comments, review, and diff links, but those functions can be supplied by other stores. Branches supply isolation and revision history; deleted or rebased branches are a poor sole evidence store. Keep accepted records reachable independently of disposable branches.

One application uses progressive context: a small orientation file, current task packet, then referenced evidence on demand. Other tasks benefit from a larger shared context or direct interaction. Assess what was missing, misleading, and useful for each task type; [evaluate the information strategy](evaluating-the-system.md), not just its token count. A summary should say what it covers, when it was checked, and where to verify it. Never turn an agent's confident narrative into stronger evidence merely by copying it into memory.

Adopt incrementally: inventory existing records; choose a canonical home for each question; migrate one active workstream; test a cold start; reconcile contradictory state; archive superseded instructions with a visible status. Record why an old rule changed so it is not rediscovered and reintroduced later.

Keep restricted evidence in an appropriate restricted store; public records get safe references only when those references themselves are safe. For public examples, invent a scenario and re-derive general mechanisms. Removing names from copied operational records does not reliably remove confidential facts or identifying structure. Review the complete diff, including fixtures, output, and untracked files.

Choose retention, redaction, and deletion rules alongside audit needs. Durable does not mean permanent; records can expire while preserving the decision-relevant facts and any required accountability.

**Tradeoff:** duplication can improve retrieval but creates drift. Prefer generated views with provenance. A database can help querying and concurrent writes; a few files can be easier to inspect and maintain. Choose on actual readers, volume, retention, and privacy needs.
