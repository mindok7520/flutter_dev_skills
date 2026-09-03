# Review UI hierarchy and consistency

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
