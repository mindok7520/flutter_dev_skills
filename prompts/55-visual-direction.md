# Compare feasible visual directions

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [DESIGN_WORKFLOW](../docs/design/DESIGN_WORKFLOW.md)
- [PRODUCT_DESIGN_BRIEF](../docs/design/PRODUCT_DESIGN_BRIEF.md)
- [DESIGN_TOKENS](../docs/design/DESIGN_TOKENS.md)

## Procedure

1. Verify that the user has answered the brief or explicitly delegated the open design decisions; ask and wait if not.
2. Analyze supplied references by their hierarchy, typography, spacing, imagery, content, and task fit; state when an image could not be inspected.
3. When direction is open, compare two feasible treatments of one representative screen with realistic copy and data.
4. Explain tradeoffs in usability, character, accessibility, motion, implementation effort, and maintainability without forcing a fashionable style.
5. Present the concise alternatives and ask the user to choose before application implementation; reuse a complete approved design when one already exists.
6. Record the selected direction, rejected alternative, shared roles, and approved scope.

## Evidence and completion

Inspectable alternatives, reference interpretation, recommendation, actual user selection, and shared visual decisions.
