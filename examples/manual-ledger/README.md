# A manual ledger with executable helpers

This example applies the principles to fictional export work. It provides **read-only** validation, dependency-aware selection, and a disposition packet. The project can keep its own execution and review arrangements. Python 3.9+; standard library only. No installation, network, model, PR, database service, or schedule is required.

From the library root:

```sh
python3 examples/manual-ledger/ledger.py check examples/manual-ledger/plan.json
python3 examples/manual-ledger/ledger.py next examples/manual-ledger/plan.json
python3 examples/manual-ledger/ledger.py packet examples/manual-ledger/submitted.json
python3 -m unittest discover -s examples/manual-ledger -p 'test_*.py'
```

The first `next` selects `T-FORMAT`; it does not claim or perform it. `submitted.json` is a separate synthetic later-stage fixture: the first task is accepted and the second submitted. Its packet exposes the finding and residual. `next` on that fixture returns `task: null`: submitted work needs disposition, rather than being silently marked accepted. No real export work or outcome is claimed. `task: null` means only that this selector found no eligible ready task; inspect the packet for submitted, blocked, deferred, or stopped work. It does not mean the project is finished or healthy.

## Use the idea in your project

1. Copy this example to a local experimental directory and replace the fictional workstream and tasks. Run `check` and inspect `next`.
2. Before performing a selected task, preserve its acceptance contract and mark it active in your canonical ledger. The CLI refuses selection while any task is active, requiring manual reconciliation first.
3. Perform the task using your agent or tools. Preserve a new attempt record and actual artifacts. Record checks against a revision/hash, findings, and concrete residuals in an evidence file. Do not overwrite failed-attempt evidence.
4. Update the task to submitted with `result`: `attempt`, `artifact_version`, `contract` path, `evidence` path, `finding`, and `residual`. All artifact paths are relative to the ledger's directory and must resolve inside it.
5. Generate the packet, inspect original evidence, and record an authorised disposition. Acceptance needs a `decision` with `by`, `authority`, `reason`, and matching `artifact_version`. Revision returns to ready with a new attempt next time; keep prior reports in the evidence history. Blocked/deferred work needs `wake`; stopped work needs a decision. A stopped dependency does not satisfy dependents: reconsider them explicitly.
6. Re-select after acceptance. Observe benefit separately from artifact acceptance.

Schema version 1 has `workstreams` (ID → object with outcome) and `tasks` (see JSON fixtures). Tasks require ID, workstream, title, acceptance, positive integer priority, state, and dependencies. States: ready, active, submitted, accepted, blocked, deferred, stopped. Lower priority numbers go first; task ID breaks ties. This is an example ordering policy, not a universal prioritisation model.

## Policies selected by this example

This fixture requires a workstream per task, serial activity, acceptance-gated dependencies, integer priorities, particular state names, and local evidence files. Those are demonstration choices. None is a general requirement of planning, execution, or disposition. An active task may be legitimate in a concurrent project; an available artifact may be enough for a provisional dependent task; restricted external evidence may be the correct store. See [policy choices](../../applications/policy-choices.md).

The packet preserves findings for accepted as well as submitted results: artifact acceptance must not make a significant discovery disappear. It does not track whether a reader received or acted on the finding. A project needing that guarantee must add an attention-delivery record or use another existing channel.

## Deliberate limits

This is not a transaction engine: transitions and history are maintained by the operator and Git. It checks structure, file existence, containment, and decision-version consistency. It cannot verify the truth of evidence, authority, review independence, immutable snapshots, or whether an artifact version is a real hash. In particular, the fictional fixture passes schema validation without proving any work succeeded.

It has no locking, claims, automatic retry, recurring occurrences, execution budget enforcement, model routing, or automated disposition. Use one writer; separate clones are not coordinated. Do not run it over confidential input expecting sanitisation: packets repeat the ledger's content. If a project needs stronger invariants, add them deliberately or choose a transactional store. Keep intent, findings, residuals, and decisions regardless of storage choice.
