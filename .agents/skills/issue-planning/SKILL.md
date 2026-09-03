---
name: issue-planning
description: "Use to plan a bounded issue in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Plan a bounded issue

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

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

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
