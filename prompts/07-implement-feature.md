# Implement an agreed feature

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [DEVELOPMENT_PRINCIPLES](../docs/engineering/DEVELOPMENT_PRINCIPLES.md)
- [APP_ARCHITECTURE](../docs/architecture/APP_ARCHITECTURE.md)
- [DESIGN_WORKFLOW](../docs/design/DESIGN_WORKFLOW.md)

## Procedure

1. Read the acceptance criteria and current code. Confirm that the requested product and UI decisions have been answered or explicitly delegated.
2. For a new visual direction, ask the missing question and wait; for an already approved complete design, reuse that approval and proceed.
3. Implement one complete flow with existing components and state conventions, including relevant loading, empty, failure, cancellation, and retry behavior.
4. Keep presentation separate from persistent data authority and assign ownership to controllers, subscriptions, requests, and caches.
5. Run the meaningful behavioral checks and inspect actual UI evidence for visible changes. Update the plan and documentation to match delivered behavior.

## Evidence and completion

Implemented behavior, key decisions, changed files, actual test and visual evidence, remaining limits, and next action.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
