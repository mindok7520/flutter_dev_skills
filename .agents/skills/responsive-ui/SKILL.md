---
name: responsive-ui
description: "Use to review responsive and adaptive ui in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Review responsive and adaptive UI

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Confirm target platforms, inputs, representative content, and the approved navigation/layout direction.
2. Inspect actual component constraints and choose content-driven boundary values instead of assuming fixed device categories.
3. Test below/at/above each selected breakpoint, an intermediate width, short height, text enlargement, and keyboard insets.
4. Resize or rotate during editing, loading, selection, and navigation to verify state preservation.
5. Capture layouts and check reading/focus order, reachable actions, and meaningful use of expanded space.

## References to load for this task

- [RESPONSIVE_ADAPTIVE](../../../docs/design/RESPONSIVE_ADAPTIVE.md)
- [BREAKPOINTS](../../../docs/design/BREAKPOINTS.md)
- [KEYBOARD_MOUSE_TOUCH](../../../docs/design/KEYBOARD_MOUSE_TOUCH.md)
- [Task prompt](../../../prompts/19-responsive-review.md)

## Completion contract

Platform/constraint matrix, boundary behavior, state preservation, captures, and remaining untested environments.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
