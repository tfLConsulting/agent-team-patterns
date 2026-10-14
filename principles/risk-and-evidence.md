# Controls reduce specific risks

**Principle:** describe what could go wrong, which controls actually address it, and what remains. The existence of a test suite is not evidence that this change was checked.

Separate exposure (what could be affected), control evidence (what ran over which version), and residual uncertainty (what survives). Keep finding significance separate; see [consequences](consequences.md). Categories may help comparison, but avoid subtracting arbitrary test credits from an arbitrary risk score and calling the result a probability.

| Potential failure | Useful control | What can remain |
|---|---|---|
| Parser loses quoted line breaks | Regression fixture from the failure, plus boundary cases | Other consumers may interpret the export differently |
| Shared library changes a contract | Consumer contract/integration checks | Unlisted consumers, old deployed versions |
| Access boundary becomes permissive | Negative permission tests and configuration inspection | Live identity/configuration differences |
| A decision rests on a false premise | Verify original sources and competing explanations | Unobserved conditions or ambiguous evidence |
| Release fails after a correct build | Staging, migration rehearsal, monitored rollout, rollback | Production-only dependencies and irreversible data effects |

Choose tests from plausible failures, not from the lines changed. A useful regression check fails on the original defect. Match broad or irreversible effects with broader verification. A prose change to a decision rule can have more reach than many source files. Path rules can suggest exposure but miss external consumers and indirect policy effects.

Record command/check, artifact or revision, result, environment, and the failure it addresses. Distinguish passed, failed, not run, and not applicable. If the checks, configuration, or diff change, determine which evidence must be renewed. Review of the checking machinery needs care: it cannot establish its own correctness merely by reporting green.

Write residuals concretely: "checked with consumer A; consumer B is untested" is actionable; "medium risk" is not. Decide whether to add a test, narrow scope, stage exposure, prepare rollback, monitor, accept explicitly, or stop. Give unresolved residuals an owner and revisit trigger when further action is needed. Some uncertainty is irreducible at sensible cost. Residual risk and missing knowledge are related but different: not knowing a failure probability does not make the remaining harm small. Describe both without giving uncertainty a false numerical precision.

A bounded accepted residual need not become permanent backlog. A blocked dependency is different: it prevents the contract being met. A failed check is not erased by moving it into the residual paragraph. Human acceptance is a decision about evidence and authority, not a substitute for an available, necessary check. A passed control also needs a defensible detection scope; see [evaluation and calibration](evaluating-the-system.md).

**Tradeoff:** controls cost time and can create false confidence. Evaluate whether they find material failures and whether their alarms are precise enough to be read. Add tests for meaningful failure modes; do not demand new tests for every reversible wording change.
