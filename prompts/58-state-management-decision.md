# Choose state management from ownership needs

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [STATE_MANAGEMENT](../docs/architecture/STATE_MANAGEMENT.md)
- [DATA_FLOW](../docs/architecture/DATA_FLOW.md)
- [ASYNC_CONCURRENCY](../docs/engineering/ASYNC_CONCURRENCY.md)

## Procedure

1. Inventory local presentation state, screen/application state, authoritative domain data, writers, readers, lifetime, and persistence.
2. Inspect the existing solution and its exact version. Compare keeping it with only plausible alternatives such as local state, ChangeNotifier, Riverpod, Cubit, or Bloc.
3. Evaluate dependency scope, asynchronous states, disposal, cache bounds, stale results, event ordering, testing, and migration cost.
4. Choose duplicate/latest/sequential semantics per operation; do not treat local cancellation as undoing remote writes.
5. Record the decision and verify it with representative transitions, late responses, route exit, account switching, and cleanup.
6. Measure rebuild or memory changes before claiming a performance advantage from the chosen tool.

## Evidence and completion

State inventory, bounded candidate comparison, decision rationale, lifecycle/event contracts, and verification plan.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
