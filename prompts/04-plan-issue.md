# Plan a bounded issue

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
