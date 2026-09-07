# Review asynchronous ownership and ordering

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
