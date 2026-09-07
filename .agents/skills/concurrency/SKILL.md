---
name: concurrency
description: "Use to review asynchronous ownership and ordering in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Review asynchronous ownership and ordering

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Inventory operations, owners, lifetimes, timeouts, cancellation, queue bounds, and error propagation.
2. Exercise overlapping inputs, stale responses, account switches, route disposal, and worker shutdown.
3. Choose explicit ordering and duplicate semantics appropriate to the operation; cancellation does not undo an external mutation.
4. Check cross-handler interactions and backpressure rather than assuming one transformer or mounted check protects all state.
5. Verify behavior with controlled delays/failures and measure worker overhead if parallel execution is proposed.

## References to load for this task

- [ASYNC_CONCURRENCY](../../../docs/engineering/ASYNC_CONCURRENCY.md)
- [ISOLATES](../../../docs/engineering/ISOLATES.md)
- [STATE_MANAGEMENT](../../../docs/architecture/STATE_MANAGEMENT.md)
- [Task prompt](../../../prompts/16-concurrency-review.md)

## Completion contract

Ownership map, reproducible interleavings, ordering policy, cleanup and recovery evidence.
