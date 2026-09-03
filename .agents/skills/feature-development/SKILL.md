---
name: feature-development
description: "Use to implement an agreed feature in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Implement an agreed feature

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Read the acceptance criteria and current code. Confirm that the requested product and UI decisions have been answered or explicitly delegated.
2. For a new visual direction, ask the missing question and wait; for an already approved complete design, reuse that approval and proceed.
3. Implement one complete flow with existing components and state conventions, including relevant loading, empty, failure, cancellation, and retry behavior.
4. Keep presentation separate from persistent data authority and assign ownership to controllers, subscriptions, requests, and caches.
5. Run the meaningful behavioral checks and inspect actual UI evidence for visible changes. Update the plan and documentation to match delivered behavior.

## References to load for this task

- [DEVELOPMENT_PRINCIPLES](../../../docs/engineering/DEVELOPMENT_PRINCIPLES.md)
- [APP_ARCHITECTURE](../../../docs/architecture/APP_ARCHITECTURE.md)
- [DESIGN_WORKFLOW](../../../docs/design/DESIGN_WORKFLOW.md)
- [Task prompt](../../../prompts/07-implement-feature.md)

## Completion contract

Implemented behavior, key decisions, changed files, actual test and visual evidence, remaining limits, and next action.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
