---
name: state-management
description: "Use to choose state management from ownership needs in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Choose state management from ownership needs

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Inventory local presentation state, screen/application state, authoritative domain data, writers, readers, lifetime, and persistence.
2. Inspect the existing solution and its exact version. Compare keeping it with only plausible alternatives such as local state, ChangeNotifier, Riverpod, Cubit, or Bloc.
3. Evaluate dependency scope, asynchronous states, disposal, cache bounds, stale results, event ordering, testing, and migration cost.
4. Choose duplicate/latest/sequential semantics per operation; do not treat local cancellation as undoing remote writes.
5. Record the decision and verify it with representative transitions, late responses, route exit, account switching, and cleanup.
6. Measure rebuild or memory changes before claiming a performance advantage from the chosen tool.

## References to load for this task

- [STATE_MANAGEMENT](../../../docs/architecture/STATE_MANAGEMENT.md)
- [DATA_FLOW](../../../docs/architecture/DATA_FLOW.md)
- [ASYNC_CONCURRENCY](../../../docs/engineering/ASYNC_CONCURRENCY.md)
- [Task prompt](../../../prompts/58-state-management-decision.md)

## Completion contract

State inventory, bounded candidate comparison, decision rationale, lifecycle/event contracts, and verification plan.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
