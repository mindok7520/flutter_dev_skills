---
name: flutter-development
description: "Use when implementing or changing Flutter widgets, presentation state, asynchronous UI, and platform boundaries. Inspect the target toolchain and preserve agreed design and architecture conventions."
---

# Implement an agreed feature

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Read the acceptance criteria and current code. Confirm that the requested product and UI decisions have been answered or explicitly delegated.
2. For a new visual direction, ask the missing question and wait; for an already approved complete design, reuse that approval and proceed.
3. Implement one complete flow with existing components and state conventions, including relevant loading, empty, failure, cancellation, and retry behavior.
4. Keep presentation separate from persistent data authority and assign ownership to controllers, subscriptions, requests, and caches.
5. Run the meaningful behavioral checks and inspect actual UI evidence for visible changes. Update the plan and documentation to match delivered behavior.

Keep animation controllers and focus in their presentation lifetime. Check semantics, cancellation, route exit, state updates, and actual platform behavior. A successful web build alone does not verify a native interaction.

## References to load for this task

- [DEVELOPMENT_PRINCIPLES](../../../docs/engineering/DEVELOPMENT_PRINCIPLES.md)
- [APP_ARCHITECTURE](../../../docs/architecture/APP_ARCHITECTURE.md)
- [DESIGN_WORKFLOW](../../../docs/design/DESIGN_WORKFLOW.md)
- [Task prompt](../../../prompts/07-implement-feature.md)

## Completion contract

Implemented behavior, key decisions, changed files, actual test and visual evidence, remaining limits, and next action.
