# Distinguish capability, authority, and policy

**Design consideration:** a tool being available, an account paying for it, a task being selected, and a reviewer accepting an artifact answer different questions. Work crosses these boundaries in code projects and in administration, research, and operations.

Identify the affected resource or information owner, the person entitled to decide, the operator, and the relevant existing authorisation. Do not infer one from another. This is an operational design question; legal ownership and regulatory duties require their own evidence and applicable expertise.

A useful decision record distinguishes recommendation, decision, authorised action, applied action, and observation. Record only distinctions the project needs, but do not collapse them merely to close a task. A draft may be accepted as a draft while a submission remains pending. A human need not approve every result when an existing policy delegates that decision.

## Define delegated decisions and exceptions

State which choices the agent is expected to make, which require another decision maker, and how existing authorisation is recognised. Excessive escalation is a failure alongside acting beyond authority. A useful recommendation includes a reason and an implementable next step; a menu of unresolved options can leave the original work undone. Where the user wants exploration rather than a recommendation, preserve that distinction.

A standing policy can permit execution or disposition with recorded evidence. Choose its scope, exclusions, expiry/review trigger, and stop condition. Acceptance of a policy is different from permission for a worker to change that policy. Decide who can alter priorities, gates, evaluation rubrics, and controls, especially when the alteration would make the current work pass.

## Guidance and enforcement

Written scope guides behavior; access controls and validation can enforce some boundaries. Choose whether an out-of-scope edit is prohibited, permitted with a report, or grounds for review. Do not describe an advisory check as a mechanical gate. Fail-closed and warn-and-proceed policies have different costs; select them for the affected failure.

Distinguish trusted instructions from evidence supplied by websites, documents, tool responses, or other tasks. Retrieved content can inform a decision without acquiring authority to change it. Match tool access and external side effects to the work actually authorised. Keep sensitive evidence appropriately restricted; useful auditability does not require copying it into every record.

**Choices to keep local:** permitted autonomy, human approval points, enforcement mechanisms, cross-owner changes, who can amend rules, and incident escalation. A file-based team boundary or a particular approval ritual is one implementation, not the transferable principle.
