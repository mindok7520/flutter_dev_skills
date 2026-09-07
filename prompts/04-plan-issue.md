# Plan a bounded issue

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [ISSUE_WORKFLOW](../docs/workflow/ISSUE_WORKFLOW.md)
- [TEMPLATE](../docs/exec-plans/TEMPLATE.md)

## Procedure

1. Read the issue, actual code, prior decisions, and baseline failures. Determine whether the request is investigation, implementation, or a design decision.
2. Record only necessary steps with concrete files, behavior, validation, dependencies, and recovery actions.
3. Resolve missing design direction with the user before UI implementation; existing approved specifications remain valid within their scope.
4. Size each step so it produces an assessable result. Prefer the simplest complete vertical slice to a broad skeleton of unfinished features.
5. Mark external actions and unavailable environments accurately without adding unnecessary approval ceremonies for already authorized local work.

## Evidence and completion

Execution plan with scope, decisions, step outcomes, checks, recovery paths, and next action.
