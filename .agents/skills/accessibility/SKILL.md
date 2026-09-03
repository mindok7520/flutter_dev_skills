---
name: accessibility
description: "Use to review accessibility with actual interaction in a Flutter app or its reusable development materials. Apply only to relevant user requests and preserve the current task scope."
---

# Review accessibility with actual interaction

Read [AGENTS.md](../../../AGENTS.md), the current request, and the [shared contract](../../../docs/agent/PROMPT_CONTRACT.md). Ask questions and report decisions in Korean; keep reusable execution prose and code comments in English.

## Inputs and scope

Inspect the actual target manifest, dependencies, code, approved decisions, and execution plan. Do not create a Flutter app inside this materials repository. Use the [design workflow](../../../docs/design/DESIGN_WORKFLOW.md) when the work affects UI/UX. Ask the missing user question before a new design, wait for the answer, and reuse an explicit approval already recorded for the same scope.

## Required workflow

1. Identify the target flow, platforms, input methods, and accessibility expectations from the user and product brief.
2. Inspect semantic names/roles/values, contrast, hit regions, keyboard actions, and focus visibility.
3. Complete the important flow with relevant screen readers and keyboard, including errors, dialogs, and focus restoration.
4. Check large text, localized content, reduced motion, non-color cues, and alternatives to precision gestures.
5. Distinguish automated checks, manual observations, and untested conditions; do not convert a partial check into a compliance claim.

## References to load for this task

- [ACCESSIBILITY](../../../docs/design/ACCESSIBILITY.md)
- [ACCESSIBILITY_TESTING](../../../docs/testing/ACCESSIBILITY_TESTING.md)
- [KEYBOARD_MOUSE_TOUCH](../../../docs/design/KEYBOARD_MOUSE_TOUCH.md)
- [Task prompt](../../../prompts/20-accessibility-review.md)

## Completion contract

Criterion-level findings, actual assistive/input evidence, corrections, and the limits of the assessment.

Ground conclusions in actual artifacts and distinguish observed results, assumptions, recommendations, and unavailable environments. Do not claim a screenshot was reviewed when only code or a tool status was inspected. Run meaningful checks for the requested risk, preserve user work, and record decisions and the next action in the relevant plan. Do not introduce unrelated dependencies, external publication, or a larger redesign merely to exercise this skill.
