# Compare feasible visual directions

Use this prompt with the current user request and [AGENTS.md](../AGENTS.md). Apply the [shared execution contract](../docs/agent/PROMPT_CONTRACT.md). Respond and ask questions in Korean unless the user requests another language; keep code and code comments in English.

## Inputs and consultation

Read the actual product definition, relevant code, manifest/lockfile, approved decisions, and current execution plan. Reuse supplied answers and permissions. For UI/UX work, follow the [design workflow](../docs/design/DESIGN_WORKFLOW.md): ask about missing goals and constraints before new design work, wait for the answer, and establish the direction before application implementation. Do not invent approval or repeat it inside an already approved scope.

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

Tie conclusions to actual files, user decisions, observed behavior, or raw measurements. Distinguish facts, assumptions, recommendations, failed checks, and unavailable environments. Select checks that detect the relevant failure rather than duplicating implementation or inflating test counts. For a review-only request, report findings without making unrequested application changes. For authorized implementation, complete the correction and its relevant verification, then update the decision record or execution plan.
