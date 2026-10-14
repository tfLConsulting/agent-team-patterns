# Workstream: a design library that another repository can adapt

Follow-up: [the second-pass review](2026-10-design-review.md) corrects omissions and
local choices treated too generally. This file preserves the first pass as recorded.

Date: 2026-10-14. Execution: manual. Review: self-review, not independent review.

## Plan and original acceptance contract

The library should explain planning, bounded execution, workstreams, tasks, and
disposition without prescribing a single framework. Design reasoning should cover
attention, consequences, tests, residuals, information strategy, and runtime choices.
A new repository should get a useful adoption route, examples, and working code.
Preserve useful earlier principles and applications without keeping their operating
model as the default. Keep all public material free of private reference details.
Do not automate this repository.

Chosen scope: establish an initial coherent library, one runnable reference, and
several documented application choices. A complete taxonomy or production queue
engine would cost more than its unproven value. Those are not required for this pass.

## Tasks and execution

| Task | Acceptance evidence | Result |
|---|---|---|
| L-01: Extract design distinctions | Principles explain choices and limits using fresh, generic prose | Six topic guides plus vocabulary and design index |
| L-02: Make adoption practical | A new repo can discover constraints and choose mechanisms | Adoption prompt, four application guides, earlier-pattern reuse map, four templates |
| L-03: Provide working code | Runnable selection, validation, packet generation, meaningful failure checks | Standard-library ledger with fictional fixtures and tests |
| L-04: Align this repo | Manual state, consistent current instructions, visible historical status | AGENTS.md, CLAUDE.md adapter, compatibility entry points, historical notices, this record |

All four bounded tasks have implementation results. This table records execution,
not a claim of user acceptance or downstream adoption.

## Design decisions

- Keep principles separate from applications so a new project can choose its own mechanisms.
- Separate risk remaining after controls from the significance of findings.
- Preserve workstream synthesis above task evidence to concentrate attention.
- Use a read-only helper: it makes mechanical errors visible without pretending to
  execute agents, grant authority, enforce transitions, or provide concurrency safety.
- Preserve earlier material with visible navigation and status rather than deleting
  evidence or treating old practitioner findings as newly verified facts.
- Record vendor capabilities with official links and a check date; install nothing.

## Evidence and self-review

Checks completed on 2026-10-14:

- `python3 -m unittest discover -s examples/manual-ledger -p 'test_*.py'`:
  10 tests passed. Covers dependency acceptance, interruption, malformed state,
  missing evidence, decision-version mismatch, path traversal/symlinks, wake
  conditions, packet content, and read-only CLI behavior.
- Documented `check`, `next`, and `packet` commands succeeded on the fictional
  fixtures. Selection on the submitted fixture returned no ready work.
- 59 relative links in new/current documents resolved. Official vendor pages were
  fetched for the dated capability notes; historical citations were not re-audited.
- `git diff --check` passed. Changed and added text was inspected for private
  identifiers and local paths. A pre-existing literal path-pattern instruction
  was distinguished from an actual disclosure. No private details were found in
  the new material.

These checks establish runnable helper behavior and navigable documentation,
not effectiveness of the method or the truth of arbitrary ledger evidence.
The original baseline is Git revision `39d6ee5`. The proposed artifact is the current
working-tree diff and its added files; no release or publication is claimed.

## Disposition

Contributor assessment: the initial implementation is ready for reader review,
subject to the recorded checks. Authority is the requested repository redesign;
this assessment does not claim the user's approval of the editorial direction.
No commits, pushes, external messages, or schedules are part of this work.

Remaining uncertainty and triggers:

- **Usefulness:** no new repo has piloted adoption. When one does, record cold-start
  friction and whether evidence/disposition can be reconstructed; revise from that evidence.
- **Example strength:** the helper intentionally does not enforce transitions,
  history immutability, authority, or concurrency. If a real adopter needs those,
  design the smallest additional mechanism in that repo rather than expanding this by default.
- **Historical claims:** earlier citations and quantitative assertions were not
  re-audited. Reassess the relevant claim before relying on it in a new application.
- **Vendor drift:** recheck official docs when implementing an adapter; the dated
  capability map is not a promise about every account or runtime.

Next useful action: use the adoption prompt against one new repository and evaluate
whether the principles help it choose a smaller, more appropriate workflow. No
scheduled follow-up is needed.
