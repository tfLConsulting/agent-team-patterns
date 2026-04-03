---
name: build
description: Structured 6-step execution recipe for non-trivial implementation work. Use when building features, fixing complex bugs, or making multi-file changes. Covers investigate, plan review, execute, implementation review, QA, and close-out. Do NOT use for one-line fixes or single-file changes — just do those directly. Also use when the user says "use the build recipe", "follow the 6-step process", or references the execution recipe.
---

# Build Recipe

A 6-step execution recipe for non-trivial implementation work. Each step runs as a separate subagent with fresh context, preventing the failure mode where 82% of tokens are wasted on post-completion troubleshooting (Judy, InfoQ 2026).

See `references/research-synthesis.md` for the evidence base behind each step.

## When to use this

Use when: multi-file changes, features with edge cases, anything where "just do it" would produce code you'd need to debug.

Skip when: single-file changes you could describe in one sentence, config tweaks, copy changes. Just do those directly.

## Before you start

Read the project's CLAUDE.md (or equivalent setup docs) to understand the codebase conventions, build commands, and project structure. If the project tracks tech debt, scan for relevant items. This gives the subagents the right context from the start.

Choose a **plan location** — for example, `specs/<feature-name>/plan.md` or wherever your project keeps development plans. Create the directory if needed.

## The 6 steps

Run each step as a **separate subagent** (Agent tool, subagent_type: `general-purpose`). Separate context is not optional — it prevents anchoring bias and context pollution.

Between steps, briefly tell the user what happened and what's next. Commit after steps 3 and 5.

---

### Step 1: Investigate

Spin off a subagent to understand the current state and create an implementation plan.

**The subagent prompt must include:**
- The feature/fix description (what and why)
- The project's setup docs path (e.g., CLAUDE.md)
- The plan output path
- Instruction to read existing code BEFORE planning

**What the subagent does:**
1. Read the project's setup docs, relevant specs, and existing patterns
2. Find 2-3 similar implementations in the codebase — these are the patterns to follow, not invent new ones
3. Read ALL files that will be modified (not just the entry points)
4. Create a plan at the designated path with:
   - **Problem statement** — what's wrong or missing, grounded in specifics
   - **Approach** — which existing patterns to follow, with file path references
   - **Phases** — ordered steps, each with exact file paths and the specific change
   - **Tests** — what tests to write, what they verify, test-first where possible
   - **Done when** — concrete acceptance criteria (not "it works")

**What the subagent must NOT do:**
- Write any implementation code
- Invent new patterns when existing ones exist
- Create the plan without reading the codebase first

**Why this matters:** Context blindness — AI not reading existing code — is the root cause of most AI coding failures. This step forces codebase understanding before any planning begins.

---

### Step 2: Review the plan

Spin off a **different subagent** to review the plan. Fresh context is critical — "Claude won't be biased toward code it just wrote" (Anthropic best practices).

**The subagent prompt must include:**
- The plan file path
- The project's setup docs path
- Instruction to read source files independently (don't trust the investigation blindly)

**What the subagent does:**
1. Read the plan from Step 1
2. Read the relevant source files independently
3. Check against this rubric:
   - **Standards alignment** — does it follow the project's conventions and patterns?
   - **Completeness** — are there files, edge cases, or integration points the investigator missed?
   - **Executability** — could a fresh session implement this without ambiguity? Are file paths exact?
   - **Scope** — does the plan add unnecessary complexity? Does it only change what's needed?
   - **Tests** — are test cases specific enough? Do they test behavior, not just compilation?
4. Fix any issues directly in the plan file
5. Add a "Reviewed" line with the date at the top of the plan

**What the subagent must NOT do:**
- Write implementation code
- Approve a plan that's vague about file paths or changes

---

### Step 3: Execute

Spin off a subagent to implement the plan.

**The subagent prompt must include:**
- The plan file path
- The project's build/test/lint commands (from CLAUDE.md or build config)
- Instruction to implement test-first where the plan specifies tests

**What the subagent does:**
1. Read the plan
2. Implement each phase in order, following these rules:
   - **Test-first where specified** — write the failing test, then the implementation. Test behavior, not compilation (a stub that compiles but fails the test is the correct RED state)
   - **One behavior per pass** — don't batch unrelated changes
   - **Follow existing patterns** — if the plan says "follow the pattern in X", read X and match it
   - **Run tests after each phase** — don't accumulate changes without verification
   - **Only implement what the plan says** — no bonus features, no "while I'm here" improvements
3. If anything in the plan doesn't work as written, fix it and note the deviation in the plan
4. Run the project's lint command when done

**What the subagent must NOT do:**
- Deviate from the plan without noting why
- Skip test execution between phases
- Add features not in the plan
- Delete or weaken existing tests to make new code pass

**If the subagent hits a wall (2+ failed attempts at the same thing):** Stop, document what failed and why in the plan, and return. Don't spiral.

---

### Step 4: Review the implementation

Spin off a **different subagent** to review what was built. Again, fresh context.

**The subagent prompt must include:**
- The plan file path
- Instruction to run `git diff` to see exactly what changed
- The project's setup docs path

**What the subagent does:**
1. Read the plan
2. Run `git diff` (or `git diff --cached` if staged) to see all changes
3. Check against this rubric:
   - **Plan fidelity** — does the implementation match the plan? Are deviations justified?
   - **Correctness** — are there bugs, off-by-one errors, missing null checks, race conditions?
   - **Pattern consistency** — does new code match existing patterns in the codebase?
   - **Security** — any hardcoded secrets, injection vectors, XSS, missing auth checks?
   - **Test quality** — do tests actually verify the behavior? Could they pass with a broken implementation?
   - **Scope creep** — was anything changed that wasn't in the plan?
4. Fix any issues found directly in the code
5. If fixes are significant, re-run tests

**What the subagent must NOT do:**
- Rubber-stamp the implementation
- Refactor code outside the scope of the plan
- Add features

---

### Step 5: QA

Spin off a subagent to run all quality checks.

**The subagent prompt must include:**
- The project's test, lint, and type-check commands (as defined in your project's CLAUDE.md or build config)
- What was changed (summary from Step 4)

