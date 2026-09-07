---
name: issue-planning
description: "Use to plan a bounded issue in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Plan a bounded issue

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Read the goal, acceptance criteria, current plan, actual toolchain, and relevant code. Apply the shared contract for scope, design decisions, safety, and evidence. Load the references below only when needed; the task prompt is an alternative entry point.

## Required workflow

1. Read the issue, actual code, prior decisions, and baseline failures. Determine whether the request is investigation, implementation, or a design decision.
2. Record only necessary steps with concrete files, behavior, validation, dependencies, and recovery actions.
3. Resolve missing design direction with the user before UI implementation; existing approved specifications remain valid within their scope.
4. Size each step so it produces an assessable result. Prefer the simplest complete vertical slice to a broad skeleton of unfinished features.
5. Mark external actions and unavailable environments accurately without adding unnecessary approval ceremonies for already authorized local work.

## References to load for this task

- [ISSUE_WORKFLOW](../../../docs/workflow/ISSUE_WORKFLOW.md)
- [TEMPLATE](../../../docs/exec-plans/TEMPLATE.md)
- [Task prompt](../../../prompts/04-plan-issue.md)

## Completion contract

Execution plan with scope, decisions, step outcomes, checks, recovery paths, and next action.
