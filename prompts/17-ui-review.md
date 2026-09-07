# Review UI hierarchy and consistency

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs

Read the goal, acceptance criteria, current plan, relevant code, and actual toolchain. Reuse approved decisions; resolve missing design decisions through the shared contract before implementation.

## Task-specific references

- [UI_GUIDELINES](../docs/design/UI_GUIDELINES.md)
- [DESIGN_SYSTEM](../docs/design/DESIGN_SYSTEM.md)
- [VISUAL_REVIEW](../docs/design/VISUAL_REVIEW.md)

## Procedure

1. Confirm the review target and product priorities if missing; reuse a supplied scope and approved visual direction.
2. Inspect actual screens, content, and state variants, separating observations from code-only inferences.
3. Review hierarchy, primary actions, typography, spacing, grouping, semantic color, component consistency, and feedback.
4. Include long content, narrow space, large text, loading, empty, and error states relevant to the task.
5. Report actionable discrepancies with evidence and impact. If corrections are requested, verify them against the same agreed direction and captures.

## Evidence and completion

Screen/state evidence, prioritized UI findings, specific corrections, visual verification, and unverified states.
