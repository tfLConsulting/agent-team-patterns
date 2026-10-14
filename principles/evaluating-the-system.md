# Evaluate the controls and the context

**Design consideration:** reviews, grades, tests, and instruction files are interventions with failure modes. Their presence does not establish their effectiveness. Evaluation itself needs a budget and a way to detect misleading conclusions.

## Does a control detect the failures that matter?

For each important control, state its target defect class, scope, evidence of detection, false alarms, and known blind spots. A compiler can catch particular contract violations; a green exit does not establish that all relevant behavior was checked. Deterministic execution makes a check reproducible, not complete. An independent reviewer can still share the author's mistaken assumptions.

Use known failures, seeded defects, adversarial cases, independent source checks, or sampled downstream outcomes where practical. Include both failures caught and bad outcomes missed. Agreement between judges measures agreement; it does not provide ground truth. Judge a reviewer partly on missed defects and unnecessary rejection, not the fluency or length of the review.

Version rubrics, prompts, controls, and relevant environment assumptions. A scoring change can move the measured quality without changing the work. Compare on a shared sample before pooling results. If evaluation cannot support the confidence claimed, reduce that claim or limit the policy that relies on it. Requiring a particular calibration score before every use is a local decision, not a universal rule.

## Is the information strategy helping this task?

Measure more than document size. Ask what useful context was available at the right time, what was missing or discovered late, what instructions misled the run, and what irrelevant context consumed time or displaced useful evidence. Include automatically loaded guidance, tool descriptions, inherited history, and retrieval failures when observable. Label estimates and incomplete traces.

An instruction never quoted in a report may still have prevented a mistake. An instruction repeatedly followed may still be wrong. Removal experiments or matched task comparisons can help distinguish unnecessary material from quiet safeguards. Preserve important rare-event protections until there is a justified alternative. Token reduction alone is not success.

Review information by task type and decision: one project's background may be necessary for a planning task and distracting for a bounded parser fix. The right context boundary can be a task, role, workstream, or tool surface. A short root file and on-demand references are one application, not a guarantee of sufficiency.

## Choose resources against actual performance

Compare complete execution configurations: model, effort, context, tools, review, and retries. Model size alone is a poor proxy for fit. For work with non-negotiable correctness or authority constraints, establish those constraints before optimising cost or latency. Other exploratory work may reasonably trade breadth, speed, and precision differently.

Include repair, review, operator attention, and delayed discovery in cost. Use representative tasks, record selection effects, and avoid generalising from a few easy cases. Safe experiments can be sampled gradually; some classes should not be exploration candidates. When no configuration meets the required standard, report that gap rather than redefining success as the best score currently available.

**Tradeoff:** a permanent grading pipeline can cost more than it discovers. Occasional outcome review and a few regression cases may suffice. Choose evaluation intensity from the decisions it supports, not because a sophisticated reference project has a grading stage.
