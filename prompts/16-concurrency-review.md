# Review asynchronous ownership and ordering

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [ASYNC_CONCURRENCY](../docs/engineering/ASYNC_CONCURRENCY.md)
- [ISOLATES](../docs/engineering/ISOLATES.md)
- [STATE_MANAGEMENT](../docs/architecture/STATE_MANAGEMENT.md)

## Procedure

1. Inventory operations, owners, lifetimes, timeouts, cancellation, queue bounds, and error propagation.
2. Exercise overlapping inputs, stale responses, account switches, route disposal, and worker shutdown.
3. Choose explicit ordering and duplicate semantics appropriate to the operation; cancellation does not undo an external mutation.
4. Check cross-handler interactions and backpressure rather than assuming one transformer or mounted check protects all state.
5. Verify behavior with controlled delays/failures and measure worker overhead if parallel execution is proposed.

## Evidence and completion

Ownership map, reproducible interleavings, ordering policy, cleanup and recovery evidence.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
