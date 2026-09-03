# Review accessibility with actual interaction

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

## Task-specific references

- [ACCESSIBILITY](../docs/design/ACCESSIBILITY.md)
- [ACCESSIBILITY_TESTING](../docs/testing/ACCESSIBILITY_TESTING.md)
- [KEYBOARD_MOUSE_TOUCH](../docs/design/KEYBOARD_MOUSE_TOUCH.md)

## Procedure

1. Identify the target flow, platforms, input methods, and accessibility expectations from the user and product brief.
2. Inspect semantic names/roles/values, contrast, hit regions, keyboard actions, and focus visibility.
3. Complete the important flow with relevant screen readers and keyboard, including errors, dialogs, and focus restoration.
4. Check large text, localized content, reduced motion, non-color cues, and alternatives to precision gestures.
5. Distinguish automated checks, manual observations, and untested conditions; do not convert a partial check into a compliance claim.

## Evidence and completion

Criterion-level findings, actual assistive/input evidence, corrections, and the limits of the assessment.

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
