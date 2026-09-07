# Review responsive and adaptive UI

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [RESPONSIVE_ADAPTIVE](../docs/design/RESPONSIVE_ADAPTIVE.md)
- [BREAKPOINTS](../docs/design/BREAKPOINTS.md)
- [KEYBOARD_MOUSE_TOUCH](../docs/design/KEYBOARD_MOUSE_TOUCH.md)

## Procedure

1. Confirm target platforms, inputs, representative content, and the approved navigation/layout direction.
2. Inspect actual component constraints and choose content-driven boundary values instead of assuming fixed device categories.
3. Test below/at/above each selected breakpoint, an intermediate width, short height, text enlargement, and keyboard insets.
4. Resize or rotate during editing, loading, selection, and navigation to verify state preservation.
5. Capture layouts and check reading/focus order, reachable actions, and meaningful use of expanded space.

## Evidence and completion

Platform/constraint matrix, boundary behavior, state preservation, captures, and remaining untested environments.
