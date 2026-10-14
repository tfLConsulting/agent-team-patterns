# Second pass: omissions and accidental generalisation

Date: 2026-10-14. Requested review of the examples and initial synthesis.
Review method: source comparison and self-review, not independent review.

## Plan and acceptance

Identify important missing considerations and distinguish portable design questions
from local policies. Correct misleading defaults, add contrasting fictional examples,
and keep private reference details out of the public artifacts. Preserve the first
pass's record as history. Verify changed code and local links.

Bounded tasks:

- R-01: Check planning, evaluation, information, authority, and lifecycle coverage.
- R-02: Correct local choices presented as defaults or universal constraints.
- R-03: Demonstrate contrasting applications and fix any example behavior that
  contradicts the principles it is intended to illustrate.

## Findings

The first pass overemphasised recordkeeping and underexplained plan refinement,
review of task quality, information-strategy evaluation, control calibration,
unobtainable evidence, and reopening decisions. Its acceptance/dependency vocabulary
also carried local policies into general guidance.

Corrections and validation will be recorded after implementation. This review does
not establish that the revised method is effective in new repositories.

## Important omissions addressed

| Omission | Why it matters | Correction |
|---|---|---|
| Capture and plan refinement | A reliable executor can keep doing obsolete or low-value work | [Planning and replanning](../principles/planning-and-replanning.md) covers admission, displacement, starvation, and system-maintenance cost |
| Review the task itself | Compliance with a weak brief can still produce the wrong result | Review purpose and acceptance criteria while preserving the original instruction |
| Unobtainable evidence | Endless follow-up tasks disguise decisions made without necessary knowledge | Distinguish uncollected, unaffordable, and currently unestablishable evidence; choose explicit treatment |
| Re-entry and invalidation | Accepted premises can become false without reopening dependent work | Preserve and supersede decisions; propagate changes and route urgent findings |
| Calibration of controls | A plausible review or a green check can miss the relevant failure | [Evaluation](../principles/evaluating-the-system.md) treats detection scope, missed failures, false alarms, and judge agreement separately |
| Information-strategy effectiveness | A shorter instruction set can be cheaper and worse | Assess missing, misleading, useful, and silently protective context by task type |
| Authority over policy changes | A worker can make its work pass by weakening the rules | [Authority and policy](../principles/authority-and-policy.md) separates capability, authorisation, and changing controls |
| Mixed progress dimensions | One state can hide that design is blocked, a partial result is reviewed, or release is pending | [Policy choices](../applications/policy-choices.md) explains independent axes and dependency predicates |

Resource selection now includes context, tools, review, and repair costs rather than
assuming model capability alone determines fit. Retention now considers privacy,
recovery needs, and deletion rather than implying all history should be kept forever.

## Where local choices became too general

| Initial wording/design | What is portable | What remains local |
|---|---|---|
| Start every adoption manually | Establish useful, recoverable behavior before expanding unattended work | Manual, replay, sandbox, existing runner, or automated pilot |
| Workstream-focused records and attention | Group information around a meaningful decision | Stream, standalone fix, service exception, portfolio choice |
| Planning → execution → disposition | Distinguish intent, action, and judgment | Serial phases, overlapping responsibilities, or repeated re-entry |
| Acceptance-gated dependencies | Name the prerequisite actually needed | Accepted artifact, provisional availability, test, release, or authority |
| N counts attempts and includes blockers | Bound execution and report truthfully | Attempts, completions with a cap, elapsed time, tokens, or spending |
| Single canonical location | Know the authority for each fact and reconcile views | One file, multiple stores, or a transactional system |
| Snapshot and ID on every task | Preserve enough identity to reconstruct material work | Inline Git record versus full occurrence/attempt model |
| Retain failed attempts | Do not erase needed recovery/review evidence | Retention duration, selective summaries, restricted storage, deletion |
| Consequence means belief change | Surface decision-relevant significance | Domain harm, reach, timing, reversibility, or belief change dimensions |
| Risk and significance have separate lanes | Ask the two questions without conflating them | Whether either or both gate action, and who receives findings |
| Ledger state names and one active task | Make ownership and readiness legible | Exact state machine, serial execution, concurrency, and local evidence paths |

These were not all absolute claims in the first pass: several had caveats. The
problem was that prompts and executable defaults still made them easy to inherit
without a fresh decision. The revised prose and policy register make that boundary
visible where adoption occurs.

## Example review and disposition

The ledger packet originally omitted findings and residuals once an artifact was
accepted. That contradicted the separation between accepting a change and ensuring
a significant finding reaches its reader. The packet now includes accepted results,
decision attribution, and an explicit statement that finding delivery is not tracked.
A regression test verifies the finding survives acceptance. This does not implement
an attention acknowledgment system or imply that receipt proves understanding.

Three [fictional design cases](../examples/design-cases.md) contrast a small repair,
a direction-changing investigation, and a continuing service check. They expose
choices that the original happy-path ledger did not exercise. They are thought
experiments, not measured outcomes or production-ready implementations.

R-01, R-02, and R-03 have implementation results. Contributor disposition: corrections
ready for reader review under the requested scope; self-review only. No new scheduler,
external action, commit, or publication is part of the work.

## Validation and remaining limits

- 11 helper tests passed, including the new accepted-finding regression.
- The documented packet command shows both accepted and submitted findings.
- 85 local links resolved; changed/added files passed the private-reference scan
  and manual content review. The pre-existing generic path-pattern instruction was
  distinguished from an actual private path. `git diff --check` passed.
- Existing vendor capability notes were not changed or re-researched in this pass.

This remains a qualitative comparison, not an exhaustive design inventory. The
read-only helper still does not demonstrate execution, durable transitions,
reopening a decision, or external side effects end to end. Those needs should guide
future worked implementations if adopters encounter them. No universal workflow or
empirical effectiveness claim follows from these cases.

Next useful evidence: an adoption pilot that includes an awkward case—changed
premise, partial evidence, or mixed authority—not only successful task completion.