**What the subagent does:**
1. Run the project's full quality checks. At minimum:
   - Lint (e.g., `eslint`, `ruff`, `cargo clippy`, or your project's lint command)
   - Type checking (e.g., `tsc --noEmit`, `mypy`, or equivalent)
   - Tests (e.g., `pytest`, `vitest`, `cargo test`, or your project's test command)
   - If the project has a combined health-check command, run that instead
2. If tests fail, fix them — but only the failures related to the new code
3. If test coverage is low for the new code and the project has coverage standards, add tests
4. Verify no lint errors, no type errors in the changed files

**What the subagent must NOT do:**
- Fix pre-existing test failures unrelated to the change
- Delete tests to make the suite pass
- Skip any of the checks

---

### Step 6: Close out

Do this in the main conversation (no subagent needed).

1. **Commit** the changes with a descriptive message following the repo's commit style
2. **Update the plan** — mark status as complete with the date
3. **Update development history** — if the project maintains a development history or changelog, add an entry
4. **Note learnings** — if anything surprised you (a pattern that didn't work, a file the plan missed, an edge case discovered during review), note it. If the project tracks tech debt, add relevant items there. Otherwise, mention it to the user.

---

## Parallelism rules

- Steps 1-6 are **strictly sequential** for a single item (each depends on the previous)
- Multiple independent items CAN run in parallel if they touch different files
- When parallelising, each item gets its own complete 1-6 pipeline
- Maximum 3-4 parallel pipelines — more decreases quality
- Items with file dependencies must run sequentially

## Subagent invocation rules

Every subagent prompt must be **specific**. Vague invocations are the primary failure mode.

**Bad:** "Investigate the authentication feature"
**Good:** "Read CLAUDE.md, then investigate the current authentication flow in src/lib/auth.ts and src/api/actions/auth.*.ts. Create an implementation plan at specs/auth-refresh/plan.md for adding token refresh logic. Find 2-3 similar auth patterns in the codebase first."

Every subagent prompt must include:
- Specific file paths to read
- Clear deliverable (what file to create/modify, what check to run)
- The project's setup docs path
- What NOT to do (prevents scope creep)

## Known failure modes

| Failure | Prevention |
|---------|-----------|
| Agent doesn't read existing code | Step 1 mandates codebase analysis before planning |
| Agent declares "done" prematurely | Steps 4+5 verify independently in fresh context |
| Correction spiral (2+ failed fixes) | Step 3 rule: stop after 2 failures, document, return |
| Over-engineering | Plan constrains scope; reviewer checks for extras |
| Tests pass but are wrong | Step 3 mandates behavioral tests, not compilation stubs |
| Code doesn't match existing patterns | Step 1 finds 2-3 similar implementations to follow |
| Reviewer rubber-stamps | Explicit rubric in Steps 2 and 4 |
| Agent deletes tests to pass | Explicit prohibition in Steps 3 and 5 |
| Context pollution across steps | Each step is a separate subagent with fresh context |
