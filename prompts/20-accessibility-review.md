# Review accessibility with actual interaction

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

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
